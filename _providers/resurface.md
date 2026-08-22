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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 5
apis:
- description: Resurface captures complete API request and response data in real time, providing full-payload API call logging with no sampling. Security teams use it to detect threats, identify data leaks, and ensu
  name: Resurface Platform
  slug: resurface-platform
- description: Open-source Go library for logging API requests and responses to the Resurface database. Integrates with gorilla/mux and other Go HTTP frameworks.
  name: Resurface Logger for Go
  slug: resurface-logger-go
- description: eBPF-based kernel-level API call logger that captures HTTP traffic without application code changes for zero-instrumentation observability.
  name: Resurface Logger for eBPF
  slug: resurface-logger-ebpf
- description: Official Helm charts and container images for deploying the Resurface API security database on Kubernetes.
  name: Resurface Containers
  slug: resurface-containers
- description: Connector for querying Resurface API call data via Trino distributed SQL query engine.
  name: Resurface Trino Connector
  slug: resurface-trino-connector
artifact_total: 13
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/resurface-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://resurface.io
- group: docs
  title: ''
  type: Documentation
  url: https://resurface.io/docs
- group: company
  title: ''
  type: Blog
  url: https://resurface.io/blog
- group: build
  title: ''
  type: GitHub
  url: https://github.com/resurfaceio
- group: commercial
  title: ''
  type: Pricing
  url: https://resurface.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://resurface.io/support
- group: start
  title: ''
  type: Login
  url: https://resurface.io/login
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/resabordeio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/resurfacelabs
- group: other
  title: ''
  type: HelmChart
  url: https://artifacthub.io/packages/helm/resurfaceio/resurface
- group: other
  title: ''
  type: AcquiredBy
  url: https://graylog.org
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/resurface/refs/heads/main/vocabulary/resurface-vocabulary.yml
created: '2026-03-26'
description: Resurface (now Graylog API Security) is an API runtime security and observability platform that captures and analyzes complete API request and response payloads in real time. It provides full API call logging, threat detection, data leak prevention, and compliance auditing for API traffic without sampling or aggregation. Acquired by Graylog and integrated into the Graylog SIEM platform.
finops:
- name: Resurface Finops
  service_category: API
  slug: resurface-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/resurface.png
json_schemas:
- name: Resurface API Call Log
  property_count: 12
  slug: resurface-api-call-log
json_structures:
- name: Resurface Api Call Log Structure
  property_count: 0
  slug: resurface-api-call-log-structure
jsonld:
- class_count: 5
  name: Resurface Context
  property_count: 10
  slug: resurface-context
layout: provider
modified: '2026-05-02'
name: Resurface
nav: Providers
network: true
overview: 'Resurface publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Analytics, API Compliance, API Logging, API Observability, and API Security.


  The Resurface catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Resurface''s developer surface includes documentation, engineering blog, GitHub presence, pricing, support, and 8 more developer resources.'
plans:
- name: Resurface Plans Pricing
  plan_count: 3
  slug: resurface-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Resurface Rate Limits
  slug: resurface-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Resurface API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: resurface-jsonschema-spectral-rules
score:
  band: emerging
  composite: 23.6
  delta: -10.6
  facets:
    access_clarity: 22.4
    commercial_clarity: 22.4
    contract_governance: 25.0
    contract_quality: 23.9
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 13.2
  previous_composite: 34.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/resurface/refs/heads/main/screenshots/resurface-2026-06-20T193038.png
security:
- kind: domain-security
  name: Resurface Domain Security
  slug: resurface-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: resurface
tags:
- API Analytics
- API Compliance
- API Logging
- API Observability
- API Security
- Data Leak Prevention
- Runtime Security
- SIEM
- Threat Detection
website: https://resurface.io
---
