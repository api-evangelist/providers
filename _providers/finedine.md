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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finedine-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finedine-llms.txt
- group: company
  title: ''
  type: Website
  url: https://finedinemenu.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.finedinemenu.com/en/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.finedinemenu.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.finedinemenu.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.finedinemenu.com/en/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.finedinemenu.com/en/privacy-and-terms/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.finedinemenu.com/en/privacy-and-terms/
- group: operate
  title: ''
  type: Support
  url: mailto:info@finedinemenu.com
created: '2026-07-17'
description: FineDine is an AI-powered restaurant growth platform that helps restaurants increase revenue through digital menus (QR code, tablet, and web), online and in-venue ordering, reservations, a lite point-of-sale, CRM and loyalty programs, menu-engineering and pricing analytics, and an AI business agent (FineDine IQ). It markets to restaurants and hospitality operators with tiered SaaS pricing (Starter, Growth, Premium). As of this API Evangelist profiling, FineDine publishes no public developer API, SDKs, webhooks, CLI, MCP server, or OpenAPI specification — this profile captures its public commercial and content surface. FineDine is backed by 500 Global.
image: https://cdn.sanity.io/images/vzi1jds2/production/26c5de5d2314079d3ad75348594a6a74845e7cfa-2400x1260.png
layout: provider
modified: '2026-07-19'
name: FineDine
nav: Providers
network: true
overview: 'FineDine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Restaurants, Hospitality, Digital Menu, and Ordering.


  FineDine''s developer surface includes pricing, signup flow, engineering blog, support, and 6 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 16.0
  delta: -1.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/finedine/refs/heads/main/screenshots/finedine-2026-07-25T214517.png
security:
- kind: domain-security
  name: Finedine Domain Security
  slug: finedine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finedine
tags:
- Company
- Restaurants
- Hospitality
- Digital Menu
- Ordering
- Point of Sale
- Reservations
- Food and Beverage
- SaaS
website: https://finedinemenu.com
---
