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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.2
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 64
  human_in_the_loop: 2
  name: Streamelements Agentic Access
  operation_count: 137
  slug: streamelements-agentic-access
  summary_line: 137 operations · 64 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to interract with activities collected by StreamElements
  name: StreamElements activities API
  slug: streamelements-activities-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to manage StreamElements chat bot
  name: StreamElements bot API
  slug: streamelements-bot-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to get channel data
  name: StreamElements channels API
  slug: streamelements-channels-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoint to get chat statistics
  name: StreamElements chatstats API
  slug: streamelements-chatstats-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Bot commands management
  name: StreamElements commands API
  slug: streamelements-commands-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to interract with contests
  name: StreamElements contests API
  slug: streamelements-contests-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Bot spam filters management
  name: StreamElements filters API
  slug: streamelements-filters-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: 'This endpoint is available only in the API version 3. Make sure to use the v3 base URL: https://api.streamelements.com/kappa/v3.'
  name: StreamElements giveaways API
  slug: streamelements-giveaways-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to manage loyalty settings
  name: StreamElements loyalties API
  slug: streamelements-loyalties-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to manage bot modules
  name: StreamElements modules API
  slug: streamelements-modules-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to manage overlays assigned to channel
  name: StreamElements overlays API
  slug: streamelements-overlays-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to manage loyalty points
  name: StreamElements points API
  slug: streamelements-points-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: The redemptions API from StreamElements — 4 operation(s) for redemptions.
  name: StreamElements redemptions API
  slug: streamelements-redemptions-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to manage session data
  name: StreamElements sessions API
  slug: streamelements-sessions-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: The single contest API from StreamElements — 6 operation(s) for single contest.
  name: StreamElements single contest API
  slug: streamelements-single-contest-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: 'This endpoint is available only in the API version 3. Make sure to use the v3 base URL: https://api.streamelements.com/kappa/v3.'
  name: StreamElements single giveaway API
  slug: streamelements-single-giveaway-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to manage single user points data
  name: StreamElements single user API
  slug: streamelements-single-user-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to interact with StreamElements Mediashare
  name: StreamElements songrequests API
  slug: streamelements-songrequests-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Folder for loyalty
  name: StreamElements stats API
  slug: streamelements-stats-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Store items management
  name: StreamElements store API
  slug: streamelements-store-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to browse StreamElements themes
  name: StreamElements themes API
  slug: streamelements-themes-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Bot timers (chat "cron" messages) management
  name: StreamElements timers API
  slug: streamelements-timers-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Endpoints to interract with tips
  name: StreamElements tips API
  slug: streamelements-tips-api
- baseURL: https://api.streamelements.com/kappa/v2
  baseurl_source: declared
  description: Folder for loyalty
  name: StreamElements users API
  slug: streamelements-users-api
artifact_total: 55
asyncapis:
- description: StreamElements' dedicated pubsub WebSocket gateway. Subscribe to per-channel topics to receive live stream events (tips, activities, session updates, overlay/chatbot events) the moment they happen. Ca
  name: StreamElements Astro Real-Time Gateway
  slug: streamelements-astro-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SE API Docs activities API
  slug: open-streamelements-activities-api
- collection_type: open
  name: SE API Docs activities bot API
  slug: open-streamelements-bot-api
- collection_type: open
  name: SE API Docs activities channels API
  slug: open-streamelements-channels-api
- collection_type: open
  name: SE API Docs activities chatstats API
  slug: open-streamelements-chatstats-api
- collection_type: open
  name: SE API Docs activities commands API
  slug: open-streamelements-commands-api
- collection_type: open
  name: SE API Docs activities contests API
  slug: open-streamelements-contests-api
- collection_type: open
  name: SE API Docs activities filters API
  slug: open-streamelements-filters-api
- collection_type: open
  name: SE API Docs activities giveaways API
  slug: open-streamelements-giveaways-api
- collection_type: open
  name: SE API Docs activities loyalties API
  slug: open-streamelements-loyalties-api
- collection_type: open
  name: SE API Docs activities modules API
  slug: open-streamelements-modules-api
- collection_type: open
  name: SE API Docs activities overlays API
  slug: open-streamelements-overlays-api
- collection_type: open
  name: SE API Docs activities points API
  slug: open-streamelements-points-api
- collection_type: open
  name: SE API Docs activities redemptions API
  slug: open-streamelements-redemptions-api
- collection_type: open
  name: SE API Docs activities sessions API
  slug: open-streamelements-sessions-api
- collection_type: open
  name: SE API Docs activities single contest API
  slug: open-streamelements-single-contest-api
- collection_type: open
  name: SE API Docs activities single giveaway API
  slug: open-streamelements-single-giveaway-api
- collection_type: open
  name: SE API Docs activities single user API
  slug: open-streamelements-single-user-api
- collection_type: open
  name: SE API Docs activities songrequests API
  slug: open-streamelements-songrequests-api
- collection_type: open
  name: SE API Docs activities stats API
  slug: open-streamelements-stats-api
- collection_type: open
  name: SE API Docs activities store API
  slug: open-streamelements-store-api
- collection_type: open
  name: SE API Docs activities themes API
  slug: open-streamelements-themes-api
- collection_type: open
  name: SE API Docs activities timers API
  slug: open-streamelements-timers-api
- collection_type: open
  name: SE API Docs activities tips API
  slug: open-streamelements-tips-api
- collection_type: open
  name: SE API Docs activities users API
  slug: open-streamelements-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/streamelements-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/streamelements-api-overlay.yaml
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
  name: StreamElements MCP Server
  slug: streamelements-mcp-server
modified: '2026-07-21'
name: StreamElements
nav: Providers
network: true
overview: 'StreamElements publishes 24 APIs on the [APIs.io](https://apis.io/) network, including activities API, bot API, channels API, and 21 more. Tagged areas include Company, Consumer, Live Streaming, Creator Economy, and Overlays.


  The StreamElements catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  StreamElements'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 23 more developer resources.'
random_paper: 1
scopes:
- name: Streamelements Scopes
  scope_count: 20
  slug: streamelements-scopes
  summary_line: 20 scopes · authorizationCode
score:
  band: developing
  composite: 43.3
  coverage:
    artifact_dirs: 23
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 61.5
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 43.3
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/streamelements/refs/heads/main/screenshots/streamelements-2026-08-17T082134.png
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
- Chatbots
- Monetization
- Donations
- Loyalty Points
- Giveaways
- Video
- Twitch
- YouTube
- Real-Time
- WebSockets
- Webhook
- REST
website: https://dev.streamelements.com/
---
