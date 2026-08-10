---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Victoriametrics Agentic Access
  operation_count: 25
  slug: victoriametrics-agentic-access
  summary_line: 25 operations · 13 acting
api_count: 9
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
- description: Administrative operations
  name: VictoriaMetrics Admin API
  slug: victoriametrics-admin-api
- description: Raw sample export endpoints
  name: VictoriaMetrics Export API
  slug: victoriametrics-export-api
- description: Data ingestion endpoints
  name: VictoriaMetrics Import API
  slug: victoriametrics-import-api
- description: Prometheus-compatible query endpoints (PromQL / MetricsQL)
  name: VictoriaMetrics Query API
  slug: victoriametrics-query-api
- description: Endpoints compatible with other monitoring formats
  name: VictoriaMetrics Third-Party API
  slug: victoriametrics-third-party-api
artifact_total: 18
collections:
- collection_type: open
  name: VictoriaMetrics HTTP API
  slug: open-victoriametrics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/victoriametrics-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/victoriametrics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/victoriametrics-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/victoriametrics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/victoriametrics-rate-limits.yml
- group: commercial
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
- name: Victoriametrics Finops
  service_category: Observability / Time-Series
  slug: victoriametrics-finops
graphqls:
- description: 'This directory contains a conceptual GraphQL schema for the VictoriaMetrics time-series database and monitoring platform. VictoriaMetrics does not natively expose a GraphQL endpoint; this schema is a '
  name: VictoriaMetrics GraphQL Schema
  slug: victoriametrics-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/victoriametrics.png
layout: provider
modified: '2026-05-08'
name: VictoriaMetrics
nav: Providers
network: true
overview: 'VictoriaMetrics publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Export API, Import API, and 2 more. Tagged areas include Database, Time-Series, Monitoring, Open Source, and Prometheus.


  VictoriaMetrics'' developer surface includes authentication, documentation, pricing, GitHub presence, engineering blog, and 9 more developer resources.'
plans:
- name: Victoriametrics Plans Pricing
  plan_count: 4
  slug: victoriametrics-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Victoriametrics Rate Limits
  slug: victoriametrics-rate-limits
score:
  band: thin
  composite: 40.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 57.4
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/victoriametrics/refs/heads/main/screenshots/victoriametrics-2026-06-20T201019.png
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
  summary_line: disclosure policy published
slug: victoriametrics
tags:
- Database
- Time-Series
- Monitoring
- Open Source
- Prometheus
- PromQL
- MetricsQL
- Observability
website: https://victoriametrics.com/
---
