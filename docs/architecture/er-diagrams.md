# Entity-Relationship Diagrams

This document provides detailed entity-relationship diagrams for the CherryBomb database structure, illustrating how data is organized and related within the system.

## Core Data Model

```mermaid
erDiagram
    USER ||--o{ PROJECT : creates
    USER ||--o{ API_KEY : owns
    USER ||--o{ PLATFORM_AUTH : connects
    
    PROJECT ||--o{ DATASET : contains
    PROJECT ||--o{ CONTENT_CALENDAR : has
    
    DATASET ||--o{ ACCOUNT : includes
    DATASET ||--o{ DATASET_METRIC : measures
    
    ACCOUNT ||--o{ POST : contains
    ACCOUNT ||--o{ ACCOUNT_METRIC : measures
    ACCOUNT ||--o{ AUDIENCE : has
    
    POST ||--o{ MEDIA : includes
    POST ||--o{ POST_METRIC : measures
    POST ||--o{ COMMENT : receives
    POST ||--o{ HASHTAG : uses
    
    POST ||--o{ PREDICTION : forecasts
    DRAFT_POST ||--o{ PREDICTION : generates
    
    CONTENT_CALENDAR ||--o{ CALENDAR_ITEM : contains
    CALENDAR_ITEM ||--o{ DRAFT_POST : schedules
    
    MODEL ||--o{ PREDICTION : produces
    DATASET ||--o{ MODEL : trains
    
    USER {
        string user_id PK
        string username
        string email
        string password_hash
        datetime created_at
        datetime last_login
        boolean is_active
        string subscription_tier
    }
    
    PROJECT {
        string project_id PK
        string user_id FK
        string name
        string description
        datetime created_at
        datetime updated_at
        boolean is_public
        string thumbnail_url
    }
    
    API_KEY {
        string key_id PK
        string user_id FK
        string key_value
        datetime created_at
        datetime expires_at
        string[] permissions
        boolean is_active
    }
    
    PLATFORM_AUTH {
        string auth_id PK
        string user_id FK
        string platform
        string access_token
        string refresh_token
        datetime token_expiry
        boolean is_active
        json metadata
    }
    
    DATASET {
        string dataset_id PK
        string project_id FK
        string name
        string description
        string platform
        datetime created_at
        datetime updated_at
        int records_count
        datetime start_date
        datetime end_date
        string status
        boolean is_processing
    }
    
    ACCOUNT {
        string account_id PK
        string dataset_id FK
        string platform_id
        string username
        string display_name
        string profile_url
        string avatar_url
        int followers_count
        int following_count
        datetime last_scraped
        json metadata
    }
    
    AUDIENCE {
        string audience_id PK
        string account_id FK
        json demographics
        json locations
        json interests
        datetime measured_at
        float engagement_rate
        int active_followers
    }
    
    POST {
        string post_id PK
        string account_id FK
        string platform_id
        datetime posted_at
        string content_type
        string text_content
        string url
        boolean is_sponsored
        boolean is_reply
        json metadata
    }
    
    MEDIA {
        string media_id PK
        string post_id FK
        string media_type
        string url
        int duration
        int width
        int height
        string thumbnail_url
        json features
        json metadata
    }
    
    COMMENT {
        string comment_id PK
        string post_id FK
        string author_id
        string author_name
        datetime commented_at
        string text_content
        int likes_count
        boolean is_reply
        string parent_id
        json sentiment
    }
    
    HASHTAG {
        string hashtag_id PK
        string post_id FK
        string tag_text
        int position
    }
    
    POST_METRIC {
        string metric_id PK
        string post_id FK
        string metric_name
        float value
        datetime measured_at
        string unit
        json historical_values
    }
    
    ACCOUNT_METRIC {
        string metric_id PK
        string account_id FK
        string metric_name
        float value
        datetime measured_at
        string unit
        json historical_values
    }
    
    DATASET_METRIC {
        string metric_id PK
        string dataset_id FK
        string metric_name
        float value
        datetime measured_at
        string unit
        json historical_values
    }
    
    DRAFT_POST {
        string draft_id PK
        string project_id FK
        string content_type
        string text_content
        datetime created_at
        datetime updated_at
        string status
        json media_references
        json metadata
    }
    
    PREDICTION {
        string prediction_id PK
        string post_id FK "nullable"
        string draft_id FK "nullable"
        string model_id FK
        datetime created_at
        float predicted_likes
        float predicted_comments
        float predicted_shares
        float predicted_engagement_rate
        float confidence_score
        json suggested_improvements
        json prediction_metadata
    }
    
    CONTENT_CALENDAR {
        string calendar_id PK
        string project_id FK
        string name
        string description
        datetime created_at
        datetime updated_at
        string timezone
        json settings
    }
    
    CALENDAR_ITEM {
        string item_id PK
        string calendar_id FK
        string draft_id FK "nullable"
        string title
        datetime scheduled_at
        string status
        boolean is_recurring
        string recurrence_pattern
        string platform
        json publishing_settings
    }
    
    MODEL {
        string model_id PK
        string dataset_id FK
        string model_type
        string name
        datetime created_at
        datetime updated_at
        boolean is_active
        float accuracy
        json hyperparameters
        json features
        json evaluation_metrics
    }
```

