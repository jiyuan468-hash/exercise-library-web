import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AppProvider } from './contexts/AppContext';
import Header from './components/Header';
import HomePage from './pages/HomePage';
import FavoritesPage from './pages/FavoritesPage';
import PlansPage from './pages/PlansPage';

export default function App() {
  return (
    <AppProvider>
      <Router>
        <div style={s.root}>
          <Header />
          <main style={s.main}>
            <Routes>
              <Route path="/" element={<HomePage />} />
              <Route path="/favorites" element={<FavoritesPage />} />
              <Route path="/plans" element={<PlansPage />} />
            </Routes>
          </main>
          <footer style={s.footer}>
            <span>Data from <a href="https://github.com/hasaneyldrm/exercises-dataset" target="_blank" rel="noreferrer">exercises-dataset</a> \u00b7 Media \u00a9 Gym visual</span>
          </footer>
        </div>
      </Router>
    </AppProvider>
  );
}

const s: Record<string, React.CSSProperties> = {
  root: { minHeight: '100vh', background: 'linear-gradient(180deg, #0f0f1a 0%, #1a1a2e 50%, #16213e 100%)', color: '#fff', fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif' },
  main: { minHeight: 'calc(100vh - 64px - 60px)' },
  footer: { padding: '20px 24px', textAlign: 'center', color: 'rgba(255,255,255,0.3)', fontSize: 12, borderTop: '1px solid rgba(255,255,255,0.05)' },
};
