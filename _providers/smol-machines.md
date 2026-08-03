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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 49
  human_in_the_loop: 5
  name: Smol Machines Agentic Access
  operation_count: 83
  slug: smol-machines-agentic-access
  summary_line: 83 operations · 49 acting · 5 human-in-the-loop
api_count: 19
apis:
- description: API key management
  name: Smol Machines apikeys API
  slug: smol-machines-apikeys-api
- description: Long-running app deployments
  name: Smol Machines apps API
  slug: smol-machines-apps-api
- description: Self-service account and metering
  name: Smol Machines billing API
  slug: smol-machines-billing-api
- description: Container management within sandboxes
  name: Smol Machines Containers API
  slug: smol-machines-containers-api
- description: Command execution in sandboxes
  name: Smol Machines Execution API
  slug: smol-machines-execution-api
- description: Health, probes, and metrics
  name: Smol Machines health API
  slug: smol-machines-health-api
- description: OCI image management
  name: Smol Machines Images API
  slug: smol-machines-images-api
- description: Log streaming
  name: Smol Machines Logs API
  slug: smol-machines-logs-api
- description: First-class machine lifecycle and exec
  name: Smol Machines machines API
  slug: smol-machines-machines-api
- description: Persistent microVM management
  name: Smol Machines MicroVMs API
  slug: smol-machines-microvms-api
- description: Cluster node enrollment and status
  name: Smol Machines nodes API
  slug: smol-machines-nodes-api
- description: Async operations
  name: Smol Machines operations API
  slug: smol-machines-operations-api
- description: Quota + rate + budget plans
  name: Smol Machines plans API
  slug: smol-machines-plans-api
- description: Warm machine pools
  name: Smol Machines pools API
  slug: smol-machines-pools-api
- description: Sandbox lifecycle management
  name: Smol Machines Sandboxes API
  slug: smol-machines-sandboxes-api
- description: Customer accounts (product-backend)
  name: Smol Machines tenants API
  slug: smol-machines-tenants-api
- description: Node join tokens
  name: Smol Machines tokens API
  slug: smol-machines-tokens-api
- description: Usage and billing
  name: Smol Machines usage API
  slug: smol-machines-usage-api
- description: Persistent volumes
  name: Smol Machines volumes API
  slug: smol-machines-volumes-api
artifact_total: 23
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/smol-machines-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smol-machines-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smol-machines-agentic-access.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://smolmachines.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://smolmachines.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://smolmachines.com/docs/cloud-api
- group: start
  title: ''
  type: GettingStarted
  url: https://smolmachines.com/docs/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://smolmachines.com/docs/cloud-quickstart
- group: start
  title: ''
  type: SignUp
  url: https://smolmachines.com/console
- group: commercial
  title: ''
  type: Pricing
  url: https://smolmachines.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smolmachines.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smolmachines.com/legal/privacy
- group: company
  title: ''
  type: Blog
  url: https://smolmachines.com/engineering
- group: operate
  title: ''
  type: StatusPage
  url: https://smolmachines.com/status
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smol-machines
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/E5r8rEWY9J
- group: start
  title: ''
  type: Registry
  url: https://smolmachines.com/registry
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/smol-machines-smolfleet-openapi.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/smol-machines-smolvm-openapi.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smol-machines-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/smol-machines-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/smol-machines-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/smol-machines-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/smol-machines-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/smol-machines-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/smol-machines-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/smol-machines-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/smol-machines-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/smol-machines-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/smol-machines-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/smol-machines-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Smol Machines (smol machines, inc.) is a Y Combinator-backed developer infrastructure company building portable, self-contained Linux microVMs. Its open-source `smolvm` engine and `smol` CLI (both Rust, Apache-2.0) boot hardware-isolated virtual machines from any OCI image in under 200ms — on a laptop, in the smolfleet cloud, or self-hosted — with no daemon and no Docker. The same Machine API runs locally as an in-process microVM or against the hosted smolfleet control plane at api.smolmachines.com, so teams sandbox untrusted code and AI-agent workloads, ship stateful `.smolmachine` artifacts, and deploy machines across a cluster without changing a line. Node and Python SDKs (`smolmachines`), a local REST API, and a cloud REST API are all public.
image: https://smolmachines.com/install.sh
layout: provider
mcp_servers:
- description: ''
  name: smol-machines-mcp.yml
  slug: smol-machines-mcpyml
modified: '2026-07-21'
name: Smol Machines
nav: Providers
network: true
overview: 'Smol Machines publishes 19 APIs on the [APIs.io](https://apis.io/) network, including apikeys API, apps API, billing API, and 16 more. Tagged areas include Company, MicroVM, Sandbox, Virtualization, and Developer Tools.


  Smol Machines'' developer surface includes authentication, documentation, API reference, getting-started guide, quickstart, signup flow, pricing, and 25 more developer resources.'
random_paper: 93
score:
  band: developing
  composite: 49.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 46.9
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Smol Machines Authentication
  slug: smol-machines-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Smol Machines Domain Security
  slug: smol-machines-domain-security
  summary_line: TLSv1.3 · DMARC
slug: smol-machines
tags:
- Company
- MicroVM
- Sandbox
- Virtualization
- Developer Tools
- Infrastructure
- AI Agents
- Code Execution
- Containers
- Cloud
website: https://smolmachines.com/docs
---
