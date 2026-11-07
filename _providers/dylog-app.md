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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
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
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Dylog API reference page
  name: Dylog API
  slug: dylog-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/dylog-app/llms/dylog-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dylog-app-llms.txt
- group: other
  href: https://artifacts.apis.io/dylog-app/hosts/dylog-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dylog-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/dylog-app/vendors/dylog-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dylog-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dylog-app/security/dylog-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dylog-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dylog.app/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dylog.app/privacy
coverage:
  checked: '2026-11-06'
  detail: API reference page returns HTML with no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL specifications.
  evidence:
  - status: 200
    url: https://dylog.app/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: Dylog provides a unified index for meetings, files, and jobs, allowing users to search and organize information by job, name, or topic. The platform reads inputs from various sources, groups them, and presents searchable results, enabling efficient workflow management and collaboration across teams.
layout: provider
modified: '2026-11-06'
name: Dylog
nav: Providers
network: true
overview: Dylog is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Indexing, Collaboration, Search, and Workflows.
random_paper: 21
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dylog App Domain Security
  slug: dylog-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dylog-app
tags:
- Company
- Indexing
- Collaboration
- Search
- Workflows
website: https://dylog.app/
---
