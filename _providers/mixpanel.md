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
    agent_skills: true
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Mixpanel Agentic Access
  operation_count: 54
  slug: mixpanel-agentic-access
  summary_line: 54 operations · 30 acting
api_count: 22
apis:
- description: Outbound webhook surfaces delivered by Mixpanel to customer-hosted HTTPS endpoints, covering Custom Alert notifications (fired from reports configured in Project Settings) and Cohort Sync Custom Webho
  name: Mixpanel Webhooks
  slug: mixpanel-webhooks
- description: Manage chart annotations for time-based markers
  name: Mixpanel Annotations API
  slug: mixpanel-annotations-api
- description: Manage and query user cohorts
  name: Mixpanel Cohorts API
  slug: mixpanel-cohorts-api
- description: Manage warehouse data connections
  name: Mixpanel Connectors API
  slug: mixpanel-connectors-api
- description: Submit and check data deletion requests
  name: Mixpanel Deletion API
  slug: mixpanel-deletion-api
- description: Track and import event data
  name: Mixpanel Events API
  slug: mixpanel-events-api
- description: Export raw event data
  name: Mixpanel Export API
  slug: mixpanel-export-api
- description: Analyze conversion funnels
  name: Mixpanel Funnels API
  slug: mixpanel-funnels-api
- description: Manage group analytics profiles
  name: Mixpanel Group Profiles API
  slug: mixpanel-group-profiles-api
- description: Manage user identity resolution and merging
  name: Mixpanel Identity API
  slug: mixpanel-identity-api
- description: Manage and trigger warehouse import runs
  name: Mixpanel Imports API
  slug: mixpanel-imports-api
- description: Query event data with aggregation and breakdowns
  name: Mixpanel Insights API
  slug: mixpanel-insights-api
- description: Manage lookup tables for data enrichment
  name: Mixpanel Lookup Tables API
  slug: mixpanel-lookup-tables-api
- description: Monitor and manage pipeline execution runs
  name: Mixpanel Pipeline Runs API
  slug: mixpanel-pipeline-runs-api
- description: Create and manage data export pipelines
  name: Mixpanel Pipelines API
  slug: mixpanel-pipelines-api
- description: Manage service account project access
  name: Mixpanel Project Memberships API
  slug: mixpanel-project-memberships-api
- description: Query retention analysis data
  name: Mixpanel Retention API
  slug: mixpanel-retention-api
- description: Submit and check data retrieval requests
  name: Mixpanel Retrieval API
  slug: mixpanel-retrieval-api
- description: Manage Lexicon schema definitions
  name: Mixpanel Schemas API
  slug: mixpanel-schemas-api
- description: Query event segmentation data over time
  name: Mixpanel Segmentation API
  slug: mixpanel-segmentation-api
- description: Manage service accounts for API access
  name: Mixpanel Service Accounts API
  slug: mixpanel-service-accounts-api
- description: Manage user profile properties
  name: Mixpanel User Profiles API
  slug: mixpanel-user-profiles-api
arazzos:
- description: List project cohorts then segment an event filtered to a chosen cohort.
  name: Mixpanel Cohort-Driven Segmentation
  slug: mixpanel-cohort-driven-segmentation-workflow
- description: Find a saved funnel, query its conversion data, and annotate the chart.
  name: Mixpanel Funnel Analysis and Annotate
  slug: mixpanel-funnel-analysis-workflow
- description: Submit a GDPR/CCPA deletion request and poll its task status, branching on completion.
  name: Mixpanel GDPR Data Deletion Flow
  slug: mixpanel-gdpr-deletion-flow-workflow
- description: Submit a GDPR/CCPA retrieval request and poll for the download URL, branching on completion.
  name: Mixpanel GDPR Data Retrieval Flow
  slug: mixpanel-gdpr-retrieval-flow-workflow
- description: Set properties on a group profile and then read insights for the project.
  name: Mixpanel Update Group Profile and Query Insights
  slug: mixpanel-group-profile-and-insights-workflow
- description: Link an anonymous ID to a known user, track an event, then segment that event.
  name: Mixpanel Resolve Identity and Track
  slug: mixpanel-identity-resolve-and-track-workflow
