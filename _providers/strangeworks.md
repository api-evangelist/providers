---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.5
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: The GraphQL API the Strangeworks Python SDK is built on. Exposes the workspace a user's API key belongs to, the compute backends available to it, and mutations for uploading workspace files, initiatin
  name: Strangeworks SDK GraphQL API
  slug: sdk
- description: The full Strangeworks platform GraphQL API covering user accounts, workspaces and members, invitations, billing accounts, credits and transactions, products and the product catalog, resources, jobs, f
  name: Strangeworks Platform GraphQL API
  slug: platform
- description: The product-side GraphQL API used by compute products published on the Strangeworks platform to register and update backends, create and update jobs, upload job files, store resource configuration, an
  name: Strangeworks Products GraphQL API
  slug: products
artifact_total: 7
asyncapis:
- description: ''
  name: Strangeworks Webhooks
  slug: strangeworks-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://strangeworks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.strangeworks.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.strangeworks.com/welcome/get-started
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.strangeworks.com/
- group: start
  title: ''
  type: SignUp
  url: https://portal.strangeworks.com/
- group: operate
  title: ''
  type: Support
  url: https://strangeworks.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://strangeworks.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://strangeworks.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/strangeworks
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/strangeworks-changelog.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/strangeworks-sdk.graphql
- group: build
  title: ''
  type: Packages
  url: packages/strangeworks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/strangeworks-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/strangeworks-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/strangeworks-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/strangeworks-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/strangeworks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/strangeworks-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/strangeworks-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/strangeworks-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/strangeworks-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/strangeworks-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/strangeworks-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/strangeworks-domain-security.yml
- group: other
  title: ''
  type: ContentSignal
  url: https://strangeworks.com/robots.txt
created: '2026-08-05'
description: Strangeworks is an Austin, Texas based optimization and quantum computing company founded in 2018 by whurley (William Hurley). It operates a "heterogeneous hybrid compute" platform that gives enterprises and governments managed access to quantum processors, quantum-inspired annealers and classical optimization solvers from a single API and Python SDK, alongside its Compute, Workflows, Decisions and HybridSolver products and an expert services practice. The platform is organized around workspaces, products, resources, jobs and backends, and is programmable through three public GraphQL endpoints (sdk, platform, products) at api.strangeworks.com plus a REST proxy that forwards calls to an activated resource. Compute partners reachable through the platform include IBM Quantum, Amazon Braket, Azure Quantum, IonQ, Rigetti, Quantinuum, QuEra, IQM, AQT, Pasqal, D-Wave, Toshiba, Hitachi, Fujitsu, NEC, Gurobi, JIJ, LightSolver and Quantagonia (acquired 2025).
image: https://strangeworks.com/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Strangeworks MCP Server
  slug: strangeworks-mcp-server
modified: '2026-08-05'
name: Strangeworks
nav: Providers
network: true
overview: 'Strangeworks publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Quantum Computing, Optimization, High Performance Computing, and Artificial Intelligence.


  The Strangeworks catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Strangeworks'' developer surface includes documentation, getting-started guide, signup flow, support, changelog, authentication, and 20 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 50.0
    developer_ergonomics: 56.5
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 42.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/strangeworks/refs/heads/main/screenshots/strangeworks-2026-08-17T082131.png
security:
- kind: authentication
  name: Strangeworks Authentication
  slug: strangeworks-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Strangeworks Domain Security
  slug: strangeworks-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: strangeworks
tags:
- Company
- Quantum Computing
- Optimization
- High Performance Computing
- Artificial Intelligence
- Developer Platform
- GraphQL
- Compute
- Scientific Computing
- Operations Research
website: https://strangeworks.com/
---
