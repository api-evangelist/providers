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
- description: File your acreage report digitally with FSA and RMA. Less paperwork, fewer errors, and more accuracy with your existing field data.
  name: MyAgData API
  slug: myagdata-api
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/myagdata/hosts/myagdata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/myagdata-hosts.yml
- group: other
  href: https://artifacts.apis.io/myagdata/vendors/myagdata-vendors.yml
  title: ''
  type: Vendors
  url: vendors/myagdata-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://myagdata.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://myagdata.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://myagdata.com/news
- group: auth
  href: https://artifacts.apis.io/myagdata/security/myagdata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/myagdata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://myagdata.com/
- group: auth
  href: https://artifacts.apis.io/myagdata/security/myagdata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/myagdata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://myagdata.com/
- group: company
  title: ''
  type: Blog
  url: https://myagdata.com/blogs
- group: operate
  title: ''
  type: Support
  url: https://myagdata.com/contact-us
coverage:
  checked: '2026-10-28'
  detail: No API documentation or machine-readable contract was found; attempts to fetch common OpenAPI and GraphQL endpoints returned 404 or no response.
  evidence:
  - status: 404
    url: https://myagdata.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: MyAgData provides USDA‑authorized electronic acreage reporting services for farmers and agribusinesses. Founded in 2012, the platform digitizes the submission of acreage reports to the Farm Service Agency (FSA) and Risk Management Agency (RMA), reducing paperwork, minimizing errors, and accelerating processing. Users can upload field data, validate reports, and submit directly to USDA through a secure portal. The service offers a dedicated account manager, transparent pricing per report or per acre, and integrates with existing farm management systems.
image: https://cdn.prod.website-files.com/6943c6f5e5551530d5ad7a85/69d952205997492c07e387d1_MyAgData_Website_Open%20Graph%20Images_1200x628px.png
layout: provider
modified: '2026-10-28'
name: MyAgData
nav: Providers
network: true
overview: 'MyAgData is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agriculture, USDA, Reporting, and Data.


  MyAgData''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 0
scopes:
- name: Myagdata Scopes
  scope_count: 0
  slug: myagdata-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 58.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 12.8
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
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/myagdata/myagdata-2026-11-03T135937.png
security:
- kind: authentication
  name: Myagdata Authentication
  slug: myagdata-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Myagdata Domain Security
  slug: myagdata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: myagdata
tags:
- Company
- Agriculture
- USDA
- Reporting
- Data
- Technology
website: https://myagdata.com/
---
