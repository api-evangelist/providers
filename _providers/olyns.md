---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/olyns-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://olyns.com/
- group: company
  title: ''
  type: About
  url: https://olyns.com/about-us
- group: company
  title: ''
  type: Blog
  url: https://olyns.com/news
- group: operate
  title: ''
  type: Support
  url: https://olyns.com/app/support
- group: start
  title: ''
  type: SignUp
  url: https://olyns.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://olyns.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://olyns.com/privacy-policy
- group: operate
  title: ''
  type: ContactUs
  url: https://olyns.com/contact-us
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/olyns-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/olyns-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/olyns-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/olyns-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Olyns ships software only as an end-user product — a consumer wallet SPA at app.olyns.com and a sign-in-gated self-service ad portal at ads.olyns.com — and its only API host, api.olyns.com, is a private application backend that answers GET /health with 200 but returns a hard 404 for /openapi.json, /swagger.json, /docs, /redoc, /graphql, /api-docs, ?wsdl and every /.well-known/* path, with no developer portal, API reference, SDK or published contract anywhere on the sitemap.
  evidence:
  - status: 200
    url: https://api.olyns.com/health
  - status: 404
    url: https://api.olyns.com/openapi.json
  - status: 404
    url: https://api.olyns.com/graphql
  - status: 404
    url: https://api.olyns.com/.well-known/agent-card.json
  - status: 404
    url: https://olyns.com/llms.txt
  - status: 404
    url: https://olyns.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/olyns
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Olyns is a Silicon Valley company, founded in 2019, that operates an AI-powered reverse vending and retail media network built around the Olyns Cube — a self-serve kiosk that accepts beverage containers and rigid plastic packaging, uses computer vision to identify and sort each item at the point of deposit, pays the consumer their deposit (CRV) refund electronically, and carries a 55-inch screen that Olyns sells as digital-out-of-home advertising inventory. Cubes are placed with supermarkets, big-box retailers, pharmacies and gas stations, and the advertising side is sold both directly and programmatically through Screenverse. Olyns ships consumer and operations software — a mobile/web wallet app at app.olyns.com and a self-service ad portal at ads.olyns.com — but publishes no public API, developer portal, SDK or machine-readable contract of any kind.
image: https://cdn.prod.website-files.com/60abbd1fb2acc04328ed01e7/60b7cf28487dad27361d72ed_olyns-icon-256.png
layout: provider
modified: '2026-08-26'
name: Olyns
nav: Providers
network: true
overview: 'Olyns is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recycling, Sustainability, Circular Economy, and Retail Media.


  Olyns'' developer surface includes engineering blog, support, signup flow, and 10 more developer resources.'
plans:
- name: Olyns Plans Pricing
  plan_count: 0
  slug: olyns-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Olyns Rate Limits
  slug: olyns-rate-limits
score:
  band: emerging
  composite: 16.2
  coverage:
    artifact_dirs: 8
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 16.2
  provenance:
    conformance: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Olyns Domain Security
  slug: olyns-domain-security
  summary_line: TLSv1.3 · HSTS
slug: olyns
tags:
- Company
- Recycling
- Sustainability
- Circular Economy
- Retail Media
- Digital Out Of Home
- Advertising
- Artificial Intelligence
- Reverse Vending
- Consumer
website: https://olyns.com/
---
