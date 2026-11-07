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
- description: Ecere Runtime Library API reference
  name: Ecere API
  slug: ecere-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/ecere-corporation/hosts/ecere-corporation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ecere-corporation-hosts.yml
- group: auth
  href: https://artifacts.apis.io/ecere-corporation/security/ecere-corporation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ecere-corporation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://ecere.ca
- group: docs
  title: ''
  type: Documentation
  url: http://ecere.ca/gnosis/
- group: start
  title: ''
  type: DeveloperPortal
  url: http://ecere.ca/gnosis/
- group: docs
  title: ''
  type: APIReference
  url: http://ecere.ca/gnosis/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ecere
coverage:
  checked: '2026-10-26'
  detail: Docs page at https://ecere.org/docs/ loads content via JavaScript, no machine‑readable OpenAPI found.
  evidence:
  - status: 200
    url: https://ecere.org/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Ecere Corporation is a graphics software company founded in 2005, based in Canada. It develops the Ecere SDK and related tools for creating cross‑platform applications and games. The company’s website showcases its products, provides documentation, and offers downloads for developers interested in leveraging its graphics engine and development framework.
layout: provider
modified: '2026-10-26'
name: Ecere Corporation
nav: Providers
network: true
overview: 'Ecere Corporation is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Graphics, Software, SDK, and Development.


  Ecere Corporation''s developer surface includes documentation, API reference, and 5 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 6.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 53.6
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 9.9
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/ecere-corporation/ecere-corporation-2026-11-03T131254.png
security:
- kind: domain-security
  name: Ecere Corporation Domain Security
  slug: ecere-corporation-domain-security
  summary_line: TLSv1.3
slug: ecere-corporation
tags:
- Company
- Graphics
- Software
- SDK
- Development
website: http://ecere.ca
---
