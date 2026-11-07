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
  score: 8.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Atomic CSS 프레임워크를 소개합니다. 설계 철학, 특징, 동작 방식을 설명합니다.
  name: Atomic CSS API
  slug: atomic-css-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/atomiccss-dev/mcp/atomiccss-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/atomiccss-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/atomiccss-dev/hosts/atomiccss-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/atomiccss-dev-hosts.yml
- group: build
  href: https://artifacts.apis.io/atomiccss-dev/packages/atomiccss-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/atomiccss-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/atomiccss-dev/packages/atomiccss-dev-packages.yml
  title: ''
  type: Packages
  url: packages/atomiccss-dev-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://atomiccss.dev/playground
- group: auth
  href: https://artifacts.apis.io/atomiccss-dev/security/atomiccss-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/atomiccss-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://atomiccss.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atomiccss.dev/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://atomiccss.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://atomiccss.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://atomiccss.dev/en/docs/introduction
- group: operate
  title: ''
  type: Support
  url: https://atomiccss.dev/support/
- group: company
  title: ''
  type: Blog
  url: https://atomiccss.dev/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nicecss-com
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are HTML only and no machine‑readable OpenAPI/GraphQL/AsyncAPI spec was found.
  evidence:
  - status: 200
    url: https://atomiccss.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Atomic CSS is a utility‑first CSS framework that lets you combine the first letters of CSS properties into concise class names, enabling you to style any element instantly. It works without any configuration or build step – just write classes and see results immediately. The framework emphasizes a minimal, class‑only approach, turning CSS property names into short, memorable utilities for rapid development.
image: https://atomiccss.dev/favicon.ico
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.atomiccss.dev.
  name: Atomic CSS MCP Server
  slug: atomiccss-dev-mcp-yml
modified: '2026-11-01'
name: Atomic CSS
nav: Providers
network: true
overview: 'Atomic CSS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CSS, utility-first, Framework, atomic, and Open Source.


  Atomic CSS''s developer surface includes sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 8 more developer resources.'
plans:
- name: Atomiccss Dev Plans Pricing
  plan_count: 0
  slug: atomiccss-dev-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Atomiccss Dev Rate Limits
  slug: atomiccss-dev-rate-limits
scopes:
- name: Atomiccss Dev Scopes
  scope_count: 0
  slug: atomiccss-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 13.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 19.1
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Atomiccss Dev Authentication
  slug: atomiccss-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Atomiccss Dev Domain Security
  slug: atomiccss-dev-domain-security
  summary_line: TLSv1.3
slug: atomiccss-dev
tags:
- CSS
- utility-first
- Framework
- atomic
- Open Source
website: https://atomiccss.dev/
---
