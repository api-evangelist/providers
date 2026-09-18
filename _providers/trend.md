---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 21.8
  scored_at: '2026-09-17'
api_count: 2
apis:
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The AI API from Trend — 3 operation(s) for ai.
  name: Trend AI API
  slug: trend-ai-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Auth API from Trend — 2 operation(s) for auth.
  name: Trend Auth API
  slug: trend-auth-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Basic Authentication (AI) API from Trend — 5 operation(s) for basic authentication (ai).
  name: Trend Basic Authentication (AI) API
  slug: trend-basic-authentication-ai-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Brand Admin API from Trend — 7 operation(s) for brand admin.
  name: Trend Brand Admin API
  slug: trend-brand-admin-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Brand API from Trend — 10 operation(s) for brand.
  name: Trend Brand API
  slug: trend-brand-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Brand Authentication API from Trend — 7 operation(s) for brand authentication.
  name: Trend Brand Authentication API
  slug: trend-brand-authentication-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Campaign API from Trend — 19 operation(s) for campaign.
  name: Trend Campaign API
  slug: trend-campaign-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Content API from Trend — 9 operation(s) for content.
  name: Trend Content API
  slug: trend-content-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Creator API from Trend — 22 operation(s) for creator.
  name: Trend Creator API
  slug: trend-creator-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Creator Authentication API from Trend — 6 operation(s) for creator authentication.
  name: Trend Creator Authentication API
  slug: trend-creator-authentication-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Creator Portfolio API from Trend — 4 operation(s) for creator portfolio.
  name: Trend Creator Portfolio API
  slug: trend-creator-portfolio-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Creator Profiles API from Trend — 6 operation(s) for creator profiles.
  name: Trend Creator Profiles API
  slug: trend-creator-profiles-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Health Check API from Trend — 1 operation(s) for health check.
  name: Trend Health Check API
  slug: trend-health-check-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Message API from Trend — 6 operation(s) for message.
  name: Trend Message API
  slug: trend-message-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Metrics API from Trend — 1 operation(s) for metrics.
  name: Trend Metrics API
  slug: trend-metrics-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Partnership API from Trend — 12 operation(s) for partnership.
  name: Trend Partnership API
  slug: trend-partnership-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Payment API from Trend — 6 operation(s) for payment.
  name: Trend Payment API
  slug: trend-payment-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Review API from Trend — 1 operation(s) for review.
  name: Trend Review API
  slug: trend-review-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Shipment API from Trend — 3 operation(s) for shipment.
  name: Trend Shipment API
  slug: trend-shipment-api
- baseURL: https://api.trend.io
  baseurl_source: declared
  description: The Upload API from Trend — 2 operation(s) for upload.
  name: Trend Upload API
  slug: trend-upload-api
artifact_total: 25
collections:
- collection_type: open
  name: Trend API - 1.28.31
  slug: open-trend-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/capabilities/trend-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/trend-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://trend.io
- group: commercial
  title: ''
  type: Pricing
  url: https://trend.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.trend.io/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.trend.io/
- group: operate
  title: ''
  type: Support
  url: https://support.soona.co
- group: company
  title: ''
  type: Blog
  url: https://trend.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://soona.co/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://soona.co/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Trend-io
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/openapi/_original/trend-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/trend-api-openapi.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.trend.io/docs-json
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/authentication/trend-authentication.yml
  title: ''
  type: Authentication
  url: authentication/trend-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/conventions/trend-conventions.yml
  title: ''
  type: Conventions
  url: conventions/trend-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/data-model/trend-data-model.yml
  title: ''
  type: DataModel
  url: data-model/trend-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/errors/trend-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/trend-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/conformance/trend-conformance.yml
  title: ''
  type: Conformance
  url: conformance/trend-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/lifecycle/trend-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/trend-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/plans/trend-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/trend-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/rate-limits/trend-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/trend-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/mcp/trend-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/trend-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/overlays/trend-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/trend-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/llms/trend-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/trend-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/security/trend-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/trend-domain-security.yml
created: '2026-07-17'
description: Trend (branded "Trend by soona") is a user-generated content (UGC) platform that connects brands with a network of vetted independent creators to produce custom photo and video content — product and lifestyle photography, testimonial, unboxing, and product-in-action videos — optimized for TikTok, Instagram, Facebook, YouTube, and Amazon. Brands post a creative brief, hire creators from a network of 3,700+, and receive full licensing and distribution rights to the delivered content. Pricing is credit-based with no subscriptions or contracts. Trend is part of soona.co. It was surfaced as a 500 Global portfolio company and added to the API Evangelist network. Trend publishes no developer program or developer portal, but the platform's own NestJS backend at api.trend.io serves a public, machine-readable OpenAPI 3.0 document at /docs-json covering 124 operations across brands, campaigns, creators, partnerships, content submission, messaging, shipments, AI image generation, and Stripe
  credit purchases. The Swagger UI at /docs is password-protected; the specification behind it is not.
image: https://cdn.prod.website-files.com/62c13e3f6b73683c91c0df7c/649ae4e9626c096bdb7ca6ca_trend-by-soona-black.svg
layout: provider
modified: '2026-09-16'
name: Trend
nav: Providers
network: true
overview: 'Trend publishes 20 APIs on the [APIs.io](https://apis.io/) network, including AI API, Auth API, Basic Authentication (AI) API, and 17 more. Tagged areas include Company, User Generated Content, Creator Economy, Content Marketing, and Video Production.


  Trend''s developer surface includes pricing, signup flow, support, engineering blog, API reference, authentication, and 19 more developer resources.'
plans:
- name: Trend Plans Pricing
  plan_count: 4
  slug: trend-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Trend Rate Limits
  slug: trend-rate-limits
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 46.9
    developer_ergonomics: 28.0
    discoverability: 68.5
    operational_transparency: 2.6
  previous_composite: 40.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/trend/refs/heads/main/screenshots/trend-2026-08-17T082448.png
security:
- kind: authentication
  name: Trend Authentication
  slug: trend-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Trend Domain Security
  slug: trend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trend
tags:
- Company
- User Generated Content
- Creator Economy
- Content Marketing
- Video Production
- Photography
- Marketing
- E-Commerce
- Creator Marketplace
- Influencer Marketing
- AI Image Generation
- Payments
website: https://trend.io
---
