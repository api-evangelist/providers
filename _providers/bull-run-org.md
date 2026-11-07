---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/bull-run-org/plans/bull-run-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bull-run-org-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/bull-run-org/well-known/bull-run-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bull-run-org-well-known.yml
- group: other
  href: https://artifacts.apis.io/bull-run-org/hosts/bull-run-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bull-run-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/bull-run-org/vendors/bull-run-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bull-run-org-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bull-run.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bull-run.org/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://bull-run.org/pricing
- group: auth
  href: https://artifacts.apis.io/bull-run-org/security/bull-run-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bull-run-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bull-run.org/
coverage:
  checked: '2026-11-03'
  detail: Bullrun provides a fintech comparison service but offers no public developer API.
  evidence:
  - status: 200
    url: https://bull-run.org/
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: Bullrun is a Zurich‑based fintech platform that helps investors find the cheapest UCITS ETFs for their chosen indexes. It provides a searchable comparison of ETFs by fee, domicile, payout, and trading venues, along with research on companies worldwide. The service is free, web‑based, and aims to simplify ETF selection for both retail and professional investors.
image: https://bull-run.org/og/default.png
layout: provider
modified: '2026-11-03'
name: Bullrun
nav: Providers
network: true
overview: 'Bullrun is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, ETFs, Comparison, Zurich, and Fintech.


  Bullrun''s developer surface includes pricing and 8 more developer resources.'
plans:
- name: Bull Run Org Plans Pricing
  plan_count: 2
  slug: bull-run-org-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - switzerland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 20.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bull Run Org Domain Security
  slug: bull-run-org-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bull-run-org
tags:
- Finance
- ETFs
- Comparison
- Zurich
- Fintech
website: https://bull-run.org/
---
