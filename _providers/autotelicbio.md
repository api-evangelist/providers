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
  href: https://raw.githubusercontent.com/api-evangelist/autotelicbio/refs/heads/main/hosts/autotelicbio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autotelicbio-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autotelic.co.kr/en/sub/policy/privacy.php
- group: company
  title: ''
  type: Newsroom
  url: https://autotelic.co.kr/en/sub/news/news.php
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autotelicbio/refs/heads/main/security/autotelicbio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autotelicbio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autotelic.co.kr/en
coverage:
  checked: 2026-09-26
  detail: No OpenAPI or other machine‑readable contract discovered at https://api.co.kr/openapi.json (HTTP 0).
  evidence:
  - status: 0
    url: https://api.co.kr/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Autotelicbio is a biotechnology company focused on developing innovative therapies for central nervous system and rare diseases. Based in South Korea, the firm aims to improve patients’ quality of life through cutting‑edge drug discovery, leveraging expertise in ASO, small‑molecule, and combination therapies. Autotelic Bio emphasizes scientific excellence, shared growth, and transparency in its mission to become a global leader in treating incurable conditions.
image: https://autotelic.co.kr/img/common/img.jpg
layout: provider
modified: '2026-09-26'
name: Autotelicbio
nav: Providers
network: true
overview: Autotelicbio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, CNS, Rare Disease, and South Korea.
random_paper: 8
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autotelicbio Domain Security
  slug: autotelicbio-domain-security
  summary_line: TLSv1.3
slug: autotelicbio
tags:
- Company
- Biotechnology
- CNS
- Rare Disease
- South Korea
website: https://autotelic.co.kr/en
---
