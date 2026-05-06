---
aid: mixpanel
name: Mixpanel
description: Mixpanel is a business analytics service company that tracks user interactions with web and mobile applications and provides tools for targeted communication with them.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://mixpanel.com
created: '2024'
modified: '2026-05-04'
specificationVersion: '0.19'
apis:
  - name: Mixpanel Ingestion API
    description: API for sending event data to Mixpanel for tracking and analysis, including importing events, tracking events, managing user profiles, group profiles, and lookup tables.
    image: https://mixpanel.com/wp-content/uploads/2021/07/mixpanel-logo.svg
    humanURL: https://developer.mixpanel.com/reference/ingestion-api
    baseURL: https://api.mixpanel.com
    tags:
      - Analytics
      - Events
      - Group Profiles
      - Ingestion
      - Tracking
      - User Profiles
    properties:
      - type: Documentation
        url: https://developer.mixpanel.com/reference/ingestion-api
      - type: OpenAPI
        url: https://developer.mixpanel.com/reference/openapi
      - type: OpenAPI
        url: openapi/mixpanel-ingestion-openapi.yml
    contact:
      - FN: Mixpanel Support
        email: support@mixpanel.com
        url: https://mixpanel.com/get-support
  - name: Mixpanel Query API
    description: API for querying and retrieving analytics data from Mixpanel, including cohorts, funnels, insights, retention, segmentation, activity feeds, and event breakdowns.
    image: https://mixpanel.com/wp-content/uploads/2021/07/mixpanel-logo.svg
    humanURL: https://developer.mixpanel.com/reference/query-api
    baseURL: https://mixpanel.com/api
    tags:
      - Analytics
      - Cohorts
      - Data Export
      - Funnels
      - Query
      - Retention
      - Segmentation
    properties:
      - type: Documentation
        url: https://developer.mixpanel.com/reference/query-api
      - type: OpenAPI
        url: https://developer.mixpanel.com/reference/openapi
      - type: OpenAPI
        url: openapi/mixpanel-query-openapi.yml
    contact:
      - FN: Mixpanel Support
        email: support@mixpanel.com
        url: https://mixpanel.com/get-support
  - name: Mixpanel Data Pipelines API
    description: API for creating, managing, and monitoring data export pipelines in Mixpanel, including creating, editing, pausing, resuming, and deleting pipelines.
    image: https://mixpanel.com/wp-content/uploads/2021/07/mixpanel-logo.svg
    humanURL: https://developer.mixpanel.com/reference/overview-2
    baseURL: https://data.mixpanel.com
    tags:
      - Data Pipeline
      - Export
      - Import
    properties:
      - type: Documentation
        url: https://developer.mixpanel.com/reference/raw-data-export-api
      - type: OpenAPI
        url: https://developer.mixpanel.com/reference/openapi
      - type: OpenAPI
        url: openapi/mixpanel-data-pipelines-openapi.yml
    contact:
      - FN: Mixpanel Support
        email: support@mixpanel.com
        url: https://mixpanel.com/get-support
  - name: Mixpanel Identity API
    description: API for managing user identity in Mixpanel, including creating identities, creating aliases, and merging identities to accurately resolve users across multiple devices.
    image: https://mixpanel.com/wp-content/uploads/2021/07/mixpanel-logo.svg
    humanURL: https://developer.mixpanel.com/reference/create-identity
    baseURL: https://api.mixpanel.com
    tags:
      - ID Merge
      - Identity
      - User Management
    properties:
      - type: Documentation
        url: https://developer.mixpanel.com/reference/create-identity
      - type: OpenAPI
        url: openapi/mixpanel-identity-openapi.yml
    contact:
      - FN: Mixpanel Support
        email: support@mixpanel.com
        url: https://mixpanel.com/get-support
  - name: Mixpanel Event Export API
    description: API for downloading raw event data as it is received and stored within Mixpanel, complete with all event properties including distinct_id and exact timestamps.
    image: https://mixpanel.com/wp-content/uploads/2021/07/mixpanel-logo.svg
    humanURL: https://developer.mixpanel.com/reference/raw-event-export
    baseURL: https://data.mixpanel.com/api/2.0
    tags:
      - Data Export
      - Events
      - Raw Data
    properties:
      - type: Documentation
        url: https://developer.mixpanel.com/reference/raw-event-export
      - type: OpenAPI
        url: openapi/mixpanel-event-export-openapi.yml
    contact:
      - FN: Mixpanel Support
        email: support@mixpanel.com
        url: https://mixpanel.com/get-support
  - name: Mixpanel Lexicon Schemas API
    description: API for syncing your internal data dictionary or tracking plan with Mixpanel using schemas, allowing you to create, replace, retrieve, and delete schema definitions that describe the data you send to Mixpanel.
    image: https://mixpanel.com/wp-content/uploads/2021/07/mixpanel-logo.svg
    humanURL: https://developer.mixpanel.com/reference/lexicon-schemas-api
    baseURL: https://mixpanel.com/api/app
    tags:
      - Data Dictionary
      - Data Governance
      - Lexicon
      - Schemas
    properties:
      - type: Documentation
        url: https://developer.mixpanel.com/reference/lexicon-schemas-api
      - type: OpenAPI
        url: openapi/mixpanel-lexicon-schemas-openapi.yml
    contact:
      - FN: Mixpanel Support
        email: support@mixpanel.com
        url: https://mixpanel.com/get-support
  - name: Mixpanel Service Accounts API
    description: API for programmatically managing service accounts within your organization, including creating, deleting, listing service accounts, and managing their project memberships.
    image: https://mixpanel.com/wp-content/uploads/2021/07/mixpanel-logo.svg
    humanURL: https://developer.mixpanel.com/reference/service-accounts-api
    baseURL: https://mixpanel.com/api/app
    tags:
      - Administration
      - Authentication
      - Service Accounts
    properties:
      - type: Documentation
        url: https://developer.mixpanel.com/reference/service-accounts-api
      - type: OpenAPI
        url: openapi/mixpanel-service-accounts-openapi.yml
    contact:
      - FN: Mixpanel Support
        email: support@mixpanel.com
        url: https://mixpanel.com/get-support
  - name: Mixpanel Annotations API
    description: API for creating, retrieving, updating, and deleting annotations that label specific points in time on Mixpanel charts with descriptions, useful for marking product launches, campaigns, or data anomalies.
    image: https://mixpanel.com/wp-content/uploads/2021/07/mixpanel-logo.svg
    humanURL: https://developer.mixpanel.com/reference/create-annotation
    baseURL: https://mixpanel.com/api/app
    tags:
      - Annotations
      - Charts
      - Reports
    properties:
      - type: Documentation
        url: https://developer.mixpanel.com/reference/create-annotation
      - type: OpenAPI
        url: openapi/mixpanel-annotations-openapi.yml
    contact:
      - FN: Mixpanel Support
        email: support@mixpanel.com
        url: https://mixpanel.com/get-support
  - name: Mixpanel GDPR and CCPA API
    description: API for submitting data retrieval and deletion requests to help meet GDPR and CCPA compliance requirements, including creating and checking the status of retrieval and deletion tasks.
    image: https://mixpanel.com/wp-content/uploads/2021/07/mixpanel-logo.svg
    humanURL: https://developer.mixpanel.com/reference/gdpr-api
    baseURL: https://mixpanel.com/api/app
    tags:
      - CCPA
      - Compliance
      - Data Deletion
      - Data Retrieval
      - GDPR
      - Privacy
    properties:
      - type: Documentation
        url: https://developer.mixpanel.com/reference/gdpr-api
      - type: OpenAPI
        url: openapi/mixpanel-gdpr-ccpa-openapi.yml
    contact:
      - FN: Mixpanel Support
        email: support@mixpanel.com
        url: https://mixpanel.com/get-support
  - name: Mixpanel Warehouse Connectors API
    description: API for connecting a data warehouse to import events, users, groups, and lookup tables into Mixpanel, and for manually triggering specific warehouse import runs.
    image: https://mixpanel.com/wp-content/uploads/2021/07/mixpanel-logo.svg
    humanURL: https://developer.mixpanel.com/reference/warehouse-connectors-api
    baseURL: https://mixpanel.com/api/app
    tags:
      - Connectors
      - Data Import
      - Integrations
      - Warehouse
    properties:
      - type: Documentation
        url: https://developer.mixpanel.com/reference/warehouse-connectors-api
      - type: OpenAPI
        url: openapi/mixpanel-warehouse-connectors-openapi.yml
    contact:
      - FN: Mixpanel Support
        email: support@mixpanel.com
        url: https://mixpanel.com/get-support
