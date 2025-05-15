# Prediction API

The Prediction API provides programmatic access to CherryBomb's machine learning capabilities for forecasting content performance, identifying trends, and optimizing social media strategy before publication.

## Overview

The Prediction API enables:

- Forecasting engagement metrics for draft content
- Predicting optimal posting times
- Generating content optimization suggestions
- Forecasting audience growth and trends
- Managing and evaluating prediction models

## Content Performance Prediction

### Predict Content Performance

```text
POST /api/prediction/content
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "accountId": "account_12345",
  "content": {
    "type": "post",
    "platform": "instagram",
    "caption": "Introducing our new sustainable collection! #sustainability #fashion",
    "mediaUrls": ["https://example.com/images/product1.jpg", "https://example.com/images/product2.jpg"],
    "mediaType": "carousel",
    "hashtags": ["sustainability", "fashion", "newcollection"],
    "mentionedAccounts": ["@partnerbrand"]
  },
  "scheduledTime": "2025-05-20T14:30:00Z",
  "predictionDetails": {
    "metrics": ["engagement_rate", "likes", "comments", "saves", "shares", "reach"],
    "audienceSegments": true,
    "confidenceIntervals": true,
    "benchmarking": true
  }
}
```

**Response:**

```json
{
  "success": true,
  "predictionId": "pred_1234567890",
  "accountId": "account_12345",
  "predictions": {
    "overall": {
      "performanceTier": "above_average",
      "confidence": 0.87
    },
    "metrics": {
      "engagement_rate": {
        "value": 4.3,
        "confidenceInterval": {
          "low": 3.8,
          "high": 4.9
        },
        "benchmark": {
          "accountAverage": 3.2,
          "percentile": 78
        }
      },
      "likes": {
        "value": 580,
        "confidenceInterval": {
          "low": 520,
          "high": 650
        },
        "benchmark": {
          "accountAverage": 430,
          "percentile": 82
        }
      },
      "comments": {
        "value": 42,
        "confidenceInterval": {
          "low": 36,
          "high": 49
        },
        "benchmark": {
          "accountAverage": 36,
          "percentile": 68
        }
      },
      "saves": {
        "value": 85,
        "confidenceInterval": {
          "low": 72,
          "high": 98
        },
        "benchmark": {
          "accountAverage": 65,
          "percentile": 75
        }
      },
      "shares": {
        "value": 28,
        "confidenceInterval": {
          "low": 22,
          "high": 35
        },
        "benchmark": {
          "accountAverage": 22,
          "percentile": 65
        }
      },
      "reach": {
        "value": 5200,
        "confidenceInterval": {
          "low": 4800,
          "high": 5600
        },
        "benchmark": {
          "accountAverage": 4300,
          "percentile": 72
        }
      }
    },
    "audienceSegments": {
      "demographics": [
        {
          "segment": "females_25_34",
          "engagementRate": 5.2,
          "percentOfAudience": 38
        },
        {
          "segment": "females_18_24",
          "engagementRate": 4.8,
          "percentOfAudience": 22
        },
        {
          "segment": "males_25_34",
          "engagementRate": 3.7,
          "percentOfAudience": 18
        }
      ],
      "interests": [
        {
          "segment": "sustainable_living",
          "engagementRate": 5.7,
          "percentOfAudience": 24
        },
        {
          "segment": "fashion",
          "engagementRate": 4.8,
          "percentOfAudience": 42
        }
      ]
    },
    "timing": {
      "scheduledTime": {
        "score": 82,
        "assessment": "good"
      },
      "optimalTimes": [
        {
          "time": "2025-05-20T16:00:00Z",
          "score": 94,
          "potentialImprovement": "+12%"
        },
        {
          "time": "2025-05-21T14:00:00Z",
          "score": 91,
          "potentialImprovement": "+9%"
        }
      ]
    }
  },
  "optimizationSuggestions": [
    {
      "type": "caption",
      "suggestion": "Add a question to increase comment engagement",
      "potentialImprovement": "+15% comments",
      "confidence": 0.82
    },
    {
      "type": "media",
      "suggestion": "Add a close-up product shot as the first image",
      "potentialImprovement": "+8% engagement rate",
      "confidence": 0.75
    },
    {
      "type": "hashtags",
      "suggestion": "Add #ecofriendly and #sustainablestyle hashtags",
      "potentialImprovement": "+5% reach",
      "confidence": 0.78
    },
    {
      "type": "timing",
      "suggestion": "Reschedule to 4PM for optimal engagement",
      "potentialImprovement": "+12% engagement rate",
      "confidence": 0.88
    }
  ],
  "modelInfo": {
    "modelId": "model_instagram_v3.2",
    "lastTrainingDate": "2025-05-01T00:00:00Z",
    "accuracy": 0.85,
    "dataPoints": 12500
  }
}
```

