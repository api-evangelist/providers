---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Read-only access to Clash of Clans game data — clan search, global and local leaderboards, clan and player profiles, leagues, war logs, capital raid seasons and the Gold Pass season. Authenticated wit
  name: Clash of Clans API
  slug: clash-of-clans-api
- description: Read-only access to Clash Royale game data — clan search, player and clan profiles, cards, tournaments, challenges, global tournaments and locations/leaderboards. Authenticated with a JWT bearer API t
  name: Clash Royale API
  slug: clash-royale-api
- description: 'Read-only access to Brawl Stars game data — player and club profiles, club members, rankings/leaderboards, brawlers, gadgets/star-powers and rotating events. Authenticated with a JWT bearer API token '
  name: Brawl Stars API
  slug: brawl-stars-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/supercell-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://supercell.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/supercell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/supercell-authentication.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/supercell-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/supercell-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.supercell.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clashofclans.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://supercell.com/en/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://supercell.com/en/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://support.supercell.com/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://supercell.com/.well-known/security.txt
created: '2026-07-17'
description: Supercell is the Finnish mobile game developer behind Clash of Clans, Clash Royale, Brawl Stars, Hay Day, Boom Beach and Squad Busters. Supercell operates three official public game APIs — the Clash of Clans API, the Clash Royale API and the Brawl Stars API — that expose read-only game data including clan search, global and local leaderboards, player and clan profiles, leagues, cards, brawlers, rankings and live events. Access is authenticated with a JWT bearer API token created in each game's developer portal and locked to a set of whitelisted IP addresses. Added to the API Evangelist network from a VC-portfolio lead and enriched with verified developer-surface artifacts.
image: https://cdn.supercell.com/gameapi/website/og_coc_share_img.jpg
layout: provider
modified: '2026-07-21'
name: Supercell
nav: Providers
network: true
overview: 'Supercell publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gaming, Mobile Games, and Video Games.


  Supercell''s developer surface includes authentication, support, and 10 more developer resources.'
random_paper: 27
score:
  band: emerging
  composite: 19.6
  delta: -0.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 23.9
    discoverability: 92.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Supercell Authentication
  slug: supercell-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Supercell Domain Security
  slug: supercell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Supercell Vulnerability Disclosure
  slug: supercell-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: supercell
tags:
- Company
- Consumer
- Gaming
- Mobile Games
- Video Games
- Game Data
- Developer API
- Leaderboards
- Esports
website: https://www.supercell.com
---
