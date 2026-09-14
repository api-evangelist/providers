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
- description: Live REST API serving grocery store and product data to Freshop-powered storefronts. Numeric path versioning (/1/, /2/); app_key query-parameter authentication; flat JSON error envelope.
  name: Freshop API
  slug: freshop-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://freshop.com
- group: operate
  title: ''
  type: Support
  url: https://freshop.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ncr.com/privacy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/freshop-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freshop-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/freshop-llms.txt
created: '2026-07-17'
description: Freshop is an eCommerce platform purpose-built for grocery and specialty retail, now part of NCR Voyix. It powers branded online storefronts, mobile shopping, order fulfillment, pickup, and delivery for independent and regional grocers, and integrates third-party services for loyalty, coupons, email, SMS, and fulfillment. Freshop exposes a live REST API at api.freshop.com that serves store and product data to Freshop-powered storefronts and apps, authenticated with an application key (app_key) query-string parameter and versioned by a numeric path segment.
image: https://freshop.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Freshop
nav: Providers
network: true
overview: 'Freshop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Grocery, E-Commerce, Retail, and Online Shopping.


  Freshop''s developer surface includes support and 5 more developer resources.'
random_paper: 3
screenshot: https://raw.githubusercontent.com/api-evangelist/freshop/refs/heads/main/screenshots/freshop-2026-07-25T215203.png
security:
- kind: authentication
  name: Freshop Authentication
  slug: freshop-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Freshop Domain Security
  slug: freshop-domain-security
  summary_line: TLSv1.3 · HSTS
slug: freshop
tags:
- Company
- Grocery
- E-Commerce
- Retail
- Online Shopping
- Fulfillment
- Delivery
- NCR Voyix
website: https://freshop.com
---