### Get Prediction Details

```text
GET /api/prediction/{predictionId}
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "predictionId": "pred_1234567890",
  "createTime": "2025-05-15T10:20:30Z",
  "contentId": "draft_12345",
  "accountId": "account_12345",
  "status": "completed",
  "predictions": {
    // Same content as in the POST response
  }
}
```

### Compare Content Variations

```text
POST /api/prediction/compare
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "accountId": "account_12345",
  "baseContent": {
    "contentId": "draft_12345",
    "type": "post",
    "platform": "instagram",
    "caption": "Introducing our new sustainable collection! #sustainability #fashion",
    "mediaUrls": ["https://example.com/images/product1.jpg", "https://example.com/images/product2.jpg"],
    "mediaType": "carousel"
  },
  "variations": [
    {
      "id": "variation_1",
      "caption": "Our most sustainable collection yet! Which style is your favorite? #sustainability #fashion",
      "mediaUrls": ["https://example.com/images/product1.jpg", "https://example.com/images/product2.jpg"],
      "mediaType": "carousel"
    },
    {
      "id": "variation_2",
      "caption": "Introducing our new sustainable collection! #sustainability #fashion",
      "mediaUrls": ["https://example.com/images/product2.jpg", "https://example.com/images/product1.jpg", "https://example.com/images/product3.jpg"],
      "mediaType": "carousel"
    }
  ],
  "metrics": ["engagement_rate", "comments", "saves"],
  "scheduledTime": "2025-05-20T14:30:00Z"
}
```

**Response:**

```json
{
  "success": true,
  "comparisonId": "comp_1234567890",
  "accountId": "account_12345",
  "baseContent": {
    "contentId": "draft_12345",
    "predictions": {
      "engagement_rate": {
        "value": 4.3,
        "ranking": 2
      },
      "comments": {
        "value": 42,
        "ranking": 3
      },
      "saves": {
        "value": 85,
        "ranking": 2
      },
      "overall": {
        "score": 78,
        "ranking": 2
      }
    }
  },
  "variations": [
    {
      "id": "variation_1",
      "predictions": {
        "engagement_rate": {
          "value": 4.8,
          "ranking": 1,
          "improvement": "+11.6%"
        },
        "comments": {
          "value": 58,
          "ranking": 1,
          "improvement": "+38.1%"
        },
        "saves": {
          "value": 83,
          "ranking": 3,
          "improvement": "-2.4%"
        },
        "overall": {
          "score": 85,
          "ranking": 1,
          "improvement": "+9.0%"
        }
      },
      "keyDifferences": [
        "Question in caption driving more comments",
        "More engaging first sentence"
      ]
    },
    {
      "id": "variation_2",
      "predictions": {
        "engagement_rate": {
          "value": 4.2,
          "ranking": 3,
          "improvement": "-2.3%"
        },
        "comments": {
          "value": 43,
          "ranking": 2,
          "improvement": "+2.4%"
        },
        "saves": {
          "value": 92,
          "ranking": 1,
          "improvement": "+8.2%"
        },
        "overall": {
          "score": 77,
          "ranking": 3,
          "improvement": "-1.3%"
        }
      },
      "keyDifferences": [
        "Third image improving save rate",
        "Different image order reducing overall engagement"
      ]
    }
  ],
  "recommendation": "variation_1",
  "insights": [
    "Adding a question in the caption significantly improves comment engagement",
    "The order of carousel images impacts overall engagement",
    "Variation 1 shows the best overall performance metrics"
  ]
}
```

