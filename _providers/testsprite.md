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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://testsprite.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.testsprite.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.testsprite.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.testsprite.com/cli/reference/command-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.testsprite.com/mcp/getting-started/overview
- group: start
  title: ''
  type: Quickstart
  url: https://docs.testsprite.com/cli/getting-started/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TestSprite
- group: company
  title: ''
  type: Blog
  url: https://www.testsprite.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.testsprite.com/changelog
- group: operate
  title: ''
  type: Roadmap
  url: https://docs.testsprite.com/cli/reference/whats-included
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/QQB9tJ973e
- group: commercial
  title: ''
  type: Pricing
  url: https://www.testsprite.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.testsprite.com/auth/cognito/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.testsprite.com/auth/cognito/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.testsprite.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.testsprite.com/privacy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/testsprite-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/testsprite-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/testsprite-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/testsprite-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/testsprite-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/testsprite-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/testsprite-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/testsprite-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/testsprite-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/testsprite-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/testsprite-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/testsprite-llms.txt
created: '2026-07-17'
description: 'TestSprite is an AI-powered software testing platform (a Techstars-backed company) that gives autonomous coding agents a verification loop: it uses an app like a real user, generates and executes end-to-end UI and backend API tests, and returns actionable failure bundles (screenshots, DOM snapshots, root causes, and fix suggestions) so an agent can repair its own work before bugs ship. It is delivered as an official Model Context Protocol (MCP) server that runs inside AI coding assistants (Cursor, Claude Code, VS Code, Copilot), a first-party command-line interface for terminal and CI/CD use, a browser Web Portal, and a GitHub App that tests every pull request. Authentication is by scoped API key.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/testsprite.png
layout: provider
mcp_servers:
- description: ''
  name: testsprite-mcp.yml
  slug: testsprite-mcpyml
modified: '2026-07-21'
name: TestSprite
nav: Providers
network: true
overview: 'TestSprite is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software Testing, API Testing, Test Automation, and AI.


  TestSprite''s developer surface includes documentation, API reference, getting-started guide, quickstart, engineering blog, changelog, support, and 22 more developer resources.'
random_paper: 58
scopes:
- name: Testsprite Scopes
  scope_count: 5
  slug: testsprite-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 33.4
  delta: -0.5
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 68.5
    governance: 3.1
    operational_transparency: 26.3
  previous_composite: 33.9
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Testsprite Authentication
  slug: testsprite-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Testsprite Domain Security
  slug: testsprite-domain-security
  summary_line: TLSv1.3 · DMARC
slug: testsprite
tags:
- Company
- Software Testing
- API Testing
- Test Automation
- AI
- Developer Tools
- Model Context Protocol
- Quality Assurance
- CI/CD
- Agentic
website: https://testsprite.com/
---
