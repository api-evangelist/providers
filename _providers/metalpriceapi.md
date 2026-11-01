---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/metalpriceapi/plans/metalpriceapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/metalpriceapi-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/metalpriceapi/hosts/metalpriceapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/metalpriceapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/metalpriceapi/vendors/metalpriceapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/metalpriceapi-vendors.yml
- group: build
  href: https://artifacts.apis.io/metalpriceapi/packages/metalpriceapi-packages.yml
  title: ''
  type: SDKs
  url: packages/metalpriceapi-packages.yml
- group: build
  href: https://artifacts.apis.io/metalpriceapi/packages/metalpriceapi-packages.yml
  title: ''
  type: Packages
  url: packages/metalpriceapi-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://metalpriceapi.com/use-cases/media
- group: start
  title: ''
  type: Login
  url: https://metalpriceapi.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/metalpriceapi
- group: auth
  href: https://artifacts.apis.io/metalpriceapi/security/metalpriceapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/metalpriceapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metalpriceapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://metalpriceapi.com/documentation
- group: commercial
  title: ''
  type: Pricing
  url: https://metalpriceapi.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://metalpriceapi.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://metalpriceapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://metalpriceapi.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://metalpriceapi.com/#support
coverage:
  checked: '2026-10-27'
  detail: The provider's documentation site returns HTML pages and redirects for typical spec URLs (e.g., /openapi.json) but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL files are available.
  evidence:
  - status: 301
    url: https://metalpriceapi.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Metal Price API provides free real-time and historical precious metals and foreign exchange (FOREX) rates via a simple RESTful API. It offers spot prices for gold, silver, platinum, palladium and more, enabling businesses to integrate up-to-date metal pricing data into applications, dashboards, and trading systems. The service includes hourly and daily endpoints, supports multiple currencies, and is designed for easy integration with clear documentation and example code.
image: https://metalpriceapi.com/share.png
layout: provider
modified: '2026-10-27'
name: Metal Price API
nav: Providers
network: true
overview: 'Metal Price API is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Metals, Finance, API, and Data.


  Metal Price API''s developer surface includes documentation, pricing, engineering blog, support, and 12 more developer resources.'
plans:
- name: Metalpriceapi Plans Pricing
  plan_count: 9
  slug: metalpriceapi-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Metalpriceapi Domain Security
  slug: metalpriceapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: metalpriceapi
tags:
- Company
- Metals
- Finance
- API
- Data
website: https://metalpriceapi.com/
---
