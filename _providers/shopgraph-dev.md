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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: ShopGraph provides a GraphQL API for accessing e-commerce shop data, as described on the developer site.
  name: ShopGraph API
  slug: shopgraph-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/shopgraph-dev/hosts/shopgraph-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shopgraph-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/shopgraph-dev/vendors/shopgraph-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shopgraph-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/shopgraph-dev/security/shopgraph-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shopgraph-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://shopgraph.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://shopgraph.dev/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://shopgraph.dev/pricing
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, GraphQL SDL, AsyncAPI, gRPC, or WSDL spec was found on the provider's hosts.
  evidence:
  - status: 404
    url: https://api.shopgraph.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: shopgraph-dev is a company that provides a developer-friendly GraphQL API for accessing e-commerce shop data. It enables developers to query product catalogs, inventory, orders, and customer information across multiple storefronts using a unified schema. The platform focuses on simplifying integration for SaaS applications, mobile apps, and analytics tools, offering robust documentation, rate limiting, and webhook support. It aims to accelerate time‑to‑market for merchants and developers alike, fostering a vibrant ecosystem of extensions and third‑party services.
layout: provider
modified: '2026-10-31'
name: shopgraph-dev
nav: Providers
network: true
overview: 'shopgraph-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-commerce, GraphQL, API, and DeveloperTools.


  shopgraph-dev''s developer surface includes documentation, pricing, and 4 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
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
  name: Shopgraph Dev Domain Security
  slug: shopgraph-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: shopgraph-dev
tags:
- Company
- E-commerce
- GraphQL
- API
- DeveloperTools
website: https://shopgraph.dev/
---
