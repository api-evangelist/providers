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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Jaeger Agentic Access
  operation_count: 9
  slug: jaeger-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: The Jaeger Collector API receives trace spans from instrumented applications and SDKs. Since Jaeger v1.11 the primary protocol is the jaeger.api_v2.CollectorService gRPC endpoint; the collector also a
  name: Jaeger Collector API
  slug: jaeger-collector-api
- description: The Jaeger Remote Storage API is a gRPC-based interface that allows extending Jaeger with custom storage backends. Any backend implementing this API can be deployed as a remote gRPC server and plugged
  name: Jaeger Remote Storage API
  slug: jaeger-remote-storage-api
- description: The Jaeger Remote Sampling API provides HTTP and gRPC endpoints that SDKs use to retrieve sampling strategies for distributed trace collection. It is implemented by the jaeger-collector and defined in
  name: Jaeger Remote Sampling API
  slug: jaeger-remote-sampling-api
- description: Endpoints for retrieving service dependency graphs.
  name: Jaeger Dependencies API
  slug: jaeger-dependencies-api
- description: Endpoints for retrieving service performance metrics including latency, call rates, and error rates.
  name: Jaeger Metrics API
  slug: jaeger-metrics-api
- description: Endpoints for listing services and their operations.
  name: Jaeger Services API
  slug: jaeger-services-api
- description: Endpoints for searching and retrieving distributed traces.
  name: Jaeger Traces API
  slug: jaeger-traces-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Jaeger Query Dependencies API
  slug: open-jaeger-dependencies-api
- collection_type: open
  name: Jaeger Query Dependencies Metrics API
  slug: open-jaeger-metrics-api
- collection_type: open
  name: Jaeger Query API
  slug: open-jaeger-query-api
- collection_type: open
  name: Jaeger Query Dependencies Services API
  slug: open-jaeger-services-api
- collection_type: open
  name: Jaeger Query Dependencies Traces API
  slug: open-jaeger-traces-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/jaegertracing/jaeger/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/jaegertracing/jaeger/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/jaegertracing/jaeger/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/jaegertracing/jaeger/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/jaegertracing/jaeger/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/jaegertracing/jaeger/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jaeger-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jaeger-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jaegertracing.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.jaegertracing.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.jaegertracing.io/docs/latest/getting-started/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jaegertracing
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jaegertracing/jaeger
- group: company
  title: ''
  type: Blog
  url: https://www.jaegertracing.io/news/
- group: operate
  title: ''
  type: Community
  url: https://www.jaegertracing.io/get-involved/
- group: operate
  title: ''
  type: Support
  url: https://www.jaegertracing.io/get-in-touch/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/jaegertracing/jaeger/blob/main/CHANGELOG.md
- group: design
  title: ''
  type: JSONLD
  url: json-ld/jaeger-trace.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/jaeger-trace.yml
created: '2025-01-01'
description: Jaeger is an open source, end-to-end distributed tracing system for monitoring and troubleshooting microservices-based architectures. Jaeger provides visibility into distributed system behavior through trace collection, storage, and visualization.
finops:
- name: Jaeger Finops
  service_category: API
  slug: jaeger-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jaeger.png
layout: provider
modified: '2026-05-19'
name: Jaeger
nav: Providers
network: true
overview: 'Jaeger publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Dependencies API, Metrics API, Services API, and 1 more. Tagged areas include Distributed Tracing, Microservices, Monitoring, and Observability.


  The Jaeger catalog on APIs.io includes 1 Spectral governance ruleset.


  Jaeger''s developer surface includes documentation, getting-started guide, engineering blog, support, changelog, and 14 more developer resources.'
plans:
- name: Jaeger Plans Pricing
  plan_count: 3
  slug: jaeger-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Jaeger Rate Limits
  slug: jaeger-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Jaeger API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: jaeger-jsonschema-spectral-rules
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 66.8
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 6.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 46.1
    developer_ergonomics: 35.7
    discoverability: 50.0
    governance: 9.8
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 30.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/jaeger/refs/heads/main/screenshots/jaeger-2026-06-20T183651.png
security:
- kind: domain-security
  name: Jaeger Domain Security
  slug: jaeger-domain-security
  summary_line: TLSv1.3 · HSTS
slug: jaeger
tags:
- Distributed Tracing
- Microservices
- Monitoring
- Observability
website: https://www.jaegertracing.io/
---
