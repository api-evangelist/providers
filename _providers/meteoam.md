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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Provides weather forecasts and observations for aviation and maritime operations.
  name: MeteoAM API
  slug: meteoam-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/meteoam/well-known/meteoam-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meteoam-well-known.yml
- group: other
  href: https://artifacts.apis.io/meteoam/hosts/meteoam-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meteoam-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.google.com/
- group: auth
  href: https://artifacts.apis.io/meteoam/security/meteoam-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meteoam-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meteoam.it/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meteoam.it/it/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meteoam.it/it/condizioni-utilizzo
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.meteoam.it/it/cookie-policy
- group: operate
  title: ''
  type: Contact
  url: https://www.meteoam.it/it/come-contattarci
- group: other
  title: ''
  type: MobileApp
  url: https://apps.apple.com/it/app/meteo-aeronautica/id956516781
- group: other
  title: ''
  type: MobileApp
  url: https://play.google.com/store/apps/details?id=it.meteoam.app&hl=it&gl=US&pli=1
coverage:
  checked: '2026-10-28'
  detail: Provider's documentation site requires JavaScript rendering and offers no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.meteoam.it/it/home
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Servizio Meteo AM (Meteo Aeronautica Militare) provides official Italian military aviation weather forecasts, observations, satellite data, and alerts. The service offers detailed short‑term forecasts, meteorological maps, and specialized products for aviation and maritime operations, supporting both civilian and defense users with reliable meteorological information across Italy and surrounding regions.
image: https://cm.meteoam.it/it/media/1579687923239/native/News5.png
layout: provider
modified: '2026-10-28'
name: Servizio Meteo AM
nav: Providers
network: true
overview: 'Servizio Meteo AM is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Aviation, Meteorology, and Italy.


  Servizio Meteo AM''s developer surface includes documentation and 10 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 9
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - italy
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - italy-southern-europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/meteoam/meteoam-2026-11-03T135544.png
security:
- kind: domain-security
  name: Meteoam Domain Security
  slug: meteoam-domain-security
  summary_line: TLSv1.3 · DMARC
slug: meteoam
tags:
- Company
- Weather
- Aviation
- Meteorology
- Italy
website: https://meteoam.it/
---
