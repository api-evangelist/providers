---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - docs
  trial: false
  try_now: false
api_count: 1
apis:
- description: Real-time surcharge calculation API. The caller sends a base transaction amount and payment-method details (card brand and type) and receives the permitted surcharge amount, evaluated against U.S. sta
  name: Yeeld Surcharging API
  slug: yeeld
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://theyeeld.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.theyeeld.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.theyeeld.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.theyeeld.com/getting-started/overview
- group: operate
  title: ''
  type: Support
  url: https://theyeeld.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://theyeeld.com/products/yeeld-surcharging-for-stripe
- group: start
  title: ''
  type: SignUp
  url: https://theyeeld.com/yeeld-pay-signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://theyeeld.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://theyeeld.com/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://theyeeld.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://theyeeld.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/theyeeld
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yeeld-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yeeld-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/yeeld-packages.yml
- group: design
  title: ''
  type: Components
  url: components/yeeld-components.yml
created: '2025-02-21'
description: 'Yeeld builds credit-card surcharging infrastructure for merchants and platforms across the United States and Canada, and provides payments consulting and development services. The Yeeld Surcharging API is a real-time rules engine: a caller passes a transaction amount and payment-method details, and Yeeld returns the surcharge that jurisdictional law and Visa, Mastercard, American Express and Discover rules permit, or zero where surcharging is prohibited. Yeeld also ships a Stripe App Marketplace app for Stripe Checkout and Payment Links, and YeeldPay, a no-code branded hosted checkout. Founded by ex-Stripe staff and headquartered in Chicago, Illinois.'
finops:
- name: Yeeld Finops
  service_category: API
  slug: yeeld-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yeeld.png
layout: provider
modified: '2026-08-28'
name: Yeeld
nav: Providers
network: true
overview: 'Yeeld publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Surcharging, Credit Cards, Compliance, and Stripe.


  Yeeld''s developer surface includes documentation, getting-started guide, support, pricing, signup flow, engineering blog, and 10 more developer resources.'
plans:
- name: Yeeld Plans Pricing
  plan_count: 0
  slug: yeeld-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Yeeld Rate Limits
  slug: yeeld-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/yeeld/refs/heads/main/screenshots/yeeld-2026-06-20T201737.png
security:
- kind: authentication
  name: Yeeld Authentication
  slug: yeeld-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Yeeld Domain Security
  slug: yeeld-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: yeeld
tags:
- Payments
- Surcharging
- Credit Cards
- Compliance
- Stripe
- Checkout
- Fintech
- Payment Consulting
website: https://theyeeld.com/
---
