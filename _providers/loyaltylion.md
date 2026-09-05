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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Loyaltylion Agentic Access
  operation_count: 15
  slug: loyaltylion-agentic-access
  summary_line: 15 operations · 9 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.loyaltylion.com/v2
  baseurl_source: declared
  description: Customer activities recorded against loyalty rules to award points.
  name: LoyaltyLion Activities API
  slug: loyaltylion-activities-api
- baseURL: https://api.loyaltylion.com/v2
  baseurl_source: declared
  description: Loyalty customer profiles, points balances, tiers, and referrals.
  name: LoyaltyLion Customers API
  slug: loyaltylion-customers-api
- baseURL: https://api.loyaltylion.com/v2
  baseurl_source: declared
  description: Manual point adjustments and immutable point transactions.
  name: LoyaltyLion Points API
  slug: loyaltylion-points-api
- baseURL: https://api.loyaltylion.com/v2
  baseurl_source: declared
  description: Claiming and refunding rewards on behalf of a customer.
  name: LoyaltyLion Redemptions API
  slug: loyaltylion-redemptions-api
- baseURL: https://api.loyaltylion.com/v2
  baseurl_source: declared
  description: Rewards a customer can claim and program reward catalog controls.
  name: LoyaltyLion Rewards API
  slug: loyaltylion-rewards-api
- baseURL: https://api.loyaltylion.com/v2
  baseurl_source: declared
  description: Identity and diagnostic endpoints.
  name: LoyaltyLion Utility API
  slug: loyaltylion-utility-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LoyaltyLion Activities API
  slug: open-loyaltylion-activities-api
- collection_type: open
  name: LoyaltyLion Activities Customers API
  slug: open-loyaltylion-customers-api
- collection_type: open
  name: LoyaltyLion Activities Points API
  slug: open-loyaltylion-points-api
- collection_type: open
  name: LoyaltyLion Activities Redemptions API
  slug: open-loyaltylion-redemptions-api
- collection_type: open
  name: LoyaltyLion Activities Rewards API
  slug: open-loyaltylion-rewards-api
- collection_type: open
  name: LoyaltyLion Activities Utility API
  slug: open-loyaltylion-utility-api
- collection_type: open
  name: LoyaltyLion API
  slug: open-loyaltylion
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/loyaltylion-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loyaltylion-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/loyaltylion-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/loyaltylion
- group: company
  title: ''
  type: Website
  url: https://loyaltylion.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.loyaltylion.com
- group: commercial
  title: ''
  type: Plans
  url: plans/loyaltylion-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loyaltylion-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loyaltylion-finops.yml
created: '2026-07-10'
description: LoyaltyLion is an e-commerce loyalty and rewards platform for Shopify, BigCommerce, and custom storefronts, letting merchants run points, referrals, VIP tiers, and reward programs. Its v2 REST API (base https://api.loyaltylion.com/v2) is split into an Admin API for moving data in and out of LoyaltyLion - retrieving customers and transactions, tracking orders, and adjusting points - and a Headless API for building custom shopper-facing loyalty experiences in web, mobile, and POS apps. Requests authenticate with a Program API key passed as a Bearer token (with scoped access), or the deprecated token/secret pair over HTTP Basic auth. All endpoints share a 20 requests-per-second rate limit.
finops:
- name: Loyaltylion Finops
  service_category: Marketing and Loyalty
  slug: loyaltylion-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loyaltylion.png
layout: provider
modified: '2026-07-10'
name: LoyaltyLion
nav: Providers
network: true
overview: 'LoyaltyLion publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Activities API, Customers API, Points API, and 3 more. Tagged areas include Loyalty, Rewards, E-Commerce, Points, and Shopify.


  LoyaltyLion''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Loyaltylion Plans Pricing
  plan_count: 4
  slug: loyaltylion-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Loyaltylion Rate Limits
  slug: loyaltylion-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 60.0
    catalog_earned_first_party: 0.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loyaltylion/refs/heads/main/screenshots/loyaltylion-2026-07-25T225628.png
security:
- kind: authentication
  name: Loyaltylion Authentication
  slug: loyaltylion-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Loyaltylion Domain Security
  slug: loyaltylion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: loyaltylion
tags:
- Loyalty
- Rewards
- E-Commerce
- Points
- Shopify
- Retention
website: https://loyaltylion.com
---
