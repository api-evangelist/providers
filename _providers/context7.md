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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Context7 Agentic Access
  operation_count: 11
  slug: context7-agentic-access
  summary_line: 11 operations · 8 acting
api_count: 7
apis:
- description: The Context7 MCP Server implements the Model Context Protocol so AI coding assistants such as Cursor, Claude, and Windsurf can call Context7 tools directly from a developer's editor. It exposes resolv
  name: Context7 MCP Server
  slug: mcp-server
- description: The Context7 CLI (ctx7) is a command-line tool for querying the Context7 index from the terminal. It provides ctx7 library for searching the catalog by library name and ctx7 docs for retrieving docume
  name: Context7 CLI
  slug: cli
- description: The Add API from Context7 — 6 operation(s) for add.
  name: Context7 Add API
  slug: context7-add-api
- description: The Context API from Context7 — 1 operation(s) for context.
  name: Context7 Context API
  slug: context7-context-api
- description: The Libs API from Context7 — 1 operation(s) for libs.
  name: Context7 Libs API
  slug: context7-libs-api
- description: The Policies API from Context7 — 1 operation(s) for policies.
  name: Context7 Policies API
  slug: context7-policies-api
- description: The Refresh API from Context7 — 1 operation(s) for refresh.
  name: Context7 Refresh API
  slug: context7-refresh-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Context7 REST Add API
  slug: open-context7-add-api
- collection_type: open
  name: Context7 REST Add Context API
  slug: open-context7-context-api
- collection_type: open
  name: Context7 REST Add Libs API
  slug: open-context7-libs-api
- collection_type: open
  name: Context7 REST Add Policies API
  slug: open-context7-policies-api
- collection_type: open
  name: Context7 REST Add Refresh API
  slug: open-context7-refresh-api
- collection_type: open
  name: Context7 REST API
  slug: open-context7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/upstash/context7/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/upstash/context7/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/upstash/context7/blob/master/SECURITY.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/upstash/context7/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/context7-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/context7-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/context7-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/context7-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://context7.com/
- group: docs
  title: ''
  type: Documentation
  url: https://context7.com/docs
- group: other
  title: ''
  type: Dashboard
  url: https://context7.com/dashboard
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upstash
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/upstash/context7
- group: commercial
  title: ''
  type: Pricing
  url: https://context7.com/pricing
created: '2026-03-16'
description: Context7 is an Upstash service providing up-to-date, version-specific documentation and code examples for libraries and frameworks, exposed as both a REST API and a Model Context Protocol (MCP) server so AI coding assistants can fetch authoritative reference material at prompt time.
finops:
- name: Context7 Finops
  service_category: API
  slug: context7-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/context7.png
layout: provider
modified: '2026-05-19'
name: Context7
nav: Providers
network: true
overview: 'Context7 publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Add API, Context API, Libs API, and 2 more. Tagged areas include Artificial Intelligence, Context, Documentation, LLM, and MCP.


  Context7''s developer surface includes authentication, documentation, pricing, and 11 more developer resources.'
plans:
- name: Context7 Plans Pricing
  plan_count: 3
  slug: context7-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Context7 Rate Limits
  slug: context7-rate-limits
score:
  band: thin
  composite: 31.3
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 47.6
    developer_ergonomics: 21.4
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/context7/refs/heads/main/screenshots/context7-2026-06-20T174932.png
security:
- kind: authentication
  name: Context7 Authentication
  slug: context7-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Context7 Domain Security
  slug: context7-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Context7 Vulnerability Disclosure
  slug: context7-vulnerability-disclosure
  summary_line: disclosure policy published
slug: context7
tags:
- Artificial Intelligence
- Context
- Documentation
- LLM
- MCP
website: https://context7.com/
---