- description: Bulk-import historical events into Mixpanel and then export the raw events back out.
  name: Mixpanel Import Events and Export Raw
  slug: mixpanel-import-and-export-workflow
- description: Refresh a lookup table's CSV contents then track an event that references the join key.
  name: Mixpanel Refresh Lookup Table and Track Enriched Event
  slug: mixpanel-lookup-table-enrichment-workflow
- description: Compute the sum and average of a numeric event property, then annotate the period.
  name: Mixpanel Numeric Metric Monitor and Annotate
  slug: mixpanel-numeric-metric-monitor-workflow
- description: Set a user's People profile and then query an engagement event for that activity.
  name: Mixpanel Update Profile and Query Engagement
  slug: mixpanel-profile-and-engage-query-workflow
- description: Mark a release on the timeline and then measure retention from that born event.
  name: Mixpanel Annotate Release and Measure Retention
  slug: mixpanel-retention-with-annotation-workflow
- description: List event schemas, create or update a schema entry, then segment the governed event.
  name: Mixpanel Schema Governance and Verify
  slug: mixpanel-schema-governance-workflow
- description: Send a live event to Mixpanel and then segment that event over a date range.
  name: Mixpanel Track Event and Segment
  slug: mixpanel-track-and-segment-workflow
- description: Create a warehouse source connection, trigger an import run, and read the run history.
  name: Mixpanel Provision Warehouse Source and Trigger Import
  slug: mixpanel-warehouse-import-run-workflow
artifact_total: 138
asyncapis:
- description: 'AsyncAPI 2.6 description of Mixpanel''s outbound webhook surfaces. Mixpanel delivers two distinct, documented webhook event streams to customer-hosted HTTPS endpoints: 1. Alert Webhooks (Custom Alerts)'
  name: Mixpanel Webhooks
  slug: mixpanel-webhooks-asyncapi
collections:
- collection_type: postman
  name: Mixpanel Annotations API
  slug: postman-mixpanel-annotations
- collection_type: postman
  name: Mixpanel Data Pipelines API
  slug: postman-mixpanel-data-pipelines
- collection_type: postman
  name: Mixpanel Event Export API
  slug: postman-mixpanel-event-export
- collection_type: postman
  name: Mixpanel GDPR and CCPA API
  slug: postman-mixpanel-gdpr-ccpa
- collection_type: postman
  name: Mixpanel Identity API
  slug: postman-mixpanel-identity
- collection_type: postman
  name: Mixpanel Ingestion API
  slug: postman-mixpanel-ingestion
- collection_type: postman
  name: Mixpanel Lexicon Schemas API
  slug: postman-mixpanel-lexicon-schemas
- collection_type: postman
  name: Mixpanel Query API
  slug: postman-mixpanel-query
- collection_type: postman
  name: Mixpanel Service Accounts API
  slug: postman-mixpanel-service-accounts
- collection_type: postman
  name: Mixpanel Warehouse Connectors API
  slug: postman-mixpanel-warehouse-connectors
- collection_type: open
  name: Mixpanel Annotations API
  slug: open-mixpanel-annotations
- collection_type: open
  name: Mixpanel Data Pipelines API
  slug: open-mixpanel-data-pipelines
- collection_type: open
  name: Mixpanel Event Export API
  slug: open-mixpanel-event-export
- collection_type: open
  name: Mixpanel GDPR and CCPA API
  slug: open-mixpanel-gdpr-ccpa
- collection_type: open
  name: Mixpanel Identity API
  slug: open-mixpanel-identity
- collection_type: open
  name: Mixpanel Ingestion API
  slug: open-mixpanel-ingestion
- collection_type: open
  name: Mixpanel Lexicon Schemas API
  slug: open-mixpanel-lexicon-schemas
- collection_type: open
  name: Mixpanel Query API
  slug: open-mixpanel-query
- collection_type: open
  name: Mixpanel Service Accounts API
  slug: open-mixpanel-service-accounts
