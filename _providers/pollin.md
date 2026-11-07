---
access_model:
  confidence: low
  label: Enterprise · Open access
  onboarding: open
  pricing: enterprise
  public: true
  source:
  - authentication
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
artifact_total: 5
common:
- group: other
  href: https://artifacts.apis.io/pollin/hosts/pollin-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pollin-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://www.pollin.de/account/login
- group: auth
  href: https://artifacts.apis.io/pollin/security/pollin-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pollin-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.pollin.de/
- group: company
  title: ''
  type: Impressum
  url: https://www.pollin.de/impressum
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pollin.de/datenschutz-und-sicherheit
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pollin.de/agb
- group: operate
  title: ''
  type: Support
  url: https://www.pollin.de/kontakt-service
coverage:
  checked: '2026-10-28'
  detail: No public API documentation or machine‑readable specification was found on the website or any discovered subdomains.
  evidence:
  - status: 404
    url: https://www.pollin.de/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Pollin Electronic GmbH is a German online retailer specializing in consumer electronics, offering a broad selection of products ranging from audio equipment to computer components. The company focuses on providing discounted prices and frequent promotions, serving customers across Germany and neighboring markets through its e‑commerce platform.
image: https://www.pollin.de/media/6b/1c/a9/1704269404/pollin-logoNEW.svg?ts=1704269406
layout: provider
modified: '2026-10-28'
name: Pollin Electronic
nav: Providers
network: true
overview: 'Pollin Electronic is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electronics, Retail, E-Commerce, and Germany.


  Pollin Electronic''s developer surface includes support and 7 more developer resources.'
plans:
- name: Pollin Plans Pricing
  plan_count: 0
  slug: pollin-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Pollin Rate Limits
  slug: pollin-rate-limits
scopes:
- name: Pollin Scopes
  scope_count: 0
  slug: pollin-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 13.9
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/pollin/pollin-2026-11-03T141350.png
security:
- kind: authentication
  name: Pollin Authentication
  slug: pollin-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pollin Domain Security
  slug: pollin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pollin
tags:
- Company
- Electronics
- Retail
- E-Commerce
- Germany
website: https://www.pollin.de/
---
