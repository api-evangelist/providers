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
api_count: 1
apis:
- description: API for Artnguide platform
  name: Artnguide API
  slug: artnguide-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/artnguide/refs/heads/main/hosts/artnguide-hosts.yml
  title: ''
  type: Hosts
  url: hosts/artnguide-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.artnguide.co.kr/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/artnguide/refs/heads/main/security/artnguide-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/artnguide-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.artnguide.co.kr
coverage:
  checked: 2026-09-26
  detail: Developer portal returns a JavaScript shell with no machine‑readable OpenAPI spec
  evidence:
  - status: 200
    url: https://dev.artnguide.co.kr/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Artnguide (아트앤가이드) is a Korean platform that issues art‑investment contract securities, enabling fractional ownership of artworks. It provides a digital marketplace where users can easily start investing in art pieces through a user‑friendly interface, offering transparency, liquidity, and regulatory compliance for art‑based financial products.
image: https://artnguide.s3.ap-northeast-2.amazonaws.com/etc/artng_1715940223611_bd839ae5810a1ad3.jpg
layout: provider
modified: '2026-09-26'
name: Artnguide
nav: Providers
network: true
overview: 'Artnguide publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Art, Investment, Fintech, and South Korea.


  Artnguide''s developer surface includes documentation and 3 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 4
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 57.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Artnguide Domain Security
  slug: artnguide-domain-security
  summary_line: TLSv1.3
slug: artnguide
tags:
- Company
- Art
- Investment
- Fintech
- South Korea
website: https://www.artnguide.co.kr
---
