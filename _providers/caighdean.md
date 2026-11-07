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
- description: Provides linguistic data and tools for Irish and other Celtic languages via a public API documented on GitHub.
  name: Caighdean API
  slug: caighdean-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/caighdean/hosts/caighdean-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caighdean-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/kscanne/filiocht/releases
- group: auth
  href: https://artifacts.apis.io/caighdean/security/caighdean-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caighdean-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cadhan.com/
coverage:
  checked: '2026-10-27'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract is published; only API documentation links are on GitHub.
  evidence:
  - status: 404
    url: https://cadhan.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Caighdean (cadhan.com) is an Irish language digital resource platform offering a suite of linguistic tools, dictionaries, spell‑checkers, and corpora. It provides open‑source APIs for Gaelic, Irish, Manx, and other Celtic languages, supporting developers, researchers, and language learners with access to lexical data, grammar resources, and text processing services.
layout: provider
modified: '2026-10-27'
name: Caighdean (cadhan.com)
nav: Providers
network: true
overview: 'Caighdean (cadhan.com) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Language, Open Source, Irish, and Celtic.


  Caighdean (cadhan.com)''s developer surface includes changelog and 3 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 6.0
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
screenshot: https://apis.io/screenshots/caighdean/caighdean-2026-11-03T122943.png
security:
- kind: domain-security
  name: Caighdean Domain Security
  slug: caighdean-domain-security
  summary_line: TLSv1.3
slug: caighdean
tags:
- Company
- Language
- Open Source
- Irish
- Celtic
website: https://cadhan.com/
---
