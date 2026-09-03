---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - rate-limits
  - security
  trial: false
  try_now: false
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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mayan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mayan.co/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mayan.co/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.mayan.co/signup
- group: start
  title: ''
  type: Login
  url: https://app.mayan.co/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mayan.co/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mayan.co/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.mayan.co/contact
- group: company
  title: ''
  type: Blog
  url: https://www.mayan.co/blog-category/updates
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mayanco
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mayan.co/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trymayan
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCps7NamcWMEU5IxwJ5vvx1Q
- group: commercial
  title: ''
  type: Plans
  url: plans/mayan-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mayan-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mayan-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mayan-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/mayan-packages.yml
coverage:
  checked: '2026-08-26'
  detail: Mayan ships an Amazon-seller SaaS as an end-user web app only — its own sitemap enumerates marketing, pricing, blog, case-study and legal pages with no developer section, api.mayan.co and docs.mayan.co do not resolve in DNS, and every spec and /.well-known probe on www.mayan.co and app.mayan.co returned 404.
  evidence:
  - status: 200
    url: https://www.mayan.co/sitemap.xml
  - status: 404
    url: https://www.mayan.co/openapi.json
  - status: 404
    url: https://www.mayan.co/.well-known/api-catalog
  - status: 404
    url: https://app.mayan.co/openapi.json
  - status: 404
    url: https://www.mayan.co/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'Mayan is a Las Vegas, Nevada growth-automation platform for Amazon sellers, founded in 2020 and a Y Combinator W21 company. Its software pairs advertising optimization with inventory intelligence: automated Sponsored Products campaign creation, keyword and category targeting, competitor product targeting, placement adjustments, search expansion, pricing optimization, profit dashboards and replenishment alerts. It is sold self-serve as Copilot Lite (free) and the Smart Ads Platform, and as expert-managed Gold, Diamond and Enterprise engagements. Mayan is an official Amazon Ads partner and consumes Amazon''s Selling Partner and Advertising APIs; as of this profile it publishes no public API, developer portal, or machine-readable contract of its own.'
image: https://cdn.prod.website-files.com/63ea8205733cc93bcb2836e5/6407877bdecd95d7099abb69_mayan-256x256.png
layout: provider
modified: '2026-08-26'
name: Mayan
nav: Providers
network: true
overview: 'Mayan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Amazon, E-Commerce, Advertising, and Retail Media.


  Mayan''s developer surface includes pricing, signup flow, support, engineering blog, YouTube channel, and 13 more developer resources.'
plans:
- name: Mayan Plans Pricing
  plan_count: 5
  slug: mayan-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Mayan Rate Limits
  slug: mayan-rate-limits
score:
  band: emerging
  composite: 24.1
  coverage:
    artifact_dirs: 9
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 24.1
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mayan/refs/heads/main/screenshots/mayan-2026-09-02T150443.png
security:
- kind: domain-security
  name: Mayan Domain Security
  slug: mayan-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mayan
tags:
- Company
- Amazon
- E-Commerce
- Advertising
- Retail Media
- Marketing Automation
- Inventory Management
- Analytics
- Software-as-a-Service
website: https://www.mayan.co/
---
