import { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import api from "../services/api";

const CreatureDetail = () => {
  const { id } = useParams();
  const [creature, setCreature] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchCreature = async () => {
      try {
        const response = await api.get(`creatures/${id}/`);
        setCreature(response.data);
      } catch (error) {
        console.error("Error fetching creature:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchCreature();
  }, [id]);

  if (loading) return <div>Chargement...</div>;
  if (!creature) return <div>Créature introuvable.</div>;

  return (
    <div
      style={{
        marginTop: "40px",
        background: "white",
        padding: "40px",
        borderRadius: "12px",
        boxShadow: "var(--shadow)",
      }}
    >
      <Link
        to="/"
        style={{ color: "var(--primary-color)", textDecoration: "none" }}
      >
        &larr; Retour à l'encyclopédie
      </Link>

      <div
        style={{
          display: "flex",
          gap: "40px",
          marginTop: "20px",
          flexWrap: "wrap",
        }}
      >
        <div style={{ flex: "1", minWidth: "300px" }}>
          <div
            style={{
              width: "100%",
              height: "400px",
              backgroundColor: "#e0e0e0",
              borderRadius: "8px",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
            }}
          >
            {creature.image ? (
              <img
                src={creature.image}
                alt={creature.nom_commun}
                style={{
                  width: "100%",
                  height: "100%",
                  objectFit: "cover",
                  borderRadius: "8px",
                }}
              />
            ) : (
              "Pas d'image"
            )}
          </div>
        </div>

        <div style={{ flex: "2", minWidth: "300px" }}>
          <h1 style={{ color: "var(--primary-color)", marginBottom: "5px" }}>
            {creature.nom_commun}
          </h1>
          <h3 style={{ fontStyle: "italic", color: "#666", marginTop: "0" }}>
            {creature.nom_scientifique}
          </h3>

          <div
            style={{
              display: "grid",
              gridTemplateColumns: "repeat(auto-fit, minmax(150px, 1fr))",
              gap: "20px",
              margin: "30px 0",
              background: "#f9f9f9",
              padding: "20px",
              borderRadius: "8px",
            }}
          >
            <div>
              <strong>Poids</strong>
              <br />
              {creature.poids} kg
            </div>
            <div>
              <strong>Taille</strong>
              <br />
              {creature.taille} m
            </div>
            <div>
              <strong>Espérance de vie</strong>
              <br />
              {creature.esperance_vie} ans
            </div>
            <div>
              <strong>Status UICN</strong>
              <br />
              <span
                style={{
                  color:
                    creature.statut_conservation === "LC" ? "green" : "orange",
                  fontWeight: "bold",
                }}
              >
                {creature.statut_conservation_display}
              </span>
            </div>
          </div>

          <h3>Description</h3>
          <p style={{ lineHeight: "1.6" }}>{creature.description}</p>

          <h3>Ecosystèmes & Habitats</h3>
          <div style={{ display: "flex", gap: "10px", flexWrap: "wrap" }}>
            {creature.ecosystemes &&
              creature.ecosystemes.map((eco) => (
                <Link
                  key={eco.id}
                  to={`/?ecosystem=${eco.id}`}
                  style={{ textDecoration: "none" }}
                >
                  <span
                    style={{
                      padding: "6px 12px",
                      background: "var(--secondary-color)",
                      color: "white",
                      borderRadius: "20px",
                      fontSize: "0.9rem",
                      display: "inline-block",
                    }}
                  >
                    🌿 {eco.nom}
                  </span>
                </Link>
              ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default CreatureDetail;
