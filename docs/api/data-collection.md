# Data Collection API

The Data Collection API allows you to programmatically collect social media data from various platforms, manage collection jobs, and monitor their status.

## Platform Authentication

Before collecting data from a social media platform, you must authenticate with that platform.

### Connect Platform Account

```
POST /api/platforms/connect
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "platform": "instagram",  // Options: instagram, tiktok, youtube, twitter, facebook
  "authMethod": "oauth",    // Options: oauth, credentials
  "credentials": {          // Only required if authMethod is "credentials"
    "username": "yourusername",
    "password": "yourpassword"
  },
  "oauthToken": "..." // Only required if authMethod is "oauth"
}
```

**Response:**

```json
{
  "success": true,
  "connection": {
    "id": "conn_123456789",
    "platform": "instagram",
    "username": "yourusername",
    "profileUrl": "https://instagram.com/yourusername",
    "avatarUrl": "https://cdn.instagram.com/profiles/yourusername.jpg",
    "status": "connected",
    "connectedAt": "2025-05-15T10:30:00Z"
  }
}
```

### List Connected Platforms

```
GET /api/platforms/connected
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "connections": [
    {
      "id": "conn_123456789",
      "platform": "instagram",
      "username": "yourusername",
      "profileUrl": "https://instagram.com/yourusername",
      "avatarUrl": "https://cdn.instagram.com/profiles/yourusername.jpg",
      "status": "connected",
      "connectedAt": "2025-05-15T10:30:00Z"
    },
    {
      "id": "conn_987654321",
      "platform": "youtube",
      "username": "YourChannel",
      "profileUrl": "https://youtube.com/c/YourChannel",
      "avatarUrl": "https://yt3.googleusercontent.com/ytc/YourChannel.jpg",
      "status": "connected",
      "connectedAt": "2025-05-14T08:45:00Z"
    }
  ]
}
```

### Disconnect Platform

```
DELETE /api/platforms/connected/{connectionId}
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "message": "Platform disconnected successfully"
}
```

## Collection Jobs

### Create Collection Job

```
POST /api/collection/jobs
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "name": "Monthly Competitor Analysis",
  "description": "Collect data from top competitors",
  "projectId": "proj_123456789",
  "datasetId": "ds_123456789",  // Optional, will create new dataset if not provided
  "targets": [
    {
      "platform": "instagram",
      "accountUrl": "https://instagram.com/competitor1",
      "dataTypes": ["posts", "engagement", "audience"]
    },
    {
      "platform": "tiktok",
      "accountUrl": "https://tiktok.com/@competitor2",
      "dataTypes": ["videos", "engagement"]
    }
  ],
  "timeRange": {
    "start": "2025-01-01T00:00:00Z",
    "end": "2025-05-01T00:00:00Z"
  },
  "schedule": {
    "type": "oneTime",  // Options: oneTime, recurring
    "recurringPattern": null  // Required if type is "recurring"
  },
  "options": {
    "includeComments": true,
    "includeMedia": true,
    "maxPostsPerAccount": 500,
    "maxCommentsPerPost": 100
  }
}
```

**Response:**

```json
{
  "success": true,
  "job": {
    "id": "job_123456789",
    "name": "Monthly Competitor Analysis",
    "status": "created",
    "createdAt": "2025-05-15T10:30:00Z",
    "datasetId": "ds_987654321",
    "estimated": {
      "accounts": 2,
      "posts": "~1000",
      "dataSize": "~50MB",
      "duration": "~15 minutes"
    }
  }
}
```

### List Collection Jobs

