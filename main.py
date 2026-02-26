import os
import requests
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Jeeves")

DNDTOOLS_URL = os.getenv("DNDTOOLS_URL", "http://localhost:8000")


def roll(die: str, count: int) -> dict:
    response = requests.get(f"{DNDTOOLS_URL}/roll/{die}/{count}")
    response.raise_for_status()
    return response.json()


@app.get("/roll/{die}/{count}")
def roll_dice(die: str, count: int):
    return roll(die, count)


@app.get("/", response_class=HTMLResponse)
def index():
    return """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Jeeves - DnD Roller</title>
  <style>
    body { font-family: sans-serif; padding: 2rem; background: #1e1e2e; color: #cdd6f4; }
    h1 { color: #cba6f7; }
    .roller { display: flex; align-items: center; gap: 1rem; margin: 1.5rem 0; }
    label { width: 3rem; font-weight: bold; color: #89b4fa; }
    input[type=number] {
      width: 5rem; padding: 0.4rem; border-radius: 6px;
      border: 1px solid #45475a; background: #313244; color: #cdd6f4;
    }
    button {
      padding: 0.4rem 1.2rem; border-radius: 6px; border: none;
      background: #cba6f7; color: #1e1e2e; font-weight: bold; cursor: pointer;
    }
    button:hover { background: #b4befe; }
    .result { font-size: 1.1rem; color: #a6e3a1; }
  </style>
</head>
<body>
  <h1>Jeeves - DnD Dice Roller</h1>

  <div class="roller">
    <label>D6</label>
    <input type="number" id="d6count" value="1" min="1">
    <button onclick="roll('d6', 'd6count', 'd6result')">Roll</button>
    <span class="result" id="d6result"></span>
  </div>

  <div class="roller">
    <label>D10</label>
    <input type="number" id="d10count" value="1" min="1">
    <button onclick="roll('d10', 'd10count', 'd10result')">Roll</button>
    <span class="result" id="d10result"></span>
  </div>

  <script>
    async function roll(die, inputId, resultId) {
      const count = document.getElementById(inputId).value;
      const resp = await fetch(`/roll/${die}/${count}`);
      const data = await resp.json();
      document.getElementById(resultId).textContent = data.result;
    }
  </script>
</body>
</html>
"""

