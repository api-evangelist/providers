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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nomi-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nomi-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.nomihealth.com/
- group: company
  title: ''
  type: About
  url: https://www.nomihealth.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.nomihealth.com/blog
- group: company
  title: ''
  type: Press
  url: https://www.nomihealth.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.nomihealth.com/careers
- group: operate
  title: ''
  type: Support
  url: https://www.nomihealth.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.nomihealth.com/pc/join-the-network
- group: start
  title: ''
  type: Login
  url: https://app.nomihealth.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nomihealth.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nomihealth.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.nomihealth.com/security-controls
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nomi-health/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/nomihealth
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Nomi-Health-106470774923973/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/nomihealth/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/nomi-health_stock/
coverage:
  checked: '2026-08-04'
  detail: Nomi Health ships its payments, claims and analytics platform only through authenticated tenant portals — app.nomihealth.com and provider.nomihealth.com are single-page apps that answer 200 with the same HTML shell for /openapi.json, /swagger.json and every /.well-known/ path — while developer., developers., docs. and api.nomihealth.com do not resolve in DNS, the published sitemap lists no developer or integration page, and the nomihealth GitHub account has zero public repositories.
  evidence:
  - status: 200
    url: https://www.nomihealth.com/sitemap.xml
  - status: 404
    url: https://www.nomihealth.com/llms.txt
  - status: 404
    url: https://www.nomihealth.com/.well-known/security.txt
  - status: 200
    url: https://app.nomihealth.com/openapi.json
  - status: 200
    url: https://api.github.com/users/nomihealth/repos
  reason: no-developer-program
  state: none
created: '2026-08-04'
description: Nomi Health is a Utah-based direct healthcare and healthcare fintech company founded in 2019 that operates a payments, claims and analytics platform for self-funded employers, health plans, brokers and providers. Its stack spans real-time provider payments and claims adjudication (Healthcare Financial Services), directly contracted provider networks (Direct Network / Open Network), benefits-data analytics through Artemis by Nomi Health, and direct patient care services. Nomi Health operates authenticated web portals for providers, members and employers, but publishes no public developer program, API reference, or machine-readable specification.
image: https://cdn.prod.website-files.com/6536dc5e6afea703703d0814/6536e93a7fa28173391ba2ab_App%201%202.jpg
layout: provider
modified: '2026-08-04'
name: Nomi Health
nav: Providers
network: true
overview: 'Nomi Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Payments, and Financial Services.


  Nomi Health''s developer surface includes engineering blog, support, signup flow, and 15 more developer resources.'
random_paper: 30
score:
  band: emerging
  composite: 17.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 28.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nomi-health/refs/heads/main/screenshots/nomi-health-2026-08-07T185444.png
security:
- kind: domain-security
  name: Nomi Health Domain Security
  slug: nomi-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nomi-health
tags:
- Company
- Health
- Healthcare
- Payments
- Financial Services
- Insurance
- Benefits
- Analytics
- Claims
website: https://www.nomihealth.com/
---
