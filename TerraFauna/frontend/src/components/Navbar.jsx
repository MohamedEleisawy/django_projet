import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="container">
        <Link to="/" className="navbar-brand">
          🌿 TerraFauna
        </Link>
        <div className="navbar-links">
          <Link to="/" className="nav-link">
            Encyclopédie
          </Link>
          <Link to="/especes" className="nav-link">
            Par Espèces
          </Link>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
