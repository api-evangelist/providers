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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API documentation not publicly available; no machine‑readable spec discovered.
  name: Digital Brands Group API
  slug: digital-brands-group-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dstld/llms/dstld-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dstld-llms.txt
- group: agent
  href: https://artifacts.apis.io/dstld/well-known/dstld-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dstld-well-known.yml
- group: other
  href: https://artifacts.apis.io/dstld/hosts/dstld-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dstld-hosts.yml
- group: other
  href: https://artifacts.apis.io/dstld/vendors/dstld-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dstld-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dstld/security/dstld-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dstld-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dstld.la/
coverage:
  checked: '2026-10-24'
  detail: No public machine‑readable API specification was found despite probing known hosts and documentation pages.
  evidence:
  - status: 0
    url: https://api.digitalbrandsgroup.co/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Digital Brands Group (DBG) is a modern retail and technology ecosystem reshaping the shopping experience. It combines apparel brands with a suite of technology tools, leveraging operational expertise to solve logistical challenges, expand addressable markets, and protect brand assets through eCommerce and retail platforms. DBG focuses on direct‑to‑consumer sales, brand authenticity, data security, and enhanced consumer engagement across its portfolio, including the premium denim brand DSTLD.
image: http://static1.squarespace.com/static/5aa6ea9cf2e6b1a8c4d739e5/t/5b46798c8a922d14ae9a76cd/1531345297483/dbg_logo.png?format=1500w
layout: provider
modified: '2026-10-24'
name: Digital Brands Group
nav: Providers
network: true
overview: Digital Brands Group is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Fashion, Technology, and E-commerce.
random_paper: 11
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dstld Domain Security
  slug: dstld-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dstld
tags:
- Company
- Retail
- Fashion
- Technology
- E-commerce
website: https://www.dstld.la/
---
