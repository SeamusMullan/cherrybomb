# Frontend Overview

This document provides an overview of the CherryBomb desktop application's frontend architecture, technology stack, and key structural elements. The frontend is designed to be intuitive, responsive, and provide a seamless user experience for managing social media analytics and content strategy.

## Goals

- **User-Friendly Interface**: Simplify complex data analysis and prediction tasks.
- **Responsiveness**: Ensure a smooth experience across different interactions within the desktop application.
- **Modularity**: Build components that are reusable and maintainable.
- **Performance**: Optimize for quick data loading and interaction.
- **Accessibility**: Adhere to accessibility standards to make the application usable by a wider audience.

## Technology Stack

The frontend of CherryBomb is primarily built using the following technologies:

- **Electron**: For building the cross-platform desktop application shell using web technologies.
- **React**: A JavaScript library for building user interfaces, chosen for its component-based architecture and strong community support.
- **Redux (or similar state management like Zustand/Context API)**: For managing application state in a predictable way, especially for complex data flows.
- **TypeScript**: For static typing, improving code quality and maintainability.
- **HTML5 & CSS3**: For structuring and styling the application.
  - **CSS Modules / Styled-Components / Tailwind CSS**: For scoped styling and efficient CSS management.
- **D3.js / Recharts / Chart.js**: For creating interactive and informative data visualizations.
- **Axios / Fetch API**: For making requests to any potential local backend services or external APIs (though primarily a desktop app, some integrations might require this).
- **Jest / React Testing Library**: For unit and integration testing of components and logic.

## Architecture

The frontend follows a component-based architecture, promoting reusability and separation of concerns.

```mermaid
graph TD
    App[Application Shell (Electron)] --> MainProcess[Electron Main Process]
    App --> RendererProcess[Electron Renderer Process (React App)]

    RendererProcess --> UIRoot[UI Root (React)]
    UIRoot --> StateManagement[State Management (e.g., Redux)]
    UIRoot --> Routing[Routing (e.g., React Router)]
    UIRoot --> Pages[Pages/Views]
    UIRoot --> SharedComponents[Shared UI Components]

    Pages --> DashboardPage[Dashboard Page]
    Pages --> DataCollectionPage[Data Collection Page]
    Pages --> DatasetMgmtPage[Dataset Management Page]
    Pages --> AnalysisPage[Analysis & Reports Page]
    Pages --> PredictionPage[Prediction Models Page]
    Pages --> CalendarPage[Content Calendar Page]
    Pages --> AccountMgmtPage[Account Management Page]
    Pages --> SettingsPage[Settings Page]

    SharedComponents --> Buttons[Buttons]
    SharedComponents --> Forms[Forms & Inputs]
    SharedComponents --> Modals[Modals]
    SharedComponents --> Charts[Chart Wrappers]
    SharedComponents --> NavigationElements[Navigation (Sidebar, Tabs)]

    StateManagement --> DataLogic[Data Fetching & Caching Logic]
    DataLogic --> LocalStorage[Local Data Storage Adapters]
    LocalStorage --> FileSystem[File System (via Electron Main)]
    LocalStorage --> SQLite[SQLite DB (via Electron Main)]

    Pages --> APIIntegration[API/Service Integration Layer]
    APIIntegration --> LocalServices[Local Backend Services (if any)]
    APIIntegration --> PlatformAPIs[Platform API Connectors (via secure handling)]
```

### Key Architectural Components

1. **Electron Shell**
   - **Main Process**: Manages application lifecycle, native OS interactions (dialogs, menus), and background tasks. Handles communication with the Renderer process.
   - **Renderer Process**: Runs the React application (the user interface). Each window in Electron typically has its own renderer process.

2. **React Application**
   - **Routing**: Manages navigation between different views/pages of the application.
   - **State Management**: Centralized store for application data, ensuring consistency and facilitating data flow between components.
   - **Pages/Views**: Top-level components representing major sections of the application (e.g., Dashboard, Content Calendar).
   - **Shared UI Components**: Reusable UI elements (buttons, forms, charts) used across multiple pages.
   - **Service Integration Layer**: Handles communication with local data sources, file system, or any backend services if applicable.

## Directory Structure (Conceptual)

A typical frontend directory structure might look like this:

```plaintext
src/
|-- main.ts (Electron Main Process entry)
|-- preload.ts (Electron Preload Script)
|-- renderer/
|   |-- App.tsx (React App Root)
|   |-- index.tsx (React Renderer Entry)
|   |-- assets/ (images, fonts)
|   |-- components/ (shared UI components)
|   |   |-- Button/
|   |   |-- Chart/
|   |   |-- ...
|   |-- constants/ (application-wide constants)
|   |-- contexts/ (React Context API providers)
|   |-- features/ (module-specific components and logic)
|   |   |-- dashboard/
|   |   |-- dataCollection/
|   |   |-- ...
|   |-- hooks/ (custom React hooks)
|   |-- layouts/ (page layout components)
|   |-- pages/ (top-level page components)
|   |-- services/ (data fetching, API interactions)
|   |-- store/ (state management configuration and slices)
|   |-- styles/ (global styles, theme)
|   |-- types/ (TypeScript type definitions)
|   |-- utils/ (utility functions)
|-- index.html (HTML entry for Electron Renderer)
```

This overview provides a foundational understanding of the CherryBomb frontend. Detailed documentation for specific components, pages, and features can be found in their respective sections.
