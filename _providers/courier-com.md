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
    asyncapi_events: false
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
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Courier Com Agentic Access
  operation_count: 60
  slug: courier-com-agentic-access
  summary_line: 60 operations · 32 acting
api_count: 14
apis:
- description: Dynamic audiences defined by profile filters.
  name: Courier Audiences API
  slug: courier-com-audiences-api
- description: Workspace audit events.
  name: Courier Audit Events API
  slug: courier-com-audit-events-api
- description: Multi-step notification workflows.
  name: Courier Automations API
  slug: courier-com-automations-api
- description: Reusable logos, colors, and email styling.
  name: Courier Brands API
  slug: courier-com-brands-api
- description: One-to-many sends via jobs.
  name: Courier Bulk API
  slug: courier-com-bulk-api
- description: Push notification device tokens for a user.
  name: Courier Device Tokens API
  slug: courier-com-device-tokens-api
- description: Subscription lists and their subscribers.
  name: Courier Lists API
  slug: courier-com-lists-api
- description: Inspect, track, cancel, and archive sent messages.
  name: Courier Messages API
  slug: courier-com-messages-api
- description: Notification templates designed in the Courier studio.
  name: Courier Notification Templates API
  slug: courier-com-notification-templates-api
- description: Dispatch a notification across channels.
  name: Courier Send API
  slug: courier-com-send-api
- description: Organizations/accounts for multi-tenant apps.
  name: Courier Tenants API
  slug: courier-com-tenants-api
- description: Localization strings per domain and locale.
  name: Courier Translations API
  slug: courier-com-translations-api
- description: Per-user, per-topic notification preferences.
  name: Courier User Preferences API
  slug: courier-com-user-preferences-api
- description: Recipient profiles keyed by your user id.
  name: Courier User Profiles API
  slug: courier-com-user-profiles-api
artifact_total: 22
collections:
- collection_type: open
  name: Courier API
  slug: open-courier-com
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/courier-com-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/courier-com-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/courier-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/courier-com-authentication.yml
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
  url: https://www.courier.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.courier.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/courier-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/courier-com-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/courier-com-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.courier.com/blog/feed
created: '2026-07-02'
description: Courier is notification infrastructure for product and engineering teams - a single API that orchestrates transactional and product messaging across email, SMS, push, chat (Slack, Teams), and an in-app inbox. One Send call routes a notification to the right channel(s) per recipient using templates designed in a visual studio, subscription topics, user preferences, brands, audiences, and automation workflows. The REST API (base https://api.courier.com) also manages users/profiles, lists, tenants for multi-tenant apps, translations, bulk sends, and audit events, and is wrapped by official server SDKs (Node, Python, Go, Ruby, PHP, Java) and a CLI.
finops:
- name: Courier Com Finops
  service_category: Notifications and Messaging
  slug: courier-com-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/courier-com.png
layout: provider
modified: '2026-07-02'
name: Courier
nav: Providers
network: true
overview: 'Courier publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Audiences API, Audit Events API, Automations API, and 11 more. Tagged areas include Notifications, Messaging, Email, SMS, and Push.


  Courier''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Courier Com Plans Pricing
  plan_count: 3
  slug: courier-com-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 5
  name: Courier Com Rate Limits
  slug: courier-com-rate-limits
score:
  band: thin
  composite: 41.4
  delta: 3.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.1
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.1
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/courier-com/refs/heads/main/screenshots/courier-com-2026-07-25T210513.png
security:
- kind: authentication
  name: Courier Com Authentication
  slug: courier-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Courier Com Domain Security
  slug: courier-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Courier Com Trust Center
  slug: courier-com-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
slug: courier-com
tags:
- Notifications
- Messaging
- Email
- SMS
- Push
- Multi-Channel
- Notification Infrastructure
- In-App Inbox
website: https://www.courier.com
---
