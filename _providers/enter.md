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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/enter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.enter.de/
- group: company
  title: ''
  type: Blog
  url: https://www.enter.de/blog
- group: operate
  title: ''
  type: Support
  url: https://www.enter.de/kundenservice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enter.de/waermepumpe-agb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enter.de/datenschutz
created: '2026-07-17'
description: Enter is a Berlin-based residential energy-efficiency company that positions itself as Germany's largest energy advisor, combining on-site building analysis with installation of heat pumps, photovoltaic (solar) systems, battery storage, EV wallboxes, and home energy-management systems. It guides homeowners through energy consulting, subsidy (Foerderung) applications, and financing, and reports 37,000+ completed projects and 150M+ EUR in secured subsidies. Enter is a B2C service provider with no public developer API, documentation portal, or SDKs; it was surfaced as a VC-portfolio lead and added to the API Evangelist network as a stub for enrichment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/enter.png
layout: provider
modified: '2026-07-19'
name: Enter
nav: Providers
network: true
overview: 'Enter is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Cleantech, Energy Efficiency, and Heat Pumps.


  Enter''s developer surface includes engineering blog, support, and 4 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.6
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 10.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/enter/refs/heads/main/screenshots/enter-2026-07-25T213426.png
security:
- kind: domain-security
  name: Enter Domain Security
  slug: enter-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: enter
tags:
- Company
- Energy
- Cleantech
- Energy Efficiency
- Heat Pumps
- Solar
- Building Renovation
- Germany
- Consumer
website: https://www.enter.de/
---
