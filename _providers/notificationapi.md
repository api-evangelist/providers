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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Notificationapi Agentic Access
  operation_count: 12
  slug: notificationapi-agentic-access
  summary_line: 12 operations · 11 acting
api_count: 7
apis:
- description: Read and update a user's in-app (INAPP_WEB) notifications.
  name: NotificationAPI In-App Inbox API
  slug: notificationapi-in-app-inbox-api
- description: Query delivery and event logs.
  name: NotificationAPI Logs API
  slug: notificationapi-logs-api
- description: Configure notifications and their subNotifications.
  name: NotificationAPI Notifications API
  slug: notificationapi-notifications-api
- description: Update or delete scheduled notifications.
  name: NotificationAPI Schedule API
  slug: notificationapi-schedule-api
- description: Send and retract notifications across channels.
  name: NotificationAPI Send API
  slug: notificationapi-send-api
- description: Read and write per-user channel and opt-out preferences.
  name: NotificationAPI User Preferences API
  slug: notificationapi-user-preferences-api
- description: Identify and manage the users you notify.
  name: NotificationAPI Users API
  slug: notificationapi-users-api
artifact_total: 14
collections:
- collection_type: open
  name: NotificationAPI REST API
  slug: open-notificationapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/notificationapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/notificationapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/notificationapi-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.pingram.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/notificationapi-com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/notificationapi
- group: company
  title: ''
  type: Website
  url: https://www.notificationapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.notificationapi.com
- group: commercial
  title: ''
  type: Plans
  url: plans/notificationapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/notificationapi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/notificationapi-finops.yml
created: '2026-07-01'
description: NotificationAPI is notifications infrastructure for developers. A single REST API and drop-in in-app inbox component send multi-channel notifications - email, SMS, mobile and web push, in-app inbox, automated voice call, and Slack - while managing user identities, per-user preferences and opt-outs, templates, scheduling, and delivery logs. All calls are scoped to a clientId and authenticated with HTTP Basic auth.
finops:
- name: Notificationapi Finops
  service_category: Developer Tools and Messaging
  slug: notificationapi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/notificationapi.png
layout: provider
modified: '2026-07-01'
name: NotificationAPI
nav: Providers
network: true
overview: 'NotificationAPI publishes 7 APIs on the [APIs.io](https://apis.io/) network, including In-App Inbox API, Logs API, Notifications API, and 4 more. Tagged areas include Notifications, Messaging, Email, SMS, and Push.


  NotificationAPI''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Notificationapi Plans Pricing
  plan_count: 4
  slug: notificationapi-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Notificationapi Rate Limits
  slug: notificationapi-rate-limits
score:
  band: thin
  composite: 36.2
  delta: -5.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
security:
- kind: authentication
  name: Notificationapi Authentication
  slug: notificationapi-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Notificationapi Domain Security
  slug: notificationapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: notificationapi
tags:
- Notifications
- Messaging
- Email
- SMS
- Push
- In-App Inbox
website: https://www.notificationapi.com/
---
