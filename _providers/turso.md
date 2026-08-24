---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 24
  human_in_the_loop: 2
  name: Turso Agentic Access
  operation_count: 49
  slug: turso-agentic-access
  summary_line: 49 operations · 24 acting · 2 human-in-the-loop
api_count: 6
apis:
- description: 'HTTP API for executing SQL statements directly against a Turso database instance at the edge. Supports query execution via the /v2/pipeline endpoint, health checks, server version retrieval, database '
  name: Turso SQL over HTTP API
  slug: http-database-api
- description: Model Context Protocol (MCP) server that exposes Turso databases, filesystem operations, and key-value storage to AI assistants such as Claude Desktop, Cursor, and Windsurf. Enables AI agents to disco
  name: Turso AgentFS MCP Server
  slug: agentfs-mcp
- description: The Auth API from Turso — 3 operation(s) for auth.
  name: Turso Auth API
  slug: turso-auth-api
- description: The Locations API from Turso — 1 operation(s) for locations.
  name: Turso Locations API
  slug: turso-locations-api
- description: The Organizations API from Turso — 31 operation(s) for organizations.
  name: Turso Organizations API
  slug: turso-organizations-api
- description: The User API from Turso — 1 operation(s) for user.
  name: Turso User API
  slug: turso-user-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Turso Platform Auth API
  slug: open-turso-auth-api
- collection_type: open
  name: Turso Platform Auth Locations API
  slug: open-turso-locations-api
- collection_type: open
  name: Turso Platform Auth Organizations API
  slug: open-turso-organizations-api
- collection_type: open
  name: Turso Platform Auth User API
  slug: open-turso-user-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/turso-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/turso-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turso-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/turso-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://turso.tech
- group: docs
  title: ''
  type: Documentation
  url: https://docs.turso.tech
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tursodatabase
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/turso
- group: other
  title: ''
  type: X
  url: https://x.com/tursodatabase
- group: company
  title: ''
  type: Blog
  url: https://turso.tech/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://turso.tech/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.turso.tech
- group: build
  title: ''
  type: SDKs
  url: https://docs.turso.tech/sdk/introduction
- group: build
  title: ''
  type: CLI
  url: https://github.com/tursodatabase/turso-cli
- group: commercial
  title: ''
  type: Plans
  url: plans/turso-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/turso-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/turso-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/turso-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/turso-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/
created: '2026-06-12'
description: Turso is an edge database platform built on libSQL, a fork of SQLite, offering both an embedded in-process database engine and a managed cloud service (Turso Cloud) for deploying millions of SQLite databases at the edge. Developers can programmatically manage databases, groups, organizations, and authentication tokens via the Turso Platform API, and execute SQL queries directly over HTTP using the libSQL HTTP API. Turso targets multi-tenant SaaS, AI agent architectures, and edge/serverless workloads where per-user or per-agent database isolation is required. The platform provides official SDKs for TypeScript, Go, Python, and mobile (iOS/Android), a CLI tool, and an MCP server integration for AI assistant access.
examples:
- key_count: 3
  name: Turso Create Database Example
  slug: turso-create-database-example
- key_count: 3
  name: Turso Create Database Token Example
  slug: turso-create-database-token-example
- key_count: 3
  name: Turso List Databases Example
  slug: turso-list-databases-example
finops:
- name: Turso Finops
  service_category: Database
  slug: turso-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turso.png
json_schemas:
- name: APIToken
  property_count: 6
  slug: turso-api-token
- name: Database
  property_count: 10
  slug: turso-database
- name: Group
  property_count: 6
  slug: turso-group
- name: Organization
  property_count: 10
  slug: turso-organization
jsonld:
- class_count: 0
  name: Turso Context
  property_count: 30
  slug: turso-context
layout: provider
modified: '2026-06-12'
name: Turso
nav: Providers
network: true
overview: 'Turso publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Locations API, Organizations API, and 1 more. Tagged areas include Database, Edge Computing, SQLite, Developer Tools, and Multi-Tenant.


  The Turso catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Turso''s developer surface includes authentication, documentation, engineering blog, pricing, CLI, code examples, and 15 more developer resources.'
plans:
- name: Turso Plans Pricing
  plan_count: 5
  slug: turso-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 11
  name: Turso Rate Limits
  slug: turso-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Turso API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: turso-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.2
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 25.0
    contract_quality: 58.7
    developer_ergonomics: 38.1
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 34.2
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/turso/refs/heads/main/screenshots/turso-2026-06-20T195837.png
security:
- kind: authentication
  name: Turso Authentication
  slug: turso-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Turso Domain Security
  slug: turso-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Turso Vulnerability Disclosure
  slug: turso-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: turso
tags:
- Database
- Edge Computing
- SQLite
- Developer Tools
- Multi-Tenant
- AI Agents
website: https://turso.tech
---
