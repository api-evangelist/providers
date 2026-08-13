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
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-12'
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
- description: ''
  name: rescale-mcp.yml
  slug: rescale-mcpyml
modified: '2026-07-20'
name: Rescale
nav: Providers
network: true
overview: 'Rescale publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, High Performance Computing, Simulation, Cloud, and Engineering.


  Rescale''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, support, CLI, and 17 more developer resources.'
random_paper: 15
score:
  band: thin
  composite: 32.9
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 63.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 32.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
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
- Jobs
- Compute
website: https://rescale.com
---
