---
aid: amplitude
url: https://raw.githubusercontent.com/api-evangelist/amplitude/refs/heads/main/apis.yml
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
name: Amplitude
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Considerations Keep the following in mind as you use the HTTP V2 API. Rate limiting Amplitude rate.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

