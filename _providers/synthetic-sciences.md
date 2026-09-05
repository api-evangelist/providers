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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.5
  scored_at: '2026-09-04'
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
  name: Synthetic Sciences MCP Server
  slug: synthetic-sciences-mcp-server
modified: '2026-07-21'
name: Synthetic Sciences
nav: Providers
network: true
overview: 'Synthetic Sciences publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Scientific Research, and Developer Tools.


  Synthetic Sciences'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, CLI, and 17 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 16.9
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/synthetic-sciences/refs/heads/main/screenshots/synthetic-sciences-2026-09-02T161636.png
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
- Machine-Learning
- Scientific Research
- Developer Tools
- Agents
- Foundation Models
- Knowledge Graph
- MCP
- CLI
- Research Infrastructure
website: https://syntheticsciences.ai
---
