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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Programmatic advertising exchange API (no public machine-readable spec discovered)
  name: Index Exchange API
  slug: index-exchange-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/index-exchange/well-known/index-exchange-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/index-exchange-well-known.yml
- group: other
  href: https://artifacts.apis.io/index-exchange/hosts/index-exchange-hosts.yml
  title: ''
  type: Hosts
  url: hosts/index-exchange-hosts.yml
- group: build
  href: https://artifacts.apis.io/index-exchange/packages/index-exchange-packages.yml
  title: ''
  type: SDKs
  url: packages/index-exchange-packages.yml
- group: build
  href: https://artifacts.apis.io/index-exchange/packages/index-exchange-packages.yml
  title: ''
  type: Packages
  url: packages/index-exchange-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.indexexchange.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.indexexchange.com/privacy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.indexexchange.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://www.indexexchange.com/about/team/
- group: company
  title: ''
  type: Blog
  url: https://www.indexexchange.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/indexexchange
- group: auth
  href: https://artifacts.apis.io/index-exchange/security/index-exchange-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/index-exchange-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.indexexchange.com
coverage:
  checked: '2026-10-14'
  detail: The API OpenAPI spec endpoint returns a login HTML page requiring authentication.
  evidence:
  - status: 200
    url: https://api.indexexchange.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-14'
description: Index Exchange is a global programmatic advertising exchange that connects publishers and advertisers through a transparent, efficient, and data‑driven platform. It offers a suite of products including addressable advertising, real‑time bidding, analytics, and streaming‑TV solutions, enabling media owners to maximize revenue while providing buyers with high‑quality inventory and robust reporting.
image: https://s46182.pcdn.co/wp-content/uploads/2021/11/Index-Exchange-Stacked-Logo-Homepage.png
layout: provider
modified: '2026-10-14'
name: Index Exchange
nav: Providers
network: true
overview: 'Index Exchange is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Advertising, Programmatic, Supply Side Platform, Real-Time Bidding, and Media Technology.


  Index Exchange''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 9.2
  coverage:
    artifact_dirs: 9
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
    developer_ergonomics: 8.3
    discoverability: 58.9
    operational_transparency: 2.6
  previous_composite: 12.7
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
screenshot: https://apis.io/screenshots/index-exchange/index-exchange-2026-11-03T133733.png
security:
- kind: domain-security
  name: Index Exchange Domain Security
  slug: index-exchange-domain-security
  summary_line: TLSv1.3 · DMARC
slug: index-exchange
tags:
- Advertising
- Programmatic
- Supply Side Platform
- Real-Time Bidding
- Media Technology
- Company
website: https://www.indexexchange.com
---
