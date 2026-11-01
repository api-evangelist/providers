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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Provides access to city data functions such as address profiles, crime statistics, budget information, and more.
  name: City Data API
  slug: city-data-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/adamwanninger-com/hosts/adamwanninger-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adamwanninger-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/adamwanninger-com/vendors/adamwanninger-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adamwanninger-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/adamwanninger-com/security/adamwanninger-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adamwanninger-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adamwanninger.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adamwanninger.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adamwanninger.com/terms/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ajwann
coverage:
  checked: '2026-10-30'
  detail: No machine‑readable OpenAPI, GraphQL, AsyncAPI, or gRPC spec is publicly accessible; attempts to fetch common spec URLs returned 503 or were blocked.
  evidence:
  - status: 0
    url: https://api.adamwanninger.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Adam Wanninger operates a suite of Model Context Protocol (MCP) servers that expose public transit, city data, and other municipal information as AI‑ready tools. Hosted at queenscoach.adamwanninger.com and queensestate.adamwanninger.com, these servers let assistants retrieve real‑time bus arrivals, schedule timetables, address profiles, crime statistics, and budget data. The site also provides links to source code on GitHub and packages on PyPI, emphasizing open‑source transparency and community‑driven development.
image: https://placehold.co/600x400
layout: provider
modified: '2026-10-29'
name: adamwanninger-com
nav: Providers
network: true
overview: adamwanninger-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include MCP, Transit, Open-Data, AI-Tools, and City-Data.
plans:
- name: Adamwanninger Com Plans Pricing
  plan_count: 0
  slug: adamwanninger-com-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Adamwanninger Com Rate Limits
  slug: adamwanninger-com-rate-limits
scopes:
- name: Adamwanninger Com Scopes
  scope_count: 0
  slug: adamwanninger-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adamwanninger Com Authentication
  slug: adamwanninger-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adamwanninger Com Domain Security
  slug: adamwanninger-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adamwanninger-com
tags:
- MCP
- Transit
- Open-Data
- AI-Tools
- City-Data
- Company
website: https://adamwanninger.com/
---
