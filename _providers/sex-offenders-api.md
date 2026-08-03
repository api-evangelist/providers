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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sex Offenders Api Agentic Access
  operation_count: 1
  slug: sex-offenders-api-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: Sex Offenders API Definition. The Sex Offenders API lets you request registered sex offenders across the US by name or zip code (Disclaimer).
  name: Sex Offenders API
  slug: sex-offenders-api
- description: The Sex Offenders API from Sex Offenders API — 1 operation(s) for sex offenders.
  name: Sex Offenders API Sex Offenders API
  slug: sex-offenders-api-sex-offenders-api
artifact_total: 9
collections:
- collection_type: open
  name: Crimeometer Sex Offenders API
  slug: open-sex-offenders-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sex-offenders-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sex-offenders-api-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sex-offenders-api-authentication.yml
created: '2024-11-13'
description: Sex Offenders API Definition. The Sex Offenders API lets you request registered sex offenders across the US by name or zip code (Disclaimer).
finops:
- name: Sex Offenders Api Finops
  service_category: API
  slug: sex-offenders-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sex-offenders-api.png
layout: provider
modified: '2026-03-16'
name: Sex Offenders API
nav: Providers
network: true
overview: 'Sex Offenders API publishes 1 API on the [APIs.io](https://apis.io/) network: Sex Offenders API. Tagged areas include Sex Offenders.


  Sex Offenders API''s developer surface includes authentication and 2 more developer resources.'
plans:
- name: Sex Offenders Api Plans Pricing
  plan_count: 3
  slug: sex-offenders-api-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 5
  name: Sex Offenders Api Rate Limits
  slug: sex-offenders-api-rate-limits
score:
  band: thin
  composite: 31.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.3
    developer_ergonomics: 10.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 31.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sex-offenders-api/refs/heads/main/screenshots/sex-offenders-api-2026-06-20T193740.png
security:
- kind: authentication
  name: Sex Offenders Api Authentication
  slug: sex-offenders-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sex Offenders Api Domain Security
  slug: sex-offenders-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sex-offenders-api
tags:
- Sex Offenders
---
