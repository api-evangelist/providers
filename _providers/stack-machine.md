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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.5
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Single GraphQL endpoint for deploying and managing StackMachine apps, custom domains and DNS, managed databases and volumes, cron jobs, secrets, transactional email, cloud storage, package publishing,
  name: StackMachine GraphQL API
  slug: stackmachine-graphql-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stack-machine-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.stackmachine.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stackmachine.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.stackmachine.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.stackmachine.com/getting-started/installation
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/stackmachine
- group: operate
  title: ''
  type: Support
  url: https://github.com/stackmachine/sdks/issues
- group: commercial
  title: ''
  type: Pricing
  url: https://stackmachine.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.stackmachine.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.stackmachine.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://stackmachine.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://stackmachine.com/privacy
- group: docs
  title: ''
  type: GraphQL
  url: graphql/stack-machine-schema.graphql
- group: build
  title: ''
  type: Packages
  url: packages/stack-machine-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/stack-machine-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/stack-machine-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/stack-machine-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/stack-machine-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/stack-machine-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/stack-machine-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/stack-machine-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/stack-machine-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/stack-machine-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/stack-machine-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/stack-machine-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/stack-machine-sandbox.yml
created: '2026-07-17'
description: StackMachine is elastic, headless infrastructure for AI applications and agents. It runs existing Node.js, Python, and PHP codebases as WebAssembly with sub-5ms cold starts and sandboxed execution for untrusted or AI-generated code, packing thousands of apps per server. The platform is driven by a single GraphQL API (api.stackmachine.com/graphql) plus official JavaScript and Python SDKs, exposing app deployment, custom domains and DNS, managed databases and volumes, cron jobs, secrets, transactional email, cloud storage, package publishing, SSH access, and usage metering. Backed by a16z.
image: https://www.stackmachine.com/opengraph-image.png
layout: provider
mcp_servers:
- description: ''
  name: Stack Machine MCP Server
  slug: stack-machine-mcp-server
modified: '2026-07-21'
name: Stack Machine
nav: Providers
network: true
overview: 'Stack Machine publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Serverless, WebAssembly, and Edge Compute.


  Stack Machine''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 20 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 39.8
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 41.5
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 39.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/stack-machine/refs/heads/main/screenshots/stack-machine-2026-08-17T082055.png
security:
- kind: authentication
  name: Stack Machine Authentication
  slug: stack-machine-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Stack Machine Domain Security
  slug: stack-machine-domain-security
  summary_line: TLSv1.3
slug: stack-machine
tags:
- Company
- Infrastructure
- Serverless
- WebAssembly
- Edge Compute
- AI Applications
- GraphQL
- Platform-as-a-Service
- Deployment
- Hosting
- DNS
- Databases
website: https://docs.stackmachine.com/
---
