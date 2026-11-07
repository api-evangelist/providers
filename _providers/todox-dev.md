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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for todox platform
  name: todox API
  slug: todox-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/todox-dev/llms/todox-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/todox-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/todox-dev/hosts/todox-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/todox-dev-hosts.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://todox.dev/privacy
- group: company
  title: ''
  type: Blog
  url: https://todox.dev/blog
- group: auth
  href: https://artifacts.apis.io/todox-dev/security/todox-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/todox-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://todox.dev/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://todox.dev/api/mcp
  - status: 401
    url: https://www.todox.dev/api/mcp
  - status: 200
    url: https://todox.dev/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: todox is a working‑memory platform for developers and their AI agents. It records project decisions, task logs, and context notes, enabling seamless hand‑offs between humans and machines. Built on an open‑source stack, todox offers a web UI, API, and MCP server for integration, emphasizing privacy, no third‑party tracking, and easy export of data.
image: https://todox.dev/favicon.ico
layout: provider
modified: '2026-10-31'
name: todox-dev
nav: Providers
network: true
overview: 'todox-dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Developer Tools, Artificial Intelligence, Productivity, Open Source, and Privacy.


  todox-dev''s developer surface includes engineering blog and 5 more developer resources.'
plans:
- name: Todox Dev Plans Pricing
  plan_count: 0
  slug: todox-dev-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Todox Dev Rate Limits
  slug: todox-dev-rate-limits
scopes:
- name: Todox Dev Scopes
  scope_count: 0
  slug: todox-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 8.8
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/todox-dev/todox-dev-2026-11-03T144831.png
security:
- kind: authentication
  name: Todox Dev Authentication
  slug: todox-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Todox Dev Domain Security
  slug: todox-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: todox-dev
tags:
- Developer Tools
- Artificial Intelligence
- Productivity
- Open Source
- Privacy
website: https://todox.dev/
---
