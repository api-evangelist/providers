---
access_model:
  confidence: low
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Splitgate Agentic Access
  operation_count: 5
  slug: splitgate-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://api.1047games.com
  baseurl_source: declared
  description: The Matches API from Splitgate — 1 operation(s) for matches.
  name: Splitgate Matches API
  slug: splitgate-matches-api
- baseURL: https://api.1047games.com
  baseurl_source: declared
  description: The Players API from Splitgate — 4 operation(s) for players.
  name: Splitgate Players API
  slug: splitgate-players-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 1047 Games Third-Party Matches API
  slug: open-splitgate-matches-api
- collection_type: open
  name: 1047 Games Third-Party Players API
  slug: open-splitgate-players-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/1047Games/sdk-api/issues
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
  name: Splitgate MCP Server
  slug: splitgate-mcp-server
modified: '2026-08-05'
name: Splitgate
nav: Providers
network: true
overview: 'Splitgate publishes 2 APIs on the [APIs.io](https://apis.io/) network: Matches API and Players API. Tagged areas include Company, Gaming, Video Games, Esports, and Player Statistics.


  Splitgate''s developer surface includes API reference, support, engineering blog, YouTube channel, and 19 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 0
  name: Splitgate Rate Limits
  slug: splitgate-rate-limits
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 3.4
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 54.4
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 30.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/splitgate/refs/heads/main/screenshots/splitgate-2026-09-02T160519.png
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
