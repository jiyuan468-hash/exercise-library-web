import { useApp } from '../contexts/AppContext';
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
