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
- description: API for Scratch Music Group services, referenced from their documentation.
  name: Scratch Music Group API
  slug: scratch-music-group-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/scratch-music-group/llms/scratch-music-group-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/scratch-music-group-llms.txt
- group: other
  href: https://artifacts.apis.io/scratch-music-group/hosts/scratch-music-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/scratch-music-group-hosts.yml
- group: other
  href: https://artifacts.apis.io/scratch-music-group/vendors/scratch-music-group-vendors.yml
  title: ''
  type: Vendors
  url: vendors/scratch-music-group-vendors.yml
- group: auth
  href: https://artifacts.apis.io/scratch-music-group/security/scratch-music-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/scratch-music-group-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scratchmusicgroup.com
- group: docs
  title: ''
  type: Documentation
  url: https://academy.scratch.com
- group: operate
  title: ''
  type: Support
  url: https://academy.scratch.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://academy.scratch.com/privacy-policy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.scratchmusicgroup.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Scratch Music Group, founded in 2002, is a leading provider of DJ bookings, education, and event services. Co‑founded by Jam Master Jay of Run DMC, the company runs the Scratch DJ Academy offering beginner to professional curricula, both online and in‑person at locations in New York and Los Angeles. With over 500,000 students taught, 10,000+ DJ events annually, and a network of 7,600+ DJs, Scratch serves brand clients, retailers, hospitality venues, and corporate events worldwide. Their proprietary event platform powers 100,000+ events, delivering scalable solutions and guaranteed paid gigs for graduates. The company also offers equipment discounts and certification tracks, positioning itself as a comprehensive ecosystem for DJ talent and event management.
image: https://cdn.sanity.io/images/091xs2ok/production/139f10d1aa0141182f8290034954f74faeb1464f-7360x4912.jpg?rect=0,524,7360,3864&w=1200&h=630&fit=max&auto=format
layout: provider
modified: '2026-10-22'
name: Scratch Music Group
nav: Providers
network: true
overview: 'Scratch Music Group is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DJ, Education, Event, and Music.


  Scratch Music Group''s developer surface includes documentation, support, and 6 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 64.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/scratch-music-group/scratch-music-group-2026-11-03T142839.png
security:
- kind: domain-security
  name: Scratch Music Group Domain Security
  slug: scratch-music-group-domain-security
  summary_line: TLSv1.3 · HSTS
slug: scratch-music-group
tags:
- Company
- DJ
- Education
- Event
- Music
website: https://www.scratchmusicgroup.com
---
