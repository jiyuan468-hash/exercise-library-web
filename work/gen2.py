import os, json

base = r'C:\Users\Administrator\Documents\Codex\2026-09-07\https-github-com-hasaneyldrm-exercises-dataset\web-app'
src = os.path.join(base, 'src')

zh = {
  "app": {"title": "\u5065\u8eab\u52a8\u4f5c\u5e93", "subtitle": "1,324 \u4e2a\u52a8\u4f5c \u00b7 10 \u79cd\u8bed\u8a00"},
  "nav": {"home": "\u9996\u9875", "favorites": "\u6536\u85cf", "plans": "\u8bad\u7ec3\u8ba1\u5212"},
  "search": {"placeholder": "\u641c\u7d22\u52a8\u4f5c..."},
  "filters": {"all": "\u5168\u90e8", "bodyPart": "\u8eab\u4f53\u90e8\u4f4d", "equipment": "\u5668\u68b0", "target": "\u76ee\u6807\u808c\u7fa4", "clear": "\u6e05\u9664", "results": "__fn__"},
  "bodyParts": {"waist": "\u8170\u8179", "upperLegs": "\u4e0b\u80a2", "back": "\u80cc\u90e8", "chest": "\u80f8\u90e8", "shoulders": "\u80a9\u90e8", "upperArms": "\u4e0a\u80a2", "lowerLegs": "\u5c0f\u817f", "lowerArms": "\u524d\u81c2", "cardio": "\u6709\u6c27", "neck": "\u9888\u90e8"},
  "equipment": {"body weight": "\u81ea\u91cd", "dumbbell": "\u5495\u549a", "barbell": "\u6746\u94c3", "cable": "\u7ed5\u7ec6\u7ef3", "kettlebell": "\u58f6\u94c3", "band": "\u5f39\u529b\u5e26", "weighted": "\u8d1f\u91cd", "stability ball": "\u7a33\u5b9a\u7403", "medicine ball": "\u836f\u7403", "rope": "\u7ef3\u7d22", "ez barbell": "EZ\u68d2", "sled machine": "\u96ea\u6a47\u673a", "bosu ball": "\u535a\u901f\u7403", "roller": "\u6eda\u8f6e", "resistance band": "\u963b\u529b\u5e26", "upper body ergometer": "\u4e0a\u80a2\u8f66", "leverage machine": "\u6746\u6746\u673a", "smith machine": "\u53f2\u5bc6\u65af\u673a"},
  "exercise": {"name": "\u52a8\u4f5c\u540d\u79f0", "bodyPart": "\u8eab\u4f53\u90e8\u4f4d", "target": "\u76ee\u6807\u808c\u7fa4", "equipment": "\u6240\u9700\u5668\u68b0", "muscleGroup": "\u534f\u540c\u808c\u7fa4", "secondaryMuscles": "\u8f85\u52a9\u808c\u7fa4", "instructions": "\u52a8\u4f5c\u8bf4\u660e", "steps": "\u6b65\u9aa4", "stepsLabel": "__fn__", "gif": "\u52a8\u753b", "image": "\u56fe\u7247", "attribution": "\u7248\u6743"},
  "favorites": {"title": "\u6536\u85cf", "empty": "\u6682\u65e0\u6536\u85cf", "remove": "\u53d6\u6d88", "addToPlan": "\u52a0\u5165\u8ba1\u5212"},
  "plans": {"title": "\u8ba1\u5212", "empty": "\u6682\u65e0\u8ba1\u5212", "newPlan": "\u65b0\u5efa", "planName": "\u540d\u79f0", "addExercise": "\u6dfb\u52a0\u52a8\u4f5c", "sets": "\u7ec4\u6570", "reps": "\u6b21\u6570", "notes": "\u5907\u6ce8", "savePlan": "\u4fdd\u5b58", "deletePlan": "\u5220\u9664", "runPlan": "\u5f00\u59cb\u8bad\u7ec3", "exercises": "__fn__"},
  "compare": {"title": "\u5bf9\u6bd4", "empty": "\u9009\u62e9\u4e24\u4e2a\u52a8\u4f5c", "selectFirst": "\u7b2c\u4e00\u4e2a", "selectSecond": "\u7b2c\u4e8c\u4e2a", "clear": "\u6e05\u7a7a"},
  "lang": {"zh": "\u4e2d\u6587", "en": "English"},
  "loading": "\u52a0\u8f7d\u4e2d...", "error": "\u52a0\u8f7d\u5931\u8d25", "noResults": "\u672a\u627e\u5230\u7ed3\u679c", "back": "\u8fd4\u56de"
}

en = {
  "app": {"title": "Exercise Library", "subtitle": "1,324 exercises"},
  "nav": {"home": "Home", "favorites": "Favorites", "plans": "Workout Plans"},
  "search": {"placeholder": "Search exercises..."},
  "filters": {"all": "All", "bodyPart": "Body Part", "equipment": "Equipment", "target": "Target Muscle", "clear": "Clear", "results": "__fn__"},
  "bodyParts": {"waist": "Waist", "upperLegs": "Upper Legs", "back": "Back", "chest": "Chest", "shoulders": "Shoulders", "upperArms": "Upper Arms", "lowerLegs": "Lower Legs", "lowerArms": "Lower Arms", "cardio": "Cardio", "neck": "Neck"},
  "equipment": {"body weight": "Body Weight", "dumbbell": "Dumbbell", "barbell": "Barbell", "cable": "Cable", "kettlebell": "Kettlebell", "band": "Band", "weighted": "Weighted", "stability ball": "Stability Ball", "medicine ball": "Medicine Ball", "rope": "Rope", "ez barbell": "EZ Barbell", "sled machine": "Sled Machine", "bosu ball": "Bosu Ball", "roller": "Roller", "resistance band": "Resistance Band", "upper body ergometer": "Upper Body Ergometer", "leverage machine": "Leverage Machine", "smith machine": "Smith Machine"},
  "exercise": {"name": "Name", "bodyPart": "Body Part", "target": "Target", "equipment": "Equipment", "muscleGroup": "Muscle Group", "secondaryMuscles": "Secondary", "instructions": "Instructions", "steps": "Steps", "stepsLabel": "__fn__", "gif": "Animation", "image": "Image", "attribution": "Attribution"},
  "favorites": {"title": "Favorites", "empty": "No favorites yet", "remove": "Remove", "addToPlan": "Add to Plan"},
  "plans": {"title": "Plans", "empty": "No plans yet", "newPlan": "New Plan", "planName": "Name", "addExercise": "Add Exercise", "sets": "Sets", "reps": "Reps", "notes": "Notes", "savePlan": "Save", "deletePlan": "Delete", "runPlan": "Start", "exercises": "__fn__"},
  "compare": {"title": "Compare", "empty": "Select two exercises", "selectFirst": "First", "selectSecond": "Second", "clear": "Clear"},
  "lang": {"zh": "Chinese", "en": "English"},
  "loading": "Loading...", "error": "Failed to load", "noResults": "No results", "back": "Back"
}

with open(os.path.join(src, 'i18n', 'index.ts'), 'w', encoding='utf-8') as f:
    f.write('export const zh = ' + json.dumps(zh, ensure_ascii=False, indent=2) + ';\n\n')
    f.write('export const en = ' + json.dumps(en, ensure_ascii=False, indent=2) + ';\n\n')
    f.write('export type Translations = typeof zh;\n')
print('i18n done')
