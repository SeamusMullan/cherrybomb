# Backend Services

This document details the specific local backend services that power the CherryBomb desktop application. These services run within or are managed by the Electron Main process and handle core functionalities like data collection, storage, machine learning, and analytics.

## 1. Data Collection Service

**Responsibilities**:

- Manage and authenticate connections to various social media platforms (Instagram, TikTok, YouTube, Twitter, Facebook, LinkedIn).
- Execute data scraping tasks based on user configuration (target accounts, content types, time range).
- Handle platform-specific API interactions and rate limiting.
- Normalize collected data into a standard schema before storage.
- Provide real-time progress updates to the frontend during collection.
- Securely manage API keys and user authentication tokens for platforms.

**Key Components**:

- **Platform Adapters**: Modules specific to each social media platform for handling API calls or scraping logic.

  ```mermaid
  graph TD
      DCS[Data Collection Service] --> InstagramAdapter
      DCS --> TikTokAdapter
      DCS --> YouTubeAdapter
      DCS --> TwitterAdapter
      DCS --> FacebookAdapter
      DCS --> LinkedInAdapter
      InstagramAdapter --> IAPI[Instagram API/Scraper]
      TikTokAdapter --> TAPI[TikTok API/Scraper]
      YouTubeAdapter --> YAPI[YouTube API]
      TwitterAdapter --> TwAPI[Twitter API]
      FacebookAdapter --> FAPI[Facebook Graph API]
      LinkedInAdapter --> LiAPI[LinkedIn API/Scraper]
  end
  ```

- **Job Scheduler/Queue**: Manages pending and active collection jobs.
- **Data Normalizer**: Transforms platform-specific data structures into a consistent internal format.
- **Authentication Manager**: Handles OAuth flows and secure storage/retrieval of access tokens (using Electron SafeStorage or system keychain).

## 2. Data Storage Service

**Responsibilities**:

- Provide a unified interface for storing and retrieving all application data.
- Manage a local SQLite database for structured metadata (projects, user settings, dataset information, smaller analytics results).
- Handle storage of large files on the local file system (e.g., raw scraped data, processed datasets in formats like JSON or Parquet, machine learning models).
- Ensure data integrity, backups (if implemented), and efficient querying.

**Key Components**:

- **Database Manager (SQLite)**: Wrapper around SQLite operations (CRUD, schema management, migrations).
- **File System Manager**: Handles reading/writing large data files, organizing them in user-specified or application-defined directories.
- **Data Indexer**: Optimizes data for fast searching and retrieval, potentially using full-text search capabilities of SQLite or separate indexing for file-based data.

## 3. Machine Learning Service

**Responsibilities**:

- Load and manage machine learning models for prediction and analysis (e.g., trend prediction, content performance forecasting, content optimization suggestions).
- Provide an API for the frontend or Analytics Service to make predictions.
- Execute model inference efficiently on the user's local machine.
- Potentially manage local model training or fine-tuning based on user data.
- If Python is used for ML models:
  - Manage the Python child process lifecycle.
  - Handle inter-process communication (IPC) between Node.js (Electron Main) and Python.

**Key Components**:

- **Model Loader**: Loads pre-trained models (bundled with the app or downloaded) or user-trained models from local storage.
- **Inference Engine**: Executes predictions using the loaded models. This could be TensorFlow.js (if models are in JS format) or an interface to a Python script running TensorFlow, PyTorch, or Scikit-learn.
- **Feature Extractor**: Preprocesses input data into the format expected by the ML models.
- **(Optional) Local Training Module**: If local training/fine-tuning is supported, this module would handle the training loop, data preparation for training, and saving updated models.

## 4. Analytics Service

**Responsibilities**:

- Perform complex data analysis on collected datasets.
- Generate aggregated metrics, statistics, and insights.
- Identify trends, patterns, and anomalies in the data.
- Prepare data in a format suitable for visualization in the frontend dashboard and reports.
- Interface with the Data Storage Service to retrieve data and the ML Service for predictive analytics.

**Key Components**:

- **Data Aggregator**: Processes raw data to compute summary statistics (e.g., average engagement rates, follower growth over time).
- **Trend Analysis Module**: Implements algorithms to detect emerging trends or seasonality in the data.
- **Reporting Engine**: Generates structured data for reports and visualizations.
- **Query Interface**: Allows other services or the frontend (via IPC) to request specific analytical computations.

## 5. Notification Service

**Responsibilities**:

- Provide feedback to the user about long-running background tasks.
- Send notifications for events like:
  - Data collection job completion or failure.
  - Model training completion.
  - New significant trend detected.
  - Errors or important system messages.
- Utilize Electron's native notification capabilities or in-app notification UI elements.

## Inter-Service Communication

- Within the Electron Main process, services can communicate directly via JavaScript module imports and function calls.
- Communication between the Electron Renderer process (Frontend UI) and these Main process services is handled via Electron's Inter-Process Communication (IPC) mechanisms (`ipcMain` and `ipcRenderer`).
- If Python processes are used (e.g., for ML), communication between Node.js and Python will use standard IPC methods like standard I/O pipes or a local messaging queue (e.g., ZeroMQ if more complex interaction is needed).

These backend services work together to provide the core functionality of CherryBomb, ensuring that data is handled efficiently, securely, and intelligently on the user's local machine.
