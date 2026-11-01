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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/zucks/hosts/zucks-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zucks-hosts.yml
- group: build
  href: https://artifacts.apis.io/zucks/packages/zucks-packages.yml
  title: ''
  type: SDKs
  url: packages/zucks-packages.yml
- group: build
  href: https://artifacts.apis.io/zucks/packages/zucks-packages.yml
  title: ''
  type: Packages
  url: packages/zucks-packages.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zucks
- group: auth
  href: https://artifacts.apis.io/zucks/security/zucks-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zucks-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zucks.co.jp/
coverage:
  checked: '2026-10-28'
  detail: Provider homepage https://zucks.co.jp/ serves a JavaScript shell with no accessible API documentation
  evidence:
  - status: 200
    url: https://zucks.co.jp/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Zucks operates a smartphone advertising platform connecting advertisers and publishers. It offers an ad network and affiliate services, providing tools for media and app developers to monetize their content. The company emphasizes performance-driven mobile ads and supports multiple languages (JP, EN, CN). It is part of CARTA ZERO Inc., focusing on innovative mobile ad solutions.
image: http://zucks.co.jp/assets/img/common/logo_ogp.png
layout: provider
modified: '2026-10-28'
name: Zucks
nav: Providers
network: true
overview: Zucks is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 8
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 39.3
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Zucks Domain Security
  slug: zucks-domain-security
  summary_line: TLSv1.2
slug: zucks
tags:
- Company
website: https://zucks.co.jp/
---
