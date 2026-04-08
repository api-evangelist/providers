---
aid: matomo
url: https://raw.githubusercontent.com/api-evangelist/matomo/refs/heads/main/apis.yml
apis:
- aid: matomo:reporting-api
  name: Matomo Reporting API
  description: The Matomo Reporting API provides programmatic access to all analytics reports available in the Matomo interface. It exposes over 200 API methods organized into modules such as VisitsSummary, Actions, Referrers, UserCountry, DevicesDetection, Goals, and more. Each module provides methods to retrieve metrics, dimensions, and segmented data for building custom dashboards and reporting tools.
  humanURL: https://developer.matomo.org/api-reference/reporting-api
  tags:
  - Analytics
  - Dashboards
  - Metrics
  - Reporting
  properties:
  - type: Documentation
    url: https://developer.matomo.org/api-reference/reporting-api
  - type: GettingStarted
    url: https://developer.matomo.org/api-reference/reporting-api-introduction
- aid: matomo:tracking-api
  name: Matomo Tracking API
  description: The Matomo Tracking API allows developers to send tracking data to Matomo from any server-side application, mobile app, or IoT device via HTTP requests. It supports recording pageviews, custom events, e-commerce transactions, content interactions, site search queries, and custom dimensions. The API also supports bulk tracking for sending multiple events in a single request.
  humanURL: https://developer.matomo.org/api-reference/tracking-api
  tags:
  - Analytics
  - Events
  - Server-Side
  - Tracking
  properties:
  - type: Documentation
    url: https://developer.matomo.org/api-reference/tracking-api
- aid: matomo:live-api
  name: Matomo Live API
  description: The Matomo Live API provides real-time access to visitor data including the most recent visits, visitor profiles, and live counters showing current visitors on the site. It enables developers to build real-time dashboards, visitor activity feeds, and monitoring tools that display up-to-the-minute analytics data.
  humanURL: https://developer.matomo.org/api-reference/reporting-api#Live
  tags:
  - Analytics
  - Live Data
  - Real-Time
  - Visitors
  properties:
  - type: Documentation
    url: https://developer.matomo.org/api-reference/reporting-api#Live
- aid: matomo:goals-api
  name: Matomo Goals API
  description: The Matomo Goals API allows developers to manage and retrieve data about conversion goals. It supports creating, updating, and deleting goals, as well as retrieving goal conversion metrics, revenue data, and conversion rates segmented by various dimensions such as referrer, country, and device type.
  humanURL: https://developer.matomo.org/api-reference/reporting-api#Goals
  tags:
  - Analytics
  - Conversions
  - Goals
  - Revenue
  properties:
  - type: Documentation
    url: https://developer.matomo.org/api-reference/reporting-api#Goals
- aid: matomo:segments-api
  name: Matomo Segments API
  description: The Matomo Segments API enables developers to create and manage saved segments for filtering analytics data. Segments allow filtering visits and actions by any combination of visitor properties, behavior patterns, and custom dimensions. Any Reporting API method can accept a segment parameter to return data for a specific subset of visitors.
  humanURL: https://developer.matomo.org/api-reference/reporting-api-segmentation
  tags:
  - Analytics
  - Filters
  - Segmentation
  - Visitors
  properties:
  - type: Documentation
    url: https://developer.matomo.org/api-reference/reporting-api-segmentation
name: Matomo
tags:
- Analytics
- Data Ownership
- Open Source
- Privacy
- Self-Hosted
- Web Analytics
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Matomo is an open source web analytics platform that provides comprehensive website and application usage analytics with full data ownership. Formerly known as Piwik, it offers an alternative to Google Analytics with on-premise or cloud hosting options, ensuring complete control over analytics data and compliance with privacy regulations including GDPR.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

