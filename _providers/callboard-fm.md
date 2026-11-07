---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
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
- description: AI-powered concert booking brief engine
  name: Callboard API
  slug: callboard-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/callboard-fm/plans/callboard-fm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/callboard-fm-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/callboard-fm/conformance/callboard-fm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/callboard-fm-conformance.yml
- group: other
  href: https://artifacts.apis.io/callboard-fm/hosts/callboard-fm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/callboard-fm-hosts.yml
- group: other
  href: https://artifacts.apis.io/callboard-fm/vendors/callboard-fm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/callboard-fm-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.callboard.fm/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.callboard.fm/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.callboard.fm/pricing
- group: start
  title: ''
  type: Login
  url: https://www.callboard.fm/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://www.callboard.fm/docs/mcp
- group: company
  title: ''
  type: Blog
  url: https://www.callboard.fm/blog
- group: auth
  href: https://artifacts.apis.io/callboard-fm/security/callboard-fm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/callboard-fm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://callboard.fm/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.callboard.fm/openapi.json
  - status: 401
    url: https://api.callboard.fm/mcp
  - status: 200
    url: https://callboard.fm/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: Callboard.fm provides booking intelligence for independent concert promoters, offering market fit scores, venue size estimates, ticket pricing, and risk flags for artists in specific cities. Users can input an artist and city to receive a concise brief that helps assess the viability of a concert, supported by data on over 340 markets and 8 million artists. The service aims to streamline decision‑making for promoters seeking to book shows efficiently and profitably.
image: https://www.callboard.fm/opengraph-image?1cf1a0ed2e5596d7
layout: provider
modified: '2026-11-03'
name: Callboard.fm
nav: Providers
network: true
overview: 'Callboard.fm is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Concerts, Booking, Intelligence, and Promoters.


  Callboard.fm''s developer surface includes pricing, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Callboard Fm Plans Pricing
  plan_count: 4
  slug: callboard-fm-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Callboard Fm Domain Security
  slug: callboard-fm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: callboard-fm
tags:
- Music
- Concerts
- Booking
- Intelligence
- Promoters
website: https://callboard.fm/
---
