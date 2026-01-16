import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import api from "../services/api";

const SpeciesList = () => {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const response = await api.get("categories/");
        setCategories(response.data.results || response.data);
      } catch (error) {
        console.error("Error fetching categories:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchCategories();
  }, []);

  if (loading)
    return (
      <div style={{ textAlign: "center", marginTop: "50px" }}>
        Chargement des espèces...
      </div>
    );

  return (
    <div>
      <header style={{ padding: "40px 0", textAlign: "center" }}>
        <h1 style={{ color: "var(--primary-color)", fontSize: "2.5rem" }}>
          Classification par Espèces
        </h1>
        <p>Explorez la biodiversité rangée par familles.</p>
      </header>

      {categories.map((category) => (
        <section
          key={category.id}
          style={{
            marginBottom: "60px",
            background: "white",
            padding: "30px",
            borderRadius: "12px",
            boxShadow: "var(--shadow)",
          }}
        >
          <h2
            style={{
              color: "var(--primary-color)",
              borderBottom: "2px solid #eee",
              paddingBottom: "10px",
            }}
          >
            {category.nom} ({category.creatures.length})
          </h2>
          <p
            style={{ color: "#666", fontStyle: "italic", marginBottom: "20px" }}
          >
            {category.description}
          </p>

          <div
            className="card-grid"
            style={{
              gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))",
            }}
          >
            {category.creatures.map((creature) => (
              <Link
                key={creature.id}
                to={`/creature/${creature.id}`}
                className="card"
              >
                <div className="card-image" style={{ height: "150px" }}>
                  {creature.image ? (
                    <img
                      src={creature.image}
                      alt={creature.nom_commun}
                      style={{
                        width: "100%",
                        height: "100%",
                        objectFit: "cover",
                      }}
                    />
                  ) : (
                    <div
                      style={{
                        width: "100%",
                        height: "100%",
                        display: "flex",
                        alignItems: "center",
                        justifyContent: "center",
                        color: "#999",
                      }}
                    >
                      Pas d'image
                    </div>
                  )}
                </div>
                <div className="card-content" style={{ padding: "10px" }}>
                  <h4
                    className="card-title"
                    style={{ fontSize: "1rem", marginBottom: "5px" }}
                  >
                    {creature.nom_commun}
                  </h4>
                  <div className="card-meta" style={{ fontSize: "0.8rem" }}>
                    {creature.nom_scientifique}
                  </div>
                </div>
              </Link>
            ))}
            {category.creatures.length === 0 && (
              <div style={{ color: "#999", fontStyle: "italic" }}>
                Aucune créature répertoriée dans cette catégorie pour le moment.
              </div>
            )}
          </div>
        </section>
      ))}
    </div>
  );
};

export default SpeciesList;
