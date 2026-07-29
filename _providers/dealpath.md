---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Dealpath's REST API for programmatic access to deals, pipeline, and portfolio data. Bearer-token authentication (token provisioned by Dealpath); responses are JSON and advertise X-RateLimit-* headers.
  name: Dealpath API
  slug: dealpath-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://dealpath.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dealpath.stoplight.io/docs/dealpath-api
- group: docs
  title: ''
  type: Documentation
  url: https://dealpath.stoplight.io/docs/dealpath-api
- group: docs
  title: ''
  type: APIReference
  url: https://dealpath.stoplight.io/docs/dealpath-api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dealpath.com/plans/
- group: start
  title: ''
  type: Login
  url: https://app.dealpath.com/account/login
- group: start
  title: ''
  type: SignUp
  url: https://www.dealpath.com/request-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dealpath.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dealpath.com/privacy/
- group: company
  title: ''
  type: Blog
  url: https://www.dealpath.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dealpath
- group: auth
  title: ''
  type: Authentication
  url: authentication/dealpath-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dealpath-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dealpath-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dealpath-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dealpath-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dealpath-llms.txt
created: '2026-07-17'
description: Dealpath is an AI-powered deal management platform for commercial real estate investing, used by 300+ institutional firms to centralize deal data, automate workflows, and surface analytics across the full investment lifecycle from sourcing and pipeline management through underwriting, due diligence, IC approval, close, and portfolio insights. Its product areas include market tracking and comps, Dealpath Connect deal sourcing, pipeline visibility, deal execution, reporting dashboards, relationship/CRM management, and Dealpath AI. Dealpath exposes a bearer-token REST API at api.dealpath.com (documented on Stoplight) so customers can programmatically feed opportunities into their pipeline and establish bidirectional data flows with other business systems.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dealpath.png
layout: provider
modified: '2026-07-18'
name: Dealpath
nav: Providers
network: true
overview: 'Dealpath publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, PropTech, Deal Management, and Commercial Real Estate.


  Dealpath''s developer surface includes documentation, API reference, pricing, signup flow, engineering blog, authentication, and 11 more developer resources.'
random_paper: 45
rate_limits:
- limit_count: 0
  name: Dealpath Rate Limits
  slug: dealpath-rate-limits
score:
  band: emerging
  composite: 25.7
  delta: -0.6
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 37.0
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dealpath/refs/heads/main/screenshots/dealpath-2026-07-25T211514.png
security:
- kind: authentication
  name: Dealpath Authentication
  slug: dealpath-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dealpath Domain Security
  slug: dealpath-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dealpath
tags:
- Company
- Real Estate
- PropTech
- Deal Management
- Commercial Real Estate
- Investment Management
- Real Estate Technology
- API
website: https://dealpath.com
---
