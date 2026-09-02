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
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freewill-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/freewill-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/freewill-trust-center.yml
- group: operate
  title: ''
  type: Support
  url: https://help.freewill.com/
- group: start
  title: ''
  type: Login
  url: https://app.freewill.com/login
- group: start
  title: ''
  type: SignUp
  url: https://app.freewill.com/will
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.freewill.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.freewill.com/legal/privacy
- group: company
  title: ''
  type: Website
  url: https://www.freewill.com/
created: '2026-07-17'
description: 'FreeWill is an online estate-planning platform that lets people create legal documents for free, including last wills, revocable living trusts (California only), advance healthcare directives, financial powers of attorney, and beneficiary designations, through a guided questionnaire. It runs a dual model: individuals use the tools at no cost, while more than 2,400 nonprofit organizations partner with FreeWill for planned-giving and legacy-gift features. Related surfaces include the Estately advisor platform and a Nonprofit Solutions offering. FreeWill was surfaced as a portfolio company of iconiq-capital and qed-investors. Enrichment found no public developer portal, OpenAPI, SDK, or API documentation — this profile is a consumer/nonprofit company record, not an API producer, with security and legal properties captured from the public site.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/freewill.png
layout: provider
modified: '2026-07-19'
name: FreeWill
nav: Providers
network: true
overview: 'FreeWill is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Estate Planning, Wills, and Non-Profit.


  FreeWill''s developer surface includes support, signup flow, and 7 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.6
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freewill/refs/heads/main/screenshots/freewill-2026-07-25T215148.png
security:
- kind: domain-security
  name: Freewill Domain Security
  slug: freewill-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Freewill Trust Center
  slug: freewill-trust-center
  summary_line: SOC 2 Type II
slug: freewill
tags:
- Company
- Fintech
- Estate Planning
- Wills
- Non-Profit
- Planned Giving
- Legal Tech
website: https://www.freewill.com/
---
