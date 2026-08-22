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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.2
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Pushbullet Agentic Access
  operation_count: 23
  slug: pushbullet-agentic-access
  summary_line: 23 operations · 17 acting
api_count: 11
apis:
- description: 'REST API for sending and managing pushes, devices, chats, channels, subscriptions, and file uploads across the Pushbullet ecosystem. Authentication uses an access token from account settings supplied '
  name: Pushbullet HTTP API
  slug: http-api
- description: Secure WebSocket stream that delivers realtime events to a Pushbullet account, including periodic `nop` keep-alives, `tickle` notifications that signal changes to pushes or devices, and `push` ephemer
  name: Pushbullet Realtime Event Stream
  slug: realtime-event-stream
- description: The Channels API from Pushbullet — 2 operation(s) for channels.
  name: Pushbullet Channels API
  slug: pushbullet-channels-api
- description: The Chats API from Pushbullet — 2 operation(s) for chats.
  name: Pushbullet Chats API
  slug: pushbullet-chats-api
- description: The Devices API from Pushbullet — 2 operation(s) for devices.
  name: Pushbullet Devices API
  slug: pushbullet-devices-api
- description: The Ephemerals API from Pushbullet — 1 operation(s) for ephemerals.
  name: Pushbullet Ephemerals API
  slug: pushbullet-ephemerals-api
- description: The Pushes API from Pushbullet — 2 operation(s) for pushes.
  name: Pushbullet Pushes API
  slug: pushbullet-pushes-api
- description: The Subscriptions API from Pushbullet — 2 operation(s) for subscriptions.
  name: Pushbullet Subscriptions API
  slug: pushbullet-subscriptions-api
- description: The Texts API from Pushbullet — 1 operation(s) for texts.
  name: Pushbullet Texts API
  slug: pushbullet-texts-api
- description: The Upload API from Pushbullet — 1 operation(s) for upload.
  name: Pushbullet Upload API
  slug: pushbullet-upload-api
- description: The Users API from Pushbullet — 1 operation(s) for users.
  name: Pushbullet Users API
  slug: pushbullet-users-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Pushbullet Realtime Event Stream
  slug: open-pushbullet-asyncapi
- collection_type: open
  name: Pushbullet HTTP Channels API
  slug: open-pushbullet-channels-api
- collection_type: open
  name: Pushbullet HTTP Channels Chats API
  slug: open-pushbullet-chats-api
- collection_type: open
  name: Pushbullet HTTP Channels Devices API
  slug: open-pushbullet-devices-api
- collection_type: open
  name: Pushbullet HTTP Channels Ephemerals API
  slug: open-pushbullet-ephemerals-api
- collection_type: open
  name: Pushbullet HTTP Channels Pushes API
  slug: open-pushbullet-pushes-api
- collection_type: open
  name: Pushbullet HTTP Channels Subscriptions API
  slug: open-pushbullet-subscriptions-api
- collection_type: open
  name: Pushbullet HTTP Channels Texts API
  slug: open-pushbullet-texts-api
- collection_type: open
  name: Pushbullet HTTP Channels Upload API
  slug: open-pushbullet-upload-api
- collection_type: open
  name: Pushbullet HTTP Channels Users API
  slug: open-pushbullet-users-api
- collection_type: open
  name: Pushbullet HTTP API
  slug: open-pushbullet
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pushbullet-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pushbullet-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pushbullet-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pushbullet-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pushbullet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pushbullet
- group: company
  title: ''
  type: Website
  url: https://www.pushbullet.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pushbullet.com
- group: start
  title: ''
  type: Signup
  url: https://www.pushbullet.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pushbullet.com/pro
- group: other
  title: ''
  type: Account Settings
  url: https://www.pushbullet.com/#settings/account
- group: operate
  title: ''
  type: Help
  url: https://help.pushbullet.com
- group: company
  title: ''
  type: Blog
  url: http://blog.pushbullet.com/feed.xml
created: '2026-05-11'
description: Pushbullet is a cross-device messaging and notification service that lets users sync notifications, links, files, and SMS between phones, tablets, and computers. The Pushbullet HTTP API enables developers to send pushes, manage devices and contacts, transfer files, subscribe to channels, and stream real-time events over WebSockets. Authentication uses access tokens passed in the `Access-Token` header, with optional OAuth 2.0 for third-party applications.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pushbullet.png
layout: provider
modified: '2026-05-30'
name: Pushbullet
nav: Providers
network: true
overview: 'Pushbullet publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Realtime Event Stream, Channels API, Chats API, and 7 more. Tagged areas include Notifications, Messaging, Push Notifications, Device Sync, and SMS.


  Pushbullet''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, and 8 more developer resources.'
random_paper: 4
scopes:
- name: Pushbullet Scopes
  scope_count: 1
  slug: pushbullet-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 34.0
  delta: 0.4
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 60.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 40.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pushbullet/refs/heads/main/screenshots/pushbullet-2026-06-20T192316.png
security:
- kind: authentication
  name: Pushbullet Authentication
  slug: pushbullet-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Pushbullet Domain Security
  slug: pushbullet-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pushbullet
tags:
- Notifications
- Messaging
- Push Notifications
- Device Sync
- SMS
- File Transfer
website: https://www.pushbullet.com
---
