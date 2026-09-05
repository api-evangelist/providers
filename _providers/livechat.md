---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 35
  human_in_the_loop: 0
  name: Livechat Agentic Access
  operation_count: 35
  slug: livechat-agentic-access
  summary_line: 35 operations · 35 acting
api_count: 1
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
- baseURL: https://api.livechatinc.com/v3.5/agent
  baseurl_source: declared
  description: The Chats API from LiveChat — 12 operation(s) for chats.
  name: LiveChat Chats API
  slug: livechat-chats-api
- baseURL: https://api.livechatinc.com/v3.5/agent
  baseurl_source: declared
  description: The Customers API from LiveChat — 3 operation(s) for customers.
  name: LiveChat Customers API
  slug: livechat-customers-api
- baseURL: https://api.livechatinc.com/v3.5/agent
  baseurl_source: declared
  description: The Events API from LiveChat — 5 operation(s) for events.
  name: LiveChat Events API
  slug: livechat-events-api
- baseURL: https://api.livechatinc.com/v3.5/agent
  baseurl_source: declared
  description: The Other API from LiveChat — 3 operation(s) for other.
  name: LiveChat Other API
  slug: livechat-other-api
- baseURL: https://api.livechatinc.com/v3.5/agent
  baseurl_source: declared
  description: The Properties API from LiveChat — 6 operation(s) for properties.
  name: LiveChat Properties API
  slug: livechat-properties-api
- baseURL: https://api.livechatinc.com/v3.5/agent
  baseurl_source: declared
  description: The Status API from LiveChat — 2 operation(s) for status.
  name: LiveChat Status API
  slug: livechat-status-api
- baseURL: https://api.livechatinc.com/v3.5/agent
  baseurl_source: declared
  description: The Threads API from LiveChat — 4 operation(s) for threads.
  name: LiveChat Threads API
  slug: livechat-threads-api
artifact_total: 25
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LiveChat Webhooks and RTM API
  slug: open-livechat-asyncapi
- collection_type: open
  name: LiveChat Agent Chat Chats API
  slug: open-livechat-chats-api
- collection_type: open
  name: LiveChat Agent Chat Chats Customers API
  slug: open-livechat-customers-api
- collection_type: open
  name: LiveChat Agent Chat Chats Events API
  slug: open-livechat-events-api
- collection_type: open
  name: LiveChat Agent Chat Chats Other API
  slug: open-livechat-other-api
- collection_type: open
  name: LiveChat Agent Chat Chats Properties API
  slug: open-livechat-properties-api
- collection_type: open
  name: LiveChat Agent Chat Chats Status API
  slug: open-livechat-status-api
- collection_type: open
  name: LiveChat Agent Chat Chats Threads API
  slug: open-livechat-threads-api
- collection_type: open
  name: LiveChat Agent Chat API
  slug: open-livechat
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/livechat-capability-edges.yml
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
overview: 'LiveChat publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Webhooks and RTM API, Chats API, Customers API, and 5 more. Tagged areas include Live Chat, Customer Service, Customer-Support, Messaging, and Sales.


  LiveChat''s developer surface includes authentication, documentation, developer console, signup flow, pricing, engineering blog, and 6 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 59.0
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 32.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
- Customer-Support
- Messaging
- Sales
- Help Desk
website: https://www.livechat.com
---