## Analytics Data Model

```mermaid
erDiagram
    INSIGHT ||--o{ INSIGHT_METRIC : contains
    INSIGHT ||--o{ RECOMMENDATION : generates
    TREND ||--o{ TREND_DATAPOINT : contains
    REPORT ||--o{ REPORT_SECTION : contains
    BENCHMARK ||--o{ BENCHMARK_METRIC : defines
    
    DATASET ||--o{ INSIGHT : analyzes
    DATASET ||--o{ TREND : discovers
    PROJECT ||--o{ REPORT : generates
    ACCOUNT ||--o{ BENCHMARK : measures_against
    
    INSIGHT {
        string insight_id PK
        string dataset_id FK
        string title
        string description
        datetime discovered_at
        float confidence_score
        string insight_type
        json supporting_data
        boolean is_actionable
    }
    
    INSIGHT_METRIC {
        string metric_id PK
        string insight_id FK
        string name
        float value
        string unit
        float change_percent
        string change_direction
        json historical_values
    }
    
    RECOMMENDATION {
        string recommendation_id PK
        string insight_id FK
        string title
        string description
        float expected_impact
        string impact_area
        datetime created_at
        boolean is_implemented
        datetime implemented_at
        json results
    }
    
    TREND {
        string trend_id PK
        string dataset_id FK
        string name
        string description
        string trend_type
        datetime discovered_at
        datetime start_date
        datetime end_date
        float strength
        float confidence
        json metadata
    }
    
    TREND_DATAPOINT {
        string datapoint_id PK
        string trend_id FK
        datetime timestamp
        float value
        json metadata
    }
    
    REPORT {
        string report_id PK
        string project_id FK
        string name
        string description
        datetime created_at
        datetime time_period_start
        datetime time_period_end
        string status
        string format
        string access_url
        json settings
    }
    
    REPORT_SECTION {
        string section_id PK
        string report_id FK
        string title
        int order_index
        string content_type
        json content
        json visualization_config
    }
    
    BENCHMARK {
        string benchmark_id PK
        string account_id FK
        string name
        string description
        string category
        datetime created_at
        datetime period_start
        datetime period_end
        float overall_score
        json comparison_accounts
    }
    
    BENCHMARK_METRIC {
        string metric_id PK
        string benchmark_id FK
        string name
        float account_value
        float industry_average
        float top_performer_value
        float percentile
        string unit
        json breakdown
    }
```

## Machine Learning Data Model

