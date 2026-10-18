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
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: API surface not discovered; no machine-readable contract found.
  name: brrr API
  slug: brrr-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brrr/refs/heads/main/hosts/brrr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brrr-hosts.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.brrr.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.brrr.com/category/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brrr/refs/heads/main/security/brrr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brrr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.brrr.com
- group: company
  title: ''
  type: About
  url: https://www.brrr.com/who-we-are/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brrr.com/privacy-policy/
coverage:
  checked: '2026-10-06'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract was found on api.brrr.com or www.brrr.com.
  evidence:
  - status: 0
    url: https://api.brrr.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Brrr is a fashion‑tech company that creates cooling performance fabrics using its proprietary Triple Chill Effect™ technology. The fabrics draw heat and moisture away from the skin, providing continuous cooling for everyday wear. Brrr offers a range of products, including the brrr° Pro line with micro‑mineral enhancements and recycled polyester blends, and provides custom fabric development for clients.
image: https://www.brrr.com/wp-content/uploads/2024/05/cooling-minerals.png
layout: provider
modified: '2026-10-06'
name: Brrr
nav: Providers
network: true
overview: 'Brrr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, FashionTech, CoolingFabric, Sustainable, and CustomFabric.


  Brrr''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Brrr Domain Security
  slug: brrr-domain-security
  summary_line: TLSv1.2 · DMARC
slug: brrr
tags:
- Company
- FashionTech
- CoolingFabric
- Sustainable
- CustomFabric
website: https://www.brrr.com
---
