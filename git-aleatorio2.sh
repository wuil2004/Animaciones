#!/bin/bash

# Configuración
year=2025
start_month=05
start_day=11
end_month=06
end_day=14
branch="main"  # Cambia la rama si es necesario

# Función para generar fecha aleatoria
random_datetime() {
  local day=$1
  local month=$2
  hour=$((RANDOM % 24))
  minute=$((RANDOM % 60))
  second=$((RANDOM % 60))
  echo "${year}-${month}-${day} ${hour}:${minute}:${second}"
}

# Generar commits para mayo (del 11 al 31)
for day in $(seq -f "%02g" $start_day 31); do
  commits_count=$((RANDOM % 7 + 2))  # 2-8 commits
  echo "-> Generando $commits_count commits para $day/$start_month/$year"
  for ((i=1; i<=$commits_count; i++)); do
    git commit --allow-empty -m "Commit aleatorio #$i - $day/$start_month" --date="$(random_datetime $day $start_month)"
  done
done

# Generar commits para junio (del 1 al 14)
for day in $(seq -f "%02g" 1 $end_day); do
  commits_count=$((RANDOM % 7 + 2))  # 2-8 commits
  echo "-> Generando $commits_count commits para $day/$end_month/$year"
  for ((i=1; i<=$commits_count; i++)); do
    git commit --allow-empty -m "Commit aleatorio #$i - $day/$end_month" --date="$(random_datetime $day $end_month)"
  done
done

# Opcional: Empujar cambios (elimina --force si no es necesario)
git push origin $branch --force

echo "Finalizado: Commits aleatorios generados del $start_day/$start_month al $end_day/$end_month/$year"