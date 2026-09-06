---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 5
apis:
- description: REST API for retrieving end-user accounts, transactions, and balances across 3,400+ European banks via PSD2 AISP.
  name: Tink Account Aggregation API
  slug: account-aggregation-api
- description: Verify account ownership and IBAN details for an end user.
  name: Tink Account Check API
  slug: account-check-api
- description: Categorized income data derived from aggregated transaction history.
  name: Tink Income Check API
  slug: income-check-api
- description: Risk indicators and affordability signals derived from aggregated bank data.
  name: Tink Risk Insights API
  slug: risk-insights-api
- description: Initiate single, recurring, and bulk SEPA / domestic-rail payments via PSD2 PISP.
  name: Tink Payments API
  slug: payments-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tink-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tink-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fintecsystems
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tink-ab
- group: start
  title: ''
  type: Portal
  url: https://tink.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tink.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://tink.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/tink-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tink-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tink-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.tink.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://tink.com/blog/
created: '2026-05-08'
description: Tink (a Visa company) is a European open-banking platform offering account aggregation, payment initiation, identity, and KYC products across 3,400+ banks. The Tink API exposes Account Check, Account Aggregation, Income Check, Risk Insights, Money Manager, and Payments products under a single OAuth-protected REST surface at api.tink.com.
finops:
- name: Tink Finops
  service_category: Open Banking
  slug: tink-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tink.png
layout: provider
modified: '2026-05-08'
name: Tink
nav: Providers
network: true
overview: 'Tink publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Open Banking, PSD2, Europe, and Visa.


  Tink''s developer surface includes developer portal, documentation, pricing, engineering blog, and 8 more developer resources.'
plans:
- name: Tink Plans Pricing
  plan_count: 2
  slug: tink-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 3
  name: Tink Rate Limits
  slug: tink-rate-limits
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 48.0
    catalog_earned_first_party: 0.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 14.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 15.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tink/refs/heads/main/screenshots/tink-2026-06-20T195408.png
security:
- kind: domain-security
  name: Tink Domain Security
  slug: tink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tink Vulnerability Disclosure
  slug: tink-vulnerability-disclosure
  summary_line: security.txt
slug: tink
tags:
- Fintech
- Open Banking
- PSD2
- Europe
- Visa
- Account Aggregation
- Payments
- KYC
website: https://tink.com/
---
