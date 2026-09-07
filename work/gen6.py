import os
base = r'C:\Users\Administrator\Documents\Codex\2026-09-07\https-github-com-hasaneyldrm-exercises-dataset\web-app'
src = os.path.join(base, 'src')

# ExerciseCard.tsx
code = """import { Exercise } from '../types';
import { useApp } from '../contexts/AppContext';
import { zh, en } from '../i18n';

interface Props {
  exercise: Exercise;
  onClick: () => void;
}

export default function ExerciseCard({ exercise, onClick }: Props) {
  const { isFavorite, toggleFavorite } = useApp();
  const { lang } = useApp();
  const t = lang === 'zh' ? zh : en;
  const isFav = isFavorite(exercise.id);
  const gifUrl = 'https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/' + exercise.gif_url;
  const imgSrc = 'https://raw.githubusercontent.com/hasaneyldrm-exercises-dataset/main/' + exercise.image;
  const bpEmoji: Record<string, string> = {
    waist: '\\ud83c\\udfaf', upperLegs: '\\ud83e\\uddb5', back: '\\ud83d\\udd19',
    chest: '\\ud83d\\udd25', shoulders: '\\ud83c\\udfcb\\ufe0f', upperArms: '\\ud83d\\udcaa',
    lowerLegs: '\\ud83e\\uddb6', lowerArms: '\\ud83e\\ude84', cardio: '\\u2764\\ufe0f', neck: '\\ud83e\\ude91',
  };
  return (
    <div style={s.card} onClick={onClick}>
      <div style={s.media}>
        <img src={imgSrc} alt={exercise.name} style={s.img} loading="lazy" />
        <div style={s.badge}>{exercise.body_part}</div>
        <button style={{ ...s.favBtn, ...(isFav ? s.favBtnActive : {}) }}
          onClick={e => { e.stopPropagation(); toggleFavorite(exercise.id); }}>
          {isFav ? '\\u2764\\ufe0f' : '\\ud83d\\udc90'}
        </button>
      </div>
      <div style={s.info}>
        <div style={s.name}>{exercise.name}</div>
        <div style={s.meta}>
          <span>{t.exercise.target}: {exercise.target}</span>
          <span style={s.dot}>\\u00b7</span>
          <span>{exercise.equipment}</span>
        </div>
      </div>
    </div>
  );
}

const s: Record<string, React.CSSProperties> = {
  card: { background: 'rgba(255,255,255,0.04)', borderRadius: 16, overflow: 'hidden', cursor: 'pointer', transition: 'all 0.25s', border: '1px solid rgba(255,255,255,0.06)', display: 'flex', flexDirection: 'column' },
  media: { position: 'relative', aspectRatio: '1', overflow: 'hidden', background: 'rgba(0,0,0,0.3)' },
  img: { width: '100%', height: '100%', objectFit: 'cover', transition: 'transform 0.3s' },
  badge: { position: 'absolute', top: 10, left: 10, background: 'rgba(0,0,0,0.6)', backdropFilter: 'blur(8px)', color: '#fff', fontSize: 11, fontWeight: 600, padding: '4px 10px', borderRadius: 20, textTransform: 'uppercase' },
  favBtn: { position: 'absolute', top: 10, right: 10, background: 'rgba(0,0,0,0.5)', border: 'none', borderRadius: '50%', width: 36, height: 36, display: 'flex', alignItems: 'center', justifyContent: 'center', cursor: 'pointer', fontSize: 18, backdropFilter: 'blur(8px)' },
  favBtnActive: { background: 'rgba(255,50,80,0.3)' },
  info: { padding: '14px 16px', flex: 1 },
  name: { color: '#fff', fontSize: 15, fontWeight: 600, lineHeight: 1.4, marginBottom: 6, display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical', overflow: 'hidden' },
  meta: { color: 'rgba(255,255,255,0.45)', fontSize: 12, display: 'flex', alignItems: 'center', gap: 6 },
  dot: { opacity: 0.5 },
};
"""
with open(os.path.join(src, 'components', 'ExerciseCard.tsx'), 'w', encoding='utf-8') as f:
    f.write(code)
print('ExerciseCard done')
