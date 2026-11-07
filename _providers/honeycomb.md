---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 79
  human_in_the_loop: 0
  name: Honeycomb Agentic Access
  operation_count: 133
  slug: honeycomb-agentic-access
  summary_line: 133 operations · 79 acting
api_count: 2
apis:
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: The Honeycomb Events API is the lowest-level interface for sending event data to Honeycomb. It supports both single event creation and batch event submission, allowing developers to send structured te
  name: Honeycomb Events API
  slug: events-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: The Honeycomb Queries API allows developers to programmatically create and manage query specifications within Honeycomb. Queries are used to identify and reference queries across other parts of the AP
  name: Honeycomb Queries API
  slug: queries-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: 'The Honeycomb Datasets API provides management capabilities for datasets, which represent collections of related events from the same source. It allows developers to list, create, and update datasets '
  name: Honeycomb Datasets API
  slug: datasets-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: 'The Honeycomb Boards API allows developers to programmatically create and manage boards, which are collections of queries displayed together as a dashboard-like view. Boards provide a way to organize '
  name: Honeycomb Boards API
  slug: boards-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: The Honeycomb Markers API enables developers to create and manage markers that indicate points in time on graphs where notable events occurred, such as deploys, configuration changes, or outages. Mark
  name: Honeycomb Markers API
  slug: markers-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: 'The Honeycomb Triggers API allows developers to programmatically configure alerting rules that fire when query results meet specified conditions. Triggers work in conjunction with the Recipients API, '
  name: Honeycomb Triggers API
  slug: triggers-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: The Honeycomb Environments API provides administrative capabilities for managing environments within a Honeycomb team. Environments allow organizations to separate telemetry data across different stag
  name: Honeycomb Environments API
  slug: environments-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Validate authentication for a key, determine what authorizations have been granted to a key, and determine the Team and Environment it belongs to.
  name: honeycomb Auth API
  slug: honeycomb-auth-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Manage burn alerts that notify you when issues impact your SLO budget.
  name: honeycomb Burn Alerts API
  slug: honeycomb-burn-alerts-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Manage calculated fields (derived columns) that compute values from expressions applied to event fields.
  name: honeycomb Calculated Fields API
  slug: honeycomb-calculated-fields-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Manage columns (fields) in the events you send to Honeycomb datasets.
  name: honeycomb Columns API
  slug: honeycomb-columns-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Manage dataset definitions that configure how columns are interpreted and displayed.
  name: honeycomb Dataset Definitions API
  slug: honeycomb-dataset-definitions-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Manage API keys for a team, including listing, creating, updating, and deleting keys.
  name: honeycomb Key Management API
  slug: honeycomb-key-management-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Process streaming events from Amazon Kinesis into Honeycomb.
  name: honeycomb Kinesis Events API
  slug: honeycomb-kinesis-events-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Manage marker settings that group similar markers together with consistent visual styling.
  name: honeycomb Marker Settings API
  slug: honeycomb-marker-settings-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Associate names and descriptions to queries for collaboration features.
  name: honeycomb Query Annotations API
  slug: honeycomb-query-annotations-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Access completed query result data.
  name: honeycomb Query Data API
  slug: honeycomb-query-data-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Manage notification destinations for triggers and burn alerts including PagerDuty, Email, Webhook, Microsoft Teams, and Slack.
  name: honeycomb Recipients API
  slug: honeycomb-recipients-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Access historical SLO performance reporting data.
  name: honeycomb Reporting API
  slug: honeycomb-reporting-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Visualize relationships between services using dependency requests.
  name: honeycomb Service Maps API
  slug: honeycomb-service-maps-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Define and monitor Service Level Objectives for your organization.
  name: Honeycomb SL Os API
  slug: honeycomb-slos-api
- baseURL: https://api.honeycomb.io
  baseurl_source: declared
  description: Anomaly Detection identifies Signals - patterns in your services that deviate from their historical baseline - and can notify Recipients when a Signal turns anomalous. Each Signal is scoped to a servi
  name: Honeycomb Anomaly Detection API
  slug: honeycomb-anomaly-detection-api
