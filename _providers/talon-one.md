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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Talon One Agentic Access
  operation_count: 35
  slug: talon-one-agentic-access
  summary_line: 35 operations · 19 acting
api_count: 13
apis:
- description: Management API - accounts, users, and sessions.
  name: Talon.One Account API
  slug: talon-one-account-api
- description: Management API - Applications and their health.
  name: Talon.One Applications API
  slug: talon-one-applications-api
- description: Management API - custom attributes.
  name: Talon.One Attributes API
  slug: talon-one-attributes-api
- description: Manage audiences and their memberships.
  name: Talon.One Audiences API
  slug: talon-one-audiences-api
- description: Management API - campaigns and rulesets.
  name: Talon.One Campaigns API
  slug: talon-one-campaigns-api
- description: Management API - account and campaign collections.
  name: Talon.One Collections API
  slug: talon-one-collections-api
- description: Coupon reservation (Integration) and coupon management (Management).
  name: Talon.One Coupons API
  slug: talon-one-coupons-api
- description: Integration API - sync customer profile data and read inventory.
  name: Talon.One Customer Profiles API
  slug: talon-one-customer-profiles-api
- description: Integration API - create and update customer sessions and receive effects.
  name: Talon.One Customer Sessions API
  slug: talon-one-customer-sessions-api
- description: Integration API - submit custom events that trigger rules.
  name: Talon.One Events API
  slug: talon-one-events-api
- description: Management API - analytics, coupon, and effect exports.
  name: Talon.One Exports API
  slug: talon-one-exports-api
- description: Loyalty program balances, points, cards, and transactions.
  name: Talon.One Loyalty API
  slug: talon-one-loyalty-api
- description: Create and manage referral codes.
  name: Talon.One Referrals API
  slug: talon-one-referrals-api
artifact_total: 20
collections:
- collection_type: open
  name: Talon.One API
  slug: open-talon-one
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/talon-one-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/talon-one-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/talon-one-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/talon-one
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/talon-one
- group: company
  title: ''
  type: Website
  url: https://www.talon.one
- group: docs
  title: ''
  type: Documentation
  url: https://docs.talon.one
- group: start
  title: ''
  type: SignUp
  url: https://www.talon.one/demo
- group: commercial
  title: ''
  type: Plans
  url: plans/talon-one-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/talon-one-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/talon-one-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.talon.one/blog
created: '2026-07-10'
description: Talon.One is an enterprise promotion, loyalty, and incentives engine that lets teams build and run coupons, discounts, referrals, bundles, giveaways, and multi-tier loyalty programs from a single rules-based platform. It exposes two primary REST APIs. The Integration API pushes real-time customer sessions, profiles, and events into the rules engine and returns the effects (discounts, awarded loyalty points, accepted coupons) to apply in the calling application. The Management API programmatically administers applications, campaigns, rulesets, coupons, loyalty programs, audiences, custom attributes, collections, and analytics exports that back the Campaign Manager. Talon.One is delivered as a managed, per-customer deployment; each account calls its own base URL (https://yourbaseurl.talon.one) and authenticates with an API key whose prefix distinguishes the Integration key (ApiKey-v1) from the Management key (ManagementKey-v1).
finops:
- name: Talon One Finops
  service_category: Marketing and Promotions
  slug: talon-one-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/talon-one.png
layout: provider
modified: '2026-07-10'
name: Talon.One
nav: Providers
network: true
overview: 'Talon.One publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Account API, Applications API, Attributes API, and 10 more. Tagged areas include Promotions, Loyalty, Coupons, Incentives, and Campaigns.


  Talon.One''s developer surface includes authentication, documentation, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: Talon One Plans Pricing
  plan_count: 3
  slug: talon-one-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 4
  name: Talon One Rate Limits
  slug: talon-one-rate-limits
score:
  band: thin
  composite: 41.4
  delta: -2.1
  facets:
    commercial_clarity: 52.6
    contract_quality: 57.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Talon One Authentication
  slug: talon-one-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Talon One Domain Security
  slug: talon-one-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: talon-one
tags:
- Promotions
- Loyalty
- Coupons
- Incentives
- Campaigns
- Personalization
- MarTech
- Rules Engine
website: https://www.talon.one
---
