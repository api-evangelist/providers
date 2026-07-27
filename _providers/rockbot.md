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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 38
  human_in_the_loop: 7
  name: Rockbot Agentic Access
  operation_count: 55
  slug: rockbot-agentic-access
  summary_line: 55 operations · 38 acting · 7 human-in-the-loop
api_count: 6
apis:
- description: Audio-messaging campaigns and assets by group or zone.
  name: Rockbot Audio Messaging API
  slug: rockbot-audio-messaging-api
- description: OAuth 2.0 client-credentials token exchange.
  name: Rockbot Auth API
  slug: rockbot-auth-api
- description: Playback history and asynchronous history exports.
  name: Rockbot Data API
  slug: rockbot-data-api
- description: Device status, screenshots, and remote reboot.
  name: Rockbot Devices API
  slug: rockbot-devices-api
- description: Playback control and playlist overrides per zone.
  name: Rockbot Music API
  slug: rockbot-music-api
- description: Digital-signage campaigns and assets by group or zone.
  name: Rockbot Signage API
  slug: rockbot-signage-api
artifact_total: 11
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rockbot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rockbot-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/rockbot-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rockbot-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://rockbot.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.rockbot.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.rockbot.com/api.html
- group: docs
  title: ''
  type: APIReference
  url: https://developer.rockbot.com/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.rockbot.com/start.html
- group: operate
  title: ''
  type: Support
  url: https://support.rockbot.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://blog.rockbot.com
- group: commercial
  title: ''
  type: Pricing
  url: https://rockbot.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://buy.rockbot.com/trial
- group: start
  title: ''
  type: Login
  url: https://rockbot.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rockbot.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rockbot.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rockbot.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rockbot-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rockbot-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rockbot-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rockbot-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rockbot-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rockbot-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rockbot-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rockbot-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Rockbot is a unified in-location media platform for businesses, giving multi-location operators one system to control background music, audio messaging, digital signage, Rockbot TV, music videos, and retail-media advertising across their venues. Its v5 REST API lets customers programmatically manage that estate: control music playback and playlist overrides per zone, run audio-messaging and signage campaigns by group or zone, upload and attach assets, check device status / screenshots and reboot players remotely, and pull or export music, messaging, and signage playback history. Authentication is OAuth 2.0 client-credentials issuing 24-hour bearer tokens, with a documented default rate limit of one request per second. Rockbot is a GV (Google Ventures) portfolio company in the consumer sector.'
image: https://cdn.sanity.io/images/6h2uzio7/production/f258140dd891894dc1e27722af21f29a7c8c33e5-1581x1581.png
layout: provider
mcp_servers:
- description: ''
  name: rockbot-mcp.yml
  slug: rockbot-mcpyml
modified: '2026-07-21'
name: Rockbot
nav: Providers
network: true
overview: 'Rockbot publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audio Messaging API, Auth API, Data API, and 3 more. Tagged areas include Company, Consumer, Music, Digital Signage, and Audio Messaging.


  Rockbot''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 19 more developer resources.'
random_paper: 8
scopes:
- name: Rockbot Scopes
  scope_count: 0
  slug: rockbot-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.1
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 54.6
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 48.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Rockbot Authentication
  slug: rockbot-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Rockbot Domain Security
  slug: rockbot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rockbot
tags:
- Company
- Consumer
- Music
- Digital Signage
- Audio Messaging
- Retail Media
- In-Location Media
- Media
- Entertainment
website: https://rockbot.com
---
