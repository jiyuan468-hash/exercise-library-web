import os

base = r'C:\Users\Administrator\Documents\Codex\2026-09-07\https-github-com-hasaneyldrm-exercises-dataset\web-app'
src = os.path.join(base, 'src')

# Fix all files with broken imports
fixes = {
    'components/ExerciseCard.tsx': "import type { Exercise } from '../types';\nimport { useApp } from '../contexts/AppContext';\nimport { zh, en } from '../i18n';",
    'components/ExerciseDetail.tsx': "import type { Exercise } from '../types';\nimport { useApp } from '../contexts/AppContext';\nimport { zh, en } from '../i18n';",
    'components/SearchAndFilter.tsx': "import { useApp } from '../contexts/AppContext';\nimport { zh, en } from '../i18n';\nimport type { Exercise, Filters } from '../types';",
    'contexts/AppContext.tsx': "import { createContext, useContext, ReactNode } from 'react';\nimport type { Language, WorkoutPlan } from '../types';\nimport { useLocalStorage } from '../hooks/useLocalStorage';",
    'hooks/useExercises.ts': "import { useState, useEffect, useRef } from 'react';\nimport type { Exercise } from '../types';",
    'pages/FavoritesPage.tsx': "import type { Exercise } from '../types';\nimport { useExercises } from '../hooks/useExercises';\nimport { useApp } from '../contexts/AppContext';\nimport { zh, en } from '../i18n';",
    'pages/HomePage.tsx': "import { useState, useMemo } from 'react';\nimport { useExercises } from '../hooks/useExercises';\nimport { useApp } from '../contexts/AppContext';\nimport { zh, en } from '../i18n';\nimport type { Exercise, Filters } from '../types';",
    'pages/PlansPage.tsx': "import { useState } from 'react';\nimport type { WorkoutPlan, WorkoutExercise } from '../types';\nimport { useExercises } from '../hooks/useExercises';\nimport { useApp } from '../contexts/AppContext';\nimport { zh, en } from '../i18n';",
}

for rel, imports in fixes.items():
    fp = os.path.join(src, rel)
    with open(fp, 'r', encoding='utf-8') as f:
        code = f.read()
    # Replace the broken import lines at the top
    lines = code.split('\n')
    # Find where the real content starts (first non-import line or first interface/component)
    new_lines = []
    skip = True
    for line in lines:
        if skip and (line.startswith('import') or line.strip() == ''):
            continue
        skip = False
        new_lines.append(line)
    code = imports + '\n\n' + '\n'.join(new_lines)
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(code)
    print(f'Fixed: {rel}')
