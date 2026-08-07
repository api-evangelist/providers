---
access_model:
  confidence: medium
  label: Freemium · Requires approval
  onboarding: approval
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maestro-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/maestro-pms
- group: other
  title: ''
  type: ProductPage
  url: https://maestropms.com
created: '2025-02-21'
description: Maestro PMS is an all-in-one property management software solution serving independent hotels, resorts, and multi-property groups. The platform advertises open APIs that support more than 800 third-party integrations, but does not publish public OpenAPI documentation; integrations are arranged through the partner program.
finops:
- name: Maestro Finops
  service_category: API
  slug: maestro-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maestro.png
layout: provider
modified: '2026-07-25'
name: Maestro PMS
nav: Providers
network: true
overview: Maestro PMS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Property Management, Hospitality, Hotels, PMS, and Resorts.
plans:
- name: Maestro Plans Pricing
  plan_count: 3
  slug: maestro-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 5
  name: Maestro Rate Limits
  slug: maestro-rate-limits
score:
  band: emerging
  composite: 17.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 17.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/maestro/refs/heads/main/screenshots/maestro-2026-06-20T184834.png
security:
- kind: domain-security
  name: Maestro Domain Security
  slug: maestro-domain-security
  summary_line: TLSv1.3 · DMARC
slug: maestro
tags:
- Property Management
- Hospitality
- Hotels
- PMS
- Resorts
---
