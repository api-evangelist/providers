---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
  score: 18.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: AnimeHunt provides a searchable catalog of anime, manga and webtoons via a JSON API.
  name: AnimeHunt API
  slug: animehunt-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/animehunt-co/mcp/animehunt-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/animehunt-co-mcp.yml
- group: agent
  href: https://artifacts.apis.io/animehunt-co/well-known/animehunt-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/animehunt-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/animehunt-co/hosts/animehunt-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/animehunt-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/animehunt-co/vendors/animehunt-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/animehunt-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://animehunt.co/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://animehunt.co/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://animehunt.co/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://animehunt.co/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://animehunt.co/guides
- group: auth
  href: https://artifacts.apis.io/animehunt-co/security/animehunt-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/animehunt-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://animehunt.co/
coverage:
  checked: '2026-11-01'
  detail: API spec endpoints on https://api.animehunt.co return 401 Unauthorized, indicating authentication is required.
  evidence:
  - status: 404
    url: https://api.animehunt.co/openapi.json
  - status: 401
    url: https://api.animehunt.co/docs
  reason: auth-required
  state: gated
created: '2026-11-01'
description: AnimeHunt is a free anime, manga and webtoon discovery directory and tracker that lists independent series next to studio titles. Discover hidden anime, manga and webtoons you will love, from studio hits to indie series.
image: https://animehunt.co/opengraph-image?347186fedf5da014
layout: provider
mcp_servers:
- description: Remote MCP server at animehunt.co.
  name: AnimeHunt MCP Server
  slug: animehunt-co-mcp-yml
modified: '2026-11-01'
name: AnimeHunt
nav: Providers
network: true
overview: 'AnimeHunt is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Anime, Manga, Webtoons, Discovery, and Tracker.


  AnimeHunt''s developer surface includes support, documentation, and 9 more developer resources.'
random_paper: 0
scopes:
- name: Animehunt Co Scopes
  scope_count: 0
  slug: animehunt-co-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 18.3
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Animehunt Co Authentication
  slug: animehunt-co-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Animehunt Co Domain Security
  slug: animehunt-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: animehunt-co
tags:
- Anime
- Manga
- Webtoons
- Discovery
- Tracker
website: https://animehunt.co/
---
