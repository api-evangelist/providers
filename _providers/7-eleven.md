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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 19
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/7-eleven-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ok7-eleven
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/7-eleven
- group: company
  title: ''
  type: Website
  url: https://www.7-eleven.com/
- group: start
  title: ''
  type: Login
  url: https://www.7-eleven.com/account/sign-in
- group: start
  title: ''
  type: Signup
  url: https://www.7-eleven.com/account/sign-up
- group: auth
  title: ''
  type: Authentication
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
created: '2026-05-05'
description: A global convenience store chain offering everyday essentials, snacks, and beverages. Known for its 24/7 operations and Slurpee brand drinks.
features:
- description: Digital loyalty program where customers earn points on qualifying purchases redeemable for free products and exclusive offers.
  name: 7Rewards Loyalty Program
- description: On-demand delivery service for convenience store items, food, and beverages from local 7-Eleven stores.
  name: 7NOW Delivery
- description: In-app mobile checkout enabling customers to scan and pay without using a register inside participating stores.
  name: Mobile Checkout
- description: Locate nearby 7-Eleven stores with hours, fuel pricing, and in-store services.
  name: Store Locator
- description: Real-time fuel prices for 7-Eleven and Speedway branded fuel stations.
  name: Fuel Pricing
- description: Accept Apple Pay, Google Pay, and 7-Eleven Wallet for in-store and online purchases.
  name: Mobile Payments
finops:
- name: 7 Eleven Finops
  service_category: Retail / Convenience
  slug: 7-eleven-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/7-eleven.png
integrations:
- description: Speedway convenience stores and fuel locations are part of 7-Eleven's North American retail footprint.
  name: Speedway
- description: Apple Pay tokenized payment acceptance for in-store and in-app purchases.
  name: Apple Pay
- description: Google Pay tokenized payment acceptance for in-store and in-app purchases.
  name: Google Pay
- description: Third-party delivery integration making 7-Eleven inventory available through the DoorDash marketplace.
  name: DoorDash
- description: Third-party delivery integration making 7-Eleven inventory available through Uber Eats.
  name: Uber Eats
layout: provider
modified: '2026-05-16'
name: 7-Eleven
nav: Providers
network: true
overview: '7-Eleven is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Retail and Convenience Stores.


  7-Eleven''s developer surface includes signup flow, authentication, and 4 more developer resources.'
plans:
- name: 7 Eleven Plans Pricing
  plan_count: 1
  slug: 7-eleven-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: 7 Eleven Rate Limits
  slug: 7-eleven-rate-limits
score:
  band: emerging
  composite: 18.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 31.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/7-eleven/refs/heads/main/screenshots/7-eleven-2026-06-20T162752.png
security:
- kind: domain-security
  name: 7 Eleven Domain Security
  slug: 7-eleven-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 7-eleven
tags:
- Retail
- Convenience Stores
use_cases:
- description: Customer engagement and retention through points-based loyalty rewards and personalized offers.
  name: Loyalty Engagement
- description: Last-mile delivery of convenience goods, food, and beverages to consumers in metro areas.
  name: Convenience Delivery
- description: In-app ordering, payment, and pickup for convenience store products.
  name: Mobile Commerce
- description: Branded retail fuel sales through 7-Eleven and Speedway fuel locations.
  name: Fuel Retail
website: https://www.7-eleven.com/
---
