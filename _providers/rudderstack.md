---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Rudderstack Agentic Access
  operation_count: 12
  slug: rudderstack-agentic-access
  summary_line: 12 operations · 12 acting
api_count: 13
apis:
- description: The RudderStack Config Backend API manages workspace configuration objects — sources, destinations, connections, and workspace settings — supporting full programmatic provisioning of pipelines outside
  name: RudderStack Config Backend API
  slug: rudderstack-config-backend-api
- description: The RudderStack Transformations API manages user-defined transformation functions (JavaScript, with Python on Enterprise) attached to a destination connection to filter, mask, enrich, or reshape event
  name: RudderStack Transformations API
  slug: rudderstack-transformations-api
- description: The RudderStack Tracking Plan API defines and enforces the canonical event schema (events, properties, traits, types, required fields) used to validate ingested events and surface violations.
  name: RudderStack Tracking Plan API
  slug: rudderstack-tracking-plan-api
- description: The RudderStack Data Catalog API exposes the inventory of events and properties seen across all sources, supporting schema discovery, lineage, and governance reporting.
  name: RudderStack Data Catalog API
  slug: rudderstack-data-catalog-api
- description: The RudderStack Profiles API powers warehouse-native identity resolution, customer feature engineering, and unified Customer 360 model definitions executed inside the customer's data warehouse.
  name: RudderStack Profiles API
  slug: rudderstack-profiles-api
- description: The RudderStack Audiences API builds and manages audience definitions in the warehouse and activates them across destinations via Reverse ETL.
  name: RudderStack Audiences API
  slug: rudderstack-audiences-api
- description: The RudderStack Reverse ETL API manages warehouse-source-to-SaaS-destination syncs, including model definitions, sync schedules, run history, and incremental cursor management.
  name: RudderStack Reverse ETL API
  slug: rudderstack-reverse-etl-api
- description: The RudderStack Event Stream API manages real-time event-stream pipelines — sources, destinations, connections, event filters, and feature toggles — that route events from collection to downstream too
  name: RudderStack Event Stream API
  slug: rudderstack-event-stream-api
- description: The RudderStack Webhook Source API receives inbound webhooks from third-party SaaS tools and normalizes them into RudderStack events for downstream routing.
  name: RudderStack Webhook Source API
  slug: rudderstack-webhook-source-api
- description: The RudderStack Warehouse Destination API configures and operates loads into supported warehouses (Snowflake, BigQuery, Redshift, Postgres, Databricks, Trino, S3 Data Lake) with configurable sync inte
  name: RudderStack Warehouse Destination API
  slug: rudderstack-warehouse-destination-api
- description: The RudderStack Orchestration API integrates with Airflow and Dagster to coordinate Reverse ETL syncs, Profiles model runs, and other RudderStack jobs from external orchestration systems.
  name: RudderStack Orchestration API
  slug: rudderstack-orchestration-api
- description: The HTTP API API from RudderStack — 7 operation(s) for http api.
  name: RudderStack HTTP API API
  slug: rudderstack-http-api-api
- description: The Internal API API from RudderStack — 5 operation(s) for internal api.
  name: RudderStack Internal API API
  slug: rudderstack-internal-api-api
artifact_total: 23
asyncapis:
- description: AsyncAPI 2.6 specification describing RudderStack's event-streaming surfaces over HTTP. RudderStack ingests customer events server-side via the HTTP Tracking API (identify, track, page, screen, group,
  name: RudderStack Event Streaming API
  slug: rudderstack-event-streaming-asyncapi
collections:
- collection_type: open
  name: RudderStack HTTP API
  slug: open-rudderstack-gateway
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rudderstack-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rudderstack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rudderstack-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rudderstack
- group: company
  title: ''
  type: Website
  url: https://www.rudderstack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.rudderstack.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.rudderstack.com/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.rudderstack.com/docs/get-started/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rudderstack.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://app.rudderstack.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.rudderstack.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rudderlabs
- group: other
  title: ''
  type: Open Source Server
  url: https://github.com/rudderlabs/rudder-server
