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
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/amekazetaiyo/refs/heads/main/hosts/amekazetaiyo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amekazetaiyo-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://ame-kaze-taiyo.jp/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/amekazetaiyo/refs/heads/main/security/amekazetaiyo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amekazetaiyo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ame-kaze-taiyo.jp
- group: operate
  title: ''
  type: Contact
  url: https://ame-kaze-taiyo.jp/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ame-kaze-taiyo.jp/privacy_policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ame-kaze-taiyo.jp/consumer_protection
coverage:
  checked: 2026-09-24
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found at the provider's API hosts.
  evidence:
  - status: failed
    url: https://api.ame-kaze-taiyo.jp/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Amekazetaiyo (株式会社雨風太陽) is a Japanese company focused on connecting urban and rural areas, fostering "relationship population" through various services such as food distribution, local commerce platforms, and community impact projects. Their mission is to blend cities and countryside, creating mutual support and sustainable growth across Japan.
image: https://ame-kaze-taiyo.jp/wp-content/uploads/2022/04/ogp.jpg
layout: provider
modified: '2026-09-24'
name: Amekazetaiyo
nav: Providers
network: true
overview: Amekazetaiyo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Japan, UrbanRural, Community, and Services.
random_paper: 8
score:
  band: minimal
  composite: 8.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 8.9
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amekazetaiyo Domain Security
  slug: amekazetaiyo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: amekazetaiyo
tags:
- Company
- Japan
- UrbanRural
- Community
- Services
website: https://ame-kaze-taiyo.jp
---
