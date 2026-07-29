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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Airship Agentic Access
  operation_count: 29
  slug: airship-agentic-access
  summary_line: 29 operations · 16 acting
api_count: 16
apis:
- description: Send push notifications across iOS, Android and web channels.
  name: Airship Push API
  slug: airship-push-api
- description: Register, list and manage channels (devices) and named users.
  name: Airship Channels & Named Users API
  slug: airship-channels-named-users-api
- description: Create and manage segments and tags for targeting.
  name: Airship Segments API
  slug: airship-segments-api
- description: Build automated and triggered journeys across channels.
  name: Airship Automation & Journeys API
  slug: airship-automation-journeys-api
- description: Send email and SMS messages alongside push.
  name: Airship Email & SMS API
  slug: airship-email-sms-api
- description: Read message and engagement reports.
  name: Airship Reports API
  slug: airship-reports-api
- description: The Channels API from Airship — 2 operation(s) for channels.
  name: Airship Channels API
  slug: airship-channels-api
- description: The Custom Events API from Airship — 1 operation(s) for custom events.
  name: Airship Custom Events API
  slug: airship-custom-events-api
- description: The Lists API from Airship — 2 operation(s) for lists.
  name: Airship Lists API
  slug: airship-lists-api
- description: The Message Center API from Airship — 2 operation(s) for message center.
  name: Airship Message Center API
  slug: airship-message-center-api
- description: The Named Users API from Airship — 3 operation(s) for named users.
  name: Airship Named Users API
  slug: airship-named-users-api
- description: The Push API from Airship — 2 operation(s) for push.
  name: Airship Push API
  slug: airship-push-api
- description: The Reports API from Airship — 2 operation(s) for reports.
  name: Airship Reports API
  slug: airship-reports-api
- description: The Schedules API from Airship — 2 operation(s) for schedules.
  name: Airship Schedules API
  slug: airship-schedules-api
- description: The Segments API from Airship — 2 operation(s) for segments.
  name: Airship Segments API
  slug: airship-segments-api
- description: The Templates API from Airship — 2 operation(s) for templates.
  name: Airship Templates API
  slug: airship-templates-api
artifact_total: 25
collections:
- collection_type: open
  name: Airship REST API
  slug: open-airship
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airship-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/airship-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airship-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airship-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/airship-scopes.yml
- group: company
  title: ''
  type: Blog
  url: https://www.airship.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airship-social
- group: company
  title: ''
  type: Website
  url: https://www.airship.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/airship-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/airship-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/airship-finops.yml
created: '2026-05-08'
description: Airship is a mobile experience and customer engagement platform offering push, in-app, email, SMS, MMS, and feature-flagged in-app messaging across mobile and web.
finops:
- name: Airship Finops
  service_category: Notifications
  slug: airship-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/airship.png
layout: provider
modified: '2026-05-08'
name: Airship
nav: Providers
network: true
overview: 'Airship publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Push API, Segments API, Reports API, and 10 more. Tagged areas include Notifications, Push, Email, Mobile, and CDP.


  Airship''s developer surface includes authentication, engineering blog, and 9 more developer resources.'
plans:
- name: Airship Plans Pricing
  plan_count: 1
  slug: airship-plans-pricing
random_paper: 41
rate_limits:
- limit_count: 1
  name: Airship Rate Limits
  slug: airship-rate-limits
scopes:
- name: Airship Scopes
  scope_count: 11
  slug: airship-scopes
  summary_line: 11 scopes · clientCredentials
score:
  band: thin
  composite: 31.0
  delta: -1.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 53.4
    developer_ergonomics: 13.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airship/refs/heads/main/screenshots/airship-2026-06-20T171434.png
security:
- kind: authentication
  name: Airship Authentication
  slug: airship-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Airship Domain Security
  slug: airship-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Airship Vulnerability Disclosure
  slug: airship-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: airship
tags:
- Notifications
- Push
- Email
- Mobile
- CDP
website: https://www.airship.com/
---