## Posting Time Prediction

### Get Optimal Posting Times

```text
GET /api/prediction/posting-times/{accountId}
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Query Parameters:**

```text
platform=instagram
daysAhead=7
contentType=photo
```

**Response:**

```json
{
  "success": true,
  "accountId": "account_12345",
  "platform": "instagram",
  "contentType": "photo",
  "optimalTimes": [
    {
      "day": "Monday",
      "times": [
        {
          "time": "2025-05-19T16:00:00Z",
          "score": 92,
          "audienceActivity": "high",
          "competition": "medium"
        },
        {
          "time": "2025-05-19T20:30:00Z",
          "score": 87,
          "audienceActivity": "high",
          "competition": "high"
        }
      ]
    },
    {
      "day": "Tuesday",
      "times": [
        {
          "time": "2025-05-20T14:00:00Z",
          "score": 90,
          "audienceActivity": "high",
          "competition": "low"
        },
        {
          "time": "2025-05-20T19:00:00Z",
          "score": 85,
          "audienceActivity": "medium",
          "competition": "low"
        }
      ]
    }
  ],
  "weeklyHeatmap": {
    "monday": [40, 45, 50, 60, 70, 85, 92, 88, 84, 80, 75, 70, 65, 60, 55, 60, 70, 80, 87, 84, 75, 65, 50, 45],
    "tuesday": [38, 42, 48, 55, 65, 75, 85, 90, 85, 80, 75, 70, 65, 60, 65, 70, 75, 80, 85, 82, 75, 65, 55, 45],
    "wednesday": [35, 40, 45, 55, 65, 80, 90, 88, 85, 80, 75, 70, 65, 62, 65, 72, 80, 85, 88, 85, 75, 65, 55, 45]
  }
}
```

### Evaluate Specific Posting Time

```text
POST /api/prediction/evaluate-time
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "accountId": "account_12345",
  "platform": "instagram",
  "contentType": "video",
  "proposedTime": "2025-05-21T18:30:00Z",
  "contentTags": ["product", "tutorial", "outdoor"]
}
```

**Response:**

```json
{
  "success": true,
  "evaluation": {
    "score": 78,
    "rating": "good",
    "audienceActivity": {
      "level": "medium-high",
      "percentOfPeak": 85
    },
    "competitionLevel": {
      "level": "medium",
      "accountsPosting": 42
    },
    "algorithmFavorability": {
      "level": "favorable",
      "recentChanges": false
    },
    "historicalPerformance": {
      "similarPosts": 12,
      "averageEngagement": 4.2
    }
  },
  "alternatives": [
    {
      "time": "2025-05-21T20:00:00Z",
      "score": 92,
      "improvement": "+18%"
    },
    {
      "time": "2025-05-22T17:30:00Z",
      "score": 88,
      "improvement": "+13%"
    }
  ]
}
```

## Content Optimization

### Get Content Optimization Suggestions

```text
POST /api/prediction/optimize
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "accountId": "account_12345",
  "contentId": "draft_12345",
  "optimizationTypes": [
    "caption",
    "hashtags",
    "media",
    "postingTime"
  ],
  "contentGoals": [
    "engagement",
    "reach",
    "saves"
  ]
}
```

**Response:**

```json
{
  "success": true,
  "contentId": "draft_12345",
  "currentPrediction": {
    "engagementRate": 3.8,
    "reach": 4500,
    "saves": 65
  },
  "optimizationSuggestions": {
    "caption": [
      {
        "suggestion": "Add a question to encourage comments",
        "examples": [
          "Which color would you choose?",
          "What's your favorite sustainable fashion tip?"
        ],
        "impact": {
          "engagement": "+15%",
          "comments": "+32%"
        },
        "confidence": 0.88
      },
      {
        "suggestion": "Include a call-to-action",
        "examples": [
          "Tap the link in bio to shop the collection",
          "Save this post for later inspiration"
        ],
        "impact": {
          "engagement": "+8%",
          "saves": "+22%"
        },
        "confidence": 0.82
      }
    ],
    "hashtags": [
      {
        "suggestion": "Add niche-specific hashtags",
        "examples": [
          "#sustainablestyle",
          "#ecofashion",
          "#consciousfashion"
        ],
        "impact": {
          "reach": "+12%",
          "discovery": "+18%"
        },
        "confidence": 0.85
      },
      {
        "suggestion": "Remove low-performing hashtags",
        "examples": [
          "#fashion",
          "#style"
        ],
        "reasoning": "Too generic and competitive",
        "impact": {
          "algorithm_favor": "+5%"
        },
        "confidence": 0.75
      }
    ],
    "media": [
      {
        "suggestion": "Reorder carousel images",
        "recommendation": "Place the image with the person wearing the product first",
        "impact": {
          "impressions": "+10%",
          "swipes": "+25%"
        },
        "confidence": 0.78
      },
      {
        "suggestion": "Enhance color contrast",
        "recommendation": "Increase vibrance of the main product image",
        "impact": {
          "engagement": "+7%",
          "saves": "+12%"
        },
        "confidence": 0.72
      }
    ],
    "postingTime": [
      {
        "currentTime": "2025-05-20T14:30:00Z",
        "optimalTime": "2025-05-20T19:00:00Z",
        "impact": {
          "engagement": "+14%",
          "reach": "+18%"
        },
        "confidence": 0.85
      }
    ]
  },
  "combinedImpact": {
    "projected": {
      "engagementRate": 4.7,
      "reach": 5800,
      "saves": 95
    },
    "improvement": {
      "engagementRate": "+23.7%",
      "reach": "+28.9%",
      "saves": "+46.2%"
    }
  }
}
```

### Generate AI-Enhanced Content

```text
POST /api/prediction/enhance
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "accountId": "account_12345",
  "contentId": "draft_12345",
  "enhancementTypes": [
    "caption",
    "hashtags"
  ],
  "tonePreferences": {
    "voice": "friendly",
    "formality": "casual",
    "brandValues": ["sustainable", "innovative", "authentic"]
  },
  "constraints": {
    "maximumLength": 220,
    "mustInclude": ["new collection", "sustainable"],
    "mustExclude": ["limited time", "discount"]
  }
}
```

**Response:**

```json
{
  "success": true,
  "contentId": "draft_12345",
  "enhancements": {
    "caption": {
      "original": "Introducing our new sustainable collection! #sustainability #fashion",
      "enhanced": "Our most sustainable collection yet has arrived! Made from 100% recycled materials that look good and feel even better. Which piece would you add to your wardrobe first? #sustainability #fashion",
      "reasoning": "Added product details, brand values, and an engagement question",
      "predictedImprovement": {
        "engagement": "+18%",
        "comments": "+35%"
      }
    },
    "hashtags": {
      "original": ["sustainability", "fashion"],
      "enhanced": ["sustainability", "sustainablestyle", "ecofashion", "consciousfashion", "recycledfashion", "ethicalstyle"],
      "reasoning": "Added niche-specific hashtags with less competition and higher relevance",
      "predictedImprovement": {
        "reach": "+15%",
        "discovery": "+22%"
      }
    }
  },
  "alternativeVersions": [
    {
      "caption": "Sustainability meets style in our newest collection. Crafted from 100% recycled materials, each piece helps reduce fashion waste while keeping you looking your best. Tap to shop your favorites! #sustainability #fashion",
      "predictedEngagement": 4.2
    },
    {
      "caption": "The wait is over! Our new sustainable collection just dropped, featuring pieces made entirely from recycled materials. Perfect for the conscious fashionista who doesn't compromise on style. What's catching your eye? #sustainability #fashion",
      "predictedEngagement": 4.0
    }
  ],
  "overallPrediction": {
    "before": {
      "engagementRate": 3.8,
      "reach": 4500
    },
    "after": {
      "engagementRate": 4.5,
      "reach": 5175
    },
    "improvement": {
      "engagementRate": "+18.4%",
      "reach": "+15.0%"
    }
  }
}
```

## Trend Prediction

### Predict Trending Topics

```text
POST /api/prediction/trends/forecast
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "industry": "fashion",
  "subCategories": ["sustainable", "streetwear", "accessories"],
  "timeframe": {
    "start": "2025-05-15T00:00:00Z",
    "end": "2025-07-15T00:00:00Z"
  },
  "trendTypes": [
    "topics",
    "hashtags",
    "content_formats",
    "visual_elements"
  ]
}
```

**Response:**

```json
{
  "success": true,
  "predictionId": "trend_pred_12345",
  "industry": "fashion",
  "timeframe": {
    "start": "2025-05-15T00:00:00Z",
    "end": "2025-07-15T00:00:00Z"
  },
  "trendPredictions": {
    "topics": [
      {
        "trend": "Biodegradable fashion",
        "currentVolume": "low",
        "predictedGrowth": "+230%",
        "confidence": 0.85,
        "peakTime": "2025-06-20T00:00:00Z",
        "lifecycle": "emerging",
        "relevanceScore": 89
      },
      {
        "trend": "Modular clothing systems",
        "currentVolume": "very low",
        "predictedGrowth": "+450%",
        "confidence": 0.78,
        "peakTime": "2025-07-05T00:00:00Z",
        "lifecycle": "early emerging",
        "relevanceScore": 92
      }
    ],
    "hashtags": [
      {
        "trend": "#zerowastefashion",
        "currentVolume": "medium",
        "predictedGrowth": "+85%",
        "confidence": 0.92,
        "peakTime": "2025-05-30T00:00:00Z",
        "lifecycle": "growing",
        "relevanceScore": 95
      },
      {
        "trend": "#capsulewardrobe",
        "currentVolume": "high",
        "predictedGrowth": "+40%",
        "confidence": 0.88,
        "peakTime": "2025-06-15T00:00:00Z",
        "lifecycle": "growing",
        "relevanceScore": 87
      }
    ],
    "content_formats": [
      {
        "trend": "Behind-the-scenes production videos",
        "currentVolume": "medium",
        "predictedGrowth": "+75%",
        "confidence": 0.87,
        "peakTime": "2025-06-10T00:00:00Z",
        "lifecycle": "growing",
        "relevanceScore": 91
      },
      {
        "trend": "Sustainable materials close-ups",
        "currentVolume": "low",
        "predictedGrowth": "+120%",
        "confidence": 0.82,
        "peakTime": "2025-06-25T00:00:00Z",
        "lifecycle": "emerging",
        "relevanceScore": 88
      }
    ],
    "visual_elements": [
      {
        "trend": "Natural dye color palettes",
        "currentVolume": "medium-low",
        "predictedGrowth": "+95%",
        "confidence": 0.84,
        "peakTime": "2025-06-05T00:00:00Z",
        "lifecycle": "emerging",
        "relevanceScore": 90
      },
      {
        "trend": "Raw edge finishing",
        "currentVolume": "low",
        "predictedGrowth": "+150%",
        "confidence": 0.79,
        "peakTime": "2025-07-10T00:00:00Z",
        "lifecycle": "early emerging",
        "relevanceScore": 85
      }
    ]
  },
  "strategicOpportunities": [
    {
      "opportunity": "Early adopter advantage for biodegradable fashion content",
      "recommendedTimeframe": "Next 2-3 weeks",
      "potentialImpact": "Very High",
      "implementationDifficulty": "Medium"
    },
    {
      "opportunity": "Behind-the-scenes production content series",
      "recommendedTimeframe": "Next 4 weeks",
      "potentialImpact": "High",
      "implementationDifficulty": "Low"
    },
    {
      "opportunity": "Natural dye process demonstration content",
      "recommendedTimeframe": "Next 3 weeks",
      "potentialImpact": "Medium-High",
      "implementationDifficulty": "Medium"
    }
  ]
}
```

### Track Trend Prediction Accuracy

```text
GET /api/prediction/trends/{predictionId}/accuracy
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "predictionId": "trend_pred_12345",
  "createdAt": "2025-04-15T00:00:00Z",
  "timeframe": {
    "start": "2025-05-15T00:00:00Z",
    "end": "2025-07-15T00:00:00Z"
  },
  "overallAccuracy": {
    "score": 0.84,
    "rating": "very good"
  },
  "trendAccuracy": [
    {
      "trend": "Biodegradable fashion",
      "predicted": {
        "growth": "+230%",
        "peakTime": "2025-06-20T00:00:00Z"
      },
      "actual": {
        "growth": "+210%",
        "peakTime": "2025-06-18T00:00:00Z"
      },
      "accuracy": {
        "growth": 0.91,
        "timing": 0.93,
        "overall": 0.92
      }
    },
    {
      "trend": "#zerowastefashion",
      "predicted": {
        "growth": "+85%",
        "peakTime": "2025-05-30T00:00:00Z"
      },
      "actual": {
        "growth": "+65%",
        "peakTime": "2025-06-05T00:00:00Z"
      },
      "accuracy": {
        "growth": 0.76,
        "timing": 0.83,
        "overall": 0.80
      }
    }
  ]
}
```

## Model Management

### List Available Models

```text
GET /api/prediction/models
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Query Parameters:**

