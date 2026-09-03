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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Smile Io Agentic Access
  operation_count: 14
  slug: smile-io-agentic-access
  summary_line: 14 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.smile.io/v1
  baseurl_source: declared
  description: Record custom customer activities that can earn points.
  name: Smile.io Activities API
  slug: smile-io-activities-api
- baseURL: https://api.smile.io/v1
  baseurl_source: declared
  description: Create or update a customer from an external system identity.
  name: Smile.io Customer Identities API
  slug: smile-io-customer-identities-api
- baseURL: https://api.smile.io/v1
  baseurl_source: declared
  description: Loyalty program members and their point balances and state.
  name: Smile.io Customers API
  slug: smile-io-customers-api
- baseURL: https://api.smile.io/v1
  baseurl_source: declared
  description: Rules that define how customers earn points.
  name: Smile.io Earning Rules API
  slug: smile-io-earning-rules-api
- baseURL: https://api.smile.io/v1
  baseurl_source: declared
  description: Redeemable products a customer can purchase with points.
  name: Smile.io Points Products API
  slug: smile-io-points-products-api
- baseURL: https://api.smile.io/v1
  baseurl_source: declared
  description: Program-level points configuration (currency name, ratios).
  name: Smile.io Points Settings API
  slug: smile-io-points-settings-api
- baseURL: https://api.smile.io/v1
  baseurl_source: declared
  description: Point balance changes - earn, redeem, adjust - for a customer.
  name: Smile.io Points Transactions API
  slug: smile-io-points-transactions-api
- baseURL: https://api.smile.io/v1
  baseurl_source: declared
  description: Fulfillment records for rewards a customer has redeemed.
  name: Smile.io Reward Fulfillments API
  slug: smile-io-reward-fulfillments-api
- baseURL: https://api.smile.io/v1
  baseurl_source: declared
  description: VIP program tiers and their thresholds and perks.
  name: Smile.io VIP Tiers API
  slug: smile-io-vip-tiers-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Smile.io REST Activities API
  slug: open-smile-io-activities-api
- collection_type: open
  name: Smile.io REST Activities Customer Identities API
  slug: open-smile-io-customer-identities-api
- collection_type: open
  name: Smile.io REST Activities Customers API
  slug: open-smile-io-customers-api
- collection_type: open
  name: Smile.io REST Activities Earning Rules API
  slug: open-smile-io-earning-rules-api
- collection_type: open
  name: Smile.io REST Activities Points Products API
  slug: open-smile-io-points-products-api
- collection_type: open
  name: Smile.io REST Activities Points Settings API
  slug: open-smile-io-points-settings-api
- collection_type: open
  name: Smile.io REST Activities Points Transactions API
  slug: open-smile-io-points-transactions-api
- collection_type: open
  name: Smile.io REST Activities Reward Fulfillments API
  slug: open-smile-io-reward-fulfillments-api
- collection_type: open
  name: Smile.io REST Activities VIP Tiers API
  slug: open-smile-io-vip-tiers-api
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
overview: 'Smile.io publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Customer Identities API, Customers API, and 6 more. Tagged areas include Loyalty, Rewards, Referrals, E-Commerce, and Points.


  Smile.io''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Smile Io Plans Pricing
  plan_count: 6
  slug: smile-io-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Smile Io Rate Limits
  slug: smile-io-rate-limits
score:
  band: developing
  composite: 39.3
  coverage:
    artifact_dirs: 9
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smile-io/refs/heads/main/screenshots/smile-io-2026-09-02T155946.png
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
- E-Commerce
- Points
- Customer Retention
- Shopify
website: https://smile.io
---
