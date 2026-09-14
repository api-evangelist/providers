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
- acting_count: 2
  human_in_the_loop: 0
  name: J Quants Agentic Access
  operation_count: 21
  slug: j-quants-agentic-access
  summary_line: 21 operations · 2 acting
api_count: 1
apis:
- description: The J-Quants API (V2) is a data distribution service operated by Japan Exchange Group (JPX) that makes it easy to obtain cleansed financial data such as Japanese stock prices and financials in histori
  name: J-Quants API
  slug: j-quants-api
- baseURL: https://api.jquants.com/
  baseurl_source: declared
  description: The Derivatives API from J-Quants — 2 operation(s) for derivatives.
  name: J-Quants Derivatives API
  slug: j-quants-derivatives-api
- baseURL: https://api.jquants.com/
  baseurl_source: declared
  description: The Equities API from J-Quants — 1 operation(s) for equities.
  name: J-Quants Equities API
  slug: j-quants-equities-api
- baseURL: https://api.jquants.com/
  baseurl_source: declared
  description: The Fins API from J-Quants — 4 operation(s) for fins.
  name: J-Quants Fins API
  slug: j-quants-fins-api
- baseURL: https://api.jquants.com/
  baseurl_source: declared
  description: The Indices API from J-Quants — 1 operation(s) for indices.
  name: J-Quants Indices API
  slug: j-quants-indices-api
- baseURL: https://api.jquants.com/
  baseurl_source: declared
  description: The Listed API from J-Quants — 1 operation(s) for listed.
  name: J-Quants Listed API
  slug: j-quants-listed-api
- baseURL: https://api.jquants.com/
  baseurl_source: declared
  description: The Markets API from J-Quants — 7 operation(s) for markets.
  name: J-Quants Markets API
  slug: j-quants-markets-api
- baseURL: https://api.jquants.com/
  baseurl_source: declared
  description: The Option API from J-Quants — 1 operation(s) for option.
  name: J-Quants Option API
  slug: j-quants-option-api
- baseURL: https://api.jquants.com/
  baseurl_source: declared
  description: The Prices API from J-Quants — 2 operation(s) for prices.
  name: J-Quants Prices API
  slug: j-quants-prices-api
- baseURL: https://api.jquants.com/
  baseurl_source: declared
  description: The Token API from J-Quants — 2 operation(s) for token.
  name: J-Quants Token API
  slug: j-quants-token-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: J-Quants Derivatives API
  slug: open-j-quants-derivatives-api
- collection_type: open
  name: J-Quants Derivatives Equities API
  slug: open-j-quants-equities-api
- collection_type: open
  name: J-Quants Derivatives Fins API
  slug: open-j-quants-fins-api
- collection_type: open
  name: J-Quants Derivatives Indices API
  slug: open-j-quants-indices-api
- collection_type: open
  name: J-Quants Derivatives Listed API
  slug: open-j-quants-listed-api
- collection_type: open
  name: J-Quants Derivatives Markets API
  slug: open-j-quants-markets-api
- collection_type: open
  name: J-Quants Derivatives Option API
  slug: open-j-quants-option-api
- collection_type: open
  name: J-Quants Derivatives Prices API
  slug: open-j-quants-prices-api
- collection_type: open
  name: J-Quants Derivatives Token API
  slug: open-j-quants-token-api
- collection_type: open
  name: J-Quants API
  slug: open-j-quants
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/j-quants-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/j-quants-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/j-quants-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/J-Quants
- group: company
  title: ''
  type: Website
  url: https://jpx-jquants.com/
- group: docs
  title: ''
  type: Documentation
  url: https://jpx-jquants.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://jpx-jquants.com/llms.txt
created: '2025-02-12'
description: J-Quants is a financial data API service operated by Japan Exchange Group (JPX) that makes it easy for retail investors to obtain cleansed financial data such as stock prices and financials in historical format. The service democratizes access to raw financial data for investment analysis.
finops:
- name: J Quants Finops
  service_category: API
  slug: j-quants-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/j-quants.png
layout: provider
modified: '2026-04-28'
name: J-Quants
nav: Providers
network: true
overview: 'J-Quants publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Derivatives API, Equities API, Fins API, and 6 more. Tagged areas include Financial Data, Investment, Japan, and Stock Market.


  J-Quants'' developer surface includes authentication, documentation, and 5 more developer resources.'
plans:
- name: J Quants Plans Pricing
  plan_count: 3
  slug: j-quants-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: J Quants Rate Limits
  slug: j-quants-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/j-quants/refs/heads/main/screenshots/j-quants-2026-06-20T183644.png
security:
- kind: authentication
  name: J Quants Authentication
  slug: j-quants-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: J Quants Domain Security
  slug: j-quants-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: j-quants
tags:
- Financial Data
- Investment
- Japan
- Stock Market
website: https://jpx-jquants.com/
---
