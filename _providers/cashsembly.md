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
api_count: 1
apis:
- description: Cashsembly provides a set of financial calculator endpoints accessible via a public API.
  name: Cashsembly API
  slug: cashsembly-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/cashsembly/hosts/cashsembly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cashsembly-hosts.yml
- group: other
  href: https://artifacts.apis.io/cashsembly/vendors/cashsembly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cashsembly-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cashsembly.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cashsembly.com/privacy
- group: auth
  href: https://artifacts.apis.io/cashsembly/security/cashsembly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cashsembly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cashsembly.com/
coverage:
  checked: '2026-10-16'
  detail: OpenAPI spec endpoints on api.cashsembly.com return 404, and no documentation host is listed.
  evidence:
  - status: 404
    url: https://api.cashsembly.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: Cashsembly provides free financial calculators for both Canada and the United States, covering a wide range of personal finance topics such as income tax, capital gains, GST/HST, mortgage calculations, retirement planning, and more. Users can access tools for budgeting, net worth tracking, loan payments, and investment projections, all without needing to register. The platform aims to simplify complex financial calculations for individuals and professionals alike.
image: https://cashsembly.com/og/home.png
layout: provider
modified: '2026-10-16'
name: Cashsembly
nav: Providers
network: true
overview: Cashsembly is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Calculators, Personal Finance, and Canada.
random_paper: 11
score:
  band: minimal
  composite: 7.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cashsembly/cashsembly-2026-11-03T123443.png
security:
- kind: domain-security
  name: Cashsembly Domain Security
  slug: cashsembly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cashsembly
tags:
- Company
- Finance
- Calculators
- Personal Finance
- Canada
- USA
website: https://cashsembly.com/
---
