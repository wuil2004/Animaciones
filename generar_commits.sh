#!/bin/bash

# Rama donde se harán los commits
branch="main"  # Cámbiala si tu rama se llama diferente

# Commits del 24 al 31 de marzo de 2025
for day in $(seq -f "%02g" 24 31); do
  date="2025-03-${day} 12:00:00"
  git commit --allow-empty -m "Commit del 2025-03-${day}" --date="${date}"
done

# Commits del 01 al 30 de abril de 2025
for day in $(seq -f "%02g" 1 30); do
  date="2025-04-${day} 12:00:00"
  git commit --allow-empty -m "Commit del 2025-04-${day}" --date="${date}"
done

# Commits del 01 al 04 de mayo de 2025
for day in $(seq -f "%02g" 1 4); do
  date="2025-05-${day} 12:00:00"
  git commit --allow-empty -m "Commit del 2025-05-${day}" --date="${date}"
done

# Empujar al repositorio remoto
git push origin $branch --force

echo "Commits realizados del 24 de marzo al 4 de mayo de 2025."

