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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: As directed by the OPEN (Open, Public, Electronic, and Necessary) Government Data Act and through its commitment to United States agriculturalists and interested public, FSA provides numerous data res
  name: Farm Service Agency
  slug: farm-service-agency
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/farm-service-agency-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda-farm-service-agency
created: '2024-12-03'
description: As directed by the OPEN (Open, Public, Electronic, and Necessary) Government Data Act and through its commitment to United States agriculturalists and interested public, FSA provides numerous data resources through reports, visualizations, and other formats.
finops:
- name: Farm Service Agency Finops
  service_category: API
  slug: farm-service-agency-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/farm-service-agency.png
layout: provider
modified: '2026-04-28'
name: Farm Service Agency
nav: Providers
network: true
overview: Farm Service Agency publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Agriculture and Federal-Government.
plans:
- name: Farm Service Agency Plans Pricing
  plan_count: 3
  slug: farm-service-agency-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Farm Service Agency Rate Limits
  slug: farm-service-agency-rate-limits
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
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 9.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/farm-service-agency/refs/heads/main/screenshots/farm-service-agency-2026-06-20T181041.png
security:
- kind: domain-security
  name: Farm Service Agency Domain Security
  slug: farm-service-agency-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: farm-service-agency
tags:
- Agriculture
- Federal-Government
---
