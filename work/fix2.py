import os

base = r'C:\Users\Administrator\Documents\Codex\2026-09-07\https-github-com-hasaneyldrm-exercises-dataset\web-app'
src = os.path.join(base, 'src')

# ComparePanel.tsx
with open(os.path.join(src, 'components', 'ComparePanel.tsx'), 'w', encoding='utf-8') as f:
    f.write("""import type { Exercise } from '../types';

interface Props {
  exercises: Exercise[];
  onClose: () => void;
  onRemove: (id: string) => void;
}

export default function ComparePanel({ exercises, onClose, onRemove }: Props) {
  const fields = ['name', 'body_part', 'equipment', 'target', 'muscle_group', 'secondary_muscles'] as const;
  const labels: Record<string, string> = {
    name: 'Name', body_part: 'Body Part', equipment: 'Equipment',
    target: 'Target', muscle_group: 'Muscle Group', secondary_muscles: 'Secondary'
  };
  return (
    <div style={s.overlay} onClick={onClose}>
      <div style={s.panel} onClick={e => e.stopPropagation()}>
        <button style={s.close} onClick={onClose}>X</button>
        <h3 style={s.title}>Compare Exercises</h3>
        <div style={s.tableWrap}>
          <table style={s.table}>
            <thead>
              <tr>
                <th style={s.th}>Field</th>
                {exercises.map(ex => (
                  <th key={ex.id} style={s.th}>
                    <div style={s.thContent}>
                      <span>{ex.name}</span>
                      <button style={s.removeBtn} onClick={() => onRemove(ex.id)}>X</button>
                    </div>
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              {fields.map(f => (
                <tr key={f}>
                  <td style={s.td}>{labels[f] || f}</td>
                  {exercises.map(ex => (
                    <td key={ex.id} style={s.td}>
                      {Array.isArray(ex[f as keyof Exercise])
                        ? (ex[f as keyof Exercise] as string[]).join(', ')
                        : String(ex[f as keyof Exercise] || '')}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

const s: Record<string, React.CSSProperties> = {
  overlay: { position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.7)', zIndex: 300, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: 20 },
  panel: { background: 'linear-gradient(180deg, #1a1a2e, #16213e)', borderRadius: 20, maxWidth: 700, width: '100%', maxHeight: '85vh', overflow: 'auto', position: 'relative', border: '1px solid rgba(255,255,255,0.1)' },
  close: { position: 'absolute', top: 16, right: 16, background: 'rgba(255,255,255,0.1)', border: 'none', borderRadius: '50%', width: 32, height: 32, color: '#fff', fontSize: 16, cursor: 'pointer' },
  title: { color: '#fff', fontSize: 18, fontWeight: 700, margin: '0', padding: '20px 24px 16px', borderBottom: '1px solid rgba(255,255,255,0.08)' },
  tableWrap: { padding: '16px 24px 24px', overflowX: 'auto' },
  table: { width: '100%', borderCollapse: 'collapse' },
  th: { textAlign: 'left', padding: '10px 12px', borderBottom: '1px solid rgba(255,255,255,0.08)', color: 'rgba(255,255,255,0.5)', fontSize: 12, fontWeight: 600, textTransform: 'uppercase' },
  thContent: { display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 8 },
  td: { padding: '12px', borderBottom: '1px solid rgba(255,255,255,0.04)', color: 'rgba(255,255,255,0.8)', fontSize: 14, verticalAlign: 'top' },
  removeBtn: { background: 'none', border: 'none', color: 'rgba(255,255,255,0.4)', cursor: 'pointer', fontSize: 14, padding: 0 },
};
""")
print('ComparePanel done')

# AppContext.tsx - fix ReactNode import
with open(os.path.join(src, 'contexts', 'AppContext.tsx'), 'w', encoding='utf-8') as f:
    f.write("""import { createContext, useContext } from 'react';
import type { ReactNode, Language, WorkoutPlan } from '../types';
import { useLocalStorage } from '../hooks/useLocalStorage';

interface AppContextType {
  lang: Language;
  setLang: (l: Language) => void;
  favorites: string[];
  toggleFavorite: (id: string) => void;
  isFavorite: (id: string) => boolean;
  plans: WorkoutPlan[];
  addPlan: (plan: WorkoutPlan) => void;
  updatePlan: (plan: WorkoutPlan) => void;
  deletePlan: (id: string) => void;
}

const AppContext = createContext<AppContextType | null>(null);

export function AppProvider({ children }: { children: ReactNode }) {
  const [lang, setLang] = useLocalStorage<Language>('app_lang', 'zh');
  const [favorites, setFavorites] = useLocalStorage<string[]>('app_favorites', []);
  const [plans, setPlans] = useLocalStorage<WorkoutPlan[]>('app_plans', []);
  const toggleFavorite = (id: string) =>
    setFavorites(prev => prev.includes(id) ? prev.filter(f => f !== id) : [...prev, id]);
  const isFavorite = (id: string) => favorites.includes(id);
  const addPlan = (plan: WorkoutPlan) => setPlans(prev => [...prev, plan]);
  const updatePlan = (plan: WorkoutPlan) => setPlans(prev => prev.map(p => p.id === plan.id ? plan : p));
  const deletePlan = (id: string) => setPlans(prev => prev.filter(p => p.id !== id));
  return (
    <AppContext.Provider value={{ lang, setLang, favorites, toggleFavorite, isFavorite, plans, addPlan, updatePlan, deletePlan }}>
      {children}
    </AppContext.Provider>
  );
}

export function useApp() {
  const ctx = useContext(AppContext);
  if (!ctx) throw new Error('useApp must be within AppProvider');
  return ctx;
}
""")
print('AppContext done')
