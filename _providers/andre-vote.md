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
    agent_skills: unknown
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
  score: 3.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/andre-vote/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/andre-vote/hosts/andre-vote-hosts.yml
  title: ''
  type: Hosts
  url: hosts/andre-vote-hosts.yml
- group: other
  href: https://artifacts.apis.io/andre-vote/vendors/andre-vote-vendors.yml
  title: ''
  type: Vendors
  url: vendors/andre-vote-vendors.yml
- group: auth
  href: https://artifacts.apis.io/andre-vote/security/andre-vote-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/andre-vote-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://andre.vote/
- group: operate
  title: ''
  type: Support
  url: https://andre.vote/a-propos
- group: start
  title: ''
  type: SignUp
  url: https://andre.vote/auth
- group: start
  title: ''
  type: Login
  url: https://andre.vote/auth
coverage:
  checked: '2026-11-01'
  detail: No public API documentation or machine‑readable contract is available on the provider's website.
  evidence:
  - status: 200
    url: https://andre.vote/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: André is an AI‑powered web application that analyses French election results dating back to 1999. It aggregates official voting data, maps, and demographic information to help users understand constituencies, communes, and individual polling stations. The service provides visualizations, vote reserve statistics, typologies, and temporal evolution insights, all accessible through an intuitive interface.
image: https://andre.vote/img/andre.png
layout: provider
modified: '2026-11-01'
name: André
nav: Providers
network: true
overview: 'André is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Elections, France, Artificial Intelligence, Data Analysis, and Civic Tech.


  André''s developer surface includes support, signup flow, and 6 more developer resources.'
random_paper: 5
scopes:
- name: Andre Vote Scopes
  scope_count: 0
  slug: andre-vote-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.8
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.8
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  previous_composite: 9.9
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Andre Vote Authentication
  slug: andre-vote-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Andre Vote Domain Security
  slug: andre-vote-domain-security
  summary_line: TLSv1.3 · DMARC
slug: andre-vote
tags:
- Elections
- France
- Artificial Intelligence
- Data Analysis
- Civic Tech
website: https://andre.vote/
---
