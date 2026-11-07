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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://artifacts.apis.io/thepackworks-com/well-known/thepackworks-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/thepackworks-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/thepackworks-com/hosts/thepackworks-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thepackworks-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/thepackworks-com/security/thepackworks-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thepackworks-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thepackworks.com/
- group: company
  title: ''
  type: Blog
  url: https://packworks.io/blog/
coverage:
  checked: '2026-10-29'
  detail: Packworks website and subdomains return no OpenAPI, AsyncAPI, GraphQL, or other machine-readable API specifications.
  evidence:
  - status: 404
    url: https://packworks.io/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Packworks is dedicated to empowering Filipino sari-sari entrepreneurs. With adaptable technology built from the ground up, we design systems that bring sari-sari stores to the digital age. Meet the high-powered, passionate and driven team that makes Packworks. With our combined experience and expertise, we're always on the lookout for new ways to help our sari-preneurs.
image: https://packworks.io/wp-content/uploads/2023/03/wp-thumb-1.png
layout: provider
modified: '2026-10-29'
name: Packworks
nav: Providers
network: true
overview: 'Packworks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Marketplace, Philippines, and Sari-sari.


  Packworks'' developer surface includes engineering blog and 4 more developer resources.'
random_paper: 10
scopes:
- name: Thepackworks Com Scopes
  scope_count: 0
  slug: thepackworks-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - philippines
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Thepackworks Com Authentication
  slug: thepackworks-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Thepackworks Com Domain Security
  slug: thepackworks-com-domain-security
  summary_line: DMARC
slug: thepackworks-com
tags:
- Company
- Fintech
- Marketplace
- Philippines
- Sari-sari
website: https://thepackworks.com/
---
