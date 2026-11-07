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
- description: API reference page discovered at https://bootsandbassline.com/api (no machine‑readable contract found).
  name: Boots & Bassline API
  slug: boots-bassline-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/bootsandbassline-com/llms/bootsandbassline-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bootsandbassline-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bootsandbassline-com/well-known/bootsandbassline-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bootsandbassline-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bootsandbassline-com/hosts/bootsandbassline-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bootsandbassline-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bootsandbassline-com/vendors/bootsandbassline-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bootsandbassline-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://bootsandbassline.com/releases/same-way-home
- group: auth
  href: https://artifacts.apis.io/bootsandbassline-com/security/bootsandbassline-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bootsandbassline-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bootsandbassline.com/
- group: company
  title: ''
  type: About
  url: https://bootsandbassline.com/about
- group: company
  title: ''
  type: Press
  url: https://bootsandbassline.com/press
- group: operate
  title: ''
  type: Contact
  url: https://bootsandbassline.com/agents
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract was found despite an API reference page.
  evidence:
  - status: 404
    url: https://bootsandbassline.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Boots & Bassline is a music collective and brand that creates and shares original songs and albums. Their flagship album "All of It Was Ours" features seventeen tracks about friendship, family, love and the open road, available on Spotify and Apple Music. The site offers a listening room, back room, artwork, wallpapers, and a press page, plus contact via hello@bootsandbassline.com.
image: https://bootsandbassline.com/assets/artist/all-of-it-was-ours-cover.png
layout: provider
modified: '2026-11-02'
name: Boots & Bassline
nav: Providers
network: true
overview: 'Boots & Bassline is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Collective, Album, Streaming, and Creative.


  Boots & Bassline''s developer surface includes changelog and 9 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 58.0
    operational_transparency: 7.9
  provenance:
    mcp: derived
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
  name: Bootsandbassline Com Domain Security
  slug: bootsandbassline-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bootsandbassline-com
tags:
- Music
- Collective
- Album
- Streaming
- Creative
website: https://bootsandbassline.com/
---
