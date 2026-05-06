---
aid: swetrix
name: Swetrix
description: Swetrix is an open source, privacy-focused web analytics platform that provides cookieless tracking, real-time dashboards, and GDPR-compliant analytics without collecting personal data. It offers a fully-featured REST API for tracking events, querying statistics, managing projects, and integrating analytics into custom applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Cookieless Tracking
  - GDPR Compliant
  - Open Source
  - Privacy
  - Real-Time Analytics
  - Web Analytics
url: https://raw.githubusercontent.com/api-evangelist/swetrix/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: swetrix:swetrix-events-api
    name: Swetrix Events API
    description: The Swetrix Events API provides endpoints for recording pageview events, custom events, heartbeat events, error events, and revenue transactions. Used for sending analytics data from client or server-side applications to Swetrix analytics projects.
    humanURL: https://swetrix.com/docs/events-api
    baseURL: https://api.swetrix.com
    properties:
      - type: Documentation
        url: https://swetrix.com/docs/events-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/swetrix/refs/heads/main/openapi/swetrix-events-api-openapi.yml
    tags:
      - Analytics
      - Cookieless Tracking
      - Custom Events
      - Error Tracking
      - Events
      - Pageviews
      - Revenue Tracking
  - aid: swetrix:swetrix-statistics-api
    name: Swetrix Statistics API
    description: The Swetrix Statistics API enables querying aggregated analytics data including traffic logs, performance metrics, session details, funnel analysis, user flows, error overviews, and feature flag statistics. Authenticated with an X-Api-Key header.
    humanURL: https://swetrix.com/docs/statistics-api
    baseURL: https://api.swetrix.com
    properties:
      - type: Documentation
        url: https://swetrix.com/docs/statistics-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/swetrix/refs/heads/main/openapi/swetrix-statistics-api-openapi.yml
    tags:
      - Analytics
      - Funnels
      - Performance
      - Statistics
      - Traffic
  - aid: swetrix:swetrix-admin-api
    name: Swetrix Admin API
    description: The Swetrix Admin API manages projects, funnels, annotations, project views (segments), and organisations. Supports full CRUD operations for analytics project management. Authenticated with an X-Api-Key header.
    humanURL: https://swetrix.com/docs/admin-api
    baseURL: https://api.swetrix.com
    properties:
      - type: Documentation
        url: https://swetrix.com/docs/admin-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/swetrix/refs/heads/main/openapi/swetrix-admin-api-openapi.yml
    tags:
      - Administration
      - Analytics
      - Organisations
      - Project Management
      - Projects
common:
  - type: Website
    url: https://swetrix.com
  - type: Documentation
    url: https://docs.swetrix.com
  - type: Blog
    url: https://swetrix.com/blog
  - type: Pricing
    url: https://swetrix.com/pricing
  - type: GitHub
    url: https://github.com/Swetrix/swetrix
  - type: GitHubOrganization
    url: https://github.com/Swetrix
  - type: Login
    url: https://swetrix.com/login
  - type: Signup
    url: https://swetrix.com/signup
  - type: Support
    url: https://swetrix.com/contact
  - type: OpenSource
    url: https://github.com/Swetrix/swetrix-api
  - type: SDK
    url: https://github.com/Swetrix/swetrix-js
  - type: SDK
    url: https://github.com/Swetrix/swetrix-nextjs
  - type: SDK
    url: https://github.com/Swetrix/swetrix-browser
  - type: SDK
    url: https://github.com/Swetrix/django-plugin
  - type: Status
    url: https://swetrix.com/status
  - type: TermsOfService
    url: https://swetrix.com/privacy
  - type: PrivacyPolicy
    url: https://swetrix.com/privacy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
