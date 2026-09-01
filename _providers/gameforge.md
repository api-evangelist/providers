---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Read-only public game-data feeds for OGame, served per game server. Returns highscore rankings, player and alliance rosters, universe/planet layouts, localization tables, and server metadata as XML (a
  name: OGame Public API
  slug: ogame-public-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://gameforge.com/en-US/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://corporate.gameforge.com/
- group: operate
  title: ''
  type: Support
  url: https://support.gameforge.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agbserver.gameforge.com/enGB-Switch-GF-Portal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agbserver.gameforge.com/enGB-Privacy-GF-Portal.html
- group: start
  title: ''
  type: SignUp
  url: https://gameforge.com/en-US/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/gameforge-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/gameforge-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gameforge-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gameforge-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gameforge-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://security.gameforge.com/en
created: '2026-07-17'
description: Gameforge AG is a German publisher of free-to-play online and browser games, headquartered in Karlsruhe, Germany. Its catalog includes long-running titles such as OGame, Ikariam, Metin2, AION, NosTale, and other strategy and MMO games played across dozens of localized game servers. Gameforge's flagship title OGame exposes a public read-only game-data API that returns highscores, player and alliance rosters, universe/planet layouts, and per-server metadata as XML feeds (with an opt-in JSON representation), plus a separate access-controlled API that approved third-party tool developers can request for combat and report data. Gameforge also runs a coordinated vulnerability disclosure program through Bugcrowd. This profile was surfaced as a portfolio company of Accel and enriched by the API Evangelist pipeline.
image: https://gameforge.com/.resources/portal/images/logos/gameforge-logo.svg
layout: provider
modified: '2026-07-19'
name: Gameforge
nav: Providers
network: true
overview: 'Gameforge publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gaming, Games, and Online Games.


  Gameforge''s developer surface includes support, signup flow, and 10 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 14.0
  coverage:
    artifact_dirs: 4
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gameforge/refs/heads/main/screenshots/gameforge-2026-07-25T215416.png
security:
- kind: domain-security
  name: Gameforge Domain Security
  slug: gameforge-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gameforge Vulnerability Disclosure
  slug: gameforge-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: gameforge
tags:
- Company
- Consumer
- Gaming
- Games
- Online Games
- Browser Games
- Free-to-Play
- Publishers
- Entertainment
website: https://gameforge.com/en-US/
---
