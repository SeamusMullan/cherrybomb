# Frontend Content Calendar

CherryBomb's Content Calendar is a key frontend component that allows users to plan, schedule, and visualize their social media content across multiple platforms. This document describes its features and functionality.

## Overview

The Content Calendar provides a visual interface for:

- Viewing scheduled and published posts.
- Drafting and scheduling new content.
- Rescheduling and editing existing content items.
- Filtering content by platform, status, or campaign.
- Identifying optimal posting times based on predictions.

## Key Features

```mermaid
graph TD
    ContentCalendar --> Views[Calendar Views]
    ContentCalendar --> ContentManagement[Content Management]
    ContentCalendar --> Scheduling[Scheduling & Optimization]
    ContentCalendar --> Filtering[Filtering & Search]
    ContentCalendar --> Integration[Integration with Other Modules]

    Views --> MonthView[Month View]
    Views --> WeekView[Week View]
    Views --> DayView[Day View]
    Views --> ListView[List View]

    ContentManagement --> CreateDraft[Create New Draft directly on Calendar]
    ContentManagement --> EditScheduled[Edit Scheduled Content]
    ContentManagement --> DragAndDrop[Drag & Drop Rescheduling]
    ContentManagement --> PostStatus[Visual Post Status (Draft, Scheduled, Published, Error)]

    Scheduling --> OptimalTimes[Optimal Posting Time Suggestions]
    Scheduling --> PlatformSpecific[Platform-Specific Scheduling]
    Scheduling --> RecurringPosts[Recurring Post Setup (e.g., weekly series)]

    Filtering --> FilterByPlatform[Filter by Platform]
    Filtering --> FilterByStatus[Filter by Status]
    Filtering --> FilterByCampaign[Filter by Campaign/Tag]
    Filtering --> SearchContent[Search Content by Keyword]

    Integration --> PredictionIntegration[Integration with Prediction Engine]
    Integration --> AssetLibrary[Access to Asset Library]
    Integration --> AnalyticsLink[Link to Performance Analytics of Published Posts]
```

### 1. Calendar Views

- **Month View**: Provides a broad overview of the content schedule for the entire month.
- **Week View**: Shows a more detailed schedule for the selected week.
- **Day View**: Focuses on the content scheduled for a specific day, often with hourly slots.
- **List View**: Displays scheduled content in a chronological list, useful for bulk actions or a compact overview.

### 2. Content Management

- **Create Drafts**: Users can click on a date/time slot to start creating a new content draft directly within the calendar interface.
- **Edit Content**: Scheduled posts can be easily edited (text, media, target platforms).
- **Drag & Drop Rescheduling**: Users can drag and drop content items to different dates or times to reschedule them.
- **Visual Status Indicators**: Posts are color-coded or marked with icons to indicate their status (e.g., draft, scheduled, published, needs approval, error in publishing).

### 3. Scheduling and Optimization

- **Optimal Posting Times**: The calendar can highlight suggested optimal posting times based on CherryBomb's prediction engine and historical data analysis.
- **Platform-Specific Scheduling**: Allows tailoring of content or posting times for different social media platforms if a single piece of content is cross-posted.
- **Recurring Posts**: Functionality to set up posts that repeat on a regular schedule.

### 4. Filtering and Search

- Users can filter the calendar view by:
  - Social media platform (e.g., show only Instagram posts).
  - Content status (e.g., show only drafts or only published content).
  - Campaigns or tags associated with the content.
- A search bar allows users to find specific content items within the calendar.

### 5. Integration with Other Modules

- **Prediction Engine**: When scheduling, users can see performance predictions for the chosen time slot.
- **Asset Library**: Easy access to an asset library (images, videos, templates) when creating content.
- **Analytics**: Published posts on the calendar can link directly to their performance analytics.

## User Interaction

- **Hover Details**: Hovering over a calendar item can show a quick summary of the post.
- **Click Actions**: Clicking on a calendar item typically opens it for editing or viewing details.
- **Context Menus**: Right-clicking might provide quick actions like duplicate, delete, or change status.

## Technical Aspects

- Built with React, utilizing a robust calendar component library (e.g., FullCalendar, React Big Calendar) adapted for CherryBomb's needs.
- State management for calendar events and filters.
- API integration for fetching, creating, and updating scheduled content.

The Content Calendar is designed to be a central tool for social media managers, streamlining their workflow and helping them to publish content more strategically.
