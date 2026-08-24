---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Array's REST API for embedded consumer-credit, identity and background-data products. Confirmed live at https://array.io/api — the /api/user/v2 and /api/report/v2 routes answer with structured JSON va
  name: Array API
  slug: array-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/array-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://array.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://array.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.array.com
- group: other
  title: ''
  type: Deployment
  url: https://array.com/deployment
- group: commercial
  title: ''
  type: Pricing
  url: https://array.com/product-pricing/all-features
- group: operate
  title: ''
  type: Support
  url: https://array.com/help
- group: company
  title: ''
  type: Blog
  url: https://array.com/company/newsroom
- group: company
  title: ''
  type: About
  url: https://array.com/company/about-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://array.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://array.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.array.com
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/array-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/array-llms.txt
- group: design
  title: ''
  type: Components
  url: components/array-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/array-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/array-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/array-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/array-problem-types.yml
- group: build
  title: ''
  type: Packages
  url: packages/array-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/array-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/array-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/array-plans-pricing.yml
created: '2026-07-17'
description: Array is an embedded fintech products platform that lets financial institutions, fintechs, credit-service companies, and consumer brands seamlessly integrate consumer credit, identity, and background data into their own user experiences and marketing funnels. Array packages products such as credit scores and monitoring (My Credit Manager), identity and privacy protection, background checks, credit building (BuildCredit), debt management and navigation, an offers engine, property and home-value data, and a subscription manager, delivered as embeddable white-label components, private- label experiences, and APIs so clients can drive engagement, conversion, revenue, and consumer financial progress. Headquartered in New York City and led by CEO Martin Toha, Array is backed by investors including General Catalyst. Array's production API is served from https://array.io/api with a mirrored sandbox at https://sandbox.array.io/api, and its embeddable web components load from https://embed.array.io.
  This profile was seeded from a VC portfolio lead and enriched from Array's public website, its live API error responses, its Statuspage API and its public embed loader; its developer documentation (docs.array.com, on ReadMe) is password-protected at every path, so the OpenAPI specification and Postman collection Array advertises there could not be harvested.
image: https://array.com/assets/array-featured-image.png
layout: provider
modified: '2026-08-10'
name: Array
nav: Providers
network: true
overview: 'Array publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Embedded Finance, Credit Data, and Identity.


  Array''s developer surface includes documentation, pricing, support, engineering blog, authentication, sandbox, and 17 more developer resources.'
plans:
- name: Array Plans Pricing
  plan_count: 0
  slug: array-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Array Rate Limits
  slug: array-rate-limits
score:
  band: emerging
  composite: 25.5
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 25.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/array/refs/heads/main/screenshots/array-2026-07-25T201251.png
security:
- kind: authentication
  name: Array Authentication
  slug: array-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Array Domain Security
  slug: array-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: array
tags:
- Company
- Fintech
- Embedded Finance
- Credit Data
- Identity
- Background Checks
- Credit Monitoring
- Consumer Data
- Financial-Services
website: https://array.com
---
