from django.contrib import admin
from .models import Categorie, Ecosysteme, Creature

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'description')

@admin.register(Ecosysteme)
class EcosystemeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'localisation')

@admin.register(Creature)
class CreatureAdmin(admin.ModelAdmin):
    list_display = ('nom_commun', 'nom_scientifique', 'categorie', 'statut_conservation', 'date_decouverte')
    list_filter = ('categorie', 'statut_conservation', 'ecosystemes')
    search_fields = ('nom_commun', 'nom_scientifique', 'description')
    
    actions = ['export_pdf']
    
    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        my_urls = [
            path('stats/', self.admin_site.admin_view(self.stats_view), name='creature-stats'),
        ]
        return my_urls + urls

    def stats_view(self, request):
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import io
        import base64
        from django.shortcuts import render
        from django.db.models import Count

        # Prepare data
        status_counts = Creature.objects.values('statut_conservation').annotate(total=Count('statut_conservation'))
        # Using dict() on choices to get labels directly
        status_dict = dict(Creature.STATUT_CONSERVATION_CHOICES)
        labels = [status_dict.get(item['statut_conservation'], item['statut_conservation']) for item in status_counts]
        sizes = [item['total'] for item in status_counts]

        # Generate Chart
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(labels, sizes, color='skyblue')
        ax.set_xlabel('Statut de Conservation')
        ax.set_ylabel('Nombre de Créatures')
        ax.set_title('Répartition des Espèces par Statut')
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()

        # Save to buffer
        buffer = io.BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        graphic = base64.b64encode(image_png).decode('utf-8')

        context = dict(
            self.admin_site.each_context(request),
            graphic=graphic,
            title="Statistiques de la Biodiversité",
        )
        return render(request, "admin/creature_stats.html", context)

    def export_pdf(self, request, queryset):
        import io
        from django.http import FileResponse
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        from reportlab.lib.units import inch

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter)
        
        for creature in queryset:
            y = 10 * inch
            p.setFont("Helvetica-Bold", 16)
            p.drawString(1 * inch, y, f"Fiche d'Identite: {creature.nom_commun}")
            y -= 0.5 * inch
            
            p.setFont("Helvetica", 12)
            p.drawString(1 * inch, y, f"Nom Scientifique: {creature.nom_scientifique}")
            y -= 0.3 * inch
            p.drawString(1 * inch, y, f"Categorie: {creature.categorie.nom}")
            y -= 0.3 * inch
            p.drawString(1 * inch, y, f"Statut: {creature.get_statut_conservation_display()}")
            y -= 0.3 * inch
            p.drawString(1 * inch, y, f"Esperance de vie: {creature.esperance_vie} ans")
            y -= 0.3 * inch
            p.drawString(1 * inch, y, f"Poids: {creature.poids} kg")
            y -= 0.3 * inch
            p.drawString(1 * inch, y, f"Taille: {creature.taille} m")
            y -= 0.5 * inch
            
            p.drawString(1 * inch, y, "Description:")
            y -= 0.2 * inch
            
            text = p.beginText(1 * inch, y)
            text.setFont("Helvetica", 10)
            description_lines = creature.description.split('\n')
            for line in description_lines:
                text.textLine(line)
            p.drawText(text)
            
            p.showPage()
            
        p.save()
        buffer.seek(0)
        return FileResponse(buffer, as_attachment=True, filename='rapport_creatures.pdf')
    export_pdf.short_description = "Exporter Fiche PDF"
