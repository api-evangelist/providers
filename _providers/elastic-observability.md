---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Elastic Observability Agentic Access
  operation_count: 8
  slug: elastic-observability-agentic-access
  summary_line: 8 operations · 5 acting
api_count: 5
apis:
- description: Elastic Observability provides unified logs, metrics, traces, and AI-driven anomaly detection built on the Elastic Stack.
  name: Elastic Observability
  slug: elastic-observability
- description: The Agent Configuration API from Elastic Observability — 2 operation(s) for agent configuration.
  name: Elastic Observability Agent Configuration API
  slug: elastic-observability-agent-configuration-api
- description: The Intake API from Elastic Observability — 2 operation(s) for intake.
  name: Elastic Observability Intake API
  slug: elastic-observability-intake-api
- description: The OpenTelemetry API from Elastic Observability — 3 operation(s) for opentelemetry.
  name: Elastic Observability OpenTelemetry API
  slug: elastic-observability-opentelemetry-api
- description: The Server Info API from Elastic Observability — 1 operation(s) for server info.
  name: Elastic Observability Server Info API
  slug: elastic-observability-server-info-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Elastic Observability (APM Server) Agent Configuration API
  slug: open-elastic-observability-agent-configuration-api
- collection_type: open
  name: Elastic Observability (APM Server) Agent Configuration Intake API
  slug: open-elastic-observability-intake-api
- collection_type: open
  name: Elastic Observability (APM Server) Agent Configuration OpenTelemetry API
  slug: open-elastic-observability-opentelemetry-api
- collection_type: open
  name: Elastic Observability (APM Server) Agent Configuration Server Info API
  slug: open-elastic-observability-server-info-api
- collection_type: open
  name: Elastic Observability (APM Server) API
  slug: open-elastic-observability
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elastic-observability-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/elastic-observability-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elastic-observability-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elastic-observability-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.elastic.co/observability
- group: docs
  title: ''
  type: Documentation
  url: https://www.elastic.co/guide/en/observability/current/index.html
created: '2026-03-27'
description: Elastic Observability provides unified logs, metrics, traces, and AI-driven anomaly detection built on the Elastic Stack.
finops:
- name: Elastic Observability Finops
  service_category: API
  slug: elastic-observability-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elastic-observability.png
layout: provider
modified: '2026-03-27'
name: Elastic Observability
nav: Providers
network: true
overview: 'Elastic Observability publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Agent Configuration API, Intake API, OpenTelemetry API, and 1 more. Tagged areas include AIOps and Observability.


  Elastic Observability''s developer surface includes authentication, documentation, and 4 more developer resources.'
plans:
- name: Elastic Observability Plans Pricing
  plan_count: 3
  slug: elastic-observability-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Elastic Observability Rate Limits
  slug: elastic-observability-rate-limits
score:
  band: thin
  composite: 27.2
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 50.0
    developer_ergonomics: 21.4
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 27.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elastic-observability/refs/heads/main/screenshots/elastic-observability-2026-06-20T180529.png
security:
- kind: authentication
  name: Elastic Observability Authentication
  slug: elastic-observability-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Elastic Observability Domain Security
  slug: elastic-observability-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Elastic Observability Trust Center
  slug: elastic-observability-trust-center
  summary_line: GDPR
slug: elastic-observability
tags:
- AIOps
- Observability
website: https://www.elastic.co/observability
---
