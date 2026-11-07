---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP JSON-RPC API for AI assistants to manage trips, tools, and data.
  name: Aitrips AI MCP
  slug: aitrips-ai-mcp
artifact_total: 5
common:
- group: operate
  href: https://artifacts.apis.io/aitrips-io/rate-limits/aitrips-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aitrips-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aitrips-io/plans/aitrips-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aitrips-io-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/aitrips-io/authentication/aitrips-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aitrips-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/aitrips-io/conformance/aitrips-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aitrips-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aitrips-io/well-known/aitrips-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aitrips-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/aitrips-io/hosts/aitrips-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aitrips-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/aitrips-io/vendors/aitrips-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aitrips-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.aitrips.io/sign-in
- group: auth
  href: https://artifacts.apis.io/aitrips-io/security/aitrips-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aitrips-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aitrips.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.aitrips.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.aitrips.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.aitrips.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aitrips.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aitrips.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aitrips.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aitrips.io/privacy
coverage:
  checked: '2026-11-01'
  detail: API endpoints require authentication (OAuth or API key) and return 401/405 when accessed without credentials.
  evidence:
  - status: 405
    url: https://www.aitrips.io/api/ai/mcp
  reason: auth-required
  state: gated
created: '2026-11-01'
description: Aitrips.io provides a map-first trip planning platform that lets users plan journeys across eleven transport modes, view weather for each activity, and share itineraries. The service offers a web app and an AI integration via MCP for personalized travel planning.
image: https://www.aitrips.io/favicon.ico
layout: provider
modified: '2026-11-01'
name: Aitrips.io
nav: Providers
network: true
overview: 'Aitrips.io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Mapping, Trip Planning, Artificial Intelligence, and Transportation.


  Aitrips.io''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 12 more developer resources.'
plans:
- name: Aitrips Io Plans Pricing
  plan_count: 2
  slug: aitrips-io-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 2
  name: Aitrips Io Rate Limits
  slug: aitrips-io-rate-limits
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 53.0
    catalog_earned_first_party: 16.0
    catalog_gap: 62.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 35.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aitrips Io Authentication
  slug: aitrips-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aitrips Io Domain Security
  slug: aitrips-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aitrips-io
tags:
- Travel
- Mapping
- Trip Planning
- Artificial Intelligence
- Transportation
- Weather
website: https://aitrips.io/
---
