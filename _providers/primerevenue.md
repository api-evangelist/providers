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
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/primerevenue-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://primerevenue.com/
- group: company
  title: ''
  type: Blog
  url: https://primerevenue.com/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://primerevenue.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://primerevenue.com/privacy/
- group: start
  title: ''
  type: Login
  url: https://primerevenue.com/login/
- group: start
  title: ''
  type: SignUp
  url: https://primerevenue.com/request-demo/
- group: operate
  title: ''
  type: Support
  url: https://primerevenue.com/contact/
- group: auth
  title: ''
  type: Compliance
  url: https://primerevenue.com/primerevenue-security-compliance/
- group: design
  title: ''
  type: Conformance
  url: conformance/primerevenue-conformance.yml
created: '2026-07-17'
description: PrimeRevenue is a global financial technology company providing working capital and B2B payment solutions through a bank-agnostic, ERP-integrated platform. Its offerings include Supply Chain Finance (buyers extend payment terms while suppliers are paid early), Receivables Finance (suppliers sell invoices for early payment without buyer disclosure), Dynamic Discounting (early payment at variable discount rates), and Payments as a Service (a modern B2B payment layer). The platform manages more than $25B in daily assets, has accelerated over 12.5M invoices, and supports 30+ languages. PrimeRevenue does not publish a public developer portal or API documentation; this profile captures its corporate, security, and compliance surface. Backed by Battery Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/primerevenue.png
layout: provider
modified: '2026-07-20'
name: PrimeRevenue
nav: Providers
network: true
overview: 'PrimeRevenue is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Supply Chain Finance, Working Capital, B2B Payments, and Receivables Finance.


  PrimeRevenue''s developer surface includes engineering blog, pricing, signup flow, support, and 6 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 16.8
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 16.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/primerevenue/refs/heads/main/screenshots/primerevenue-2026-09-02T152027.png
security:
- kind: domain-security
  name: Primerevenue Domain Security
  slug: primerevenue-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: primerevenue
tags:
- Company
- Supply Chain Finance
- Working Capital
- B2B Payments
- Receivables Finance
- Dynamic Discounting
- Fintech
- Financial-Services
website: https://primerevenue.com/
---
