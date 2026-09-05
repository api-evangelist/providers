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
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The Specific control plane and CLI that builds, deploys and runs agent-defined infrastructure from a single specific.hcl file, spanning local development and production on Specific Cloud.
  name: Specific Platform
  slug: specific-platform
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://specific.dev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.specific.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.specific.dev
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.specific.dev/quickstart
- group: company
  title: ''
  type: Blog
  url: https://specific.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://specific.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.specific.dev
- group: start
  title: ''
  type: Login
  url: https://dashboard.specific.dev
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/specific-dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://specific.dev/changelog
- group: build
  title: ''
  type: Packages
  url: packages/specific-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/specific-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/specific-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/specific-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/specific-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/specific-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/specific-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/specific-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/specific-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/specific-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/specific-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Specific is an infrastructure-as-code platform built for coding agents, positioned as "AWS for coding agents." Any coding agent (Claude Code, Cursor, Codex) defines its whole system in a single specific.hcl file — services, managed Postgres, S3-compatible object storage, Redis, real-time Postgres sync (powered by Electric), Temporal workflows, crons, secrets, volumes, custom domains, preview environments and environments — then runs it locally with `specific dev` and ships it to production with `specific deploy`. Everything is reached through the Specific CLI and a hosted docs MCP server rather than proprietary SDKs, so agents can build backends from natural-language prompts and deploy production infrastructure in minutes.
image: https://specific.dev/opengraph-image?2b9073564a4e0222
layout: provider
mcp_servers:
- description: Official hosted MCP server that lets coding agents search and read the Specific documentation directly. Install commands are published for Claude Code, Cursor, Codex, and VS Code.
  name: Specific MCP Server
  slug: specific-mcp-server
modified: '2026-07-21'
name: Specific
nav: Providers
network: true
overview: 'Specific publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Infrastructure as Code, Platform-as-a-Service, and Backend-as-a-Service.


  Specific''s developer surface includes documentation, getting-started guide, engineering blog, pricing, signup flow, changelog, CLI, and 15 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 25.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 66.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 25.4
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/specific/refs/heads/main/screenshots/specific-2026-09-02T160346.png
security:
- kind: authentication
  name: Specific Authentication
  slug: specific-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Specific Domain Security
  slug: specific-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: specific
tags:
- Company
- Infrastructure
- Infrastructure as Code
- Platform-as-a-Service
- Backend-as-a-Service
- Coding Agents
- Deployment
- PostgreSQL
- Developer Tools
- Cloud
- CLI
- MCP
website: https://specific.dev
---
