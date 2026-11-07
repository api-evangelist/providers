---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
- description: Ask your Google Analytics questions in plain English through an MCP server. Create a GA4 property and its tag from the dashboard, audit what it is measuring, and read it on a free terminal dashboard.
  name: anacraft MCP Server
  slug: anacraft-mcp
artifact_total: 4
common:
- group: other
  href: https://artifacts.apis.io/anacraft-dev/hosts/anacraft-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anacraft-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/anacraft-dev/vendors/anacraft-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anacraft-dev-vendors.yml
- group: auth
  href: https://artifacts.apis.io/anacraft-dev/security/anacraft-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anacraft-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anacraft.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://anacraft.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anacraft.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anacraft.dev/privacy
coverage:
  checked: '2026-11-01'
  detail: No public machine‑readable API contract (OpenAPI/GraphQL/etc.) is published; only a web UI is available.
  evidence:
  - status: 200
    url: https://anacraft.dev/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: anacraft provides a conversational Google Analytics assistant powered by a Machine‑Control‑Protocol (MCP) server. Users can ask natural‑language questions about their GA4 data, generate one‑shot reports, and manage properties via a terminal‑style dashboard. The service runs entirely locally in the browser, without telemetry or server‑side data collection, and offers free basic dashboards with optional paid plans for advanced monitoring, alerts, and automation. It is open‑source software released under the Apache License 2.0.
image: https://anacraft.dev/dash.png
layout: provider
modified: '2026-11-01'
name: anacraft
nav: Providers
network: true
overview: 'anacraft is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Analytics, Google Analytics, MCP, Open Source, and Dashboards.


  anacraft''s developer surface includes pricing and 6 more developer resources.'
random_paper: 20
scopes:
- name: Anacraft Dev Scopes
  scope_count: 0
  slug: anacraft-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 13.3
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Anacraft Dev Authentication
  slug: anacraft-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Anacraft Dev Domain Security
  slug: anacraft-dev-domain-security
  summary_line: TLSv1.3
slug: anacraft-dev
tags:
- Analytics
- Google Analytics
- MCP
- Open Source
- Dashboards
- Company
website: https://anacraft.dev/
---
