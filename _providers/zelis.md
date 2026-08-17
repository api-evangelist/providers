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
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: 'Zelis'' partner-facing API platform, published through the Zelis developer portal and API marketplace. The catalog spans claims document search and viewing, member ID card search and viewing, provider '
  name: Zelis API
  slug: zelis-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://www.zelis.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.zelis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zelis.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://marketplace.zelis.com/api-catalog/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.zelis.com/guides/getting-started-guests
- group: start
  title: ''
  type: SignUp
  url: https://devportalsignup.zelis.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://marketplace.zelis.com/connect-with-zelis/
- group: operate
  title: ''
  type: Support
  url: https://developer.zelis.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.zelis.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zelis.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zelis.com/terms-of-use/
- group: auth
  title: ''
  type: Authentication
  url: authentication/zelis-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zelis-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zelis-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zelis-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zelis-domain-security.yml
created: '2026-07-17'
description: Zelis is a healthcare financial technology company that modernizes the business of healthcare by connecting payers, providers, and members through a connected platform for claims cost management, electronic payments, and member and provider communications. Its solutions span network analytics and optimization, claims pricing, editing and payment integrity, electronic provider payments (including the ZAPP platform), member engagement, price transparency and Transparency in Coverage compliance, and provider directory data. Zelis exposes these capabilities to partners through a public developer portal and API marketplace, where integrators can register for OAuth2 client-credential access to a catalog of claims, ID card, provider directory, enrollment, payments, and member-engagement communication APIs. The company serves 725+ payers and processes payments to hundreds of thousands of healthcare providers.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zelis.png
layout: provider
modified: '2026-07-21'
name: Zelis
nav: Providers
network: true
overview: 'Zelis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Healthcare Payments, Claims, and Payments.


  Zelis'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, engineering blog, and 9 more developer resources.'
random_paper: 104
score:
  band: thin
  composite: 28.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 52.2
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 28.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 37.9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Zelis Authentication
  slug: zelis-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Zelis Domain Security
  slug: zelis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zelis
tags:
- Company
- Healthcare
- Healthcare Payments
- Claims
- Payments
- Price Transparency
- Provider Directory
- Member Engagement
- Insurance
- FinTech
website: https://www.zelis.com/
---
