---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    auth_clarity: false
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
  score: 3.2
  scored_at: '2026-08-12'
api_count: 14
apis:
- description: Records customer interactions from e-commerce, POS, websites, and mobile apps as loyalty events (for example point_add, checkout_accept), driving the rules and workflows of the loyalty program. Suppor
  name: Antavo Events API
  slug: antavo-events-api
- description: Queues events for reliable background processing during high-traffic periods, returning a correlation id that can be polled for status. Uses token-based authentication via the /v1/auth/token endpoint.
  name: Antavo Async Events API
  slug: antavo-async-events-api
- description: Search, retrieve, and manage loyalty member profiles - including login, opt-in registration, password reset, verification, account merging, and active-customer counts - while maintaining member privac
  name: Antavo Customer API
  slug: antavo-customer-api
- description: The primary headless API for building the member-facing loyalty experience - listing earn and spend activities, challenges, rewards, offers, coupons, transactions, wallet passes, quizzes, contests, pr
  name: Antavo Display API
  slug: antavo-display-api
- description: 'Generic CRUD surface for the foundational building blocks of a program - rewards, challenges, stores, products, transactions, and customer lists - addressed as entities under a module namespace, with '
  name: Antavo Entities API
  slug: antavo-entities-api
- description: Manage the reward catalog and redemptions - create, list, retrieve, update, and archive rewards via the entities surface, and claim rewards. Legacy /rewards claim endpoints are superseded by the Displ
  name: Antavo Rewards API
  slug: antavo-rewards-api
- description: Query coupon usage independent of a customer and create or manage coupon pools - configuring value, expiration, and code patterns - with bulk import of codes and status/error reporting on the batch op
  name: Antavo Coupons and Coupon Pools API
  slug: antavo-coupons-api
- description: Submit a cart and retrieve applicable pre-purchase offers used for customer acquisition and engagement, and list a member's available offers through the Display surface.
  name: Antavo Offers API
  slug: antavo-offers-api
- description: Preview the loyalty points a transaction would earn, including bonus points assigned by the Workflows module, before the transaction is committed.
  name: Antavo Points Preview API
  slug: antavo-points-preview-api
- description: Retrieve ranked lists of top customers with their scores for display in mobile apps, websites, and CRMs.
  name: Antavo Leaderboard API
  slug: antavo-leaderboard-api
- description: Batch processing for reward claims across many customers and for adding or removing customers from lists, each returning a batch id with status and error reporting endpoints.
  name: Antavo Bulk Operations API
  slug: antavo-bulk-operations-api
- description: Create and administer member clubs and communities - templates, membership, invitations, applicants, bans, ownership, point adjustments and donations, history, and disbanding.
  name: Antavo Clubs API
  slug: antavo-clubs-api
- description: List and manage promotions and apply them at checkout - submit a cart to retrieve applicable promotions and finalize the checkout with the resulting discounts.
  name: Antavo Promotion Engine API
  slug: antavo-promotion-engine-api
- description: Generate short-lived access tokens for credential clients configured in the Authentication Manager, used for token-based authentication such as the Async Events API.
  name: Antavo Authentication API
  slug: antavo-authentication-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/antavo-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/antavo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/antavo
- group: company
  title: ''
  type: Website
  url: https://antavo.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.antavo.com/docs/antavo-apis
- group: commercial
  title: ''
  type: Plans
  url: plans/antavo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/antavo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/antavo-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://antavo.com/blog/
created: '2026-07-10'
description: Antavo is an enterprise loyalty management platform - the Antavo AI Loyalty Cloud - that lets brands build and run omnichannel, multi-brand, multi-country loyalty programs. Its API-first, headless Loyalty Engine exposes a comprehensive REST API covering customer events, customer profiles, the headless Display surface for loyalty experiences, configurable entities (rewards, challenges, stores, products, transactions), coupons, offers, leaderboards, clubs, promotions, and bulk operations. Requests use standard HTTP verbs with JSON, secured by API key/secret with optional request signing, IP filtering, and token-based auth. API access is provisioned per Antavo environment for enterprise customers, while the developer documentation is fully public.
finops:
- name: Antavo Finops
  service_category: Marketing and Customer Loyalty
  slug: antavo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/antavo.png
layout: provider
modified: '2026-07-10'
name: Antavo
nav: Providers
network: true
overview: 'Antavo publishes 14 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Loyalty, Customer Loyalty, Rewards, Enterprise, and Headless.


  Antavo''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Antavo Plans Pricing
  plan_count: 2
  slug: antavo-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 4
  name: Antavo Rate Limits
  slug: antavo-rate-limits
score:
  band: emerging
  composite: 20.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 20.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/antavo/refs/heads/main/screenshots/antavo-2026-07-25T200404.png
security:
- kind: domain-security
  name: Antavo Domain Security
  slug: antavo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: antavo
tags:
- Loyalty
- Customer Loyalty
- Rewards
- Enterprise
- Headless
- Retail
- Marketing
- Engagement
website: https://antavo.com
---
