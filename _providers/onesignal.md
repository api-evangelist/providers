---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: The Apps API from OneSignal — 21 operation(s) for apps.
  name: OneSignal Apps API
  slug: onesignal-apps-api
- description: The Notifications API from OneSignal — 4 operation(s) for notifications.
  name: OneSignal Notifications API
  slug: onesignal-notifications-api
- description: The Players API from OneSignal — 1 operation(s) for players.
  name: OneSignal Players API
  slug: onesignal-players-api
- description: The Templates API from OneSignal — 3 operation(s) for templates.
  name: OneSignal Templates API
  slug: onesignal-templates-api
artifact_total: 11
collections:
- collection_type: open
  name: OneSignal
  slug: open-onesignal
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/onesignal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/onesignal-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OneSignal
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onesignal
- group: company
  title: ''
  type: Website
  url: https://onesignal.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/onesignal-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/onesignal-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/onesignal-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://onesignal.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://onesignal.com/blog/feed
created: '2026-05-08'
description: OneSignal is a customer engagement platform with push notifications, in-app messaging, email, SMS, and live activities. Free tier serves billions of messages monthly.
finops:
- name: Onesignal Finops
  service_category: Notifications
  slug: onesignal-finops
graphqls:
- description: Conceptual GraphQL schema for the OneSignal multi-channel customer engagement platform, derived from the OneSignal REST API v1 (https://documentation.onesignal.com/reference).
  name: OneSignal GraphQL Schema
  slug: onesignal-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onesignal.png
layout: provider
modified: '2026-05-08'
name: OneSignal
nav: Providers
network: true
overview: 'OneSignal publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Notifications API, Players API, and 1 more. Tagged areas include Notifications, Push, Email, SMS, and Mobile.


  OneSignal''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: Onesignal Plans Pricing
  plan_count: 1
  slug: onesignal-plans-pricing
random_paper: 42
rate_limits:
- limit_count: 1
  name: Onesignal Rate Limits
  slug: onesignal-rate-limits
score:
  band: thin
  composite: 30.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.8
    developer_ergonomics: 2.2
    discoverability: 55.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 30.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/onesignal/refs/heads/main/screenshots/onesignal-2026-06-20T190717.png
security:
- kind: domain-security
  name: Onesignal Domain Security
  slug: onesignal-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Onesignal Vulnerability Disclosure
  slug: onesignal-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: onesignal
tags:
- Notifications
- Push
- Email
- SMS
- Mobile
website: https://onesignal.com/
---
