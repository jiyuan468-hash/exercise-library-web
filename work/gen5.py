import os
base = r'C:\Users\Administrator\Documents\Codex\2026-09-07\https-github-com-hasaneyldrm-exercises-dataset\web-app'
src = os.path.join(base, 'src')

# Header.tsx
code = """import { useApp } from '../contexts/AppContext';
import { useNavigate, useLocation } from 'react-router-dom';
import { zh, en } from '../i18n';

export default function Header() {
  const { lang, setLang } = useApp();
  const navigate = useNavigate();
  const location = useLocation();
  const t = lang === 'zh' ? zh : en;
  const navItems = [
    { path: '/', label: t.nav.home },
    { path: '/favorites', label: t.nav.favorites },
    { path: '/plans', label: t.nav.plans },
  ];
  return (
    <header style={s.header}>
      <div style={s.inner}>
        <div style={s.logo} onClick={() => navigate('/')}>
          <span style={s.icon}>\\ud83d\\udcaa</span>
          <span style={s.title}>{t.app.title}</span>
        </div>
        <nav style={s.nav}>
          {navItems.map(item => (
            <button key={item.path} onClick={() => navigate(item.path)}
              style={{ ...s.navBtn, ...(location.pathname === item.path ? s.navBtnActive : {}) }}>
              {item.label}
            </button>
          ))}
        </nav>
        <button onClick={() => setLang(lang === 'zh' ? 'en' : 'zh')} style={s.langBtn}>
          {t.lang[lang]}
        </button>
      </div>
    </header>
  );
}

const s: Record<string, React.CSSProperties> = {
  header: { background: 'linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)', padding: '0 24px', position: 'sticky', top: 0, zIndex: 100, borderBottom: '1px solid rgba(255,255,255,0.08)' },
  inner: { maxWidth: 1400, margin: '0 auto', display: 'flex', alignItems: 'center', height: 64, gap: 32 },
  logo: { display: 'flex', alignItems: 'center', gap: 10, cursor: 'pointer', flexShrink: 0 },
  icon: { fontSize: 28 },
  title: { color: '#fff', fontSize: 20, fontWeight: 700 },
  nav: { display: 'flex', gap: 4, flex: 1 },
  navBtn: { background: 'transparent', border: 'none', color: 'rgba(255,255,255,0.6)', fontSize: 15, fontWeight: 500, padding: '8px 16px', borderRadius: 8, cursor: 'pointer' },
  navBtnActive: { color: '#fff', background: 'rgba(255,255,255,0.1)' },
  langBtn: { background: 'rgba(255,255,255,0.1)', border: '1px solid rgba(255,255,255,0.2)', color: '#fff', fontSize: 14, fontWeight: 600, padding: '6px 14px', borderRadius: 8, cursor: 'pointer', flexShrink: 0 },
};
"""
with open(os.path.join(src, 'components', 'Header.tsx'), 'w', encoding='utf-8') as f:
    f.write(code)
print('Header done')
