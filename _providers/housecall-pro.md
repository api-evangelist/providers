---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
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
  score: 33.8
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Housecall Pro Public API is a REST + JSON API hosted on Stoplight that gives MAX-plan customers programmatic access to core platform resources — customers, leads, jobs, estimates, invoices, paymen
  name: Housecall Pro Public API
  slug: housecall-pro-public-api
artifact_total: 29
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/housecall-pro/overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/housecall-pro-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.housecallpro.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.housecallpro.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.housecallpro.com/en/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.housecallpro.com/en/articles/8505035-api-overview
- group: auth
  title: ''
  type: Authentication
  url: https://docs.housecallpro.com/docs/housecall-public-api/ZG9jOjU4NjM4-authentication
- group: design
  title: ''
  type: Webhooks
  url: https://docs.housecallpro.com/docs/housecall-public-api/46e9e1be07621-webhooks
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.housecallpro.com/docs/housecall-public-api/06ba3d648e345-changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.housecallpro.com/pricing/
- group: start
  title: ''
  type: Signup
  url: https://www.housecallpro.com/free-trial/
- group: start
  title: ''
  type: Login
  url: https://pro.housecallpro.com/pro/login
- group: company
  title: ''
  type: Blog
  url: https://www.housecallpro.com/resources/
- group: operate
  title: ''
  type: PressReleases
  url: https://www.housecallpro.com/news/
- group: company
  title: ''
  type: AboutUs
  url: https://www.housecallpro.com/about/
- group: other
  title: ''
  type: Leadership
  url: https://www.housecallpro.com/about/leadership/
- group: company
  title: ''
  type: Careers
  url: https://www.housecallpro.com/careers/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.housecallpro.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.housecallpro.com/privacy-policy/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.housecallpro.com/contact-us/
- group: operate
  title: ''
  type: Support
  url: https://help.housecallpro.com/en/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/housecallpro/
- group: other
  title: ''
  type: XHandle
  url: https://twitter.com/housecallpro
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/housecallpro
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/housecallpro/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/HousecallPro
- group: other
  title: ''
  type: AppStoreiOS
  url: https://apps.apple.com/us/app/housecall-pro/id814134276
- group: other
  title: ''
  type: AppStoreAndroid
  url: https://play.google.com/store/apps/details?id=com.housecallpro.app
- group: operate
  title: ''
  type: Forums
  url: https://www.facebook.com/groups/superprocommunity/
- group: commercial
  title: ''
  type: Plans
  url: plans/housecall-pro-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/housecall-pro-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/housecall-pro-finops.yml
created: '2026-05-25'
description: Housecall Pro is an all-in-one home services business management platform headquartered in Denver, Colorado (with offices in San Diego), founded in 2013 by Ian Heidt, Roland Ligtenberg, Reza Olfat, Adam Perry-Pelletier, and Chris Zwickilton under the parent entity Codefied Inc. The platform serves 200K+ residential and commercial service pros across 50+ trades — HVAC, plumbing, electrical, cleaning, landscaping, pest control, garage doors, locksmiths, appliance repair, and more — providing scheduling, dispatching, online booking, estimates, invoicing, payments, marketing, GPS fleet tracking, customer communications, recurring service plans, and an AI-powered call answering agent. Developer integrations are exposed via the Housecall Pro Public API, available on the MAX plan, with Stoplight-hosted documentation, bearer-token API keys, multi- location key scoping, and webhook subscriptions for customer, estimate, invoice, job, lead, and payment events.
features:
- Scheduling and dispatching for field service teams
- Online booking widget for the company website
- Estimates with multi-option (good/better/best) approval flow
- Invoicing with sent, paid, voided, and refunded statuses
- Integrated payment processing (cards, ACH, financing)
- Recurring service plans and maintenance agreements
- Employee GPS tracking and dispatch board
- QuickBooks Online integration
- HCP AI for call answering and job booking
- Postcard and email marketing
- Customer equipment tracking
- Premium review management
- Visual price book
- Sales proposal tool (add-on)
- Multi-location support with single-key API access
- Public REST API at api.housecallpro.com (MAX plan)
- Webhook subscriptions for customer, estimate, invoice, job, lead, and payment events
- Webhook payload signing secret for verification
- 14-day full-MAX free trial
finops:
- name: Housecall Pro Finops
  service_category: Business Applications
  slug: housecall-pro-finops
image: https://static-assets.housecallpro.com/brand/logos/square-door-only.svg
json_schemas:
- name: Housecall Pro Customer
  property_count: 14
  slug: housecall-pro-customer
- name: Housecall Pro Invoice
  property_count: 9
  slug: housecall-pro-invoice
- name: Housecall Pro Job
  property_count: 14
  slug: housecall-pro-job
jsonld:
- class_count: 35
  name: Housecall Pro Context
  property_count: 0
  slug: housecall-pro-context
layout: provider
modified: '2026-05-25'
name: Housecall Pro
nav: Providers
network: true
overview: 'Housecall Pro publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include Home Services, Field Service Management, Scheduling, Dispatching, and Invoicing.


  The Housecall Pro catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Housecall Pro''s developer surface includes developer portal, documentation, getting-started guide, authentication, changelog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Housecall Pro Plans Pricing
  plan_count: 3
  slug: housecall-pro-plans-pricing
random_paper: 46
rate_limits:
- limit_count: 0
  name: Housecall Pro Rate Limits
  slug: housecall-pro-rate-limits
rules:
- name: Housecall Pro API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: housecall-pro-jsonschema-spectral-rules
score:
  band: strong
  composite: 57.8
  delta: -5.7
  facets:
    commercial_clarity: 84.2
    contract_quality: 69.4
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 23.7
  previous_composite: 63.5
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/housecall-pro/refs/heads/main/screenshots/housecall-pro-2026-06-20T182849.png
security:
- kind: domain-security
  name: Housecall Pro Domain Security
  slug: housecall-pro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: housecall-pro
tags:
- Home Services
- Field Service Management
- Scheduling
- Dispatching
- Invoicing
- Payments
- HVAC
- Plumbing
- Electrical
- Cleaning
- Landscaping
- Pest Control
- SaaS
website: https://www.housecallpro.com
---
