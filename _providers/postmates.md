---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: 'The Postmates Fleet API (also referred to as the Postmates On-Demand Delivery API and Postmates Anywhere API) was a REST API that let merchants programmatically create delivery jobs, quote pickup and '
  name: Postmates Fleet API (Historical / Deprecated)
  slug: postmates-fleet-api-historical
- description: Uber Direct is the supported successor to the Postmates Fleet and Postmates Customer APIs for programmatic on-demand delivery. Merchants use Direct to quote, create, and track deliveries dispatched to
  name: Uber Direct API (Successor)
  slug: uber-direct-successor
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postmates-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postmates.com
- group: company
  title: ''
  type: About
  url: https://postmates.com/about
- group: operate
  title: ''
  type: Support
  url: https://help.uber.com/postmates
- group: other
  title: ''
  type: Announcement
  url: https://www.uber.com/newsroom/uber-completes-acquisition-of-postmates/
- group: start
  title: ''
  type: Portal
  url: https://developer.uber.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uber.com/docs/deliveries
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.uber.com/legal/en/document/?name=general-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.uber.com/legal/en/document/?name=privacy-notice
- group: other
  title: ''
  type: X
  url: https://x.com/Postmates
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Postmates
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/postmates
created: '2024-01-01'
description: Postmates was an on-demand delivery platform founded in 2011 that pioneered urban courier-style delivery of food, groceries, alcohol, and convenience goods across the United States. Uber acquired Postmates in December 2020 for approximately $2.65 billion, and by 2023 the Postmates merchant, courier, and consumer experiences were fully absorbed into the Uber Eats and Uber Direct product lines. The historical Postmates Fleet API (courier dispatch) and Postmates Customer API (anonymous delivery) have been retired and replaced by Uber Direct as the supported on-demand delivery API surface. The Postmates consumer brand still operates as a front door that funnels orders into the Uber Eats marketplace. This profile is maintained as a historical record and redirect pointer to the successor Uber developer APIs.
finops:
- name: Postmates Finops
  service_category: API
  slug: postmates-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postmates.png
layout: provider
modified: '2026-05-23'
name: Postmates
nav: Providers
network: true
overview: 'Postmates publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Acquired, Couriers, Delivery, Food Delivery, and Historical.


  Postmates'' developer surface includes support, developer portal, documentation, and 9 more developer resources.'
plans:
- name: Postmates Plans Pricing
  plan_count: 1
  slug: postmates-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 2
  name: Postmates Rate Limits
  slug: postmates-rate-limits
score:
  band: emerging
  composite: 24.7
  delta: -1.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postmates/refs/heads/main/screenshots/postmates-2026-06-20T192010.png
security:
- kind: domain-security
  name: Postmates Domain Security
  slug: postmates-domain-security
  summary_line: TLSv1.3 · DMARC
slug: postmates
tags:
- Acquired
- Couriers
- Delivery
- Food Delivery
- Historical
- Logistics
- On-Demand
- Sunset
website: https://postmates.com
---
