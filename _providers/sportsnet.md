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
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/sportsnet/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/sportsnet/hosts/sportsnet-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sportsnet-hosts.yml
- group: other
  href: https://artifacts.apis.io/sportsnet/vendors/sportsnet-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sportsnet-vendors.yml
- group: auth
  href: https://artifacts.apis.io/sportsnet/security/sportsnet-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sportsnet-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sportsnet.ca/
- group: operate
  title: ''
  type: Support
  url: https://www.sportsnet.ca/contact-us/
coverage:
  checked: '2026-10-28'
  detail: Sportsnet provides sports news content and does not expose a public API; attempts to locate OpenAPI specifications returned 404.
  evidence:
  - status: 404
    url: https://sandbox.sportsnet.ca/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-10-28'
description: Sportsnet is a Canadian sports media brand delivering news, scores, live streaming, and highlights across major leagues such as NHL, MLB, NBA, and CFL. While the company’s website hosts a sports‑stats ticker, no public API documentation or endpoints were discovered during probing. The organization’s primary online presence is at sportsnet.ca, which provides extensive sports coverage and a contact page for support.
image: https://www.sportsnet.ca/wp-content/themes/sportsnet-nhl/images/sn_logo_60x60_bg_white.png
layout: provider
modified: '2026-10-28'
name: Sportsnet stats ticker
nav: Providers
network: true
overview: 'Sportsnet stats ticker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Sports, News, Canada, and Media.


  Sportsnet stats ticker''s developer surface includes support and 5 more developer resources.'
plans:
- name: Sportsnet Plans Pricing
  plan_count: 0
  slug: sportsnet-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Sportsnet Rate Limits
  slug: sportsnet-rate-limits
scopes:
- name: Sportsnet Scopes
  scope_count: 0
  slug: sportsnet-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 5.8
  coverage:
    artifact_dirs: 21
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.8
    discoverability: 39.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.2
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
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
screenshot: https://apis.io/screenshots/sportsnet/sportsnet-2026-11-03T143651.png
security:
- kind: authentication
  name: Sportsnet Authentication
  slug: sportsnet-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sportsnet Domain Security
  slug: sportsnet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sportsnet
tags:
- Sports
- News
- Canada
- Media
website: https://sportsnet.ca/
---
