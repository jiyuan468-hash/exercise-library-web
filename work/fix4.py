import os

base = r'C:\Users\Administrator\Documents\Codex\2026-09-07\https-github-com-hasaneyldrm-exercises-dataset\web-app'
src = os.path.join(base, 'src')

# SearchAndFilter.tsx - complete rewrite
with open(os.path.join(src, 'components', 'SearchAndFilter.tsx'), 'w', encoding='utf-8') as f:
    f.write("""import { useApp } from '../contexts/AppContext';
import { zh, en } from '../i18n';
import type { Exercise, Filters } from '../types';

interface Props {
  exercises: Exercise[];
  filters: Filters;
  setFilters: (f: Filters) => void;
  resultsCount: number;
}

export default function SearchAndFilter({ exercises, filters, setFilters, resultsCount }: Props) {
  const { lang } = useApp();
  const t = lang === 'zh' ? zh : en;
  const bodyParts = [...new Set(exercises.map(e => e.body_part))].sort();
  const equipments = [...new Set(exercises.map(e => e.equipment))].sort();
  const targets = [...new Set(exercises.map(e => e.target))].sort();
  const bpMap: Record<string, string> = t.bodyParts;
  const eqMap: Record<string, string> = t.equipment;
  const hasFilters = filters.search || filters.bodyPart || filters.equipment || filters.target;
  return (
    <div style={s.container}>
      <div style={s.searchRow}>
        <div style={s.searchBox}>
          <span style={s.searchIcon}>🔍</span>
          <input type="text" value={filters.search}
            onChange={e => setFilters({ ...filters, search: e.target.value })}
            placeholder={t.search.placeholder} style={s.searchInput} />
        </div>
        {hasFilters && (
          <button onClick={() => setFilters({ search: '', bodyPart: '', equipment: '', target: '' })} style={s.clearBtn}>
            ✕ {t.filters.clear}
          </button>
        )}
      </div>
      <div style={s.filterRows}>
        {[
          { key: 'bodyPart', label: t.filters.bodyPart, options: bodyParts, map: bpMap },
          { key: 'equipment', label: t.filters.equipment, options: equipments, map: eqMap },
          { key: 'target', label: t.filters.target, options: targets, map: {} },
        ].map(({ key, label, options, map }) => (
          <div key={key} style={s.filterGroup}>
            <label style={s.filterLabel}>{label}</label>
            <select value={(filters as any)[key]}
              onChange={e => setFilters({ ...filters, [key]: e.target.value })}
              style={s.select}>
              <option value="">{t.filters.all}</option>
              {options.map(opt => (
                <option key={opt} value={opt}>{map[opt] || opt}</option>
              ))}
            </select>
          </div>
        ))}
      </div>
      <div style={s.results}>{resultsCount} {t.filters.results.replace('__fn__', 'found')}</div>
    </div>
  );
}

const s: Record<string, React.CSSProperties> = {
  container: { background: 'rgba(255,255,255,0.03)', borderRadius: 16, padding: '20px 24px', marginBottom: 24, border: '1px solid rgba(255,255,255,0.06)' },
  searchRow: { display: 'flex', gap: 12, marginBottom: 16 },
  searchBox: { flex: 1, position: 'relative', display: 'flex', alignItems: 'center' },
  searchIcon: { position: 'absolute', left: 14, fontSize: 18, opacity: 0.5 },
  searchInput: { width: '100%', padding: '12px 16px 12px 44px', background: 'rgba(255,255,255,0.07)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: 12, color: '#fff', fontSize: 16, outline: 'none' },
  clearBtn: { background: 'rgba(255,80,80,0.15)', border: '1px solid rgba(255,80,80,0.3)', color: '#ff6b6b', padding: '10px 18px', borderRadius: 10, fontSize: 14, fontWeight: 600, cursor: 'pointer', whiteSpace: 'nowrap' },
  filterRows: { display: 'flex', gap: 16, flexWrap: 'wrap' },
  filterGroup: { display: 'flex', flexDirection: 'column', gap: 6, flex: 1, minWidth: 180 },
  filterLabel: { color: 'rgba(255,255,255,0.5)', fontSize: 12, fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.5px' },
  select: { padding: '10px 14px', background: 'rgba(255,255,255,0.07)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: 10, color: '#fff', fontSize: 14, outline: 'none', cursor: 'pointer' },
  results: { marginTop: 16, color: 'rgba(255,255,255,0.4)', fontSize: 13 },
};
""")
print('SearchAndFilter done')

# HomePage.tsx - complete rewrite
with open(os.path.join(src, 'pages', 'HomePage.tsx'), 'w', encoding='utf-8') as f:
    f.write("""import { useState, useMemo } from 'react';
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
""")
print('HomePage done')
