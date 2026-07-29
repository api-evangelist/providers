---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
- acting_count: 6
  human_in_the_loop: 0
  name: Reviews Io Agentic Access
  operation_count: 16
  slug: reviews-io-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 6
apis:
- description: Retrieve company (merchant) reviews.
  name: REVIEWS.io Company Reviews API
  slug: reviews-io-company-reviews-api
- description: Queue, list, and edit product and company review invitations.
  name: REVIEWS.io Invitations API
  slug: reviews-io-invitations-api
- description: Retrieve, create, and vote on product reviews.
  name: REVIEWS.io Product Reviews API
  slug: reviews-io-product-reviews-api
- description: Create and retrieve customer questions.
  name: REVIEWS.io Questions API
  slug: reviews-io-questions-api
- description: Aggregate product ratings and review statistics.
  name: REVIEWS.io Ratings API
  slug: reviews-io-ratings-api
- description: Manage review-submitted webhook subscriptions.
  name: REVIEWS.io Webhooks API
  slug: reviews-io-webhooks-api
artifact_total: 13
collections:
- collection_type: open
  name: REVIEWS.io API
  slug: open-reviews-io
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reviews-io-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reviews-io-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reviews-io-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reviewscouk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reviews-io
- group: company
  title: ''
  type: Website
  url: https://www.reviews.io
- group: docs
  title: ''
  type: Documentation
  url: https://developer.reviews.io/reference
- group: commercial
  title: ''
  type: Plans
  url: plans/reviews-io-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/reviews-io-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/reviews-io-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.reviews.io/
created: '2026-06-25'
description: REVIEWS.io is a product and company reviews and user-generated content (UGC) platform that helps brands collect, manage, and display verified customer reviews. Its REST API (https://api.reviews.io) lets developers queue review invitations, retrieve product and company reviews, fetch ratings and widget data, manage questions, and subscribe to webhooks using store + apikey authentication.
finops:
- name: Reviews Io Finops
  service_category: Marketing and Customer Experience
  slug: reviews-io-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reviews-io.png
layout: provider
modified: '2026-06-25'
name: REVIEWS.io
nav: Providers
network: true
overview: 'REVIEWS.io publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Company Reviews API, Invitations API, Product Reviews API, and 3 more. Tagged areas include Reviews, UGC, Ratings, Reputation, and eCommerce.


  REVIEWS.io''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Reviews Io Plans Pricing
  plan_count: 5
  slug: reviews-io-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 4
  name: Reviews Io Rate Limits
  slug: reviews-io-rate-limits
score:
  band: thin
  composite: 38.6
  delta: -2.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 56.8
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Reviews Io Authentication
  slug: reviews-io-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Reviews Io Domain Security
  slug: reviews-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reviews-io
tags:
- Reviews
- UGC
- Ratings
- Reputation
- eCommerce
website: https://www.reviews.io
---
