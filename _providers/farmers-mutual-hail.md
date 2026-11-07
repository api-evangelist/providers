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
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/farmers-mutual-hail/hosts/farmers-mutual-hail-hosts.yml
  title: ''
  type: Hosts
  url: hosts/farmers-mutual-hail-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.fmh.com/about/news/2026/05/01/InsureCast-Spring26
- group: start
  title: ''
  type: Login
  url: https://ph.fmh.com/policyholderCenter/preLogIn/logIn
- group: other
  title: ''
  type: Leadership
  url: https://www.fmh.com/about/leadership
- group: docs
  title: ''
  type: Documentation
  url: https://www.fmh.com/docs/librariesprovider79/support-library/teamviewerqs_en.exe
- group: auth
  href: https://artifacts.apis.io/farmers-mutual-hail/security/farmers-mutual-hail-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/farmers-mutual-hail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fmh.com/
- group: operate
  title: ''
  type: Support
  url: https://www.fmh.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fmh.com/legal-compliance/privacy-statement
coverage:
  checked: '2026-10-28'
  detail: All attempted OpenAPI spec URLs returned HTML pages, not machine-readable specifications.
  evidence:
  - status: 200
    url: https://ci.fmh.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Farmers Mutual Hail (FMH) is a U.S.-based insurance provider specializing in crop hail coverage. With six generations of protecting farmers against hail damage, FMH leads the industry in offering comprehensive crop hail insurance solutions. The company serves agricultural producers across the United States, helping them mitigate financial losses from severe weather events and ensuring the continuity of farming operations. FMH’s mission is to safeguard the livelihoods of farmers by delivering reliable, affordable insurance products tailored to the unique risks of agriculture.
image: https://www.fmh.com/images/librariesprovider79/default-album/fmh_logo.png
layout: provider
modified: '2026-10-28'
name: Farmers Mutual Hail
nav: Providers
network: true
overview: 'Farmers Mutual Hail is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Agriculture, Hail, and Crop.


  Farmers Mutual Hail''s developer surface includes documentation, support, and 7 more developer resources.'
plans:
- name: Farmers Mutual Hail Plans Pricing
  plan_count: 0
  slug: farmers-mutual-hail-plans-pricing
random_paper: 0
scopes:
- name: Farmers Mutual Hail Scopes
  scope_count: 0
  slug: farmers-mutual-hail-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.2
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
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
  previous_composite: 13.8
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/farmers-mutual-hail/farmers-mutual-hail-2026-11-03T131846.png
security:
- kind: authentication
  name: Farmers Mutual Hail Authentication
  slug: farmers-mutual-hail-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Farmers Mutual Hail Domain Security
  slug: farmers-mutual-hail-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: farmers-mutual-hail
tags:
- Company
- Insurance
- Agriculture
- Hail
- Crop
- United States
website: https://www.fmh.com/
---
