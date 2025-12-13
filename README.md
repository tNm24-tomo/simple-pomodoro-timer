# Pomotai

A minimal Pomodoro timer web app served by a tiny Python script. Open the page locally, start work/break sessions, and track completed cycles.

## Features
- 25-minute work / 5-minute break defaults with clear “Working” / “Break” states.
- Start, pause, resume, reset controls.
- Cycle history and badge count (work → break completes one cycle).
- Simple, dependency-free static page.

## Getting Started

### Prerequisites
- Python 3.8+ (for the local server)
- A modern browser

### Run the local server
From the project root:
```bash
python main.py
```
Then open:
```
http://localhost:8000
```

## Project Structure
- `main.py` — Serves static files from the project directory using `SimpleHTTPRequestHandler`.
- `index.html` — Pomotai UI and timer logic (HTML/CSS/JS).
- `.mypy_cache/` — Type checker cache (ignored).

## Usage
- Click “Start Work (25)” to begin a focus session.
- Click “Start Break (5)” after finishing work to begin a short break.
- Use “Pause” / “Resume” to manage interruptions.
- “Reset” clears the current timer. Closing the browser clears history.

## Customization
- Adjust durations in `index.html` by changing `WORK_DURATION` and `BREAK_DURATION` (seconds).
- Change the default port by running `serve(<port>)` inside `main.py` or editing the `serve` default argument.

## Development Notes
- No external dependencies; uses Python’s standard library.
- Served files resolve relative to `main.py`, so keep `index.html` alongside it.

## License
MIT (or add your preferred license).
