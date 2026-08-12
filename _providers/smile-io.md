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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Smile Io Agentic Access
  operation_count: 14
  slug: smile-io-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 9
apis:
- description: Record custom customer activities that can earn points.
  name: Smile.io Activities API
  slug: smile-io-activities-api
- description: Create or update a customer from an external system identity.
  name: Smile.io Customer Identities API
  slug: smile-io-customer-identities-api
- description: Loyalty program members and their point balances and state.
  name: Smile.io Customers API
  slug: smile-io-customers-api
- description: Rules that define how customers earn points.
  name: Smile.io Earning Rules API
  slug: smile-io-earning-rules-api
- description: Redeemable products a customer can purchase with points.
  name: Smile.io Points Products API
  slug: smile-io-points-products-api
- description: Program-level points configuration (currency name, ratios).
  name: Smile.io Points Settings API
  slug: smile-io-points-settings-api
- description: Point balance changes - earn, redeem, adjust - for a customer.
  name: Smile.io Points Transactions API
  slug: smile-io-points-transactions-api
- description: Fulfillment records for rewards a customer has redeemed.
  name: Smile.io Reward Fulfillments API
  slug: smile-io-reward-fulfillments-api
- description: VIP program tiers and their thresholds and perks.
  name: Smile.io VIP Tiers API
  slug: smile-io-vip-tiers-api
artifact_total: 16
collections:
- collection_type: open
  name: Smile.io REST API
  slug: open-smile-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smile-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smile-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/smile-io-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smile-rewards
- group: company
  title: ''
  type: Website
  url: https://smile.io
- group: docs
  title: ''
  type: Documentation
  url: https://dev.smile.io/api/introduction
- group: commercial
  title: ''
  type: Plans
  url: plans/smile-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smile-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smile-io-finops.yml
created: '2026-07-10'
description: Smile.io is a loyalty, rewards, and referrals platform for e-commerce brands (widely used on Shopify). Merchants run points programs, referral programs, and VIP tiers, and integrate them programmatically through the Smile.io REST API (base https://api.smile.io/v1). The REST API exposes customers and customer identities, points transactions and settings, points products and purchases, earning rules, rewards and reward fulfillments, VIP tiers, and custom activities. It uses resource-oriented URLs, returns JSON, and is authenticated with an HTTP Bearer token (a merchant API key or an app OAuth access token). REST API access is gated to the Plus and Enterprise plans.
finops:
- name: Smile Io Finops
  service_category: Marketing and Loyalty
  slug: smile-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smile-io.png
layout: provider
modified: '2026-07-10'
name: Smile.io
nav: Providers
network: true
overview: 'Smile.io publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Customer Identities API, Customers API, and 6 more. Tagged areas include Loyalty, Rewards, Referrals, E-commerce, and Points.


  Smile.io''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Smile Io Plans Pricing
  plan_count: 6
  slug: smile-io-plans-pricing
random_paper: 103
rate_limits:
- limit_count: 3
  name: Smile Io Rate Limits
  slug: smile-io-rate-limits
score:
  band: thin
  composite: 38.5
  delta: -0.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Smile Io Authentication
  slug: smile-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Smile Io Domain Security
  slug: smile-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smile-io
tags:
- Loyalty
- Rewards
- Referrals
- E-commerce
- Points
- Customer Retention
- Shopify
website: https://smile.io
---
