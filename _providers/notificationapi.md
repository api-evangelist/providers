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
  - '{''url'': ''https://www.notificationapi.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.pingram.io/ — a different registrable domain (notificationapi.com -> pingram.io), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: true
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Notificationapi Agentic Access
  operation_count: 12
  slug: notificationapi-agentic-access
  summary_line: 12 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.notificationapi.com/{clientId}
  baseurl_source: declared
  description: Read and update a user's in-app (INAPP_WEB) notifications.
  name: NotificationAPI In-App Inbox API
  slug: notificationapi-in-app-inbox-api
- baseURL: https://api.notificationapi.com/{clientId}
  baseurl_source: declared
  description: Query delivery and event logs.
  name: NotificationAPI Logs API
  slug: notificationapi-logs-api
- baseURL: https://api.notificationapi.com/{clientId}
  baseurl_source: declared
  description: Configure notifications and their subNotifications.
  name: NotificationAPI Notifications API
  slug: notificationapi-notifications-api
- baseURL: https://api.notificationapi.com/{clientId}
  baseurl_source: declared
  description: Update or delete scheduled notifications.
  name: NotificationAPI Schedule API
  slug: notificationapi-schedule-api
- baseURL: https://api.notificationapi.com/{clientId}
  baseurl_source: declared
  description: Send and retract notifications across channels.
  name: NotificationAPI Send API
  slug: notificationapi-send-api
- baseURL: https://api.notificationapi.com/{clientId}
  baseurl_source: declared
  description: Read and write per-user channel and opt-out preferences.
  name: NotificationAPI User Preferences API
  slug: notificationapi-user-preferences-api
- baseURL: https://api.notificationapi.com/{clientId}
  baseurl_source: declared
  description: Identify and manage the users you notify.
  name: NotificationAPI Users API
  slug: notificationapi-users-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NotificationAPI REST In-App Inbox API
  slug: open-notificationapi-in-app-inbox-api
- collection_type: open
  name: NotificationAPI REST In-App Inbox Logs API
  slug: open-notificationapi-logs-api
- collection_type: open
  name: NotificationAPI REST In-App Inbox Notifications API
  slug: open-notificationapi-notifications-api
- collection_type: open
  name: NotificationAPI REST In-App Inbox Schedule API
  slug: open-notificationapi-schedule-api
- collection_type: open
  name: NotificationAPI REST In-App Inbox Send API
  slug: open-notificationapi-send-api
- collection_type: open
  name: NotificationAPI REST In-App Inbox User Preferences API
  slug: open-notificationapi-user-preferences-api
- collection_type: open
  name: NotificationAPI REST In-App Inbox Users API
  slug: open-notificationapi-users-api
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
overview: 'NotificationAPI publishes 7 APIs on the [APIs.io](https://apis.io/) network, including In-App Inbox API, Logs API, Notifications API, and 4 more. Tagged areas include Notification, Messaging, Email, SMS, and Push.


  NotificationAPI''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Notificationapi Plans Pricing
  plan_count: 4
  slug: notificationapi-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Notificationapi Rate Limits
  slug: notificationapi-rate-limits
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 10
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 56.5
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.6
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/notificationapi/refs/heads/main/screenshots/notificationapi-2026-08-07T185548.png
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
- Notification
- Messaging
- Email
- SMS
- Push
- In-App Inbox
website: https://www.notificationapi.com/
---
