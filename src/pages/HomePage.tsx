import { useState, useMemo } from 'react';
import { useExercises } from '../hooks/useExercises';
import { useApp } from '../contexts/AppContext';
import { zh, en } from '../i18n';
import type { Exercise, Filters } from '../types';
import ExerciseCard from '../components/ExerciseCard';
import ExerciseDetail from '../components/ExerciseDetail';
import SearchAndFilter from '../components/SearchAndFilter';
import ComparePanel from '../components/ComparePanel';

export default function HomePage() {
  const { exercises, loading, error } = useExercises();
  const { lang } = useApp();
  const t = lang === 'zh' ? zh : en;
  const [filters, setFilters] = useState<Filters>({ search: '', bodyPart: '', equipment: '', target: '' });
  const [selected, setSelected] = useState<Exercise | null>(null);
  const [compareList, setCompareList] = useState<Exercise[]>([]);

  const filtered = useMemo(() => {
    return exercises.filter((ex: Exercise) => {
      if (filters.search && !ex.name.toLowerCase().includes(filters.search.toLowerCase())) return false;
      if (filters.bodyPart && ex.body_part !== filters.bodyPart) return false;
      if (filters.equipment && ex.equipment !== filters.equipment) return false;
      if (filters.target && ex.target !== filters.target) return false;
      return true;
    });
  }, [exercises, filters]);

  const handleCompare = (ex: Exercise) => {
    setCompareList(prev => {
      if (prev.includes(ex)) return prev.filter((e: Exercise) => e.id !== ex.id);
      if (prev.length >= 2) return [prev[1], ex];
      return [...prev, ex];
    });
  };

  if (loading) return <div style={s.center}>{t.loading}</div>;
  if (error) return <div style={s.center}>{t.error}: {error}</div>;

  return (
    <div style={s.container}>
      <p style={s.subtitle}>{t.app.subtitle}</p>
      <SearchAndFilter exercises={exercises} filters={filters} setFilters={setFilters} resultsCount={filtered.length} />
      {filtered.length === 0 ? (
        <div style={s.empty}>{t.noResults}</div>
      ) : (
        <div style={s.grid}>
          {filtered.map(ex => (
            <ExerciseCard key={ex.id} exercise={ex} onClick={() => setSelected(ex)} />
          ))}
        </div>
      )}
      {selected && <ExerciseDetail exercise={selected} onClose={() => setSelected(null)} onCompare={handleCompare} isComparing={compareList.includes(selected)} />}
      {compareList.length > 0 && <ComparePanel exercises={compareList} onClose={() => setCompareList([])} onRemove={(id: string) => setCompareList(prev => prev.filter(e => e.id !== id))} />}
    </div>
  );
}

const s: Record<string, React.CSSProperties> = {
  container: { maxWidth: 1400, margin: '0 auto', padding: '24px 24px 60px' },
  subtitle: { color: 'rgba(255,255,255,0.4)', fontSize: 14, margin: '0 0 20px' },
  grid: { display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(220, 1fr))', gap: 20 },
  empty: { color: 'rgba(255,255,255,0.4)', textAlign: 'center', padding: '80px 0', fontSize: 18 },
  center: { color: 'rgba(255,255,255,0.5)', textAlign: 'center', padding: '120px 0', fontSize: 18 },
};
