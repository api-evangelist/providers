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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.profitero.com
- group: company
  title: ''
  type: Blog
  url: https://www.profitero.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.profitero.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.profitero.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://app.profitero.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/profitero
- group: auth
  title: ''
  type: DomainSecurity
  url: security/profitero-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/profitero-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/profitero-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/profitero-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/profitero-llms.txt
coverage:
  checked: '2026-08-12'
  detail: 'Profitero''s CEO states on the company blog that technology partners "integrate directly with Profitero via API", but no reference for it exists on any public host — every surface that could carry it is a login: app.profitero.com 301s every path to /login.html, docs.profitero.com 302s to an internal Google Drive workspace, and help.profitero.com is a private Zendesk whose article API returns 401.'
  evidence:
  - status: 200
    url: https://www.profitero.com/blog/2020-09-why-we-launched-an-open-commerce-ecosystem-qa-with-profitero-ceo-bryan-wiener
  - status: 301
    url: https://app.profitero.com/api-docs
  - status: 302
    url: http://docs.profitero.com/
  - status: 401
    url: https://help.profitero.com/api/v2/help_center/en-us/articles.json
  - status: 404
    url: https://www.profitero.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-07-17'
description: Profitero+ is an eCommerce data, technology and services platform that helps consumer brands measure and grow their digital shelf presence across major retailers including Amazon, Walmart, Tesco and Target. It combines digital shelf analytics, Amazon sales and share measurement, content optimisation, retail media activation (Shelf Intelligent Media) and managed services, monitoring more than 1,400 retailer sites in 70+ countries for over 9,000 global brands. Founded in Dublin in 2010 and acquired by Publicis Groupe in March 2022, it now operates inside Publicis Commerce. Profitero was surfaced as a portfolio company of Seedcamp and added to the API Evangelist network. A partner API does exist — Profitero's own CEO wrote in 2020 that technology partners such as Kenshoo and Pacvue "integrate directly with Profitero via API" — but the company publishes no developer portal, API reference, OpenAPI or AsyncAPI definition, GraphQL endpoint, Postman collection, MCP server, agent card
  or SDK on any public host, and no pricing. Access runs through the Open Commerce Ecosystem partner programme and a sales demo request.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/profitero.png
layout: provider
modified: '2026-08-12'
name: Profitero
nav: Providers
network: true
overview: 'Profitero is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, eCommerce, Digital Shelf, Retail Analytics, and Retail Media.


  Profitero''s developer surface includes engineering blog, support, and 9 more developer resources.'
plans:
- name: Profitero Plans Pricing
  plan_count: 0
  slug: profitero-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 0
  name: Profitero Rate Limits
  slug: profitero-rate-limits
score:
  band: minimal
  composite: 10.9
  delta: -1.6
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Profitero Domain Security
  slug: profitero-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: profitero
tags:
- Company
- eCommerce
- Digital Shelf
- Retail Analytics
- Retail Media
- Consumer Brands
- Marketing Analytics
- Commerce Intelligence
- Publicis Groupe
website: https://www.profitero.com
---
