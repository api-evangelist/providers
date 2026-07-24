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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 42.3
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The direct HTTP API behind the Atlas CLI — the research graph, Library, runs, evidence, compute, and research surfaces. Bearer (thk_*) auth; JSON responses; Idempotency-Key on writes. Base https://app
  name: Atlas REST API
  slug: atlas-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://syntheticsciences.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.syntheticsciences.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.syntheticsciences.ai/atlas
- group: docs
  title: ''
  type: APIReference
  url: https://docs.syntheticsciences.ai/atlas/commands
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.syntheticsciences.ai/atlas/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.syntheticsciences.ai/atlas/billing
- group: start
  title: ''
  type: SignUp
  url: https://app.syntheticsciences.ai
- group: operate
  title: ''
  type: Support
  url: mailto:team@syntheticsciences.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synthetic-sciences
- group: other
  title: ''
  type: ProductSite
  url: https://tryatlas.sh
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synthetic-sciences-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/synthetic-sciences-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/synthetic-sciences-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/synthetic-sciences-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/synthetic-sciences-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/synthetic-sciences-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/synthetic-sciences-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/synthetic-sciences-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/synthetic-sciences-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/synthetic-sciences-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/synthetic-sciences-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/synthetic-sciences-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synthetic-sciences-domain-security.yml
created: '2026-07-17'
description: 'Synthetic Sciences is a Y Combinator-backed AI research lab building foundation models for scientific discovery. Its flagship product, Atlas, is an agent-first research graph and infrastructure layer for autonomous science: durable typed nodes (hypotheses, experiment plans, recorded runs, evidence, decisions) linked into a shared, forkable map that humans and AI agents read and write directly over a REST API and the @synsci/atlas CLI. Atlas bundles a Library for indexing and grounded search over repos, docs, papers, and datasets, a cross-provider GPU compute marketplace, GEPA-based optimization and refereed autoresearch, and nine agent Skills. The lab also ships two open-source (Apache 2.0) projects: OpenScience, a model-agnostic AI workbench that runs the full research loop, and Delphi, a self-hosted MCP server that gives coding agents semantic context over code, papers, and HuggingFace datasets.'
image: https://app.syntheticsciences.ai/synsc-logo.png
layout: provider
mcp_servers:
- description: ''
  name: synthetic-sciences-mcp.yml
  slug: synthetic-sciences-mcpyml
modified: '2026-07-21'
name: Synthetic Sciences
nav: Providers
network: true
overview: 'Synthetic Sciences publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine Learning, Scientific Research, and Developer Tools.


  Synthetic Sciences'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, CLI, and 17 more developer resources.'
random_paper: 41
score:
  band: thin
  composite: 30.3
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 78.3
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Synthetic Sciences Authentication
  slug: synthetic-sciences-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Synthetic Sciences Domain Security
  slug: synthetic-sciences-domain-security
  summary_line: TLSv1.3 · HSTS
slug: synthetic-sciences
tags:
- Company
- Artificial Intelligence
- Machine Learning
- Scientific Research
- Developer Tools
- Agents
- Foundation Models
- Knowledge Graph
- Model Context Protocol
- CLI
- Research Infrastructure
website: https://syntheticsciences.ai
---
