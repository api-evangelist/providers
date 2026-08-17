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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Betgenius Agentic Access
  operation_count: 13
  slug: betgenius-agentic-access
  summary_line: 13 operations · 8 acting
api_count: 3
apis:
- description: The current Booking API. Three operations that let a contracted sportsbook list the upcoming fixtures it can book, book a fixture to turn on its data feeds, and un-book it again. Served from BetGenius
  name: BetGenius Booking API V2
  slug: betgenius-booking-api-v2
- description: The pre-v2 Booking API, still served alongside V2 from the same Swashbuckle discovery list. The same three operations on the /api/booking path; the only contract difference from V2 is that its Feed ob
  name: BetGenius Booking API V1
  slug: betgenius-booking-api-v1
- description: The server-side half of BetVision and the Genius Live Player. Lists fixtures with live and VOD streams together with their per-stream entitlement (device, region, DMA, maximum player size), lists supp
  name: BetGenius Video Streaming API v3
  slug: betgenius-video-streaming-api-v3
artifact_total: 10
asyncapis:
- description: ''
  name: Betgenius Event Surface
  slug: betgenius-event-surface
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/betgenius-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/betgenius-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/betgenius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.geniussports.com/bet/
- group: other
  title: ''
  type: ParentCompany
  url: https://www.geniussports.com
- group: other
  title: ''
  type: Sportsbooks
  url: https://www.geniussports.com/sportsbooks/
- group: other
  title: ''
  type: DataOddsAPIs
  url: https://www.geniussports.com/bet/odds-feeds-api/
- group: other
  title: ''
  type: GeniusTradingServices
  url: https://www.geniussports.com/bet/genius-trading-services/
- group: other
  title: ''
  type: BetVision
  url: https://www.geniussports.com/bet/bet-vision/
- group: other
  title: ''
  type: FANHub
  url: https://www.geniussports.com/engage/fanhub/
- group: other
  title: ''
  type: MediaBuying
  url: https://www.geniussports.com/engage/fanhub/media-buying/
- group: other
  title: ''
  type: DeveloperCentre
  url: https://developer.geniussports.com/
- group: docs
  title: ''
  type: IntegrationDocs
  url: https://geniussports.atlassian.net/wiki/spaces/BID
- group: docs
  title: ''
  type: BetstreamIntegrationGuide
  url: https://dap-docs.betstream.betgenius.com/
- group: docs
  title: ''
  type: BookingSystemSwagger
  url: https://dataservices.betgenius.com/BookingSystem/swagger/ui/index
- group: company
  title: ''
  type: Investors
  url: https://investors.geniussports.com
- group: company
  title: ''
  type: News
  url: https://news.geniussports.com
- group: operate
  title: ''
  type: ContactSales
  url: https://www.geniussports.com/contact-sales/sportsbook-contact/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/genius-sports/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/GeniusSports
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.geniussports.com/
- group: docs
  title: ''
  type: Documentation
  url: https://geniussports.atlassian.net/wiki/spaces/BID
- group: docs
  title: ''
  type: APIReference
  url: https://dataservices.betgenius.com/BookingSystem/swagger/ui/index
- group: start
  title: ''
  type: GettingStarted
  url: https://dap-docs.betstream.betgenius.com/
- group: operate
  title: ''
  type: Support
  url: https://geniussports.atlassian.net/wiki/spaces/BID/pages/6097764412/Support+User+Guides+and+Info
- group: company
  title: ''
  type: Blog
  url: https://www.geniussports.com/content-hub/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/genius-sports
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.geniussports.com/policies/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.geniussports.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/betgenius-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/betgenius-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/betgenius-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/betgenius-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/betgenius-plans-pricing.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/betgenius-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/betgenius-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/betgenius-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/betgenius-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/betgenius-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/betgenius-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/betgenius-event-surface.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/betgenius-llms.txt
created: '2026-05-25'
description: BetGenius is the sportsbook-operator brand of Genius Sports, a London- and New York-listed sports data, technology, and commercial-services group. Founded in 2000 and operating as a Genius Sports business unit since the 2015 corporate consolidation, BetGenius provides licensed sportsbooks with an end-to-end B2B platform spanning official data and odds feeds, fully managed trading and risk management (Genius Trading Services), low-latency live video and interactive in-play streaming (BetVision and Genius Live Player), BetBuilder same-game-parlay pricing, ScoreCentre widgets, acquisition and retention marketing (FANHub, media buying, dynamic creative optimisation), and back-office sportsbook platform services (used by operators such as OPAP, 888, Betway, and Hard Rock Bet). Genius Sports sources official data from 400+ league partners — including the NFL, English Premier League, Serie A, EuroLeague, and PGA Tour — and serves 300+ licensed sportsbooks across regulated markets worldwide.
  BetGenius itself does not expose a self-service developer portal; its APIs (Booking API, Fixtures API v2, Matching API v2, Warehouse REST/Streaming/Publish APIs, LiveStats In-Arena and Licensing APIs, BetVision and Live Player integration SDKs) are documented at developer.geniussports.com and delivered to contracted operators via UAT and production environments using API-key authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/betgenius.png
layout: provider
modified: '2026-08-13'
name: BetGenius
nav: Providers
network: true
overview: 'BetGenius publishes 3 APIs on the [APIs.io](https://apis.io/) network: Booking API V2, Booking API V1, and Video Streaming API v3. Tagged areas include Sportsbook, Sports Betting, Sports Data, Odds Feeds, and Trading Services.


  The BetGenius catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  BetGenius'' developer surface includes authentication, product news, documentation, API reference, getting-started guide, support, engineering blog, and 36 more developer resources.'
plans:
- name: Betgenius Plans Pricing
  plan_count: 0
  slug: betgenius-plans-pricing
random_paper: 72
rate_limits:
- limit_count: 5
  name: Betgenius Rate Limits
  slug: betgenius-rate-limits
scopes:
- name: Betgenius Scopes
  scope_count: 10
  slug: betgenius-scopes
  summary_line: 10 scopes
score:
  band: developing
  composite: 47.2
  delta: 42.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 54.2
    developer_ergonomics: 65.2
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 60.5
  previous_composite: 5.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/betgenius/refs/heads/main/screenshots/betgenius-2026-06-20T173202.png
security:
- kind: authentication
  name: Betgenius Authentication
  slug: betgenius-authentication
  summary_line: http/apiKey/oauth2 · 5 schemes
- kind: domain-security
  name: Betgenius Domain Security
  slug: betgenius-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: betgenius
tags:
- Sportsbook
- Sports Betting
- Sports Data
- Odds Feeds
- Trading Services
- Risk Management
- Live Streaming
- In-Play Betting
- BetBuilder
- Player Engagement
- Marketing Technology
- Gambling
website: https://www.geniussports.com/bet/
---
