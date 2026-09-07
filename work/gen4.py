import os
base = r'C:\Users\Administrator\Documents\Codex\2026-09-07\https-github-com-hasaneyldrm-exercises-dataset\web-app'
src = os.path.join(base, 'src')

# AppContext
code = """import { createContext, useContext, ReactNode } from 'react';
import { Language, WorkoutPlan } from '../types';
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
  const updatePlan = (plan: WorkoutPlan) =>
    setPlans(prev => prev.map(p => p.id === plan.id ? plan : p));
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
"""
with open(os.path.join(src, 'contexts', 'AppContext.tsx'), 'w', encoding='utf-8') as f:
    f.write(code)
print('AppContext done')
