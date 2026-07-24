---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 12
  human_in_the_loop: 0
  name: Friendbuy Agentic Access
  operation_count: 31
  slug: friendbuy-agentic-access
  summary_line: 31 operations · 12 acting
api_count: 7
apis:
- description: Pull campaign, share, click, conversion, and reward analytics.
  name: Friendbuy Analytics API
  slug: friendbuy-analytics-api
- description: Exchange account key and secret for a Bearer token.
  name: Friendbuy Authorization API
  slug: friendbuy-authorization-api
- description: Create and retrieve customer records and manage customer data requests.
  name: Friendbuy Customers API
  slug: friendbuy-customers-api
- description: Track purchase, sign-up, and custom conversion events.
  name: Friendbuy Events API
  slug: friendbuy-events-api
- description: Block users from campaigns.
  name: Friendbuy Management API
  slug: friendbuy-management-api
- description: Generate personal referral links and check referral status.
  name: Friendbuy Referrals API
  slug: friendbuy-referrals-api
- description: Manage loyalty ledger balances, adjustments, redemptions, and coupons.
  name: Friendbuy Rewards & Loyalty API
  slug: friendbuy-rewards-loyalty-api
artifact_total: 14
collections:
- collection_type: open
  name: Friendbuy Merchant API
  slug: open-friendbuy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/friendbuy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/friendbuy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/friendbuy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/friendbuy
- group: company
  title: ''
  type: Website
  url: https://friendbuy.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.friendbuy.com
- group: commercial
  title: ''
  type: Plans
  url: plans/friendbuy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/friendbuy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/friendbuy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://friendbuy.com/blog
created: '2026-07-10'
description: Friendbuy is a referral and loyalty marketing platform for ecommerce and direct-to-consumer brands. Merchants launch referral, loyalty, and reward campaigns through on-site widgets and a no-code dashboard, and integrate server-to-server through the Friendbuy Merchant API (base https://mapi.fbot.me/v1). The Merchant API lets merchants sync customer records, generate personal referral links, track purchase / sign-up / custom conversion events, pull campaign and reward analytics, and manage loyalty ledger balances, adjustments, redemptions, and coupons. Authentication is a key/secret exchange at POST /authorization that returns a short-lived Bearer JWT. Access to the API and to production credentials is gated behind a paid, contact-sales plan.
finops:
- name: Friendbuy Finops
  service_category: Marketing and Advertising
  slug: friendbuy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/friendbuy.png
layout: provider
modified: '2026-07-10'
name: Friendbuy
nav: Providers
network: true
overview: 'Friendbuy publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Authorization API, Customers API, and 4 more. Tagged areas include Referral Marketing, Loyalty, Rewards, Ecommerce, and Marketing.


  Friendbuy''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Friendbuy Plans Pricing
  plan_count: 3
  slug: friendbuy-plans-pricing
random_paper: 50
rate_limits:
- limit_count: 4
  name: Friendbuy Rate Limits
  slug: friendbuy-rate-limits
score:
  band: thin
  composite: 37.8
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.9
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Friendbuy Authentication
  slug: friendbuy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Friendbuy Domain Security
  slug: friendbuy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: friendbuy
tags:
- Referral Marketing
- Loyalty
- Rewards
- Ecommerce
- Marketing
- Advocacy
website: https://friendbuy.com
---
