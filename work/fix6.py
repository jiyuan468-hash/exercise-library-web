import os

base = r'C:\Users\Administrator\Documents\Codex\2026-09-07\https-github-com-hasaneyldrm-exercises-dataset\web-app'
src = os.path.join(base, 'src')

# Fix AppContext.tsx
with open(os.path.join(src, 'contexts', 'AppContext.tsx'), 'r', encoding='utf-8') as f:
    code = f.read()
code = code.replace(\"import type { ReactNode, Language, WorkoutPlan } from '../types';\", \"import type { ReactNode } from 'react';\\nimport type { Language, WorkoutPlan } from '../types';\")
with open(os.path.join(src, 'contexts', 'AppContext.tsx'), 'w', encoding='utf-8') as f:
    f.write(code)
print('AppContext fixed')

# Fix FavoritesPage.tsx
with open(os.path.join(src, 'pages', 'FavoritesPage.tsx'), 'r', encoding='utf-8') as f:
    code = f.read()
code = code.replace(\"import { useMemo } from 'react';\", \"import { useState, useMemo } from 'react';\")
with open(os.path.join(src, 'pages', 'FavoritesPage.tsx'), 'w', encoding='utf-8') as f:
    f.write(code)
print('FavoritesPage fixed')
