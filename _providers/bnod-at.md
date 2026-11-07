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
    mcp_server: documented
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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bnod-at/llms/bnod-at-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bnod-at-llms.txt
- group: agent
  href: https://artifacts.apis.io/bnod-at/well-known/bnod-at-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bnod-at-well-known.yml
- group: other
  href: https://artifacts.apis.io/bnod-at/hosts/bnod-at-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bnod-at-hosts.yml
- group: other
  href: https://artifacts.apis.io/bnod-at/vendors/bnod-at-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bnod-at-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.bnod.at/support
- group: start
  title: ''
  type: Login
  url: https://www.bnod.at/login
- group: company
  title: ''
  type: Blog
  url: https://www.bnod.at/blog
- group: auth
  href: https://artifacts.apis.io/bnod-at/security/bnod-at-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bnod-at-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bnod.at/
coverage:
  checked: '2026-11-02'
  detail: No public API documentation or machine-readable contract was found; the /api endpoint returns 404.
  evidence:
  - status: 404
    url: https://www.bnod.at/api
  reason: tenant-only
  state: none
created: '2026-11-02'
description: bnod is an online appointment scheduling platform for small businesses and service providers. It offers a simple booking page, team planning, and customer management without requiring a separate website. Users can create a profile link to embed on existing sites or social media, and customers can book appointments directly. The service is free to start, with no fixed contracts, and can be paused or deleted at any time.
image: https://www.bnod.at/og
layout: provider
modified: '2026-11-02'
name: bnod
nav: Providers
network: true
overview: 'bnod is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Scheduling, Booking, Software-as-a-Service, and Small Business.


  bnod''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bnod At Domain Security
  slug: bnod-at-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bnod-at
tags:
- Company
- Scheduling
- Booking
- Software-as-a-Service
- Small Business
website: https://bnod.at/
---
