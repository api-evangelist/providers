---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
  score: 10.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides a Structured Data Extraction API that transforms unstructured text and images into structured JSON using LLMs.
  name: Structured Data Extraction API
  slug: structured-data-extraction-api
artifact_total: 2
common:
- group: auth
  href: https://artifacts.apis.io/l1m/well-known/l1m-developers-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/l1m-developers-security.txt
- group: auth
  href: https://artifacts.apis.io/l1m/well-known/l1m-developer-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/l1m-developer-security.txt
- group: auth
  href: https://artifacts.apis.io/l1m/well-known/l1m-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/l1m-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/l1m/well-known/l1m-datahub-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/l1m-datahub-security.txt
- group: auth
  href: https://artifacts.apis.io/l1m/well-known/l1m-data-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/l1m-data-security.txt
- group: auth
  href: https://artifacts.apis.io/l1m/well-known/l1m-apis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/l1m-apis-security.txt
- group: auth
  href: https://artifacts.apis.io/l1m/well-known/l1m-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/l1m-api-security.txt
- group: agent
  href: https://artifacts.apis.io/l1m/well-known/l1m-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/l1m-well-known.yml
- group: other
  href: https://artifacts.apis.io/l1m/hosts/l1m-hosts.yml
  title: ''
  type: Hosts
  url: hosts/l1m-hosts.yml
- group: other
  href: https://artifacts.apis.io/l1m/vendors/l1m-vendors.yml
  title: ''
  type: Vendors
  url: vendors/l1m-vendors.yml
- group: build
  href: https://artifacts.apis.io/l1m/packages/l1m-packages.yml
  title: ''
  type: SDKs
  url: packages/l1m-packages.yml
- group: build
  href: https://artifacts.apis.io/l1m/packages/l1m-packages.yml
  title: ''
  type: Packages
  url: packages/l1m-packages.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.docs.google.com/
- group: auth
  href: https://artifacts.apis.io/l1m/security/l1m-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/l1m-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://l1m.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.l1m.io/structured
coverage:
  checked: '2026-10-18'
  detail: The API reference page returns HTTP 530 errors for common OpenAPI paths, indicating the docs are behind a JavaScript-rendered interface.
  evidence:
  - status: 530
    url: https://api.l1m.io/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: l1m.io provides a Structured Data Extraction API that transforms unstructured text and images into structured JSON using LLMs. It offers a simple schema‑first approach, zero prompt engineering, provider flexibility, built‑in caching, and no data retention. The service is open‑source and also available as a hosted solution with a free tier, targeting developers who need reliable data extraction without complex prompt design.
layout: provider
modified: '2026-10-18'
name: l1m.io
nav: Providers
network: true
overview: 'l1m.io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Extraction, LLM, and Open Source.


  l1m.io''s developer surface includes documentation, API reference, and 14 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 10.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 44.6
    operational_transparency: 10.5
  previous_composite: 10.9
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: L1M Domain Security
  slug: l1m-domain-security
  summary_line: TLSv1.3
slug: l1m
tags:
- Company
- Data Extraction
- LLM
- Open Source
website: https://l1m.io/
---
