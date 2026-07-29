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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The Moderne Platform GraphQL API for programmatically executing OpenRewrite recipes across organizations of repositories, polling recipe-run state, retrieving results and recipe data tables, and commi
  name: Moderne GraphQL API
  slug: moderne-graphql-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://moderne.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.moderne.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.moderne.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.moderne.io/user-documentation/moderne-platform/references/graphql-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.moderne.io/user-documentation/moderne-platform/getting-started/running-your-first-recipe
- group: auth
  title: ''
  type: Authentication
  url: authentication/moderne-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://moderne.io/blog
- group: operate
  title: ''
  type: Support
  url: https://moderne.io/contact-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/moderneinc
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moderne.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moderne.io/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.moderne.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/moderne-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moderne-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moderne-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/moderne-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/moderne-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/moderne-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/moderne-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/moderne-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/moderne-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/moderne-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/moderne-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/moderne-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moderne-domain-security.yml
created: '2026-07-17'
description: Moderne is a deterministic, large-scale code transformation and mass-remediation platform built on the open-source OpenRewrite framework and its Lossless Semantic Trees (LST) — compiler-accurate, format-preserving models of source code. Moderne sequences codebases (from one repository to 100,000) into type-attributed LSTs and runs 10,000+ deterministic recipes across 40+ domains and 10+ languages to drive automated refactoring, framework and dependency migrations, security patching, and code governance with verifiable, regression-free results. The platform exposes a GraphQL API for recipe execution and commits, a first-party CLI (mod), local and hosted Model Context Protocol (MCP) servers plus bundled Agent Skills for AI coding agents, and Moddy, a multi-repo AI agent. Delivered as the Moderne Platform (SaaS) and Moderne DX (air-gapped, on-premises). Backed by True Ventures.
image: https://moderne.io/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: moderne-mcp.yml
  slug: moderne-mcpyml
modified: '2026-07-20'
name: Moderne
nav: Providers
network: true
overview: 'Moderne publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer Tools, Code Transformation, Automated Refactoring, and Code Migration.


  Moderne''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, signup flow, and 19 more developer resources.'
random_paper: 26
score:
  band: thin
  composite: 38.5
  delta: 1.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 0.0
    developer_ergonomics: 80.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 28.9
  previous_composite: 37.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Moderne Authentication
  slug: moderne-authentication
  summary_line: http/oauth2/openIdConnect/saml · 2 schemes
- kind: domain-security
  name: Moderne Domain Security
  slug: moderne-domain-security
  summary_line: TLSv1.3 · DMARC
slug: moderne
tags:
- Company
- Developer Tools
- Code Transformation
- Automated Refactoring
- Code Migration
- Security Patching
- OpenRewrite
- Static Analysis
- Code Governance
- DevOps
- GraphQL
- AI Agents
- MCP
website: https://moderne.ai/
---
