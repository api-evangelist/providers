---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
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
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 50
  human_in_the_loop: 0
  name: Honeycomb Io Agentic Access
  operation_count: 85
  slug: honeycomb-io-agentic-access
  summary_line: 85 operations · 50 acting
api_count: 21
apis:
- description: API Keys have various scopes permissions and belong to a specific Team or Environment. Any valid Honeycomb ingest or configuration API Key will work with this endpoint. Learn more about [API keys](htt
  name: Honeycomb Auth API
  slug: honeycomb-io-auth-api
- description: 'Boards are a place to pin and save useful queries/graphs, SLO panels, text panels, and views you want to retain for later reuse and reference. Boards can contain multiple panel types: - **Query panels'
  name: Honeycomb Boards API
  slug: honeycomb-io-boards-api
- description: This feature is available as part of the [Honeycomb Pro and Enterprise plans](https://www.honeycomb.io/pricing/). Burn Alerts notify you when issues impact your SLO budget. Learn more about [Burn Aler
  name: Honeycomb Burn Alerts API
  slug: honeycomb-io-burn-alerts-api
- description: Calculated Fields (also called Derived Columns) allow you to run queries based on the value of an expression that is calculated from the fields in an event. This API allows you to list, create, update
  name: Honeycomb Calculated Fields API
  slug: honeycomb-io-calculated-fields-api
- description: 'Columns are fields in the events you send to Honeycomb. This API allows you to list, create, update, and delete columns in a dataset. ## Authorization The API key must have the **Manage Queries and Co'
  name: Honeycomb Columns API
  slug: honeycomb-io-columns-api
- description: Dataset definitions describe the fields with special meaning in the Dataset. Refer to the [Dataset Definitions](https://docs.honeycomb.io/configure/datasets/definitions/) documentation for more inform
  name: Honeycomb Dataset Definitions API
  slug: honeycomb-io-dataset-definitions-api
- description: 'A Dataset represents a collection of related events that come from the same source, or are related to the same source. This API allows you to list, create, and update datasets. ## Authorization The AP'
  name: Honeycomb Datasets API
  slug: honeycomb-io-datasets-api
- description: 'This API allows you to list, create, and update, and delete Environments. ## Authorization This API requires a Management Key passed via the HTTP Authorization header. Join the key ID and secret with '
  name: Honeycomb Environments API
  slug: honeycomb-io-environments-api
- description: 'The Events API endpoints are the lowest-level way to send Events to Honeycomb. **This should be your last resort!** If unsure where to start when instrumenting an application, read about how to [Send '
  name: Honeycomb Events API
  slug: honeycomb-io-events-api
- description: 'This API allows you to list, create, update, and delete API Keys for a Team. Learn more about [API keys here](https://docs.honeycomb.io/configure/environments/manage-api-keys/). ## Authorization This '
  name: Honeycomb Key Management API
  slug: honeycomb-io-key-management-api
- description: The Kinesis Events API endpoints allow Honeycomb to process streaming events from Amazon Kinesis. Refer to the [Honeycomb AWS integrations](https://docs.honeycomb.io/integrations/aws/how-aws-integrati
  name: Honeycomb Kinesis Events API
  slug: honeycomb-io-kinesis-events-api
- description: 'Marker Settings apply to groups of similar Markers. For example, "deploys" markers appear with the same color on a graph. This API allows you to list, create, update, and delete Marker Settings. ## Au'
  name: Honeycomb Marker Settings API
  slug: honeycomb-io-marker-settings-api
- description: 'Markers indicate points in time on graphs where interesting things happen, such as deploys or outages. This API allows you to list, create, update, and delete Markers. ## Authorization The API key mus'
  name: Honeycomb Markers API
  slug: honeycomb-io-markers-api
- description: 'Queries in Honeycomb are specifications for queries, and are used to identify queries in other parts of the API - in particular: boards, triggers, and query annotations. This API allows you to create '
  name: Honeycomb Queries API
  slug: honeycomb-io-queries-api
- description: Query Annotations in Honeycomb allow you to associate names and descriptions to queries to add additional information in collaboration features. This API allows you to list, create, update, and delete
  name: Honeycomb Query Annotations API
  slug: honeycomb-io-query-annotations-api
- description: This feature is available as part of the [Honeycomb Enterprise plan](https://www.honeycomb.io/pricing/). Query Results are the aggregated data from a Query, similar to what is displayed in graphs or h
  name: Honeycomb Query Data API
  slug: honeycomb-io-query-data-api
- description: 'Honeycomb Recipients allow you to define and manage the Recipients that will get notified by a Trigger or Burn Alert. The types of Recipients supported are: PagerDuty, Email, Webhook, Microsoft Teams,'
  name: Honeycomb Recipients API
  slug: honeycomb-io-recipients-api
- description: 'The Reporting API provides access to historical performance data. ## Authorization The API key must have the **Manage SLOs** permission. Learn more about [API keys here](https://docs.honeycomb.io/conf'
  name: Honeycomb Reporting API
  slug: honeycomb-io-reporting-api
- description: The Service Maps API endpoints allow you to visualize the relationships between your services in Honeycomb. This API allows you to create and retrieve service Dependency Requests, which are used to ge
  name: Honeycomb Service Maps API
  slug: honeycomb-io-service-maps-api
- description: This feature is available as part of the [Honeycomb Pro and Enterprise plans](https://www.honeycomb.io/pricing). Honeycomb SLOs allow you to define and monitor Service Level Objectives (SLOs) for your
  name: Honeycomb SLOs API
  slug: honeycomb-io-slos-api
- description: 'Triggers let you receive notifications when your data in Honeycomb crosses the thresholds that you configure. The graph on which to alert is as flexible as a Honeycomb query, which helps reduce false '
  name: Honeycomb Triggers API
  slug: honeycomb-io-triggers-api
artifact_total: 53
collections:
- collection_type: open
  name: Honeycomb Auth API
  slug: open-honeycomb-auth-api
- collection_type: open
  name: Honeycomb Boards API
  slug: open-honeycomb-boards-api
- collection_type: open
  name: Honeycomb Columns API
  slug: open-honeycomb-columns-api
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
  name: Honeycomb Key Management API
  slug: open-honeycomb-key-management-api
- collection_type: open
  name: Honeycomb Markers API
  slug: open-honeycomb-markers-api
- collection_type: open
  name: Honeycomb Queries API
  slug: open-honeycomb-queries-api
- collection_type: open
  name: Honeycomb Service Maps API
  slug: open-honeycomb-service-maps-api
- collection_type: open
  name: Honeycomb SLOs API
  slug: open-honeycomb-slos-api
- collection_type: open
  name: Honeycomb Triggers API
  slug: open-honeycomb-triggers-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/honeycomb-io-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/honeycomb-io-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/honeycomb-io-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.honeycomb.io/api/
- group: start
  title: ''
  type: Portal
  url: https://docs.honeycomb.io/
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.honeycomb.io/api/openapi-public.yaml
- group: auth
  title: ''
  type: Authentication
  url: https://docs.honeycomb.io/get-started/best-practices/api-keys/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.honeycomb.io/
- group: company
  title: ''
  type: Blog
  url: https://www.honeycomb.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.honeycomb.io/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.honeycomb.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://docs.honeycomb.io/troubleshoot/community/
- group: operate
  title: ''
  type: Support
  url: https://support.honeycomb.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/honeycomb-io/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/honeycombio
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/honeycombio
- group: company
  title: ''
  type: Website
  url: https://www.honeycomb.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.honeycomb.io/product/honeycomb-intelligence
- group: docs
  title: ''
  type: Documentation
  url: https://www.honeycomb.io/product/telemetry-pipeline
- group: other
  title: ''
  type: Standards
  url: https://opentelemetry.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/honeycomb-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/honeycomb-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/honeycomb-io-finops.yml
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/honeycombio/refinery
- group: build
  title: ''
  type: SDKs
  url: https://github.com/honeycombio/honeycomb-opentelemetry-web
- group: build
  title: ''
  type: SDKs
  url: https://github.com/honeycombio/honeycomb-opentelemetry-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/honeycombio/honeycomb-opentelemetry-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/honeycombio/honeycomb-opentelemetry-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/honeycombio/libhoney-py
- group: build
  title: ''
  type: SDKs
  url: https://github.com/honeycombio/libhoney-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/honeycombio/libhoney-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/honeycombio/libhoney-dotnet
- group: build
  title: ''
  type: Tools
  url: https://github.com/honeycombio/terraform-provider-honeycombio
- group: build
  title: ''
  type: Tools
  url: https://github.com/honeycombio/honeycomb-kubernetes-agent
- group: build
  title: ''
  type: Tools
  url: https://github.com/honeycombio/helm-charts
- group: build
  title: ''
  type: Tools
  url: https://github.com/honeycombio/honeytail
- group: build
  title: ''
  type: Tools
  url: https://github.com/honeycombio/buildevents
- group: build
  title: ''
  type: Tools
  url: https://github.com/honeycombio/gha-buildevents
- group: build
  title: ''
  type: Tools
  url: https://github.com/honeycombio/honeycomb-lambda-extension
- group: build
  title: ''
  type: Tools
  url: https://github.com/honeycombio/honeyaws
- group: agent
  title: ''
  type: MCP
  url: https://github.com/honeycombio/honeycomb-mcp
examples:
- key_count: 2
  name: Honeycomb Create Marker Example
  slug: honeycomb-create-marker-example
- key_count: 2
  name: Honeycomb Run Query Example
  slug: honeycomb-run-query-example
- key_count: 2
  name: Honeycomb Send Event Example
  slug: honeycomb-send-event-example
finops:
- name: Honeycomb Io Finops
  service_category: Management and Governance
  slug: honeycomb-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/honeycomb-io.png
json_schemas:
- name: Honeycomb Board
  property_count: 9
  slug: honeycomb-board
- name: Honeycomb Column
  property_count: 1
  slug: honeycomb-column
- name: Honeycomb Dataset
  property_count: 9
  slug: honeycomb-dataset
- name: Honeycomb Marker
  property_count: 9
  slug: honeycomb-marker
- name: Honeycomb Query
  property_count: 16
  slug: honeycomb-query
- name: Honeycomb Recipient
  property_count: 1
  slug: honeycomb-recipient
- name: Honeycomb SLO
  property_count: 11
  slug: honeycomb-slo
json_structures:
- name: Honeycomb Event Structure
  property_count: 18
  slug: honeycomb-event-structure
jsonld:
- class_count: 0
  name: Honeycomb Io Context
  property_count: 12
  slug: honeycomb-io-context
layout: provider
name: Honeycomb
nav: Providers
network: true
overview: 'Honeycomb publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Boards API, Burn Alerts API, and 18 more. Tagged areas include Observability, Tracing, Distributed Tracing, Telemetry, and OpenTelemetry.


  The Honeycomb catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Honeycomb''s developer surface includes documentation, developer portal, authentication, engineering blog, changelog, pricing, support, and 34 more developer resources.'
plans:
- name: Honeycomb Io Plans Pricing
  plan_count: 4
  slug: honeycomb-io-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Honeycomb Io Rate Limits
  slug: honeycomb-io-rate-limits
rules:
- name: Honeycomb API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: honeycomb-io-jsonschema-spectral-rules
- name: Honeycomb API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 6
  slug: honeycomb-rules
score:
  band: strong
  composite: 60.8
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 66.5
    developer_ergonomics: 50.0
    discoverability: 55.0
    governance: 73.7
    operational_transparency: 63.2
  previous_composite: 60.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/honeycomb-io/refs/heads/main/screenshots/honeycomb-io-2026-06-20T182823.png
security:
- kind: domain-security
  name: Honeycomb Io Domain Security
  slug: honeycomb-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Honeycomb Io Trust Center
  slug: honeycomb-io-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR, CSA STAR
slug: honeycomb-io
tags:
- Observability
- Tracing
- Distributed Tracing
- Telemetry
- OpenTelemetry
- Events
- Logs
- Metrics
- SLO
- AIOps
- AI Observability
website: https://www.honeycomb.io/
---
