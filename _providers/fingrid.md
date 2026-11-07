---
access_model:
  confidence: low
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/fingrid/vendors/fingrid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fingrid-vendors.yml
- group: agent
  href: https://artifacts.apis.io/fingrid/llms/fingrid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fingrid-llms.txt
- group: agent
  href: https://artifacts.apis.io/fingrid/well-known/fingrid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fingrid-well-known.yml
- group: other
  href: https://artifacts.apis.io/fingrid/hosts/fingrid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fingrid-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fingrid.fi/en/privacy-statement/
- group: company
  title: ''
  type: Newsroom
  url: https://www.fingrid.fi/en/news/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fingrid.fi/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Fingrid
- group: auth
  href: https://artifacts.apis.io/fingrid/security/fingrid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fingrid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fingrid.fi/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://fingrid.fi/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Fingrid is Finland’s national electricity transmission system operator, responsible for ensuring a reliable and secure electricity supply across the country. It plans, builds, operates and maintains the high‑voltage transmission grid, balancing supply and demand, and facilitates the integration of renewable energy sources. Fingrid also provides market participants with data and services related to grid operations, system balancing, and electricity market information, supporting the transition to a sustainable energy future.
image: https://www.fingrid.fi/globalassets/kuvat/valokuvat/www_nostokuva.jpg
layout: provider
modified: '2026-10-28'
name: Fingrid
nav: Providers
network: true
overview: 'Fingrid is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Electricity, Transmission, and Finland.


  Fingrid''s developer surface includes documentation and 9 more developer resources.'
random_paper: 19
scopes:
- name: Fingrid Scopes
  scope_count: 0
  slug: fingrid-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 56.3
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - finland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 11.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fingrid/fingrid-2026-11-03T132041.png
security:
- kind: authentication
  name: Fingrid Authentication
  slug: fingrid-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Fingrid Domain Security
  slug: fingrid-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: fingrid
tags:
- Company
- Energy
- Electricity
- Transmission
- Finland
website: https://fingrid.fi/
---
