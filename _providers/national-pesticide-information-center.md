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
api_count: 1
apis:
- description: NPIC provides objective, science-based information about pesticides and pesticide-related topics to enable people to make informed decisions. NPIC does not currently publish a public web API; data and
  name: National Pesticide Information Center
  slug: national-pesticide-information-center
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-pesticide-information-center-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-pesticide-information-center
- group: company
  title: ''
  type: Website
  url: https://npic.orst.edu/
- group: operate
  title: ''
  type: Contact
  url: https://npic.orst.edu/contact.html
created: '2024-12-03'
description: The National Pesticide Information Center (NPIC) provides objective, science-based information about pesticides and their potential health and environmental effects. NPIC is a cooperative agreement between Oregon State University and the U.S. Environmental Protection Agency, serving the general public, health professionals, and pesticide manufacturers.
finops:
- name: National Pesticide Information Center Finops
  service_category: API
  slug: national-pesticide-information-center-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-pesticide-information-center.png
layout: provider
modified: '2026-04-28'
name: National Pesticide Information Center
nav: Providers
network: true
overview: National Pesticide Information Center publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Environment, Federal-Government, Pesticides, and Public Health.
plans:
- name: National Pesticide Information Center Plans Pricing
  plan_count: 3
  slug: national-pesticide-information-center-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: National Pesticide Information Center Rate Limits
  slug: national-pesticide-information-center-rate-limits
score:
  band: minimal
  composite: 9.5
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
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-pesticide-information-center/refs/heads/main/screenshots/national-pesticide-information-center-2026-06-20T190038.png
security:
- kind: domain-security
  name: National Pesticide Information Center Domain Security
  slug: national-pesticide-information-center-domain-security
  summary_line: TLSv1.3 · DMARC
slug: national-pesticide-information-center
tags:
- Environment
- Federal-Government
- Pesticides
- Public Health
website: https://npic.orst.edu/
---
