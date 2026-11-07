---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
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
  href: https://artifacts.apis.io/pwsweather/hosts/pwsweather-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pwsweather-hosts.yml
- group: other
  href: https://artifacts.apis.io/pwsweather/vendors/pwsweather-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pwsweather-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pwsweather.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pwsweather.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.pwsweather.com/login/
- group: auth
  href: https://artifacts.apis.io/pwsweather/security/pwsweather-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pwsweather-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pwsweather.com/
coverage:
  checked: '2026-10-29'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was found on any discovered host.
  evidence:
  - status: 404
    url: https://api.pwsweather.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: PWSweather provides a web platform that visualizes real‑time weather observations from personal weather stations, offering interactive maps, graphs, and forecasts. The site displays temperature, humidity, dew point, and radar views for stations worldwide, allowing users to explore current conditions and historical trends. While the public site showcases weather data, no public API documentation is currently available.
image: https://www.pwsweather.com/static/cc289db345f53bba0c86a03b370ff946/59860/18c7d4da-c63e-4b9c-9dc6-3174a9a722f5_pws-feat-graphics.png
layout: provider
modified: '2026-10-28'
name: PWSweather
nav: Providers
network: true
overview: PWSweather is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Weather, Data, Visualization, and Platform.
plans:
- name: Pwsweather Plans Pricing
  plan_count: 0
  slug: pwsweather-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Pwsweather Rate Limits
  slug: pwsweather-rate-limits
scopes:
- name: Pwsweather Scopes
  scope_count: 0
  slug: pwsweather-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.9
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
screenshot: https://apis.io/screenshots/pwsweather/pwsweather-2026-11-03T141734.png
security:
- kind: authentication
  name: Pwsweather Authentication
  slug: pwsweather-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pwsweather Domain Security
  slug: pwsweather-domain-security
  summary_line: TLSv1.3
slug: pwsweather
tags:
- Company
- Weather
- Data
- Visualization
- Platform
website: https://pwsweather.com/
---
