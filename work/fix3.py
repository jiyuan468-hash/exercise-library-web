import os

base = r'C:\Users\Administrator\Documents\Codex\2026-09-07\https-github-com-hasaneyldrm-exercises-dataset\web-app'
src = os.path.join(base, 'src')

# ExerciseCard.tsx - complete rewrite
with open(os.path.join(src, 'components', 'ExerciseCard.tsx'), 'w', encoding='utf-8') as f:
    f.write("""import type { Exercise } from '../types';
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
  const imgSrc = 'https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/' + exercise.image;
  return (
    <div style={s.card} onClick={onClick}>
      <div style={s.media}>
        <img src={imgSrc} alt={exercise.name} style={s.img} loading="lazy" />
        <div style={s.badge}>{exercise.body_part}</div>
        <button style={{ ...s.favBtn, ...(isFav ? s.favBtnActive : {}) }}
          onClick={e => { e.stopPropagation(); toggleFavorite(exercise.id); }}>
          {isFav ? '❤️' : '🤍'}
        </button>
      </div>
      <div style={s.info}>
        <div style={s.name}>{exercise.name}</div>
        <div style={s.meta}>
          <span>{t.exercise.target}: {exercise.target}</span>
          <span style={s.dot}>·</span>
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
""")
print('ExerciseCard done')

