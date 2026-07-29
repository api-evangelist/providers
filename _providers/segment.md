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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Segment Agentic Access
  operation_count: 72
  slug: segment-agentic-access
  summary_line: 72 operations · 34 acting
api_count: 23
apis:
- description: 'The Segment Pixel Tracking API provides a way to collect analytics data using image pixel requests, which is useful in environments where JavaScript cannot execute, such as email clients. It supports '
  name: Segment Pixel Tracking API
  slug: pixel-tracking-api
- description: Operations for merging two user identities together.
  name: segment Alias API
  slug: segment-alias-api
- description: Operations for sending multiple calls in a single request.
  name: segment Batch API
  slug: segment-batch-api
- description: Operations for browsing the Segment catalog of available sources and destination integrations.
  name: segment Catalog API
  slug: segment-catalog-api
- description: Operations for managing destinations where collected data is sent.
  name: segment Destinations API
  slug: segment-destinations-api
- description: Operations for retrieving events associated with a user or account profile.
  name: segment Events API
  slug: segment-events-api
- description: Operations for retrieving external identifiers linked to a user or account profile.
  name: segment External IDs API
  slug: segment-external-ids-api
- description: Operations for managing custom functions that transform or enrich data flowing through Segment.
  name: segment Functions API
  slug: segment-functions-api
- description: Operations for associating users with groups or organizations.
  name: segment Group API
  slug: segment-group-api
- description: Operations for identifying users and associating traits with them.
  name: segment Identify API
  slug: segment-identify-api
- description: Operations for managing labels used to organize and control access to workspace resources.
  name: segment Labels API
  slug: segment-labels-api
- description: Operations for retrieving linked profiles and relationships.
  name: segment Links API
  slug: segment-links-api
- description: Operations for recording page views on websites.
  name: segment Page API
  slug: segment-page-api
- description: Operations for retrieving user and account profile data from Segment Unify.
  name: segment Profiles API
  slug: segment-profiles-api
- description: Operations for managing data privacy regulations and suppression requests.
  name: segment Regulations API
  slug: segment-regulations-api
- description: Operations for recording screen views in mobile applications.
  name: segment Screen API
  slug: segment-screen-api
- description: Operations for managing data collection sources within a workspace.
  name: segment Sources API
  slug: segment-sources-api
- description: Operations for tracking events and actions performed by users.
  name: segment Track API
  slug: segment-track-api
- description: Operations for managing tracking plans that enforce data schemas.
  name: segment Tracking Plans API
  slug: segment-tracking-plans-api
- description: Operations for retrieving computed and custom traits for user and account profiles.
  name: segment Traits API
  slug: segment-traits-api
- description: Operations for managing transformations that modify event data before it reaches destinations.
  name: segment Transformations API
  slug: segment-transformations-api
- description: Operations for managing data warehouse connections, including creating and configuring warehouse destinations.
  name: segment Warehouses API
  slug: segment-warehouses-api
- description: Operations for retrieving workspace information and configuration.
  name: segment Workspaces API
  slug: segment-workspaces-api
artifact_total: 86
asyncapis:
- description: 'Segment Webhooks submit real-time user data to HTTP endpoints as POST requests. When configured as a destination, Segment forwards identify, track, page, screen, group, and alias events to up to five '
  name: Segment Webhook Events
  slug: segment-webhooks-asyncapi
collections:
- collection_type: open
  name: Segment Config API
  slug: open-segment-config-api
- collection_type: open
  name: Segment HTTP Tracking API
  slug: open-segment-http-tracking-api
- collection_type: open
  name: Segment Pixel Tracking API
  slug: open-segment-pixel-tracking-api
- collection_type: open
  name: Segment Profile API
  slug: open-segment-profile-api
- collection_type: open
  name: Segment Public API
  slug: open-segment-public-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/segment-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/segment-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/segment-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/segmentio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/segment-io
- group: design
  title: ''
  type: JSONLD
  url: json-ld/segment-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/segment-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/segment-source-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/segment-destination-schema.json
