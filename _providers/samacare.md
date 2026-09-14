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
  trial: false
  try_now: false
api_count: 1
apis:
- description: The private integration API behind the SamaCare prior authorization platform, used for two-way exchange of patient demographic data, clinical documentation and prior authorization status between SamaC
  name: SamaCare Platform API
  slug: samacare-platform-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.samacare.com/
- group: operate
  title: ''
  type: Support
  url: https://help.samacare.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.samacare.com/
- group: company
  title: ''
  type: Blog
  url: https://samacare.com/resources
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SamaCare
- group: start
  title: ''
  type: Login
  url: https://app.samacare.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://samacare.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://samacare.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: conformance/samacare-conformance.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/samacare-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/samacare-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/samacare-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/samacare-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/samacare-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/samacare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/samacare-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: 'SamaCare runs a real platform API at api.samacare.com — an Express service that answers every single path, /docs, /openapi.json, /graphql and /.well-known/* included, with HTTP 401 and WWW-Authenticate: Bearer error="invalid_token" — but publishes no developer portal, no API reference and no OpenAPI anywhere; the sitemap has no developer URL and every product page ends in a "Request Access" / "Request Demo" CTA where a reference would be.'
  evidence:
  - status: 401
    url: https://api.samacare.com/openapi.json
  - status: 401
    url: https://api.samacare.com/graphql
  - status: 404
    url: https://www.samacare.com/openapi.json
  - status: 200
    url: https://www.samacare.com/sitemap.xml
  reason: sales-gate
  state: gated
created: '2026-08-26'
description: SamaCare operates a medical benefit prior authorization platform used by specialty practices in oncology, rheumatology, neurology, retina/ophthalmology and infusion care to submit, track and renew prior authorizations for provider-administered ("buy and bill") drugs across every payer in one place. The platform combines payer-specific form intelligence and auto-fill, human-in-the-loop AI, status tracking and expiration reminders with one-click re-authorization, and a market-access analytics layer that pharmaceutical manufacturers license for benchmark and patient-access insight. SamaCare states it has processed more than two million medical benefit prior authorizations representing over $6B in annual drug spend, and integrates into practice systems — NextGen Enterprise and ModMed EMRs among them — over an API-based two-way exchange of demographic data and clinical documentation. The platform API is served from api.samacare.com behind an OAuth 2.0 Bearer challenge and is arranged
  through EHR/RCM partnership rather than a public developer program; no public API reference, OpenAPI contract or self-serve key issuance is published.
image: https://cdn.prod.website-files.com/5ea98938698e3343f5ac98f0/69e7a448f55840e8a85dc35f_1200x630.png
layout: provider
modified: '2026-08-26'
name: SamaCare
nav: Providers
network: true
overview: 'SamaCare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Prior Authorization, Patient Access, and Specialty Pharmacy.


  SamaCare''s developer surface includes support, engineering blog, authentication, and 13 more developer resources.'
plans:
- name: Samacare Plans Pricing
  plan_count: 0
  slug: samacare-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Samacare Rate Limits
  slug: samacare-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/samacare/refs/heads/main/screenshots/samacare-2026-09-02T154333.png
security:
- kind: authentication
  name: Samacare Authentication
  slug: samacare-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Samacare Domain Security
  slug: samacare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: samacare
tags:
- Company
- Healthcare
- Prior Authorization
- Patient Access
- Specialty Pharmacy
- Life Sciences
- Electronic Health Records
- Revenue Cycle Management
- Market Access
- Artificial Intelligence
website: https://www.samacare.com/
---
