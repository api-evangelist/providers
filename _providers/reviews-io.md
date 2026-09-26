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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Reviews Io Agentic Access
  operation_count: 16
  slug: reviews-io-agentic-access
  summary_line: 16 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.reviews.io
  baseurl_source: declared
  description: Retrieve company (merchant) reviews.
  name: REVIEWS.io Company Reviews API
  slug: reviews-io-company-reviews-api
- baseURL: https://api.reviews.io
  baseurl_source: declared
  description: Queue, list, and edit product and company review invitations.
  name: REVIEWS.io Invitations API
  slug: reviews-io-invitations-api
- baseURL: https://api.reviews.io
  baseurl_source: declared
  description: Retrieve, create, and vote on product reviews.
  name: REVIEWS.io Product Reviews API
  slug: reviews-io-product-reviews-api
- baseURL: https://api.reviews.io
  baseurl_source: declared
  description: Create and retrieve customer questions.
  name: REVIEWS.io Questions API
  slug: reviews-io-questions-api
- baseURL: https://api.reviews.io
  baseurl_source: declared
  description: Aggregate product ratings and review statistics.
  name: REVIEWS.io Ratings API
  slug: reviews-io-ratings-api
- baseURL: https://api.reviews.io
  baseurl_source: declared
  description: Manage review-submitted webhook subscriptions.
  name: REVIEWS.io Webhooks API
  slug: reviews-io-webhooks-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: REVIEWS.io API
  slug: open-reviews-io
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/reviews-io/refs/heads/main/agentic-access/reviews-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/reviews-io-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/reviews-io/refs/heads/main/security/reviews-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reviews-io-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/reviews-io/refs/heads/main/authentication/reviews-io-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/reviews-io/refs/heads/main/plans/reviews-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/reviews-io-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/reviews-io/refs/heads/main/rate-limits/reviews-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/reviews-io-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/reviews-io/refs/heads/main/finops/reviews-io-finops.yml
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
overview: 'REVIEWS.io publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Company Reviews API, Invitations API, Product Reviews API, and 3 more. Tagged areas include Reviews, UGC, Ratings, Reputation, and E-Commerce.


  REVIEWS.io''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Reviews Io Plans Pricing
  plan_count: 5
  slug: reviews-io-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 4
  name: Reviews Io Rate Limits
  slug: reviews-io-rate-limits
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 11
    catalog_earned: 61.6
    catalog_earned_first_party: 0.0
    catalog_gap: 53.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 36.3
    contract_governance: 0.0
    contract_quality: 47.8
    developer_ergonomics: 27.4
    discoverability: 66.1
    operational_transparency: 31.1
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/reviews-io/refs/heads/main/screenshots/reviews-io-2026-09-02T153719.png
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
- E-Commerce
website: https://www.reviews.io
---