artifact_total: 176
asyncapis:
- description: 'AsyncAPI description of Honeycomb''s event-driven and streaming-style surfaces. Honeycomb does not publish a long-lived bidirectional streaming API (no public Kafka topic, no WebSocket, no Server-Sent '
  name: Honeycomb Streaming, OTLP Ingest & Trigger Webhooks
  slug: honeycomb-streaming-asyncapi
collections:
- collection_type: open
  name: Honeycomb API
  slug: open-honeycomb-api
- collection_type: open
  name: Honeycomb Auth API
  slug: open-honeycomb-auth-api
- collection_type: open
  name: Honeycomb Auth Boards API
  slug: open-honeycomb-boards-api
- collection_type: open
  name: Honeycomb Auth Burn Alerts API
  slug: open-honeycomb-burn-alerts-api
- collection_type: open
  name: Honeycomb Auth Calculated Fields API
  slug: open-honeycomb-calculated-fields-api
- collection_type: open
  name: Honeycomb Auth Columns API
  slug: open-honeycomb-columns-api
- collection_type: open
  name: Honeycomb Auth Dataset Definitions API
  slug: open-honeycomb-dataset-definitions-api
- collection_type: open
  name: Honeycomb Auth Datasets API
  slug: open-honeycomb-datasets-api
- collection_type: open
  name: Honeycomb Auth Environments API
  slug: open-honeycomb-environments-api
- collection_type: open
  name: Honeycomb Auth Events API
  slug: open-honeycomb-events-api
- collection_type: open
  name: Honeycomb Auth Key Management API
  slug: open-honeycomb-key-management-api
- collection_type: open
  name: Honeycomb Auth Kinesis Events API
  slug: open-honeycomb-kinesis-events-api
- collection_type: open
  name: Honeycomb Auth Marker Settings API
  slug: open-honeycomb-marker-settings-api
- collection_type: open
  name: Honeycomb Auth Markers API
  slug: open-honeycomb-markers-api
- collection_type: open
  name: Honeycomb Auth Queries API
  slug: open-honeycomb-queries-api
- collection_type: open
  name: Honeycomb Auth Query Annotations API
  slug: open-honeycomb-query-annotations-api
- collection_type: open
  name: Honeycomb Auth Query Data API
  slug: open-honeycomb-query-data-api
- collection_type: open
  name: Honeycomb Auth Query Results API
  slug: open-honeycomb-query-results-api
- collection_type: open
  name: Honeycomb Auth Recipients API
  slug: open-honeycomb-recipients-api
- collection_type: open
  name: Honeycomb Auth Reporting API
  slug: open-honeycomb-reporting-api
- collection_type: open
  name: Honeycomb Auth Service Maps API
  slug: open-honeycomb-service-maps-api
- collection_type: open
  name: Honeycomb Auth SLOs API
  slug: open-honeycomb-slos-api
- collection_type: open
  name: Honeycomb Auth Triggers API
  slug: open-honeycomb-triggers-api
common:
- group: commercial
  href: https://artifacts.apis.io/honeycomb/finops/honeycomb-finops.yml
  title: ''
  type: FinOps
  url: finops/honeycomb-finops.yml
- group: operate
  href: https://artifacts.apis.io/honeycomb/rate-limits/honeycomb-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/honeycomb-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/honeycomb/plans/honeycomb-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/honeycomb-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/honeycomb/rules/honeycomb-rules.yml
  title: ''
  type: Spectral
  url: rules/honeycomb-rules.yml
- group: design
  href: https://artifacts.apis.io/honeycomb/rules/honeycomb-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/honeycomb-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/honeycomb/rules/honeycomb-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/honeycomb-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/honeycomb/vocabulary/honeycomb-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/honeycomb-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/honeycomb/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/honeycomb/data-model/honeycomb-data-model.yml
  title: ''
  type: DataModel
  url: data-model/honeycomb-data-model.yml
- group: operate
  href: https://artifacts.apis.io/honeycomb/changelog/honeycomb-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/honeycomb-changelog.yml
- group: design
  href: https://artifacts.apis.io/honeycomb/conventions/honeycomb-conventions.yml
  title: ''
  type: Conventions
  url: conventions/honeycomb-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.honeycomb.io/
