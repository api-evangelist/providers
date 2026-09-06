---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: Read-only REST API over the Gro ontology and its agricultural, climate and trade time series. Every operation was an HTTP GET under /v2/, authenticated with a bearer token issued from the Gro web appl
  name: Gro Intelligence API (retired)
  slug: gro-intelligence-api-retired
artifact_total: 5
common:
- group: docs
  title: ''
  type: Documentation
  url: https://gro.readthedocs.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gro-intelligence
- group: build
  title: ''
  type: Packages
  url: packages/gro-intelligence-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gro-intelligence-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/gro-intelligence-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gro-intelligence-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gro-intelligence-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/gro-intelligence-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gro-intelligence-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gro-intelligence-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gro-intelligence-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gro-intelligence-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gro-intelligence-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gro-intelligence-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gro-intelligence-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gro-intelligence-llms.txt
coverage:
  checked: '2026-08-22'
  detail: Gro Intelligence ceased operations in spring 2024 and was liquidated (IP acquired by Almanac, November 2024); its API host api.gro-intelligence.com, developer portal developers.gro-intelligence.com and app host app.gro-intelligence.com all return NXDOMAIN, and gro-intelligence.com is now a parked GoDaddy lander that answers HTTP 200 with the same 114-byte redirect body for every path including /openapi.json and /.well-known/agent-card.json. STEP 0b contract discovery was still run in full; the profile is built from the surfaces that survive — the company's public GitHub organization, the first-party MIT-licensed groclient library, its dated GitHub releases, and the PyPI/conda-forge listings. No OpenAPI, GraphQL SDL, MCP server or A2A agent card was ever published by this company.
  evidence:
  - status: 0
    url: https://api.gro-intelligence.com/openapi.json
  - status: 0
    url: https://developers.gro-intelligence.com/
  - status: 200
    url: https://gro-intelligence.com/openapi.json
  - status: 200
    url: https://gro-intelligence.com/zzz-soft404-control
  - status: 200
    url: https://gro-intelligence.com/.well-known/agent-card.json
  - status: 200
    url: https://github.com/gro-intelligence/api-client
  - status: 200
    url: https://pypi.org/project/groclient/
  reason: defunct
  state: none
created: '2026-08-22'
description: 'Gro Intelligence was a New York- and Nairobi-based agricultural and climate data company, founded in 2014 by Sara Menker, that built a global food-and-climate intelligence platform on top of satellite imagery, weather models, government statistics and trade data. Its product was a normalized ontology — metrics, items, regions, frequencies, sources and units — over hundreds of trillions of data points, exposed through a read-only REST API and an official Python client used by traders, insurers, lenders and CPG procurement teams to forecast yield, price and climate risk. The company raised an $85M Series B in 2021 and was named to TIME''s 100 most influential companies, then ran out of money, laid off 60% of staff in March 2024 and ceased operations that spring; Almanac (formerly Semios) acquired its IP and AI models out of liquidation in November 2024. This profile is a historical record: the API host, developer portal and web application no longer resolve, and the primary domain
  is a parked registrar lander.'
image: https://avatars.githubusercontent.com/u/15130228?v=4
layout: provider
modified: '2026-08-22'
name: Gro Intelligence
nav: Providers
network: true
overview: 'Gro Intelligence publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, Climate, Data, and Analytics.


  Gro Intelligence''s developer surface includes documentation, CLI, authentication, changelog, and 12 more developer resources.'
plans:
- name: Gro Intelligence Plans Pricing
  plan_count: 0
  slug: gro-intelligence-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Gro Intelligence Rate Limits
  slug: gro-intelligence-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/gro-intelligence/refs/heads/main/screenshots/gro-intelligence-2026-09-02T145635.png
security:
- kind: authentication
  name: Gro Intelligence Authentication
  slug: gro-intelligence-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gro Intelligence Domain Security
  slug: gro-intelligence-domain-security
  summary_line: no transport/DNS hardening detected
slug: gro-intelligence
tags:
- Company
- Agriculture
- Climate
- Data
- Analytics
- Satellite Imagery
- Commodities
- Weather
- Food Security
- Time Series
- Defunct
---
