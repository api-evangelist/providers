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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.2
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: Rescale's token-authenticated REST API (v2) for creating, submitting, monitoring and managing simulation jobs, uploading and downloading files, listing available software (analyses) and hardware (core
  name: Rescale REST API
  slug: rescale-rest-api
- description: Rescale's high-throughput computing (HTC) REST API for batch container workloads, organized around projects, tasks, job batches and a container registry, with bearer/JWT token authentication managed v
  name: Rescale HTC API
  slug: rescale-htc-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rescale-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rescale.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://rescale.com/documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://rescale.com/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://engineering.rescale.com/api-docs/
- group: company
  title: ''
  type: Blog
  url: https://rescale.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://rescale.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://rescale.com/rescale-signup/
- group: start
  title: ''
  type: Login
  url: https://rescale.com/rescale-login/
- group: operate
  title: ''
  type: Support
  url: https://rescale.com/rescale-support-request/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rescale.com/company/legal/customer-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rescale.com/company/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rescale-labs
- group: agent
  title: ''
  type: MCPServer
  url: mcp/rescale-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/rescale-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/rescale-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/rescale-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rescale-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rescale-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rescale-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rescale-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://rescale.com/platform/security-compliance/
- group: design
  title: ''
  type: DataModel
  url: data-model/rescale-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rescale-llms.txt
created: '2026-07-17'
description: Rescale is a high-performance computing (HPC) and simulation platform that gives R&D and engineering teams a unified, cloud-based environment to run modeling, simulation, and AI-physics workloads across CPU and GPU infrastructure. Engineers submit and orchestrate jobs against hundreds of packaged engineering applications (Ansys, STAR-CCM+, Abaqus, COMSOL, OpenFOAM and more), manage data and results, and increasingly automate workflows with agentic tooling. Rescale exposes a token-authenticated REST API (v2), a high-throughput computing (HTC) API with Python and Go clients, a first-party CLI, and a hosted Model Context Protocol (MCP) server so agents and automation can create, submit, monitor, and manage simulation jobs, files, workstations, and clusters programmatically. The platform is FedRAMP-authorized, SOC 2 Type II, ISO 27001, ITAR-registered, and FIPS-aligned for aerospace, automotive, energy, life-sciences and defense engineering teams.
image: https://rescale.com/wp-content/uploads/LinkedIn-Header-Employee.png
layout: provider
mcp_servers:
- description: Rescale hosts an official remote MCP server over HTTP, letting any MCP-compatible client (Claude Code, Claude Desktop, Cursor, VS Code Copilot, Windsurf, Gemini CLI) drive the Rescale platform in natu
  name: Rescale MCP Server
  slug: rescale-mcp-server
modified: '2026-07-20'
name: Rescale
nav: Providers
network: true
overview: 'Rescale publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, High Performance Computing, Simulation, Cloud, and Engineering.


  Rescale''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, support, CLI, and 17 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 32.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rescale/refs/heads/main/screenshots/rescale-2026-09-02T153521.png
security:
- kind: authentication
  name: Rescale Authentication
  slug: rescale-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Rescale Domain Security
  slug: rescale-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: rescale
tags:
- Company
- High Performance Computing
- Simulation
- Cloud
- Engineering
- CAE
- HPC
- AI Physics
- Job
- Compute
website: https://rescale.com
---