```text
platform=instagram
type=engagement
```

**Response:**

```json
{
  "success": true,
  "models": [
    {
      "modelId": "model_instagram_engagement_v3.2",
      "platform": "instagram",
      "type": "engagement",
      "version": "3.2",
      "lastTrained": "2025-05-01T00:00:00Z",
      "status": "active",
      "performance": {
        "accuracy": 0.85,
        "precision": 0.87,
        "recall": 0.82
      },
      "features": [
        "carousel optimization",
        "reel prediction",
        "story prediction"
      ],
      "usageStats": {
        "predictionsLast30Days": 12450,
        "averageLatency": 280
      }
    },
    {
      "modelId": "model_instagram_engagement_v3.1",
      "platform": "instagram",
      "type": "engagement",
      "version": "3.1",
      "lastTrained": "2025-03-15T00:00:00Z",
      "status": "deprecated",
      "performance": {
        "accuracy": 0.82,
        "precision": 0.84,
        "recall": 0.79
      },
      "features": [
        "carousel optimization",
        "reel prediction"
      ],
      "usageStats": {
        "predictionsLast30Days": 320,
        "averageLatency": 275
      }
    }
  ]
}
```

### Get Model Details

```text
GET /api/prediction/models/{modelId}
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "model": {
    "modelId": "model_instagram_engagement_v3.2",
    "platform": "instagram",
    "type": "engagement",
    "version": "3.2",
    "description": "CherryBomb's Instagram engagement prediction model optimized for 2025 algorithm changes",
    "lastTrained": "2025-05-01T00:00:00Z",
    "status": "active",
    "architecture": "Ensemble (XGBoost, LSTM, Neural Network)",
    "performance": {
      "accuracy": 0.85,
      "precision": 0.87,
      "recall": 0.82,
      "f1Score": 0.84,
      "mse": 0.08
    },
    "trainingData": {
      "sampleSize": 1250000,
      "timeRange": {
        "start": "2024-05-01T00:00:00Z",
        "end": "2025-04-30T23:59:59Z"
      },
      "accountTypes": [
        "small_business",
        "creator",
        "enterprise"
      ]
    },
    "features": [
      "carousel optimization",
      "reel prediction",
      "story prediction",
      "hashtag efficiency",
      "audience segment response"
    ],
    "updates": [
      {
        "version": "3.2",
        "date": "2025-05-01T00:00:00Z",
        "changes": [
          "Added support for Instagram's algorithm update from April 2025",
          "Improved prediction for video content",
          "Enhanced audience segment response modeling"
        ]
      },
      {
        "version": "3.1",
        "date": "2025-03-15T00:00:00Z",
        "changes": [
          "Improved carousel engagement prediction",
          "Added support for new engagement metrics",
          "Enhanced feature extraction for image content"
        ]
      }
    ]
  }
}
```

