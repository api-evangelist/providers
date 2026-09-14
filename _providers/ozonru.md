---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: RPC-over-HTTP JSON API for OZON marketplace sellers to manage products, prices, stock, warehouses, orders (FBO/FBS), returns, analytics, and finances. POST-only endpoints under a per-operation version
  name: OZON Seller API
  slug: ozon-seller-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: http://ozon.ru
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ozon.ru/api/seller/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ozon.ru/api/seller/
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/ozonru-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ozonru-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: security/ozonru-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ozonru-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ozonru-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/ozonru-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ozonru-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ozonru-llms.txt
created: '2026-07-17'
description: OZON is one of Russia's largest e-commerce marketplaces, offering retail across electronics, apparel, groceries, and more, plus its own logistics and fulfillment network (FBO/FBS). For developers, OZON exposes the OZON Seller API, a POST-based RPC-over-HTTP JSON API at https://api-seller.ozon.ru that lets marketplace sellers manage products, prices, stock, warehouses, orders, returns, analytics, and finances programmatically. Authentication uses two headers, a numeric Client-Id and a secret Api-Key issued in the seller cabinet. OZON was surfaced as a portfolio company of Index Ventures and enriched by the API Evangelist pipeline from live probes of its API host and public developer documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ozonru.png
layout: provider
modified: '2026-07-20'
name: OZON.ru
nav: Providers
network: true
overview: 'OZON.ru publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Marketplace, and Seller API.


  OZON.ru''s developer surface includes documentation and 10 more developer resources.'
random_paper: 13
security:
- kind: authentication
  name: Ozonru Authentication
  slug: ozonru-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ozonru Domain Security
  slug: ozonru-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ozonru Vulnerability Disclosure
  slug: ozonru-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: ozonru
tags:
- Company
- Retail
- E-Commerce
- Marketplace
- Seller API
- Russia
- Logistics
website: http://ozon.ru
---