- collection_type: open
  name: Mixpanel Warehouse Connectors API
  slug: open-mixpanel-warehouse-connectors
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mixpanel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mixpanel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mixpanel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mixpanel-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mixpanel/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-cohort-driven-segmentation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-funnel-analysis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-gdpr-deletion-flow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-gdpr-retrieval-flow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-group-profile-and-insights-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-identity-resolve-and-track-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-import-and-export-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-lookup-table-enrichment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-numeric-metric-monitor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-profile-and-engage-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-retention-with-annotation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-schema-governance-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-track-and-segment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mixpanel-warehouse-import-run-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mixpanel-inc-
- group: start
  title: ''
  type: Portal
  url: https://developer.mixpanel.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.mixpanel.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developer.mixpanel.com/reference/authentication
- group: build
  title: ''
  type: SDKs
  url: https://developer.mixpanel.com/docs/sdks
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.mixpanel.com/reference/rate-limits
- group: operate
  title: ''
  type: API Status
  url: https://www.mixpanelstatus.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mixpanel.com/changelogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mixpanel
- group: auth
  title: ''
  type: Security
  url: https://mixpanel.com/legal/security-overview/
- group: start
  title: ''
  type: Login
  url: https://mixpanel.com/login/
- group: start
  title: ''
  type: Signup
  url: https://mixpanel.com/register/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mixpanel.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mixpanel.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://mixpanel.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://mixpanel.com/blog
- group: operate
  title: ''
  type: Support
  url: https://mixpanel.com/get-support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/mixpanel-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mixpanel-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mixpanel-user-profile-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/mixpanel-funnel-schema.json
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/mixpanel/mcp-go
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/mixpanel/ai-plugins
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.mixpanel.com/llms.txt
created: '2024'
description: Mixpanel is a business analytics service company that tracks user interactions with web and mobile applications and provides tools for targeted communication with them.
features:
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
finops:
- name: Mixpanel Finops
  service_category: Product Analytics
  slug: mixpanel-finops
