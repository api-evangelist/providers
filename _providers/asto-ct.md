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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/asto-ct-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/asto-ct-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.astoct.com/
- group: company
  title: ''
  type: Blog
  url: https://www.astoct.com/news
- group: company
  title: ''
  type: BlogRSS
  url: https://www.astoct.com/news?format=rss
- group: operate
  title: ''
  type: Support
  url: https://www.astoct.com/support
- group: operate
  title: ''
  type: ContactInformation
  url: https://www.astoct.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.astoct.com/privacypolicy
- group: operate
  title: ''
  type: FAQ
  url: https://www.astoct.com/questions
- group: other
  title: ''
  type: CaseStudies
  url: https://www.astoct.com/case-studies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/asto-ct/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Equina_AstoCT
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCnVpRS5OYk0j-JKxihG0Tbw
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/astoct/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/asto-ct_stock/
coverage:
  checked: '2026-08-06'
  detail: Asto CT sells the Equina standing equine CT scanner as capital medical equipment operated from an on-site console; its 303-URL Squarespace sitemap has no developer, API or documentation section and every spec and .well-known probe on www.astoct.com returned 404.
  evidence:
  - status: 404
    url: https://www.astoct.com/openapi.json
  - status: 404
    url: https://www.astoct.com/.well-known/agent-card.json
  - status: 404
    url: https://www.astoct.com/.well-known/security.txt
  - status: 200
    url: https://www.astoct.com/sitemap.xml
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Asto CT, Inc. is a Middleton, Wisconsin medical-imaging device manufacturer that designs and builds Equina, a robotically positioned, weight-bearing fan-beam computed tomography (CT) scanner purpose-built for imaging mildly sedated, standing horses. Founded on a 2016 concept and first installed at UW-Madison in 2019, the company sells capital imaging equipment plus installation, training and ongoing clinical support to equine hospitals and veterinary teaching hospitals worldwide, with offices in Middleton, Wisconsin and Crawley, United Kingdom. Asto CT is a hardware company: the Equina system is operated from an on-site console and the company publishes no public developer program, API, SDK or machine-readable interface contract.'
image: https://static1.squarespace.com/static/561fb278e4b048525fcf098f/t/6830bc104e0f7274d551e013/1748024336785/6.png?format=1500w
layout: provider
modified: '2026-08-06'
name: Asto CT
nav: Providers
network: true
overview: 'Asto CT is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Medical Imaging, Veterinary, and Equine Health.


  Asto CT''s developer surface includes engineering blog, support, FAQ, YouTube channel, and 11 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 7.6
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/asto-ct/refs/heads/main/screenshots/asto-ct-2026-08-07T161836.png
security:
- kind: domain-security
  name: Asto Ct Domain Security
  slug: asto-ct-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: asto-ct
tags:
- Company
- Medical Devices
- Medical Imaging
- Veterinary
- Equine Health
- Computed Tomography
- Healthcare
- Hardware
website: https://www.astoct.com/
---
