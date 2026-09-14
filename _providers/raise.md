---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'The Raise Commerce API (business/v2) — browse gift card brands and categories, purchase fixed- and variable-load gift cards, retrieve and act on individual cards (balance check, mark redeemed, update '
  name: Raise Commerce API
  slug: raise-commerce-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/raise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.raise.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.raise.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.raise.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.raise.com/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.raise.com/
- group: operate
  title: ''
  type: Support
  url: mailto:support@raise.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.raise.com/business/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/raise-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/raise-llms.txt
created: '2026-07-17'
description: Raise is a digital gift card marketplace and commerce platform. Raise for Business exposes the Raise Commerce API — a REST/JSON API that lets partners programmatically browse a catalog of retailer gift card brands, purchase fixed- and variable-load gift cards, check and manage card balances, and reconcile transactions and commissions across 180+ currencies and many countries. Authentication is OAuth 2.0 bearer tokens (server-to-server client credentials, plus app/web auth with SR25519/RSA key pairs, SMS, or TOTP). The API uses a JSON:API-style data envelope, page-based pagination, request metadata, and client_order_id idempotency. Prior investors include Accel, PayPal, and NEA.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/raise.png
layout: provider
modified: '2026-07-20'
name: Raise
nav: Providers
network: true
overview: 'Raise publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gift Cards, Commerce, and Payments.


  Raise''s developer surface includes documentation, API reference, getting-started guide, support, and 6 more developer resources.'
random_paper: 7
screenshot: https://raw.githubusercontent.com/api-evangelist/raise/refs/heads/main/screenshots/raise-2026-09-02T152823.png
security:
- kind: authentication
  name: Raise Authentication
  slug: raise-authentication
  summary_line: oauth2/http · 2 schemes
- kind: domain-security
  name: Raise Domain Security
  slug: raise-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: raise
tags:
- Company
- Consumer
- Gift Cards
- Commerce
- Payments
- Rewards
- Marketplace
website: http://www.raise.com
---
