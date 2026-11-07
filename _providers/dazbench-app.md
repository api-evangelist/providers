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
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documentation for Dazbench platform providing AI task management.
  name: Dazbench API
  slug: dazbench-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dazbench-app/well-known/dazbench-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dazbench-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/dazbench-app/hosts/dazbench-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dazbench-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/dazbench-app/vendors/dazbench-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dazbench-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dazbench.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dazbench.app/privacy
- group: start
  title: ''
  type: Login
  url: https://dazbench.app/login
- group: docs
  title: ''
  type: Documentation
  url: https://dazbench.app/docs
- group: auth
  href: https://artifacts.apis.io/dazbench-app/security/dazbench-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dazbench-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dazbench.app/
coverage:
  checked: '2026-11-05'
  detail: Provider documentation at https://dazbench.app/docs is markdown only and contains no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://dazbench.app/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dazbench provides a platform where users can turn a single line of instruction into a fully‑fleshed AI‑generated task. It offers context‑ready work cards, allowing AI models like ChatGPT, Claude, or Codex to receive purpose, background, and acceptance criteria, then produce the completed output. The service includes a free starter tier, integration via MCP, and a UI for managing AI‑driven workflows.
layout: provider
modified: '2026-11-05'
name: Dazbench
nav: Providers
network: true
overview: 'Dazbench is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Productivity, Task Management, No-Code, and Company.


  Dazbench''s developer surface includes documentation and 8 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 14.6
  coverage:
    artifact_dirs: 7
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dazbench App Domain Security
  slug: dazbench-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dazbench-app
tags:
- Artificial Intelligence
- Productivity
- Task Management
- No-Code
- Company
website: https://dazbench.app/
---
