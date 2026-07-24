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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Loki Agentic Access
  operation_count: 27
  slug: loki-agentic-access
  summary_line: 27 operations · 8 acting
api_count: 5
apis:
- description: The Config API from Loki — 1 operation(s) for config.
  name: Loki Config API
  slug: loki-config-api
- description: The Loki API from Loki — 17 operation(s) for loki.
  name: Loki Loki API
  slug: loki-loki-api
- description: The Metrics API from Loki — 1 operation(s) for metrics.
  name: Loki Metrics API
  slug: loki-metrics-api
- description: The Otlp API from Loki — 1 operation(s) for otlp.
  name: Loki Otlp API
  slug: loki-otlp-api
- description: The Ready API from Loki — 1 operation(s) for ready.
  name: Loki Ready API
  slug: loki-ready-api
artifact_total: 12
collections:
- collection_type: open
  name: Loki HTTP API
  slug: open-loki
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loki-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/loki-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loki-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://grafana.com/oss/loki/
- group: docs
  title: ''
  type: Documentation
  url: https://grafana.com/docs/loki/latest/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/grafana
- group: company
  title: ''
  type: Blog
  url: https://grafana.com/blog/index.xml
created: '2026-03-25'
description: Loki is an open source log aggregation system from Grafana Labs designed to store and query logs efficiently using labels instead of full-text indexing.
finops:
- name: Loki Finops
  service_category: API
  slug: loki-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loki.png
layout: provider
modified: '2026-05-19'
name: Loki
nav: Providers
network: true
overview: 'Loki publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Config API, Loki API, Metrics API, and 2 more. Tagged areas include Logging, Observability, Open Source, and Grafana.


  Loki''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Loki Plans Pricing
  plan_count: 3
  slug: loki-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 5
  name: Loki Rate Limits
  slug: loki-rate-limits
score:
  band: thin
  composite: 30.4
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 38.9
    developer_ergonomics: 10.9
    discoverability: 42.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 30.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loki/refs/heads/main/screenshots/loki-2026-06-20T184708.png
security:
- kind: domain-security
  name: Loki Domain Security
  slug: loki-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Loki Trust Center
  slug: loki-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, FedRAMP, GDPR, CSA STAR
slug: loki
tags:
- Logging
- Observability
- Open Source
- Grafana
website: https://grafana.com/oss/loki/
---
