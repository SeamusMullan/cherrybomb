# Sequence Diagrams

This document provides sequence diagrams illustrating the key flows and interactions between components in the CherryBomb system.

## User Authentication Flow

```mermaid
sequenceDiagram
    participant User
    participant UI as User Interface
    participant Auth as Authentication Service
    participant DB as Database
    participant Email as Email Service
    
    User->>UI: Enter credentials
    UI->>Auth: login(username, password)
    Auth->>DB: Query user record
    DB->>Auth: Return user data
    
    alt Valid credentials
        Auth->>Auth: Generate JWT token
        Auth->>DB: Log authentication event
        Auth->>UI: Return token & user info
        UI->>UI: Store token locally
        UI->>User: Show dashboard
    else Invalid credentials
        Auth->>UI: Authentication failed
        UI->>User: Show error message
    end
    
    opt Password reset
        User->>UI: Request password reset
        UI->>Auth: resetPassword(email)
        Auth->>DB: Flag account for reset
        Auth->>Auth: Generate reset token
        Auth->>Email: Send reset email
        Email->>User: Deliver reset link
        User->>UI: Open reset link
        UI->>Auth: validateResetToken(token)
        Auth->>UI: Token valid
        User->>UI: Enter new password
        UI->>Auth: updatePassword(token, newPassword)
        Auth->>DB: Update password hash
        Auth->>UI: Password updated
        UI->>User: Show success message
    end
```

## Data Collection Flow

```mermaid
sequenceDiagram
    participant User
    participant UI as User Interface
    participant DC as Data Collection Service
    participant PA as Platform Adapter
    participant API as Social Media API
    participant DS as Data Storage Service
    participant Notify as Notification Service
    
    User->>UI: Select accounts to scrape
    User->>UI: Configure collection parameters
    UI->>DC: initiateCollection(accounts, params)
    
    DC->>DC: Create collection job
    DC->>UI: Return job ID
    
    loop For each platform
        DC->>PA: Authenticate(credentials)
        PA->>API: OAuth flow
        API->>PA: Return access token
        PA->>DC: Authentication success
        
        loop For each account
            DC->>PA: collectData(account, parameters)
            PA->>API: API requests with pagination
            API->>PA: Return data chunks
            PA->>DC: Process and normalize data
            DC->>DS: Store raw data
            DC->>UI: Update progress (websocket)
        end
    end
    
    DC->>DS: Finalize dataset
    DC->>DC: Update job status to complete
    DC->>Notify: Create completion notification
    Notify->>User: Send notification
    DC->>UI: Collection complete (websocket)
    UI->>User: Show completion notification
```

## Content Analysis & Prediction Flow

```mermaid
sequenceDiagram
    participant User
    participant UI as User Interface
    participant DP as Draft Post Component
    participant FE as Feature Extractor
    participant PES as Prediction Engine Service
    participant ML as ML Service
    participant DS as Data Service
    
    User->>UI: Create draft content
    User->>UI: Request performance prediction
    UI->>DP: prepareDraft(content)
    DP->>DP: Format and validate
    
    DP->>FE: extractFeatures(draft)
    
    alt Content has images
        FE->>FE: processImageFeatures()
    end
    
    alt Content has video
        FE->>FE: processVideoFeatures()
    end
    
    alt Content has text
        FE->>FE: processTextFeatures()
    end
    
    FE->>DP: Return features
    DP->>PES: requestPrediction(features)
    
    PES->>DS: getRelevantTrainingData()
    DS->>PES: Return historical data
    
    PES->>ML: predictMetrics(features, historicalData)
    ML->>ML: Apply prediction models
    ML->>PES: Return predicted metrics
    
    PES->>PES: Calculate confidence scores
    PES->>PES: Generate optimization suggestions
    
    PES->>DP: Return predictions and suggestions
    DP->>UI: Update prediction display
    UI->>User: Show predicted performance
    
    opt Optimize content
        User->>UI: Select suggestion to apply
        UI->>DP: applySuggestion(suggestionId)
        DP->>DP: Modify draft
        
        DP->>FE: extractFeatures(updatedDraft)
        FE->>DP: Return updated features
        DP->>PES: requestPrediction(updatedFeatures)
        PES->>ML: predictMetrics(updatedFeatures, historicalData)
        ML->>PES: Return updated predictions
        PES->>DP: Return updated predictions
        DP->>UI: Update prediction display
        UI->>User: Show improved prediction
    end
```

## Dataset Creation & Analysis Flow

