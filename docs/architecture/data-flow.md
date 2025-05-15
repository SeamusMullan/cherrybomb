# Data Flow Diagrams

This document illustrates the flow of data throughout the CherryBomb system, from initial collection to final presentation and prediction.

## Main Data Flow

```mermaid
flowchart TD
    User[User Input] --> Auth[Authentication]
    Auth --> SM[Social Media Account Selection]
    SM --> DC[Data Collection Service]
    
    DC --> Raw[Raw Data Repository]
    Raw --> Process[Data Processing Engine]
    Process --> Clean[Cleaned Dataset]
    
    Clean --> Storage[Data Storage Service]
    Storage --> Analysis[Analytics Service]
    Storage --> ML[Machine Learning Service]
    
    Analysis --> Insights[Insights Generation]
    ML --> Train[Model Training]
    ML --> Predict[Prediction Engine]
    
    Insights --> Viz[Data Visualization]
    Predict --> Forecast[Performance Forecasts]
    
    Viz --> UI[User Interface]
    Forecast --> UI
```

## Data Collection Flow

```mermaid
flowchart LR
    subgraph DataCollection[Data Collection Process]
        Init[Initialize Collection] --> Auth[Platform Authentication]
        Auth --> Params[Set Collection Parameters]
        Params --> Schedule[Schedule Collection Jobs]
        Schedule --> Execute[Execute Collection]
        
        Execute --> API[API Collection]
        Execute --> Scrape[Web Scraping]
        
        API --> Parse[Parse API Responses]
        Scrape --> Extract[Extract Data from HTML]
        
        Parse --> Validate[Validate Data]
        Extract --> Validate
        
        Validate --> Transform[Transform to Standard Format]
        Transform --> Store[Store Raw Data]
    end
```

## Analytics Processing Flow

```mermaid
flowchart TD
    Raw[Raw Dataset] --> Clean[Data Cleaning]
    Clean --> Enrich[Data Enrichment]
    Enrich --> Feature[Feature Extraction]
    
    Feature --> Split{Processing Path}
    Split -->|Trend Analysis| Group[Group & Aggregate]
    Split -->|ML Training| Norm[Normalize Data]
    
    Group --> Trend[Trend Identification]
    Group --> Corr[Correlation Analysis]
    Group --> Metric[Metric Calculation]
    
    Trend --> Insight[Insight Generation]
    Corr --> Insight
    Metric --> Insight
    
    Norm --> Split2[Split Data]
    Split2 --> Train[Training Set]
    Split2 --> Val[Validation Set]
    Split2 --> Test[Test Set]
    
    Train --> Model[Model Training]
    Val --> Tune[Hyperparameter Tuning]
    
    Model --> Tune
    Tune --> Eval[Model Evaluation]
    Test --> Eval
    
    Eval --> Deploy[Deploy Model]
```

## Content Prediction Flow

```mermaid
sequenceDiagram
    participant User
    participant UI as User Interface
    participant PE as Prediction Engine
    participant ML as ML Models
    participant DS as Data Store
    
    User->>UI: Draft new content
    User->>UI: Request prediction
    UI->>PE: Send content draft & parameters
    
    PE->>DS: Retrieve historical data
    DS->>PE: Return relevant data
    
    PE->>PE: Extract content features
    PE->>ML: Request prediction with features
    
    ML->>ML: Apply prediction models
    ML->>PE: Return predicted metrics
    
    PE->>PE: Calculate confidence intervals
    PE->>PE: Generate suggestions
    
    PE->>UI: Return predictions & suggestions
    UI->>User: Display predicted performance
```

## Data Storage Architecture

```mermaid
erDiagram
    USER ||--o{ PROJECT : creates
    PROJECT ||--o{ DATASET : contains
    DATASET ||--o{ ACCOUNT : includes
    ACCOUNT ||--o{ POST : contains
    POST ||--o{ ENGAGEMENT : has
    POST ||--o{ MEDIA : includes
    POST ||--o{ METRIC : measures
    POST ||--o{ PREDICTION : forecasts
    
    USER {
        string user_id PK
        string username
        string email
        date created_at
        array platforms
    }
    
    PROJECT {
        string project_id PK
        string user_id FK
        string name
        string description
        date created_at
        date updated_at
    }
    
    DATASET {
        string dataset_id PK
        string project_id FK
        string name
        string platform
        date created_at
        date updated_at
        int record_count
        date start_date
        date end_date
    }
    
    ACCOUNT {
        string account_id PK
        string dataset_id FK
        string platform
        string username
        int follower_count
        int following_count
        array metrics
    }
    
    POST {
        string post_id PK
        string account_id FK
        date posted_at
        string content_type
        string text_content
        array hashtags
        array mentions
    }
    
    ENGAGEMENT {
        string engagement_id PK
        string post_id FK
        int likes
        int comments
        int shares
        int saves
        float engagement_rate
    }
    
    MEDIA {
        string media_id PK
        string post_id FK
        string media_type
        string url
        int duration
        array features
    }
    
    METRIC {
        string metric_id PK
        string post_id FK
        string metric_name
        float value
        date measured_at
    }
    
    PREDICTION {
        string prediction_id PK
        string post_id FK
        date created_at
        int predicted_likes
        int predicted_comments
        int predicted_shares
        float confidence_score
    }
```

These diagrams provide a comprehensive overview of how data flows through the CherryBomb system, from collection and processing to analysis and prediction.
