import os, re

base = r'C:\Users\Administrator\Documents\Codex\2026-09-07\https-github-com-hasaneyldrm-exercises-dataset\web-app'
src = os.path.join(base, 'src')

def fix_file(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        code = f.read()
    orig = code
    # Fix type-only imports: import { X, Y } -> import type { X, Y }
    # Only when ALL imports are types (no runtime values)
    for m in re.finditer(r'import \{([^}]+)\} from ([\'"][^\'"]+[\'"])', code):
        imports_str = m.group(1)
        all_types = True
        for imp in imports_str.split(','):
            imp = imp.strip()
            # Check if it's a known runtime import
            name = imp.split(':')[0].strip() if ':' in imp else imp.strip()
            runtime = {'useState', 'useEffect', 'useRef', 'useApp', 'ReactNode', 'React', 'useMemo'}
            if name in runtime:
                all_types = False
                break
        if all_types and ',' in imports_str:
            # Multi-import all types
            code = code.replace(m.group(0), f"import type {imports_str} from {m.group(2)}")
        elif all_types:
            code = code.replace(m.group(0), f"import type {imports_str} from {m.group(2)}")
    # Remove unused variable declarations
    # gifUrl in ExerciseCard
    code = re.sub(r"  const gifUrl = .*?\n", '', code)
    # bpEmoji in ExerciseCard
    code = re.sub(r"  const bpEmoji.*?};\n", '  // emojis\n', code)
    # unused useState in SearchAndFilter
    code = code.replace("import { useState } from 'react';\n", '')
    # unused editingPlan in PlansPage
    code = re.sub(r"  const \[editingPlan, setEditingPlan\].*?\n", '', code)
    # unused Exercise import in PlansPage
    code = code.replace("import type { WorkoutPlan, WorkoutExercise, Exercise } from '../types';", "import type { WorkoutPlan, WorkoutExercise } from '../types';")
    if code != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(code)
        print(f'Fixed: {os.path.basename(fp)}')

files = [
    os.path.join(src, 'components', 'ComparePanel.tsx'),
    os.path.join(src, 'components', 'ExerciseCard.tsx'),
    os.path.join(src, 'components', 'ExerciseDetail.tsx'),
    os.path.join(src, 'components', 'SearchAndFilter.tsx'),
    os.path.join(src, 'contexts', 'AppContext.tsx'),
    os.path.join(src, 'hooks', 'useExercises.ts'),
    os.path.join(src, 'pages', 'FavoritesPage.tsx'),
    os.path.join(src, 'pages', 'HomePage.tsx'),
    os.path.join(src, 'pages', 'PlansPage.tsx'),
]
for f in files:
    fix_file(f)