- group: design
  href: https://artifacts.apis.io/honeycomb/errors/honeycomb-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/honeycomb-problem-types.yml
- group: design
  href: https://artifacts.apis.io/honeycomb/conformance/honeycomb-conformance.yml
  title: ''
  type: Conformance
  url: conformance/honeycomb-conformance.yml
- group: other
  href: https://artifacts.apis.io/honeycomb/overlays/honeycomb-events-api-overlay.yml
  title: ''
  type: Overlay
  url: overlays/honeycomb-events-api-overlay.yml
- group: agent
  href: https://artifacts.apis.io/honeycomb/llms/honeycomb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/honeycomb-llms.txt
- group: agent
  href: https://artifacts.apis.io/honeycomb/mcp/honeycomb-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/honeycomb-mcp.yml
- group: agent
  href: https://artifacts.apis.io/honeycomb/well-known/honeycomb-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/honeycomb-well-known.yml
- group: other
  href: https://artifacts.apis.io/honeycomb/hosts/honeycomb-hosts.yml
  title: ''
  type: Hosts
  url: hosts/honeycomb-hosts.yml
- group: other
  href: https://artifacts.apis.io/honeycomb/vendors/honeycomb-vendors.yml
  title: ''
  type: Vendors
  url: vendors/honeycomb-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.honeycomb.io/terms
- group: operate
  title: ''
  type: Support
  url: https://support.honeycomb.io/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.honeycomb.io/
- group: start
  title: ''
  type: SignUp
  url: https://ui.honeycomb.io/signup
- group: start
  title: ''
  type: Sandbox
  url: https://play.honeycomb.io/sandbox/tours
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.honeycomb.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.honeycomb.io/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.honeycomb.io/news
- group: other
  title: ''
  type: Leadership
  url: https://www.honeycomb.io/about/team
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.honeycomb.io/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.honeycomb.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.honeycomb.io\
- group: docs
  title: ''
  type: APIReference
  url: https://docs.honeycomb.io/api/introduction
- group: other
  href: https://artifacts.apis.io/honeycomb/a2a/honeycomb-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/honeycomb-a2a.yml
- group: company
  title: ''
  type: Website
  url: https://www.honeycomb.io/
- group: agent
  href: https://artifacts.apis.io/honeycomb/agentic-access/honeycomb-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/honeycomb-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/honeycomb/security/honeycomb-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/honeycomb-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/honeycomb/security/honeycomb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/honeycomb-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/honeycomb/authentication/honeycomb-authentication.yml
  title: ''
  type: Authentication
  url: authentication/honeycomb-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/honeycombio
- group: design
  href: https://artifacts.apis.io/honeycomb/json-ld/honeycomb-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/honeycomb-context.jsonld
- group: docs
  href: https://artifacts.apis.io/honeycomb/json-schema/honeycomb-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/honeycomb-event-schema.json
- group: docs
  href: https://artifacts.apis.io/honeycomb/json-schema/honeycomb-query-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/honeycomb-query-schema.json
- group: docs
  href: https://artifacts.apis.io/honeycomb/json-schema/honeycomb-slo-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/honeycomb-slo-schema.json
- group: docs
  href: https://artifacts.apis.io/honeycomb/json-schema/honeycomb-trigger-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/honeycomb-trigger-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.honeycomb.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.honeycomb.io/feed/
- group: other
  href: https://artifacts.apis.io/honeycomb/capabilities/honeycomb-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/honeycomb-capability-edges.yml
