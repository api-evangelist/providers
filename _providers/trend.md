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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Trend platform API — the NestJS backend behind app.trend.io and the Trend creator app. It exposes 124 operations across brand accounts and approvals, campaign creation/submission/relisting, creato
  name: Trend API
  slug: trend-api
artifact_total: 7
collections:
- collection_type: open
  name: Trend API - 1.28.31
  slug: open-trend-api
common:
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
  name: trend-mcp.yml
  slug: trend-mcpyml
modified: '2026-08-13'
name: Trend
nav: Providers
network: true
overview: 'Trend publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, User-Generated Content, Creator Economy, Content Marketing, and Video Production.


  Trend''s developer surface includes pricing, signup flow, support, engineering blog, API reference, authentication, and 18 more developer resources.'
plans:
- name: Trend Plans Pricing
  plan_count: 4
  slug: trend-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 0
  name: Trend Rate Limits
  slug: trend-rate-limits
score:
  band: developing
  composite: 42.3
  delta: -1.4
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 42.0
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 43.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
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
- User-Generated Content
- Creator Economy
- Content Marketing
- Video Production
- Photography
- Marketing
- eCommerce
- Creator Marketplace
- Influencer Marketing
- AI Image Generation
- Payments
website: https://trend.io
---