```
GET /api/collection/jobs
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Query Parameters:**

```
status=active,pending,completed,failed
projectId=proj_123456789
limit=20
offset=0
```

**Response:**

```json
{
  "success": true,
  "jobs": [
    {
      "id": "job_123456789",
      "name": "Monthly Competitor Analysis",
      "status": "active",
      "progress": 45,
      "createdAt": "2025-05-15T10:30:00Z",
      "startedAt": "2025-05-15T10:31:00Z",
      "datasetId": "ds_987654321",
      "estimatedCompletion": "2025-05-15T10:46:00Z"
    },
    {
      "id": "job_987654321",
      "name": "Weekly Performance Tracking",
      "status": "completed",
      "progress": 100,
      "createdAt": "2025-05-08T09:00:00Z",
      "startedAt": "2025-05-08T09:01:00Z",
      "completedAt": "2025-05-08T09:12:34Z",
      "datasetId": "ds_123456789"
    }
  ],
  "pagination": {
    "total": 45,
    "limit": 20,
    "offset": 0,
    "hasMore": true
  }
}
```

### Get Job Status

```
GET /api/collection/jobs/{jobId}
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "job": {
    "id": "job_123456789",
    "name": "Monthly Competitor Analysis",
    "description": "Collect data from top competitors",
    "status": "active",
    "progress": 45,
    "createdAt": "2025-05-15T10:30:00Z",
    "startedAt": "2025-05-15T10:31:00Z",
    "estimatedCompletion": "2025-05-15T10:46:00Z",
    "datasetId": "ds_987654321",
    "projectId": "proj_123456789",
    "targets": [
      {
        "platform": "instagram",
        "accountUrl": "https://instagram.com/competitor1",
        "status": "completed",
        "postsCollected": 243,
        "lastPostDate": "2025-04-30T18:22:15Z"
      },
      {
        "platform": "tiktok",
        "accountUrl": "https://tiktok.com/@competitor2",
        "status": "in_progress",
        "postsCollected": 112,
        "lastPostDate": "2025-03-15T14:08:45Z"
      }
    ],
    "statistics": {
      "accountsProcessed": 1,
      "accountsTotal": 2,
      "postsCollected": 355,
      "commentsCollected": 4328,
      "dataSize": "22.5MB"
    },
    "logs": [
      {
        "timestamp": "2025-05-15T10:31:00Z",
        "level": "info",
        "message": "Collection job started"
      },
      {
        "timestamp": "2025-05-15T10:35:22Z",
        "level": "info",
        "message": "Completed collection for instagram.com/competitor1"
      }
    ]
  }
}
```

### Cancel Collection Job

```
POST /api/collection/jobs/{jobId}/cancel
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "job": {
    "id": "job_123456789",
    "status": "cancelled",
    "cancelledAt": "2025-05-15T10:40:00Z"
  }
}
```

### Retry Failed Job

```
POST /api/collection/jobs/{jobId}/retry
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "job": {
    "id": "job_123456789",
    "status": "pending",
    "retriedAt": "2025-05-15T10:45:00Z"
  }
}
```

## Account Discovery

### Search for Accounts

```
GET /api/collection/discover
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Query Parameters:**

```
platform=instagram
query=fashion
limit=10
```

**Response:**

```json
{
  "success": true,
  "accounts": [
    {
      "platform": "instagram",
      "username": "fashionbrand1",
      "displayName": "Fashion Brand Official",
      "profileUrl": "https://instagram.com/fashionbrand1",
      "avatarUrl": "https://cdn.instagram.com/profiles/fashionbrand1.jpg",
      "followersCount": 1200000,
      "postsCount": 3245,
      "isVerified": true,
      "category": "Clothing Brand"
    },
    {
      "platform": "instagram",
      "username": "fashioninfluencer",
      "displayName": "Fashion Influencer",
      "profileUrl": "https://instagram.com/fashioninfluencer",
      "avatarUrl": "https://cdn.instagram.com/profiles/fashioninfluencer.jpg",
      "followersCount": 850000,
      "postsCount": 1876,
      "isVerified": true,
      "category": "Public Figure"
    }
  ],
  "pagination": {
    "total": 245,
    "limit": 10,
    "hasMore": true
  }
}
```

### Get Account Details

