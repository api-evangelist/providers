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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Langtrace Agentic Access
  operation_count: 5
  slug: langtrace-agentic-access
  summary_line: 5 operations · 4 acting
api_count: 3
apis:
- description: Project and API key management.
  name: Langtrace AI Projects API
  slug: langtrace-projects-api
- description: Versioned prompt storage and retrieval.
  name: Langtrace AI Prompt Registry API
  slug: langtrace-prompt-registry-api
- description: OpenTelemetry trace ingestion and retrieval.
  name: Langtrace AI Traces API
  slug: langtrace-traces-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Langtrace AI Projects API
  slug: open-langtrace-projects-api
- collection_type: open
  name: Langtrace AI Projects Prompt Registry API
  slug: open-langtrace-prompt-registry-api
- collection_type: open
  name: Langtrace AI Projects Traces API
  slug: open-langtrace-traces-api
- collection_type: open
  name: Langtrace AI API
  slug: open-langtrace
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/langtrace-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/langtrace-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/langtrace-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Scale3-Labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/langtrace
- group: company
  title: ''
  type: Website
  url: https://www.langtrace.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.langtrace.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/langtrace-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/langtrace-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/langtrace-finops.yml
created: '2026-06-20'
description: Langtrace is an open-source, OpenTelemetry-based end-to-end observability platform for LLM applications, built by Scale3 Labs. It captures real-time traces, metrics, and evaluations for popular LLMs, agent frameworks, and vector databases. Traces are ingested via an OTLP/HTTP endpoint and a REST API exposes projects, prompt registry, and trace retrieval. Available as a free self-hosted deployment or as Langtrace Cloud.
finops:
- name: Langtrace Finops
  service_category: Observability and Monitoring
  slug: langtrace-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/langtrace.png
layout: provider
modified: '2026-06-20'
name: Langtrace AI
nav: Providers
network: true
overview: 'Langtrace AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Projects API, Prompt Registry API, and Traces API. Tagged areas include AI, LLM, Observability, OpenTelemetry, and Tracing.


  Langtrace AI''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Langtrace Plans Pricing
  plan_count: 4
  slug: langtrace-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 4
  name: Langtrace Rate Limits
  slug: langtrace-rate-limits
score:
  band: thin
  composite: 38.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/langtrace/refs/heads/main/screenshots/langtrace-2026-06-20T184310.png
security:
- kind: authentication
  name: Langtrace Authentication
  slug: langtrace-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Langtrace Domain Security
  slug: langtrace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: langtrace
tags:
- AI
- LLM
- Observability
- OpenTelemetry
- Tracing
- Open Source
website: https://www.langtrace.ai
---
