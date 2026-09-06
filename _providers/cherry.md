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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cherry-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cherry-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://withcherry.com/security
- group: operate
  title: ''
  type: Support
  url: https://withcherry.com/help-center
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://withcherry.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://withcherry.com/terms
- group: company
  title: ''
  type: Blog
  url: https://withcherry.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://join.withcherry.com/demo-book
- group: start
  title: ''
  type: Login
  url: https://provider.withcherry.com/
- group: company
  title: ''
  type: Website
  url: https://withcherry.com/
created: '2026-07-17'
description: Cherry is a fintech platform providing point-of-sale patient financing for healthcare and elective-services providers across dental, medical aesthetics, plastic surgery, dermatology, veterinary, and other verticals. Rather than lending directly, Cherry facilitates consumer payment plans through partner lenders, offering Pay-in-4 and longer-term monthly plans (0-35.99% APR), a 60-second application with no hard credit check, upfront provider payout within 2-3 business days, and card-processing services. Cherry states it serves over 60,000 healthcare providers with an approximately 90% approval rate. Cherry is a portfolio company of DCM Ventures. Cherry does not publish a public developer API, developer portal, or OpenAPI at this time; this profile captures its public identity and security posture.
image: https://cdn.prod.website-files.com/681bf1d6f7dea459fe255c59/68252146834983973a92051f_cherry-logo-primary.svg
layout: provider
modified: '2026-07-18'
name: Cherry
nav: Providers
network: true
overview: 'Cherry is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Financing, and Point-of-Sale.


  Cherry''s developer surface includes support, engineering blog, signup flow, and 7 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 14.2
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 14.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 25.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cherry/refs/heads/main/screenshots/cherry-2026-07-25T205154.png
security:
- kind: domain-security
  name: Cherry Domain Security
  slug: cherry-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cherry Vulnerability Disclosure
  slug: cherry-vulnerability-disclosure
  summary_line: contact published
slug: cherry
tags:
- Company
- Fintech
- Payments
- Financing
- Point-of-Sale
- Patient Financing
- Buy Now Pay Later
- Healthcare
- Lending
website: https://withcherry.com/
---
