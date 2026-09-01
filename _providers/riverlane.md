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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'Bearer-token cloud service backing the Deltakit SDK. Exposes the compute-heavy and proprietary parts of the QEC workflow that do not run locally: leakage noise generation and simulation, decoding with'
  name: Deltakit Cloud API
  slug: deltakit-cloud-api
artifact_total: 4
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Deltakit/deltakit/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Deltakit/deltakit/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Deltakit/deltakit/blob/main/docs/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Deltakit/deltakit/blob/main/docs/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Deltakit/deltakit/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.riverlane.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://deltakit.riverlane.com/
- group: docs
  title: ''
  type: Documentation
  url: https://deltakit.readthedocs.io/
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/Deltakit/deltakit/blob/main/docs/api.rst
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/Deltakit/deltakit/blob/main/docs/guide/getting_started.md
- group: operate
  title: ''
  type: Support
  url: https://github.com/Deltakit/deltakit/discussions
- group: company
  title: ''
  type: Blog
  url: https://www.riverlane.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Deltakit
- group: start
  title: ''
  type: SignUp
  url: https://deltakit.riverlane.com/dashboard/token
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.riverlane.com/privacy-policy
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Deltakit/deltakit
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/riverlane-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/riverlane-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/riverlane-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/riverlane-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/riverlane-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/riverlane-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/riverlane-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/riverlane-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/riverlane-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/riverlane-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/riverlane-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/riverlane-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/Deltakit/deltakit/blob/main/docs/SECURITY.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/riverlane-domain-security.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://www.hiive.com/securities/riverlane-stock
created: '2026-08-05'
description: 'Riverlane is a Cambridge (UK) quantum computing company building the quantum error correction (QEC) stack. Its two product lines are Deltaflow — a real-time QEC system covering qubit data readout, decoding, logical operations and orchestration, running error correction on up to 250 physical qubits with the proprietary Local Clustering Decoder — and Deltakit, an Apache-2.0 open-source Python SDK for designing, generating, simulating, decoding and analysing QEC experiments. The public developer surface is the Deltakit cloud service at https://deltakit.riverlane.com/proxy, a bearer-token API with two coexisting versions: a GraphQL endpoint (/api/graphql, API v1) and an asynchronous task REST API (/api/v2/tasks/add|get|kill, API v2). Both front Riverlane''s proprietary decoders (Ambiguity Clustering, Local Clustering, Collision Clustering), leakage-aware decoding and simulation, iSWAP native-gate circuit generation, and stability-experiment generation. Riverlane publishes no OpenAPI
  or AsyncAPI document; the machine-readable contract is the open-source client library at github.com/Deltakit/deltakit, which is where every endpoint recorded in this profile was read from.'
image: https://avatars.githubusercontent.com/u/41478377?v=4
layout: provider
modified: '2026-08-05'
name: Riverlane
nav: Providers
network: true
overview: 'Riverlane publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Quantum Computing, Quantum Error Correction, Decoders, Scientific Computing, and Python SDK.


  Riverlane''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, changelog, and 24 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 61.9
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 65.0
  previous_composite: 31.9
  provenance:
    conformance: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Riverlane Authentication
  slug: riverlane-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Riverlane Domain Security
  slug: riverlane-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Riverlane Vulnerability Disclosure
  slug: riverlane-vulnerability-disclosure
  summary_line: Hackerone
slug: riverlane
tags:
- Quantum Computing
- Quantum Error Correction
- Decoders
- Scientific Computing
- Python SDK
- GraphQL
- Simulation
- Research Tools
- Open-Source
- HPC
website: https://www.riverlane.com/
---
