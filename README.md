# Pomotai

Pomotai is a minimal Pomodoro timer web app, served by a tiny Python script.
Open the page locally, start work/break sessions, and track completed focus cycles.

This repository is named `simple-pomodoro-timer` and focuses on clarity and minimal implementation.

## Features
- 25-minute work / 5-minute break defaults with clear “Working” / “Break” states
- Start, pause, resume, and reset controls
- Cycle history and badge count (one work + break = one cycle)
- Dependency-free static page (plain HTML, CSS, and JavaScript)

## Getting Started

### Prerequisites
- Python 3.8+ (for the local server)
- A modern web browser

### Run the local server
From the project root:

    python main.py

Then open the following URL in your browser:

    http://localhost:8000

## Project Structure
- `main.py` — Serves static files using Python’s built-in `SimpleHTTPRequestHandler`
- `index.html` — Pomotai UI and timer logic (HTML / CSS / JavaScript)

## Usage
- Click “Start Work (25)” to begin a focus session
- Click “Start Break (5)” to begin a break
- Use “Pause” / “Resume” to manage interruptions
- “Reset” clears the current timer (history resets when the browser is closed)

## Customization
- Adjust durations in `index.html` by changing `WORK_DURATION` and `BREAK_DURATION` (in seconds)
- Change the default port by editing the `serve` function in `main.py`

## Development Notes
- Uses only Python’s standard library
- Designed as a small learning-focused personal project

## License
MIT
