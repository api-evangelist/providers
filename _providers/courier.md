---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 60
  human_in_the_loop: 0
  name: Courier Agentic Access
  operation_count: 103
  slug: courier-agentic-access
  summary_line: 103 operations · 60 acting
api_count: 22
apis:
- description: WebSocket service that delivers Inbox messages and message-state events (read, unread, opened, archived, clicked, mark-all-read, archive-all, archive-read) to authenticated users in real time.
  name: Courier Inbox Real-Time API
  slug: courier-inbox-real-time-api
- description: The Audiences API from Courier — 3 operation(s) for audiences.
  name: Courier Audiences API
  slug: courier-audiences-api
- description: The Audit Events API from Courier — 2 operation(s) for audit events.
  name: Courier Audit Events API
  slug: courier-audit-events-api
- description: The Authentication API from Courier — 1 operation(s) for authentication.
  name: Courier Authentication API
  slug: courier-authentication-api
- description: The Automations API from Courier — 3 operation(s) for automations.
  name: Courier Automations API
  slug: courier-automations-api
- description: The Brands API from Courier — 2 operation(s) for brands.
  name: Courier Brands API
  slug: courier-brands-api
- description: The Bulk API from Courier — 4 operation(s) for bulk.
  name: Courier Bulk API
  slug: courier-bulk-api
- description: The Courier Create API from Courier — 4 operation(s) for courier create.
  name: Courier Courier Create API
  slug: courier-courier-create-api
- description: The Device Tokens API from Courier — 2 operation(s) for device tokens.
  name: Courier Device Tokens API
  slug: courier-device-tokens-api
- description: The Inbound API from Courier — 1 operation(s) for inbound.
  name: Courier Inbound API
  slug: courier-inbound-api
- description: The Journeys API from Courier — 2 operation(s) for journeys.
  name: Courier Journeys API
  slug: courier-journeys-api
- description: The Lists API from Courier — 5 operation(s) for lists.
  name: Courier Lists API
  slug: courier-lists-api
- description: The Notification Templates API from Courier — 8 operation(s) for notification templates.
  name: Courier Notification Templates API
  slug: courier-notification-templates-api
- description: The Providers API from Courier — 3 operation(s) for providers.
  name: Courier Providers API
  slug: courier-providers-api
- description: The Routing Strategies API from Courier — 3 operation(s) for routing strategies.
  name: Courier Routing Strategies API
  slug: courier-routing-strategies-api
- description: The Send API from Courier — 1 operation(s) for send.
  name: Courier Send API
  slug: courier-send-api
- description: The Sent Messages API from Courier — 6 operation(s) for sent messages.
  name: Courier Sent Messages API
  slug: courier-sent-messages-api
- description: The Tenants API from Courier — 4 operation(s) for tenants.
  name: Courier Tenants API
  slug: courier-tenants-api
- description: The Translations API from Courier — 1 operation(s) for translations.
  name: Courier Translations API
  slug: courier-translations-api
- description: The User Preferences API from Courier — 2 operation(s) for user preferences.
  name: Courier User Preferences API
  slug: courier-user-preferences-api
- description: The User Profiles API from Courier — 2 operation(s) for user profiles.
  name: Courier User Profiles API
  slug: courier-user-profiles-api
- description: The User Tenants API from Courier — 2 operation(s) for user tenants.
  name: Courier User Tenants API
  slug: courier-user-tenants-api
artifact_total: 33
asyncapis:
- description: AsyncAPI definition for Courier's Inbox WebSocket service used by the Courier client SDKs (JS, React, React Native, iOS, Android, Flutter, Web Components) to receive real-time, in-app notification eve
  name: Courier Inbox Real-Time API
  slug: courier-asyncapi
collections:
- collection_type: open
  name: Courier
  slug: open-courier
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/courier-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/courier-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/courier-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/courier-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trycourier
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trycourier
- group: company
  title: ''
  type: Website
  url: https://www.courier.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/courier-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/courier-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/courier-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.courier.com/blog/feed
created: '2026-05-08'
description: Courier is a multi-channel notification API offering routing across email, SMS, push, chat, and in-app, with templates, preferences, and a no-code studio.
finops:
- name: Courier Finops
  service_category: Notifications
  slug: courier-finops
graphqls:
- description: Courier provides a native GraphQL API in addition to its REST API. The GraphQL endpoint is available at `https://api.courier.com/graphql` and supports querying and mutating notifications, messages, re
  name: Courier GraphQL API
  slug: courier-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/courier.png
layout: provider
modified: '2026-05-29'
name: Courier
nav: Providers
network: true
overview: 'Courier publishes 22 APIs on the [APIs.io](https://apis.io/) network, including Inbox Real-Time API, Audiences API, Audit Events API, and 19 more. Tagged areas include Notifications, Email, SMS, Push, and API.


  The Courier catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Courier''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Courier Plans Pricing
  plan_count: 1
  slug: courier-plans-pricing
random_paper: 65
rate_limits:
- limit_count: 1
  name: Courier Rate Limits
  slug: courier-rate-limits
rules:
- name: Courier API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: courier-asyncapi-spectral-rules
score:
  band: thin
  composite: 40.5
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 71.6
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 47.9
    operational_transparency: 26.3
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 21
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/courier/refs/heads/main/screenshots/courier-2026-06-20T175109.png
security:
- kind: authentication
  name: Courier Authentication
  slug: courier-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Courier Domain Security
  slug: courier-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Courier Trust Center
  slug: courier-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
slug: courier
tags:
- Notifications
- Email
- SMS
- Push
- API
website: https://www.courier.com/
---
