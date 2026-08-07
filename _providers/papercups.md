---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.0
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Papercups Agentic Access
  operation_count: 15
  slug: papercups-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 7
apis:
- description: Outbound event subscriptions delivered as webhooks (message:created, conversation:created, conversation:updated, and a webhook:verify challenge handshake) notifying external systems of activity.
  name: Papercups Notifications & Webhooks API
  slug: notifications
- description: Bidirectional realtime live chat over Phoenix WebSocket channels. Clients join conversation, conversation-lobby, and account-room channels and exchange shout (message), messages:seen, and presence eve
  name: Papercups Realtime Chat API (WebSocket / Phoenix Channels)
  slug: realtime-chat
- description: Register external HTTPS endpoints to receive Papercups events as POSTed JSON payloads of shape { event, payload }, with a verify-challenge handshake on registration.
  name: Papercups Webhooks
  slug: webhooks
- description: Threads of messages between customers and agents.
  name: Papercups Conversations API
  slug: papercups-conversations-api
- description: Customer records (users, leads, or contacts).
  name: Papercups Customers API
  slug: papercups-customers-api
- description: Individual messages within conversations.
  name: Papercups Messages API
  slug: papercups-messages-api
- description: Authenticated user and team members.
  name: Papercups Users API
  slug: papercups-users-api
artifact_total: 16
asyncapis:
- description: 'AsyncAPI 2.6 description of Papercups'' **realtime live chat** surface. Unlike many providers, Papercups exposes a genuine, bidirectional **WebSocket** transport: the chat widget and agent dashboard co'
  name: Papercups Realtime Chat (WebSocket / Phoenix Channels)
  slug: papercups-asyncapi
collections:
- collection_type: open
  name: Papercups API
  slug: open-papercups
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/papercups-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/papercups-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/papercups-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/papercups-io
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/papercups
- group: company
  title: ''
  type: Website
  url: https://papercups.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.papercups.io
- group: commercial
  title: ''
  type: Plans
  url: plans/papercups-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/papercups-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/papercups-finops.yml
created: '2026-06-20'
description: Papercups is an open-source customer-messaging and live-chat platform built on Elixir/Phoenix, positioned as a self-hosted alternative to Intercom. It exposes a REST API for conversations, messages, and customers, a realtime chat surface over Phoenix WebSocket channels, and outbound webhooks. The project is in maintenance mode (community-maintained, no major new features).
finops:
- name: Papercups Finops
  service_category: Customer Engagement and Support
  slug: papercups-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/papercups.png
layout: provider
modified: '2026-06-20'
name: Papercups
nav: Providers
network: true
overview: 'Papercups publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Realtime Chat API (WebSocket / Phoenix Channels), Conversations API, Customers API, and 2 more. Tagged areas include Customer Messaging, Live Chat, Open Source, Support, and Intercom Alternative.


  The Papercups catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Papercups'' developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Papercups Plans Pricing
  plan_count: 2
  slug: papercups-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 3
  name: Papercups Rate Limits
  slug: papercups-rate-limits
rules:
- name: Papercups API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: papercups-asyncapi-spectral-rules
score:
  band: developing
  composite: 42.7
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 63.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/papercups/refs/heads/main/screenshots/papercups-2026-06-20T191348.png
security:
- kind: authentication
  name: Papercups Authentication
  slug: papercups-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Papercups Domain Security
  slug: papercups-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: papercups
tags:
- Customer Messaging
- Live Chat
- Open Source
- Support
- Intercom Alternative
website: https://papercups.io
---
