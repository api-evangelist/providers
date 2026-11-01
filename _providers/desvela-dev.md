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
- description: Desvela AI Brand Watch platform API
  name: Desvela API
  slug: desvela-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/desvela-dev/llms/desvela-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/desvela-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/desvela-dev/hosts/desvela-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/desvela-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/desvela-dev/vendors/desvela-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/desvela-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/desvela-dev/security/desvela-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/desvela-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://desvela.dev/
coverage:
  checked: '2026-10-30'
  detail: Provider documentation at https://desvela.dev/ contains no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 404
    url: https://desvela.dev/openapi.json
  - status: 404
    url: https://registry.desvela.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Desvela AI Brand Watch provides a platform for monitoring and analyzing brand presence using AI. It offers quickstart configurations, customizable input schemas, pricing events, output metrics, audit versus watch comparisons, and webhook payload references with signature verification. The service enables both human users and agents to run, schedule, and consume brand watch data efficiently.
image: https://desvela.dev/og.png
layout: provider
modified: '2026-10-30'
name: desvela-dev
nav: Providers
network: true
overview: desvela-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, BrandMonitoring, Analytics, SaaS, and Desvela.
random_paper: 0
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 8
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
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Desvela Dev Domain Security
  slug: desvela-dev-domain-security
  summary_line: TLSv1.3
slug: desvela-dev
tags:
- AI
- BrandMonitoring
- Analytics
- SaaS
- Desvela
website: https://desvela.dev/
---
