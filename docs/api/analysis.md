# Analysis API

The Analysis API provides programmatic access to CherryBomb's analytics capabilities, allowing you to extract insights, generate reports, and perform custom analysis on your social media datasets.

## Overview

The Analysis API enables:

- Running predefined analysis operations on datasets
- Generating custom metrics and reports
- Exporting analysis results in various formats
- Scheduling and automating regular analysis tasks

## Dataset Analysis

### Run Dataset Analysis

```
POST /api/analysis/datasets/{datasetId}/analyze
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "analysisTypes": [
    "engagement",
    "content",
    "audience",
    "timing"
  ],
  "dateRange": {
    "start": "2025-01-01T00:00:00Z",
    "end": "2025-04-30T23:59:59Z"
  },
  "granularity": "daily",
  "filters": {
    "contentTypes": ["photo", "video", "carousel"],
    "accounts": ["account_12345", "account_67890"]
  }
}
```

**Response:**

```json
{
  "success": true,
  "analysisId": "anal_1234567890",
  "status": "processing",
  "estimatedCompletionTime": "2025-05-15T12:30:00Z"
}
```

### Get Analysis Status

```
GET /api/analysis/{analysisId}/status
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "analysisId": "anal_1234567890",
  "status": "completed",
  "progress": 100,
  "completedAt": "2025-05-15T12:25:30Z",
  "results": {
    "summaryUrl": "/api/analysis/anal_1234567890/summary",
    "detailedUrl": "/api/analysis/anal_1234567890/detailed",
    "exportFormats": ["json", "csv", "pdf"]
  }
}
```

### Get Analysis Summary

```
GET /api/analysis/{analysisId}/summary
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "analysisId": "anal_1234567890",
  "summary": {
    "totalPosts": 287,
    "averageEngagement": 3.4,
    "topPerformingContent": [
      {
        "postId": "post_12345",
        "platform": "instagram",
        "engagementRate": 8.7,
        "contentType": "carousel"
      },
      {
        "postId": "post_23456",
        "platform": "tiktok",
        "engagementRate": 7.2,
        "contentType": "video"
      }
    ],
    "engagementTrend": "increasing",
    "keyInsights": [
      "Video content outperforms static images by 43%",
      "Posting between 2PM-4PM generates 22% higher engagement",
      "User-generated content receives 31% more comments"
    ]
  }
}
```

### Get Detailed Analysis

```
GET /api/analysis/{analysisId}/detailed
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Query Parameters:**

```
section=engagement
includeRawData=false
format=json
```

**Response:**

```json
{
  "success": true,
  "analysisId": "anal_1234567890",
  "section": "engagement",
  "detailed": {
    "metrics": {
      "engagementRate": {
        "average": 3.4,
        "median": 2.8,
        "percentiles": {
          "25": 1.9,
          "75": 4.2,
          "90": 6.7
        },
        "trend": {
          "direction": "increasing",
          "changePercent": 12.5
        }
      },
      "likes": {
        "average": 342,
        "median": 287,
        "percentiles": {
          "25": 180,
          "75": 456,
          "90": 920
        }
      },
      "comments": {
        "average": 24,
        "median": 18,
        "percentiles": {
          "25": 9,
          "75": 36,
          "90": 78
        }
      }
    },
    "breakdowns": {
      "byContentType": [
        {
          "contentType": "photo",
          "count": 158,
          "averageEngagement": 2.7
        },
        {
          "contentType": "video",
          "count": 89,
          "averageEngagement": 4.1
        },
        {
          "contentType": "carousel",
          "count": 40,
          "averageEngagement": 3.8
        }
      ],
      "byDay": [
        {
          "day": "Monday",
          "averageEngagement": 3.1
        },
        {
          "day": "Tuesday",
          "averageEngagement": 3.0
        },
        {
          "day": "Wednesday",
          "averageEngagement": 3.5
        }
      ]
    }
  }
}
```

### Export Analysis

```
GET /api/analysis/{analysisId}/export
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Query Parameters:**

```
format=csv
sections=engagement,content,audience
```

**Response:**

Binary file download

## Content Analysis

### Analyze Specific Content

```
POST /api/analysis/content/{contentId}/analyze
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "analysisTypes": [
    "engagement",
    "audience",
    "sentiment",
    "visualAnalysis"
  ],
  "benchmarks": {
    "compareToAccount": true,
    "compareToSimilarContent": true
  }
}
```

**Response:**

```json
{
  "success": true,
  "contentId": "post_12345",
  "analysis": {
    "performance": {
      "engagementRate": 4.2,
      "accountAverage": 3.4,
      "percentileRank": 78,
      "benchmark": "+23% above account average"
    },
    "audience": {
      "reachedSegments": [
        {
          "segment": "18-24 Female",
          "percentage": 34
        },
        {
          "segment": "25-34 Female",
          "percentage": 28
        }
      ],
      "engagingSegments": [
        {
          "segment": "18-24 Female",
          "engagementRate": 5.1
        },
        {
          "segment": "25-34 Female",
          "engagementRate": 3.8
        }
      ]
    },
    "sentiment": {
      "overall": "positive",
      "score": 0.72,
      "commentSentiments": {
        "positive": 68,
        "neutral": 24,
        "negative": 8
      }
    },
    "visualAnalysis": {
      "dominantColors": ["#3a6ea5", "#c4d4e0"],
      "composition": "rule-of-thirds",
      "detectedElements": ["person", "outdoors", "water"],
      "brandConsistency": "high"
    }
  }
}
```

