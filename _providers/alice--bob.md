---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Health API from Alice Bob — 1 operation(s) for health.
  name: Alice Bob Health API
  slug: alice--bob-health-api
- description: The Jobs API from Alice Bob — 7 operation(s) for jobs.
  name: Alice Bob Jobs API
  slug: alice--bob-jobs-api
- description: The Targets API from Alice Bob — 3 operation(s) for targets.
  name: Alice Bob Targets API
  slug: alice--bob-targets-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Felis Cloud • API Reference Health API
  slug: open-alice--bob-health-api
- collection_type: open
  name: Felis Cloud • API Reference Jobs API
  slug: open-alice--bob-jobs-api
- collection_type: open
  name: Felis Cloud • API Reference Targets API
  slug: open-alice--bob-targets-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alice--bob-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/alice--bob-felis-cloud-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alice--bob-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alice-bob.com/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/alice--bob-stock
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-gcp.alice-bob.com/console/
- group: docs
  title: ''
  type: Documentation
  url: https://felis.alice-bob.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api-gcp.alice-bob.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://felis.alice-bob.com/docs/getting_started/install_the_qiskit_provider/
- group: operate
  title: ''
  type: Support
  url: https://felis.alice-bob.com/docs/contact_us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Alice-Bob-SW
- group: commercial
  title: ''
  type: Pricing
  url: https://felis.alice-bob.com/docs/felis_cloud/about_felis_cloud/
- group: start
  title: ''
  type: SignUp
  url: https://console.cloud.google.com/marketplace/product/cloud-prod-0/felis-cloud
- group: start
  title: ''
  type: Login
  url: https://api-gcp.alice-bob.com/console/
- group: operate
  title: ''
  type: StatusPage
  url: https://api-gcp.alice-bob.com/console/status
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/alice--bob-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/alice--bob-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alice--bob-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/alice--bob-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/alice--bob-plans.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alice--bob-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/alice--bob-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alice--bob-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alice--bob-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alice--bob-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alice--bob-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alice--bob-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-06'
description: Alice & Bob is a quantum computing company headquartered in Paris with a presence in Boston, founded in 2020, building a universal fault-tolerant quantum computer on cat qubits — superconducting qubits that are intrinsically protected against bit-flip errors. Its commercial developer surface is Felis Cloud, a Quantum Computing as a Service (QCaaS) product that executes quantum circuits on Boson 4 cat-qubit QPUs hosted in Alice & Bob's own premises and on cloud-hosted physical and logical qubit emulators. Felis Cloud is reached through a public REST API (jobs, targets, availability and health) that accepts circuits in QIR format, and through the open-source qiskit-alice-bob-provider Qiskit provider that wraps it.
image: https://avatars.githubusercontent.com/u/72556371?v=4
layout: provider
mcp_servers:
- description: A CANDIDATE tool surface, not a real one. This file records what an MCP server over the Felis Cloud API would expose if Alice & Bob built one, derived one-to-one from the published OpenAPI operations.
  name: Alice Bob MCP Server
  slug: alice-bob-mcp-server
modified: '2026-08-06'
name: Alice Bob
nav: Providers
network: true
overview: 'Alice Bob publishes 3 APIs on the [APIs.io](https://apis.io/) network: Health API, Jobs API, and Targets API. Tagged areas include Company, Quantum Computing, Quantum, Cloud Computing, and Emulation.


  Alice Bob''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 21 more developer resources.'
plans:
- name: Alice  Bob Plans
  plan_count: 3
  slug: alice--bob-plans
random_paper: 4
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 4.5
    contract_quality: 47.6
    developer_ergonomics: 70.8
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 34.2
  previous_composite: 49.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alice--bob/refs/heads/main/screenshots/alice--bob-2026-08-07T161203.png
security:
- kind: authentication
  name: Alice  Bob Authentication
  slug: alice--bob-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Alice  Bob Domain Security
  slug: alice--bob-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alice--bob
tags:
- Company
- Quantum Computing
- Quantum
- Cloud Computing
- Emulation
- Developer Tools
- Compute
- Hardware
- Research
- Qiskit
- QIR
website: https://alice-bob.com/
---