```mermaid
erDiagram
    MODEL ||--o{ MODEL_VERSION : has
    MODEL_VERSION ||--o{ TRAINING_RUN : created_by
    TRAINING_RUN ||--o{ TRAINING_METRIC : tracks
    DATASET ||--o{ FEATURE_SET : extracts
    FEATURE_SET ||--o{ FEATURE : contains
    MODEL_VERSION ||--o{ PREDICTION_LOG : generates
    MODEL_VERSION ||--o{ MODEL_METRIC : evaluates
    
    MODEL {
        string model_id PK
        string name
        string description
        string model_type
        string target_platform
        string content_type
        datetime created_at
        boolean is_active
        string created_by
        json metadata
    }
    
    MODEL_VERSION {
        string version_id PK
        string model_id FK
        string version_number
        datetime created_at
        float accuracy
        float precision
        float recall
        float f1_score
        string status
        string deployment_environment
        string artifact_location
    }
    
    TRAINING_RUN {
        string run_id PK
        string version_id FK
        datetime started_at
        datetime completed_at
        string status
        string dataset_id
        int epochs
        int samples_count
        json hyperparameters
        json environment_info
    }
    
    TRAINING_METRIC {
        string metric_id PK
        string run_id FK
        string name
        float value
        int epoch
        string phase
        datetime recorded_at
        json metadata
    }
    
    FEATURE_SET {
        string feature_set_id PK
        string dataset_id FK
        string name
        string description
        datetime created_at
        int features_count
        string extraction_method
        json metadata
    }
    
    FEATURE {
        string feature_id PK
        string feature_set_id FK
        string name
        string data_type
        float importance_score
        boolean is_selected
        json statistics
        json metadata
    }
    
    PREDICTION_LOG {
        string log_id PK
        string version_id FK
        datetime created_at
        string input_hash
        json input_data
        json prediction_result
        float confidence_score
        boolean is_feedback_provided
        json actual_result
        float error_margin
    }
    
    MODEL_METRIC {
        string metric_id PK
        string version_id FK
        string name
        float value
        datetime calculated_at
        string calculation_method
        json metadata
    }
```

## System Configuration Data Model

```mermaid
erDiagram
    SYSTEM_CONFIG ||--o{ CONFIG_ENTRY : contains
    USER ||--o{ USER_PREFERENCE : has
    JOB ||--o{ JOB_LOG : records
    NOTIFICATION ||--o{ NOTIFICATION_RECIPIENT : targets
    
    SYSTEM_CONFIG {
        string config_id PK
        string name
        string description
        datetime created_at
        datetime updated_at
        string environment
        boolean is_active
        string created_by
    }
    
    CONFIG_ENTRY {
        string entry_id PK
        string config_id FK
        string key
        string value
        string data_type
        boolean is_encrypted
        boolean is_editable
        string description
    }
    
    USER_PREFERENCE {
        string preference_id PK
        string user_id FK
        string category
        string key
        string value
        datetime updated_at
    }
    
    JOB {
        string job_id PK
        string type
        string status
        datetime created_at
        datetime started_at
        datetime completed_at
        string created_by
        json parameters
        float progress
        string error_message
    }
    
    JOB_LOG {
        string log_id PK
        string job_id FK
        datetime timestamp
        string level
        string message
        json context
    }
    
    NOTIFICATION {
        string notification_id PK
        string type
        string title
        string message
        datetime created_at
        datetime expires_at
        string action_url
        boolean is_system
        string created_by
        json metadata
    }
    
    NOTIFICATION_RECIPIENT {
        string recipient_id PK
        string notification_id FK
        string user_id
        boolean is_read
        datetime read_at
        boolean is_dismissed
        datetime dismissed_at
    }
```

These entity-relationship diagrams provide a comprehensive view of the data model for CherryBomb, illustrating how different entities relate to each other and what attributes they contain. This structure supports all the core functionality while maintaining flexibility for future expansion.
