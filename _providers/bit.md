---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.6
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Bit is API-first: every aspect exposes a programmatic API that also composes into a GraphQL API used by the CLI, web UI, and Bit Cloud. The hosted GraphQL endpoint is served from api.v2.bit.cloud/grap'
  name: Bit Cloud GraphQL API
  slug: bit-cloud-graphql-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://bit.cloud/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bit.dev/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://bit.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://bit.dev/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://bit.dev/docs/getting-started/installing-bit/installing-bit/
- group: start
  title: ''
  type: Quickstart
  url: https://bit.dev/docs/quick-start/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/teambit
- group: company
  title: ''
  type: Blog
  url: https://bit.cloud/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bit.cloud/pricing
- group: start
  title: ''
  type: Login
  url: https://bit.cloud/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bit.cloud/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bit.cloud/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bit.cloud
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/teambit/bit/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bit-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/bit-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bit-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/bit-cli.md
- group: build
  title: ''
  type: Packages
  url: packages/bit-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bit-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bit-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bit-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bit-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bit-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bit-llms.txt
created: '2026-07-17'
description: 'Bit (teambit) is the platform for the modular web — a build system and cloud for component-driven development. Bit lets teams create, version, and share reusable components as standard npm packages across projects and frameworks (React, Vue, Angular, Node.js, Next.js and more), with independent build, test, and CI/CD per component. Every Bit feature is API-first: an aspect-based programmatic API plus a GraphQL API power the CLI, the web UI, and Bit Cloud. Bit ships a built-in Model Context Protocol (MCP) server and a published Claude Agent Skill so AI agents can intelligently create and reuse components without duplication. Backed by Insight Partners.'
image: https://avatars.githubusercontent.com/u/24789812?v=4
layout: provider
mcp_servers:
- description: Bit ships a built-in Model Context Protocol server as part of the Bit CLI, enabling AI agents (Cursor, GitHub Copilot, Claude Code, Windsurf) to create and reuse components, inspect component/workspac
  name: Bit MCP Server
  slug: bit-mcp-server
modified: '2026-07-18'
name: Bit
nav: Providers
network: true
overview: 'Bit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DevOps, Component Development, Frontend, and Monorepo.


  Bit''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, pricing, changelog, and 18 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 66.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 28.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bit/refs/heads/main/screenshots/bit-2026-07-25T203125.png
security:
- kind: authentication
  name: Bit Authentication
  slug: bit-authentication
  summary_line: token/oauth-browser-login · 2 schemes
- kind: domain-security
  name: Bit Domain Security
  slug: bit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bit
tags:
- Company
- DevOps
- Component Development
- Frontend
- Monorepo
- npm
- GraphQL
- CLI
- MCP
- Developer Tools
- AI Agents
website: https://bit.cloud/
---
