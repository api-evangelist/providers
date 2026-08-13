---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Splitgate Agentic Access
  operation_count: 5
  slug: splitgate-agentic-access
  summary_line: 5 operations
api_count: 2
apis:
- description: The Matches API from Splitgate — 1 operation(s) for matches.
  name: Splitgate Matches API
  slug: splitgate-matches-api
- description: The Players API from Splitgate — 4 operation(s) for players.
  name: Splitgate Players API
  slug: splitgate-players-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/splitgate-match-history.md
- group: other
  title: ''
  type: Overlay
  url: overlays/splitgate-third-party-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.splitgate.com/
- group: company
  title: ''
  type: CompanyWebsite
  url: https://1047games.com/
- group: docs
  title: ''
  type: APIReference
  url: https://1047games.github.io/sdk-api/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1047Games
- group: operate
  title: ''
  type: Support
  url: https://support.splitgate.com/hc
- group: company
  title: ''
  type: Blog
  url: https://www.splitgate.com/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.splitgate.com/tos-eula
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.splitgate.com/privacy-policy
- group: build
  title: ''
  type: CodeOfConduct
  url: https://www.splitgate.com/code-of-conduct
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/splitgate
- group: build
  title: ''
  type: Packages
  url: packages/splitgate-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/splitgate-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/splitgate-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/splitgate-llms.txt
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/splitgate
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCdUA8I1gJ606kBa9MfTZIyw
- group: other
  title: ''
  type: Twitch
  url: https://www.twitch.tv/splitgate
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/splitgate/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Splitgate/
- group: other
  title: ''
  type: Forge
  url: https://forgeglobal.com/splitgate_stock/
created: '2026-08-05'
description: 'Splitgate is the free-to-play sci-fi arena first-person shooter franchise built by 1047 Games, the Stanford-founded studio behind the portal-plus-FPS formula that shipped as Splitgate (2019), Splitgate 2 (June 2025) and, after a full rebuild, SPLITGATE: Arena Reloaded (December 2025). Beyond the game itself, 1047 Games publishes a small public Third-Party API — an OpenAPI 3.0.1 contract served from the studio''s own GitHub organization with a Swagger UI reference — exposing player search, career and per-mode statistics, competitive ranks, match history and full match details so community stat trackers, esports tooling and leaderboard sites can build against real game data.'
image: https://lp-cms-prod.images.maverick-rooster.prod.1047games.com/tiny_Rooster_Social_Discord_Banner_960x540_2a5d61e42b.png
layout: provider
mcp_servers:
- description: ''
  name: splitgate-mcp.yml
  slug: splitgate-mcpyml
modified: '2026-08-05'
name: Splitgate
nav: Providers
network: true
overview: 'Splitgate publishes 2 APIs on the [APIs.io](https://apis.io/) network: Matches API and Players API. Tagged areas include Company, Gaming, Video Games, Esports, and Player Statistics.


  Splitgate''s developer surface includes API reference, support, engineering blog, YouTube channel, and 18 more developer resources.'
random_paper: 13
rate_limits:
- limit_count: 0
  name: Splitgate Rate Limits
  slug: splitgate-rate-limits
score:
  band: thin
  composite: 32.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 61.2
    developer_ergonomics: 14.7
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 32.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Splitgate Authentication
  slug: splitgate-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Splitgate Domain Security
  slug: splitgate-domain-security
  summary_line: TLSv1.3 · DMARC
slug: splitgate
tags:
- Company
- Gaming
- Video Games
- Esports
- Player Statistics
- Leaderboards
- Match Data
- Entertainment
website: https://www.splitgate.com/
---
