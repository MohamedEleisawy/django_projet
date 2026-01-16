import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import CreatureDetail from "./pages/CreatureDetail";
import SpeciesList from "./pages/SpeciesList";

function App() {
  return (
    <Router>
      <div className="app">
        <Navbar />
        <main className="container">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/creature/:id" element={<CreatureDetail />} />
            <Route path="/especes" element={<SpeciesList />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
