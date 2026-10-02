"""
Environment / configuration loading.

Hints:
- load_dotenv() here once, at import time.
- Read OPENAI_API_KEY and OPENAI_MODEL from env (fail fast / raise if the
  key is missing rather than letting the SDK fail later with a vague error).
- Keep this the single place other modules pull config from, so tests can
  monkeypatch it easily instead of touching os.environ everywhere.
"""
