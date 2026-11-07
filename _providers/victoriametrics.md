---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Victoriametrics Agentic Access
  operation_count: 25
  slug: victoriametrics-agentic-access
  summary_line: 25 operations · 12 acting
api_count: 1
apis:
- description: Prometheus-compatible HTTP API for instant and range queries (PromQL / MetricsQL), label discovery, series search, metadata and TSDB status. Single-node default port 8428; in cluster mode served by vm
  name: VictoriaMetrics Prometheus-Compatible Query API
  slug: prometheus-query
- description: Multi-protocol ingestion — Prometheus remote-write (/api/v1/write), InfluxDB line protocol (/write or /insert/0/influx/write), DataDog v1 (/datadog/api/v1/series) and v2 (/datadog/api/v2/series), Grap
  name: VictoriaMetrics Ingestion APIs
  slug: ingestion
- description: Administrative endpoints for time-series deletion (/api/v1/admin/tsdb/ delete_series), data export/import (/api/v1/export, /api/v1/import in various formats), Prometheus federation (/federate), TSDB s
  name: VictoriaMetrics Admin / Federation API
  slug: admin
- description: Enterprise-only ML-driven anomaly detection. Reads via Prometheus query API, writes anomaly scores back via Prometheus remote-write. Multivariate models, confidence intervals and HA deployment support
  name: VictoriaMetrics Anomaly Detection (vmanomaly)
  slug: vmanomaly
- baseURL: http://<host>:8428
  baseurl_source: declared
  description: Administrative operations
  name: VictoriaMetrics Admin API
  slug: victoriametrics-admin-api
- baseURL: http://<host>:8428
  baseurl_source: declared
  description: Raw sample export endpoints
  name: VictoriaMetrics Export API
  slug: victoriametrics-export-api
- baseURL: http://<host>:8428
  baseurl_source: declared
  description: Data ingestion endpoints
  name: VictoriaMetrics Import API
  slug: victoriametrics-import-api
- baseURL: http://<host>:8428
  baseurl_source: declared
  description: Prometheus-compatible query endpoints (PromQL / MetricsQL)
  name: VictoriaMetrics Query API
  slug: victoriametrics-query-api
- baseURL: http://<host>:8428
  baseurl_source: declared
  description: Endpoints compatible with other monitoring formats
  name: VictoriaMetrics Third-Party API
  slug: victoriametrics-third-party-api
artifact_total: 23
collections:
- collection_type: open
  name: VictoriaMetrics HTTP Admin API
  slug: open-victoriametrics-admin-api
- collection_type: open
  name: VictoriaMetrics HTTP Admin Export API
  slug: open-victoriametrics-export-api
- collection_type: open
  name: VictoriaMetrics HTTP Admin Import API
  slug: open-victoriametrics-import-api
- collection_type: open
  name: VictoriaMetrics HTTP Admin Query API
  slug: open-victoriametrics-query-api
- collection_type: open
  name: VictoriaMetrics HTTP Admin Third-Party API
  slug: open-victoriametrics-third-party-api
- collection_type: open
  name: VictoriaMetrics HTTP API
  slug: open-victoriametrics
common:
- group: other
  href: https://artifacts.apis.io/victoriametrics/capabilities/victoriametrics-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/victoriametrics-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/victoriametrics/agentic-access/victoriametrics-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/victoriametrics-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/victoriametrics/security/victoriametrics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/victoriametrics-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/victoriametrics/security/victoriametrics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/victoriametrics-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/victoriametrics/authentication/victoriametrics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/victoriametrics-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/victoriametrics
- group: company
  title: ''
  type: Website
  url: https://victoriametrics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.victoriametrics.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://victoriametrics.com/products/enterprise/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/VictoriaMetrics/VictoriaMetrics
- group: start
  title: ''
  type: EnterpriseTrial
  url: https://victoriametrics.com/products/enterprise/trial/
- group: commercial
  href: https://artifacts.apis.io/victoriametrics/plans/victoriametrics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/victoriametrics-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/victoriametrics/rate-limits/victoriametrics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/victoriametrics-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/victoriametrics/finops/victoriametrics-finops.yml
  title: ''
  type: FinOps
  url: finops/victoriametrics-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://victoriametrics.com/index.xml
created: '2026-05-08'
description: VictoriaMetrics is a fast open-source time-series database and monitoring solution. It exposes a Prometheus-compatible HTTP query API, a wide range of ingestion endpoints (Prometheus remote-write, InfluxDB Line Protocol, DataDog v1/v2, Graphite, OpenTSDB, CSV, JSON, native), a federation endpoint and admin endpoints. The commercial Enterprise edition adds anomaly detection (vmanomaly), downsampling, multi-tenancy and other features.
finops:
- has_sources: true
  method: generated
  name: Victoriametrics Finops
  primary_unit: ingestion-rate / active-series
  service_category: Observability / Time-Series
  slug: victoriametrics-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/victoriametrics.png
layout: provider
modified: '2026-05-08'
name: VictoriaMetrics
nav: Providers
network: true
overview: 'VictoriaMetrics publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Admin API, Export API, Import API, and 6 more. Tagged areas include Database, Time Series, Monitoring, Open Source, and Prometheus.


  The VictoriaMetrics catalog on APIs.io includes 1 Spectral governance ruleset.


  VictoriaMetrics'' developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Victoriametrics Plans Pricing
  plan_count: 4
  slug: victoriametrics-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Victoriametrics Rate Limits
  slug: victoriametrics-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: VictoriaMetrics API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: victoriametrics-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    contract_governance: 13.6
    contract_quality: 40.4
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 23.7
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/victoriametrics/victoriametrics-2026-06-20T201019.png
security:
- kind: authentication
  name: Victoriametrics Authentication
  slug: victoriametrics-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Victoriametrics Domain Security
  slug: victoriametrics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Victoriametrics Vulnerability Disclosure
  slug: victoriametrics-vulnerability-disclosure
  summary_line: no policy recorded
slug: victoriametrics
tags:
- Database
- Time Series
- Monitoring
- Open Source
- Prometheus
- PromQL
- MetricsQL
- Observability
website: https://victoriametrics.com/
---
