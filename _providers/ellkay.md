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
api_count: 2
apis:
- description: Single-endpoint healthcare interoperability API exposing proprietary LK* operations (appointments, patient bridge/search, documents, charges, patient balance, master lists) that bi-directionally conne
  name: LKCloud Interop API
  slug: lkcloud-interop-api
- description: HL7 FHIR R4 RESTful API (read/search/create/update/delete across R4 resources) over the ELLKAY interoperability platform, with a published CapabilityStatement. OAuth 2.0 Bearer + SiteServiceKey; error
  name: LKCloud FHIR R4 API
  slug: lkcloud-fhir-r4-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.ellkay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://lkcloud-api.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://lkcloud-api.readme.io/docs/lk-cloud-overview
- group: docs
  title: ''
  type: APIReference
  url: https://lkcloud-api.readme.io/reference
- group: auth
  title: ''
  type: Authentication
  url: authentication/ellkay-authentication.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ellkay-changelog.yml
- group: company
  title: ''
  type: Blog
  url: https://www.ellkay.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.ellkay.com/support
- group: start
  title: ''
  type: Login
  url: https://dashboard.ellkay.com/Login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ellkay.com/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ellkay-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ellkay-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ellkay-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ellkay-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ellkay-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ellkay-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ellkay-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ellkay-sandbox.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ellkay-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ellkay-domain-security.yml
created: '2026-07-17'
description: 'ELLKAY is a healthcare data interoperability and data-management company that connects disparate health IT systems so clinical and financial data can move where it is needed. Its LKOpera, LKOrbit, and LKOasis product lines provide interface-engine integration, orders and results, payer data retrieval, network/lab connectivity, and data archiving/migration across 750+ EMR/PM systems, 400+ hospitals, 58k+ practices, and 725+ laboratories. For developers, ELLKAY exposes the LKCloud platform: a single-endpoint Interop API (proprietary LK* operations) and a full HL7 FHIR R4 RESTful API, both authenticated with OAuth 2.0 against the LKIdentity authorization server and routed with a SiteServiceKey.'
image: https://cdn.prod.website-files.com/68470d9028f4a074323fde70/689b3ac60177b4bae93d407b_Asset%2028.png
layout: provider
modified: '2026-07-19'
name: ELLKAY
nav: Providers
network: true
overview: 'ELLKAY publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Interoperability, FHIR, and HL7.


  ELLKAY''s developer surface includes documentation, API reference, authentication, changelog, engineering blog, support, sandbox, and 13 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 1
  name: Ellkay Rate Limits
  slug: ellkay-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/ellkay/refs/heads/main/screenshots/ellkay-2026-07-25T213153.png
security:
- kind: authentication
  name: Ellkay Authentication
  slug: ellkay-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Ellkay Domain Security
  slug: ellkay-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: ellkay
tags:
- Company
- Healthcare
- Interoperability
- FHIR
- HL7
- EHR Integration
- Health Data
website: https://www.ellkay.com/
---
