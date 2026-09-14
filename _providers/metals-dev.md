---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Metals Dev Agentic Access
  operation_count: 6
  slug: metals-dev-agentic-access
  summary_line: 6 operations
api_count: 1
apis:
- baseURL: https://api.metals.dev/v1
  baseurl_source: declared
  description: Usage and quota information.
  name: Metals.Dev Account API
  slug: metals-dev-account-api
- baseURL: https://api.metals.dev/v1
  baseurl_source: declared
  description: Authority pricing from LBMA, LME, MCX, and IBJA.
  name: Metals.Dev Authority API
  slug: metals-dev-authority-api
- baseURL: https://api.metals.dev/v1
  baseurl_source: declared
  description: Currency rates and conversions.
  name: Metals.Dev Currency API
  slug: metals-dev-currency-api
- baseURL: https://api.metals.dev/v1
  baseurl_source: declared
  description: Latest and historical metal and currency rates.
  name: Metals.Dev Rates API
  slug: metals-dev-rates-api
- baseURL: https://api.metals.dev/v1
  baseurl_source: declared
  description: Spot pricing for individual metals.
  name: Metals.Dev Spot Prices API
  slug: metals-dev-spot-prices-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Metals.Dev Account API
  slug: open-metals-dev-account-api
- collection_type: open
  name: Metals.Dev Account Authority API
  slug: open-metals-dev-authority-api
- collection_type: open
  name: Metals.Dev Account Currency API
  slug: open-metals-dev-currency-api
- collection_type: open
  name: Metals.Dev Account Rates API
  slug: open-metals-dev-rates-api
- collection_type: open
  name: Metals.Dev Account Spot Prices API
  slug: open-metals-dev-spot-prices-api
- collection_type: open
  name: Metals.Dev API
  slug: open-metals-dev
common:
- group: company
  title: ''
  type: Website
  url: https://www.metals.dev/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metals-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metals-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metals-dev-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MetalsDev
- group: start
  title: ''
  type: Portal
  url: https://metals.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://metals.dev/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://metals.dev/status
- group: start
  title: ''
  type: Signup
  url: https://metals.dev/sign-up
created: '2025-03-01'
description: Metals.Dev provides a developer-friendly JSON API for spot prices of precious metals, industrial metals, and currency conversion rates. It offers real-time prices from leading authorities including LBMA, LME, MCX, and IBJA, plus 5+ years of historical data.
finops:
- name: Metals Dev Finops
  service_category: API
  slug: metals-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metals-dev.png
layout: provider
modified: '2026-05-19'
name: Metals.Dev
nav: Providers
network: true
overview: 'Metals.Dev publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Authority API, Currency API, and 2 more. Tagged areas include Financial Data, Gold, Precious Metals, Silver, and Spot Prices.


  Metals.Dev''s developer surface includes authentication, developer portal, pricing, signup flow, and 5 more developer resources.'
plans:
- name: Metals Dev Plans Pricing
  plan_count: 3
  slug: metals-dev-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Metals Dev Rate Limits
  slug: metals-dev-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/metals-dev/refs/heads/main/screenshots/metals-dev-2026-06-20T185246.png
security:
- kind: authentication
  name: Metals Dev Authentication
  slug: metals-dev-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Metals Dev Domain Security
  slug: metals-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: metals-dev
tags:
- Financial Data
- Gold
- Precious Metals
- Silver
- Spot Prices
website: https://www.metals.dev/
---
