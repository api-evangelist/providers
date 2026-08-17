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
  url: security/startengine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.startengine.com/
- group: company
  title: ''
  type: About
  url: https://www.startengine.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.startengine.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.startengine.com/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.startengine.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://user.startengine.com/signup
- group: start
  title: ''
  type: Login
  url: https://user.startengine.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.startengine.com/secure
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.startengine.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.startengine.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/StartEngine
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/startengine_stock/
- group: build
  title: ''
  type: Packages
  url: packages/startengine-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/startengine-llms.txt
coverage:
  checked: '2026-08-05'
  detail: StartEngine ships an investor app and the StartEngine Secure cap-table product to end users only; api.startengine.com, developer.startengine.com and docs.startengine.com all return NXDOMAIN, and www.startengine.com/robots.txt disallows /api for every crawler because the only /api path is the site's own internal backend.
  evidence:
  - status: 200
    url: https://www.startengine.com/robots.txt
  - status: 404
    url: https://www.startengine.com/api/openapi.json
  - status: 404
    url: https://www.startengine.com/api-docs
  - status: 500
    url: https://status.startengine.com/
  reason: no-developer-program
  state: none
created: '2026-08-05'
description: StartEngine is a Los Angeles based online private-market investment platform that lets everyday investors buy equity in startups and pre-IPO companies, and lets founders raise capital under Regulation Crowdfunding, Regulation A+ and Regulation D. The company operates StartEngine Capital, its FINRA-registered funding portal; StartEngine Private, a fund vehicle for later-stage pre-IPO companies; a secondary marketplace for trading eligible private shares; and StartEngine Secure, an SEC-registered transfer agent and cap-table management service sold to issuers on a published monthly plan. StartEngine publishes no public developer API, SDK, webhook catalog or developer portal - its public engineering output is an internal design-system npm scope, agent examples, and Ethereum security-token standards work (the ERC-1450 reference implementation).
image: https://d17th0s7i8wl11.cloudfront.net/SE_Thumbnail_5d5cb9e21b.png
layout: provider
modified: '2026-08-05'
name: StartEngine
nav: Providers
network: true
overview: 'StartEngine is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Investing, Crowdfunding, Private Markets, and Capital Markets.


  StartEngine''s developer surface includes engineering blog, support, signup flow, pricing, and 11 more developer resources.'
random_paper: 145
score:
  band: emerging
  composite: 18.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 18.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Startengine Domain Security
  slug: startengine-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: startengine
tags:
- Company
- Investing
- Crowdfunding
- Private Markets
- Capital Markets
- Financial Services
- Transfer Agent
- Securities
website: https://www.startengine.com/
---
