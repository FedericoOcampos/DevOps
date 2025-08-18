# FastAPI Time API

Simple FastAPI application that exposes an endpoint returning the current server time in JSON.

## Project structure

```
fastapi-time-api
├── app
│   ├── main.py          # Entry point of the FastAPI application
│   └── api
│       └── time.py      # Defines the /current-time endpoint
├── requirements.txt     # Project dependencies
├── Procfile             # Start command for Render
├── .github/workflows    # CI workflow for tests + deploy to Render
└── tests                # Unit tests
```

## Local setup

1. Clone the repository

```
git clone <repository-url>
cd fastapi-time-api
```

2. Create and activate a venv (Windows PowerShell example):

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
```

3. Install dependencies

```powershell
pip install -r requirements.txt
```

4. Run the app (local dev)

```powershell
python -m uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000 and http://127.0.0.1:8000/current-time

## Tests

Run tests with:

```powershell
python -m pytest -q
```

## Deploy to Render using GitHub Actions

This repository includes a GitHub Actions workflow (`.github/workflows/deploy-to-render.yml`) that:
- Installs dependencies
- Runs tests with `pytest`
- If tests pass, triggers a deploy on Render by calling the Render Deploy API

Steps to configure:

1. Create a Web Service on Render and connect your GitHub repository. Choose a Python service.
2. Set Render build command to:

```
pip install -r requirements.txt
```

3. Set start command (Render):

```
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

4. Add two GitHub repository secrets (Settings → Secrets and variables → Actions):
- `RENDER_API_KEY` — a Render API key (create it in the Render dashboard; keep it secret).
- `RENDER_SERVICE_ID` — the Render service id for your Web Service.

5. Push to `main` (or `master`). The workflow will run and, if tests pass, call Render to trigger a deploy.

Notes:
- You can enable direct auto-deploys in Render, in which case the webhook deploy step is optional.
- The workflow only triggers the deploy job for `main`/`master` branch pushes.

## License

MIT