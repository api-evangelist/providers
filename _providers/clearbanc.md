---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.clear.co/
- group: company
  title: ''
  type: Blog
  url: https://www.clear.co/blog
- group: start
  title: ''
  type: Login
  url: https://my.clearbanc.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clear.co/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clear.co/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clearbanc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clear.co/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clearbanc-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clearbanc-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clearbanc-domain-security.yml
coverage:
  checked: '2026-08-09'
  detail: 'Clearco runs a real partner API — api.clearbanc.com answers 403 "RBAC: access denied" on every path, and its developer documentation host docs.clearbanc.com returns a Cloudflare Access SSO interstitial for the root and for /openapi.json, /swagger.json, /api-docs and /.well-known/*, so no contract, reference or auth description is readable without a partner identity.'
  evidence:
  - status: 403
    url: https://docs.clearbanc.com/
  - status: 403
    url: https://docs.clearbanc.com/openapi.json
  - status: 403
    url: https://api.clearbanc.com/openapi.json
  - status: 404
    url: https://www.clear.co/developers
  - status: 200
    url: https://www.clear.co/llms.txt
  reason: partner-login
  state: gated
created: '2026-08-09'
description: Clearco (formerly Clearbanc) is a Toronto-based fintech that provides non-dilutive, revenue-based working capital to ecommerce and direct-to-consumer brands. Founders connect the sales, advertising and banking platforms they already run on — Shopify, Amazon, Stripe, PayPal, Square, BigCommerce — and Clearco underwrites from that data, funding inventory and marketing spend as a cash advance or as invoice funding, in as little as 24 hours, without equity dilution. The company was founded in 2015 as Clearbanc, rebranded to Clearco in 2021, and reports having deployed more than $3.3 billion to over 10,000 businesses.
image: https://cdn.prod.website-files.com/65fde10e62e6a7603e9221cc/660190120ed591c2ca6658f4_clearco-logo-black.png
layout: provider
modified: '2026-08-09'
name: Clearco
nav: Providers
network: true
overview: 'Clearco is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Financial-Services, Fintech, and Lending.


  Clearco''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 20
security:
- kind: domain-security
  name: Clearbanc Domain Security
  slug: clearbanc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: clearbanc
tags:
- Company
- Finance
- Financial-Services
- Fintech
- Lending
- Working Capital
- Revenue-Based Financing
- Invoice Funding
- E-Commerce
website: https://www.clear.co/
---
