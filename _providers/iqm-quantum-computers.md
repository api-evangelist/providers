---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.7
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The REST API behind IQM Resonance, IQM's quantum cloud service. It lists the quantum computers available on a server, reports their health and calibration state, accepts circuit and sweep jobs for exe
  name: IQM Resonance API
  slug: iqm-quantum-computers-resonance
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iqm-quantum-computers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://iqm.tech/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.iqm.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.iqm.tech/iqm-client/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.iqm.tech/iqm-client/API.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.iqm.tech/iqm-client/user_guide_qiskit.html
- group: start
  title: ''
  type: SignUp
  url: https://resonance.iqm.tech/sign-up
- group: commercial
  title: ''
  type: Pricing
  url: https://iqm.tech/products/iqm-resonance/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iqm.tech/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://iqm.tech/contact/
- group: company
  title: ''
  type: Blog
  url: https://iqm.tech/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iqm-finland
- group: operate
  title: ''
  type: Roadmap
  url: https://iqm.tech/technology/roadmap/
- group: build
  title: ''
  type: Packages
  url: packages/iqm-quantum-computers-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/iqm-quantum-computers-packages.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/iqm-quantum-computers-protobuf.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iqm-quantum-computers-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/iqm-quantum-computers-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/iqm-quantum-computers-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/iqm-quantum-computers-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/iqm-quantum-computers-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/iqm-quantum-computers-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/iqm-quantum-computers-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/iqm-quantum-computers-mcp.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/iqm-quantum-computers-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/iqm-quantum-computers-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iqm-quantum-computers-rate-limits.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iqm-quantum-computers-llms.txt
created: '2026-08-23'
description: IQM Quantum Computers (IQM Finland Oy) builds superconducting quantum computers and sells access to them, both as on-premises systems and as a cloud service. Its developer surface is IQM Resonance, a quantum cloud platform at resonance.iqm.tech whose REST API accepts circuits, queues them against a named QPU, and returns measurement results — billed in QPU seconds rather than API calls. Access is through a bearer API token generated from the Resonance dashboard, and the practical client contract is IQM's Apache-2.0 Python stack (iqm-client, with Qiskit, Cirq and Qrisp adapters) rather than a published OpenAPI, which IQM does not ship. IQM does publish 14 first-party Protobuf message contracts defining the Station Control wire format, a dated changelog with explicit breaking-change notices, and a free Starter tier with a monthly credit allowance.
image: https://iqm.tech/wp-content/uploads/2025/02/IQM-Logo-black-transparent.png
layout: provider
mcp_servers:
- description: ''
  name: IQM Quantum Computers MCP Server
  slug: iqm-quantum-computers-mcp-server
modified: '2026-08-23'
name: IQM Quantum Computers
nav: Providers
network: true
overview: 'IQM Quantum Computers publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Quantum Computing, Quantum Cloud, High Performance Computing, Research, and Scientific Computing.


  IQM Quantum Computers'' developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, support, engineering blog, and 21 more developer resources.'
plans:
- name: Iqm Quantum Computers Plans Pricing
  plan_count: 3
  slug: iqm-quantum-computers-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Iqm Quantum Computers Rate Limits
  slug: iqm-quantum-computers-rate-limits
score:
  band: developing
  composite: 44.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 26.7
    developer_ergonomics: 71.4
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 44.6
  provenance:
    conformance: derived
    mcp: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Iqm Quantum Computers Authentication
  slug: iqm-quantum-computers-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Iqm Quantum Computers Domain Security
  slug: iqm-quantum-computers-domain-security
  summary_line: TLSv1.3 · DMARC
slug: iqm-quantum-computers
tags:
- Quantum Computing
- Quantum Cloud
- High Performance Computing
- Research
- Scientific Computing
- Developer Tools
- Protobuf
- Hardware
- Finland
- Deep Tech
website: https://iqm.tech/
---
