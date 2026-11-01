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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API referenced on the public site, hosted at https://api.gonitros.com
  name: GoNitro API
  slug: gonitro-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/gonitros-com/hosts/gonitros-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gonitros-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/gonitros-com/vendors/gonitros-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gonitros-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/gonitros-com/security/gonitros-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gonitros-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gonitros.com
coverage:
  checked: '2026-10-21'
  detail: The developer site appears to be a JavaScript‑rendered portal with no machine‑readable OpenAPI spec.
  evidence:
  - status: 404
    url: https://api.gonitros.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: GoNitro provides a Shopify‑based e‑commerce platform offering digital products and services. Its public site https://gonitros.com shows an Arabic‑language storefront with product listings, a shopping cart, and references to an API at https://api.gonitros.com. The company is backed by 500‑global and appears in venture‑portfolio data.
layout: provider
modified: '2026-10-21'
name: GoNitro
nav: Providers
network: true
overview: GoNitro is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, e-commerce, Shopify, DigitalProducts, and API.
random_paper: 1
score:
  band: minimal
  composite: 4.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 62.5
    operational_transparency: 0.0
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
  name: Gonitros Com Domain Security
  slug: gonitros-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gonitros-com
tags:
- Company
- e-commerce
- Shopify
- DigitalProducts
- API
website: https://gonitros.com
---
