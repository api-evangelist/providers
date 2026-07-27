---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 37.5
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Pushover Agentic Access
  operation_count: 6
  slug: pushover-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 6
apis:
- description: Real-time client API for Pushover. Combines a WebSocket channel at wss://client.pushover.net/push that streams single-byte control frames (`#` keepalive, `!` new message, `R` reload, `E` permanent err
  name: Pushover Open Client API
  slug: open-client-api
- description: The Apps API from Pushover — 1 operation(s) for apps.
  name: Pushover Apps API
  slug: pushover-apps-api
- description: The Messages.json API from Pushover — 1 operation(s) for messages.json.
  name: Pushover Messages.json API
  slug: pushover-messages-json-api
- description: The Receipts API from Pushover — 2 operation(s) for receipts.
  name: Pushover Receipts API
  slug: pushover-receipts-api
- description: The Sounds.json API from Pushover — 1 operation(s) for sounds.json.
  name: Pushover Sounds.json API
  slug: pushover-sounds-json-api
- description: The Users API from Pushover — 1 operation(s) for users.
  name: Pushover Users API
  slug: pushover-users-api
artifact_total: 10
collections:
- collection_type: open
  name: Pushover Open Client API
  slug: open-pushover-asyncapi
- collection_type: open
  name: Pushover Message API
  slug: open-pushover
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pushover-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pushover-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pushoverapp
- group: company
  title: ''
  type: Website
  url: https://pushover.net
- group: docs
  title: ''
  type: Documentation
  url: https://pushover.net/api
- group: commercial
  title: ''
  type: Pricing
  url: https://pushover.net/pricing
- group: start
  title: ''
  type: Signup
  url: https://pushover.net/signup
- group: operate
  title: ''
  type: FAQ
  url: https://pushover.net/faq
- group: operate
  title: ''
  type: Support
  url: https://pushover.net/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pushover.net
- group: company
  title: ''
  type: Blog
  url: https://blog.pushover.net/rss
created: '2026-05-11'
description: Pushover is a simple push notification service that delivers real-time notifications to phones, tablets, desktops, and watches from servers, scripts, and applications. The Pushover Message API accepts HTTPS POSTs with an application token and user/group key to send formatted messages with priorities, sounds, images, and supplementary URLs. Additional APIs exist for groups, subscriptions, licensing, receipts, and Open Client.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pushover.png
layout: provider
modified: '2026-05-30'
name: Pushover
nav: Providers
network: true
overview: 'Pushover publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Open Client API, Apps API, Messages.json API, and 3 more. Tagged areas include Notifications, Push Notifications, Messaging, Alerts, and Monitoring.


  Pushover''s developer surface includes documentation, pricing, signup flow, FAQ, support, engineering blog, and 5 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 32.3
  delta: 3.3
  facets:
    commercial_clarity: 10.5
    contract_quality: 57.5
    developer_ergonomics: 15.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pushover/refs/heads/main/screenshots/pushover-2026-06-20T192319.png
security:
- kind: domain-security
  name: Pushover Domain Security
  slug: pushover-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pushover
tags:
- Notifications
- Push Notifications
- Messaging
- Alerts
- Monitoring
website: https://pushover.net
---
