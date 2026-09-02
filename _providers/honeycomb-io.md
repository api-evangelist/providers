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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 50
  human_in_the_loop: 0
  name: Honeycomb Io Agentic Access
  operation_count: 85
  slug: honeycomb-io-agentic-access
  summary_line: 85 operations · 50 acting
api_count: 13
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
- description: The Anomaly Detection API exposes Honeycomb Signals - the anomaly detection profiles Honeycomb maintains per service - and their historical anomalies. List and retrieve Signals, update a Signal's conf
  name: Honeycomb Anomaly Detection API
  slug: honeycomb-io-anomaly-detection-api
artifact_total: 102
asyncapis:
- description: ''
  name: Honeycomb Io Webhooks
  slug: honeycomb-io-webhooks
collections:
- collection_type: postman
  name: Honeycomb Auth API
  slug: postman-honeycomb-io-auth-api
- collection_type: postman
  name: Honeycomb Auth Boards API
  slug: postman-honeycomb-io-boards-api
- collection_type: postman
  name: Honeycomb Auth Burn Alerts API
  slug: postman-honeycomb-io-burn-alerts-api
- collection_type: postman
  name: Honeycomb Auth Calculated Fields API
  slug: postman-honeycomb-io-calculated-fields-api
- collection_type: postman
  name: Honeycomb Auth Columns API
  slug: postman-honeycomb-io-columns-api
- collection_type: postman
  name: Honeycomb Auth Dataset Definitions API
  slug: postman-honeycomb-io-dataset-definitions-api
- collection_type: postman
  name: Honeycomb Auth Datasets API
  slug: postman-honeycomb-io-datasets-api
- collection_type: postman
  name: Honeycomb Auth Environments API
  slug: postman-honeycomb-io-environments-api
- collection_type: postman
  name: Honeycomb Auth Events API
  slug: postman-honeycomb-io-events-api
- collection_type: postman
  name: Honeycomb Auth Key Management API
  slug: postman-honeycomb-io-key-management-api
- collection_type: postman
  name: Honeycomb Auth Kinesis Events API
  slug: postman-honeycomb-io-kinesis-events-api
- collection_type: postman
  name: Honeycomb Auth Marker Settings API
  slug: postman-honeycomb-io-marker-settings-api
- collection_type: postman
  name: Honeycomb Auth Markers API
  slug: postman-honeycomb-io-markers-api
- collection_type: postman
  name: Honeycomb Auth Queries API
  slug: postman-honeycomb-io-queries-api
- collection_type: postman
  name: Honeycomb Auth Query Annotations API
  slug: postman-honeycomb-io-query-annotations-api
- collection_type: postman
  name: Honeycomb Auth Query Data API
  slug: postman-honeycomb-io-query-data-api
- collection_type: postman
  name: Honeycomb Auth Recipients API
  slug: postman-honeycomb-io-recipients-api
- collection_type: postman
  name: Honeycomb Auth Reporting API
  slug: postman-honeycomb-io-reporting-api
- collection_type: postman
  name: Honeycomb Auth Service Maps API
  slug: postman-honeycomb-io-service-maps-api
- collection_type: postman
  name: Honeycomb Auth SLOs API
  slug: postman-honeycomb-io-slos-api
- collection_type: postman
  name: Honeycomb Auth Triggers API
  slug: postman-honeycomb-io-triggers-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  name: Honeycomb Auth API
  slug: open-honeycomb-io-auth-api
- collection_type: open
  name: Honeycomb Auth Boards API
  slug: open-honeycomb-io-boards-api
- collection_type: open
  name: Honeycomb Auth Burn Alerts API
  slug: open-honeycomb-io-burn-alerts-api
- collection_type: open
  name: Honeycomb Auth Calculated Fields API
  slug: open-honeycomb-io-calculated-fields-api
- collection_type: open
  name: Honeycomb Auth Columns API
  slug: open-honeycomb-io-columns-api
- collection_type: open
  name: Honeycomb Auth Dataset Definitions API
  slug: open-honeycomb-io-dataset-definitions-api
- collection_type: open
  name: Honeycomb Auth Datasets API
  slug: open-honeycomb-io-datasets-api
- collection_type: open
  name: Honeycomb Auth Environments API
  slug: open-honeycomb-io-environments-api
- collection_type: open
  name: Honeycomb Auth Events API
  slug: open-honeycomb-io-events-api
- collection_type: open
  name: Honeycomb Auth Key Management API
  slug: open-honeycomb-io-key-management-api
- collection_type: open
  name: Honeycomb Auth Kinesis Events API
  slug: open-honeycomb-io-kinesis-events-api
- collection_type: open
  name: Honeycomb Auth Marker Settings API
  slug: open-honeycomb-io-marker-settings-api
- collection_type: open
  name: Honeycomb Auth Markers API
  slug: open-honeycomb-io-markers-api
- collection_type: open
  name: Honeycomb Auth Queries API
  slug: open-honeycomb-io-queries-api
- collection_type: open
  name: Honeycomb Auth Query Annotations API
  slug: open-honeycomb-io-query-annotations-api
- collection_type: open
  name: Honeycomb Auth Query Data API
  slug: open-honeycomb-io-query-data-api
- collection_type: open
  name: Honeycomb Auth Recipients API
  slug: open-honeycomb-io-recipients-api
- collection_type: open
  name: Honeycomb Auth Reporting API
  slug: open-honeycomb-io-reporting-api