## Comparative Analysis

### Compare Accounts

```
POST /api/analysis/compare/accounts
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "accountIds": [
    "account_12345",
    "account_67890",
    "account_24680"
  ],
  "metrics": [
    "engagementRate",
    "followerGrowth",
    "postFrequency",
    "contentMix"
  ],
  "dateRange": {
    "start": "2025-01-01T00:00:00Z",
    "end": "2025-04-30T23:59:59Z"
  }
}
```

**Response:**

```json
{
  "success": true,
  "comparisonId": "comp_1234567890",
  "accounts": [
    {
      "accountId": "account_12345",
      "accountName": "BrandA",
      "metrics": {
        "engagementRate": {
          "value": 3.8,
          "rank": 2
        },
        "followerGrowth": {
          "value": 5.2,
          "rank": 1
        },
        "postFrequency": {
          "value": 4.5,
          "rank": 3
        },
        "contentMix": {
          "photo": 45,
          "video": 40,
          "carousel": 15
        }
      }
    },
    {
      "accountId": "account_67890",
      "accountName": "BrandB",
      "metrics": {
        "engagementRate": {
          "value": 4.1,
          "rank": 1
        },
        "followerGrowth": {
          "value": 3.7,
          "rank": 2
        },
        "postFrequency": {
          "value": 6.2,
          "rank": 1
        },
        "contentMix": {
          "photo": 30,
          "video": 60,
          "carousel": 10
        }
      }
    }
  ],
  "insights": [
    "BrandB has higher engagement despite posting more frequently",
    "BrandA leads in follower growth with less frequent posting",
    "Video content dominates BrandB's strategy while BrandA has a more balanced approach"
  ]
}
```

### Compare Time Periods

```
POST /api/analysis/compare/timeperiods
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "accountId": "account_12345",
  "periods": [
    {
      "name": "Pre-Campaign",
      "start": "2025-01-01T00:00:00Z",
      "end": "2025-02-28T23:59:59Z"
    },
    {
      "name": "Campaign",
      "start": "2025-03-01T00:00:00Z",
      "end": "2025-04-30T23:59:59Z"
    }
  ],
  "metrics": [
    "engagementRate",
    "followerGrowth",
    "impressions",
    "contentPerformance"
  ]
}
```

**Response:**

```json
{
  "success": true,
  "comparisonId": "comp_0987654321",
  "account": {
    "accountId": "account_12345",
    "accountName": "BrandA"
  },
  "periodComparison": [
    {
      "periodName": "Pre-Campaign",
      "metrics": {
        "engagementRate": 3.2,
        "followerGrowth": 2.8,
        "impressions": 45000,
        "contentPerformance": {
          "averageEngagement": 342,
          "topContentType": "photo"
        }
      }
    },
    {
      "periodName": "Campaign",
      "metrics": {
        "engagementRate": 4.7,
        "followerGrowth": 7.3,
        "impressions": 87000,
        "contentPerformance": {
          "averageEngagement": 587,
          "topContentType": "video"
        }
      }
    }
  ],
  "changes": {
    "engagementRate": {
      "absolute": 1.5,
      "percent": 46.9
    },
    "followerGrowth": {
      "absolute": 4.5,
      "percent": 160.7
    },
    "impressions": {
      "absolute": 42000,
      "percent": 93.3
    }
  },
  "insights": [
    "The campaign period showed significant improvements across all metrics",
    "Video content performed better during the campaign period",
    "Follower growth saw the most dramatic improvement at 160.7%"
  ]
}
```

## Trend Analysis

### Identify Trends

```
POST /api/analysis/trends/identify
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "datasetId": "dataset_12345",
  "trendTypes": [
    "content",
    "engagement",
    "hashtags",
    "topics"
  ],
  "parameters": {
    "minConfidence": 0.7,
    "timeframe": "last30days",
    "minGrowthRate": 10
  }
}
```

**Response:**

```json
{
  "success": true,
  "trends": {
    "content": [
      {
        "trend": "Short-form vertical video",
        "growthRate": 27.3,
        "confidence": 0.89,
        "stage": "growing"
      },
      {
        "trend": "User-generated content reposts",
        "growthRate": 18.5,
        "confidence": 0.74,
        "stage": "emerging"
      }
    ],
    "engagement": [
      {
        "trend": "Increased comment depth",
        "growthRate": 15.2,
        "confidence": 0.81,
        "stage": "growing"
      }
    ],
    "hashtags": [
      {
        "trend": "#sustainablefashion",
        "growthRate": 42.1,
        "confidence": 0.92,
        "stage": "growing"
      }
    ],
    "topics": [
      {
        "trend": "Product tutorials",
        "growthRate": 23.7,
        "confidence": 0.85,
        "stage": "growing"
      }
    ]
  },
  "relatedInsights": [
    "Tutorial content is driving 31% higher comment engagement",
    "Sustainability-focused content performs better with 25-34 demographic",
    "User-generated content receives 24% more shares than brand-created content"
  ]
}
```

