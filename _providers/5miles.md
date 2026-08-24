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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/5miles-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/5miles-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.5miles.com/
- group: company
  title: ''
  type: About
  url: https://www.5miles.com/info/about
- group: operate
  title: ''
  type: Support
  url: https://www.5miles.com/info/support
- group: company
  title: ''
  type: Press
  url: https://www.5miles.com/press
- group: company
  title: ''
  type: News
  url: https://www.5miles.com/info/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.5miles.com/info/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.5miles.com/info/privacy
- group: other
  title: ''
  type: iOSApp
  url: https://apps.apple.com/us/app/id917554930
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.thirdrock.fivemiles
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/5miles-llc
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/5miles
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/5miles_stock/
coverage:
  checked: '2026-08-05'
  detail: 5miles ships only consumer iOS, Android and web marketplace products — /developers, /docs and every OpenAPI, GraphQL, MCP and .well-known discovery path on api.5miles.com return 404, and www.5miles.com/robots.txt disallows all crawlers.
  evidence:
  - status: 404
    url: https://www.5miles.com/developers
  - status: 404
    url: https://api.5miles.com/openapi.json
  - status: 404
    url: https://api.5miles.com/graphql
  - status: 404
    url: https://www.5miles.com/.well-known/agent-card.json
  - status: 200
    url: https://www.5miles.com/robots.txt
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: '5miles is a hyper-local mobile marketplace for buying and selling used goods — cars, furniture, electronics, fashion, baby and kids items — and for offering local services such as beauty, auto repair and home cleaning. Founded in 2014 in Dallas, Texas by Lucas Lu and acquired by a China-based buyer in 2020, the company runs the 5miles iOS and Android apps, the 5miles.com web marketplace, and the 5miles Dash bidding site. 5miles operates as an end-user consumer product only: it publishes no developer portal, no API reference and no machine-readable specification, and its api.5miles.com host serves the company''s own mobile and web clients rather than third-party integrators.'
image: https://www.5miles.com/images/logoOrange_nosub.png
layout: provider
modified: '2026-08-05'
name: 5miles
nav: Providers
network: true
overview: '5miles is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Classifieds, E-Commerce, and Local Commerce.


  5miles'' developer surface includes support, product news, and 12 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 10.9
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.9
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/5miles/refs/heads/main/screenshots/5miles-2026-08-07T160708.png
security:
- kind: domain-security
  name: 5Miles Domain Security
  slug: 5miles-domain-security
  summary_line: TLSv1.3
slug: 5miles
tags:
- Company
- Marketplace
- Classifieds
- E-Commerce
- Local Commerce
- Mobile Apps
- Consumer
- Secondhand
website: https://www.5miles.com/
---
