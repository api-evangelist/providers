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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 34
  human_in_the_loop: 0
  name: Segment Agentic Access
  operation_count: 72
  slug: segment-agentic-access
  summary_line: 72 operations · 34 acting
api_count: 4
apis:
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
artifact_total: 108
asyncapis:
- description: 'Segment Webhooks submit real-time user data to HTTP endpoints as POST requests. When configured as a destination, Segment forwards identify, track, page, screen, group, and alias events to up to five '
  name: Segment Webhook Events
  slug: segment-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Segment Config Alias API
  slug: open-segment-alias-api
- collection_type: open
  name: Segment Config Alias Batch API
  slug: open-segment-batch-api
- collection_type: open
  name: Segment Config Alias Catalog API
  slug: open-segment-catalog-api
- collection_type: open
  name: Segment Config API
  slug: open-segment-config-api
- collection_type: open
  name: Segment Config Alias Destinations API
  slug: open-segment-destinations-api
- collection_type: open
  name: Segment Config Alias Events API
  slug: open-segment-events-api
- collection_type: open
  name: Segment Config Alias External IDs API
  slug: open-segment-external-ids-api
- collection_type: open
  name: Segment Config Alias Functions API
  slug: open-segment-functions-api
- collection_type: open
  name: Segment Config Alias Group API
  slug: open-segment-group-api
- collection_type: open
  name: Segment HTTP Tracking API
  slug: open-segment-http-tracking-api
- collection_type: open
  name: Segment Config Alias Identify API
  slug: open-segment-identify-api
- collection_type: open
  name: Segment Config Alias Labels API
  slug: open-segment-labels-api
- collection_type: open
  name: Segment Config Alias Links API
  slug: open-segment-links-api
- collection_type: open
  name: Segment Config Alias Page API
  slug: open-segment-page-api
- collection_type: open
  name: Segment Config Alias Pixel Tracking API
  slug: open-segment-pixel-tracking-api
- collection_type: open
  name: Segment Profile API
  slug: open-segment-profile-api
- collection_type: open
  name: Segment Config Alias Profiles API
  slug: open-segment-profiles-api
- collection_type: open
  name: Segment Public API
  slug: open-segment-public-api
- collection_type: open
  name: Segment Config Alias Regulations API
  slug: open-segment-regulations-api
- collection_type: open
  name: Segment Config Alias Screen API
  slug: open-segment-screen-api
- collection_type: open
  name: Segment Config Alias Sources API
  slug: open-segment-sources-api
- collection_type: open
  name: Segment Config Alias Track API
  slug: open-segment-track-api
- collection_type: open
  name: Segment Config Alias Tracking Plans API
  slug: open-segment-tracking-plans-api
- collection_type: open
  name: Segment Config Alias Traits API
  slug: open-segment-traits-api
- collection_type: open
  name: Segment Config Alias Transformations API
  slug: open-segment-transformations-api
- collection_type: open
  name: Segment Config Alias Warehouses API
  slug: open-segment-warehouses-api
- collection_type: open
  name: Segment Config Alias Workspaces API
  slug: open-segment-workspaces-api
common:
- group: company
  title: ''
  type: Website
  url: https://segment.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.twilio.com/docs/segment
- group: docs
  title: ''
  type: Documentation
  url: https://www.twilio.com/docs/segment
- group: docs
  title: ''
  type: APIReference
  url: https://docs.segmentapis.com
- group: start
  title: ''
  type: GettingStarted
  url: https://www.twilio.com/docs/segment/api
- group: commercial
  title: ''
  type: Pricing
  url: https://segment.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.segment.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://segment.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://segment.com/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://segment.com/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.segment.com
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
created: '2026-05-19'
description: 'Twilio Segment is a customer data platform that collects, cleans, and routes customer data to hundreds of downstream tools for analytics, marketing, and data warehousing. Its surface spans event collection (the HTTP Tracking API with identify, track, page, screen, group and alias calls, plus a pixel endpoint for environments where JavaScript cannot run), a Public API for programmatic management of workspaces, sources, destinations, warehouses, tracking plans, functions and transformations, Unify for identity resolution, Engage for audiences, Protocols for tracking-plan governance, Reverse ETL for warehouse-to-tool syncs, and connections to 90+ warehouses including BigQuery, Snowflake and Databricks. Segment was acquired by Twilio in a $3.2B all-stock deal completed in 2020 and now sits inside Twilio''s platform; Twilio completed an operational review in March 2024 and retained the business despite activist-investor pressure to divest. The docs, pricing and legal pages have
  moved onto twilio.com, and the legacy Segment Analytics libraries for iOS and Android reached full sunset on 2026-03-31. The older Config API is deprecated — no new tokens have been issued since early 2024 — with the Public API as the recommended replacement. The Public API host is authenticated: api.segmentapis.com returns 401 anonymously, and no OpenAPI is publicly fetchable (see x-evidence).'
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
name: Twilio Segment
nav: Providers
network: true
overview: 'Twilio Segment publishes 22 APIs on the [APIs.io](https://apis.io/) network, including segment Alias API, segment Batch API, segment Catalog API, and 19 more. Tagged areas include Company, Customer Data Platform, CDP, Identity Resolution, and Event Streaming.


  The Twilio Segment catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Twilio Segment''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, authentication, and 14 more developer resources.'
plans:
- name: Segment Plans Pricing
  plan_count: 3
  slug: segment-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Segment Rate Limits
  slug: segment-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Twilio Segment API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: segment-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Twilio Segment API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: segment-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 13.6
    contract_quality: 73.3
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 45.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
tags:
- Company
- Customer Data Platform
- CDP
- Identity Resolution
- Event Streaming
- Reverse ETL
- Data Pipeline
- Customer Data
- Analytics
- Acquired
website: https://segment.com
---
