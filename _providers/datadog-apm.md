---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: Search, list and aggregate APM spans. Three operations covering cursor-paginated span search (POST and GET forms) and a span analytics aggregation that returns single numbers, single strings or timese
  name: Datadog APM Spans API
  phrasing_intents:
  - id: AggregateSpans
    intent: Aggregate spans into metrics and timeseries
    question: Can I compute p95 latency per service from my spans over a time range?
  - id: ListSpansGet
    intent: List recent spans matching a query
    question: What are the latest spans for a service in the last 15 minutes?
  - id: ListSpans
    intent: Search spans with a complex filter body
    question: How do I run an advanced span search with a full filter object in the request body?
  phrasing_ops: 3
  slug: datadog-apm-spans-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: Create, read, update and delete span-based metric definitions — a compute over a span attribute, a filter query and group-by tags. Five operations.
  name: Datadog APM Spans Metrics API
  phrasing_intents:
  - id: ListSpansMetrics
    intent: List span-based metrics
    question: Which custom metrics have we generated from our ingested spans?
  - id: CreateSpansMetric
    intent: Create a metric from ingested spans
    question: How do I turn span data into a long-lived metric?
  - id: DeleteSpansMetric
    intent: Delete a span-based metric
    question: How do I stop generating a metric from spans?
  - id: GetSpansMetric
    intent: Get one span-based metric
    question: What filter and group-bys does a particular span-based metric use?
  - id: UpdateSpansMetric
    intent: Update a span-based metric
    question: Can I change the filter on an existing span-based metric?
  phrasing_ops: 5
  slug: datadog-apm-spans-metrics-api
