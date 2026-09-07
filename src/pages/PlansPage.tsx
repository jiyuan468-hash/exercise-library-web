import { useState, useMemo } from 'react';
import type { WorkoutPlan, WorkoutExercise } from '../types';
import { useExercises } from '../hooks/useExercises';
import { useApp } from '../contexts/AppContext';
import { zh, en } from '../i18n';

export default function PlansPage() {
  const { exercises } = useExercises();
  const { plans, addPlan, updatePlan, deletePlan, favorites } = useApp();
  const { lang } = useApp();
  const t = lang === 'zh' ? zh : en;
  const [showNew, setShowNew] = useState(false);
  const [newName, setNewName] = useState('');
  const [newExerciseId, setNewExerciseId] = useState('');

  const favExercises = useMemo(() =>
    exercises.filter((ex: any) => favorites.includes(ex.id)),
    [exercises, favorites]
  );

  const handleCreate = () => {
    if (!newName.trim()) return;
    const plan: WorkoutPlan = { id: Date.now().toString(), name: newName.trim(), exercises: [], created_at: new Date().toISOString() };
    addPlan(plan);
    setNewName('');
    setShowNew(false);
  };

  const handleAddExercise = (planId: string) => {
    if (!newExerciseId) return;
    const ex = exercises.find((e: any) => e.id === newExerciseId);
    if (!ex) return;
    const plan = plans.find(p => p.id === planId);
    if (!plan) return;
    const we: WorkoutExercise = { exercise: ex, sets: 3, reps: '12' };
    updatePlan({ ...plan, exercises: [...plan.exercises, we] });
    setNewExerciseId('');
  };

  const handleUpdateExercise = (planId: string, idx: number, field: string, value: string | number) => {
    const plan = plans.find(p => p.id === planId);
    if (!plan) return;
    const updated = [...plan.exercises];
    (updated[idx] as any)[field] = value;
    updatePlan({ ...plan, exercises: updated });
  };

  const handleRemoveExercise = (planId: string, idx: number) => {
    const plan = plans.find(p => p.id === planId);
    if (!plan) return;
    updatePlan({ ...plan, exercises: plan.exercises.filter((_: any, i: number) => i !== idx) });
  };

  return (
    <div style={{ maxWidth: 900, margin: '0 auto', padding: '24px' }}>
      <div style={s.header}>
        <h1 style={s.title}>{t.plans.title}</h1>
        <button style={s.newBtn} onClick={() => setShowNew(!showNew)}>{showNew ? t.back : '+ ' + t.plans.newPlan}</button>
      </div>
      {showNew && (
        <div style={s.newPlanBox}>
          <input value={newName} onChange={e => setNewName(e.target.value)} placeholder={t.plans.planName} style={s.input} />
          <button onClick={handleCreate} style={s.saveBtn}>{t.plans.savePlan}</button>
        </div>
      )}
      {plans.length === 0 && !showNew ? (
        <div style={s.empty}>{t.plans.empty}</div>
      ) : (
        plans.map(plan => (
          <div key={plan.id} style={s.planCard}>
            <div style={s.planHeader}>
              <h3 style={s.planName}>{plan.name}</h3>
              <span style={s.planCount}>{plan.exercises.length} exercises</span>
              <button style={s.deleteBtn} onClick={() => deletePlan(plan.id)}>{t.plans.deletePlan}</button>
            </div>
            {plan.exercises.map((we: WorkoutExercise, idx: number) => (
              <div key={idx} style={s.exerciseRow}>
                <div style={s.exerciseInfo}>
                  <span style={s.exName}>{we.exercise.name}</span>
                  <span style={s.exMeta}>{we.exercise.body_part} · {we.exercise.target}</span>
                </div>
                <div style={s.exControls}>
                  <select value={we.sets} onChange={e => handleUpdateExercise(plan.id, idx, 'sets', parseInt(e.target.value))} style={s.select}>
                    {[1,2,3,4,5,6].map(n => <option key={n} value={n}>{n} sets</option>)}
                  </select>
                  <input value={we.reps} onChange={e => handleUpdateExercise(plan.id, idx, 'reps', e.target.value)} placeholder="reps" style={s.inputSmall} />
                  <button style={s.removeExBtn} onClick={() => handleRemoveExercise(plan.id, idx)}>✕</button>
                </div>
              </div>
            ))}
            <div style={s.addRow}>
              <select value={newExerciseId} onChange={e => setNewExerciseId(e.target.value)} style={s.select}>
                <option value="">{t.plans.addExercise}</option>
                {favExercises.map((ex: any) => <option key={ex.id} value={ex.id}>{ex.name}</option>)}
              </select>
              <button onClick={() => handleAddExercise(plan.id)} style={s.addBtn}>+</button>
            </div>
          </div>
        ))
      )}
    </div>
  );
}

