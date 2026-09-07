import { useState, useEffect, useRef } from 'react';
import type { Exercise } from '../types';

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
