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
- group: company
  title: ''
  type: Website
  url: https://www.moneyview.in
- group: company
  title: ''
  type: Blog
  url: https://moneyview.in/blog
- group: operate
  title: ''
  type: Support
  url: https://www.moneyview.in/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.moneyview.in/privacy-policy-loans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.moneyview.in/terms-and-conditions
- group: auth
  title: ''
  type: Security
  url: https://www.moneyview.in/security-money-view-app
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/money-view-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.moneyview.in/security-money-view-app
- group: design
  title: ''
  type: Conformance
  url: conformance/money-view-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/money-view-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/money-view-llms.txt
created: '2026-07-17'
description: Moneyview is an Indian consumer fintech platform offering a suite of financial services including personal loans (up to Rs 10L), home loans, business loans, loans against property, credit cards, fixed deposits, digital gold, motor insurance, credit tracking, and UPI payments. The platform reports serving over 12 crore users across 18,400+ pincodes. Moneyview publishes ISO 27001:2022 and PCI DSS certifications and a responsible vulnerability disclosure program, but exposes no public developer API, developer portal, or OpenAPI surface. This profile was surfaced as a portfolio company of Accel and enriched by the API Evangelist pipeline.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/money-view.png
layout: provider
modified: '2026-08-08'
name: Money View
nav: Providers
network: true
overview: 'Money View is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Fintech, Lending, and Personal Loans.


  Money View''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 19.2
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/money-view/refs/heads/main/screenshots/money-view-2026-08-07T184158.png
security:
- kind: domain-security
  name: Money View Domain Security
  slug: money-view-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Money View Vulnerability Disclosure
  slug: money-view-vulnerability-disclosure
  summary_line: contact published
slug: money-view
tags:
- Company
- Consumer
- Fintech
- Lending
- Personal Loans
- Credit
- Payments
- Insurance
- India
website: https://www.moneyview.in
---
