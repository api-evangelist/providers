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
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-02'
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
artifact_total: 26
collections:
- collection_type: open
  name: Trend API - 1.28.31
  slug: open-trend-api
common:
- group: other
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
  title: ''
  type: OpenAPI
  url: openapi/trend-api-openapi.yml
- group: docs
  title: ''
  type: APIReference
  url: https://api.trend.io/docs-json
- group: auth
  title: ''
  type: Authentication
  url: authentication/trend-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/trend-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/trend-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/trend-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/trend-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/trend-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/trend-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/trend-rate-limits.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/trend-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/trend-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/trend-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trend-domain-security.yml
created: '2026-07-17'
description: Trend (branded "Trend by soona") is a user-generated content (UGC) platform that connects brands with a network of vetted independent creators to produce custom photo and video content — product and lifestyle photography, testimonial, unboxing, and product-in-action videos — optimized for TikTok, Instagram, Facebook, YouTube, and Amazon. Brands post a creative brief, hire creators from a network of 3,700+, and receive full licensing and distribution rights to the delivered content. Pricing is credit-based with no subscriptions or contracts. Trend is part of soona.co. It was surfaced as a 500 Global portfolio company and added to the API Evangelist network. Trend publishes no developer program or developer portal, but the platform's own NestJS backend at api.trend.io serves a public, machine-readable OpenAPI 3.0 document at /docs-json covering 124 operations across brands, campaigns, creators, partnerships, content submission, messaging, shipments, AI image generation, and Stripe
  credit purchases. The Swagger UI at /docs is password-protected; the specification behind it is not.
image: https://cdn.prod.website-files.com/62c13e3f6b73683c91c0df7c/649ae4e9626c096bdb7ca6ca_trend-by-soona-black.svg
layout: provider
mcp_servers:
- description: ''
  name: Trend MCP Server
  slug: trend-mcp-server
modified: '2026-08-13'
name: Trend
nav: Providers
network: true
overview: 'Trend publishes 20 APIs on the [APIs.io](https://apis.io/) network, including AI API, Auth API, Basic Authentication (AI) API, and 17 more. Tagged areas include Company, User Generated Content, Creator Economy, Content Marketing, and Video Production.


  Trend''s developer surface includes pricing, signup flow, support, engineering blog, API reference, authentication, and 19 more developer resources.'
plans:
- name: Trend Plans Pricing
  plan_count: 4
  slug: trend-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Trend Rate Limits
  slug: trend-rate-limits
score:
  band: developing
  composite: 40.3
  coverage:
    artifact_dirs: 19
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 42.8
    developer_ergonomics: 28.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 40.3
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
