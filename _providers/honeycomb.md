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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 79
  human_in_the_loop: 0
  name: Honeycomb Agentic Access
  operation_count: 133
  slug: honeycomb-agentic-access
  summary_line: 133 operations · 79 acting
api_count: 22
apis:
- description: The Honeycomb Events API is the lowest-level interface for sending event data to Honeycomb. It supports both single event creation and batch event submission, allowing developers to send structured te
  name: Honeycomb Events API
  slug: events-api
- description: The Honeycomb Queries API allows developers to programmatically create and manage query specifications within Honeycomb. Queries are used to identify and reference queries across other parts of the AP
  name: Honeycomb Queries API
  slug: queries-api
- description: The Honeycomb SLOs API enables developers to define and monitor Service Level Objectives programmatically. It supports creating, listing, updating, and deleting SLO objects for an organization. Combin
  name: Honeycomb SLOs API
  slug: slos-api
- description: 'The Honeycomb Datasets API provides management capabilities for datasets, which represent collections of related events from the same source. It allows developers to list, create, and update datasets '
  name: Honeycomb Datasets API
  slug: datasets-api
- description: 'The Honeycomb Boards API allows developers to programmatically create and manage boards, which are collections of queries displayed together as a dashboard-like view. Boards provide a way to organize '
  name: Honeycomb Boards API
  slug: boards-api
- description: The Honeycomb Markers API enables developers to create and manage markers that indicate points in time on graphs where notable events occurred, such as deploys, configuration changes, or outages. Mark
  name: Honeycomb Markers API
  slug: markers-api
- description: 'The Honeycomb Triggers API allows developers to programmatically configure alerting rules that fire when query results meet specified conditions. Triggers work in conjunction with the Recipients API, '
  name: Honeycomb Triggers API
  slug: triggers-api
- description: The Honeycomb Environments API provides administrative capabilities for managing environments within a Honeycomb team. Environments allow organizations to separate telemetry data across different stag
  name: Honeycomb Environments API
  slug: environments-api
- description: Validate authentication for a key, determine what authorizations have been granted to a key, and determine the Team and Environment it belongs to.
  name: honeycomb Auth API
  slug: honeycomb-auth-api
- description: Manage burn alerts that notify you when issues impact your SLO budget.
  name: honeycomb Burn Alerts API
  slug: honeycomb-burn-alerts-api
- description: Manage calculated fields (derived columns) that compute values from expressions applied to event fields.
  name: honeycomb Calculated Fields API
  slug: honeycomb-calculated-fields-api
- description: Manage columns (fields) in the events you send to Honeycomb datasets.
  name: honeycomb Columns API
  slug: honeycomb-columns-api
- description: Manage dataset definitions that configure how columns are interpreted and displayed.
  name: honeycomb Dataset Definitions API
  slug: honeycomb-dataset-definitions-api
- description: Manage API keys for a team, including listing, creating, updating, and deleting keys.
  name: honeycomb Key Management API
  slug: honeycomb-key-management-api
- description: Process streaming events from Amazon Kinesis into Honeycomb.
  name: honeycomb Kinesis Events API
  slug: honeycomb-kinesis-events-api
- description: Manage marker settings that group similar markers together with consistent visual styling.
  name: honeycomb Marker Settings API
  slug: honeycomb-marker-settings-api
- description: Associate names and descriptions to queries for collaboration features.
  name: honeycomb Query Annotations API
  slug: honeycomb-query-annotations-api
- description: Access completed query result data.
  name: honeycomb Query Data API
  slug: honeycomb-query-data-api
- description: Create and poll for asynchronous query results.
  name: honeycomb Query Results API
  slug: honeycomb-query-results-api
- description: Manage notification destinations for triggers and burn alerts including PagerDuty, Email, Webhook, Microsoft Teams, and Slack.
  name: honeycomb Recipients API
  slug: honeycomb-recipients-api
- description: Access historical SLO performance reporting data.
  name: honeycomb Reporting API
  slug: honeycomb-reporting-api
- description: Visualize relationships between services using dependency requests.
  name: honeycomb Service Maps API
  slug: honeycomb-service-maps-api
artifact_total: 112
asyncapis:
- description: 'AsyncAPI description of Honeycomb''s event-driven and streaming-style surfaces. Honeycomb does not publish a long-lived bidirectional streaming API (no public Kafka topic, no WebSocket, no Server-Sent '
  name: Honeycomb Streaming, OTLP Ingest & Trigger Webhooks
  slug: honeycomb-streaming-asyncapi
collections:
- collection_type: open
  name: Honeycomb API
  slug: open-honeycomb-api
- collection_type: open
  name: Honeycomb Boards API
  slug: open-honeycomb-boards-api
- collection_type: open
  name: Honeycomb Datasets API
  slug: open-honeycomb-datasets-api
- collection_type: open
  name: Honeycomb Environments API
  slug: open-honeycomb-environments-api
