---
aid: amplitude
url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/apis.yml
modified: '2026-05-04'
name: Amplitude
description: Amplitude is a digital analytics platform that helps product teams understand user behavior, run experiments, and drive growth. It provides a suite of APIs for event ingestion, user management, cohort syncing, taxonomy governance, A/B testing, and data export. Amplitude is widely used by product, data, and engineering teams to build better digital experiences through data-driven insights.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - A/B Testing
  - Analytics
  - Experimentation
  - Feature Flags
  - Product Analytics
  - User Behavior
apis:
  - aid: amplitude:http-v2-api
    name: Amplitude HTTP V2 API
    tags:
      - Analytics
      - Events
      - Ingestion
      - Tracking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api2.amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/http-v2
    properties:
      - url: https://amplitude.com/docs/apis/analytics/http-v2
        type: Documentation
      - url: openapi/amplitude-http-v2-api-openapi.yml
        type: OpenAPI
    description: The Amplitude HTTP V2 API enables developers to send event data directly from servers or clients to Amplitude's analytics platform. It supports uploading individual or batched events along with user properties, event properties, and group properties. This API is the primary method for server-side event ingestion and is designed for high-throughput data collection with built-in validation and error reporting.
  - aid: amplitude:batch-event-upload-api
    name: Amplitude Batch Event Upload API
    tags:
      - Analytics
      - Batch
      - Events
      - Ingestion
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api2.amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/batch-event-upload
    properties:
      - url: https://amplitude.com/docs/apis/analytics/batch-event-upload
        type: Documentation
    description: The Amplitude Batch Event Upload API is optimized for high-volume server-side event ingestion. It accepts batches of events up to 20MB per request and is designed for use cases where data volume may exceed the limits of the standard HTTP V2 API. The API uses the same event structure as the HTTP V2 API and is recommended for data pipelines processing millions of events.
  - aid: amplitude:identify-api
    name: Amplitude Identify API
    tags:
      - Analytics
      - Identity
      - Properties
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api2.amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/identify
    properties:
      - url: https://amplitude.com/docs/apis/analytics/identify
        type: Documentation
      - url: openapi/amplitude-identify-api-openapi.yml
        type: OpenAPI
    description: The Amplitude Identify API allows developers to update user properties for a specific user without needing to send an accompanying event. This is useful for setting or modifying user attributes such as demographics, subscription status, or preferences outside of the normal event tracking flow. The API supports operations like set, unset, append, and prepend on user properties.
  - aid: amplitude:group-identify-api
    name: Amplitude Group Identify API
    tags:
      - Analytics
      - Groups
      - Identity
      - Properties
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api2.amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/group-identify
    properties:
      - url: https://amplitude.com/docs/apis/analytics/group-identify
        type: Documentation
    description: The Amplitude Group Identify API allows developers to set or update properties on groups within Amplitude. Groups are entities such as companies, teams, or accounts that users belong to. This API enables B2B analytics use cases by attaching account-level properties to groups for segmentation and reporting purposes.
  - aid: amplitude:dashboard-rest-api
    name: Amplitude Dashboard REST API
    tags:
      - Analytics
      - Dashboards
      - Metrics
      - Reporting
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/dashboard-rest
    properties:
      - url: https://amplitude.com/docs/apis/analytics/dashboard-rest
        type: Documentation
      - url: openapi/amplitude-dashboard-rest-api-openapi.yml
        type: OpenAPI
    description: The Amplitude Dashboard REST API provides programmatic access to the same data displayed in Amplitude's dashboard charts and graphs. It returns results in JSON format and supports queries filtered by event types, user segments, cohorts, and date ranges. Developers can use this API to build custom reporting tools, export chart data, or integrate Amplitude analytics into external dashboards and business intelligence systems.
  - aid: amplitude:export-api
    name: Amplitude Export API
    tags:
      - Analytics
      - Data
      - Events
      - Export
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/export
    properties:
      - url: https://amplitude.com/docs/apis/analytics/export
        type: Documentation
      - url: openapi/amplitude-export-api-openapi.yml
        type: OpenAPI
    description: The Amplitude Export API enables bulk export of raw event data for a given project within a specified date range. Results are returned as zipped archives of JSON files containing complete event records with timestamps, user properties, device information, and attribution data. This API is commonly used for data warehousing, offline analysis, and feeding event data into external processing pipelines.
  - aid: amplitude:behavioral-cohorts-api
    name: Amplitude Behavioral Cohorts API
    tags:
      - Analytics
      - Cohorts
      - Segmentation
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/behavioral-cohorts
    properties:
      - url: https://amplitude.com/docs/apis/analytics/behavioral-cohorts
        type: Documentation
      - url: openapi/amplitude-behavioral-cohorts-api-openapi.yml
        type: OpenAPI
    description: The Amplitude Behavioral Cohorts API allows developers to list, export, and upload cohorts in Amplitude. Cohorts are groups of users defined by shared behavioral patterns or properties. This API supports downloading cohort membership lists, creating new cohorts from external data, and retrieving cohort metadata. It is commonly used for syncing audience segments with marketing platforms, CRMs, and other downstream tools.
  - aid: amplitude:taxonomy-api
    name: Amplitude Taxonomy API
    tags:
      - Analytics
      - Data Governance
      - Events
      - Taxonomy
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/taxonomy
    properties:
      - url: https://amplitude.com/docs/apis/analytics/taxonomy
        type: Documentation
      - url: openapi/amplitude-taxonomy-api-openapi.yml
        type: OpenAPI
    description: The Amplitude Taxonomy API provides programmatic management of your analytics tracking plan. It supports creating, reading, updating, and deleting event categories, event types, event properties, and user properties. This API is essential for data governance workflows, enabling teams to maintain a consistent and well-organized event taxonomy across their instrumentation without needing to use the Amplitude UI directly.
  - aid: amplitude:attribution-api
    name: Amplitude Attribution API
    tags:
      - Analytics
      - Attribution
      - Campaigns
      - Marketing
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api2.amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/attribution
    properties:
      - url: https://amplitude.com/docs/apis/analytics/attribution
        type: Documentation
      - url: openapi/amplitude-attribution-api-openapi.yml
        type: OpenAPI
    description: The Amplitude Attribution API allows developers to send attribution campaign events to Amplitude from ad networks, attribution providers, or custom marketing tools. It associates users with the campaigns, channels, and creatives that drove their acquisition or re-engagement. This API is used to enrich Amplitude user profiles with marketing attribution data for campaign performance analysis and ROI measurement.
  - aid: amplitude:chart-annotations-api
    name: Amplitude Chart Annotations API
    tags:
      - Analytics
      - Annotations
      - Charts
      - Reporting
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/chart-annotations
    properties:
      - url: https://amplitude.com/docs/apis/analytics/chart-annotations
        type: Documentation
      - url: openapi/amplitude-chart-annotations-api-openapi.yml
        type: OpenAPI
    description: The Amplitude Chart Annotations API enables developers to programmatically create, retrieve, update, and delete annotations on Amplitude charts. Annotations mark significant events such as product releases, marketing campaigns, or incidents on timeline-based charts. This API allows teams to automate annotation management as part of their deployment or release pipelines, ensuring that important context is always visible alongside analytics data.
  - aid: amplitude:releases-api
    name: Amplitude Releases API
    tags:
      - Analytics
      - Deployments
      - Releases
      - Tracking
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/releases
    properties:
      - url: https://amplitude.com/docs/apis/analytics/releases
        type: Documentation
    description: The Amplitude Releases API allows developers to programmatically track software releases and deployments in Amplitude. By recording release events, teams can correlate product changes with analytics metrics to understand the impact of each deployment on user behavior, retention, and engagement.
  - aid: amplitude:session-replay-api
    name: Amplitude Session Replay API
    tags:
      - Analytics
      - Replay
      - Sessions
      - User Experience
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/session-replay
    properties:
      - url: https://amplitude.com/docs/apis/analytics/session-replay
        type: Documentation
    description: The Amplitude Session Replay API enables developers to upload and manage session replay data for playback within Amplitude. Session replays provide qualitative insights by recording user interactions and pairing them with quantitative analytics data. This API is used for server-side ingestion of session replay events and metadata.
  - aid: amplitude:user-profile-api
    name: Amplitude User Profile API
    tags:
      - Analytics
      - Profiles
      - Recommendations
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://profile-api.amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/user-profile
    properties:
      - url: https://amplitude.com/docs/apis/analytics/user-profile
        type: Documentation
      - url: openapi/amplitude-user-profile-api-openapi.yml
        type: OpenAPI
    description: The Amplitude User Profile API serves user profiles that include user properties, computed user properties, a list of cohort IDs the user belongs to, and personalized recommendations. It enables real-time access to enriched user data for powering personalization engines, in-app experiences, and targeted content delivery. This API is particularly useful for retrieving recommendation results generated by Amplitude's machine learning models.
  - aid: amplitude:user-mapping-api
    name: Amplitude User Mapping API
    tags:
      - Aliasing
      - Analytics
      - Identity
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api2.amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/user-mapping
    properties:
      - url: https://amplitude.com/docs/apis/analytics/user-mapping
        type: Documentation
      - url: openapi/amplitude-user-mapping-api-openapi.yml
        type: OpenAPI
    description: The Amplitude User Mapping (Aliasing) API allows developers to merge users with different user IDs together in Amplitude. This is useful when a user initially interacts with a product anonymously and later creates an account, or when users have multiple identifiers across different systems. The API maps these distinct identities into a single unified user profile to ensure accurate analytics and attribution.
  - aid: amplitude:user-privacy-api
    name: Amplitude User Privacy API
    tags:
      - Compliance
      - GDPR
      - Privacy
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/user-privacy
    properties:
      - url: https://amplitude.com/docs/apis/analytics/user-privacy
        type: Documentation
    description: The Amplitude User Privacy API provides endpoints for managing user data in compliance with privacy regulations such as GDPR and CCPA. It supports requesting the deletion or suppression of user data by user ID or device ID, enabling organizations to fulfill data subject rights requests and maintain regulatory compliance.
  - aid: amplitude:scim-api
    name: Amplitude SCIM API
    tags:
      - Access Management
      - Identity
      - Provisioning
      - Users
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://analytics.amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/scim
    properties:
      - url: https://amplitude.com/docs/apis/analytics/scim
        type: Documentation
      - url: openapi/amplitude-scim-api-openapi.yml
        type: OpenAPI
    description: The Amplitude SCIM API implements the System for Cross-domain Identity Management (SCIM) 2.0 standard for automated user provisioning and deprovisioning. It allows identity providers such as Okta, Azure AD, and OneLogin to automatically create, update, and deactivate user accounts in Amplitude. This API is essential for enterprise organizations that need centralized user lifecycle management and compliance with security policies.
  - aid: amplitude:dsar-api
    name: Amplitude Data Subject Access Request API
    tags:
      - CCPA
      - Compliance
      - GDPR
      - Privacy
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://amplitude.com
    humanURL: https://amplitude.com/docs/apis/analytics/ccpa-dsar
    properties:
      - url: https://amplitude.com/docs/apis/analytics/ccpa-dsar
        type: Documentation
      - url: openapi/amplitude-dsar-api-openapi.yml
        type: OpenAPI
    description: The Amplitude Data Subject Access Request (DSAR) API enables organizations to programmatically handle privacy requests in compliance with GDPR, CCPA, and other data protection regulations. It supports submitting deletion requests for user data based on user IDs or device IDs. This API allows companies to automate their privacy compliance workflows and ensure timely processing of data subject requests at scale.
  - aid: amplitude:experiment-evaluation-api
    name: Amplitude Experiment Evaluation API
    tags:
      - A/B Testing
      - Experimentation
      - Feature Flags
      - Variants
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.lab.amplitude.com
    humanURL: https://amplitude.com/docs/apis/experiment/experiment-evaluation-api
    properties:
      - url: https://amplitude.com/docs/apis/experiment/experiment-evaluation-api
        type: Documentation
      - url: openapi/amplitude-experiment-evaluation-api-openapi.yml
        type: OpenAPI
    description: The Amplitude Experiment Evaluation API retrieves variant assignment data for users through remote evaluation. When called, it evaluates targeting rules and returns the assigned variant for each active experiment or feature flag. The API also tracks assignment events automatically in Amplitude Analytics. It is used by server-side applications that need to determine which experiment variant or feature flag value to serve to a given user in real time.
  - aid: amplitude:experiment-management-api
    name: Amplitude Experiment Management API
    tags:
      - A/B Testing
      - Experimentation
      - Feature Flags
      - Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://experiment.amplitude.com
    humanURL: https://amplitude.com/docs/apis/experiment/experiment-management-api
    properties:
      - url: https://amplitude.com/docs/apis/experiment/experiment-management-api
        type: Documentation
      - url: openapi/amplitude-experiment-management-api-openapi.yml
        type: OpenAPI
    description: The Amplitude Experiment Management API provides programmatic control over feature flags and experiments. It supports creating, updating, activating, and archiving experiments and flags, as well as managing deployments, variants, holdout groups, and mutual exclusion groups. This API enables teams to integrate experiment lifecycle management into their CI/CD pipelines, automate flag rollouts, and manage experimentation workflows without using the Amplitude UI.
