---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API for Carbon38 e‑commerce platform
  name: Carbon38 API
  slug: carbon38-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carbon38/refs/heads/main/llms/carbon38-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carbon38-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/carbon38/refs/heads/main/well-known/carbon38-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/carbon38-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbon38/refs/heads/main/hosts/carbon38-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carbon38-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/carbon38/refs/heads/main/vendors/carbon38-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carbon38-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://carbon38.com/pages/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/carbon38/refs/heads/main/security/carbon38-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carbon38-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbon38.com/
created: '2026-10-07'
description: Carbon38 is a performance‑fashion brand offering activewear, accessories and apparel designed for movement. The company focuses on high‑quality, functional clothing for yoga, Pilates, running and everyday wear, emphasizing sustainability and innovative fabrics. Their online store provides a wide range of products, including leggings, sports bras, shoes, and digital gift cards, serving a global customer base.
image: http://carbon38.com/cdn/shop/files/URL_Block.jpg?v=1758564277
layout: provider
modified: '2026-10-07'
name: Carbon38
nav: Providers
network: true
overview: Carbon38 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Activewear, E-Commerce, and Apparel.
random_paper: 10
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 75.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carbon38 Domain Security
  slug: carbon38-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carbon38
tags:
- Company
- Fashion
- Activewear
- E-Commerce
- Apparel
website: https://carbon38.com/
---
