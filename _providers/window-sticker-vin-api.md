---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-09-23'
api_count: 1
apis:
- baseURL: https://windowsticker.org
  baseurl_source: declared
  description: 'Keyless REST/JSON API for VIN decoding and factory window sticker (Monroney label) PDF lookup. Endpoints: GET /api/v1/vin/{vin} and GET /api/sticker/{vin}.'
  name: Window Sticker VIN API
  slug: window-sticker-vin-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://windowsticker.org/
- group: docs
  title: ''
  type: Documentation
  url: https://windowsticker.org/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://windowsticker.org/api-docs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://windowsticker.org/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://windowsticker.org/status
- group: agent
  title: ''
  type: LLMsTxt
  url: https://windowsticker.org/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/well-known/window-sticker-vin-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/window-sticker-vin-api-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/authentication/window-sticker-vin-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/window-sticker-vin-api-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/conventions/window-sticker-vin-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/window-sticker-vin-api-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/lifecycle/window-sticker-vin-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/window-sticker-vin-api-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/conformance/window-sticker-vin-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/window-sticker-vin-api-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/security/window-sticker-vin-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/window-sticker-vin-api-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/rate-limits/window-sticker-vin-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/window-sticker-vin-api-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/window-sticker-vin-api/refs/heads/main/plans/window-sticker-vin-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/window-sticker-vin-api-plans-pricing.yml
created: '2026-09-19'
description: A free, keyless VIN-lookup service that returns the original factory window sticker (Monroney label) PDF plus an NHTSA vPIC specification decode for any 17-character US VIN. Serves decoded vehicle specs, EPA fuel economy, crash ratings, and recalls over an open, CORS-enabled JSON API with no registration, no API key and no paid tiers. Factory PDFs are available for 16 makes (Ford, GM, Stellantis, Subaru, Kia, Hyundai, Genesis and more); every other make still returns a full specification decode.
image: https://windowsticker.org/og.png
layout: provider
modified: '2026-09-20'
name: Window Sticker VIN API
nav: Providers
network: true
overview: 'Window Sticker VIN API publishes 1 API on the [APIs.io](https://apis.io/) network: Window Sticker VIN API. Tagged areas include Automotive, Vehicle Data, VIN Decoding, Monroney, and Window sticker.


  Window Sticker VIN API''s developer surface includes documentation, API reference, authentication, and 12 more developer resources.'
plans:
- name: Window Sticker Vin Api Plans Pricing
  plan_count: 0
  slug: window-sticker-vin-api-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Window Sticker Vin Api Rate Limits
  slug: window-sticker-vin-api-rate-limits
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 45.6
    developer_ergonomics: 30.4
    discoverability: 70.4
    operational_transparency: 15.8
  previous_composite: 31.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Window Sticker Vin Api Authentication
  slug: window-sticker-vin-api-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Window Sticker Vin Api Domain Security
  slug: window-sticker-vin-api-domain-security
  summary_line: TLSv1.3 · HSTS
slug: window-sticker-vin-api
tags:
- Automotive
- Vehicle Data
- VIN Decoding
- Monroney
- Window sticker
- Government open data
- Auto Retail
- Dealer tooling
website: https://windowsticker.org/
---
