import { useState, useMemo } from 'react';
import type { Exercise } from '../types';
import { useExercises } from '../hooks/useExercises';
import { useApp } from '../contexts/AppContext';
import { zh, en } from '../i18n';
import ExerciseCard from '../components/ExerciseCard';
import ExerciseDetail from '../components/ExerciseDetail';

export default function FavoritesPage() {
  const { exercises } = useExercises();
  const { favorites, toggleFavorite } = useApp();
  const { lang } = useApp();
  const t = lang === 'zh' ? zh : en;
  const [selected, setSelected] = useState<Exercise | null>(null);

  const favExercises = useMemo(() =>
    exercises.filter((ex: Exercise) => favorites.includes(ex.id)),
    [exercises, favorites]
  );

  return (
    <div style={{ maxWidth: 1400, margin: '0 auto', padding: '24px' }}>
      <h1 style={s.title}>{t.favorites.title} ({favExercises.length})</h1>
      {favExercises.length === 0 ? (
        <div style={s.empty}>{t.favorites.empty}</div>
      ) : (
        <div style={s.grid}>
          {favExercises.map(ex => (
            <div key={ex.id} style={s.cardWrap}>
              <ExerciseCard exercise={ex} onClick={() => setSelected(ex)} />
              <button style={s.removeBtn} onClick={() => toggleFavorite(ex.id)}>
                {t.favorites.remove}
              </button>
            </div>
          ))}
        </div>
      )}
      {selected && <ExerciseDetail exercise={selected} onClose={() => setSelected(null)} />}
    </div>
  );
}

const s: Record<string, React.CSSProperties> = {
  title: { color: '#fff', fontSize: 28, fontWeight: 700, margin: '0 0 24px' },
  grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(220, 1fr))', gap: 20 },
  cardWrap: { display: 'flex', flexDirection: 'column', gap: 8 },
  removeBtn: { background: 'rgba(255,80,80,0.1)', border: '1px solid rgba(255,80,80,0.2)', color: '#ff6b6b', padding: '6px 12px', borderRadius: 8, fontSize: 12, cursor: 'pointer', alignSelf: 'stretch' },
  empty: { color: 'rgba(255,255,255,0.4)', textAlign: 'center', padding: '80px 0', fontSize: 16 },
};
