#!/bin/bash

# Verificar si se proporcionaron los parámetros necesarios
if [ $# -lt 4 ]; then
  echo "Uso: $0 <año> <mes> <día_inicio> <día_fin>"
  exit 1
fi

# Definir el año, mes, día de inicio y día de fin
year=$1
month=$2
start_day=$3
end_day=$4

# Verificar que los días sean válidos
if [ $start_day -gt $end_day ]; then
  echo "El día de inicio debe ser menor o igual al día de fin."
  exit 1
fi

# Definir la rama del repositorio
branch="main"  # Cambia a la rama donde quieras hacer los commits

# Loop para cada día en el rango especificado
for day in $(seq -f "%02g" $start_day $end_day); do
  # Construir la fecha completa para la verificación
  full_date="${year}-${month}-${day}"

  # ===== MODIFICACIÓN CLAVE =====
  # 1. Obtener el día de la semana (1=Lunes, 6=Sábado, 7=Domingo)
  day_of_week=$(date -d "$full_date" +%u)

  # 2. Si es 6 (Sábado) o 7 (Domingo), saltar al siguiente día
  if [[ $day_of_week -ge 6 ]]; then
    echo "Día ${day}: Saltando fin de semana (Sábado/Domingo)."
    continue # <-- Esta es la instrucción clave para saltar la iteración
  fi

  # Decidir al azar cuántos commits hacer este día (entre 1 y 8)
  num_commits=$(( (RANDOM % 8) + 1 ))
  echo "Día ${day}: Creando ${num_commits} commits..."

  # Loop anidado para crear el número aleatorio de commits
  for i in $(seq 1 $num_commits); do
    # Generar una hora aleatoria
    hour=$(printf "%02d" $((RANDOM % 24)))
    minute=$(printf "%02d" $((RANDOM % 60)))
    second=$(printf "%02d" $((RANDOM % 60)))
    
    # Establecer la fecha y hora para el commit
    commit_date="${full_date} ${hour}:${minute}:${second}"

    # Realizar un commit vacío con la fecha deseada
    git commit --allow-empty -m "Commit #${i} para el día ${day}" --date="${commit_date}"
  done
done

# Empujar los cambios al repositorio remoto
echo "Subiendo todos los commits al repositorio..."
git push origin $branch --force

echo "¡Listo! Se crearon commits aleatorios, omitiendo fines de semana."