- group: build
  title: ''
  type: JavaScript SDK
  url: https://github.com/rudderlabs/rudder-sdk-js
- group: build
  title: ''
  type: Node.js SDK
  url: https://github.com/rudderlabs/rudder-sdk-node
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/rudderlabs/rudder-sdk-python
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/rudderlabs/rudder-sdk-java
- group: build
  title: ''
  type: Go SDK
  url: https://github.com/rudderlabs/analytics-go
- group: build
  title: ''
  type: Ruby SDK
  url: https://github.com/rudderlabs/rudder-sdk-ruby
- group: build
  title: ''
  type: PHP SDK
  url: https://github.com/rudderlabs/rudder-sdk-php
- group: build
  title: ''
  type: .NET SDK
  url: https://github.com/rudderlabs/rudder-analytics-dotnet
- group: build
  title: ''
  type: iOS SDK
  url: https://github.com/rudderlabs/rudder-sdk-ios
- group: build
  title: ''
  type: Android SDK
  url: https://github.com/rudderlabs/rudder-sdk-android
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rudderstack.com/
- group: company
  title: ''
  type: Blog
  url: https://www.rudderstack.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.rudderstack.com/docs/release-notes/
- group: commercial
  title: ''
  type: License
  url: https://github.com/rudderlabs/rudder-server/blob/master/LICENSE.md
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/RudderStack
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/RudderStack
- group: operate
  title: ''
  type: Slack Community
  url: https://www.rudderstack.com/join-rudderstack-slack-community/
- group: commercial
  title: ''
  type: Plans
  url: plans/rudderstack-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rudderstack-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rudderstack-finops.yml
created: '2026-05-08'
description: RudderStack is a warehouse-native customer data platform (CDP) for developers, with open-source data plane SDKs (rudder-server) and a managed control plane. The platform exposes an HTTP Tracking (Event Stream) API for ingest, a Config Backend API for managing sources/destinations/connections, a Transformations API for in-flight event transforms, a Tracking Plan API for schema governance, a Profiles API for identity resolution and audiences, and a Reverse ETL API for warehouse-to-SaaS sync.
finops:
- name: Rudderstack Finops
  service_category: Customer Data Platform
  slug: rudderstack-finops
graphqls:
- description: This conceptual GraphQL schema models the RudderStack customer data platform (CDP) API surface. RudderStack is a warehouse-native CDP for developers that provides an open-source data plane and a manag
  name: RudderStack GraphQL Schema
  slug: rudderstack-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rudderstack.png
layout: provider
modified: '2026-05-30'
name: RudderStack
nav: Providers
network: true
overview: 'RudderStack publishes 3 APIs on the [APIs.io](https://apis.io/) network: Webhook Source API, HTTP API API, and Internal API API. Tagged areas include Customer Data Platform, CDP, Data Pipeline, Open Source, and Event Streaming.


  The RudderStack catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  RudderStack''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 26 more developer resources.'
plans:
- name: Rudderstack Plans Pricing
  plan_count: 5
  slug: rudderstack-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 6
  name: Rudderstack Rate Limits
  slug: rudderstack-rate-limits
rules:
- name: RudderStack API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: rudderstack-asyncapi-spectral-rules
score:
  band: strong
  composite: 65.0
  delta: 0.8
  facets:
    commercial_clarity: 63.2
    contract_quality: 71.2
    developer_ergonomics: 54.3
    discoverability: 75.0
    governance: 60.5
    operational_transparency: 68.4
  previous_composite: 64.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rudderstack/refs/heads/main/screenshots/rudderstack-2026-06-20T193249.png
security:
- kind: authentication
  name: Rudderstack Authentication
  slug: rudderstack-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rudderstack Domain Security
  slug: rudderstack-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rudderstack
tags:
- Customer Data Platform
- CDP
- Data Pipeline
- Open Source
- Event Streaming
- Reverse ETL
- Analytics
- Identity Resolution
website: https://www.rudderstack.com/
---
