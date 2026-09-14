---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bizzycar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bizzycar.com/
- group: company
  title: ''
  type: Blog
  url: https://www.bizzycar.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.bizzycar.com/support
- group: start
  title: ''
  type: Login
  url: https://www.portal.bizzycar.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bizzycar.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bizzycar.com/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bizzycar
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bizzycar-llms.txt
coverage:
  checked: '2026-08-07'
  detail: api.bizzycar.com is live but is BizzyCar's own application backend, not a product — every contract path (/openapi.json, /swagger.json, /api-docs, /graphql) returns the app's Rails JSON 404 envelope, none of the 238 URLs in the sitemap is a developer, docs or API page, and there is no bizzycar GitHub org or package on any registry; BizzyCar sells the DMS connectors it consumes, not an API it exposes.
  evidence:
  - status: 404
    url: https://api.bizzycar.com/openapi.json
  - status: 404
    url: https://api.bizzycar.com/graphql
  - status: 200
    url: https://www.bizzycar.com/sitemap.xml
  - status: 404
    url: https://api.github.com/orgs/bizzycar
  reason: no-developer-program
  state: none
created: '2026-08-07'
description: 'BizzyCar is a B2B SaaS platform for automotive dealerships that automates service recall management, customer outreach and mobile service. Founded in 2018 and headquartered in Saint Peters, Missouri, the company ingests VIN-level open-recall data from OEM partners, matches it against a dealer''s market area and DMS records, then uses AI-driven outreach (SMS, email, voice) to book service appointments and dispatch mobile service vans. Products include Recall Outreach, Recall Scout, Recall Radar, Service Engine, Mobile Service and Fleet IQ. BizzyCar is primarily an API *consumer* rather than an API producer: it ships pre-built connectors into dealer management systems (Dealertrack, DMS Plus, Open/Mate, Asbury, PBS, Tekion, Fortellis, Reynolds & Reynolds) and service schedulers (Xtime, TCC, DealerFX, Affinitiv, Update Promise), but publishes no public developer program, API reference or machine-readable contract of its own.'
image: https://www.bizzycar.com/hubfs/1.%201200x630.png
layout: provider
modified: '2026-08-07'
name: BizzyCar
nav: Providers
network: true
overview: 'BizzyCar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Automotive, Recall Management, Dealerships, and Mobile Service.


  BizzyCar''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 17
screenshot: https://raw.githubusercontent.com/api-evangelist/bizzycar/refs/heads/main/screenshots/bizzycar-2026-08-07T162605.png
security:
- kind: domain-security
  name: Bizzycar Domain Security
  slug: bizzycar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bizzycar
tags:
- Company
- Automotive
- Recall Management
- Dealerships
- Mobile Service
- Vehicle Service
- Fleet Management
- Scheduling
- Software-as-a-Service
website: https://www.bizzycar.com/
---
