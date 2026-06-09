@echo off

REM start cmd /k "docker compose -f src/database/docker-compose.yml down"

wt -w 0 nt -d . cmd /k "docker compose -f database/docker-compose.yml up"

wt -w 0 nt -d . cmd /k "api\.venv\Scripts\python -m fastapi dev api/app/main.py"

wt -w 0 nt -d . cmd /k "npm --prefix frontend run dev"