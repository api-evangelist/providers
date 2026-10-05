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
api_count: 1
apis:
- description: API documentation hosted at Bioportkorea's developer portal.
  name: Bioportkorea API
  slug: bioportkorea-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bioportkorea/refs/heads/main/hosts/bioportkorea-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bioportkorea-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://doc.biopk.co.kr/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bioportkorea/refs/heads/main/security/bioportkorea-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bioportkorea-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.biopk.co.kr
coverage:
  checked: '2026-09-28'
  detail: Documentation site renders JavaScript and provides no machine‑readable spec.
  evidence:
  - status: 200
    url: https://doc.biopk.co.kr/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: Bioportkorea (바이오포트코리아) is a Korean food and health product company that aims to deliver healthy happiness by discovering value in nature. It operates as a global comprehensive food company, focusing on product development, R&D, and quality management, offering domestic and overseas products, and providing detailed corporate information, investment data, and customer support through its website.
image: https://www.biopk.co.kr/image/og.jpg
layout: provider
modified: '2026-09-28'
name: Bioportkorea
nav: Providers
network: true
overview: 'Bioportkorea publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food, Health, South Korea, and Consumer Goods.


  Bioportkorea''s developer surface includes documentation and 3 more developer resources.'
random_paper: 21
score:
  band: minimal
  composite: 6.5
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bioportkorea Domain Security
  slug: bioportkorea-domain-security
  summary_line: TLSv1.2
slug: bioportkorea
tags:
- Company
- Food
- Health
- South Korea
- Consumer Goods
website: https://www.biopk.co.kr
---