graphqls:
- description: Conceptual GraphQL schema for the [Mixpanel](https://mixpanel.com) product analytics platform. Mixpanel provides a suite of REST APIs — Ingestion, Query, Engage, Export, Identity, Lexicon/Schemas, Ser
  name: Mixpanel GraphQL Schema
  slug: mixpanel-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mixpanel.png
json_schemas:
- name: Annotation
  property_count: 5
  slug: mixpanel-annotation
- name: BigQueryConfig
  property_count: 3
  slug: mixpanel-bigqueryconfig
- name: Cohort
  property_count: 5
  slug: mixpanel-cohort
- name: CreateAnnotationRequest
  property_count: 2
  slug: mixpanel-createannotationrequest
- name: CreatePipelineRequest
  property_count: 10
  slug: mixpanel-createpipelinerequest
- name: CreateServiceAccountRequest
  property_count: 1
  slug: mixpanel-createserviceaccountrequest
- name: CreateWarehouseSourceRequest
  property_count: 5
  slug: mixpanel-createwarehousesourcerequest
- name: ErrorResponse
  property_count: 5
  slug: mixpanel-errorresponse
- name: Mixpanel Event
  property_count: 2
  slug: mixpanel-event
- name: Mixpanel Funnel
  property_count: 4
  slug: mixpanel-funnel
- name: FunnelResponse
  property_count: 1
  slug: mixpanel-funnelresponse
- name: FunnelStep
  property_count: 5
  slug: mixpanel-funnelstep
- name: FunnelSummary
  property_count: 2
  slug: mixpanel-funnelsummary
- name: GCSConfig
  property_count: 3
  slug: mixpanel-gcsconfig
- name: GroupUpdate
  property_count: 7
  slug: mixpanel-groupupdate
- name: IdentityResponse
  property_count: 2
  slug: mixpanel-identityresponse
- name: ImportResponse
  property_count: 3
  slug: mixpanel-importresponse
- name: InsightsResponse
  property_count: 2
  slug: mixpanel-insightsresponse
- name: LookupTable
  property_count: 6
  slug: mixpanel-lookuptable
- name: Pipeline
  property_count: 10
  slug: mixpanel-pipeline
- name: PipelineRun
  property_count: 7
  slug: mixpanel-pipelinerun
- name: PrivacyRequest
  property_count: 2
  slug: mixpanel-privacyrequest
- name: ProfileUpdate
  property_count: 11
  slug: mixpanel-profileupdate
- name: ProjectMembership
  property_count: 3
  slug: mixpanel-projectmembership
- name: PropertySchema
  property_count: 4
  slug: mixpanel-propertyschema
- name: RetentionResponse
  property_count: 0
  slug: mixpanel-retentionresponse
- name: S3Config
  property_count: 4
  slug: mixpanel-s3config
- name: SchemaDefinition
  property_count: 6
  slug: mixpanel-schemadefinition
- name: SchemaEntry
  property_count: 6
  slug: mixpanel-schemaentry
- name: SegmentationResponse
  property_count: 1
  slug: mixpanel-segmentationresponse
- name: ServiceAccount
  property_count: 5
  slug: mixpanel-serviceaccount
- name: ServiceAccountWithSecret
  property_count: 0
  slug: mixpanel-serviceaccountwithsecret
- name: SnowflakeConfig
  property_count: 6
  slug: mixpanel-snowflakeconfig
- name: TableConfig
  property_count: 5
  slug: mixpanel-tableconfig
- name: TaskResponse
  property_count: 3
  slug: mixpanel-taskresponse
- name: TaskStatus
  property_count: 2
  slug: mixpanel-taskstatus
- name: TrackResponse
  property_count: 2
  slug: mixpanel-trackresponse
- name: UpdatePipelineRequest
  property_count: 4
  slug: mixpanel-updatepipelinerequest
- name: UpdateWarehouseSourceRequest
  property_count: 3
  slug: mixpanel-updatewarehousesourcerequest
- name: Mixpanel User Profile
  property_count: 2
  slug: mixpanel-user-profile
- name: WarehouseRun
  property_count: 6
  slug: mixpanel-warehouserun
- name: WarehouseSource
  property_count: 7
  slug: mixpanel-warehousesource
- name: WarehouseTable
  property_count: 4
  slug: mixpanel-warehousetable
json_structures:
- name: Mixpanel Structure
  property_count: 0
  slug: mixpanel-structure
jsonld:
- class_count: 0
  name: Mixpanel Context
  property_count: 10
  slug: mixpanel-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: Mixpanel
nav: Providers
network: true
overview: 'Mixpanel publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Annotations API, Cohorts API, and 19 more. Tagged areas include Analytics, Data Analysis, Event Tracking, Product Analytics, and User Behavior.


  The Mixpanel catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Mixpanel''s developer surface includes authentication, developer portal, getting-started guide, changelog, signup flow, pricing, engineering blog, and 36 more developer resources.'
plans:
- name: Mixpanel Plans Pricing
  plan_count: 3
  slug: mixpanel-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 4
  name: Mixpanel Rate Limits
  slug: mixpanel-rate-limits
rules:
- name: Mixpanel API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: mixpanel-asyncapi-spectral-rules
- name: Mixpanel API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: mixpanel-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 66.0
  delta: -1.1
  facets:
    commercial_clarity: 84.2
    contract_quality: 79.5
    developer_ergonomics: 56.5
    discoverability: 48.1
    governance: 41.7
    operational_transparency: 63.2
  previous_composite: 67.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mixpanel/refs/heads/main/screenshots/mixpanel-2026-06-20T185622.png
security:
- kind: authentication
  name: Mixpanel Authentication
  slug: mixpanel-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Mixpanel Domain Security
  slug: mixpanel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Mixpanel Vulnerability Disclosure
  slug: mixpanel-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 9
skills:
- name: create-dashboard
  slug: create-dashboard-2
- name: create-dashboard
  slug: create-dashboard-3
- name: create-dashboard
  slug: create-dashboard
- name: deep-research
  slug: deep-research-2
- name: deep-research
  slug: deep-research-3
- name: deep-research
  slug: deep-research
- name: tracking-implementation
  slug: tracking-implementation-2
- name: tracking-implementation
  slug: tracking-implementation-3
- name: tracking-implementation
  slug: tracking-implementation
slug: mixpanel
tags:
- Analytics
- Data Analysis
- Event Tracking
- Product Analytics
- User Behavior
website: https://developer.mixpanel.com/
---