### Request Custom Model Training

```text
POST /api/prediction/models/train
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "name": "Custom Fashion Brand Model",
  "baseModelId": "model_instagram_engagement_v3.2",
  "trainingData": {
    "datasetIds": ["dataset_12345", "dataset_67890"],
    "timeRange": {
      "start": "2025-01-01T00:00:00Z",
      "end": "2025-04-30T23:59:59Z"
    }
  },
  "modelParameters": {
    "optimizationTarget": "engagement_rate",
    "secondaryTargets": ["saves", "shares"],
    "specializationFocus": [
      "product_photography",
      "sustainable_fashion"
    ]
  },
  "validationSettings": {
    "testSplitPercent": 20,
    "crossValidationFolds": 5
  }
}
```

**Response:**

```json
{
  "success": true,
  "trainingJobId": "job_12345",
  "estimatedCompletionTime": "2025-05-16T12:00:00Z",
  "modelInfo": {
    "name": "Custom Fashion Brand Model",
    "baseModelId": "model_instagram_engagement_v3.2",
    "status": "training_scheduled"
  }
}
```

### Get Model Training Status

```text
GET /api/prediction/models/training/{trainingJobId}
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "trainingJobId": "job_12345",
  "status": "in_progress",
  "progress": 65,
  "currentPhase": "model_tuning",
  "phases": [
    {
      "phase": "data_preparation",
      "status": "completed",
      "startTime": "2025-05-15T10:30:00Z",
      "endTime": "2025-05-15T10:45:00Z"
    },
    {
      "phase": "feature_extraction",
      "status": "completed",
      "startTime": "2025-05-15T10:45:00Z",
      "endTime": "2025-05-15T11:10:00Z"
    },
    {
      "phase": "model_tuning",
      "status": "in_progress",
      "startTime": "2025-05-15T11:10:00Z",
      "endTime": null
    },
    {
      "phase": "validation",
      "status": "pending",
      "startTime": null,
      "endTime": null
    },
    {
      "phase": "deployment",
      "status": "pending",
      "startTime": null,
      "endTime": null
    }
  ],
  "estimatedCompletionTime": "2025-05-16T12:00:00Z",
  "preliminaryMetrics": {
    "accuracy": 0.87,
    "mse": 0.07
  }
}
```

### Set Default Prediction Model

```text
POST /api/prediction/models/{modelId}/set-default
```

**Request Headers:**

```text
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "platformScope": "instagram",
  "predictorType": "engagement"
}
```

**Response:**

```json
{
  "success": true,
  "modelId": "model_instagram_engagement_v3.2",
  "defaultFor": {
    "platform": "instagram",
    "predictorType": "engagement"
  },
  "previousDefault": "model_instagram_engagement_v3.1"
}
```