- collection_type: open
  name: Honeycomb Events API
  slug: open-honeycomb-events-api
- collection_type: open
  name: Honeycomb Markers API
  slug: open-honeycomb-markers-api
- collection_type: open
  name: Honeycomb Queries API
  slug: open-honeycomb-queries-api
- collection_type: open
  name: Honeycomb SLOs API
  slug: open-honeycomb-slos-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/honeycomb-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/honeycomb-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/honeycomb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/honeycomb-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/honeycombio
- group: design
  title: ''
  type: JSONLD
  url: json-ld/honeycomb-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/honeycomb-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/honeycomb-query-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/honeycomb-slo-schema.json
- group: docs
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
description: Build integrations and automate workflows with the Honeycomb API. Programmatically manage datasets, queries, triggers, SLOs, environments, API keys, and more.
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
- name: Honeycomb Finops
  service_category: Observability
  slug: honeycomb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/honeycomb.png
json_schemas:
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
  slug: honeycomb-authinfo
- name: AuthPermissions
  property_count: 1
  slug: honeycomb-authpermissions
- name: BatchEvent
  property_count: 3
  slug: honeycomb-batchevent
- name: BatchEventResponse
  property_count: 2
  slug: honeycomb-batcheventresponse
- name: Board
  property_count: 9
  slug: honeycomb-board
- name: BoardCreateRequest
  property_count: 5
  slug: honeycomb-boardcreaterequest
- name: BoardQuery
  property_count: 6
  slug: honeycomb-boardquery
- name: BoardUpdateRequest
  property_count: 5
  slug: honeycomb-boardupdaterequest
- name: BurnAlert
  property_count: 9
  slug: honeycomb-burnalert
- name: BurnAlertCreateRequest
  property_count: 6
  slug: honeycomb-burnalertcreaterequest
- name: BurnAlertUpdateRequest
  property_count: 4
  slug: honeycomb-burnalertupdaterequest
- name: CalculatedField
  property_count: 6
  slug: honeycomb-calculatedfield
- name: CalculatedFieldCreateRequest
  property_count: 3
  slug: honeycomb-calculatedfieldcreaterequest
- name: CalculatedFieldUpdateRequest
  property_count: 2
  slug: honeycomb-calculatedfieldupdaterequest
- name: Column
  property_count: 8
  slug: honeycomb-column
- name: ColumnCreateRequest
  property_count: 4
  slug: honeycomb-columncreaterequest
- name: ColumnUpdateRequest
  property_count: 3
  slug: honeycomb-columnupdaterequest
- name: Dataset
  property_count: 6
  slug: honeycomb-dataset
- name: DatasetCreateRequest
  property_count: 2
  slug: honeycomb-datasetcreaterequest
- name: DatasetDefinition
  property_count: 9
  slug: honeycomb-datasetdefinition
- name: DatasetUpdateRequest
  property_count: 2
  slug: honeycomb-datasetupdaterequest
- name: Environment
  property_count: 7
  slug: honeycomb-environment
- name: EnvironmentCreateRequest
  property_count: 3
  slug: honeycomb-environmentcreaterequest
- name: EnvironmentUpdateRequest
  property_count: 3
  slug: honeycomb-environmentupdaterequest
- name: Honeycomb Event
  property_count: 3
  slug: honeycomb-event
- name: Marker
  property_count: 8
  slug: honeycomb-marker
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
- name: Honeycomb Query Specification
  property_count: 11
  slug: honeycomb-query
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
- name: Recipient
  property_count: 5
  slug: honeycomb-recipient
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
  slug: honeycomb-servicemaprequest
- name: ServiceMapResult
  property_count: 2
  slug: honeycomb-servicemapresult
- name: Honeycomb SLO
  property_count: 8
  slug: honeycomb-slo
- name: SLOCreateRequest
  property_count: 5
  slug: honeycomb-slocreaterequest
- name: SLOReport
  property_count: 5
  slug: honeycomb-sloreport
- name: SLOUpdateRequest
  property_count: 5
  slug: honeycomb-sloupdaterequest
- name: Honeycomb Trigger
  property_count: 10
  slug: honeycomb-trigger
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
modified: '2026-05-30'
name: honeycomb
nav: Providers
network: true
overview: 'honeycomb publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Events API, Queries API, SLOs API, and 19 more.


  The honeycomb catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  honeycomb''s developer surface includes authentication, engineering blog, and 10 more developer resources.'
plans:
- name: Honeycomb Plans Pricing
  plan_count: 3
  slug: honeycomb-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 4
  name: Honeycomb Rate Limits
  slug: honeycomb-rate-limits
rules:
- name: honeycomb API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: honeycomb-asyncapi-spectral-rules
- name: honeycomb API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: honeycomb-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.0
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 80.6
    developer_ergonomics: 13.0
    discoverability: 50.0
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/honeycomb/refs/heads/main/screenshots/honeycomb-2026-06-20T182822.png
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
slug: honeycomb
---
