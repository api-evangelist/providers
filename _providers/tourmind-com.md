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
- description: Travel planning and booking API suite
  name: TourMind API
  slug: tourmind-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/tourmind-com/hosts/tourmind-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tourmind-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/tourmind-com/vendors/tourmind-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tourmind-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tourmind-com/security/tourmind-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tourmind-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tourmind.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tourmind.com/en-US
- group: docs
  title: ''
  type: Documentation
  url: https://tourmind.com/en-US/aboutus
- group: docs
  title: ''
  type: APIReference
  url: https://tourmind.com/en-US/skills
- group: start
  title: ''
  type: GettingStarted
  url: https://tourmind.com/en-US/introduction/resource
- group: company
  title: ''
  type: Blog
  url: https://tourmind.com/en-US/news
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/tourmind/workspace
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract was discovered on the provider's hosts.
  evidence:
  - status: 502
    url: https://api.tourmind.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: TourMind provides AI-powered travel planning and booking solutions, enabling agents and platforms to turn customer travel requests into complete itineraries with integrated flight, hotel, and ancillary services. Their platform offers a suite of APIs for AI travel skill integration, booking automation, revenue management, and white‑label solutions for travel agencies, OTAs, and super‑apps.
layout: provider
modified: '2026-10-30'
name: tourmind-com
nav: Providers
network: true
overview: 'tourmind-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Artificial Intelligence, Booking, Software-as-a-Service, and B2B.


  tourmind-com''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 6 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tourmind-com/tourmind-com-2026-11-03T144927.png
security:
- kind: domain-security
  name: Tourmind Com Domain Security
  slug: tourmind-com-domain-security
  summary_line: TLSv1.2
slug: tourmind-com
tags:
- Travel
- Artificial Intelligence
- Booking
- Software-as-a-Service
- B2B
website: https://tourmind.com/
---
