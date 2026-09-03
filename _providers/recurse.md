---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.recurse.ml/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.recurse.ml/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.recurse.ml/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.recurse.ml/docs/rml/getting-started/installing-on-macos
- group: build
  title: ''
  type: CLI
  url: cli/recurse-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/recurse-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/recurse-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/recurse-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recurse-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Recurse-ML
- group: company
  title: ''
  type: Blog
  url: https://recurse-ml.notion.site
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/qEjHQk64Z9
- group: commercial
  title: ''
  type: Pricing
  url: https://www.recurse.ml/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://github.com/marketplace/recurse-ml
created: '2026-07-17'
description: Recurse ML is an AI-powered code review platform built for modern development workflows that lean on AI coding assistants like Cursor, Claude Code, and GitHub Copilot. It understands a whole codebase's context to catch subtle bugs, breaking changes, library/API misuse, and SQL query issues that tests and static analyzers miss, and returns actionable feedback with one-click fixes. Recurse ships as a GitHub App that reviews pull requests, an rml CLI for local and CI/CD review, and ReMCP, a Model Context Protocol server that turns Recurse into a self-healing quality gate AI agents call to fix their own mistakes. It advertises a zero data retention policy and is pursuing SOC 2 compliance.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recurse.png
layout: provider
mcp_servers:
- description: ReMCP is Recurse ML's Model Context Protocol server. Installed as a local stdio server (remcp serve), it lets AI coding assistants (Claude Code, Cursor) run Recurse's AI code review on their own chang
  name: Recurse MCP Server
  slug: recurse-mcp-server
modified: '2026-07-21'
name: Recurse
nav: Providers
network: true
overview: 'Recurse is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Code Review, Code Review, Developer Tools, and CLI.


  Recurse''s developer surface includes documentation, getting-started guide, CLI, engineering blog, support, pricing, signup flow, and 7 more developer resources.'
random_paper: 5
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.3
  provenance:
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recurse/refs/heads/main/screenshots/recurse-2026-09-02T153059.png
security:
- kind: domain-security
  name: Recurse Domain Security
  slug: recurse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: recurse
tags:
- Company
- AI Code Review
- Code Review
- Developer Tools
- CLI
- MCP
- AI Agents
- Static Analysis
- Bug Detection
- Code Quality
website: https://www.recurse.ml/
---
