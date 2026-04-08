---
aid: mixpanel
url: https://raw.githubusercontent.com/api-evangelist/mixpanel/refs/heads/main/apis.yml
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
name: Mixpanel
tags:
- Analytics
- Data Analysis
- Event Tracking
- Product Analytics
- User Behavior
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Mixpanel is a business analytics service company that tracks user interactions with web and mobile applications and provides tools for targeted communication with them.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

