---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.5
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nx.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://nx.dev
- group: docs
  title: ''
  type: Documentation
  url: https://nx.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://nx.dev/docs/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://nx.dev/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://nx.dev/community
- group: company
  title: ''
  type: Blog
  url: https://nx.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nrwl
- group: commercial
  title: ''
  type: Pricing
  url: https://nx.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.nx.app/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.nx.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloud.nx.app/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.nx.app/
- group: build
  title: ''
  type: Packages
  url: packages/nx-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/nx-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nx-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nx-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nx-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/nx-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nx-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://nx.dev/docs/reference/releases
- group: commercial
  title: ''
  type: Plans
  url: plans/nx-plans.yml
created: '2026-07-17'
description: Nx is an open-source, technology-agnostic monorepo build platform from Nrwl (backed by a16z) that speeds up builds and CI through computation caching, task orchestration, and running only the projects affected by a change. Its developer surface spans a local CLI (nx) with a large family of first-party @nx/* technology plugins and code generators, an official Model Context Protocol server (nx-mcp) and Nx Console editor integrations for AI-assisted development, and the hosted Nx Cloud service for remote caching, distributed task execution (Nx Agents), and self-healing CI. Nx is a build/CI tooling platform rather than a REST API provider — its integration surface is the nx CLI, the @nx/* npm packages, the MCP server, and Nx Cloud.
image: https://github.com/nrwl.png
layout: provider
mcp_servers:
- description: First-party Model Context Protocol server that gives AI coding assistants deep, graph-aware context about an Nx workspace — project dependencies, generators/plugins, live terminal output, and Nx Cloud
  name: Nx MCP Server (nx-mcp)
  slug: nx-mcp-server-nx-mcp
modified: '2026-07-20'
name: Nx
nav: Providers
network: true
overview: 'Nx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Build System, Monorepo, Developer Tools, and CI/CD.


  Nx''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
plans:
- name: Nx Plans
  plan_count: 3
  slug: nx-plans
random_paper: 20
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 38.7
  provenance:
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nx/refs/heads/main/screenshots/nx-2026-08-07T185818.png
security:
- kind: domain-security
  name: Nx Domain Security
  slug: nx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nx
tags:
- Company
- Build System
- Monorepo
- Developer Tools
- CI/CD
- Continuous Integration
- Caching
- Command Line Interface
- MCP
- JavaScript
- TypeScript
- DevOps
website: https://nx.dev
---
