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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/drizly/hosts/drizly-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drizly-hosts.yml
- group: other
  href: https://artifacts.apis.io/drizly/vendors/drizly-vendors.yml
  title: ''
  type: Vendors
  url: vendors/drizly-vendors.yml
- group: auth
  href: https://artifacts.apis.io/drizly/security/drizly-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drizly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://forgeglobal.com/drizly_stock/
created: '2026-10-24'
description: Drizly is an online alcohol delivery platform that connects consumers with local liquor stores, allowing users to browse, order, and have alcoholic beverages delivered to their door. Founded in 2012 and based in Boston, Drizly operates across the United States, offering a wide selection of wine, beer, and spirits. The service integrates with partner retailers and provides real‑time inventory, delivery tracking, and age verification. Drizly’s API enables partners to access product catalogs, place orders, and manage deliveries, supporting e‑commerce and mobile applications.
layout: provider
modified: '2026-10-24'
name: Drizly
nav: Providers
network: true
overview: Drizly is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Alcohol, Delivery, E-commerce, and API.
random_paper: 22
score:
  band: minimal
  composite: 3.1
  coverage:
    artifact_dirs: 6
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
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
  name: Drizly Domain Security
  slug: drizly-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: drizly
tags:
- Company
- Alcohol
- Delivery
- E-commerce
- API
website: https://forgeglobal.com/drizly_stock/
---
