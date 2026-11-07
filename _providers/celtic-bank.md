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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
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
  score: 10.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/celtic-bank/well-known/celtic-bank-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/celtic-bank-well-known.yml
- group: other
  href: https://artifacts.apis.io/celtic-bank/hosts/celtic-bank-hosts.yml
  title: ''
  type: Hosts
  url: hosts/celtic-bank-hosts.yml
- group: other
  href: https://artifacts.apis.io/celtic-bank/vendors/celtic-bank-vendors.yml
  title: ''
  type: Vendors
  url: vendors/celtic-bank-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.celticbank.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.celticbank.com/privacy
- group: start
  title: ''
  type: Login
  url: https://my.celticbank.com/login
- group: auth
  href: https://artifacts.apis.io/celtic-bank/security/celtic-bank-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/celtic-bank-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://celticbank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.celticbank.com/resources?format=posts
- group: company
  title: ''
  type: Blog
  url: https://www.celticbank.com/resources?format=posts
- group: operate
  title: ''
  type: Contact
  url: https://www.celticbank.com/contact
coverage:
  checked: '2026-10-27'
  detail: The provider's website is a JavaScript‑rendered site with no accessible API documentation or machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.celticbank.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Celtic Bank provides commercial financing solutions, specializing in SBA loans, construction financing, asset‑based lending, equipment leasing, and strategic financing for businesses across the United States. It serves small to midsize enterprises with tailored loan products, including SBA 7(a), SBA 504, and industry‑specific financing, and offers fintech solutions and partnership programs to support growth and development.
layout: provider
modified: '2026-10-27'
name: Celtic Bank
nav: Providers
network: true
overview: 'Celtic Bank is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, SBA Loans, Commercial Lending, and Fintech.


  Celtic Bank''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/celtic-bank/celtic-bank-2026-11-03T123633.png
security:
- kind: domain-security
  name: Celtic Bank Domain Security
  slug: celtic-bank-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: celtic-bank
tags:
- Company
- Finance
- SBA Loans
- Commercial Lending
- Fintech
website: https://celticbank.com/
---
