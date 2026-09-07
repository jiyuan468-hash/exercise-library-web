import os, json

base = r'C:\Users\Administrator\Documents\Codex\2026-09-07\https-github-com-hasaneyldrm-exercises-dataset\web-app'
src = os.path.join(base, 'src')
for d in ['types','i18n','hooks','contexts','components','pages']:
    os.makedirs(os.path.join(src, d), exist_ok=True)

types_code = """export interface Exercise {
  id: string; name: string; category: string; body_part: string; equipment: string;
  instructions: Record<string, string>;
  instruction_steps: Record<string, string[]>;
  muscle_group: string; secondary_muscles: string[]; target: string;
  media_id: string; image: string; gif_url: string;
  attribution: string; created_at: string;
}

export interface WorkoutExercise {
  exercise: Exercise; sets: number; reps: string; notes?: string;
}

export interface WorkoutPlan {
  id: string; name: string; exercises: WorkoutExercise[]; created_at: string;
}

export interface Filters {
  search: string; bodyPart: string; equipment: string; target: string;
}

export type Language = 'zh' | 'en';
"""
with open(os.path.join(src, 'types', 'index.ts'), 'w', encoding='utf-8') as f:
    f.write(types_code)
print('types done')
