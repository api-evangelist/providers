---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/end-game-interactive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://end.gg/
- group: company
  title: ''
  type: About
  url: https://end.gg/about
- group: operate
  title: ''
  type: Support
  url: https://end.gg/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://end.gg/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://end.gg/privacy
- group: company
  title: ''
  type: Press
  url: https://end.gg/press
- group: company
  title: ''
  type: Careers
  url: https://end.gg/careers
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/end-game-interactive_stock/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/end-game-interactive-llms.txt
coverage:
  checked: '2026-08-12'
  detail: End Game Interactive is a consumer game publisher whose only web properties are the end.gg marketing site and its game clients — api.end.gg, developer.end.gg and docs.end.gg do not resolve at all, and end.gg has no developer, API or documentation route in its navigation.
  evidence:
  - status: 200
    url: https://end.gg/
  - status: 200
    url: https://end.gg/games
  - status: 404
    url: https://end.gg/openapi.json
  - status: 404
    url: https://end.gg/graphql
  - status: 404
    url: https://end.gg/llms.txt
  - status: 404
    url: https://end.gg/.well-known/agent-card.json
  - status: 404
    url: https://zombsroyale.io/openapi.json
  reason: no-developer-program
  state: none
created: '2026-08-12'
description: 'End Game Interactive, Inc. (ENDGAME) is a Bellevue, Washington video game studio founded by Yang C. Liu and Luke Zbihlyj that builds free-to-play, cross-platform real-time multiplayer titles for browser, mobile and desktop — including ZombsRoyale.io, Zombs.io, Spinz.io, BOPZ.io, Fishington, Betrayal, Super Squad, Match City Puzzle and Fate Arena. The studio describes itself as technology-driven, running small agile teams against a proprietary "ENDGAME ENGINE" alongside Unity and Unreal, with AI-assisted pipelines for asset creation, animation, sound design and voicelines. It raised a $3M seed round in 2020 from Makers Fund, Supercell, Kevin Lin and Scooter Braun among others. ENDGAME is a consumer game publisher: as of this profile it operates no public developer program, no documented API, and no machine-readable contract on any of its web properties.'
image: https://end.gg/asset/image/logo-card.png
layout: provider
modified: '2026-08-12'
name: End Game Interactive
nav: Providers
network: true
overview: 'End Game Interactive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Video Games, Game Development, and Interactive Entertainment.


  End Game Interactive''s developer surface includes support and 9 more developer resources.'
random_paper: 56
score:
  band: minimal
  composite: 10.9
  delta: 0.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: End Game Interactive Domain Security
  slug: end-game-interactive-domain-security
  summary_line: TLSv1.3 · DMARC
slug: end-game-interactive
tags:
- Company
- Gaming
- Video Games
- Game Development
- Interactive Entertainment
- Multiplayer
- Mobile Games
- Consumer
website: https://end.gg/
---
