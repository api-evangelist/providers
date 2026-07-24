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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Novu Co Agentic Access
  operation_count: 49
  slug: novu-co-agentic-access
  summary_line: 49 operations · 32 acting
api_count: 13
apis:
- description: Real-time WebSocket (Socket.IO) surface that pushes live Inbox updates to browser and mobile clients - notification_received, unseen_count_changed, and unread_count_changed events - authenticated by s
  name: Novu Inbox Realtime API
  slug: novu-co-inbox-realtime-api
- description: Environments and resource promotion.
  name: Novu Environments API
  slug: novu-co-environments-api
- description: Trigger, bulk trigger, broadcast, and cancel workflow executions.
  name: Novu Events API
  slug: novu-co-events-api
- description: The in-app notification feed for a subscriber.
  name: Novu Inbox API
  slug: novu-co-inbox-api
- description: Channel provider configurations.
  name: Novu Integrations API
  slug: novu-co-integrations-api
- description: Reusable email layout wrappers.
  name: Novu Layouts API
  slug: novu-co-layouts-api
- description: Individual channel messages produced by workflow executions.
  name: Novu Messages API
  slug: novu-co-messages-api
- description: Activity feed of triggered workflow executions (events).
  name: Novu Notifications API
  slug: novu-co-notifications-api
- description: Per-subscriber notification preferences.
  name: Novu Preferences API
  slug: novu-co-preferences-api
- description: Manage notification recipients and their credentials.
  name: Novu Subscribers API
  slug: novu-co-subscribers-api
- description: Group subscribers into addressable audiences.
  name: Novu Topics API
  slug: novu-co-topics-api
- description: Localization of notification content.
  name: Novu Translations API
  slug: novu-co-translations-api
- description: Multi-channel notification workflow definitions.
  name: Novu Workflows API
  slug: novu-co-workflows-api
artifact_total: 22
asyncapis:
- description: 'AsyncAPI 2.6 description of Novu''s **Inbox real-time WebSocket** surface - the connection that powers the live bell, counts, and feed of Novu''s embeddable in-app `<Inbox>` notification center. Unlike '
  name: Novu Inbox Realtime (WebSocket / Socket.IO)
  slug: novu-co-asyncapi
collections:
- collection_type: open
  name: Novu API
  slug: open-novu-co
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/novu-co-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/novu-co-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/novu-co-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/novuhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/novuco
- group: company
  title: ''
  type: Website
  url: https://novu.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.novu.co
- group: commercial
  title: ''
  type: Plans
  url: plans/novu-co-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/novu-co-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/novu-co-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://novu.co/blog/rss.xml
created: '2026-07-02'
description: Novu is open-source notification infrastructure that sends multi-channel messages - email, SMS, push, chat, and an in-app Inbox - from a single workflow trigger. A single event API call fans a notification out across channels defined in a workflow, with subscriber management, topics, layouts, digest/aggregation, 55+ provider integrations, and a real-time embeddable Inbox notification center powered by a WebSocket connection. Novu is self-hostable (MIT) and also available as Novu Cloud, with US (api.novu.co) and EU (eu.api.novu.co) regions.
finops:
- name: Novu Co Finops
  service_category: Notifications and Messaging
  slug: novu-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/novu-co.png
layout: provider
modified: '2026-07-02'
name: Novu
nav: Providers
network: true
overview: 'Novu publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Inbox Realtime API, Environments API, Events API, and 10 more. Tagged areas include Notifications, Multi-Channel, Email, SMS, and Push.


  The Novu catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Novu''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Novu Co Plans Pricing
  plan_count: 5
  slug: novu-co-plans-pricing
random_paper: 48
rate_limits:
- limit_count: 13
  name: Novu Co Rate Limits
  slug: novu-co-rate-limits
rules:
- name: Novu API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: novu-co-asyncapi-spectral-rules
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.4
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 73.7
    operational_transparency: 36.8
  previous_composite: 48.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Novu Co Authentication
  slug: novu-co-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Novu Co Domain Security
  slug: novu-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: novu-co
tags:
- Notifications
- Multi-Channel
- Email
- SMS
- Push
- Chat
- In-App Inbox
- Open Source
- WebSocket
website: https://novu.co/
---
