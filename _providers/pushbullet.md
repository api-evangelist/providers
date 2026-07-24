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
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 47.1
  scored_at: '2026-07-23'
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
artifact_total: 17
collections:
- collection_type: open
  name: Pushbullet Realtime Event Stream
  slug: open-pushbullet-asyncapi
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
random_paper: 25
scopes:
- name: Pushbullet Scopes
  scope_count: 1
  slug: pushbullet-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 29.4
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 61.9
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 29.4
  schema_version: 0.5
  scored_at: '2026-07-23'
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