description: Segment is a customer data platform that helps companies collect, clean, and route customer data to hundreds of tools used for analytics, marketing, and data warehousing.
features:
- Free Developer plan up to ~1,000 visitors and 2 sources
- Customer Data Pipeline custom-quoted via sales
- Customer Data Platform (Unify + Engage) custom-quoted
- 700+ destinations including warehouses, advertising, analytics
- Tracking API up to 30,000 events/sec/source
- Public API at 600 req/min/workspace
- Functions for custom source/destination logic
- Reverse ETL for warehouse-to-tool syncs
- Identity resolution via Unify
- AI-powered audiences and predictions
- Generative audiences
- Protocols add-on for tracking plan governance
- OAuth 2.0 + workspace API tokens
- HIPAA-eligible regional CDP options
- Dedicated CSM on CDP plan
- Connections to 90+ warehouses including BigQuery, Snowflake, Databricks
finops:
- name: Segment Finops
  service_category: Customer Data Platform
  slug: segment-finops
graphqls:
- description: Segment GraphQL Schema
  name: Segment GraphQL
  slug: segment-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/segment.png
json_schemas:
- name: AliasCall
  property_count: 6
  slug: segment-aliascall
- name: BatchCall
  property_count: 3
  slug: segment-batchcall
- name: CatalogDestination
  property_count: 7
  slug: segment-catalogdestination
- name: CatalogSource
  property_count: 6
  slug: segment-catalogsource
- name: Context
  property_count: 7
  slug: segment-context
- name: Cursor
  property_count: 4
  slug: segment-cursor
- name: Segment Destination
  property_count: 7
  slug: segment-destination
- name: DestinationConfig
  property_count: 4
  slug: segment-destinationconfig
- name: Error
  property_count: 2
  slug: segment-error
- name: ErrorResponse
  property_count: 2
  slug: segment-errorresponse
- name: Segment Event
  property_count: 16
  slug: segment-event
- name: ExternalId
  property_count: 6
  slug: segment-externalid
- name: Function
  property_count: 9
  slug: segment-function
- name: FunctionSetting
  property_count: 6
  slug: segment-functionsetting
- name: GroupCall
  property_count: 8
  slug: segment-groupcall
- name: IdentifyCall
  property_count: 7
  slug: segment-identifycall
- name: Integrations
  property_count: 0
  slug: segment-integrations
- name: Label
  property_count: 3
  slug: segment-label
- name: PageCall
  property_count: 8
  slug: segment-pagecall
- name: Pagination
  property_count: 3
  slug: segment-pagination
- name: Regulation
  property_count: 6
  slug: segment-regulation
- name: ScreenCall
  property_count: 8
  slug: segment-screencall
- name: Segment Source
  property_count: 9
  slug: segment-source
- name: SuccessResponse
  property_count: 1
  slug: segment-successresponse
- name: TrackCall
  property_count: 8
  slug: segment-trackcall
- name: TrackingPlan
  property_count: 5
  slug: segment-trackingplan
- name: TrackingPlanRule
  property_count: 4
  slug: segment-trackingplanrule
- name: Transformation
  property_count: 9
  slug: segment-transformation
- name: Warehouse
  property_count: 4
  slug: segment-warehouse
- name: Workspace
  property_count: 4
  slug: segment-workspace
json_structures:
- name: Segment Structure
  property_count: 0
  slug: segment-structure
jsonld:
- class_count: 0
  name: Segment Context
  property_count: 9
  slug: segment-context
layout: provider
modified: '2026-05-19'
name: segment
nav: Providers
network: true
overview: 'segment publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Pixel Tracking API, Alias API, Batch API, and 20 more.


  The segment catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  segment''s developer surface includes authentication and 8 more developer resources.'
plans:
- name: Segment Plans Pricing
  plan_count: 3
  slug: segment-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 4
  name: Segment Rate Limits
  slug: segment-rate-limits
rules:
- name: segment API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: segment-asyncapi-spectral-rules
- name: segment API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: segment-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.6
  delta: -2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 76.0
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 47.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/segment/refs/heads/main/screenshots/segment-2026-06-20T193639.png
security:
- kind: authentication
  name: Segment Authentication
  slug: segment-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Segment Domain Security
  slug: segment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: segment
---