```
GET /api/collection/accounts/{platform}/{username}
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Response:**

```json
{
  "success": true,
  "account": {
    "platform": "instagram",
    "username": "fashionbrand1",
    "displayName": "Fashion Brand Official",
    "profileUrl": "https://instagram.com/fashionbrand1",
    "avatarUrl": "https://cdn.instagram.com/profiles/fashionbrand1.jpg",
    "bio": "Official account of Fashion Brand. #FashionForAll",
    "website": "https://fashionbrand.com",
    "followersCount": 1200000,
    "followingCount": 342,
    "postsCount": 3245,
    "isVerified": true,
    "category": "Clothing Brand",
    "joinDate": "2015-03-22T00:00:00Z",
    "lastPost": {
      "timestamp": "2025-05-14T15:30:00Z",
      "url": "https://instagram.com/p/abc123",
      "thumbnailUrl": "https://cdn.instagram.com/p/abc123.jpg",
      "likes": 45678,
      "comments": 2134
    },
    "engagement": {
      "rate": 3.2,
      "avgLikes": 38500,
      "avgComments": 1245
    },
    "insights": {
      "postFrequency": "4.3 posts/week",
      "topHashtags": ["#fashion", "#style", "#newcollection"],
      "mediaTypes": {
        "images": 65,
        "videos": 30,
        "carousels": 5
      }
    }
  },
  "collectionStatus": {
    "isInAnyDataset": true,
    "datasetIds": ["ds_123456789", "ds_987654321"],
    "lastCollected": "2025-05-01T08:30:00Z"
  }
}
```

## Error Handling

### Common Error Responses

**Rate Limit Exceeded:**

```json
{
  "success": false,
  "error": {
    "code": "collection/rate-limited",
    "message": "Platform rate limit exceeded",
    "details": {
      "platform": "instagram",
      "resetTime": "2025-05-15T11:30:00Z",
      "limitType": "requests_per_hour"
    }
  }
}
```

**Authentication Required:**

```json
{
  "success": false,
  "error": {
    "code": "collection/auth-required",
    "message": "Platform authentication required",
    "details": {
      "platform": "tiktok",
      "authUrl": "https://api.cherrybomb.app/api/platforms/connect?platform=tiktok"
    }
  }
}
```

**Account Not Found:**

```json
{
  "success": false,
  "error": {
    "code": "collection/account-not-found",
    "message": "The specified account could not be found",
    "details": {
      "platform": "instagram",
      "username": "nonexistentaccount"
    }
  }
}
```

**Private Account:**

```json
{
  "success": false,
  "error": {
    "code": "collection/account-private",
    "message": "Cannot collect data from private account",
    "details": {
      "platform": "instagram",
      "username": "privateaccount"
    }
  }
}
```

## Webhooks

### Register Collection Webhook

```
POST /api/collection/webhooks
```

**Request Headers:**

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Request Body:**

```json
{
  "url": "https://your-app.com/webhooks/cherrybomb",
  "events": ["job.created", "job.completed", "job.failed"],
  "secret": "yourWebhookSecret",
  "description": "Production webhook for collection job updates"
}
```

**Response:**

```json
{
  "success": true,
  "webhook": {
    "id": "wh_123456789",
    "url": "https://your-app.com/webhooks/cherrybomb",
    "events": ["job.created", "job.completed", "job.failed"],
    "createdAt": "2025-05-15T10:30:00Z",
    "status": "active"
  }
}
```

### Webhook Payload Example

When a collection job completes:

```json
{
  "event": "job.completed",
  "timestamp": "2025-05-15T10:46:00Z",
  "data": {
    "jobId": "job_123456789",
    "status": "completed",
    "datasetId": "ds_987654321",
    "statistics": {
      "accountsProcessed": 2,
      "postsCollected": 455,
      "commentsCollected": 5328,
      "dataSize": "27.8MB"
    }
  }
}
```
