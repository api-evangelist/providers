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
api_count: 1
apis:
- description: PayTo's public developer surface, published by Australian Payments Plus (AP+) and NPP Australia. Rather than a self-serve API hosted by the scheme, this covers the AP+ Developer Portal (login-gated AP
  name: PayTo / NPP Developer Resources
  slug: payto-npp-developer-resources
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/payto-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/payto-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/payto-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/auspayplus
- group: company
  title: ''
  type: Website
  url: https://www.auspayplus.com.au/brands/payto
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.developers.auspayplus.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.developers.auspayplus.com.au/docs/
- group: start
  title: ''
  type: SignUp
  url: https://www.developers.auspayplus.com.au/api/auth/signup/
- group: company
  title: ''
  type: Blog
  url: https://www.auspayplus.com.au/news
- group: operate
  title: ''
  type: Support
  url: https://www.auspayplus.com.au/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.auspayplus.com.au/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.auspayplus.com.au/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/auspayplus
created: '2026-07-24'
description: 'PayTo is Australia''s real-time mandated-payments service, operated by Australian Payments Plus (AP+) as an overlay on the New Payments Platform (NPP). It lets merchants, billers, and payment service providers establish digital, pre-authorised agreements (mandates) that debit a customer''s bank account in real time using either a PayID or BSB and account number, with the mandate authorised, viewed, and managed by the account holder inside their own banking app. PayTo is positioned as the modern successor to the legacy BECS direct-debit rails, adding instant settlement, richer ISO 20022 data, and central mandate management via the NPP Mandate Management Service. As a domestic rail and scheme operator, AP+/NPP Australia is documentation- and rulebook-first: it publishes the NPP API Framework (v5.0, aligned to ISO 20022) that defines the mandatory data attributes and technical approach for PayTo and NPP APIs, but it does not itself host or offer a self-serve public API. The actual
  PayTo APIs are implemented and exposed by NPP Participants (banks) and connected payment service providers, so the company''s public developer surface is a portal, framework, sandbox, and message specifications rather than a downloadable OpenAPI.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-24'
name: PayTo
nav: Providers
network: true
overview: 'PayTo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Australia, Real-Time Payments, Account-to-Account, and ISO 20022.


  PayTo''s developer surface includes documentation, signup flow, engineering blog, support, and 9 more developer resources.'
random_paper: 11
screenshot: https://raw.githubusercontent.com/api-evangelist/payto/refs/heads/main/screenshots/payto-2026-08-07T191702.png
security:
- kind: domain-security
  name: Payto Domain Security
  slug: payto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: payto
tags:
- Payments
- Australia
- Real-Time Payments
- Account-to-Account
- ISO 20022
- Direct Debit
- Mandates
- New Payments Platform
- Scheme Operator
- Open Banking
website: https://www.auspayplus.com.au/brands/payto
---