const s: Record<string, React.CSSProperties> = {
  header: { display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 24 },
  title: { color: '#fff', fontSize: 28, fontWeight: 700, margin: 0 },
  newBtn: { background: 'rgba(255,80,80,0.2)', border: '1px solid rgba(255,80,80,0.3)', color: '#ff6b6b', padding: '10px 20px', borderRadius: 10, fontSize: 14, fontWeight: 600, cursor: 'pointer' },
  newPlanBox: { display: 'flex', gap: 12, marginBottom: 24 },
  input: { flex: 1, padding: '12px 16px', background: 'rgba(255,255,255,0.07)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: 10, color: '#fff', fontSize: 15, outline: 'none' },
  saveBtn: { background: 'rgba(80,200,120,0.2)', border: '1px solid rgba(80,200,120,0.3)', color: '#50c878', padding: '10px 20px', borderRadius: 10, fontSize: 14, fontWeight: 600, cursor: 'pointer' },
  empty: { color: 'rgba(255,255,255,0.4)', textAlign: 'center', padding: '80px 0', fontSize: 16 },
  planCard: { background: 'rgba(255,255,255,0.04)', borderRadius: 16, padding: 20, marginBottom: 16, border: '1px solid rgba(255,255,255,0.06)' },
  planHeader: { display: 'flex', alignItems: 'center', gap: 12, marginBottom: 16 },
  planName: { color: '#fff', fontSize: 18, fontWeight: 700, margin: 0, flex: 1 },
  planCount: { color: 'rgba(255,255,255,0.4)', fontSize: 13 },
  deleteBtn: { background: 'none', border: 'none', color: 'rgba(255,80,80,0.6)', fontSize: 13, cursor: 'pointer' },
  exerciseRow: { display: 'flex', justifyContent: 'space-between', alignItems: 'center', padding: '12px 0', borderBottom: '1px solid rgba(255,255,255,0.04)' },
  exerciseInfo: { display: 'flex', flexDirection: 'column', gap: 4 },
  exName: { color: '#fff', fontSize: 15, fontWeight: 500 },
  exMeta: { color: 'rgba(255,255,255,0.4)', fontSize: 12 },
  exControls: { display: 'flex', gap: 8, alignItems: 'center' },
  select: { padding: '8px 12px', background: 'rgba(255,255,255,0.07)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: 8, color: '#fff', fontSize: 13, outline: 'none', cursor: 'pointer' },
  inputSmall: { width: 60, padding: '8px 10px', background: 'rgba(255,255,255,0.07)', border: '1px solid rgba(255,255,255,0.1)', borderRadius: 8, color: '#fff', fontSize: 13, outline: 'none' },
  removeExBtn: { background: 'none', border: 'none', color: 'rgba(255,80,80,0.6)', cursor: 'pointer', fontSize: 16, padding: '4px 8px' },
  addRow: { display: 'flex', gap: 8, marginTop: 12 },
  addBtn: { background: 'rgba(255,255,255,0.07)', border: '1px solid rgba(255,255,255,0.1)', color: '#fff', width: 36, height: 36, borderRadius: 8, fontSize: 18, cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center' },
};