### Track Trend Development

```
GET /api/analysis/trends/{trendId}/track
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Query Parameters:**

```
timeframe=last90days
granularity=weekly
```

**Response:**

```json
{
  "success": true,
  "trend": {
    "id": "trend_12345",
    "name": "Short-form vertical video",
    "category": "content",
    "firstDetected": "2025-02-15T00:00:00Z"
  },
  "development": {
    "stages": [
      {
        "stage": "emerging",
        "start": "2025-02-15T00:00:00Z",
        "end": "2025-03-01T00:00:00Z",
        "averageGrowthRate": 12.3
      },
      {
        "stage": "growing",
        "start": "2025-03-01T00:00:00Z",
        "end": "2025-04-15T00:00:00Z",
        "averageGrowthRate": 27.8
      },
      {
        "stage": "peaking",
        "start": "2025-04-15T00:00:00Z",
        "end": null,
        "averageGrowthRate": 8.2
      }
    ],
    "timeline": [
      {
        "date": "2025-02-15",
        "prevalence": 3.2,
        "growthRate": 10.5
      },
      {
        "date": "2025-02-22",
        "prevalence": 5.4,
        "growthRate": 68.7
      }
    ]
  },
  "forecast": {
    "expectedPeak": "2025-05-30T00:00:00Z",
    "expectedDecline": "2025-06-15T00:00:00Z",
    "sustainabilityScore": 0.65,
    "confidenceInterval": {
      "min": "2025-05-15T00:00:00Z",
      "max": "2025-06-15T00:00:00Z"
    }
  }
}
```

## Custom Metrics and Reporting

### Define Custom Metric

```
POST /api/analysis/metrics/custom
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "name": "Weighted Engagement Score",
  "description": "Custom engagement score that weights different interaction types",
  "formula": "(likes * 1) + (comments * 5) + (shares * 10) + (saves * 3)",
  "normalization": {
    "method": "percentile",
    "baseline": "account_average"
  },
  "display": {
    "format": "decimal",
    "precision": 2,
    "target": {
      "min": 50,
      "ideal": 75
    }
  }
}
```

**Response:**

```json
{
  "success": true,
  "metricId": "custom_metric_12345",
  "name": "Weighted Engagement Score",
  "availableIn": [
    "content_analysis",
    "dataset_reporting",
    "dashboards"
  ]
}
```

### Create Custom Report

```
POST /api/analysis/reports/custom
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "name": "Monthly Performance Summary",
  "description": "End-of-month performance analysis with key metrics and insights",
  "schedule": {
    "frequency": "monthly",
    "dayOfMonth": "last",
    "time": "08:00:00",
    "timezone": "America/New_York"
  },
  "dataSource": {
    "datasetId": "dataset_12345",
    "accountIds": ["account_12345", "account_67890"]
  },
  "sections": [
    {
      "title": "Performance Overview",
      "metrics": [
        "engagement_rate",
        "follower_growth",
        "impressions",
        "custom_metric_12345"
      ],
      "visualizations": [
        {
          "type": "time_series",
          "metrics": ["engagement_rate", "follower_growth"],
          "timeframe": "last30days"
        }
      ]
    },
    {
      "title": "Content Analysis",
      "metrics": [
        "top_performing_content",
        "content_type_breakdown",
        "hashtag_performance"
      ],
      "visualizations": [
        {
          "type": "bar_chart",
          "metric": "content_type_breakdown",
          "sort": "descending"
        }
      ]
    }
  ],
  "delivery": {
    "email": ["user@example.com"],
    "formats": ["pdf", "csv"]
  }
}
```

**Response:**

```json
{
  "success": true,
  "reportId": "report_12345",
  "name": "Monthly Performance Summary",
  "nextScheduled": "2025-05-31T08:00:00-04:00"
}
```

### Run Scheduled Report Now

```
POST /api/analysis/reports/{reportId}/run
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "reportId": "report_12345",
  "executionId": "exec_12345",
  "status": "processing",
  "estimatedCompletion": "2025-05-15T12:35:00Z"
}
```

### Get Report Execution Status

```
GET /api/analysis/reports/executions/{executionId}
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "executionId": "exec_12345",
  "reportId": "report_12345",
  "status": "completed",
  "completedAt": "2025-05-15T12:32:45Z",
  "results": {
    "downloadUrl": "/api/analysis/reports/executions/exec_12345/download?format=pdf",
    "previewUrl": "/api/analysis/reports/executions/exec_12345/preview"
  }
}
```
