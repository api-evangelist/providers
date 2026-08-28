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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tempo Agentic Access
  operation_count: 7
  slug: tempo-agentic-access
  summary_line: 7 operations
api_count: 6
apis:
- description: TraceQL is a query language developed for Grafana Tempo that allows filtering and selecting spans within traces. The TraceQL search API endpoint enables rich span-level filtering using a pipeline synt
  name: Tempo TraceQL API
  slug: tempo-traceql-api
- description: Health and readiness endpoints
  name: Tempo Health API
  slug: tempo-health-api
- description: Generate metrics from trace data
  name: Tempo Metrics API
  slug: tempo-metrics-api
- description: Search traces and spans using TraceQL
  name: Tempo Search API
  slug: tempo-search-api
- description: Discover tag keys and values in trace data
  name: Tempo Tags API
  slug: tempo-tags-api
- description: Retrieve individual traces by trace ID
  name: Tempo Traces API
  slug: tempo-traces-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Grafana Tempo HTTP Health API
  slug: open-tempo-health-api
- collection_type: open
  name: Grafana Tempo HTTP Health Metrics API
  slug: open-tempo-metrics-api
- collection_type: open
  name: Grafana Tempo HTTP Health Search API
  slug: open-tempo-search-api
- collection_type: open
  name: Grafana Tempo HTTP Health Tags API
  slug: open-tempo-tags-api
- collection_type: open
  name: Grafana Tempo HTTP Health Traces API
  slug: open-tempo-traces-api
- collection_type: open
  name: Grafana Tempo HTTP API
  slug: open-tempo
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/grafana/tempo/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tempo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/tempo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tempo-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tempohq
- group: company
  title: ''
  type: Website
  url: https://grafana.com/oss/tempo/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/tempo/latest/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/grafana/tempo
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grafana
- group: other
  title: ''
  type: Helm Chart
  url: https://grafana.github.io/helm-charts
- group: other
  title: ''
  type: Docker Hub
  url: https://hub.docker.com/r/grafana/tempo
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/grafana/tempo/releases
- group: operate
  title: ''
  type: Community
  url: https://community.grafana.com/c/grafana-tempo/
- group: operate
  title: ''
  type: Slack
  url: https://grafana.slack.com/archives/C01BULREPHA
- group: company
  title: ''
  type: Blog
  url: https://grafana.com/blog/tag/traces/
- group: start
  title: ''
  type: GettingStarted
  url: https://grafana.com/docs/tempo/latest/getting-started/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/tempo-openapi.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tempo-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tempo-trace-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/tempo-trace-structure.json
- group: design
  title: ''
  type: SpectralRules
  url: rules/tempo-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tempo-vocabulary.yml
created: '2026-03-25'
description: Tempo is an open source, high-scale distributed tracing backend from Grafana Labs. Designed for cost-efficient, object storage-backed trace storage with minimal operational overhead. Integrates with popular open telemetry standards including OpenTelemetry, Jaeger, Zipkin, and W3C Trace Context. Provides HTTP query APIs for trace retrieval, search, tag discovery, and metrics generation.
examples:
- key_count: 2
  name: Tempo Get Trace Example
  slug: tempo-get-trace-example
- key_count: 2
  name: Tempo Search Traceql Example
  slug: tempo-search-traceql-example
finops:
- name: Tempo Finops
  service_category: API
  slug: tempo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tempo.png
json_schemas:
- name: Grafana Tempo Trace
  property_count: 1
  slug: tempo-trace
json_structures:
- name: Tempo Trace Structure
  property_count: 0
  slug: tempo-trace-structure
jsonld:
- class_count: 7
  name: Tempo Context
  property_count: 14
  slug: tempo-context
layout: provider
modified: '2026-05-19'
name: Tempo
nav: Providers
network: true
overview: 'Tempo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Health API, Metrics API, Search API, and 2 more. Tagged areas include Distributed Tracing, Observability, OpenTelemetry, Grafana, and Monitoring.


  The Tempo catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tempo''s developer surface includes documentation, release notes, engineering blog, getting-started guide, and 18 more developer resources.'
plans:
- name: Tempo Plans Pricing
  plan_count: 3
  slug: tempo-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Tempo Rate Limits
  slug: tempo-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tempo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tempo-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Tempo API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 6
  slug: tempo-rules
score:
  band: thin
  composite: 37.6
  delta: 1.5
  facets:
    access_clarity: 21.4
    commercial_clarity: 21.4
    contract_governance: 28.8
    contract_quality: 55.0
    developer_ergonomics: 31.0
    discoverability: 64.8
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tempo/refs/heads/main/screenshots/tempo-2026-06-20T195059.png
security:
- kind: domain-security
  name: Tempo Domain Security
  slug: tempo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Tempo Trust Center
  slug: tempo-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: tempo
tags:
- Distributed Tracing
- Observability
- OpenTelemetry
- Grafana
- Monitoring
website: https://grafana.com/oss/tempo/
---
