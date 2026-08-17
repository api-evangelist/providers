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
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clutch-canada-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clutch.ca
- group: company
  title: ''
  type: Blog
  url: https://www.clutch.ca/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clutchcanada
- group: operate
  title: ''
  type: Support
  url: https://www.clutch.ca/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.clutch.ca/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clutch.ca/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clutch.ca/privacy-policy
- group: company
  title: ''
  type: About
  url: https://www.clutch.ca/about
- group: company
  title: ''
  type: Careers
  url: https://job-boards.greenhouse.io/clutch
coverage:
  checked: '2026-08-09'
  detail: Clutch sells cars, not software — its only API host, api.clutch.ca, answers 403 Forbidden to every path including a nonsense control path, and www.clutch.ca has no developer portal at all (/developers and /api return the same 11,345-byte React shell as a random control URL), so there is no public developer program to document.
  evidence:
  - status: 403
    url: https://api.clutch.ca/v1
  - status: 403
    url: https://api.clutch.ca/zzz-control-9987
  - status: 200
    url: https://www.clutch.ca/developers
  - status: 404
    url: https://www.clutch.ca/llms.txt
  - status: 404
    url: https://www.clutch.ca/.well-known/agent-card.json
  - status: 404
    url: https://strapi.clutch.ca/documentation/v1.0.0/full_documentation.json
  reason: no-developer-program
  state: none
created: '2026-08-09'
description: 'Clutch is a Toronto-headquartered, vertically integrated online used-car retailer serving Canadian drivers. Unlike marketplace models that broker to third-party dealers, Clutch owns its own inventory and runs an end-to-end e-commerce purchase flow at clutch.ca: browsing reconditioned pre-owned vehicles, auto financing and a loan calculator, trade-in and sell-my-car offers, protection plans, insurance, and home delivery, backed by a 10-day money-back guarantee. It operates across Ontario, Nova Scotia, New Brunswick and Prince Edward Island. Clutch is a consumer retail business rather than an API vendor: its software is shipped as an end-user web application, and it publishes no public developer program, API reference, or machine-readable specification.'
image: https://www.clutch.ca/icons/android-chrome-512x512.png
layout: provider
modified: '2026-08-09'
name: Clutch Canada
nav: Providers
network: true
overview: 'Clutch Canada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, E-Commerce, Used Cars, and Auto Financing.


  Clutch Canada''s developer surface includes engineering blog, support, FAQ, and 7 more developer resources.'
random_paper: 96
score:
  band: minimal
  composite: 11.2
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Clutch Canada Domain Security
  slug: clutch-canada-domain-security
  summary_line: TLSv1.3 · DMARC
slug: clutch-canada
tags:
- Company
- Automotive
- E-Commerce
- Used Cars
- Auto Financing
- Retail
- Canada
- Consumer
website: https://www.clutch.ca
---
