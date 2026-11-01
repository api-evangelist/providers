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
  href: https://artifacts.apis.io/jisho/hosts/jisho-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jisho-hosts.yml
- group: build
  href: https://artifacts.apis.io/jisho/packages/jisho-packages.yml
  title: ''
  type: SDKs
  url: packages/jisho-packages.yml
- group: build
  href: https://artifacts.apis.io/jisho/packages/jisho-packages.yml
  title: ''
  type: Packages
  url: packages/jisho-packages.yml
- group: auth
  href: https://artifacts.apis.io/jisho/security/jisho-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jisho-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jisho.org/
- group: docs
  title: ''
  type: Documentation
  url: https://jisho.org/docs
- group: company
  title: ''
  type: About
  url: https://jisho.org/about
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jisho-org
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation at https://jisho.org/docs is HTML without any machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract.
  evidence:
  - status: 200
    url: https://jisho.org/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Jisho.org is an online Japanese-English dictionary providing comprehensive word definitions, example sentences, kanji details, and search tools for learners and translators. The site offers a clean web interface, API-like query parameters for advanced searches, and resources such as radical lookup and voice pronunciation, serving a global community of Japanese language enthusiasts.
layout: provider
modified: '2026-10-28'
name: Jisho.org
nav: Providers
network: true
overview: 'Jisho.org is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Japanese, Dictionary, Language-Learning, and API.


  Jisho.org''s developer surface includes documentation and 7 more developer resources.'
random_paper: 13
score:
  band: minimal
  composite: 7.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
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
  name: Jisho Domain Security
  slug: jisho-domain-security
  summary_line: TLSv1.2 · HSTS
slug: jisho
tags:
- Company
- Japanese
- Dictionary
- Language-Learning
- API
website: https://jisho.org/
---
