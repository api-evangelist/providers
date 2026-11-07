---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
- description: GraphQL API providing access to American Default data (authentication required)
  name: American Default GraphQL API
  slug: american-default-graphql-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/americandefault-org/llms/americandefault-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/americandefault-org-llms.txt
- group: other
  href: https://artifacts.apis.io/americandefault-org/hosts/americandefault-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/americandefault-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/americandefault-org/vendors/americandefault-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/americandefault-org-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://americandefault.org/press/
- group: docs
  title: ''
  type: Documentation
  url: https://americandefault.org/guides/car-repossession-rates/
- group: operate
  title: ''
  type: ChangeLog
  url: https://americandefault.org/methodology/releases/
- group: auth
  href: https://artifacts.apis.io/americandefault-org/security/americandefault-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/americandefault-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://americandefault.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://americandefault.org/about/
- group: operate
  title: ''
  type: Support
  url: https://americandefault.org/help/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://americandefault.org/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://americandefault.org/terms/
coverage:
  checked: '2026-11-01'
  detail: GraphQL endpoint at https://americandefault.org/api/graphql requires authentication (401)
  evidence:
  - status: 401
    url: https://americandefault.org/api/graphql
  reason: auth-required
  state: gated
created: '2026-11-01'
description: American Default Research is an independent data project that tracks U.S. household financial distress. It publishes the American Distress Index and provides county‑level, state‑level, and national distress scores, methodology, data sources, and analysis. The site offers free data downloads, visualizations, and research reports to help policymakers, journalists, and the public understand economic hardship trends.
image: https://americandefault.org/apple-touch-icon.png
layout: provider
modified: '2026-11-01'
name: American Default Research
nav: Providers
network: true
overview: 'American Default Research is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Data, Research, Economics, and US.


  American Default Research''s developer surface includes documentation, changelog, getting-started guide, support, and 8 more developer resources.'
random_paper: 2
scopes:
- name: Americandefault Org Scopes
  scope_count: 0
  slug: americandefault-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 67.0
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 19.6
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Americandefault Org Authentication
  slug: americandefault-org-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Americandefault Org Domain Security
  slug: americandefault-org-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: americandefault-org
tags:
- Finance
- Data
- Research
- Economics
- US
website: https://americandefault.org/
---
