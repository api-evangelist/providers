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
  name: Forex Agentic Access
  operation_count: 5
  slug: forex-agentic-access
  summary_line: 5 operations
api_count: 7
apis:
- description: Foreign exchange rates and currency conversion API.
  name: Fixer.io API
  slug: fixer
- description: Free currency conversion API with 161 currencies.
  name: ExchangeRate-API
  slug: exchangerate-api
- description: Accurate and reliable foreign exchange rates API.
  name: CurrencyAPI
  slug: currencyapi
- description: Free and open-source API for current and historical forex rates.
  name: Frankfurter API
  slug: frankfurter
- baseURL: https://openexchangerates.org/api
  baseurl_source: declared
  description: The Account API from Forex — 1 operation(s) for account.
  name: Forex Account API
  slug: forex-account-api
- baseURL: https://openexchangerates.org/api
  baseurl_source: declared
  description: The Rates API from Forex — 3 operation(s) for rates.
  name: Forex Rates API
  slug: forex-rates-api
- baseURL: https://openexchangerates.org/api
  baseurl_source: declared
  description: The Reference API from Forex — 1 operation(s) for reference.
  name: Forex Reference API
  slug: forex-reference-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Open Exchange Rates Account API
  slug: open-forex-account-api
- collection_type: open
  name: Open Exchange Account Rates API
  slug: open-forex-rates-api
- collection_type: open
  name: Open Exchange Rates Account Reference API
  slug: open-forex-reference-api
- collection_type: open
  name: Open Exchange Rates API
  slug: open-forex
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/forex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/forex-authentication.yml
created: '2024-01-15'
description: A collection of foreign exchange and currency conversion APIs.
finops:
- name: Forex Finops
  service_category: API
  slug: forex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forex.png
layout: provider
modified: '2026-05-19'
name: Forex
nav: Providers
network: true
overview: 'Forex publishes 3 APIs on the [APIs.io](https://apis.io/) network: Account API, Rates API, and Reference API. Tagged areas include Currency, Exchange Rates, Financial Data, Forex, and Trading.


  Forex''s developer surface includes authentication and 2 more developer resources.'
plans:
- name: Forex Plans Pricing
  plan_count: 3
  slug: forex-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 5
  name: Forex Rate Limits
  slug: forex-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/forex/refs/heads/main/screenshots/forex-2026-06-20T181424.png
security:
- kind: authentication
  name: Forex Authentication
  slug: forex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Forex Domain Security
  slug: forex-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: forex
tags:
- Currency
- Exchange Rates
- Financial Data
- Forex
- Trading
---
