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
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 40
  human_in_the_loop: 2
  name: Fluence Agentic Access
  operation_count: 71
  slug: fluence-agentic-access
  summary_line: 71 operations · 40 acting · 2 human-in-the-loop
api_count: 12
apis:
- description: Billing and payment related endpoints
  name: Fluence Billing API
  slug: fluence-billing-api
- description: Hardware API endpoints
  name: Fluence Hardware API
  slug: fluence-hardware-api
- description: Endpoints to get prices for different resources and cost estimation
  name: Fluence Prices API
  slug: fluence-prices-api
- description: The PublicIP API from Fluence — 3 operation(s) for publicip.
  name: Fluence PublicIP API
  slug: fluence-publicip-api
- description: Endpoints to create, view, update and delete security groups
  name: Fluence SecurityGroup API
  slug: fluence-securitygroup-api
- description: The Service API from Fluence — 1 operation(s) for service.
  name: Fluence Service API
  slug: fluence-service-api
- description: Endpoints to manage SSH keys
  name: Fluence SSH keys API
  slug: fluence-ssh-keys-api
- description: Endpoints to create, view, update and delete storage resources
  name: Fluence Storage API
  slug: fluence-storage-api
- description: Endpoints to create, view, update and delete subnets
  name: Fluence Subnets API
  slug: fluence-subnets-api
- description: Users API endpoints
  name: Fluence Users API
  slug: fluence-users-api
- description: Endpoints to create, view, update and delete VMs
  name: Fluence VMs API
  slug: fluence-vms-api
- description: Endpoints to create, view, update and delete VPCs
  name: Fluence VPCs API
  slug: fluence-vpcs-api
artifact_total: 17
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/fluence-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.fluence.network
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fluence.dev/docs/build/overview
- group: docs
  title: ''
  type: Documentation
  url: https://fluence.dev/docs/build/overview
- group: docs
  title: ''
  type: APIReference
  url: https://api.fluence.dev/swagger-ui/
- group: start
  title: ''
  type: GettingStarted
  url: https://fluence.dev/docs/build/overview
- group: start
  title: ''
  type: Console
  url: https://console.fluence.network
- group: company
  title: ''
  type: Blog
  url: https://www.fluence.network/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fluencelabs
- group: start
  title: ''
  type: SignUp
  url: https://console.fluence.network/auth/sign-up
- group: commercial
  title: ''
  type: TermsOfService
  url: https://console.fluence.network/files/FLUENCE_TERMS_OF_SERVICE.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://console.fluence.network/files/FLUENCE_PRIVACY_POLICY.pdf
- group: auth
  title: ''
  type: Compliance
  url: https://www.fluence.network/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fluence-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/fluence-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fluence-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fluence-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fluence-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fluence-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fluence-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fluence-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fluence-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fluence-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fluence-domain-security.yml
created: '2026-07-17'
description: 'Fluence is a decentralized (DePIN) cloud-computing platform offering enterprise-grade CPU and GPU compute — virtual machines, GPU containers, and bare-metal instances — rented from a global marketplace of independent infrastructure providers at up to 85% below traditional clouds, with predictable pricing and zero egress fees. The Fluence API (api.fluence.dev) gives programmatic access to the marketplace: search available compute, deploy and manage VMs, attach storage and public IPs, configure VPCs, subnets, and security groups, register SSH keys, and handle billing. Compute is paid in USDC; the FLT token is used for staking and protocol governance on Fluence''s Arbitrum Orbit L2 appchain. Backed by Multicoin Capital.'
image: https://www.fluence.network/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: fluence-mcp.yml
  slug: fluence-mcpyml
modified: '2026-07-19'
name: Fluence
nav: Providers
network: true
overview: 'Fluence publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Hardware API, Prices API, and 9 more. Tagged areas include Company, Crypto Web3, Cloud Compute, DePIN, and GPU.


  Fluence''s developer surface includes documentation, API reference, getting-started guide, developer console, engineering blog, signup flow, authentication, and 18 more developer resources.'
random_paper: 42
scopes:
- name: Fluence Scopes
  scope_count: 34
  slug: fluence-scopes
  summary_line: 34 scopes
score:
  band: developing
  composite: 44.1
  delta: -0.5
  facets:
    commercial_clarity: 42.1
    contract_quality: 50.7
    developer_ergonomics: 58.2
    discoverability: 81.5
    governance: 20.8
    operational_transparency: 5.3
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fluence/refs/heads/main/screenshots/fluence-2026-07-25T214842.png
security:
- kind: authentication
  name: Fluence Authentication
  slug: fluence-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Fluence Domain Security
  slug: fluence-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fluence
tags:
- Company
- Crypto Web3
- Cloud Compute
- DePIN
- GPU
- Infrastructure
- Virtual Machines
- AI Infrastructure
- Decentralized Cloud
website: https://www.fluence.network
---
