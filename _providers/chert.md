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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Programmatic send/receive/route over iMessage — 1:1 and group chats, attachments, rich links, tapbacks, typing indicators, location pins, webhook subscriptions and events.
  name: Chert Messaging API
  slug: chert-messaging-api
artifact_total: 5
asyncapis:
- description: ''
  name: Chert Webhooks
  slug: chert-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.trychert.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trychert.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trychert.com/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.trychert.com/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://console.trychert.com
- group: operate
  title: ''
  type: Support
  url: https://www.trychert.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.trychert.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cherthq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.trychert.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.trychert.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chert-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/chert-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/chert-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/chert-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/chert-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/chert-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chert-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/chert-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/chert-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/chert-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chert-domain-security.yml
created: '2026-07-17'
description: Chert is iMessage infrastructure for reaching people at scale. Its Messaging API lets teams programmatically send, receive, route, and observe real iMessage conversations — blue-bubble threads from verified numbers with typing indicators, tapback reactions, reply context, multi-recipient group threads, SMS fallback, file attachments, rich-link previews, one-time location pins, and delivery receipts. Chert also ships native integrations for Salesforce, HubSpot, and Slack, plus webhook subscriptions and an event stream (message.received, reaction.added/removed) for real-time inbound replies. Auth is bearer token or HMAC-SHA256 request signing; writes support an idempotency_key. Chert is a Y Combinator (Spring 2026) company based in the San Francisco Bay Area.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chert.png
layout: provider
mcp_servers:
- description: ''
  name: chert-mcp.yml
  slug: chert-mcpyml
modified: '2026-07-18'
name: Chert
nav: Providers
network: true
overview: 'Chert publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Messaging, iMessage, Communications, and Conversational.


  The Chert catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Chert''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, authentication, and 14 more developer resources.'
random_paper: 42
score:
  band: thin
  composite: 40.2
  delta: 3.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 36.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 27.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chert/refs/heads/main/screenshots/chert-2026-07-25T205203.png
security:
- kind: authentication
  name: Chert Authentication
  slug: chert-authentication
  summary_line: http/hmac · 2 schemes
- kind: domain-security
  name: Chert Domain Security
  slug: chert-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chert
tags:
- Company
- Messaging
- iMessage
- Communications
- Conversational
- Webhooks
- CRM Integration
- API
website: https://console.trychert.com
---
