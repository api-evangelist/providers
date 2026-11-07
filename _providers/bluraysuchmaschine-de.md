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
- group: other
  href: https://artifacts.apis.io/bluraysuchmaschine-de/hosts/bluraysuchmaschine-de-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluraysuchmaschine-de-hosts.yml
- group: start
  title: ''
  type: SignUp
  url: https://bluraysuchmaschine.de/register
- group: other
  title: ''
  type: Leadership
  url: https://bluraysuchmaschine.de/product/management
- group: operate
  title: ''
  type: ChangeLog
  url: https://bluraysuchmaschine.de/releases
- group: auth
  href: https://artifacts.apis.io/bluraysuchmaschine-de/security/bluraysuchmaschine-de-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluraysuchmaschine-de-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluraysuchmaschine.de/
coverage:
  checked: '2026-11-02'
  detail: The site provides only product listings and no developer documentation or API information.
  evidence:
  - status: 200
    url: https://bluraysuchmaschine.de/
  reason: no-developer-program
  state: none
created: '2026-11-02'
description: Blu-ray Suchmaschine is an online platform that helps users find and purchase Blu-ray movies and TV series. It offers a searchable catalog of titles, detailed product pages, and the ability to create a free account for wishlists and collection management. The service aggregates Blu-ray releases from various sources, providing recommendations and links to purchase options, primarily through Amazon.
layout: provider
modified: '2026-11-02'
name: Blu-ray Suchmaschine
nav: Providers
network: true
overview: 'Blu-ray Suchmaschine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Blu-ray, E-Commerce, Media, Search, and German.


  Blu-ray Suchmaschine''s developer surface includes signup flow, changelog, and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.5
    operational_transparency: 7.9
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
  name: Bluraysuchmaschine De Domain Security
  slug: bluraysuchmaschine-de-domain-security
  summary_line: TLSv1.3
slug: bluraysuchmaschine-de
tags:
- Blu-ray
- E-Commerce
- Media
- Search
- German
website: https://bluraysuchmaschine.de/
---