- collection_type: open
  name: Honeycomb Auth Service Maps API
  slug: open-honeycomb-io-service-maps-api
- collection_type: open
  name: Honeycomb Auth SLOs API
  slug: open-honeycomb-io-slos-api
- collection_type: open
  name: Honeycomb Auth Triggers API
  slug: open-honeycomb-io-triggers-api
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
- group: commercial
  title: ''
  type: License
  url: https://github.com/honeycombio/agent-skill/blob/main/LICENSE
- group: auth
  title: ''
  type: Authentication
  url: authentication/honeycomb-io-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/honeycomb/overview
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
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/honeycombio/honeycomb-mcp
- group: operate
  title: ''
  type: ChangeLog
  url: https://api-changelog.honeycomb.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.honeycomb.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/honeycomb.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.honeycomb.io/platform/telemetry-pipeline
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.honeycomb.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.honeycomb.io/api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.honeycomb.io/get-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/honeycombio
- group: start
  title: ''
  type: SignUp
  url: https://ui.honeycomb.io/signup
- group: start
  title: ''
  type: Login
  url: https://ui.honeycomb.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.honeycomb.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.honeycomb.io/privacy
- group: start
  title: ''
  type: Sandbox
  url: sandbox/honeycomb-io-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: security/honeycomb-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: https://docs.honeycomb.io/security-compliance/bug-bounty-program/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.honeycomb.io/security-compliance/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/honeycomb-io-well-known.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/honeycomb-io-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/honeycomb-io-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/honeycomb-io-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/honeycomb-io-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/honeycomb-io-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/honeycomb-io-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/honeycomb-io-cli.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/honeycomb-io-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/honeycomb-io-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/honeycomb-io-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/honeycomb-io-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.honeycomb.io/troubleshoot/product-lifecycle/release-stages/
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/honeycomb-io-scopes.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/honeycomb-io-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/honeycomb-io-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/honeycomb-io-webhooks.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.honeycomb.io/notify/webhooks/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.honeycomb.io/integrations/mcp/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.honeycomb.io/integrations/agent-skills/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/honeycombio/agent-skill
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.honeycomb.io/
created: '2026-05-25'
description: 'Honeycomb is an observability platform for understanding complex distributed systems through high-cardinality, high-dimensional telemetry. Founded in 2016 by Charity Majors and Christine Yen and headquartered in San Francisco, it stores traces, logs and metrics as wide events and lets engineers query arbitrarily across every field at interactive speed, rather than pre-defining dashboards and thresholds. Honeycomb is OpenTelemetry-native: OTLP is the documented ingest path and the company has moved its own proprietary Beelines and distributions to End of Life in favour of upstream OpenTelemetry SDKs. The public REST API is described by a single OpenAPI 3.1 contract covering 89 operations across 22 resource groups - events, datasets, columns, calculated fields, queries, query data, boards, triggers, SLOs, burn alerts, markers, recipients, service maps, environments, API keys and anomaly detection signals - split across US and EU regions. Honeycomb also runs a first-party OAuth-protected
  Model Context Protocol server at mcp.honeycomb.io, publishes A2A and Agent Skills discovery documents from its docs host, and ships an official agent-skills plugin, making it one of the more complete agent-facing surfaces in the observability category. Products include the core observability platform, Refinery tail-based sampling, Telemetry Pipeline, and Canvas AI-assisted investigations.'
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
mcp_servers:
- description: 'Honeycomb operates a first-party hosted Model Context Protocol server at https://mcp.honeycomb.io/mcp (EU: https://mcp.eu1.honeycomb.io/mcp). It is OAuth-protected: an unauthenticated POST returns 401'
  name: Honeycomb MCP
  slug: honeycomb-mcp
modified: '2026-08-24'
name: Honeycomb
nav: Providers
network: true
overview: 'Honeycomb publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Boards API, Burn Alerts API, and 19 more. Tagged areas include Observability, Tracing, Distributed Tracing, Telemetry, and OpenTelemetry.


  The Honeycomb catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Honeycomb''s developer surface includes authentication, documentation, developer portal, engineering blog, pricing, support, tooling, and 72 more developer resources.'
plans:
- name: Honeycomb Io Plans Pricing
  plan_count: 4
  slug: honeycomb-io-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Honeycomb Io Rate Limits
  slug: honeycomb-io-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Honeycomb API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: honeycomb-io-jsonschema-spectral-rules
- effective_rule_count: 78
  extends:
  - spectral:oas
  - spectral:asyncapi
  name: Honeycomb API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 6
  slug: honeycomb-rules
scopes:
- name: Honeycomb Io Scopes
  scope_count: 0
  slug: honeycomb-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 82.0
  coverage:
    artifact_dirs: 34
    catalog_gap: 38.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 73.2
    developer_ergonomics: 100.0
    discoverability: 75.9
    governance: 31.8
    operational_transparency: 94.7
  previous_composite: 82.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/honeycomb-io/refs/heads/main/screenshots/honeycomb-io-2026-06-20T182823.png
security:
- kind: authentication
  name: Honeycomb Io Authentication
  slug: honeycomb-io-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Honeycomb Io Domain Security
  slug: honeycomb-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Honeycomb Io Vulnerability Disclosure
  slug: honeycomb-io-vulnerability-disclosure
  summary_line: contact published
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
- Event
- Logs
- Metrics
- SLO
- AIOps
- AI Observability
website: https://www.honeycomb.io/
---