- description: 'Datadog''s first-party remote Model Context Protocol server. OAuth 2.1 with PKCE and dynamic client registration; a dedicated apm toolset covering span search, trace queries, Watchdog anomaly stories, '
  name: Datadog MCP Server
  slug: datadog-apm-mcp-server
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: Observe, troubleshoot, and improve cloud-scale applications with all telemetry in context
  name: Datadog APM API
  phrasing_intents:
  - id: GetServiceList
    intent: List APM services in an environment
    question: Which services is Datadog APM seeing in my production environment?
  phrasing_ops: 1
  slug: datadog-apm-apm-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: Manage configuration of [APM retention filters](https://app.datadoghq.com/apm/traces/retention-filters) for your organization. You need an API and application key with Admin rights to interact with th
  name: Datadog APM Retention Filters API
  phrasing_intents:
  - id: ListApmRetentionFilters
    intent: List APM retention filters
    question: Which retention filters decide what spans get indexed in my Datadog org?
  - id: CreateApmRetentionFilter
    intent: Create a span retention filter
    question: How do I start indexing a specific slice of my spans with a new retention filter?
  - id: ReorderApmRetentionFilters
    intent: Change the execution order of retention filters
    question: Can I change the order in which my retention filters are evaluated?
  - id: DeleteApmRetentionFilter
    intent: Delete a span retention filter
    question: How do I stop a retention filter from indexing spans by removing it?
  - id: GetApmRetentionFilter
    intent: Get one APM retention filter
    question: What query and sample rate does a particular retention filter use?
  - id: UpdateApmRetentionFilter
    intent: Update a span retention filter
    question: How do I change the query or rate on a retention filter I already have?
  phrasing_ops: 6
  slug: datadog-apm-apm-retention-filters-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: 'API to create, update, retrieve and delete service definitions. Note: Service Catalog [v3.0 schema](https://docs.datadoghq.com/service_catalog/service_definitions/v3-0/) has new API endpoints document'
  name: Datadog APM Service Definition API
  phrasing_intents:
  - id: ListServiceDefinitions
    intent: List Service Catalog definitions
    question: What services are registered in our Datadog Service Catalog?
  - id: CreateOrUpdateServiceDefinitions
    intent: Create or update a service definition
    question: How do I register a new service in the Service Catalog?
  - id: DeleteServiceDefinition
    intent: Delete a service definition
    question: How do I remove a retired service from the Service Catalog?
  - id: GetServiceDefinition
    intent: Get one service's catalog definition
    question: Who owns a given service according to the Service Catalog?
  phrasing_ops: 4
  slug: datadog-apm-service-definition-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: SLO Status Corrections allow you to prevent specific time periods from negatively impacting your SLO’s status and error budget. You can use Status Corrections for various purposes, such as removing pl
  name: Datadog APM Service Level Objective Corrections API
  phrasing_intents:
  - id: ListSLOCorrection
    intent: List all SLO corrections
    question: What SLO corrections exist across our whole Datadog org?
  - id: CreateSLOCorrection
    intent: Create an SLO correction window
    question: How do I exclude a maintenance window from my SLO calculations?
  - id: DeleteSLOCorrection
    intent: Delete an SLO correction
    question: How do I permanently remove a correction so that downtime counts against the SLO again?
  - id: GetSLOCorrection
    intent: Get one SLO correction
    question: What time window and category does a specific SLO correction cover?
  - id: UpdateSLOCorrection
    intent: Update an SLO correction
    question: Can I change the start or end time of a correction I already created?
  phrasing_ops: 5
  slug: datadog-apm-service-level-objective-corrections-api
- baseURL: https://api.datadoghq.com
  baseurl_source: declared
  description: '[Service Level Objectives](https://docs.datadoghq.com/monitors/service_level_objectives/#configuration) (or SLOs) are a key part of the site reliability engineering toolkit. SLOs provide a framework f'
  name: Datadog APM Service Level Objectives API
  phrasing_intents:
  - id: ListSLOs
    intent: List SLOs with filters
    question: Which SLOs in our org carry a particular tag?
  - id: CreateSLO
    intent: Create a service level objective
    question: How do I set up a 99.9% availability SLO over 30 days?
  - id: DeleteSLOTimeframeInBulk
    intent: Bulk delete SLO thresholds by timeframe
    question: Can I drop just the 7-day threshold from several SLOs at once?
  - id: CheckCanDeleteSLO
    intent: Check whether SLOs can be safely deleted
    question: Is an SLO still used on a dashboard before I delete it?
  - id: SearchSLO
    intent: Search SLOs with facets
    question: Which SLOs belong to a given service or team when I search by query syntax?
  - id: DeleteSLO
    intent: Delete an SLO
    question: Why does deleting an SLO return a conflict when it's on a dashboard?
  - id: GetSLO
    intent: Get an SLO's details
    question: What target and timeframe is a specific SLO configured with?
  - id: UpdateSLO
    intent: Update an existing SLO
    question: How do I raise the target on an SLO I already have?
  phrasing_ops: 10
  slug: datadog-apm-service-level-objectives-api
artifact_total: 29
asyncapis:
- description: ''
  name: Datadog Apm Webhooks
  slug: datadog-apm-webhooks
common:
- group: other
  href: https://artifacts.apis.io/datadog-apm/capabilities/datadog-apm-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/datadog-apm-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/datadog-apm/overlays/datadog-apm-retention-filters-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/datadog-apm-retention-filters-overlay.yaml
- group: other
  href: https://artifacts.apis.io/datadog-apm/overlays/datadog-apm-services-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/datadog-apm-services-overlay.yaml
- group: other
  href: https://artifacts.apis.io/datadog-apm/overlays/datadog-apm-service-definitions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/datadog-apm-service-definitions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/datadog-apm/overlays/datadog-apm-slos-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/datadog-apm-slos-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/datadog-apm/skills/datadog-apm-manage-slos.md
  title: ''
  type: AgentSkill
  url: skills/datadog-apm-manage-slos.md
- group: other
  href: https://artifacts.apis.io/datadog-apm/overlays/datadog-apm-slo-corrections-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/datadog-apm-slo-corrections-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.datadoghq.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.datadoghq.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datadoghq.com/tracing/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.datadoghq.com/api/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datadoghq.com/getting_started/tracing/
- group: operate
  title: ''
  type: Support
  url: https://www.datadoghq.com/support/
- group: company
  title: ''
  type: Blog
  url: https://www.datadoghq.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DataDog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datadoghq.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.datadoghq.com/free-datadog-trial/
- group: start
  title: ''
  type: Login
  url: https://app.datadoghq.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datadoghq.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datadoghq.com/legal/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/datadog-api/datadog-api/overview
- group: auth
  href: https://artifacts.apis.io/datadog-apm/authentication/datadog-apm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datadog-apm-authentication.yml
- group: auth
  href: https://artifacts.apis.io/datadog-apm/scopes/datadog-apm-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/datadog-apm-scopes.yml
- group: build
  href: https://artifacts.apis.io/datadog-apm/packages/datadog-apm-packages.yml
  title: ''
  type: Packages
  url: packages/datadog-apm-packages.yml
- group: build
  href: https://artifacts.apis.io/datadog-apm/packages/datadog-apm-packages.yml
  title: ''
  type: SDKs
  url: packages/datadog-apm-packages.yml
- group: build
  href: https://artifacts.apis.io/datadog-apm/cli/datadog-apm-cli.yml
  title: ''
  type: CLI
  url: cli/datadog-apm-cli.yml
- group: agent
  href: https://artifacts.apis.io/datadog-apm/mcp/datadog-apm-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/datadog-apm-mcp.yml
- group: build
  href: https://artifacts.apis.io/datadog-apm/mcp/datadog-apm-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/datadog-apm-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/datadog-apm/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/datadog-apm/well-known/datadog-apm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datadog-apm-well-known.yml
- group: auth
  href: https://artifacts.apis.io/datadog-apm/well-known/datadog-apm-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/datadog-apm-security.txt
- group: design
  href: https://artifacts.apis.io/datadog-apm/conventions/datadog-apm-conventions.yml
  title: ''
  type: Conventions
  url: conventions/datadog-apm-conventions.yml
- group: design
  href: https://artifacts.apis.io/datadog-apm/errors/datadog-apm-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/datadog-apm-problem-types.yml
- group: design
  href: https://artifacts.apis.io/datadog-apm/data-model/datadog-apm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datadog-apm-data-model.yml
- group: design
  href: https://artifacts.apis.io/datadog-apm/lifecycle/datadog-apm-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/datadog-apm-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datadoghq.com/
- group: operate
  href: https://artifacts.apis.io/datadog-apm/changelog/datadog-apm-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/datadog-apm-changelog.yml
- group: design
  href: https://artifacts.apis.io/datadog-apm/conformance/datadog-apm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datadog-apm-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.datadoghq.com/
- group: design
  href: https://artifacts.apis.io/datadog-apm/asyncapi/datadog-apm-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/datadog-apm-webhooks.yml
- group: other
  href: https://artifacts.apis.io/datadog-apm/grpc/datadog-apm-tracer_payload.proto
  title: ''
  type: Protobuf
  url: grpc/datadog-apm-tracer_payload.proto
- group: other
  href: https://artifacts.apis.io/datadog-apm/grpc/datadog-apm-span.proto
  title: ''
  type: Protobuf
  url: grpc/datadog-apm-span.proto
- group: other
  href: https://artifacts.apis.io/datadog-apm/grpc/datadog-apm-stats.proto
  title: ''
  type: Protobuf
  url: grpc/datadog-apm-stats.proto
- group: other
  href: https://artifacts.apis.io/datadog-apm/grpc/datadog-apm-agent_payload.proto
  title: ''
  type: Protobuf
  url: grpc/datadog-apm-agent_payload.proto
- group: operate
  href: https://artifacts.apis.io/datadog-apm/rate-limits/datadog-apm-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/datadog-apm-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/datadog-apm/plans/datadog-apm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datadog-apm-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/datadog-apm/finops/datadog-apm-finops.yml
  title: ''
  type: FinOps
  url: finops/datadog-apm-finops.yml
- group: auth
  href: https://artifacts.apis.io/datadog-apm/security/datadog-apm-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/datadog-apm-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/datadog-apm/security/datadog-apm-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/datadog-apm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.datadoghq.com/security/
- group: auth
  href: https://artifacts.apis.io/datadog-apm/security/datadog-apm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datadog-apm-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/datadog-apm/llms/datadog-apm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datadog-apm-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.datadoghq.com/llms.txt
- group: docs
  href: https://artifacts.apis.io/datadog-apm/json-schema/trace.yml
  title: ''
  type: JSONSchema
  url: json-schema/trace.yml
- group: design
  href: https://artifacts.apis.io/datadog-apm/json-ld/datadog-apm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datadog-apm-context.jsonld
- group: design
  href: https://artifacts.apis.io/datadog-apm/vocabulary/datadog-apm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datadog-apm-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datadog-apm/rules/datadog-apm-rules.yml
  title: ''
  type: Rules
  url: rules/datadog-apm-rules.yml
created: '2026-03-26'
description: Datadog APM provides end-to-end distributed tracing, continuous profiling, and real-time performance monitoring for applications and microservices. It automatically instruments applications to provide deep visibility into request traces, latency, and error rates across distributed systems.
finops:
- has_sources: true
  method: derived
  name: Datadog Apm Finops
  primary_unit: host
  service_category: ''
  slug: datadog-apm-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/datadog-apm.png
jsonld:
- class_count: 0
  name: Datadog Apm Context
  property_count: 5
  slug: datadog-apm-context
layout: provider
mcp_servers:
- description: Datadog operates a first-party remote MCP server that bridges AI agents to Datadog observability data. It is not APM-specific — it exposes most Datadog products — but it ships a dedicated `apm` toolse
  name: Datadog MCP Server
  slug: datadog-mcp-server
modified: '2026-09-16'
name: Datadog APM
nav: Providers
network: true
overview: 'Datadog APM publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Spans API, Spans Metrics API, and 6 more. Tagged areas include APM, Distributed Tracing, Microservices, Observability, and Performance Monitoring.


  The Datadog APM catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Datadog APM''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 50 more developer resources.'
plans:
- name: Datadog Apm Plans Pricing
  plan_count: 15
  slug: datadog-apm-plans-pricing
- name: Datadog Apm Price Estimates
  plan_count: 0
  slug: datadog-apm-price-estimates
random_paper: 7
rate_limits:
- limit_count: 3
  name: Datadog Apm Rate Limits
  slug: datadog-apm-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Datadog APM — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: datadog-apm-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 46
  extends:
  - spectral:oas
  name: Datadog APM API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: datadog-apm-rules
scopes:
- name: Datadog Apm Scopes
  scope_count: 96
  slug: datadog-apm-scopes
  summary_line: 96 scopes · authorizationCode
score:
  band: exemplar
  composite: 82.0
  coverage:
    artifact_dirs: 32
    catalog_earned: 78.0
    catalog_earned_first_party: 24.0
    catalog_gap: 37.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 64.2
    developer_ergonomics: 80.2
    discoverability: 75.0
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 82.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/datadog-apm/datadog-apm-2026-06-20T175636.png
security:
- kind: authentication
  name: Datadog Apm Authentication
  slug: datadog-apm-authentication
  summary_line: apiKey/http/oauth2 · 6 schemes
- kind: domain-security
  name: Datadog Apm Domain Security
  slug: datadog-apm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Datadog Apm Vulnerability Disclosure
  slug: datadog-apm-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Datadog Apm Trust Center
  slug: datadog-apm-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
skill_count: 7
skills:
- name: datadog-app
  slug: datadog-apm-datadog-app
- name: ddconfig
  slug: datadog-apm-ddconfig
- name: ddsetup
  slug: datadog-apm-ddsetup
- name: ddtoolsets
  slug: datadog-apm-ddtoolsets
- name: ddviz
  slug: datadog-apm-ddviz
- name: datadog-apm-manage-slos
  slug: datadog-apm-manage-slos
- name: datadog-apm-search-spans
  slug: datadog-apm-search-spans
slug: datadog-apm
tags:
- APM
- Distributed Tracing
- Microservices
- Observability
- Performance Monitoring
- Spans
- SLO
- Service Catalog
- OpenTelemetry
- MCP
website: https://www.datadoghq.com/
---
