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
  href: https://artifacts.apis.io/ampol/hosts/ampol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ampol-hosts.yml
- group: other
  href: https://artifacts.apis.io/ampol/vendors/ampol-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ampol-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ampol/security/ampol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ampol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ampol.com.au/
- group: operate
  title: ''
  type: Support
  url: https://www.ampol.com.au/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ampol.com.au/business/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.ampol.com.au/about-ampol/news-and-media
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ampol.com.au/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ampol.com.au/privacy-policy
created: '2026-10-21'
description: 'Ampol is an Australian transport fuels and convenience retailer, operating since 1900, that describes itself as Australia''s leader in transport fuels. Its network of service stations supplies petrol and diesel, AmpCharge EV charging, AmpolCard fuel cards and business solutions, wholesale fuel with published terminal gate pricing, Foodary convenience food, everyday rewards and Mobil lubricants. Surfaced via the API Evangelist harvest backlog (source: australia-apidays-2026).'
image: https://www.ampol.com.au/stardust/logos/ampol_nav_logo.svg
layout: provider
modified: '2026-10-21'
name: Ampol
nav: Providers
network: true
overview: 'Ampol is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Fuel, Retail, and EV Charging.


  Ampol''s developer surface includes support, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Ampol Plans Pricing
  plan_count: 0
  slug: ampol-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Ampol Rate Limits
  slug: ampol-rate-limits
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 12
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
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
  previous_composite: 12.3
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
screenshot: https://apis.io/screenshots/ampol/ampol-2026-11-03T120823.png
security:
- kind: domain-security
  name: Ampol Domain Security
  slug: ampol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ampol
tags:
- Company
- Energy
- Fuel
- Retail
- EV Charging
- Fuel Cards
- Australia
website: https://www.ampol.com.au/
---
