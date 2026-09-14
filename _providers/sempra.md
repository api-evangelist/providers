---
access_model:
  confidence: medium
  label: Registration required — developer.sempra.com portal, nothing published anonymously
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developer.sempra.com/portals/api/sites/sempra-prod/liveportal/apis
  trial: false
  try_now: false
api_count: 1
apis:
- description: Sempra runs a Google Apigee API program. api.sempra.com is the Apigee runtime gateway and developer.sempra.com is an Apigee integrated developer portal (Apigee organization "sempra", site id "sempra-p
  name: Sempra Developer Portal APIs
  slug: sempra-developer-portal-apis
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.sempra.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sempra
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sempra.com
- group: start
  title: ''
  type: Login
  url: https://developer.sempra.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.sempra.com/newsroom
- group: operate
  title: ''
  type: Support
  url: https://www.sempra.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sempra.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sempra.com/terms-and-conditions
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sempra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sempra-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sempra-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sempra-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sempra-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sempra-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sempra-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sempra-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/sempra-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sempra-llms.txt
coverage:
  checked: '2026-09-04'
  detail: 'Sempra''s Google Apigee developer portal at developer.sempra.com is publicly reachable, but its own anonymous catalog endpoint /portals/api/sites/sempra-prod/liveportal/apis answers HTTP 200 with "apiDocs": [] and "apiProducts": [] and its header menu is exactly two items, "APIs" and "Log In" — not one API product, contract or reference is published to an unauthenticated visitor, while a live OAuth-protected proxy at https://api.sempra.com/v1 answers every anonymous request with an Apigee oauth.v2.InvalidAccessToken 401, so the API is real and callable but only by someone already issued a token through that portal.'
  evidence:
  - status: 200
    url: https://developer.sempra.com/portals/api/sites/sempra-prod/liveportal/apis
  - status: 200
    url: https://developer.sempra.com/portals/api/sites/sempra-prod/liveportal/menus
  - status: 401
    url: https://api.sempra.com/v1/graphql
  - status: 404
    url: https://api.sempra.com/openapi.json
  - status: 404
    url: https://api.sempra.com/.well-known/agent-card.json
  - status: 200
    url: https://www.sempra.com/robots.txt
  reason: partner-login
  state: gated
created: '2026-03-21'
description: Sempra is a San Diego-headquartered North American energy infrastructure holding company and a Fortune 500 constituent, operating regulated utilities and energy infrastructure across California, Texas and Mexico. Its businesses include San Diego Gas & Electric and Southern California Gas Company in California, an ownership interest in Oncor Electric Delivery in Texas, and Sempra Infrastructure, which develops LNG export terminals, natural gas pipelines and renewable generation in North America. Sempra operates a Google Apigee API program — an OAuth-protected gateway at api.sempra.com and an integrated developer portal at developer.sempra.com — and runs sibling Apigee organizations for its California utilities at developer.sdge.com (site sdge-prod) and developer.socalgas.com (site socalgas-prod). None of the three portals publishes an API product, contract, reference or price to an unauthenticated visitor, so the entire integration surface sits behind portal registration.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sempra.png
layout: provider
modified: '2026-09-04'
name: Sempra
nav: Providers
network: true
overview: 'Sempra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Utilities, Natural Gas, Electricity, and Energy Infrastructure.


  Sempra''s developer surface includes engineering blog, support, authentication, and 15 more developer resources.'
plans:
- name: Sempra Plans Pricing
  plan_count: 0
  slug: sempra-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Sempra Rate Limits
  slug: sempra-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/sempra/refs/heads/main/screenshots/sempra-2026-06-20T193648.png
security:
- kind: authentication
  name: Sempra Authentication
  slug: sempra-authentication
  summary_line: http · 0 schemes
- kind: domain-security
  name: Sempra Domain Security
  slug: sempra-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sempra
tags:
- Energy
- Utilities
- Natural Gas
- Electricity
- Energy Infrastructure
- LNG
- Apigee
- Fortune 500
website: https://www.sempra.com
---
