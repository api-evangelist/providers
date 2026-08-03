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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-03'
api_count: 5
apis:
- description: Read-only JSON endpoints for the RuneScape (RS3) Grand Exchange item database - item detail (price, trend, 30/90/180-day movement), category listings, and daily price-history graphs. Unauthenticated G
  name: RuneScape Grand Exchange API
  slug: runescape-grand-exchange-api
- description: Read-only JSON endpoints for the Old School RuneScape (OSRS) Grand Exchange item database - item detail, category listings, and price-history graphs. Unauthenticated GET.
  name: Old School RuneScape Grand Exchange API
  slug: old-school-runescape-grand-exchange-api
- description: Player skill and activity rankings for RuneScape (RS3). The index_lite endpoint returns rank, level, and experience per skill as CSV; unauthenticated GET keyed by player display name.
  name: RuneScape Hiscores API
  slug: runescape-hiscores-api
- description: Player skill and activity rankings for Old School RuneScape (OSRS). The index_lite endpoint returns rank, level, and experience per skill as CSV; unauthenticated GET keyed by player display name.
  name: Old School RuneScape Hiscores API
  slug: old-school-runescape-hiscores-api
- description: Public player-profile service for RuneScape (RS3), exposing summary statistics, skill levels, quest progress, and recent activity for accounts that have opted their profile public. Returns JSON; unaut
  name: RuneMetrics Profile API
  slug: runemetrics-profile-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.jagex.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://secure.runescape.com/m=itemdb_rs/
- group: docs
  title: ''
  type: Documentation
  url: https://runescape.wiki/w/Application_programming_interface
- group: company
  title: ''
  type: Blog
  url: https://www.jagex.com/news
- group: company
  title: ''
  type: Careers
  url: https://www.jagex.com/careers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.jagex.com/docs/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.jagex.com/docs/policies/privacy
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/jagex-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/jagex-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jagex-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.jagex.com/.well-known/security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jagex-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/jagex-llms.txt
created: '2026-07-17'
description: 'Jagex is a British video game developer and publisher headquartered in Cambridge, England, best known as the studio behind RuneScape and Old School RuneScape - persistent, community-shaped online worlds that have run for over two decades. Beyond the games, Jagex operates a set of public, read-only RuneScape web-data APIs: the Grand Exchange item price and catalogue endpoints (for both RuneScape and Old School RuneScape), the RuneScape and Old School RuneScape Hiscores, and the RuneMetrics player-profile service. These unauthenticated JSON and CSV endpoints power a large third-party ecosystem of price trackers, fan sites, clan tools, and community applications. Jagex was surfaced as a portfolio company of Insight Partners.'
image: https://framerusercontent.com/images/9PUahve9ur24noPS9vqowNzFwU.jpg
layout: provider
modified: '2026-07-19'
name: Jagex
nav: Providers
network: true
overview: 'Jagex publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Gaming, Games, RuneScape, and MMORPG.


  Jagex''s developer surface includes documentation, engineering blog, and 11 more developer resources.'
random_paper: 52
score:
  band: emerging
  composite: 18.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 92.6
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 18.8
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jagex/refs/heads/main/screenshots/jagex-2026-07-25T223038.png
security:
- kind: domain-security
  name: Jagex Domain Security
  slug: jagex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jagex Vulnerability Disclosure
  slug: jagex-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jagex
tags:
- Company
- Gaming
- Games
- RuneScape
- MMORPG
- Video Games
- Game Data
- Grand Exchange
- Hiscores
- Player Data
website: https://www.jagex.com/
---