description: Honeycomb provides an observability platform that gives engineering teams real‑time visibility into distributed tracing, log analytics, metrics, and AI agent workflows. The platform supports OpenTelemetry, private‑cloud deployments, and telemetry pipelines for enterprises, AI startups, financial services, retail and other software‑focused organizations.
features:
- 'Free: 20M events/mo + 100M metrics/mo'
- 'Pro from $130/mo: 1.5B events, 100 triggers, 2 SLOs, SSO'
- 'Enterprise: 300+ triggers, 100+ SLOs, Service Map, PrivateLink'
- Query Data API at api.honeycomb.io (Enterprise)
- OpenTelemetry-native ingest
- BubbleUp for high-cardinality outlier analysis
- Distributed tracing with span search
- Refinery for tail-based sampling
- SLOs with burn rates
- Triggers (alerts on query results)
- Service Map (Enterprise)
- Honeycomb Private Cloud (Enterprise)
- Events ingest scales with plan; batch up to 1,000 events
- 'Query Data API: 5 req/sec/team'
- API keys per environment
- Heatmaps, scatter plots, trace waterfall views
finops:
- has_sources: true
  method: derived
  name: Honeycomb Finops
  primary_unit: events
  service_category: ''
  slug: honeycomb-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/honeycomb.png
json_schemas:
- name: ApiKeyCreateRequest
  property_count: 4
  slug: honeycomb-api-key-create-request
- name: ApiKey
  property_count: 8
  slug: honeycomb-api-key
- name: ApiKeyUpdateRequest
  property_count: 3
  slug: honeycomb-api-key-update-request
- name: ApiKey
  property_count: 8
  slug: honeycomb-apikey
- name: ApiKeyCreateRequest
  property_count: 4
  slug: honeycomb-apikeycreaterequest
- name: ApiKeyUpdateRequest
  property_count: 3
  slug: honeycomb-apikeyupdaterequest
- name: AuthInfo
  property_count: 2
  slug: honeycomb-auth-info
- name: AuthPermissions
  property_count: 1
  slug: honeycomb-auth-permissions
- name: AuthInfo
  property_count: 2
  slug: honeycomb-authinfo
- name: AuthPermissions
  property_count: 1
  slug: honeycomb-authpermissions
- name: BatchEventResponse
  property_count: 2
  slug: honeycomb-batch-event-response
- name: BatchEvent
  property_count: 3
  slug: honeycomb-batch-event
- name: BatchEvent
  property_count: 3
  slug: honeycomb-batchevent
- name: BatchEventResponse
  property_count: 2
  slug: honeycomb-batcheventresponse
- name: BoardCreateRequest
  property_count: 5
  slug: honeycomb-board-create-request
- name: Board
  property_count: 9
  slug: honeycomb-board
- name: BoardUpdateRequest
  property_count: 5
  slug: honeycomb-board-update-request
- name: BoardCreateRequest
  property_count: 5
  slug: honeycomb-boardcreaterequest
- name: BoardQuery
  property_count: 6
  slug: honeycomb-boardquery
- name: BoardUpdateRequest
  property_count: 5
  slug: honeycomb-boardupdaterequest
- name: BurnAlertCreateRequest
  property_count: 6
  slug: honeycomb-burn-alert-create-request
- name: BurnAlert
  property_count: 9
  slug: honeycomb-burn-alert
- name: BurnAlertUpdateRequest
  property_count: 4
  slug: honeycomb-burn-alert-update-request
- name: BurnAlert
  property_count: 9
  slug: honeycomb-burnalert
- name: BurnAlertCreateRequest
  property_count: 6
  slug: honeycomb-burnalertcreaterequest
- name: BurnAlertUpdateRequest
  property_count: 4
  slug: honeycomb-burnalertupdaterequest
- name: CalculatedFieldCreateRequest
  property_count: 3
  slug: honeycomb-calculated-field-create-request
- name: CalculatedField
  property_count: 6
  slug: honeycomb-calculated-field
- name: CalculatedFieldUpdateRequest
  property_count: 2
  slug: honeycomb-calculated-field-update-request
- name: CalculatedField
  property_count: 6
  slug: honeycomb-calculatedfield
- name: CalculatedFieldCreateRequest
  property_count: 3
  slug: honeycomb-calculatedfieldcreaterequest
- name: CalculatedFieldUpdateRequest
  property_count: 2
  slug: honeycomb-calculatedfieldupdaterequest
- name: ColumnCreateRequest
  property_count: 4
  slug: honeycomb-column-create-request
- name: Column
  property_count: 8
  slug: honeycomb-column
- name: ColumnUpdateRequest
  property_count: 3
  slug: honeycomb-column-update-request
- name: ColumnCreateRequest
  property_count: 4
  slug: honeycomb-columncreaterequest
