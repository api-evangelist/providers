---
access_model:
  confidence: medium
  label: Paid (free trial)
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: true
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
  score: 38.5
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 44
  human_in_the_loop: 1
  name: Drycleancloud Agentic Access
  operation_count: 44
  slug: drycleancloud-agentic-access
  summary_line: 44 operations · 44 acting · 1 human-in-the-loop
api_count: 7
apis:
- description: Business accounts, reporting, photos, groups, and referrals.
  name: CleanCloud Business and Reporting API
  slug: drycleancloud-business-and-reporting-api
- description: Customer accounts, authentication, and password reset.
  name: CleanCloud Customers API
  slug: drycleancloud-customers-api
- description: Customer/store messaging and push notification tokens.
  name: CleanCloud Messaging API
  slug: drycleancloud-messaging-api
- description: Orders and the garments within them.
  name: CleanCloud Orders API
  slug: drycleancloud-orders-api
- description: Payments, cards, subscriptions, invoices, promotions, and loyalty.
  name: CleanCloud Payments API
  slug: drycleancloud-payments-api
- description: Recurring pickups, routing, scheduling, and driver location.
  name: CleanCloud Pickup and Delivery API
  slug: drycleancloud-pickup-and-delivery-api
- description: Products, price lists, and inventory.
  name: CleanCloud Products API
  slug: drycleancloud-products-api
artifact_total: 13
collections:
- collection_type: open
  name: CleanCloud API
  slug: open-drycleancloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/drycleancloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/drycleancloud-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cleancloud
- group: company
  title: ''
  type: Website
  url: https://cleancloudapp.com
- group: docs
  title: ''
  type: Documentation
  url: https://cleancloudapp.com/api
- group: commercial
  title: ''
  type: Plans
  url: plans/drycleancloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/drycleancloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/drycleancloud-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://cleancloudapp.com/blog
created: '2026-07-04'
description: CleanCloud is cloud-based point-of-sale (POS) and business management software for dry cleaners, laundromats, laundry services, and shoe repair businesses. It handles orders, garment tracking, customers, pickup and delivery routing, payments, inventory, marketing, and reporting. CleanCloud exposes a documented public REST API (base https://cleancloudapp.com/api) for programmatic access to customers, orders, garments, products, price lists, inventory, pickup and delivery scheduling, payments, subscriptions, invoices, promotions, and reporting, plus outbound Webhooks for order and customer events. API access is available on the Grow and Grow+ subscription tiers, authenticated with a per-account API token and metered at 50,000 requests per month (max 3 requests per second).
finops:
- name: Drycleancloud Finops
  service_category: Business Applications
  slug: drycleancloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/drycleancloud.png
layout: provider
modified: '2026-07-04'
name: CleanCloud
nav: Providers
network: true
overview: 'CleanCloud publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Business and Reporting API, Customers API, Messaging API, and 4 more. Tagged areas include Dry Cleaning, Laundry, Point of Sale, POS, and Field Service.


  CleanCloud''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Drycleancloud Plans Pricing
  plan_count: 4
  slug: drycleancloud-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 3
  name: Drycleancloud Rate Limits
  slug: drycleancloud-rate-limits
score:
  band: thin
  composite: 34.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.2
    developer_ergonomics: 10.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Drycleancloud Domain Security
  slug: drycleancloud-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: drycleancloud
tags:
- Dry Cleaning
- Laundry
- Point of Sale
- POS
- Field Service
- Pickup and Delivery
- SMB Software
website: https://cleancloudapp.com
---
