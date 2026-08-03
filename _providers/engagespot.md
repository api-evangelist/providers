---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: The Engagespot REST API enables sending multi-channel notifications to users, listing and deleting notification records, managing user accounts and preferences, triggering and canceling notification w
  name: Engagespot Notifications API
  slug: notifications-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/engagespot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://engagespot.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.engagespot.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Engagespot
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/engagespot-co
- group: other
  title: ''
  type: X
  url: https://x.com/engagespot
- group: company
  title: ''
  type: Blog
  url: https://engagespot.co/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://engagespot.co/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://engagespot.statuspage.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/engagespot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/engagespot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/engagespot-finops.yml
created: '2026-06-12'
description: Engagespot is a notification infrastructure platform that provides developers with a unified REST API to send multi-channel notifications including in-app, email, web push, mobile push, SMS, WhatsApp, Slack, Discord, and webhooks from a single integration. The platform includes a pre-built customizable in-app notification inbox, a visual workflow editor for complex messaging logic, and a fine-grained user preference management system. Engagespot handles over 850 million monthly notifications and 3.7 billion API requests with 99.98% uptime, supporting data residency in both US and EU regions. Teams can manage notification templates, monitor delivery logs, and connect to third-party providers such as SendGrid, AWS SES, Firebase, Twilio, and APNS through a centralized dashboard.
finops:
- name: Engagespot Finops
  service_category: ''
  slug: engagespot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/engagespot.png
jsonld:
- class_count: 15
  name: Engagespot Context
  property_count: 7
  slug: engagespot-context
layout: provider
modified: '2026-06-12'
name: Engagespot
nav: Providers
network: true
overview: 'Engagespot publishes 1 API on the [APIs.io](https://apis.io/) network: Notifications API. Tagged areas include Notifications, In-App Notifications, Push Notifications, Email, and SMS.


  The Engagespot catalog on APIs.io includes 1 JSON-LD context.


  Engagespot''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Engagespot Plans Pricing
  plan_count: 3
  slug: engagespot-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 3
  name: Engagespot Rate Limits
  slug: engagespot-rate-limits
score:
  band: thin
  composite: 33.9
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 33.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 15.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/engagespot/refs/heads/main/screenshots/engagespot-2026-06-20T180716.png
security:
- kind: domain-security
  name: Engagespot Domain Security
  slug: engagespot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: engagespot
tags:
- Notifications
- In-App Notifications
- Push Notifications
- Email
- SMS
- Multi-Channel
- Messaging
- Developer Tools
- Notification Infrastructure
website: https://engagespot.co/
---
