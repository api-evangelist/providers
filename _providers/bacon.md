---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for Bacon gig‑work platform
  name: Bacon API
  slug: bacon-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bacon/refs/heads/main/hosts/bacon-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bacon-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bacon/refs/heads/main/vendors/bacon-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bacon-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.baconwork.com/terms
- group: start
  title: ''
  type: SignUp
  url: https://www.baconwork.com/signup/business-or-worker
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.baconwork.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.baconwork.com/press
- group: start
  title: ''
  type: GettingStarted
  url: https://www.baconwork.com/signup/get-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bacon/refs/heads/main/security/bacon-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bacon-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.baconwork.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.baconwork.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.baconwork.com/support/home
coverage:
  checked: '2026-09-27'
  detail: The provider's documentation site provides only static HTML pages with no machine‑readable OpenAPI, GraphQL or AsyncAPI specifications.
  evidence:
  - status: 200
    url: https://www.baconwork.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Bacon develops a gig‑work app that connects established businesses to local gig workers. The platform allows businesses to post shifts and workers to find and accept them, featuring rating, reviews, and flexible staffing across multiple industries. Founded in 2018 and based in Provo, Utah, Bacon aims to simplify on‑demand temp labor for both employers and employees.
image: https://cdn.prod.website-files.com/5b32bcf34b8475e132296c72/62e2f45dae2240bc8b90216a_home_open_graph_image-01.jpg
layout: provider
modified: '2026-09-27'
name: Bacon
nav: Providers
network: true
overview: 'Bacon publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GigWork, Staffing, On-Demand, Marketplace, and Utah.


  Bacon''s developer surface includes signup flow, getting-started guide, documentation, support, and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 58.9
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bacon Domain Security
  slug: bacon-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bacon
tags:
- GigWork
- Staffing
- On-Demand
- Marketplace
- Utah
website: https://www.baconwork.com
---
