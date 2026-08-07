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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://www.tessl.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tessl.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tessl.io/reference/cli-commands.md
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tessl.io/introduction-to-tessl/set-up-tessl
- group: company
  title: ''
  type: Blog
  url: https://tessl.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://tessl.io/pricing
- group: start
  title: ''
  type: Login
  url: https://tessl.io/login/
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/jbb2vHnHZQ
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tesslio
- group: operate
  title: ''
  type: StatusPage
  url: https://tesslstatus.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.tessl.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tessl-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tessl-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/tessl-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/tessl-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tessl-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tessl-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tessl-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/tessl-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tessl-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tessl-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tessl-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tessl-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tessl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://tessl.io/.well-known/security.txt
created: '2026-07-17'
description: 'Tessl is an agent-enablement platform that gives engineering teams a management layer for AI agent skills and plugins: continuously build, test, distribute, and optimize the context that coding agents rely on, with the security and governance of enterprise software. It centers on the Tessl Registry (3,000+ public skills plus private workspaces), the Tessl CLI, a first-party MCP server and workspace MCP gateway, Snyk-powered security scanning with install policies, and quality reviews and evaluations that can gate skills in CI. Skills and plugins are agent-agnostic, working across Claude Code, Cursor, Copilot, Gemini, and others. Founded by Guy Podjarny (Snyk); backed by Accel and GV.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tessl.png
layout: provider
mcp_servers:
- description: ''
  name: tessl-mcp.yml
  slug: tessl-mcpyml
modified: '2026-07-21'
name: Tessl
nav: Providers
network: true
overview: 'Tessl is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Agents, Agentic Development, and Developer Tools.


  Tessl''s developer surface includes documentation, getting-started guide, engineering blog, pricing, support, changelog, CLI, and 18 more developer resources.'
random_paper: 103
score:
  band: thin
  composite: 33.0
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 47.4
  previous_composite: 33.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Tessl Authentication
  slug: tessl-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Tessl Domain Security
  slug: tessl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tessl Vulnerability Disclosure
  slug: tessl-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Tessl Trust Center
  slug: tessl-trust-center
  summary_line: trust center published
slug: tessl
tags:
- Company
- Ai
- Agents
- Agentic Development
- Developer Tools
- Agent Skills
- MCP
- CLI
- Registry
- Code Review
website: https://www.tessl.io/
---
