# Ampere Project

This project was created with [Ampere](https://github.com/SeamusMullan/ampere).

## Getting Started

### Prerequisites

- Node.js 16+
- Python 3.11+
- npm or yarn
- uv package manager

### Installation

First, install the uv package manager:

```bash
# On Linux/macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
# Download and run the installer from https://github.com/astral/uv/releases
```

Then, set up the project:

```bash
# Install dependencies
npm run install:all

# This command will:
# 1. Install root project dependencies
# 2. Set up the frontend (Electron/Vite)
# 3. Set up the backend (Python/FastAPI) with uv
```

### Development

```bash
# Start both frontend and backend
npm run dev

# Or start them separately
npm run dev:frontend
npm run dev:backend
```

## Project Structure

```
├── frontend/        # Electron/Vite frontend
├── backend/         # Python/FastAPI backend
└── package.json     # Root package.json for scripts
```

## License

This project is licensed under the MIT License.