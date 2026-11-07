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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/financial-engines/hosts/financial-engines-hosts.yml
  title: ''
  type: Hosts
  url: hosts/financial-engines-hosts.yml
- group: other
  href: https://artifacts.apis.io/financial-engines/vendors/financial-engines-vendors.yml
  title: ''
  type: Vendors
  url: vendors/financial-engines-vendors.yml
- group: auth
  href: https://artifacts.apis.io/financial-engines/security/financial-engines-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/financial-engines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://edelmanfinancialengines.com
created: '2026-10-22'
description: Edelman Financial Engines (EFE) is an American financial planning and investment advisory company. As of December 31, 2023, it has more than $270 billion in assets under management and serves over 1.3 million clients. Formed in 2018 by the merger of Financial Engines and Edelman Financial Services, it provides retirement planning, wealth management, and investment advice.
layout: provider
modified: '2026-10-22'
name: Financial Engines
nav: Providers
network: true
overview: Financial Engines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Planning, Investment-Advice, Wealth Management, Retirement Planning, and United States.
random_paper: 19
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 3.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/financial-engines/financial-engines-2026-11-03T132012.png
security:
- kind: domain-security
  name: Financial Engines Domain Security
  slug: financial-engines-domain-security
  summary_line: TLSv1.3 · DMARC
slug: financial-engines
tags:
- Financial Planning
- Investment-Advice
- Wealth Management
- Retirement Planning
- United States
website: https://edelmanfinancialengines.com
---
