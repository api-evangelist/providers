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
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arsagapartners/refs/heads/main/hosts/arsagapartners-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arsagapartners-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.arsaga.jp/news/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arsagapartners/refs/heads/main/security/arsagapartners-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arsagapartners-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.arsaga.jp
- group: company
  title: ''
  type: Blog
  url: https://www.arsaga.jp/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arsaga.jp/privacy-policy/
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://www.arsaga.jp/security-policy/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/arsagapartners
  reason: no-developer-program
  state: none
created: '2026-09-26'
description: Arsagapartners, operating as アルサーガパートナーズ株式会社, is a Japan‑based consulting and technology firm delivering end‑to‑end digital transformation (DX) solutions. It offers consulting, system development, AI services, and a suite of AI‑powered tools such as ARSAGA VIDEO CREATE and Chatty. The company combines a team of 100 consultants and 300 engineers to support clients across various industries, focusing on AI, web marketing, and custom software development.
image: https://www.arsaga.jp/wp/wp-content/uploads/2025/11/og-image.jpg
layout: provider
modified: '2026-09-26'
name: Arsagapartners
nav: Providers
network: true
overview: 'Arsagapartners is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consulting, Artificial Intelligence, Software Development, and Japan.


  Arsagapartners'' developer surface includes engineering blog and 6 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
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
    score: 9.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arsagapartners Domain Security
  slug: arsagapartners-domain-security
  summary_line: TLSv1.3 · DMARC
slug: arsagapartners
tags:
- Company
- Consulting
- Artificial Intelligence
- Software Development
- Japan
website: https://www.arsaga.jp
---
