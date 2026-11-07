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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bestcarfinder-com/well-known/bestcarfinder-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bestcarfinder-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bestcarfinder-com/hosts/bestcarfinder-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bestcarfinder-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bestcarfinder-com/vendors/bestcarfinder-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bestcarfinder-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bestcarfinder.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bestcarfinder.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.bestcarfinder.com/blog
- group: auth
  href: https://artifacts.apis.io/bestcarfinder-com/security/bestcarfinder-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bestcarfinder-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bestcarfinder.com/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract found at https://api.bestcarfinder.com/openapi.json (no response).
  evidence:
  - status: 0
    url: https://api.bestcarfinder.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Best Car Finder is an online marketplace that connects private car sellers and dealers with buyers across the United States. The platform offers listings for used cars, trucks, new cars, and specialty vehicles, providing detailed search filters, price comparisons, and a free listing service for sellers. It also includes tools like car valuation, dealer contact, and a “Best Deal” scoring system to help users find the best value. The site emphasizes privacy, allowing sellers to keep contact information hidden until they choose to share it.
image: https://www.bestcarfinder.com/images/logo_1200.png
layout: provider
modified: '2026-11-02'
name: Best Car Finder
nav: Providers
network: true
overview: 'Best Car Finder is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Cars, Used Vehicles, and Automotive.


  Best Car Finder''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 6.4
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bestcarfinder Com Domain Security
  slug: bestcarfinder-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bestcarfinder-com
tags:
- Company
- Marketplace
- Cars
- Used Vehicles
- Automotive
website: https://bestcarfinder.com/
---
