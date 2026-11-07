---
access_model:
  confidence: low
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: true
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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Brickway API for managing collections and builds
  name: Brickway API
  slug: brickway-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/brickway-app/plans/brickway-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brickway-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/brickway-app/conformance/brickway-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brickway-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/brickway-app/well-known/brickway-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brickway-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/brickway-app/hosts/brickway-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brickway-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/brickway-app/vendors/brickway-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/brickway-app-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brickway.app/privacy/
- group: start
  title: ''
  type: Login
  url: https://app.brickway.app/login/
- group: auth
  href: https://artifacts.apis.io/brickway-app/security/brickway-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brickway-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brickway.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://brickway.app/pricing/
- group: company
  title: ''
  type: About
  url: https://brickway.app/about/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.brickway.app/openapi.json
  - status: 401
    url: https://api.brickway.app/mcp
  - status: 200
    url: https://brickway.app/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: Brickway provides a LEGO® and alt‑brick collection and build tracker app. Users can track sets from wish‑list to built, monitor minifig counts, scan sealed boxes, and share collections with family. The service offers a 14‑day free trial and a subscription for full features, supporting iOS, Android, and web platforms.
layout: provider
modified: '2026-11-03'
name: Brickway
nav: Providers
network: true
overview: 'Brickway is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, LEGO, Collection, Tracker, and Mobile App.


  Brickway''s developer surface includes pricing and 10 more developer resources.'
plans:
- name: Brickway App Plans Pricing
  plan_count: 4
  slug: brickway-app-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 47.0
    catalog_earned_first_party: 12.0
    catalog_gap: 68.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brickway App Domain Security
  slug: brickway-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brickway-app
tags:
- Company
- LEGO
- Collection
- Tracker
- Mobile App
website: https://brickway.app/
---
