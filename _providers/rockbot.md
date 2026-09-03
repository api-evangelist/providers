---
access_model:
  confidence: high
  label: Paid product; API access on request
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - authentication
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.9
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 38
  human_in_the_loop: 7
  name: Rockbot Agentic Access
  operation_count: 55
  slug: rockbot-agentic-access
  summary_line: 55 operations · 38 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.rockbot.com/v5
  baseurl_source: declared
  description: Audio-messaging campaigns and assets by group or zone.
  name: Rockbot Audio Messaging API
  slug: rockbot-audio-messaging-api
- baseURL: https://api.rockbot.com/v5
  baseurl_source: declared
  description: OAuth 2.0 client-credentials token exchange.
  name: Rockbot Auth API
  slug: rockbot-auth-api
- baseURL: https://api.rockbot.com/v5
  baseurl_source: declared
  description: Playback history and asynchronous history exports.
  name: Rockbot Data API
  slug: rockbot-data-api
- baseURL: https://api.rockbot.com/v5
  baseurl_source: declared
  description: Device status, screenshots, and remote reboot.
  name: Rockbot Devices API
  slug: rockbot-devices-api
- baseURL: https://api.rockbot.com/v5
  baseurl_source: declared
  description: Playback control and playlist overrides per zone.
  name: Rockbot Music API
  slug: rockbot-music-api
- baseURL: https://api.rockbot.com/v5
  baseurl_source: declared
  description: Digital-signage campaigns and assets by group or zone.
  name: Rockbot Signage API
  slug: rockbot-signage-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rockbot Audio Messaging API
  slug: open-rockbot-audio-messaging-api
- collection_type: open
  name: Rockbot Audio Messaging Auth API
  slug: open-rockbot-auth-api
- collection_type: open
  name: Rockbot Audio Messaging Data API
  slug: open-rockbot-data-api
- collection_type: open
  name: Rockbot Audio Messaging Devices API
  slug: open-rockbot-devices-api
- collection_type: open
  name: Rockbot Audio Messaging Music API
  slug: open-rockbot-music-api
- collection_type: open
  name: Rockbot Audio Messaging Signage API
  slug: open-rockbot-signage-api
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
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/rockbot-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rockbot-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rockbot-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/rockbot-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rockbot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rockbot-rate-limits.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/rockbot-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.rockbot.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rockbot-inc
created: '2026-07-17'
description: 'Rockbot is a unified in-location media platform for businesses, giving multi-location operators one system to control background music, audio messaging, digital signage, Rockbot TV, music videos, and retail-media advertising across their venues. Its v5 REST API lets customers programmatically manage that estate: control music playback and playlist overrides per zone, run audio-messaging and signage campaigns by group or zone, upload and attach assets, check device status / screenshots and reboot players remotely, and pull or export music, messaging, and signage playback history. Authentication is OAuth 2.0 client-credentials issuing 24-hour bearer tokens, with a documented default rate limit of one request per second. Rockbot is a GV (Google Ventures) portfolio company in the consumer sector.'
image: https://cdn.sanity.io/images/6h2uzio7/production/f258140dd891894dc1e27722af21f29a7c8c33e5-1581x1581.png
layout: provider
mcp_servers:
- description: ''
  name: Rockbot MCP
  slug: rockbot-mcp
modified: '2026-08-13'
name: Rockbot
nav: Providers
network: true
overview: 'Rockbot publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Audio Messaging API, Auth API, Data API, and 3 more. Tagged areas include Company, Consumer, Music, Digital Signage, and Audio Messaging.


  Rockbot''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Rockbot Plans Pricing
  plan_count: 4
  slug: rockbot-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Rockbot Rate Limits
  slug: rockbot-rate-limits
scopes:
- name: Rockbot Scopes
  scope_count: 0
  slug: rockbot-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 56.3
  coverage:
    artifact_dirs: 21
    catalog_gap: 58.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 50.1
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 39.5
  previous_composite: 56.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rockbot/refs/heads/main/screenshots/rockbot-2026-08-17T081620.png
security:
- kind: authentication
  name: Rockbot Authentication
  slug: rockbot-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Rockbot Domain Security
  slug: rockbot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rockbot Vulnerability Disclosure
  slug: rockbot-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Rockbot Trust Center
  slug: rockbot-trust-center
  summary_line: SOC 2
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
