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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-03'
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
random_paper: 7
rate_limits:
- limit_count: 5
  name: Maestro Rate Limits
  slug: maestro-rate-limits
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 9.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
