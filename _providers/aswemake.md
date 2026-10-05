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
  href: https://raw.githubusercontent.com/api-evangelist/aswemake/refs/heads/main/hosts/aswemake-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aswemake-hosts.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.aswemake.com/team
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aswemake/refs/heads/main/security/aswemake-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aswemake-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aswemake.com
coverage:
  checked: 2026-09-26
  detail: The provider's website https://www.aswemake.com returns HTML with no accessible API documentation or machine‑readable spec.
  evidence:
  - status: 200
    url: https://www.aswemake.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: Aswemake Inc. operates a digital platform for food and beverage retail, unifying offline grocery information into an online service that reduces costs for consumers and enhances competitiveness for merchants. The company offers a marketplace where customers can purchase food items at low prices, leveraging technology to streamline logistics and provide a seamless shopping experience across South Korea.
image: https://framerusercontent.com/assets/6UK8Gu1q3JVaGIaK2mFlRkIREk.webp
layout: provider
modified: '2026-09-26'
name: Aswemake
nav: Providers
network: true
overview: Aswemake is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food Tech, Marketplace, South Korea, and Retail.
random_paper: 10
score:
  band: minimal
  composite: 3.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aswemake Domain Security
  slug: aswemake-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aswemake
tags:
- Company
- Food Tech
- Marketplace
- South Korea
- Retail
website: https://www.aswemake.com
---
