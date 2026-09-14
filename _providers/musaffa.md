---
access_model:
  confidence: high
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- description: REST API returning Shariah-compliance screening for stocks and ETFs — a compliance status and 0-5 ranking per ticker, a full screening report with revenue breakdown and interest-bearing securities/deb
  name: Musaffa B2B Shariah Compliance API
  slug: musaffa-b2b-shariah-compliance-api
artifact_total: 6
asyncapis:
- description: ''
  name: Musaffa Screening Webhooks
  slug: musaffa-screening-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/musaffa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://musaffa.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://musaffa.com/for-business/
- group: docs
  title: ''
  type: Documentation
  url: https://api.musaffa.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.musaffa.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://musaffa.com/for-business/
- group: start
  title: ''
  type: SignUp
  url: https://musaffa.com/authentication/register/
- group: start
  title: ''
  type: Login
  url: https://musaffa.com/authentication/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://musaffa.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://musaffa.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://musaffa.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://musaffa.com/news/
- group: auth
  title: ''
  type: Authentication
  url: authentication/musaffa-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/musaffa-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/musaffa-plans-pricing.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/musaffa-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/musaffa-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/musaffa-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/musaffa-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/musaffa-screening-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/musaffa-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/musaffa-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/musaffa-llms.txt
created: '2026-08-26'
description: 'Musaffa is a New York-headquartered Islamic fintech that operates a halal investing platform and sells its underlying Shariah-compliance dataset to other businesses as the Musaffa B2B API. The company screens 120,000+ stocks and ETFs across 70+ global exchanges against an AAOIFI-based methodology and exposes the results — compliance status, a 0-5 compliance ranking, revenue breakdown, interest-bearing securities and debt ratios, dividend purification amounts and related securities — through a versioned REST API at platform.musaffa.com, plus an outbound webhook that pushes compliance-status changes to a subscriber URL. The B2B API is documented publicly at api.musaffa.com (v1, v2 and the current v3) but the API itself is sold through a demo/sales process: credentials are a client ID plus a shared secret issued per client, and there is no self-service signup for the API.'
image: https://musaffa.com/assets/images/header/musaffa-logo-black.webp
layout: provider
modified: '2026-08-26'
name: Musaffa
nav: Providers
network: true
overview: 'Musaffa publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Islamic Finance, Shariah Compliance, Halal Investing, Stock Screening, and Financial Data.


  The Musaffa catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Musaffa''s developer surface includes documentation, API reference, pricing, signup flow, support, engineering blog, authentication, and 16 more developer resources.'
plans:
- name: Musaffa Plans Pricing
  plan_count: 4
  slug: musaffa-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 3
  name: Musaffa Rate Limits
  slug: musaffa-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/musaffa/refs/heads/main/screenshots/musaffa-2026-09-02T150701.png
security:
- kind: authentication
  name: Musaffa Authentication
  slug: musaffa-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Musaffa Domain Security
  slug: musaffa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: musaffa
tags:
- Islamic Finance
- Shariah Compliance
- Halal Investing
- Stock Screening
- Financial Data
- ETFs
- Market Data
- Fintech
- Investing
- Compliance
- Zakat
- Company
website: https://musaffa.com/
---
