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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Livechat Agentic Access
  operation_count: 35
  slug: livechat-agentic-access
  summary_line: 35 operations · 35 acting
api_count: 12
apis:
- description: REST and RTM APIs for agents to manage chats, send messages, transfer conversations, and update statuses. Authenticated with OAuth 2.1 bearer tokens or Personal Access Tokens.
  name: LiveChat Agent Chat API
  slug: agent-chat-api
- description: REST and RTM APIs for customers to start and participate in chats with agents on LiveChat-powered websites. Uses customer access tokens.
  name: LiveChat Customer Chat API
  slug: customer-chat-api
- description: Manage agents, groups, bots, tags, webhooks, properties, and other account configuration for a LiveChat organization.
  name: LiveChat Configuration API
  slug: configuration-api
- description: Asynchronous event surfaces for LiveChat. HTTP webhooks registered through the Configuration API and the Agent Chat Real-Time Messaging (RTM) WebSocket API share the same event payloads (incoming_chat
  name: LiveChat Webhooks and RTM API
  slug: webhooks-and-rtm
- description: Retrieve reporting data for chats, agents, tags, and customer activity across the LiveChat organization.
  name: LiveChat Reports API
  slug: reports-api
- description: The Chats API from LiveChat — 12 operation(s) for chats.
  name: LiveChat Chats API
  slug: livechat-chats-api
- description: The Customers API from LiveChat — 3 operation(s) for customers.
  name: LiveChat Customers API
  slug: livechat-customers-api
- description: The Events API from LiveChat — 5 operation(s) for events.
  name: LiveChat Events API
  slug: livechat-events-api
- description: The Other API from LiveChat — 3 operation(s) for other.
  name: LiveChat Other API
  slug: livechat-other-api
- description: The Properties API from LiveChat — 6 operation(s) for properties.
  name: LiveChat Properties API
  slug: livechat-properties-api
- description: The Status API from LiveChat — 2 operation(s) for status.
  name: LiveChat Status API
  slug: livechat-status-api
- description: The Threads API from LiveChat — 4 operation(s) for threads.
  name: LiveChat Threads API
  slug: livechat-threads-api
artifact_total: 17
collections:
- collection_type: open
  name: LiveChat Webhooks and RTM API
  slug: open-livechat-asyncapi
- collection_type: open
  name: LiveChat Agent Chat API
  slug: open-livechat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/livechat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/livechat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/livechat-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/livechatcom
- group: company
  title: ''
  type: Website
  url: https://www.livechat.com
- group: docs
  title: ''
  type: Documentation
  url: https://platform.text.com/docs
- group: start
  title: ''
  type: Console
  url: https://developers.livechat.com/console
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/livechat
- group: start
  title: ''
  type: Signup
  url: https://accounts.livechat.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.livechat.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.livechat.com/success/
created: '2026-05-11'
description: LiveChat is a customer service and live chat platform used by businesses to engage website visitors, run sales conversations, and route support tickets across agent teams. The Text Platform (which powers LiveChat) exposes a suite of REST APIs for chats, agents, customers, configuration, and reporting, with both Web API and RTM (real-time messaging) interfaces. Authentication uses OAuth 2.1 with Personal Access Tokens or full OAuth authorization code flow.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/livechat.png
layout: provider
modified: '2026-05-30'
name: LiveChat
nav: Providers
network: true
overview: 'LiveChat publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Webhooks and RTM API, Chats API, Customers API, and 5 more. Tagged areas include Live Chat, Customer Service, Customer Support, Messaging, and Sales.


  LiveChat''s developer surface includes authentication, documentation, developer console, signup flow, pricing, engineering blog, and 5 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 34.5
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 64.1
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 34.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/livechat/refs/heads/main/screenshots/livechat-2026-06-20T184613.png
security:
- kind: authentication
  name: Livechat Authentication
  slug: livechat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Livechat Domain Security
  slug: livechat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: livechat
tags:
- Live Chat
- Customer Service
- Customer Support
- Messaging
- Sales
- Help Desk
website: https://www.livechat.com
---
