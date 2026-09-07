import os
base = r'C:\Users\Administrator\Documents\Codex\2026-09-07\https-github-com-hasaneyldrm-exercises-dataset\web-app'
src = os.path.join(base, 'src')

# useLocalStorage
code1 = """import { useState } from 'react';

export function useLocalStorage<T>(key: string, initialValue: T): [T, (v: T | ((p: T) => T)) => void] {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });
  const setValue = (value: T | ((p: T) => T)) => {
    const valueToStore = value instanceof Function ? value(storedValue) : value;
    setStoredValue(valueToStore);
    window.localStorage.setItem(key, JSON.stringify(valueToStore));
  };
  return [storedValue, setValue];
}
"""
with open(os.path.join(src, 'hooks', 'useLocalStorage.ts'), 'w', encoding='utf-8') as f:
    f.write(code1)
print('useLocalStorage done')

# useExercises
code2 = """import { useState, useEffect, useRef } from 'react';
import { Exercise } from '../types';

const DATA_URL = 'https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/data/exercises.json';
const CACHE_KEY = 'exercises_cache';
const CACHE_TTL = 24 * 60 * 60 * 1000;

export function useExercises() {
  const [exercises, setExercises] = useState<Exercise[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const fetchedRef = useRef(false);

  useEffect(() => {
    if (fetchedRef.current) return;
    fetchedRef.current = true;
    try {
      const cached = localStorage.getItem(CACHE_KEY);
      if (cached) {
        const { data, timestamp } = JSON.parse(cached);
        if (Date.now() - timestamp < CACHE_TTL && data.length > 0) {
          setExercises(data);
          setLoading(false);
          return;
        }
      }
    } catch {}
    fetch(DATA_URL)
      .then(res => { if (!res.ok) throw new Error('HTTP ' + res.status); return res.json(); })
      .then(data => {
        try { localStorage.setItem(CACHE_KEY, JSON.stringify({ data, timestamp: Date.now() })); } catch {}
        setExercises(data);
        setLoading(false);
      })
      .catch(err => { setError(err.message); setLoading(false); });
  }, []);

  return { exercises, loading, error };
}
"""
with open(os.path.join(src, 'hooks', 'useExercises.ts'), 'w', encoding='utf-8') as f:
    f.write(code2)
print('useExercises done')
