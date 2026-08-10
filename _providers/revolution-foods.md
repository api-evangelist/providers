---
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
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revolution-foods-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revolution-foods-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.revolutionfoods.com/
- group: company
  title: ''
  type: About
  url: https://www.revolutionfoods.com/about/
- group: company
  title: ''
  type: Blog
  url: https://www.revolutionfoods.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.revolutionfoods.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.revolutionfoods.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.revolutionfoods.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://recruiting.ultipro.com/REV1004REVO/JobBoard/050bac60-1fcb-4b41-b850-38dc45d48f4b/
- group: start
  title: ''
  type: CustomerPortal
  url: https://centro.order.revfoods.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revolution-foods/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/RevolutionFoods/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/revolutionfoods/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@revolutionfoods8340
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/revolution-foods_stock/
coverage:
  checked: '2026-08-05'
  detail: Revolution Foods is a food manufacturer and meal-service operator — its product is 35 million prepared school and senior meals a year, not software — and its only digital surface is Centro, a customer ordering portal whose root 302s straight to an ASP.NET Identity login with no /swagger, /api or /openapi.json behind it.
  evidence:
  - status: 404
    url: https://www.revolutionfoods.com/developers
  - status: 404
    url: https://www.revolutionfoods.com/openapi.json
  - status: 302
    url: https://centro.order.revfoods.com/
  - status: 404
    url: https://centro.order.revfoods.com/swagger/v1/swagger.json
  - status: 404
    url: https://www.revolutionfoods.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/revolutionfoods
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: Revolution Foods is an Oakland, California food company founded in 2006 by Kristin Groos Richmond and Kirsten Saenz Tobey that manufactures and delivers nutritious, freshly prepared meals to schools and senior communities. It is the largest K-12 school meal vendor in California, serving more than 35 million meals a year across 800+ schools and senior centers, with programs spanning district and charter school food service, after-school and summer meals, senior center dining and homebound delivery. The company has been a Certified B Corporation since 2009 and a Public Benefit Corporation since 2021, and reports a 100% audit pass rate across NSLP, SBP, CACFP, SFSP and Title III compliance. Customers order through Centro, a login-gated web ordering portal; Revolution Foods publishes no public developer program, API documentation, or machine-readable specification of any kind.
image: https://www.revolutionfoods.com/wp-content/uploads/2025/10/revolution-foods-color.svg
layout: provider
modified: '2026-08-05'
name: Revolution Foods
nav: Providers
network: true
overview: 'Revolution Foods is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Food Service, Nutrition, and Meal Delivery.


  Revolution Foods'' developer surface includes engineering blog, YouTube channel, and 13 more developer resources.'
random_paper: 71
score:
  band: minimal
  composite: 8.3
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Revolution Foods Domain Security
  slug: revolution-foods-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: revolution-foods
tags:
- Company
- Food
- Food Service
- Nutrition
- Meal Delivery
- Education
- K-12
- Schools
- Senior Services
- B Corporation
- Public Benefit Corporation
website: https://www.revolutionfoods.com/
---
