---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API for the Splash event marketing platform. Enables programmatic management of events, guest (GroupContact) records, organization-level contacts, ticketing, check-in, and event analytics. Authen
  name: Splash API
  slug: splash-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/splashthat-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.splashthat.com/
- group: operate
  title: ''
  type: Support
  url: https://support.splashthat.com/
- group: company
  title: ''
  type: Blog
  url: https://splashthat.com/blog
- group: company
  title: ''
  type: Press
  url: https://splashthat.com/press
- group: commercial
  title: ''
  type: Pricing
  url: https://splashthat.com/pricing
- group: operate
  title: ''
  type: Status
  url: https://status.cvent.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://splashthat.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://splashthat.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://splashthat.com/security
- group: operate
  title: ''
  type: RateLimits
  url: https://support.splashthat.com/hc/en-us/articles/13759878758541-What-is-API-rate-limiting-and-what-are-the-benefits-and-impacts
created: '2026-06-13'
description: Splash is an event marketing platform that helps companies market, manage, and measure their live, virtual, and hybrid event programs. The Splash REST API enables brands and agencies to programmatically manage events, handle guest registration, process check-in, and pull event analytics. API access uses OAuth 2.0 client credentials and covers resources such as events, group contacts (guests), contacts, and ticketing.
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/splashthat.png
jsonld:
- class_count: 14
  name: Splashthat Context
  property_count: 15
  slug: splashthat-context
layout: provider
modified: '2026-06-13'
name: Splash
nav: Providers
network: true
overview: 'Splash publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Events, Event Marketing, Event Management, Guest Registration, and Ticketing.


  The Splash catalog on APIs.io includes 1 JSON-LD context.


  Splash''s developer surface includes documentation, support, engineering blog, pricing, status page, and 6 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 31
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: thin
  composite: 38.0
  delta: -4.5
  facets:
    commercial_clarity: 71.1
    contract_quality: 50.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 42.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/splashthat/refs/heads/main/screenshots/splashthat-2026-06-20T194323.png
security:
- kind: domain-security
  name: Splashthat Domain Security
  slug: splashthat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: splashthat
tags:
- Events
- Event Marketing
- Event Management
- Guest Registration
- Ticketing
- Check-In
- Analytics
---
