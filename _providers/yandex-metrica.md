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
- description: Yandex Metrica provides web analytics APIs for retrieving statistics, goals, and user behavior data.
  name: Yandex Metrica API
  slug: yandex-metrica-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Security
  url: https://ya.cc/t/1cSZixjB3gkSva
- group: auth
  href: https://artifacts.apis.io/yandex-metrica/well-known/yandex-metrica-yandex-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/yandex-metrica-yandex-security.txt
- group: agent
  href: https://artifacts.apis.io/yandex-metrica/well-known/yandex-metrica-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yandex-metrica-well-known.yml
- group: other
  href: https://artifacts.apis.io/yandex-metrica/hosts/yandex-metrica-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yandex-metrica-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://yandex.ru/support/metrica/ru/
- group: company
  title: ''
  type: Newsroom
  url: https://b2b.yandex.ru/adv/news
- group: auth
  href: https://artifacts.apis.io/yandex-metrica/security/yandex-metrica-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/yandex-metrica-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/yandex-metrica/security/yandex-metrica-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yandex-metrica-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metrica.yandex.com/
- group: docs
  title: ''
  type: Documentation
  url: https://b2b.yandex.ru/adv/metrika
- group: start
  title: ''
  type: DeveloperPortal
  url: https://b2b.yandex.ru/adv/metrika
- group: start
  title: ''
  type: GettingStarted
  url: https://b2b.yandex.ru/adv/metrika
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable contract discovery.
  evidence:
  - status: 200
    url: https://b2b.yandex.ru/adv/metrika
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Yandex Metrica is a free web analytics service provided by Yandex, offering detailed traffic statistics, user behavior analysis, and marketing tools for website owners and advertisers. It includes features such as real‑time reporting, goal tracking, heatmaps, and integration with Yandex.Direct and other Yandex services, helping businesses optimize their online presence and advertising spend.
image: https://avatars.mds.yandex.net/get-adv/60663/2a0000018a8dfaff5b4c34fdeb0d85df2701/orig
layout: provider
modified: '2026-10-27'
name: Yandex Metrica
nav: Providers
network: true
overview: 'Yandex Metrica is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Web Analytics, Marketing, Yandex, and Russia.


  Yandex Metrica''s developer surface includes support, documentation, getting-started guide, and 9 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 58.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - russia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/yandex-metrica/yandex-metrica-2026-11-03T150326.png
security:
- kind: domain-security
  name: Yandex Metrica Domain Security
  slug: yandex-metrica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Yandex Metrica Vulnerability Disclosure
  slug: yandex-metrica-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: yandex-metrica
tags:
- Analytics
- Web Analytics
- Marketing
- Yandex
- Russia
- Company
website: https://metrica.yandex.com/
---
