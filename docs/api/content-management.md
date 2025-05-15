# Content Management API

The Content Management API allows you to programmatically manage content drafts, schedule posts, and interact with the content calendar within CherryBomb.

## Overview

The Content Management API enables:

- Creating, updating, and deleting content drafts
- Scheduling content for various social media platforms
- Retrieving and managing the content calendar
- Tracking content status (draft, scheduled, published, error)

## Content Drafts

### Create Content Draft

```text
POST /api/content/drafts
```

**Request Headers:**

```text
Authorization: Bearer <YOUR_JWT_TOKEN>
Content-Type: application/json
```

**Request Body:**

```json
{
  "projectId": "proj_123abc",
  "title": "My Awesome New Post",
  "content": {
    "text": "Check out this amazing new product! #innovation #newproduct",
    "mediaUrls": ["https://example.com/image1.jpg"]
  },
  "targetPlatforms": ["instagram", "twitter"],
  "tags": ["product_launch", "q2_campaign"]
}
```

**Response (201 Created):**

```json
{
  "success": true,
  "draftId": "draft_789xyz",
  "message": "Content draft created successfully.",
  "createdAt": "2025-05-15T10:00:00Z",
  "status": "draft"
}
```

### Get Content Draft

```text
GET /api/content/drafts/{draftId}
```

**Request Headers:**

```text
Authorization: Bearer <YOUR_JWT_TOKEN>
```

**Response (200 OK):**

```json
{
  "success": true,
  "draftId": "draft_789xyz",
  "projectId": "proj_123abc",
  "title": "My Awesome New Post",
  "content": {
    "text": "Check out this amazing new product! #innovation #newproduct",
    "mediaUrls": ["https://example.com/image1.jpg"]
  },
  "targetPlatforms": ["instagram", "twitter"],
  "tags": ["product_launch", "q2_campaign"],
  "status": "draft",
  "createdAt": "2025-05-15T10:00:00Z",
  "updatedAt": "2025-05-15T10:05:00Z",
  "predictedPerformance": {
    "instagram": { "likes": 500, "comments": 20, "reach_estimate": 5000 },
    "twitter": { "likes": 100, "retweets": 30 }
  }
}
```

### Update Content Draft

```text
PUT /api/content/drafts/{draftId}
```

**Request Headers:**

```text
Authorization: Bearer <YOUR_JWT_TOKEN>
Content-Type: application/json
```

**Request Body:**

```json
{
  "title": "My Updated Awesome New Post",
  "content": {
    "text": "Check out this updated amazing new product! #innovation #newproduct #updated",
    "mediaUrls": ["https://example.com/image1.jpg", "https://example.com/image2.png"]
  },
  "targetPlatforms": ["instagram", "twitter", "facebook"]
}
```

**Response (200 OK):**

```json
{
  "success": true,
  "draftId": "draft_789xyz",
  "message": "Content draft updated successfully.",
  "updatedAt": "2025-05-15T11:00:00Z"
}
```

### Delete Content Draft

```text
DELETE /api/content/drafts/{draftId}
```

**Request Headers:**

```text
Authorization: Bearer <YOUR_JWT_TOKEN>
```

**Response (200 OK):**

```json
{
  "success": true,
  "message": "Content draft deleted successfully."
}
```

### List Content Drafts

```text
GET /api/content/drafts
```

**Request Headers:**

```text
Authorization: Bearer <YOUR_JWT_TOKEN>
```

**Query Parameters:**

```text
projectId=proj_123abc
status=draft
limit=20
offset=0
sortBy=updatedAt
order=desc
```

**Response (200 OK):**

```json
{
  "success": true,
  "data": [
    {
      "draftId": "draft_789xyz",
      "title": "My Updated Awesome New Post",
      "status": "draft",
      "targetPlatforms": ["instagram", "twitter", "facebook"],
      "updatedAt": "2025-05-15T11:00:00Z"
    }
    // ... other drafts
  ],
  "pagination": {
    "total": 1,
    "limit": 20,
    "offset": 0
  }
}
```

## Content Scheduling

### Schedule Content Draft

```text
POST /api/content/schedule
```

**Request Headers:**

```text
Authorization: Bearer <YOUR_JWT_TOKEN>
Content-Type: application/json
```

**Request Body:**

```json
{
  "draftId": "draft_789xyz",
  "scheduledTime": "2025-05-20T14:30:00Z",
  "platformSpecificOverrides": {
    "twitter": {
      "text": "Twitter specific text for this amazing product! #innovation"
    }
  }
}
```

**Response (200 OK):**

```json
{
  "success": true,
  "scheduledItemId": "sched_456uvw",
  "message": "Content scheduled successfully.",
  "status": "scheduled",
  "scheduledTime": "2025-05-20T14:30:00Z"
}
```

### Update Scheduled Content

```text
PUT /api/content/schedule/{scheduledItemId}
```

**Request Headers:**

```text
Authorization: Bearer <YOUR_JWT_TOKEN>
Content-Type: application/json
```

**Request Body:**

```json
{
  "scheduledTime": "2025-05-21T10:00:00Z",
  "contentUpdates": { // Optional: to update content of the underlying draft
    "text": "Final text for all platforms before publishing."
  }
}
```

**Response (200 OK):**

```json
{
  "success": true,
  "scheduledItemId": "sched_456uvw",
  "message": "Scheduled content updated successfully.",
  "updatedAt": "2025-05-15T12:00:00Z"
}
```

### Unschedule Content

```text
DELETE /api/content/schedule/{scheduledItemId}
```

**Request Headers:**

```text
Authorization: Bearer <YOUR_JWT_TOKEN>
```

**Response (200 OK):**

```json
{
  "success": true,
  "message": "Content unscheduled successfully. Draft is now back to 'draft' status."
}
```

## Content Calendar

### Get Calendar Items

```text
GET /api/content/calendar
```

**Request Headers:**

```text
Authorization: Bearer <YOUR_JWT_TOKEN>
```

**Query Parameters:**

```text
projectId=proj_123abc
startDate=2025-05-01
endDate=2025-05-31
platform=instagram
status=scheduled,published
```

**Response (200 OK):**

```json
{
  "success": true,
  "data": [
    {
      "scheduledItemId": "sched_456uvw",
      "draftId": "draft_789xyz",
      "title": "My Updated Awesome New Post",
      "scheduledTime": "2025-05-21T10:00:00Z",
      "platform": "instagram",
      "status": "scheduled"
    }
    // ... other calendar items
  ],
  "pagination": {
    "total": 1,
    "limit": 100, // Default or max limit for calendar view
    "offset": 0
  }
}
```

This API provides comprehensive control over your content lifecycle within CherryBomb, from drafting to scheduling and monitoring.
