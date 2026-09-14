---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: Reflexivity's institutional REST API. Documented by the company as "JSON REST based services" whose requests are authenticated with an OAuth 2.0 Bearer token obtained from the Reflexivity OAuth servic
  name: Reflexivity API
  slug: reflexivity-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://reflexivity.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.tgl.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.tgl.ai/
- group: company
  title: ''
  type: Blog
  url: https://reflexivity.com/en/blog
- group: operate
  title: ''
  type: Support
  url: https://support.reflexivity.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://reflexivity.com/app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reflexivity.com/en/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reflexivity.com/en/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.reflexivity.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://reflexivity.com/en#solutions
- group: agent
  title: ''
  type: WellKnown
  url: well-known/reflexivity-well-known.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reflexivity-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reflexivity-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/reflexivity-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reflexivity-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reflexivity-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/reflexivity-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/reflexivity-packages.yml
coverage:
  checked: '2026-08-26'
  detail: Reflexivity markets a RESTful API and its own docs say the endpoints are "detailed in the OpenAPI specifications within the service documentation", but that documentation host (api-docs.tgl.ai) 301s to docs.reflexivity.com and returns a Theneo "no-project-found?reason=PASSWORD_PROTECTED" interstitial, while the spec paths under the live API host answer 401 rather than 404 — the contract exists and is served, only never anonymously.
  evidence:
  - status: 301
    url: https://api-docs.tgl.ai/
  - status: 200
    url: https://docs.reflexivity.com/no-project-found?reason=PASSWORD_PROTECTED
  - status: 401
    url: https://api.reflexivity.com/alfred/v1/openapi.json
  - status: 404
    url: https://api.reflexivity.com/openapi.json
  - status: 200
    url: https://identity.reflexivity.com/.well-known/oauth-authorization-server
  reason: customer-only-docs
  state: gated
created: '2026-08-26'
description: Reflexivity (founded 2019 in New York as Toggle AI) is an institutional investment analysis platform that pairs licensed market data from S&P Global, LSEG Datastream, Cboe and Nasdaq with explainable AI agents that write and execute code to answer research questions across more than 40,000 stocks, bonds and commodities. Its published capabilities are Deep Research, Knowledge Graph, Portfolio Insights, Scenario Analysis, Document Intelligence and Smart Screening, delivered through a browser terminal and through a RESTful API sold to technology teams for custom model deployment, white-label distribution and real-time data feeds. The company raised a $30M Series B in October 2024 led by Greycroft with Interactive Brokers participating, is SOC 2 Type 2 audited annually, and gates both API credentials and its API reference behind a sales relationship.
image: https://reflexivity.com/favicon.ico
layout: provider
modified: '2026-08-26'
name: Reflexivity
nav: Providers
network: true
overview: 'Reflexivity publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial-Services, Investment Analysis, Market Data, and Artificial Intelligence.


  Reflexivity''s developer surface includes documentation, API reference, engineering blog, support, signup flow, pricing, and 12 more developer resources.'
plans:
- name: Reflexivity Plans Pricing
  plan_count: 0
  slug: reflexivity-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Reflexivity Rate Limits
  slug: reflexivity-rate-limits
scopes:
- name: Reflexivity Scopes
  scope_count: 0
  slug: reflexivity-scopes
  summary_line: OAuth 2.0 · no documented scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/reflexivity/refs/heads/main/screenshots/reflexivity-2026-09-02T153231.png
security:
- kind: authentication
  name: Reflexivity Authentication
  slug: reflexivity-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Reflexivity Domain Security
  slug: reflexivity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reflexivity
tags:
- Company
- Financial-Services
- Investment Analysis
- Market Data
- Artificial Intelligence
- Machine-Learning
- Fintech
- Research
- Knowledge Graph
- Agents
website: https://reflexivity.com/en
---
