---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The GoSite developer API, marketed at developers.gosite.com in two families — Business Growth APIs (online presence, listings, lead generation) and Business Management APIs (scheduling, invoicing, pay
  name: GoSite API
  slug: gosite-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.gosite.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.gosite.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.gosite.com/api-access
- group: docs
  title: ''
  type: Documentation
  url: https://help.gosite.com/en/knowledge-base
- group: operate
  title: ''
  type: Support
  url: https://help.gosite.com/en/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://www.gosite.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gosite.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.gosite.com/signup
- group: start
  title: ''
  type: Login
  url: https://cloud.gosite.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gosite.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gosite.com/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/gosite-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gosite-rate-limits.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gosite-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gosite-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gosite-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gosite-llms.txt
coverage:
  checked: '2026-08-22'
  detail: GoSite's developer portal requires a paid GoSite customer account plus an approved "request API access" form before it will issue the API key needed to view its Swagger reference, and the reference host that form points at (https://api.developers.gosite.com/docs/) has additionally gone to nginx 502 Bad Gateway on every path, so no contract is reachable even to a would-be applicant.
  evidence:
  - status: 200
    url: https://developers.gosite.com/api-access
  - status: 502
    url: https://api.developers.gosite.com/docs/
  - status: 401
    url: https://api.gosite.com/openapi.json
  - status: 200
    url: https://developer.gosite.com/
  reason: sales-gate
  state: gated
created: '2026-08-22'
description: 'GoSite is a San Diego, California software company that sells an all-in-one digital presence and business-management platform to local service businesses — HVAC, plumbing, electrical, handyman, home cleaning, locksmith, moving, auto detailing, landscaping and pest control operators. The platform bundles a done-for-you website and domain, online directory and Google Business Profile listing management, review generation, a unified Messenger inbox, appointment booking and scheduling, contactless payments, invoicing, and a Contact Hub CRM, delivered through a web app and iOS/Android mobile apps. GoSite markets a developer program at developers.gosite.com covering "Business Growth" and "Business Management" APIs, with Contact Hub (CRUD over contacts) listed as the available surface and Sites, Placements, Invoices and Emails listed as coming soon. Access to the API is approval-gated: a prospective integrator must create a GoSite customer account, submit a request-access form, and
  be issued an API key before the Swagger reference can be used. The company has raised roughly $60M from Left Lane Capital and Longley Capital and remains privately held and independently operated.'
image: https://dufzo4epsnvlh.cloudfront.net/image/gosite_logo.png
layout: provider
modified: '2026-08-22'
name: GoSite
nav: Providers
network: true
overview: 'GoSite publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Small Business, Local Services, Website Builder, and Reputation Management.


  GoSite''s developer surface includes getting-started guide, documentation, support, engineering blog, pricing, signup flow, authentication, and 10 more developer resources.'
plans:
- name: Gosite Plans Pricing
  plan_count: 2
  slug: gosite-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Gosite Rate Limits
  slug: gosite-rate-limits
score:
  band: thin
  composite: 30.4
  facets:
    access_clarity: 59.2
    commercial_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Gosite Authentication
  slug: gosite-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Gosite Domain Security
  slug: gosite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gosite
tags:
- Company
- Small Business
- Local Services
- Website Builder
- Reputation Management
- Reviews
- Messaging
- Scheduling
- Appointments
- Payments
- Invoicing
- CRM
- Contact Management
- Local SEO
- Home Services
- Field Service
website: https://www.gosite.com/
---
