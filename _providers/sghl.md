---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/sghl/hosts/sghl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sghl-hosts.yml
- group: auth
  href: https://artifacts.apis.io/sghl/security/sghl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sghl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sghl.com.au/
- group: operate
  title: ''
  type: Contact
  url: https://sghl.com.au/contact
- group: company
  title: ''
  type: InvestorRelations
  url: https://sghl.com.au/investor-centre/introduction
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sghl.com.au/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sghl.com.au/terms
created: '2026-10-22'
description: 'SGH Ltd (ASX:SGH) is an Australian diversified operating company with market-leading businesses across industrial services, energy and media. In industrial services it owns WesTrac (the sole authorised Caterpillar dealer in WA and NSW/ACT), Boral (construction materials), Coates (equipment hire) and Allight (mobile lighting and power); in energy it wholly owns SGH Energy and holds 30.0% of Beach Energy; in media it holds 20.1% of Southern Cross Media. Its corporate site sghl.com.au publishes no developer portal, API documentation or public API. Surfaced via the API Evangelist harvest backlog (source: australia-apidays-2026).'
image: https://sghl.com.au/apple-touch-icon.png
layout: provider
modified: '2026-10-22'
name: SGH Ltd
nav: Providers
network: true
overview: SGH Ltd is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Australia, Industrial Services, Energy, and Construction Materials.
plans:
- name: Sghl Plans Pricing
  plan_count: 0
  slug: sghl-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Sghl Rate Limits
  slug: sghl-rate-limits
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 8.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sghl/sghl-2026-11-03T143101.png
security:
- kind: domain-security
  name: Sghl Domain Security
  slug: sghl-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sghl
tags:
- Company
- Australia
- Industrial Services
- Energy
- Construction Materials
- Equipment Hire
- Media
- ASX Listed
website: https://sghl.com.au/
---
