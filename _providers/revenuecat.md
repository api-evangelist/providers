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
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 19
  human_in_the_loop: 2
  name: Revenuecat Agentic Access
  operation_count: 34
  slug: revenuecat-agentic-access
  summary_line: 34 operations · 19 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: Outbound webhooks that POST subscription lifecycle events (INITIAL_PURCHASE, RENEWAL, CANCELLATION, EXPIRATION, BILLING_ISSUE, PRODUCT_CHANGE, and more) to a customer endpoint, secured with an Authori
  name: RevenueCat Webhooks
  slug: revenuecat-webhooks
- description: v2 app (platform integration) management.
  name: RevenueCat Apps API
  slug: revenuecat-apps-api
- description: v2 customer management.
  name: RevenueCat Customers API
  slug: revenuecat-customers-api
- description: v1 promotional entitlement grant and revoke.
  name: RevenueCat Entitlements (v1) API
  slug: revenuecat-entitlements-v1-api
- description: v2 entitlement definitions.
  name: RevenueCat Entitlements (v2) API
  slug: revenuecat-entitlements-v2-api
- description: v1 offering fetch and override.
  name: RevenueCat Offerings (v1) API
  slug: revenuecat-offerings-v1-api
- description: v2 offering definitions.
  name: RevenueCat Offerings (v2) API
  slug: revenuecat-offerings-v2-api
- description: v2 package definitions within an offering.
  name: RevenueCat Packages API
  slug: revenuecat-packages-api
- description: v2 product catalog management.
  name: RevenueCat Products API
  slug: revenuecat-products-api
- description: v2 project management.
  name: RevenueCat Projects API
  slug: revenuecat-projects-api
- description: v1 receipt validation and transaction lifecycle operations.
  name: RevenueCat Purchases API
  slug: revenuecat-purchases-api
- description: v1 customer (app user) records, attributes, and state.
  name: RevenueCat Subscribers API
  slug: revenuecat-subscribers-api
artifact_total: 19
collections:
- collection_type: open
  name: RevenueCat REST API
  slug: open-revenuecat
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revenuecat-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revenuecat-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revenuecat-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RevenueCat
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revenuecat
- group: company
  title: ''
  type: Website
  url: https://www.revenuecat.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.revenuecat.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/revenuecat-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/revenuecat-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/revenuecat-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.revenuecat.com/blog/rss.xml
created: '2026-07-01'
description: RevenueCat provides in-app subscription and purchase infrastructure for mobile and web apps. It abstracts App Store, Google Play, Amazon, Stripe, Roku, and Paddle billing behind cross-platform SDKs and a REST API, handling receipt validation, entitlements, subscriber state, offerings and paywalls, experiments, and subscription analytics. A v1 REST API manages live subscribers and purchases; a v2 REST API manages the project catalog (projects, apps, products, entitlements, offerings, packages); webhooks stream subscription lifecycle events.
finops:
- name: Revenuecat Finops
  service_category: Developer Tools
  slug: revenuecat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revenuecat.png
layout: provider
modified: '2026-07-01'
name: RevenueCat
nav: Providers
network: true
overview: 'RevenueCat publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Customers API, Entitlements (v1) API, and 8 more. Tagged areas include Subscriptions, In-App Purchases, Billing, Mobile, and Entitlements.


  RevenueCat''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Revenuecat Plans Pricing
  plan_count: 4
  slug: revenuecat-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 7
  name: Revenuecat Rate Limits
  slug: revenuecat-rate-limits
score:
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.5
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Revenuecat Authentication
  slug: revenuecat-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Revenuecat Domain Security
  slug: revenuecat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: revenuecat
tags:
- Subscriptions
- In-App Purchases
- Billing
- Mobile
- Entitlements
website: https://www.revenuecat.com/
---