- name: ColumnUpdateRequest
  property_count: 3
  slug: honeycomb-columnupdaterequest
- name: DatasetCreateRequest
  property_count: 2
  slug: honeycomb-dataset-create-request
- name: DatasetDefinition
  property_count: 9
  slug: honeycomb-dataset-definition
- name: Dataset
  property_count: 6
  slug: honeycomb-dataset
- name: DatasetUpdateRequest
  property_count: 2
  slug: honeycomb-dataset-update-request
- name: DatasetCreateRequest
  property_count: 2
  slug: honeycomb-datasetcreaterequest
- name: DatasetDefinition
  property_count: 9
  slug: honeycomb-datasetdefinition
- name: DatasetUpdateRequest
  property_count: 2
  slug: honeycomb-datasetupdaterequest
- name: EnvironmentCreateRequest
  property_count: 3
  slug: honeycomb-environment-create-request
- name: Environment
  property_count: 7
  slug: honeycomb-environment
- name: EnvironmentUpdateRequest
  property_count: 3
  slug: honeycomb-environment-update-request
- name: EnvironmentCreateRequest
  property_count: 3
  slug: honeycomb-environmentcreaterequest
- name: EnvironmentUpdateRequest
  property_count: 3
  slug: honeycomb-environmentupdaterequest
- name: Honeycomb Event
  property_count: 3
  slug: honeycomb-event
- name: MarkerCreateRequest
  property_count: 5
  slug: honeycomb-marker-create-request
- name: Marker
  property_count: 8
  slug: honeycomb-marker
- name: MarkerSettingCreateRequest
  property_count: 2
  slug: honeycomb-marker-setting-create-request
- name: MarkerSetting
  property_count: 5
  slug: honeycomb-marker-setting
- name: MarkerSettingUpdateRequest
  property_count: 2
  slug: honeycomb-marker-setting-update-request
- name: MarkerUpdateRequest
  property_count: 5
  slug: honeycomb-marker-update-request
- name: MarkerCreateRequest
  property_count: 5
  slug: honeycomb-markercreaterequest
- name: MarkerSetting
  property_count: 5
  slug: honeycomb-markersetting
- name: MarkerSettingCreateRequest
  property_count: 2
  slug: honeycomb-markersettingcreaterequest
- name: MarkerSettingUpdateRequest
  property_count: 2
  slug: honeycomb-markersettingupdaterequest
- name: MarkerUpdateRequest
  property_count: 5
  slug: honeycomb-markerupdaterequest
- name: QueryAnnotationCreateRequest
  property_count: 3
  slug: honeycomb-query-annotation-create-request
- name: QueryAnnotation
  property_count: 6
  slug: honeycomb-query-annotation
- name: QueryAnnotationUpdateRequest
  property_count: 2
  slug: honeycomb-query-annotation-update-request
- name: QueryData
  property_count: 2
  slug: honeycomb-query-data
- name: QueryResult
  property_count: 5
  slug: honeycomb-query-result
- name: Honeycomb Query Specification
  property_count: 11
  slug: honeycomb-query
- name: QuerySpec
  property_count: 11
  slug: honeycomb-query-spec
- name: QueryAnnotation
  property_count: 6
  slug: honeycomb-queryannotation
- name: QueryAnnotationCreateRequest
  property_count: 3
  slug: honeycomb-queryannotationcreaterequest
- name: QueryAnnotationUpdateRequest
  property_count: 2
  slug: honeycomb-queryannotationupdaterequest
- name: QueryData
  property_count: 2
  slug: honeycomb-querydata
- name: QueryResult
  property_count: 5
  slug: honeycomb-queryresult
- name: QuerySpec
  property_count: 9
  slug: honeycomb-queryspec
- name: RecipientCreateRequest
  property_count: 2
  slug: honeycomb-recipient-create-request
- name: Recipient
  property_count: 5
  slug: honeycomb-recipient
- name: RecipientUpdateRequest
  property_count: 1
  slug: honeycomb-recipient-update-request
- name: RecipientCreateRequest
  property_count: 2
  slug: honeycomb-recipientcreaterequest
