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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Open Loyalty Agentic Access
  operation_count: 36
  slug: open-loyalty-agentic-access
  summary_line: 36 operations · 21 acting
api_count: 7
apis:
- description: Authentication and token issuance.
  name: Open Loyalty Authorization API
  slug: open-loyalty-authorization-api
- description: Rules that define how members earn points.
  name: Open Loyalty Earning Rules API
  slug: open-loyalty-earning-rules-api
- description: Loyalty members (customers).
  name: Open Loyalty Members API
  slug: open-loyalty-members-api
- description: Points transfers - the loyalty points ledger.
  name: Open Loyalty Points API
  slug: open-loyalty-points-api
- description: Reward campaigns, coupons, and redemption.
  name: Open Loyalty Rewards API
  slug: open-loyalty-rewards-api
- description: Levels (loyalty tiers).
  name: Open Loyalty Tiers API
  slug: open-loyalty-tiers-api
- description: Purchase transactions and points accrual.
  name: Open Loyalty Transactions API
  slug: open-loyalty-transactions-api
artifact_total: 14
collections:
- collection_type: open
  name: Open Loyalty REST API
  slug: open-open-loyalty
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-loyalty-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-loyalty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/open-loyalty-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OpenLoyalty
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/openloyalty
- group: company
  title: ''
  type: Website
  url: https://www.openloyalty.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openloyalty.io/en/latest/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/open-loyalty-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/open-loyalty-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/open-loyalty-finops.yml
created: '2026-07-10'
description: Open Loyalty is an API-first, headless loyalty and gamification platform. Every loyalty mechanic - members, transactions, points, tiers/levels, earning rules, reward campaigns, and analytics - is exposed through a documented REST API, so brands assemble custom loyalty experiences on top of Open Loyalty rather than a fixed UI. The platform grew from an open-source loyalty engine (still available as a GitHub Open Source Edition capped at 200 members for testing) into a managed, cloud-hosted SaaS. Requests are JSON over HTTPS, authenticated with a JWT bearer token (per-store and admin login) or a permanent API token. The API is scoped per store using a storeCode path segment, and change events are delivered to consumers via outbound HTTP webhook callbacks.
finops:
- name: Open Loyalty Finops
  service_category: Marketing and Customer Engagement
  slug: open-loyalty-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-loyalty.png
layout: provider
modified: '2026-07-10'
name: Open Loyalty
nav: Providers
network: true
overview: 'Open Loyalty publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Authorization API, Earning Rules API, Members API, and 4 more. Tagged areas include Loyalty, Gamification, Rewards, Points, and Loyalty Program.


  Open Loyalty''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Open Loyalty Plans Pricing
  plan_count: 3
  slug: open-loyalty-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Open Loyalty Rate Limits
  slug: open-loyalty-rate-limits
score:
  band: thin
  composite: 38.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.4
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Open Loyalty Authentication
  slug: open-loyalty-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Open Loyalty Domain Security
  slug: open-loyalty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-loyalty
tags:
- Loyalty
- Gamification
- Rewards
- Points
- Loyalty Program
- Customer Engagement
- Headless
- API First
website: https://www.openloyalty.io
---
