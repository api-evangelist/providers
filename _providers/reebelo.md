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
  - sandbox
  trial: false
  try_now: false
api_count: 1
apis:
- description: The seller-side REST API behind Reebelo's Cobalt vendor back-office. Authenticated with a Reebelo-issued x-api-key header, it exposes offer management (list offers, look up an offer by SKU, create/upd
  name: Reebelo Vendor Integration API (Cobalt)
  slug: reebelo-vendor-api
artifact_total: 6
asyncapis:
- description: ''
  name: Reebelo Webhooks
  slug: reebelo-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://reebelo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cobalt.reebelo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cobalt.reebelo.com/documentation/home
- group: docs
  title: ''
  type: APIReference
  url: https://cobalt.reebelo.com/documentation/custom-api
- group: start
  title: ''
  type: GettingStarted
  url: https://cobalt.reebelo.com/documentation/home
- group: start
  title: ''
  type: Login
  url: https://cobalt.reebelo.com/
- group: operate
  title: ''
  type: Support
  url: https://reebelo.com/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.reebelo.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://reebelo.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://reebelo.com/policies/privacy-policy
- group: commercial
  title: ''
  type: Plans
  url: plans/reebelo-plans-pricing.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reebelo-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/reebelo-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reebelo-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reebelo-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/reebelo-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reebelo-domain-security.yml
created: '2026-08-26'
description: 'Reebelo is a marketplace for certified refurbished consumer technology — smartphones, laptops, tablets, smartwatches, gaming and home electronics — sold by a vetted network of third-party refurbishers at up to 70% below new, with a 12-month warranty and a 30-day trial. Founded in 2019 and operating in the United States, Australia, New Zealand and Singapore, Reebelo positions refurbished tech as the sustainable alternative to new-device purchase. Its developer surface is seller-facing rather than buyer-facing: the Cobalt vendor back-office publishes a REST integration API on https://a.reebelo.com that lets a refurbisher list and reprice offers, pull orders, push carrier tracking and IMEI numbers, and upload seller invoices, alongside hosted-CSV feed and order-forwarding webhook alternatives for vendors without API resources.'
image: https://edge.reebelo.com/images/opengraph.png
layout: provider
modified: '2026-08-26'
name: Reebelo
nav: Providers
network: true
overview: 'Reebelo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Refurbished Electronics, Marketplace, E-Commerce, Consumer Electronics, and Reverse Logistics.


  The Reebelo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Reebelo''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 12 more developer resources.'
plans:
- name: Reebelo Plans Pricing
  plan_count: 0
  slug: reebelo-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Reebelo Rate Limits
  slug: reebelo-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/reebelo/refs/heads/main/screenshots/reebelo-2026-09-02T153209.png
security:
- kind: authentication
  name: Reebelo Authentication
  slug: reebelo-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Reebelo Domain Security
  slug: reebelo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: reebelo
tags:
- Refurbished Electronics
- Marketplace
- E-Commerce
- Consumer Electronics
- Reverse Logistics
- Circular Economy
- Retail
- Inventory
- Order
- Seller Integration
website: https://reebelo.com/
---
