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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 64
  human_in_the_loop: 2
  name: Streamelements Agentic Access
  operation_count: 137
  slug: streamelements-agentic-access
  summary_line: 137 operations · 64 acting · 2 human-in-the-loop
api_count: 24
apis:
- description: Endpoints to interract with activities collected by StreamElements
  name: StreamElements activities API
  slug: streamelements-activities-api
- description: Endpoints to manage StreamElements chat bot
  name: StreamElements bot API
  slug: streamelements-bot-api
- description: Endpoints to get channel data
  name: StreamElements channels API
  slug: streamelements-channels-api
- description: Endpoint to get chat statistics
  name: StreamElements chatstats API
  slug: streamelements-chatstats-api
- description: Bot commands management
  name: StreamElements commands API
  slug: streamelements-commands-api
- description: Endpoints to interract with contests
  name: StreamElements contests API
  slug: streamelements-contests-api
- description: Bot spam filters management
  name: StreamElements filters API
  slug: streamelements-filters-api
- description: 'This endpoint is available only in the API version 3. Make sure to use the v3 base URL: https://api.streamelements.com/kappa/v3.'
  name: StreamElements giveaways API
  slug: streamelements-giveaways-api
- description: Endpoints to manage loyalty settings
  name: StreamElements loyalties API
  slug: streamelements-loyalties-api
- description: Endpoints to manage bot modules
  name: StreamElements modules API
  slug: streamelements-modules-api
- description: Endpoints to manage overlays assigned to channel
  name: StreamElements overlays API
  slug: streamelements-overlays-api
- description: Endpoints to manage loyalty points
  name: StreamElements points API
  slug: streamelements-points-api
- description: The redemptions API from StreamElements — 4 operation(s) for redemptions.
  name: StreamElements redemptions API
  slug: streamelements-redemptions-api
- description: Endpoints to manage session data
  name: StreamElements sessions API
  slug: streamelements-sessions-api
- description: The single contest API from StreamElements — 6 operation(s) for single contest.
  name: StreamElements single contest API
  slug: streamelements-single-contest-api
- description: 'This endpoint is available only in the API version 3. Make sure to use the v3 base URL: https://api.streamelements.com/kappa/v3.'
  name: StreamElements single giveaway API
  slug: streamelements-single-giveaway-api
- description: Endpoints to manage single user points data
  name: StreamElements single user API
  slug: streamelements-single-user-api
- description: Endpoints to interact with StreamElements Mediashare
  name: StreamElements songrequests API
  slug: streamelements-songrequests-api
- description: Folder for loyalty
  name: StreamElements stats API
  slug: streamelements-stats-api
- description: Store items management
  name: StreamElements store API
  slug: streamelements-store-api
- description: Endpoints to browse StreamElements themes
  name: StreamElements themes API
  slug: streamelements-themes-api
- description: Bot timers (chat "cron" messages) management
  name: StreamElements timers API
  slug: streamelements-timers-api
- description: Endpoints to interract with tips
  name: StreamElements tips API
  slug: streamelements-tips-api
- description: Folder for loyalty
  name: StreamElements users API
  slug: streamelements-users-api
artifact_total: 30
asyncapis:
- description: StreamElements' dedicated pubsub WebSocket gateway. Subscribe to per-channel topics to receive live stream events (tips, activities, session updates, overlay/chatbot events) the moment they happen. Ca
  name: StreamElements Astro Real-Time Gateway
  slug: streamelements-astro-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/streamelements-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/streamelements-agentic-access.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/streamelements-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/streamelements-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.streamelements.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.streamelements.com/docs/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.streamelements.com/docs/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.streamelements.com/docs/api-docs/authentication
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StreamElements
- group: operate
  title: ''
  type: Support
  url: https://support.streamelements.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.streamelements.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://streamelements.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://streamelements.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://streamelements.com/login
- group: operate
  title: ''
  type: StatusPage
  url: https://status.streamelements.com/
- group: design
  title: ''
  type: Conventions
  url: conventions/streamelements-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/streamelements-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/streamelements-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/streamelements-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/streamelements-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/streamelements-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/streamelements-llms.txt
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/streamelements-astro-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/streamelements-astro-asyncapi.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/streamelements-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/streamelements-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/streamelements-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: StreamElements is a cloud-based platform for live streamers and content creators on Twitch, YouTube, Kick and Facebook, offering 100% free customizable overlays and alerts, a chatbot, tipping and donations, loyalty points, giveaways and contests, song requests, a media/merch store, brand sponsorships, and analytics — all managed from the StreamElements dashboard. Developers integrate through a public REST API at api.streamelements.com (kappa v2/v3) authenticated with JWT, overlay API keys, or OAuth2, plus the Astro real-time WebSocket gateway (wss://astro.streamelements.com) for live event topics.
image: https://streamelements.com/logo.png
layout: provider
mcp_servers:
- description: ''
  name: streamelements-mcp.yml
  slug: streamelements-mcpyml
modified: '2026-07-21'
name: StreamElements
nav: Providers
network: true
overview: 'StreamElements publishes 24 APIs on the [APIs.io](https://apis.io/) network, including activities API, bot API, channels API, and 21 more. Tagged areas include Company, Consumer, Live Streaming, Creator Economy, and Overlays.


  The StreamElements catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  StreamElements'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 21 more developer resources.'
random_paper: 37
scopes:
- name: Streamelements Scopes
  scope_count: 20
  slug: streamelements-scopes
  summary_line: 20 scopes · authorizationCode
score:
  band: developing
  composite: 52.2
  delta: -1.5
  facets:
    commercial_clarity: 34.2
    contract_quality: 65.7
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 24
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Streamelements Authentication
  slug: streamelements-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Streamelements Domain Security
  slug: streamelements-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: streamelements
tags:
- Company
- Consumer
- Live Streaming
- Creator Economy
- Overlays
- Chatbot
- Monetization
- Donations
- Loyalty Points
- Giveaways
- Video
- Twitch
- YouTube
- Real-Time
- WebSockets
- Webhooks
- REST
website: https://dev.streamelements.com/
---
