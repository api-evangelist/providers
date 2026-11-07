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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Explore the comprehensive documentation for Ardoq developers. Learn how to use the Ardoq API and integrate with your systems.
  name: Ardoq API
  slug: ardoq-api
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/ardoq/well-known/ardoq-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ardoq-status-security.txt
- group: design
  href: https://artifacts.apis.io/ardoq/lifecycle/ardoq-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ardoq-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/ardoq/llms/ardoq-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ardoq-llms.txt
- group: agent
  href: https://artifacts.apis.io/ardoq/mcp/ardoq-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ardoq-mcp.yml
- group: auth
  href: https://artifacts.apis.io/ardoq/well-known/ardoq-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/ardoq-help-security.txt
- group: agent
  href: https://artifacts.apis.io/ardoq/well-known/ardoq-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ardoq-well-known.yml
- group: other
  href: https://artifacts.apis.io/ardoq/hosts/ardoq-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ardoq-hosts.yml
- group: other
  href: https://artifacts.apis.io/ardoq/vendors/ardoq-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ardoq-vendors.yml
- group: build
  href: https://artifacts.apis.io/ardoq/packages/ardoq-packages.yml
  title: ''
  type: SDKs
  url: packages/ardoq-packages.yml
- group: build
  href: https://artifacts.apis.io/ardoq/packages/ardoq-packages.yml
  title: ''
  type: Packages
  url: packages/ardoq-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ardoq.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.ardoq.com/en/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ardoq.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ardoq.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ardoq.com/plans
- group: company
  title: ''
  type: Newsroom
  url: https://www.ardoq.com/news
- group: company
  title: ''
  type: Blog
  url: https://www.ardoq.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.ardoq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.ardoq.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ardoq
- group: auth
  href: https://artifacts.apis.io/ardoq/security/ardoq-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ardoq-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ardoq.com
coverage:
  checked: '2026-11-02'
  detail: Developer documentation is publicly accessible but no OpenAPI, GraphQL, AsyncAPI, or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://developer.ardoq.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Ardoq provides an intelligent enterprise architecture platform that streamlines IT portfolios, reduces technical debt, and manages risk through real-time insights and AI-enhanced modeling. The platform enables dynamic, data-driven architecture, integrates with numerous tools via APIs, and supports collaboration across people, processes, and technology.
image: https://www.ardoq.com/hubfs/00_Visuals%20(covers%2c%20logos%2c%20illustrations%2c%20etc)/Logos/Ardoq/RGB_Ardoq_Logo_Primary_Purple.svg
layout: provider
mcp_servers:
- description: Remote MCP server at api.ardoq.com.
  name: Ardoq MCP Server
  slug: ardoq-mcp-yml
modified: '2026-11-01'
name: Ardoq
nav: Providers
network: true
overview: 'Ardoq is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Enterprise Architecture, Software-as-a-Service, Platform, and Integration.


  Ardoq''s developer surface includes support, pricing, engineering blog, getting-started guide, documentation, and 17 more developer resources.'
plans:
- name: Ardoq Plans Pricing
  plan_count: 0
  slug: ardoq-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Ardoq Rate Limits
  slug: ardoq-rate-limits
scopes:
- name: Ardoq Scopes
  scope_count: 0
  slug: ardoq-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 49.2
    operational_transparency: 21.1
  previous_composite: 25.5
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ardoq Authentication
  slug: ardoq-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ardoq Domain Security
  slug: ardoq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ardoq
tags:
- Enterprise Architecture
- Software-as-a-Service
- Platform
- Integration
website: https://www.ardoq.com
---
