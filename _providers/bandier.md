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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bandier/refs/heads/main/security/bandier-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bandier-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bandier.com
created: '2026-09-27'
description: Bandier is a fashion retailer offering a curated selection of contemporary clothing, accessories, and lifestyle products. The brand focuses on delivering high-quality, trend-forward items for men and women, emphasizing sustainability and community engagement. Their online presence provides news, partner updates, and a platform for customers to stay informed about new collections and initiatives.
layout: provider
modified: '2026-09-27'
name: Bandier
nav: Providers
network: true
overview: Bandier is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fashion, Retail, E-Commerce, and Activewear.
random_paper: 21
score:
  band: minimal
  composite: 3.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
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
  name: Bandier Domain Security
  slug: bandier-domain-security
  summary_line: TLSv1.2 · DMARC
slug: bandier
tags:
- Company
- Fashion
- Retail
- E-Commerce
- Activewear
website: https://www.bandier.com
---
