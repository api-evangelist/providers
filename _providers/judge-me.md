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
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Judge Me Agentic Access
  operation_count: 6
  slug: judge-me-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- description: Resolve external product handles or ids to internal Judge.me product ids.
  name: Judge.me Products API
  slug: judge-me-products-api
- description: Trigger review request emails to customers.
  name: Judge.me Review Requests API
  slug: judge-me-review-requests-api
- description: List and create product and store reviews.
  name: Judge.me Reviews API
  slug: judge-me-reviews-api
- description: Ready-to-render review widget HTML.
  name: Judge.me Widgets API
  slug: judge-me-widgets-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Judge.me Products API
  slug: open-judge-me-products-api
- collection_type: open
  name: Judge.me Products Widgets API
  slug: open-judge-me-widgets-api
- collection_type: open
  name: Judge.me API
  slug: open-judge-me
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/judge-me-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/judge-me-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/judge-me-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/judge-me
- group: company
  title: ''
  type: Website
  url: https://judge.me/
- group: docs
  title: ''
  type: Documentation
  url: https://judge.me/api/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/judge-me-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/judge-me-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/judge-me-finops.yml
created: '2026-06-25'
description: Judge.me is a product reviews platform for Shopify and other e-commerce storefronts, collecting photo and video reviews, star ratings, site reviews, and Q&A. The Judge.me REST API at https://judge.me/api/v1 lets developers list and import reviews, fetch ready-to-render widget HTML, resolve products, send review requests, and build OAuth apps authenticated with a shop_domain plus public or private api_token.
finops:
- name: Judge Me Finops
  service_category: Marketing and Commerce
  slug: judge-me-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/judge-me.png
layout: provider
modified: '2026-06-25'
name: Judge.me
nav: Providers
network: true
overview: 'Judge.me publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Products API, Review Requests API, Reviews API, and 1 more. Tagged areas include Reviews, E-commerce, Shopify, Ratings, and Social Proof.


  Judge.me''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Judge Me Plans Pricing
  plan_count: 2
  slug: judge-me-plans-pricing
random_paper: 37
rate_limits:
- limit_count: 2
  name: Judge Me Rate Limits
  slug: judge-me-rate-limits
score:
  band: thin
  composite: 34.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 58.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 34.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Judge Me Authentication
  slug: judge-me-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Judge Me Domain Security
  slug: judge-me-domain-security
  summary_line: TLSv1.3 · DMARC
slug: judge-me
tags:
- Reviews
- E-commerce
- Shopify
- Ratings
- Social Proof
website: https://judge.me/
---
