---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hellohera.com/
- group: company
  title: ''
  type: Blog
  url: https://hellohera.com/guide/all
- group: operate
  title: ''
  type: Support
  url: https://hellohera.com/faq
created: '2026-07-17'
description: Hera is a Medicare-covered care-management company that pairs families with dedicated senior-care experts (called "Heroes") to coordinate healthcare for aging parents. Heroes handle Medicare/Medicaid and insurance navigation, appointment and medical coordination, pharmacy and benefits administration, and ongoing chronic-care support, with most families paying $0 out of pocket because services are covered by Original Medicare. Founded by Jenny Lee after a personal family dementia-caregiving experience, Hera augments its human care coordinators with an internal AI platform ("Juno") and is backed by Accel and Bain Capital Ventures. As of this enrichment pass Hera operates a consumer (B2C) healthcare service and publishes no public developer portal, API, or specification surface, so the technical-artifact tiers of the enrichment pipeline are not applicable.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hera.png
layout: provider
modified: '2026-07-19'
name: Hera
nav: Providers
network: true
overview: 'Hera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Healthcare, Health Tech, and Elder Care.


  Hera''s developer surface includes engineering blog, support, and 2 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hera/refs/heads/main/screenshots/hera-2026-07-25T221006.png
security:
- kind: domain-security
  name: Hera Domain Security
  slug: hera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hera
tags:
- Company
- Artificial Intelligence
- Healthcare
- Health Tech
- Elder Care
- Care Management
- Medicare
website: https://hellohera.com/
---
