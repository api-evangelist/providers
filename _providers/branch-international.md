---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Branch International services (no OpenAPI spec found)
  name: Branch API
  slug: branch-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/branch-international/well-known/branch-international-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/branch-international-well-known.yml
- group: other
  href: https://artifacts.apis.io/branch-international/hosts/branch-international-hosts.yml
  title: ''
  type: Hosts
  url: hosts/branch-international-hosts.yml
- group: other
  href: https://artifacts.apis.io/branch-international/vendors/branch-international-vendors.yml
  title: ''
  type: Vendors
  url: vendors/branch-international-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://branch.co/legal/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://branch.co/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://branch.co/legal/privacy-policies
- group: company
  title: ''
  type: Newsroom
  url: https://branch.co/news
- group: auth
  href: https://artifacts.apis.io/branch-international/security/branch-international-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/branch-international-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://branch.co/
coverage:
  checked: '2026-10-03'
  detail: JavaScript shell page at https://branch.co/ prevents machine-readable docs discovery.
  evidence:
  - status: 200
    url: https://branch.co/
  - status: 404
    url: https://api.branch.co/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-03'
description: Branch International offers a smartphone‑based finance app that provides digital banking products such as instant loans, money transfers, bill payment, high‑yield investments, savings accounts, and a debit card for payments and ATM withdrawals. The service is aimed at consumers in emerging markets, primarily across Africa and India, and is delivered through a mobile‑only platform.
layout: provider
modified: '2026-10-03'
name: Branch International
nav: Providers
network: true
overview: Branch International is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Digital Banking, Loans, Payments, Investment, and Savings.
random_paper: 3
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 54.5
    operational_transparency: 5.3
  previous_composite: 10.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 14.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/branch-international/branch-international-2026-11-03T122452.png
security:
- kind: domain-security
  name: Branch International Domain Security
  slug: branch-international-domain-security
  summary_line: TLSv1.3 · DMARC
slug: branch-international
tags:
- Digital Banking
- Loans
- Payments
- Investment
- Savings
- Emerging Markets
- Mobile Finance
website: https://branch.co/
---
