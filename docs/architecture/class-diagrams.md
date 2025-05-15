# Class Diagrams

This document provides class diagrams for the major components of the CherryBomb system, highlighting the object-oriented architecture and relationships between classes.

## Core Domain Model

```mermaid
classDiagram
    class User {
        -String userId
        -String username
        -String email
        -Date createdAt
        -List~Platform~ platforms
        +authenticate()
        +updateProfile()
        +getProjects()
    }
    
    class Project {
        -String projectId
        -String name
        -String description
        -Date createdAt
        -Date updatedAt
        -User owner
        -List~Dataset~ datasets
        +createDataset()
        +getInsights()
        +exportData()
    }
    
    class Dataset {
        -String datasetId
        -String name
        -Platform platform
        -Date createdAt
        -Date lastUpdated
        -List~Account~ accounts
        -DatasetStatus status
        +addAccount()
        +updateData()
        +analyze()
        +createBackup()
    }
    
    class Account {
        -String accountId
        -String username
        -Platform platform
        -Map~String,Object~ metadata
        -List~Post~ posts
        -List~AccountMetric~ metrics
        +scrapeData()
        +getStats()
        +getPostsByDate()
    }
    
    class Post {
        -String postId
        -String contentText
        -Date postedAt
        -ContentType type
        -List~String~ hashtags
        -List~Media~ media
        -List~Engagement~ engagements
        -List~Metric~ metrics
        +analyze()
        +predictPerformance()
        +getEngagementRate()
    }
    
    class Media {
        -String mediaId
        -MediaType type
        -String url
        -Integer duration
        -Map~String,Object~ features
        +extractFeatures()
        +getThumbnail()
    }
    
    class Engagement {
        -String engagementId
        -Post post
        -Integer likes
        -Integer comments
        -Integer shares
        -Integer saves
        -Date measuredAt
        +calculateRate()
        +compareToAverage()
    }
    
    class Metric {
        -String metricId
        -String name
        -Float value
        -Date measuredAt
        -MetricType type
        +normalize()
        +getHistoricalTrend()
    }
    
    class Prediction {
        -String predictionId
        -Post draftPost
        -Date createdAt
        -Map~String,Float~ predictedMetrics
        -Float confidenceScore
        -List~String~ suggestions
        +compareToActual()
        +getSuggestions()
        +recalculate()
    }
    
    class Platform {
        <<enumeration>>
        INSTAGRAM
        TIKTOK
        YOUTUBE
        TWITTER
        FACEBOOK
        LINKEDIN
    }
    
    class ContentType {
        <<enumeration>>
        TEXT
        IMAGE
        VIDEO
        CAROUSEL
        STORY
        REEL
    }
    
    class MediaType {
        <<enumeration>>
        IMAGE
        VIDEO
        AUDIO
        DOCUMENT
    }
    
    class MetricType {
        <<enumeration>>
        ENGAGEMENT
        REACH
        IMPRESSION
        DEMOGRAPHIC
        SENTIMENT
    }
    
    class DatasetStatus {
        <<enumeration>>
        INITIALIZING
        COLLECTING
        PROCESSING
        READY
        ERROR
    }
    
    User "1" --> "*" Project : owns
    Project "1" --> "*" Dataset : contains
    Dataset "1" --> "*" Account : includes
    Account "1" --> "*" Post : contains
    Post "1" --> "*" Media : has
    Post "1" --> "*" Engagement : receives
    Post "1" --> "*" Metric : measures
    Post "1" --> "*" Prediction : forecasts
```

## Service Layer

