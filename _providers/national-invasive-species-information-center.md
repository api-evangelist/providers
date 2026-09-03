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
- description: The NISIC gateway to invasive species information covers federal, state, local, and international sources on plants, animals, and pathogens that are non-native to ecosystems and whose introduction cau
  name: National Invasive Species Information Center
  slug: national-invasive-species-information-center
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-invasive-species-information-center-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.invasivespeciesinfo.gov/
created: '2024-12-03'
description: National Invasive Species Information Center (NISIC) is the gateway to invasive species information covering federal, state, local, and international sources. Invasive species are plants, animals, or pathogens that are non-native to the ecosystem under consideration, and whose introduction causes or is likely to cause harm.
finops:
- name: National Invasive Species Information Center Finops
  service_category: API
  slug: national-invasive-species-information-center-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-invasive-species-information-center.png
layout: provider
modified: '2026-04-28'
name: National Invasive Species Information Center
nav: Providers
network: true
overview: National Invasive Species Information Center publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Environment, Federal-Government, and Invasive Species.
plans:
- name: National Invasive Species Information Center Plans Pricing
  plan_count: 3
  slug: national-invasive-species-information-center-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: National Invasive Species Information Center Rate Limits
  slug: national-invasive-species-information-center-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/national-invasive-species-information-center/refs/heads/main/screenshots/national-invasive-species-information-center-2026-06-20T190030.png
security:
- kind: domain-security
  name: National Invasive Species Information Center Domain Security
  slug: national-invasive-species-information-center-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: national-invasive-species-information-center
tags:
- Environment
- Federal-Government
- Invasive Species
website: https://www.invasivespeciesinfo.gov/
---
