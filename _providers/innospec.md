---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
api_count: 1
apis:
- description: The Innospec API provides access to platform services and data for enterprise integration and automation.
  name: Innospec API
  slug: innospec-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/innospec-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/innospec
- group: company
  title: ''
  type: Website
  url: https://www.innospec.com
created: '2026-04-19'
description: Innospec is a major US corporation and Fortune 1000 company. The Innospec API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Innospec Finops
  service_category: Specialty Chemicals (Non-API)
  slug: innospec-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/innospec.png
layout: provider
modified: '2026-04-19'
name: Innospec
nav: Providers
network: true
overview: Innospec publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Specialty Chemicals and Fuel Additives.
plans:
- name: Innospec Plans Pricing
  plan_count: 1
  slug: innospec-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Innospec Rate Limits
  slug: innospec-rate-limits
score:
  band: minimal
  composite: 8.3
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 8.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/innospec/refs/heads/main/screenshots/innospec-2026-06-20T183357.png
security:
- kind: domain-security
  name: Innospec Domain Security
  slug: innospec-domain-security
  summary_line: TLSv1.3 · DMARC
slug: innospec
tags:
- Specialty Chemicals
- Fuel Additives
website: https://www.innospec.com
---