common:
  - type: Portal
    url: https://amplitude.com
  - type: Documentation
    url: https://amplitude.com/docs
  - type: GettingStarted
    url: https://amplitude.com/docs/get-started
  - type: Authentication
    url: https://amplitude.com/docs/apis/authentication
  - type: SDK
    url: https://amplitude.com/docs/sdks
  - type: GitHubOrganization
    url: https://github.com/amplitude
  - type: Blog
    url: https://amplitude.com/blog
  - type: Academy
    url: https://academy.amplitude.com
  - type: Support
    url: https://help.amplitude.com
  - type: Pricing
    url: https://amplitude.com/pricing
  - type: StatusPage
    url: https://status.amplitude.com
  - type: TermsOfService
    url: https://amplitude.com/terms
  - type: PrivacyPolicy
    url: https://amplitude.com/privacy
  - type: JSONLD
    url: json-ld/amplitude-context.jsonld
  - type: JSONSchema
    url: json-schema/amplitude-event-schema.json
  - type: JSONSchema
    url: json-schema/amplitude-cohort-schema.json
  - type: JSONSchema
    url: json-schema/amplitude-experiment-schema.json
  - type: Features
    data:
      - 'Starter: 10K MTUs or 2M events free, unlimited sources'
      - 'Plus from $49/mo: 300K MTUs or 25M events, behavioral cohorts'
      - 'Growth custom: advanced analysis, Feature Experimentation'
      - 'Enterprise custom: cross-product, multi-armed bandit experiments'
      - 'HTTP V2 ingest: 10 events/sec per device/user_id'
      - 'Batch ingest: 2,000 events per request'
      - 'Dashboard REST: 360 queries/hr'
      - Webhooks via destinations and Cohort Sync
      - OAuth + API keys per project
      - Session Replay across web/mobile
      - Web Experimentation and Feature Experimentation
      - AI Feedback for natural-language analysis
      - Predictive audiences (Growth+)
      - Causal insights
      - Mutual exclusion groups for A/B test scaling
      - Cross-product analysis on Enterprise
    sources:
      - https://amplitude.com/pricing
    updated: '2026-05-04'
  - type: UseCases
    data:
      - name: Product Analytics
        description: Understand how users interact with your product to prioritize features and reduce churn.
      - name: Growth Experimentation
        description: Run controlled A/B tests to measure the causal impact of product changes.
      - name: Marketing Attribution
        description: Track campaign performance and ROI by connecting acquisition events to user behavior.
      - name: Data Warehouse Integration
        description: Export raw event data to Snowflake, BigQuery, or Redshift for custom analysis.
      - name: Audience Syndication
        description: Sync behavioral cohorts to ad platforms and CRMs for targeted marketing.
      - name: Compliance Automation
        description: Automate GDPR and CCPA data deletion workflows for privacy compliance.
      - name: Enterprise Identity Management
        description: Automate user provisioning and deprovisioning via SCIM integration with IdPs.
  - type: Integrations
    data:
      - name: Segment
        description: Route events from Segment's customer data platform to Amplitude.
      - name: Snowflake
        description: Export raw event data directly into Snowflake for warehouse-native analytics.
      - name: BigQuery
        description: Sync Amplitude data with Google BigQuery for custom SQL analysis.
      - name: Salesforce
        description: Enrich Salesforce CRM records with Amplitude behavioral cohort data.
      - name: HubSpot
        description: Sync audience cohorts from Amplitude to HubSpot for marketing automation.
      - name: Braze
        description: Power personalized messaging campaigns using Amplitude behavioral cohorts.
      - name: Okta
        description: Automate user provisioning in Amplitude via Okta using the SCIM API.
      - name: Slack
        description: Receive automated alerts and chart embeds from Amplitude in Slack channels.
  - type: SpectralRules
    url: rules/amplitude-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/amplitude-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/amplitude-analytics-ingestion.yaml
  - type: NaftikoCapability
    url: capabilities/amplitude-data-export-and-cohorts.yaml
  - type: NaftikoCapability
    url: capabilities/amplitude-experimentation.yaml
  - type: NaftikoCapability
    url: capabilities/amplitude-governance-and-taxonomy.yaml
  - type: NaftikoCapability
    url: capabilities/amplitude-identity-and-privacy.yaml
  - type: JSONStructure
    url: json-structure/behavioral-cohorts-api-cohort-request-response-structure.json
  - type: JSONStructure
    url: json-structure/dashboard-rest-api-user-search-result-structure.json
  - type: JSONStructure
    url: json-structure/scim-api-scim-group-request-structure.json
  - type: JSONStructure
    url: json-structure/http-v2-api-event-structure.json
  - type: JSONStructure
    url: json-structure/experiment-evaluation-api-flag-configuration-structure.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
