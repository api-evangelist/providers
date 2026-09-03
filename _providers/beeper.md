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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Beeper Agentic Access
  operation_count: 30
  slug: beeper-agentic-access
  summary_line: 30 operations · 18 acting
api_count: 1
apis:
- baseURL: http://localhost:23373
  baseurl_source: declared
  description: Chat Accounts connected to this Beeper Desktop instance. Each Account owns a bridge and network.
  name: Beeper Accounts API
  slug: beeper-accounts-api
- baseURL: http://localhost:23373
  baseurl_source: declared
  description: 'Top-level actions: focus the app window, jump to a chat, or run unified search across chats and messages.'
  name: Beeper App API
  slug: beeper-app-api
- baseURL: http://localhost:23373
  baseurl_source: declared
  description: Chats, reminders, read state, archive state, priority, mute, and other conversation metadata.
  name: Beeper Chats API
  slug: beeper-chats-api
- baseURL: http://localhost:23373
  baseurl_source: declared
  description: Per-account address book and network lookup. The same person can appear under multiple Accounts.
  name: Beeper Contacts API
  slug: beeper-contacts-api
- baseURL: http://localhost:23373
  baseurl_source: declared
  description: File upload, download, and streaming helpers for message attachments and drafts.
  name: Beeper Files API
  slug: beeper-files-api
- baseURL: http://localhost:23373
  baseurl_source: declared
  description: 'Messages inside a Chat: list, search, send, retrieve, edit, delete, and react.'
  name: Beeper Messages API
  slug: beeper-messages-api
- baseURL: http://localhost:23373
  baseurl_source: declared
  description: Server discovery and capability metadata. Use /v1/info before authentication setup.
  name: Beeper Server API
  slug: beeper-server-api
artifact_total: 21
asyncapis:
- description: Experimental WebSocket event stream exposed by the local Beeper Desktop API. Clients subscribe to chats and receive domain events as they occur.
  name: Beeper Desktop API - Live Events
  slug: beeper-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Beeper Desktop Accounts API
  slug: open-beeper-accounts-api
- collection_type: open
  name: Beeper Desktop Accounts App API
  slug: open-beeper-app-api
- collection_type: open
  name: Beeper Desktop Accounts Chats API
  slug: open-beeper-chats-api
- collection_type: open
  name: Beeper Desktop Accounts Contacts API
  slug: open-beeper-contacts-api
- collection_type: open
  name: Beeper Desktop Accounts Files API
  slug: open-beeper-files-api
- collection_type: open
  name: Beeper Desktop Accounts Messages API
  slug: open-beeper-messages-api
- collection_type: open
  name: Beeper Desktop Accounts Server API
  slug: open-beeper-server-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/beeper-desktop-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.beeper.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.beeper.com/desktop-api/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.beeper.com/desktop-api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.beeper.com/desktop-api/
- group: auth
  title: ''
  type: Authentication
  url: authentication/beeper-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/beeper-scopes.yml
- group: build
  title: ''
  type: SDKs
  url: packages/beeper-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/beeper-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/beeper-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/beeper-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/beeper-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/beeper-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/beeper-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/beeper-conformance.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/beeper-events-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/beeper-events-asyncapi.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/beeper-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://beeperstatus.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/beeper-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beeper-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beeper-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/beeper
- group: company
  title: ''
  type: Blog
  url: https://blog.beeper.com/
- group: operate
  title: ''
  type: Support
  url: https://help.beeper.com/
- group: start
  title: ''
  type: SignUp
  url: https://www.beeper.com/download
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.beeper.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.beeper.com/privacy
- group: company
  title: ''
  type: Website
  url: https://beeper.com/
created: '2026-07-17'
description: 'Beeper is a universal chat app that brings 12+ messaging networks — WhatsApp, Instagram, Telegram, Signal, Messenger, X, Google Messages, Google Chat, Google Voice, LinkedIn, Discord and Slack — into a single unified inbox across macOS, Windows, Linux, iOS and Android. Built on the Matrix protocol and owned by Automattic, Beeper connects to networks on-device for privacy. For developers Beeper ships the Beeper Desktop API: a local-first REST API and built-in Model Context Protocol (MCP) server that runs entirely on the user''s machine, letting agents and apps search chats, read and send messages, react, manage reminders and control the app. Official SDKs are published for JavaScript, Python, Go and PHP, alongside bridges for self-hosting and Android intents/content-providers.'
image: https://www.beeper.com/wp-content/themes/beeper-site/assets/img/opengraph-image.png
layout: provider
mcp_servers:
- description: Beeper Desktop ships a built-in Model Context Protocol server that runs locally inside the Beeper Desktop app, exposing the user's unified chats, messages, contacts and accounts to MCP clients (Claude
  name: Beeper MCP Server
  slug: beeper-mcp-server
modified: '2026-07-18'
name: Beeper
nav: Providers
network: true
overview: 'Beeper publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, App API, Chats API, and 4 more. Tagged areas include Company, Consumer, Messaging, Chat, and Communications.


  The Beeper catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Beeper''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, engineering blog, support, and 23 more developer resources.'
random_paper: 18
scopes:
- name: Beeper Scopes
  scope_count: 2
  slug: beeper-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 20
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 60.6
    developer_ergonomics: 66.1
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beeper/refs/heads/main/screenshots/beeper-2026-07-25T202639.png
security:
- kind: authentication
  name: Beeper Authentication
  slug: beeper-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Beeper Domain Security
  slug: beeper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beeper
tags:
- Company
- Consumer
- Messaging
- Chat
- Communications
- Matrix
- MCP
- Desktop
- Aggregator
website: https://beeper.com/
---
