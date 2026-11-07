---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Developer API for Reekoh integration, documented at the Autodesk Tandem developer resources page.
  name: Reekoh Data API
  slug: reekoh-data-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/reekoh/vendors/reekoh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/reekoh-vendors.yml
- group: other
  href: https://artifacts.apis.io/reekoh/hosts/reekoh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/reekoh-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.autodesk.com/support/technical/product/tandem
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.autodesk.com/company/legal-notices-trademarks/privacy-statement
- group: commercial
  title: ''
  type: Pricing
  url: https://www.autodesk.com/plans
- group: auth
  href: https://artifacts.apis.io/reekoh/security/reekoh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/reekoh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://intandem.autodesk.com/
coverage:
  checked: '2026-10-21'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found on discovered hosts.
  evidence:
  - status: null
    url: https://api.reekoh.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Reekoh is an award‑winning Industrial Integration Cloud platform that enables seamless integration of data from any asset, operational or business system, on the edge or in the cloud. Acquired by Autodesk in 2023, Reekoh provides a toolkit for building IoT, PaaS, and data orchestration solutions, helping enterprises accelerate digital transformation.
layout: provider
modified: '2026-10-21'
name: Reekoh
nav: Providers
network: true
overview: 'Reekoh is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include IoT, Integration, Platform, Cloud, and Autodesk.


  Reekoh''s developer surface includes support, pricing, and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 53.6
    operational_transparency: 0.0
  previous_composite: 9.7
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/reekoh/reekoh-2026-11-03T142112.png
security:
- kind: domain-security
  name: Reekoh Domain Security
  slug: reekoh-domain-security
  summary_line: TLSv1.2 · HSTS
slug: reekoh
tags:
- IoT
- Integration
- Platform
- Cloud
- Autodesk
website: https://intandem.autodesk.com/
---
