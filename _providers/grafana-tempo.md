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
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Grafana Tempo Agentic Access
  operation_count: 10
  slug: grafana-tempo-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- baseURL: http://localhost:3200
  baseurl_source: spec
  description: The Echo API from Grafana Tempo — 1 operation(s) for echo.
  name: Grafana Tempo Echo API
  slug: grafana-tempo-echo-api
- baseURL: http://localhost:3200
  baseurl_source: spec
  description: The Metrics API from Grafana Tempo — 1 operation(s) for metrics.
  name: Grafana Tempo Metrics API
  slug: grafana-tempo-metrics-api
- baseURL: http://localhost:3200
  baseurl_source: spec
  description: The Ready API from Grafana Tempo — 1 operation(s) for ready.
  name: Grafana Tempo Ready API
  slug: grafana-tempo-ready-api
- baseURL: http://localhost:3200
  baseurl_source: spec
  description: The Search API from Grafana Tempo — 5 operation(s) for search.
  name: Grafana Tempo Search API
  slug: grafana-tempo-search-api
- baseURL: http://localhost:3200
  baseurl_source: spec
  description: The Status API from Grafana Tempo — 1 operation(s) for status.
  name: Grafana Tempo Status API
  slug: grafana-tempo-status-api
- baseURL: http://localhost:3200
  baseurl_source: spec
  description: The Traces API from Grafana Tempo — 1 operation(s) for traces.
  name: Grafana Tempo Traces API
  slug: grafana-tempo-traces-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Grafana Tempo HTTP Echo API
  slug: open-grafana-tempo-echo-api
- collection_type: open
  name: Grafana Tempo HTTP Echo Metrics API
  slug: open-grafana-tempo-metrics-api
- collection_type: open
  name: Grafana Tempo HTTP Echo Ready API
  slug: open-grafana-tempo-ready-api
- collection_type: open
  name: Grafana Tempo HTTP Echo Search API
  slug: open-grafana-tempo-search-api
- collection_type: open
  name: Grafana Tempo HTTP Echo Status API
  slug: open-grafana-tempo-status-api
- collection_type: open
  name: Grafana Tempo HTTP Echo Traces API
  slug: open-grafana-tempo-traces-api
- collection_type: open
  name: Grafana Tempo HTTP API
  slug: open-tempo-http-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/grafana-tempo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/grafana-tempo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grafana-tempo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grafana.com/oss/tempo/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/tempo/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://grafana.com/docs/tempo/latest/getting-started/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/grafana/tempo
- group: company
  title: ''
  type: Blog
  url: https://grafana.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://grafana.com/pricing/
- group: agent
  title: ''
  type: LlmsText
  url: https://grafana.com/llms.txt
created: '2026-03-26'
description: Grafana Tempo is an open-source, high-scale distributed tracing backend that requires only object storage to operate, making it cost-effective and easy to run. It integrates deeply with Grafana, Prometheus, and Loki for seamless observability across metrics, logs, and traces.
finops:
- name: Grafana Tempo Finops
  service_category: API
  slug: grafana-tempo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/grafana-tempo.png
layout: provider
modified: '2026-05-19'
name: Grafana Tempo
nav: Providers
network: true
overview: 'Grafana Tempo publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Echo API, Metrics API, Ready API, and 3 more. Tagged areas include Distributed Tracing, Grafana, Microservices, Observability, and Open-Source.


  The Grafana Tempo catalog on APIs.io includes 1 Spectral governance ruleset.


  Grafana Tempo''s developer surface includes documentation, getting-started guide, GitHub presence, engineering blog, pricing, and 5 more developer resources.'
plans:
- name: Grafana Tempo Plans Pricing
  plan_count: 3
  slug: grafana-tempo-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Grafana Tempo Rate Limits
  slug: grafana-tempo-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Grafana Tempo API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: grafana-tempo-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 12
    catalog_earned: 50.3
    catalog_earned_first_party: 0.0
    catalog_gap: 64.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 49.4
    developer_ergonomics: 23.8
    discoverability: 66.7
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grafana-tempo/refs/heads/main/screenshots/grafana-tempo-2026-06-20T182315.png
security:
- kind: domain-security
  name: Grafana Tempo Domain Security
  slug: grafana-tempo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Grafana Tempo Trust Center
  slug: grafana-tempo-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: grafana-tempo
tags:
- Distributed Tracing
- Grafana
- Microservices
- Observability
- Open-Source
website: https://grafana.com/oss/tempo/
---
