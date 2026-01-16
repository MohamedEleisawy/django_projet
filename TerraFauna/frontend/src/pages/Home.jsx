import { useState, useEffect } from "react";
import { Link, useSearchParams } from "react-router-dom";
import api from "../services/api";

const Home = () => {
  const [creatures, setCreatures] = useState([]);
  const [loading, setLoading] = useState(true);
  const [nextPage, setNextPage] = useState(null);
  const [prevPage, setPrevPage] = useState(null);
  const [page, setPage] = useState(1);

  const [searchParams] = useSearchParams();
  const ecosystemId = searchParams.get("ecosystem");

  useEffect(() => {
    setPage(1); // Reset to page 1 when filter changes
  }, [ecosystemId]);

  useEffect(() => {
    fetchCreatures(page, ecosystemId);
  }, [page, ecosystemId]);

  const fetchCreatures = async (pageNumber, ecosystem) => {
    setLoading(true);
    try {
      let url = `creatures/?page=${pageNumber}`;
      if (ecosystem) {
        url += `&ecosystemes=${ecosystem}`;
      }
      const response = await api.get(url);
      setCreatures(response.data.results);
      setNextPage(response.data.next);
      setPrevPage(response.data.previous);
    } catch (error) {
      console.error("Error fetching creatures:", error);
    } finally {
      setLoading(false);
    }
  };

  if (loading)
    return (
      <div style={{ textAlign: "center", marginTop: "50px" }}>
        Chargement de la biodiversité...
      </div>
    );

  return (
    <div>
      <header style={{ padding: "40px 0", textAlign: "center" }}>
        <h1 style={{ color: "var(--primary-color)", fontSize: "2.5rem" }}>
          Exploration de la Faune
        </h1>
        <p>Découvrez les espèces fascinantes de notre monde.</p>
      </header>

      <div className="card-grid">
        {creatures.map((creature) => (
          <Link
            key={creature.id}
            to={`/creature/${creature.id}`}
            className="card"
          >
            <div
              className="card-image"
              style={{
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                color: "#666",
              }}
            >
              {creature.image ? (
                <img
                  src={creature.image}
                  alt={creature.nom_commun}
                  style={{ width: "100%", height: "100%", objectFit: "cover" }}
                />
              ) : (
                <span>Pas d'image</span>
              )}
            </div>
            <div className="card-content">
              <h3 className="card-title">{creature.nom_commun}</h3>
              <div className="card-meta">🔬 {creature.nom_scientifique}</div>
              <div className="card-meta">📍 {creature.categorie?.nom}</div>
              <span
                style={{
                  display: "inline-block",
                  padding: "2px 8px",
                  borderRadius: "12px",
                  fontSize: "0.8rem",
                  background: "#eee",
                  marginTop: "8px",
                  fontWeight: "500",
                }}
              >
                {creature.statut_conservation_display}
              </span>
            </div>
          </Link>
        ))}
      </div>

      <div className="pagination">
        <button
          className="btn"
          disabled={!prevPage}
          onClick={() => setPage((p) => p - 1)}
        >
          &larr; Précédent
        </button>
        <span style={{ alignSelf: "center" }}>Page {page}</span>
        <button
          className="btn"
          disabled={!nextPage}
          onClick={() => setPage((p) => p + 1)}
        >
          Suivant &rarr;
        </button>
      </div>
    </div>
  );
};

export default Home;