- name: RecipientRef
  property_count: 1
  slug: honeycomb-recipientref
- name: RecipientUpdateRequest
  property_count: 1
  slug: honeycomb-recipientupdaterequest
- name: ServiceMapRequest
  property_count: 4
  slug: honeycomb-service-map-request
- name: ServiceMapResult
  property_count: 2
  slug: honeycomb-service-map-result
- name: ServiceMapRequest
  property_count: 4
  slug: honeycomb-servicemaprequest
- name: ServiceMapResult
  property_count: 2
  slug: honeycomb-servicemapresult
- name: Honeycomb SLO
  property_count: 8
  slug: honeycomb-slo
- name: SLOCreateRequest
  property_count: 5
  slug: honeycomb-slocreate-request
- name: SLOCreateRequest
  property_count: 5
  slug: honeycomb-slocreaterequest
- name: SLOReport
  property_count: 5
  slug: honeycomb-sloreport
- name: SLOUpdateRequest
  property_count: 5
  slug: honeycomb-sloupdate-request
- name: SLOUpdateRequest
  property_count: 5
  slug: honeycomb-sloupdaterequest
- name: TriggerCreateRequest
  property_count: 7
  slug: honeycomb-trigger-create-request
- name: Honeycomb Trigger
  property_count: 10
  slug: honeycomb-trigger
- name: TriggerUpdateRequest
  property_count: 7
  slug: honeycomb-trigger-update-request
- name: TriggerCreateRequest
  property_count: 7
  slug: honeycomb-triggercreaterequest
- name: TriggerUpdateRequest
  property_count: 7
  slug: honeycomb-triggerupdaterequest
json_structures:
- name: Honeycomb Structure
  property_count: 0
  slug: honeycomb-structure
jsonld:
- class_count: 0
  name: Honeycomb Context
  property_count: 11
  slug: honeycomb-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.honeycomb.io over HTTP.
  name: Honeycomb MCP Server
  slug: honeycomb
modified: '2026-09-16'
name: Honeycomb
nav: Providers
network: true
overview: 'Honeycomb publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Events API, Queries API, Datasets API, and 19 more. Tagged areas include Observability, Telemetry, Analytics, Data Management, and Monitoring.


  The Honeycomb catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Honeycomb''s developer surface includes changelog, support, signup flow, sandbox, pricing, getting-started guide, documentation, and 41 more developer resources.'
plans:
- name: Honeycomb Plans Pricing
  plan_count: 4
  slug: honeycomb-plans-pricing
- name: Honeycomb Price Estimates
  plan_count: 0
  slug: honeycomb-price-estimates
random_paper: 4
rate_limits:
- limit_count: 4
  name: Honeycomb Rate Limits
  slug: honeycomb-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Honeycomb — asyncapi rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: honeycomb-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Honeycomb — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: honeycomb-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Honeycomb API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: honeycomb-rules
score:
  band: strong
  composite: 59.9
  coverage:
    artifact_dirs: 37
    catalog_earned: 78.0
    catalog_earned_first_party: 12.0
    catalog_gap: 37.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 73.7
    contract_governance: 45.5
    contract_quality: 73.7
    developer_ergonomics: 45.8
    discoverability: 71.7
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 71.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/honeycomb/honeycomb-2026-06-20T182822.png
security:
- kind: authentication
  name: Honeycomb Authentication
  slug: honeycomb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Honeycomb Domain Security
  slug: honeycomb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Honeycomb Trust Center
  slug: honeycomb-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR, CSA STAR
skill_count: 5
skills:
- name: honeycomb-create-and-list-boards
  slug: honeycomb-create-and-list-boards
- name: honeycomb-create-and-retrieve-dataset
  slug: honeycomb-create-and-retrieve-dataset
- name: honeycomb-create-and-retrieve-query
  slug: honeycomb-create-and-retrieve-query
- name: honeycomb-create-trigger
  slug: honeycomb-create-trigger
- name: honeycomb-send-events
  slug: honeycomb-send-events
slug: honeycomb
tags:
- Observability
- Telemetry
- Analytics
- Data Management
- Monitoring
- A2A
website: https://www.honeycomb.io/
---
