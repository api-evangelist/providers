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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: TableThis provides an MCP‑based API for AI agents to read, write, and manage tables and documents. The API is accessed via the MCP endpoint and documented at the developer docs page.
  name: TableThis API
  slug: tablethis-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/tablethis-ai/mcp/tablethis-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tablethis-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tablethis-ai/well-known/tablethis-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tablethis-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/tablethis-ai/hosts/tablethis-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tablethis-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/tablethis-ai/vendors/tablethis-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tablethis-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.tablethis.ai/users/log-in
- group: auth
  href: https://artifacts.apis.io/tablethis-ai/security/tablethis-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tablethis-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tablethis.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tablethis.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.tablethis.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://www.tablethis.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tablethis.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tablethis.ai/privacy
coverage:
  checked: '2026-10-31'
  detail: Docs provide MCP endpoint but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.tablethis.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: TableThis provides a shared database platform for AI‑built internal applications, offering typed tables and Markdown documentation that teams can collaborate on. It enables developers to connect large language models like Claude or Codex to a central data store, allowing AI assistants to read, write, and update information with version history and access controls. The service is free to start with 100 MB of storage and no credit card required, targeting teams that want to build internal tools powered by AI without managing infrastructure.
image: https://www.tablethis.ai/images/logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at www.tablethis.ai.
  name: tablethis-ai MCP Server
  slug: tablethis-ai-mcp-yml
modified: '2026-10-31'
name: tablethis-ai
nav: Providers
network: true
overview: 'tablethis-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Database, Collaboration, Internal Apps, and Low-code.


  tablethis-ai''s developer surface includes documentation, API reference, engineering blog, and 9 more developer resources.'
plans:
- name: Tablethis Ai Plans Pricing
  plan_count: 0
  slug: tablethis-ai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Tablethis Ai Rate Limits
  slug: tablethis-ai-rate-limits
scopes:
- name: Tablethis Ai Scopes
  scope_count: 0
  slug: tablethis-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 65.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tablethis Ai Authentication
  slug: tablethis-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tablethis Ai Domain Security
  slug: tablethis-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tablethis-ai
tags:
- AI
- Database
- Collaboration
- Internal Apps
- Low-code
website: https://tablethis.ai/
---