```mermaid
classDiagram
    class AuthService {
        +login(username, password)
        +register(userInfo)
        +verifyToken(token)
        +refreshToken(refreshToken)
        +logout(userId)
        +resetPassword(email)
    }
    
    class DataCollectionService {
        +collectFromAccount(accountInfo)
        +scheduleScraping(schedule)
        +getCollectionStatus(jobId)
        +cancelCollection(jobId)
        +retryFailedCollection(jobId)
        +validateCredentials(platformAuth)
    }
    
    class DataStorageService {
        +saveDataset(dataset)
        +getDataset(datasetId)
        +updateDataset(datasetId, updates)
        +deleteDataset(datasetId)
        +backupDataset(datasetId)
        +restoreDataset(backupId)
        +getDatasetVersions(datasetId)
    }
    
    class AnalyticsService {
        +analyzeDataset(datasetId)
        +identifyTrends(datasetId)
        +compareDatasets(datasetIds)
        +getInsights(datasetId)
        +calculateMetrics(datasetId)
        +generateReport(datasetId, template)
    }
    
    class MachineLearningService {
        +trainModel(datasetId, modelConfig)
        +predictPerformance(draftContent, modelId)
        +evaluateModel(modelId)
        +getModelAccuracy(modelId)
        +improveModel(modelId, feedback)
        +getOptimizationSuggestions(draftContent)
    }
    
    class PlatformAdapter {
        <<interface>>
        +authenticate(credentials)
        +collectData(parameters)
        +getRateLimits()
        +handleError(error)
    }
    
    class InstagramAdapter {
        +authenticate(credentials)
        +collectData(parameters)
        +getRateLimits()
        +handleError(error)
        -parseGraphQLResponse(response)
    }
    
    class TikTokAdapter {
        +authenticate(credentials)
        +collectData(parameters)
        +getRateLimits()
        +handleError(error)
        -parseVideoMetadata(metadata)
    }
    
    class NotificationService {
        +createNotification(userId, message)
        +markAsRead(notificationId)
        +getUnreadNotifications(userId)
        +subscribeToEvents(userId, eventTypes)
        +unsubscribeFromEvents(userId, eventTypes)
    }
    
    class ReportingService {
        +generateReport(datasetId, template)
        +scheduleReport(reportConfig)
        +exportReportToPDF(reportId)
        +shareReport(reportId, recipients)
        +getReportHistory(userId)
    }
    
    class ContentCalendarService {
        +createContentItem(projectId, contentData)
        +scheduleContent(contentId, date)
        +getCalendarItems(projectId, dateRange)
        +updateContentItem(contentId, updates)
        +getPublishStatus(contentId)
    }
    
    PlatformAdapter <|-- InstagramAdapter
    PlatformAdapter <|-- TikTokAdapter
    
    DataCollectionService --> PlatformAdapter : uses
    DataCollectionService --> DataStorageService : stores data via
    AnalyticsService --> DataStorageService : retrieves data from
    MachineLearningService --> DataStorageService : uses data from
    ReportingService --> AnalyticsService : uses insights from
    ContentCalendarService --> MachineLearningService : gets predictions from
```

## Frontend Component Classes

```mermaid
classDiagram
    class Application {
        -AuthManager authManager
        -NavigationManager navManager
        -ThemeManager themeManager
        -StoreManager storeManager
        +initialize()
        +handleError(error)
        +updateSettings(settings)
    }
    
    class AuthManager {
        -String currentUserId
        -String token
        -AuthService authService
        +login(credentials)
        +logout()
        +checkAuthStatus()
        +refreshSession()
    }
    
    class StoreManager {
        -LocalStore localStore
        -RemoteStore remoteStore
        -SyncManager syncManager
        +getData(query)
        +saveData(data)
        +syncData()
        +clearCache()
    }
    
    class DashboardComponent {
        -ProjectsService projectsService
        -List~Project~ projects
        -Project activeProject
        +loadProjects()
        +createProject(projectData)
        +selectProject(projectId)
        +getProjectInsights(projectId)
    }
    
    class DataExplorerComponent {
        -DatasetService datasetService
        -Dataset currentDataset
        -FilterManager filterManager
        -VisualizationManager vizManager
        +loadDataset(datasetId)
        +applyFilters(filters)
        +exportData(format)
        +createVisualization(config)
    }
    
    class ContentPlannerComponent {
        -ContentCalendarService calendarService
        -MachineLearningService mlService
        -Date selectedDate
        -Map~Date,List~ContentItem~~ calendarItems
        +loadCalendar(dateRange)
        +createContent(contentData)
        +predictPerformance(draftContent)
        +scheduleContent(contentId, date)
    }
    
    class AccountManagerComponent {
        -PlatformService platformService
        -List~PlatformAccount~ connectedAccounts
        +connectAccount(platform, credentials)
        +disconnectAccount(accountId)
        +refreshAccountData(accountId)
        +getAccountMetrics(accountId)
    }
    
    class VisualizationComponent {
        -ChartRenderer chartRenderer
        -DataTransformer dataTransformer
        -Map~String,Object~ chartConfig
        -Map~String,Object~ chartData
        +renderChart()
        +updateData(newData)
        +exportChart(format)
        +changeChartType(type)
    }
    
    class PredictionComponent {
        -MachineLearningService mlService
        -ContentDraft contentDraft
        -Prediction prediction
        -List~String~ suggestions
        +createDraft(contentData)
        +getPrediction()
        +getOptimizationSuggestions()
        +applyOptimization(suggestionId)
    }
    
    Application --> AuthManager : manages
    Application --> StoreManager : manages
    Application --> DashboardComponent : contains
    Application --> DataExplorerComponent : contains
    Application --> ContentPlannerComponent : contains
    Application --> AccountManagerComponent : contains
    
    DataExplorerComponent --> VisualizationComponent : uses
    ContentPlannerComponent --> PredictionComponent : uses
```

