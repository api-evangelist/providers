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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  schema_version: '0.2'
  score: 13.3
  scored_at: '2026-09-12'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/greenchoice-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/greenchoice-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/greenchoice-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/greenchoice-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/greenchoice-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/greenchoice-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/greenchoice-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/greenchoice-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/greenchoice-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/greenchoice-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/greenchoice-rate-limits.yml
- group: other
  title: ''
  type: X-TechRadar
  url: techradar/greenchoice-tech-radar.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/greenchoice
- group: company
  title: ''
  type: Website
  url: https://www.greenchoice.nl
- group: operate
  title: ''
  type: Support
  url: https://www.greenchoice.nl/klantenservice/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.greenchoice.nl/tarieven/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.greenchoice.nl/klantenservice/voorwaarden/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greenchoice.nl/privacy/
- group: start
  title: ''
  type: Login
  url: https://mijn.greenchoice.nl/
- group: company
  title: ''
  type: Blog
  url: https://www.greenchoice.nl/nieuws/artikelen/
created: '2025-03-01'
description: 'Greenchoice is a Dutch energy supplier focused on green electricity and gas, offering renewable energy contracts, solar panels, home batteries, heat pumps and EV charging to consumers and businesses in the Netherlands. It runs no developer programme and publishes no API: the only machine-readable contract on any Greenchoice host is the OpenID Connect discovery document behind its own customer single sign-on at sso.greenchoice.nl.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/greenchoice.png
layout: provider
modified: '2026-09-12'
name: Greenchoice
nav: Providers
network: true
overview: 'Greenchoice is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Electricity, Gas, Renewable, and Sustainability.


  Greenchoice''s developer surface includes authentication, support, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Greenchoice Plans Pricing
  plan_count: 0
  slug: greenchoice-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Greenchoice Rate Limits
  slug: greenchoice-rate-limits
scopes:
- name: Greenchoice Scopes
  scope_count: 0
  slug: greenchoice-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 25.6
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 3.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 63.5
  schema_version: 0.22.0
  scored_at: '2026-09-12'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/greenchoice/refs/heads/main/screenshots/greenchoice-2026-06-20T182358.png
security:
- kind: authentication
  name: Greenchoice Authentication
  slug: greenchoice-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Greenchoice Domain Security
  slug: greenchoice-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: greenchoice
tags:
- Energy
- Electricity
- Gas
- Renewable
- Sustainability
- Netherlands
website: https://www.greenchoice.nl
---