# ExerciseDetail.tsx - complete rewrite
with open(os.path.join(src, 'components', 'ExerciseDetail.tsx'), 'w', encoding='utf-8') as f:
    f.write("""import type { Exercise } from '../types';
import { useApp } from '../contexts/AppContext';
import { zh, en } from '../i18n';
import { useState } from 'react';

interface Props {
  exercise: Exercise;
  onClose: () => void;
  onCompare?: (ex: Exercise) => void;
  isComparing?: boolean;
}

export default function ExerciseDetail({ exercise, onClose, onCompare, isComparing }: Props) {
  const { lang, isFavorite, toggleFavorite } = useApp();
  const t = lang === 'zh' ? zh : en;
  const [langTab, setLangTab] = useState<'zh' | 'en'>('zh');
  const steps = exercise.instruction_steps[langTab] || exercise.instruction_steps.en || [];
  const desc = exercise.instructions[langTab] || exercise.instructions.en || '';
  const gifUrl = 'https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/' + exercise.gif_url;
  const imgSrc = 'https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/' + exercise.image;
  const langLabels: Record<string, string> = { zh: '中文', en: 'English', tr: 'Turkish', es: 'Spanish', ru: 'Russian', fr: 'French' };
  return (
    <div style={s.overlay} onClick={onClose}>
      <div style={s.modal} onClick={e => e.stopPropagation()}>
        <button style={s.closeBtn} onClick={onClose}>X</button>
        <div style={s.header}>
          <div style={s.headerTop}>
            <span style={s.badge}>{exercise.body_part}</span>
            <button style={{ ...s.favBtn, ...(isFavorite(exercise.id) ? s.favBtnActive : {}) }}
              onClick={() => toggleFavorite(exercise.id)}>
              {isFavorite(exercise.id) ? '❤️' : '🤍'}
            </button>
          </div>
          <h2 style={s.title}>{exercise.name}</h2>
          <div style={s.metaRow}>
            <span>{t.exercise.target}: <b>{exercise.target}</b></span>
            <span style={s.dot}>·</span>
            <span>{t.exercise.equipment}: <b>{exercise.equipment}</b></span>
            <span style={s.dot}>·</span>
            <span>{t.exercise.muscleGroup}: <b>{exercise.muscle_group}</b></span>
          </div>
          {exercise.secondary_muscles.length > 0 && (
            <div style={s.secondary}>{t.exercise.secondaryMuscles}: {exercise.secondary_muscles.join(', ')}</div>
          )}
        </div>
        <div style={s.divider} />
        <div style={s.body}>
          <div style={s.mediaSection}>
            <img src={imgSrc} alt={exercise.name} style={s.mediaImg} />
            <div style={s.gifWrap}>
              <span style={s.gifLabel}>{t.exercise.gif}</span>
              <img src={gifUrl} alt={exercise.name + ' gif'} style={s.gifImg} />
            </div>
          </div>
          <div style={s.instructionsSection}>
            <div style={s.langTabs}>
              {(['zh', 'en'] as const).map(l => (
                <button key={l} onClick={() => setLangTab(l)}
                  style={{ ...s.langTab, ...(langTab === l ? s.langTabActive : {}) }}>
                  {langLabels[l] || l.toUpperCase()}
                </button>
              ))}
            </div>
            {desc && <p style={s.desc}>{desc}</p>}
            {steps.length > 0 && (
              <div style={s.steps}>
                <div style={s.stepsTitle}>{t.exercise.steps} ({steps.length})</div>
                {steps.map((step, i) => (
                  <div key={i} style={s.step}>
                    <span style={s.stepNum}>{i + 1}</span>
                    <span style={s.stepText}>{step}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
        <div style={s.footer}>
          <button style={s.compareBtn} onClick={() => onCompare && onCompare(exercise)} disabled={isComparing}>
            {isComparing ? '✅' : '📊'} {t.compare.selectSecond}
          </button>
        </div>
      </div>
    </div>
  );
}

const s: Record<string, React.CSSProperties> = {
  overlay: { position: 'fixed', inset: 0, background: 'rgba(0,0,0,0.8)', zIndex: 200, display: 'flex', alignItems: 'center', justifyContent: 'center', padding: 20 },
  modal: { background: 'linear-gradient(180deg, #1a1a2e 0%, #16213e 100%)', borderRadius: 24, maxWidth: 600, width: '100%', maxHeight: '90vh', overflow: 'auto', position: 'relative', border: '1px solid rgba(255,255,255,0.1)' },
  closeBtn: { position: 'absolute', top: 16, right: 16, background: 'rgba(255,255,255,0.1)', border: 'none', borderRadius: '50%', width: 36, height: 36, color: '#fff', fontSize: 18, cursor: 'pointer', zIndex: 10 },
  header: { padding: '24px 24px 16px' },
  headerTop: { display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 },
  badge: { background: 'rgba(255,80,80,0.2)', color: '#ff6b6b', fontSize: 13, fontWeight: 600, padding: '4px 12px', borderRadius: 20 },
  favBtn: { background: 'rgba(255,255,255,0.1)', border: 'none', borderRadius: '50%', width: 36, height: 36, fontSize: 18, cursor: 'pointer' },
  favBtnActive: { background: 'rgba(255,50,80,0.3)' },
  title: { color: '#fff', fontSize: 24, fontWeight: 700, margin: '0 0 12px' },
  metaRow: { color: 'rgba(255,255,255,0.6)', fontSize: 14, display: 'flex', gap: 8, flexWrap: 'wrap' },
  dot: { opacity: 0.4 },
  secondary: { color: 'rgba(255,255,255,0.4)', fontSize: 13, marginTop: 8 },
  divider: { height: 1, background: 'rgba(255,255,255,0.08)', margin: '0 24px' },
  body: { padding: '20px 24px' },
  mediaSection: { display: 'flex', gap: 16, marginBottom: 24 },
  mediaImg: { width: 120, height: 120, borderRadius: 12, objectFit: 'cover', background: 'rgba(0,0,0,0.3)' },
  gifWrap: { flex: 1, display: 'flex', flexDirection: 'column', gap: 8 },
  gifLabel: { color: 'rgba(255,255,255,0.4)', fontSize: 12, fontWeight: 600, textTransform: 'uppercase' },
  gifImg: { width: '100%', borderRadius: 12, background: 'rgba(0,0,0,0.3)' },
  instructionsSection: {},
  langTabs: { display: 'flex', gap: 8, marginBottom: 16 },
  langTab: { background: 'rgba(255,255,255,0.07)', border: '1px solid rgba(255,255,255,0.1)', color: 'rgba(255,255,255,0.5)', padding: '6px 16px', borderRadius: 8, fontSize: 13, cursor: 'pointer' },
  langTabActive: { background: 'rgba(255,80,80,0.2)', borderColor: 'rgba(255,80,80,0.4)', color: '#ff6b6b' },
  desc: { color: 'rgba(255,255,255,0.7)', fontSize: 15, lineHeight: 1.7, margin: '0 0 20px' },
  steps: {},
  stepsTitle: { color: 'rgba(255,255,255,0.5)', fontSize: 12, fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.5px', marginBottom: 12 },
  step: { display: 'flex', gap: 12, marginBottom: 12, alignItems: 'flex-start' },
  stepNum: { background: 'rgba(255,80,80,0.2)', color: '#ff6b6b', fontSize: 12, fontWeight: 700, width: 24, height: 24, borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0, marginTop: 2 },
  stepText: { color: 'rgba(255,255,255,0.7)', fontSize: 14, lineHeight: 1.6 },
  footer: { padding: '16px 24px', borderTop: '1px solid rgba(255,255,255,0.08)', display: 'flex', justifyContent: 'flex-end', gap: 12 },
  compareBtn: { background: 'rgba(255,255,255,0.07)', border: '1px solid rgba(255,255,255,0.1)', color: '#fff', padding: '10px 20px', borderRadius: 10, fontSize: 14, cursor: 'pointer' },
};
""")
print('ExerciseDetail done')