```mermaid
sequenceDiagram
    participant User
    participant UI as User Interface
    participant PM as Project Manager
    participant DM as Dataset Manager
    participant DC as Data Collector
    participant DS as Data Storage
    participant AS as Analytics Service
    
    User->>UI: Create new project
    UI->>PM: createProject(projectInfo)
    PM->>DS: Save project details
    DS->>PM: Confirm creation
    PM->>UI: Project created
    
    User->>UI: Create dataset in project
    UI->>DM: createDataset(datasetInfo)
    DM->>DS: Initialize dataset
    DS->>DM: Return dataset ID
    DM->>UI: Dataset created
    
    User->>UI: Configure data sources
    UI->>DM: addDataSources(datasetId, sources)
    DM->>DS: Update dataset config
    DS->>DM: Confirm update
    DM->>UI: Sources added
    
    User->>UI: Start data collection
    UI->>DC: startCollection(datasetId)
    DC->>DC: Create collection job
    DC->>UI: Return job ID
    
    loop Until collection complete
        DC->>DC: Execute collection tasks
        DC->>DS: Store collected data
        DC->>UI: Update progress (websocket)
    end
    
    DC->>DM: Collection complete
    DM->>DS: Finalize dataset
    DM->>UI: Dataset ready
    
    User->>UI: Request analysis
    UI->>AS: analyzeDataset(datasetId)
    AS->>DS: Retrieve dataset
    DS->>AS: Return dataset
    
    AS->>AS: Process analytics
    AS->>DS: Store analytics results
    AS->>UI: Analysis complete
    
    UI->>User: Show analysis dashboard
```

## Model Training & Improvement Flow

```mermaid
sequenceDiagram
    participant User
    participant UI as User Interface
    participant MM as Model Manager
    participant MT as Model Trainer
    participant ME as Model Evaluator
    participant DS as Data Service
    
    User->>UI: Request model training
    UI->>MM: trainModel(datasetId, config)
    
    MM->>DS: getTrainingData(datasetId)
    DS->>MM: Return dataset
    
    MM->>MT: initTraining(dataset, config)
    MT->>MT: Preprocess data
    MT->>MT: Split training/validation/test
    
    loop For each epoch
        MT->>MT: Train iteration
        MT->>MT: Validate results
        MT->>UI: Update progress (websocket)
    end
    
    MT->>ME: evaluateModel(model, testData)
    ME->>ME: Run evaluation metrics
    ME->>MT: Return evaluation results
    
    MT->>MM: finalizeModel(model, evaluation)
    MM->>DS: saveModel(model)
    DS->>MM: Confirm saved
    
    MM->>UI: Training complete
    UI->>User: Show model performance
    
    opt Improve model
        User->>UI: Request model improvement
        UI->>MM: improveModel(modelId, feedback)
        MM->>DS: getAdditionalData(feedback)
        DS->>MM: Return new data
        
        MM->>MT: finetuneModel(model, newData)
        MT->>ME: evaluateModel(finetuned, testData)
        ME->>MT: Return new evaluation
        
        MT->>MM: updateModel(finetuned, evaluation)
        MM->>DS: saveModel(finetuned)
        DS->>MM: Confirm update
        
        MM->>UI: Model improved
        UI->>User: Show improved performance
    end
```

## Content Calendar Workflow

```mermaid
sequenceDiagram
    participant User
    participant UI as User Interface
    participant CP as Content Planner
    participant PE as Prediction Engine
    participant ML as ML Service
    participant Cal as Calendar Service
    
    User->>UI: Open content calendar
    UI->>Cal: getCalendarItems(dateRange)
    Cal->>UI: Return scheduled content
    UI->>User: Display calendar
    
    User->>UI: Create content draft
    UI->>PE: predictPerformance(draft)
    PE->>ML: getPrediction(draft)
    ML->>PE: Return prediction
    PE->>UI: Return prediction and best time
    
    User->>UI: Schedule content
    UI->>CP: scheduleContent(content, date)
    CP->>Cal: addCalendarItem(content, date)
    Cal->>CP: Confirm scheduled
    CP->>UI: Content scheduled
    UI->>User: Update calendar view
    
    opt Get optimal schedule
        User->>UI: Request optimal schedule
        UI->>CP: optimizeSchedule(contentItems)
        CP->>PE: getOptimalTimes(contentItems)
        PE->>ML: analyzeHistoricalEngagement()
        ML->>PE: Return best posting times
        PE->>CP: Return optimized schedule
        CP->>UI: Show optimized calendar
        UI->>User: Display recommendation
    end
    
    opt Publish content
        User->>UI: Request publish
        UI->>CP: publishContent(contentId)
        CP->>CP: Prepare for publishing
        CP->>Cal: updateStatus(contentId, "publishing")
        
        alt Publishing success
            CP->>Cal: updateStatus(contentId, "published")
            CP->>UI: Publish successful
            UI->>User: Show success message
        else Publishing failed
            CP->>Cal: updateStatus(contentId, "failed")
            CP->>UI: Publish failed
            UI->>User: Show error message
        end
    end
```

These sequence diagrams illustrate the key interactions between components in the CherryBomb system, providing a clear understanding of the data flows and user journeys throughout the application.
