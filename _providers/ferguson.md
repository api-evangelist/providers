---
access_model:
  confidence: medium
  label: Partner approval required
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developer.ferguson.com/faq
  - https://developer.ferguson.com/get-started
  trial: false
  try_now: false
api_count: 1
apis:
- description: A curated set of REST/JSON Enterprise APIs that let approved partners and software providers transact with Ferguson — product availability and vendor cost data, and electronic purchase-order submissio
  name: Ferguson Enterprise APIs
  slug: enterprise-apis
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ferguson-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ferguson-official
- group: company
  title: ''
  type: Website
  url: https://www.ferguson.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ferguson.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ferguson.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ferguson.com/get-started
- group: company
  title: ''
  type: Blog
  url: https://developer.ferguson.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.ferguson.com/content/customer-support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ferguson.com/content/customer-support/website-information/terms-of-site-use/
- group: start
  title: ''
  type: SignUp
  url: https://www.ferguson.com/s/sign-up
- group: auth
  title: ''
  type: Authentication
  url: authentication/ferguson-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ferguson-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/ferguson-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ferguson-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ferguson-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ferguson-llms.txt
coverage:
  checked: '2026-09-09'
  detail: Ferguson's API catalog and its Swagger documentation live inside a Backstage developer portal whose backend answers HTTP 401 "Missing credentials" to every anonymous request (/api/catalog/entities, /api/search/query), and Ferguson grants portal access only to organizations that complete its partner review and approval process via api.team@ferguson.com.
  evidence:
  - status: 401
    url: https://developer.ferguson.com/api/catalog/entities?filter=kind=api
  - status: 401
    url: https://developer.ferguson.com/api/search/query?term=api
  - status: 404
    url: https://www.ferguson.com/.well-known/api-catalog
  reason: partner-login
  state: gated
created: '2026-03-21'
description: Ferguson is a Fortune 500 distributor of plumbing supplies, HVAC products, pipe, valves and fittings, waterworks, and building supplies serving professional contractors, residential homeowners, and commercial customers across the United States. Ferguson runs an Enterprise API program on Google Apigee, published through the Ferguson Developer Portal, that lets approved partners and software providers pull product availability and cost data and submit purchase orders electronically. Access is granted only to organizations that complete Ferguson's partner review and approval process, and the API catalog and its Swagger documentation are not readable without credentials.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ferguson.png
layout: provider
modified: '2026-09-09'
name: Ferguson
nav: Providers
network: true
overview: 'Ferguson publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Distribution, Plumbing, HVAC, Building Supplies, and Waterworks.


  Ferguson''s developer surface includes API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 10 more developer resources.'
plans:
- name: Ferguson Plans Pricing
  plan_count: 0
  slug: ferguson-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Ferguson Rate Limits
  slug: ferguson-rate-limits
security:
- kind: authentication
  name: Ferguson Authentication
  slug: ferguson-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Ferguson Domain Security
  slug: ferguson-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ferguson
tags:
- Distribution
- Plumbing
- HVAC
- Building Supplies
- Waterworks
- Pipe Valves Fittings
- Wholesale Distribution
- B2B
- Fortune 500
website: https://www.ferguson.com
---