common:
  - type: Portal
    url: https://developer.mixpanel.com/
  - type: Getting Started
    url: https://developer.mixpanel.com/docs/getting-started
  - type: Authentication
    url: https://developer.mixpanel.com/reference/authentication
  - type: SDKs
    url: https://developer.mixpanel.com/docs/sdks
  - type: Rate Limits
    url: https://developer.mixpanel.com/reference/rate-limits
  - type: API Status
    url: https://www.mixpanelstatus.com/
  - type: Change Log
    url: https://docs.mixpanel.com/changelogs
  - type: GitHub Organization
    url: https://github.com/mixpanel
  - type: Integrations
    url: https://mixpanel.com/partners/integrations
  - type: Security
    url: https://mixpanel.com/legal/security-overview/
  - type: Login
    url: https://mixpanel.com/login/
  - type: Sign Up
    url: https://mixpanel.com/register/
  - type: Terms of Service
    url: https://mixpanel.com/legal/terms-of-use
  - type: Privacy Policy
    url: https://mixpanel.com/legal/privacy-policy
  - type: Pricing
    url: https://mixpanel.com/pricing
  - type: Blog
    url: https://mixpanel.com/blog
  - type: Support
    url: https://mixpanel.com/get-support
  - type: JSON-LD
    url: json-ld/mixpanel-context.jsonld
  - type: JSONSchema
    url: json-schema/mixpanel-event-schema.json
  - type: JSONSchema
    url: json-schema/mixpanel-user-profile-schema.json
  - type: JSONSchema
    url: json-schema/mixpanel-funnel-schema.json
  - type: Features
    data:
      - 'Free: 1M events/mo, 5 saved reports, 10K replays'
      - 'Growth: $0.28 per 1K events above 1M free, up to 20M'
      - 'Enterprise: unlimited events, custom contract'
      - Spark AI for natural-language queries (60 free/mo on Growth)
      - 'Ingestion API: ~2,000 events/sec/IP recommended'
      - 'Batch import: 2,000 events per request'
      - 'Query API: 60 queries/hr, 5 concurrent'
      - Webhooks for cohort changes and signal alerts
      - OAuth 2.0 and project tokens / service accounts
      - Behavioral cohorts and funnel analysis
      - Web Experimentation
      - Session Replay across web and mobile
      - Lexicon for tracking plan governance
      - Group analytics for B2B accounts
      - Cohort Sync to ad platforms and CDPs
      - Data residency in EU/IN regions
    sources:
      - https://mixpanel.com/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
tags:
  - Analytics
  - Data Analysis
  - Event Tracking
  - Product Analytics
  - User Behavior
---
