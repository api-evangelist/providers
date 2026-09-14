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
api_count: 1
apis:
- description: 'TradeBB exposes a single publicly consumable machine-readable interface: an llms.txt file designed for LLM consumption. There is no public REST/GraphQL API, MCP server, or agent skills.'
  name: TradeBB
  slug: tradebb
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.tradebb.ai/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tradebb-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tradebb-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/tradebb-conformance.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.tradebb.ai/help-center
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tradebb.ai/help-center/getting-started/how-to-import-your-first-trades
- group: operate
  title: ''
  type: Support
  url: https://www.tradebb.ai/contact
- group: company
  title: ''
  type: Blog
  url: https://www.tradebb.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tradebb.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.tradebb.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.tradebb.ai/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tradebb.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tradebb.ai/privacy-policy
coverage:
  checked: '2026-08-09'
  detail: TradeBB is an end-user trading-journal SaaS with no developer program at all — the only machine-readable document it serves is /llms.txt, its api.tradebb.ai backend answers every probed path with a 404 problem+json, and the apis.json the submitter cited does not exist.
  evidence:
  - status: 200
    url: https://www.tradebb.ai/llms.txt
  - status: 404
    url: https://www.tradebb.ai/apis.json
  - status: 404
    url: https://api.tradebb.ai/openapi.json
  - status: 404
    url: https://www.tradebb.ai/developers
  - status: 404
    url: https://www.tradebb.ai/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-08-03'
description: An automated, AI-assisted trading journal and trade-analysis tool that imports, syncs, reviews, and analyzes trades across stocks, options, futures, forex, crypto, CFD, and multi-asset markets. Offers broker-file import, read-only broker sync, performance dashboards, and a Mentor Mode for coaches and educators.
image: https://static.tradebb.ai/20251121/home.webp
layout: provider
modified: '2026-08-09'
name: TradeBB
nav: Providers
network: true
overview: 'TradeBB publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include trading-journal, Trade Analytics, Fintech, trading-tools, and Stocks.


  TradeBB''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 7 more developer resources.'
random_paper: 10
screenshot: https://raw.githubusercontent.com/api-evangelist/tradebb/refs/heads/main/screenshots/tradebb-2026-09-02T164042.png
security:
- kind: domain-security
  name: Tradebb Domain Security
  slug: tradebb-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tradebb
tags:
- trading-journal
- Trade Analytics
- Fintech
- trading-tools
- Stocks
- Options
- Futures
- Forex
- Crypto
- CFD
- AI Assistant
- llms-txt
website: https://www.tradebb.ai/
---
