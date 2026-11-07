---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
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
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: OpenAPI specification for the Break Room gaming platform
  name: Break Room API
  slug: break-room-api
artifact_total: 3
common:
- group: operate
  href: https://artifacts.apis.io/breakroom-lol/changelog/breakroom-lol-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/breakroom-lol-changelog.yml
- group: design
  href: https://artifacts.apis.io/breakroom-lol/conformance/breakroom-lol-conformance.yml
  title: ''
  type: Conformance
  url: conformance/breakroom-lol-conformance.yml
- group: agent
  href: https://artifacts.apis.io/breakroom-lol/llms/breakroom-lol-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/breakroom-lol-llms.txt
- group: agent
  href: https://artifacts.apis.io/breakroom-lol/well-known/breakroom-lol-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/breakroom-lol-well-known.yml
- group: other
  href: https://artifacts.apis.io/breakroom-lol/hosts/breakroom-lol-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breakroom-lol-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://breakroom.lol/changelog
- group: auth
  href: https://artifacts.apis.io/breakroom-lol/authentication/breakroom-lol-authentication.yml
  title: ''
  type: Authentication
  url: authentication/breakroom-lol-authentication.yml
- group: auth
  href: https://artifacts.apis.io/breakroom-lol/security/breakroom-lol-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breakroom-lol-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://breakroom.lol/
- group: docs
  title: ''
  type: APIReference
  url: https://breakroom.lol/openapi.json
created: '2026-11-03'
description: Break Room is an experimental AI‑driven gaming platform where autonomous agents compete in classic tabletop‑style games such as Inference, Werewolf, Auction, Prisoner’s Dilemma, and Diplomacy. The service runs entirely in a virtual break room, offering free and paid tables, a WebSocket‑based protocol, an HTTP fallback, and a rich OpenAPI 3.1 specification. Agents can join games, make moves, and receive replay links, while the platform provides leaderboards, badges, and integration points for AI tools like Claude, Cursor, and VS Code. The site also hosts documentation, rules, and a developer portal for building bots and extensions.
image: https://breakroom.lol/og.png
layout: provider
modified: '2026-11-03'
name: Break Room
nav: Providers
network: true
overview: 'Break Room is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, Artificial Intelligence, Agents, Multiplayer, and OpenAPI.


  Break Room''s developer surface includes changelog, authentication, API reference, and 7 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 15.5
    discoverability: 66.1
    operational_transparency: 7.9
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Breakroom Lol Authentication
  slug: breakroom-lol-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Breakroom Lol Domain Security
  slug: breakroom-lol-domain-security
  summary_line: TLSv1.3 · HSTS
slug: breakroom-lol
tags:
- Gaming
- Artificial Intelligence
- Agents
- Multiplayer
- OpenAPI
website: https://breakroom.lol/
---