## Machine Learning Classes

```mermaid
classDiagram
    class ModelManager {
        -Map~String,PredictionModel~ models
        -ModelTrainer trainer
        -ModelEvaluator evaluator
        -FeatureExtractor featureExtractor
        +loadModel(modelId)
        +trainModel(datasetId, config)
        +evaluateModel(modelId, testData)
        +getPrediction(modelId, inputData)
    }
    
    class PredictionModel {
        <<interface>>
        +train(trainingData)
        +predict(inputData)
        +evaluate(testData)
        +getMetadata()
        +serialize()
        +deserialize(data)
    }
    
    class EngagementPredictionModel {
        -String modelId
        -Date trainedDate
        -Map~String,Object~ parameters
        -Float accuracy
        -String platform
        -ContentType contentType
        +train(trainingData)
        +predict(inputData)
        +evaluate(testData)
        +getMetadata()
    }
    
    class TrendDetectionModel {
        -String modelId
        -Date trainedDate
        -Map~String,Object~ parameters
        -List~Trend~ detectedTrends
        -String platform
        +train(trainingData)
        +predictTrends(inputData)
        +evaluate(testData)
        +getMetadata()
    }
    
    class SentimentAnalysisModel {
        -String modelId
        -Date trainedDate
        -Map~String,Object~ parameters
        -Float accuracy
        -Language language
        +train(trainingData)
        +analyzeSentiment(text)
        +evaluate(testData)
        +getMetadata()
    }
    
    class FeatureExtractor {
        -List~FeatureExtractorPlugin~ plugins
        +extractFeatures(content)
        +normalizeFeatures(features)
        +selectTopFeatures(features, n)
        +registerPlugin(plugin)
    }
    
    class ImageFeatureExtractor {
        +extractFeatures(image)
        +detectObjects(image)
        +analyzePalette(image)
        +getCompositionMetrics(image)
    }
    
    class TextFeatureExtractor {
        +extractFeatures(text)
        +tokenize(text)
        +extractEntities(text)
        +detectLanguage(text)
        +getReadabilityScore(text)
    }
    
    class VideoFeatureExtractor {
        +extractFeatures(video)
        +analyzeScenes(video)
        +extractAudioFeatures(video)
        +getMontageMetrics(video)
    }
    
    class ModelTrainer {
        -TrainingConfig config
        -DatasetService datasetService
        -MetricsCollector metricsCollector
        +prepareTrainingData(datasetId)
        +trainModel(modelType, trainingData)
        +validateModel(model, validationData)
        +saveModel(model)
    }
    
    class ModelEvaluator {
        -List~MetricCalculator~ metricCalculators
        +evaluatePerformance(model, testData)
        +compareModels(modelIds, testData)
        +generateReport(evaluationResults)
        +calculateConfidenceIntervals(predictions)
    }
    
    PredictionModel <|-- EngagementPredictionModel
    PredictionModel <|-- TrendDetectionModel
    PredictionModel <|-- SentimentAnalysisModel
    
    FeatureExtractor <|-- ImageFeatureExtractor
    FeatureExtractor <|-- TextFeatureExtractor
    FeatureExtractor <|-- VideoFeatureExtractor
    
    ModelManager --> PredictionModel : manages
    ModelManager --> FeatureExtractor : uses
    ModelManager --> ModelTrainer : uses
    ModelManager --> ModelEvaluator : uses
```

These class diagrams illustrate the main components and their relationships in the CherryBomb system, providing a blueprint for implementation while maintaining flexibility for future development.
