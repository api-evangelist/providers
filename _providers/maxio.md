---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'REST API for managing the full subscription lifecycle in Maxio Advanced Billing (formerly Chargify): customers, products, components, subscriptions, invoices, transactions, coupons, and webhooks. Auth'
  name: Maxio Advanced Billing API
  slug: advanced-billing-api
artifact_total: 3
common:
- group: start
  title: ''
  type: Sandbox
  url: https://www.maxio.com/sandbox
- group: auth
  title: ''
  type: Security
  url: https://www.maxio.com/security
- group: operate
  title: ''
  type: StatusPage
  url: https://maxio.statuspage.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.maxio.com/privacy-policy
- group: other
  title: ''
  type: OpenIDConnect
  url: https://www.maxio.com/.well-known/oauth-authorization-server
- group: auth
  title: ''
  type: TrustCenter
  url: security/maxio-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/maxio-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wearemaxio
- group: company
  title: ''
  type: Website
  url: https://www.maxio.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.maxio.com/
- group: operate
  title: ''
  type: Help Center
  url: https://docs.maxio.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/maxio-com
- group: start
  title: ''
  type: Signup
  url: https://www.maxio.com/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.maxio.com/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://maxio.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.maxio.com/blog
created: '2026-05-11'
description: Maxio is a SaaS billing and financial operations platform formed from the merger of Chargify and SaaSOptics, providing subscription management, recurring billing, revenue recognition, and SaaS metrics for B2B software companies. Maxio Advanced Billing (formerly Chargify) exposes a REST API for managing customers, subscriptions, products, components, invoices, and events. Authentication uses HTTP Basic auth with a per-site API key as the username.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/maxio.png
layout: provider
modified: '2026-05-11'
name: Maxio
nav: Providers
network: true
overview: 'Maxio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Billing, Subscription, Recurring Billing, Revenue Recognition, and SaaS Metrics.


  Maxio''s developer surface includes sandbox, documentation, signup flow, pricing, engineering blog, and 11 more developer resources.'
random_paper: 17
screenshot: https://raw.githubusercontent.com/api-evangelist/maxio/refs/heads/main/screenshots/maxio-2026-06-20T185049.png
security:
- kind: domain-security
  name: Maxio Domain Security
  slug: maxio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Maxio Trust Center
  slug: maxio-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
slug: maxio
tags:
- Billing
- Subscription
- Recurring Billing
- Revenue Recognition
- SaaS Metrics
- Payments
website: https://www.maxio.com
---
