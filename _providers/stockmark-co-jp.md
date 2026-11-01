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
  href: https://artifacts.apis.io/stockmark-co-jp/hosts/stockmark-co-jp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stockmark-co-jp-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://stockmark.co.jp/security/
- group: company
  title: ''
  type: Newsroom
  url: https://stockmark.co.jp/news/
- group: auth
  href: https://artifacts.apis.io/stockmark-co-jp/security/stockmark-co-jp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stockmark-co-jp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://stockmark.co.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://stockmark.co.jp/solution/
- group: docs
  title: ''
  type: APIReference
  url: https://stockmark.co.jp/solution/
- group: start
  title: ''
  type: GettingStarted
  url: https://stockmark.co.jp/solution/
- group: company
  title: ''
  type: Blog
  url: https://stockmark-tech.hatenablog.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stockmark.co.jp/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stockmark.co.jp/privacy/
coverage:
  checked: '2026-10-19'
  detail: The solution page provides documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract.
  evidence:
  - status: 200
    url: https://stockmark.co.jp/solution/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-18'
description: Stockmark株式会社は、AIを活用した価値創造の仕組みを再発明することをミッションとする日本のテクノロジー企業です。AI SaaS・PaaS事業を通じて、企業の業務プロセスを再設計し、暗黙知を資産化するソリューションを提供しています。データの構造化やナレッジグラフ構築など、組織の情報資産化を支援し、業務効率化とイノベーション創出を実現します。
image: https://stockmark.co.jp/wp/wp-content/uploads/2026/06/stockmark_ogp.png
layout: provider
modified: '2026-10-18'
name: Stockmark
nav: Providers
network: true
overview: 'Stockmark is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Software-as-a-Service, Platform-as-a-Service, Knowledge Management, and Japan.


  Stockmark''s developer surface includes documentation, API reference, getting-started guide, engineering blog, and 7 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 31.0
    discoverability: 41.1
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stockmark Co Jp Domain Security
  slug: stockmark-co-jp-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stockmark-co-jp
tags:
- Artificial Intelligence
- Software-as-a-Service
- Platform-as-a-Service
- Knowledge Management
- Japan
website: https://stockmark.co.jp/
---
