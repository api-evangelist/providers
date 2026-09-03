---
access_model:
  confidence: medium
  label: Public API, undisclosed pricing
  onboarding: unknown
  pricing: unknown
  public: true
  source:
  - https://api.cloud.quandela.com/openapi.json
  - https://www.quandela.com/products-and-services/cloud/
  - https://cloud.quandela.com/pricing
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 31
  human_in_the_loop: 3
  name: Quandela Agentic Access
  operation_count: 59
  slug: quandela-agentic-access
  summary_line: 59 operations · 31 acting · 3 human-in-the-loop
api_count: 8
apis:
- baseURL: https://api.cloud.quandela.com/
  baseurl_source: declared
  description: APIs related to job token
  name: Quandela Api - Job Token API
  slug: quandela-api-job-token-api
- baseURL: https://api.cloud.quandela.com/
  baseurl_source: declared
  description: Operations about job - Authenticate by `Cloud Job Token`
  name: Quandela Api - Perceval Job API
  slug: quandela-api-perceval-job-api
- baseURL: https://api.cloud.quandela.com/
  baseurl_source: declared
  description: Operations about job token - Authenticate by `Cloud Job Token`
  name: Quandela Api - Perceval Job Token API
  slug: quandela-api-perceval-job-token-api
- baseURL: https://api.cloud.quandela.com/
  baseurl_source: declared
  description: Service root, health check and specification endpoints
  name: Quandela Platform API
  slug: quandela-platform-api
- baseURL: https://api.cloud.quandela.com/
  baseurl_source: declared
  description: Quantum Random Number generation
  name: Quandela QRNG API
  slug: quandela-qrng-api
- baseURL: https://api.cloud.quandela.com/
  baseurl_source: declared
  description: Quantum Toolbox entrypoints
  name: Quandela Quantum Toolbox API
  slug: quandela-quantumtoolbox-api
arazzos:
- description: Price a Chemistry VQE workload with the estimator before committing credits, check the Quantum Toolbox concurrency ceiling, submit, poll and collect.
  name: Estimate then run a Chemistry VQE workload on Quandela Quantum Toolbox
  slug: quandela-estimate-and-run-chemistry-vqe
- description: Mint a replacement Cloud Job Token, read the outgoing token's per-platform consumption ledger, then revoke and delete it — the full credential rotation Quandela supports entirely over the API.
  name: Rotate and audit a Quandela Cloud Job Token
  slug: quandela-rotate-and-audit-job-token
- description: Mint a Cloud Job Token, verify account capacity, submit a photonic-circuit job, poll to completion, then retrieve the result and the submission record.
  name: Submit a Perceval job to Quandela Cloud and collect the result
  slug: quandela-submit-and-collect-perceval-job
artifact_total: 14
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Quandela/Perceval/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Quandela/Perceval/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Quandela/Perceval/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/quandela-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/quandela-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quandela-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/quandela-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/quandela-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/quandela-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/quandela-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/quandela-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://api.cloud.quandela.com/api/platforms/public
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/quandela-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Quandela/Perceval/releases
- group: start
  title: ''
  type: Sandbox
  url: sandbox/quandela-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/quandela-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/quandela-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/quandela-packages.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/quandela-cloud-overlay.yaml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/quandela-well-known.yml
- group: agent
  title: ''
  type: MCPCandidate
  url: mcp/quandela-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/quandela-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/quandela-submit-perceval-job.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/quandela-run-quantum-toolbox-algorithm.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/quandela-manage-cloud-job-tokens.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/quandela-draw-certified-quantum-randomness.md
- group: design
  title: ''
  type: Arazzo
  url: arazzo/quandela-submit-and-collect-perceval-job.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/quandela-estimate-and-run-chemistry-vqe.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/quandela-rotate-and-audit-job-token.yml
- group: company
  title: ''
  type: Website
  url: https://www.quandela.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hub.quandela.com
- group: docs
  title: ''
  type: Documentation
  url: https://perceval.quandela.net/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://perceval.quandela.net/docs/v1.2/getting_started.html
- group: operate
  title: ''
  type: Support
  url: https://community.quandela.com
- group: operate
  title: ''
  type: Community
  url: https://community.quandela.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Quandela
- group: operate
  title: ''
  type: Roadmap
  url: https://www.quandela.com/roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.quandela.com/pricing
- group: start
  title: ''
  type: Login
  url: https://account.quandela.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.quandela.com/legal-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.quandela.com/privacy-policy/
- group: other
  title: ''
  type: Cloud
  url: https://cloud.quandela.com
- group: other
  title: ''
  type: Hub
  url: https://hub.quandela.com
- group: other
  title: ''
  type: Perceval
  url: https://perceval.quandela.net
- group: learn
  title: ''
  type: Tutorials
  url: https://perceval.quandela.net/docs/v0.13/notebooks/Tutorial.html
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/perceval-quandela/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Quandela
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Quandela/Perceval
- group: build
  title: ''
  type: SDKs
  url: packages/quandela-packages.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Quandela/Perceval
- group: other
  title: ''
  type: Interop
  url: https://github.com/Quandela/Perceval_Interop
- group: learn
  title: ''
  type: Training
  url: https://training.quandela.com
- group: other
  title: ''
  type: Products
  url: https://www.quandela.com/products-and-services/
- group: other
  title: ''
  type: CloudProduct
  url: https://www.quandela.com/products-and-services/cloud/
- group: other
  title: ''
  type: PercevalProduct
  url: https://www.quandela.com/products-and-services/perceval/
- group: other
  title: ''
  type: AccelerationProgram
  url: https://www.quandela.com/products-and-services/quantum-acceleration-program/
- group: company
  title: ''
  type: Blog
  url: https://www.quandela.com/resources/blog/
- group: company
  title: ''
  type: Careers
  url: https://www.quandela.com/about-us/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.quandela.com/about-us/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quandela
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Quandela_Quantum
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@quandela
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/quandela
created: '2026-05-25'
description: 'Quandela is a Paris-region (Massy, France) photonic quantum computing company building modular, scalable, energy-efficient quantum systems driven by deterministic single-photon sources. Its hardware lineup includes Ascella (its first cloud-accessible system), Belenos (a 12-qubit second-generation machine), Canopus, and Mosaiq (its flagship prototyping platform), alongside Prometheus single-photon sources and the Entropy quantum random number generator. Quandela develops Perceval, the open-source Python framework for programming photonic quantum computers, distributed on PyPI as perceval-quandela with the perceval-interop bridges to Qiskit, QuTiP, cQASM and myQLM and the exqalibur native optimisation kernel. It operates Quandela Cloud, which — contrary to an earlier reading of this profile — DOES publish a real, anonymously readable REST contract: OpenAPI 3.0.3 at https://api.cloud.quandela.com/openapi.json, version v2.8.0-rc4, with 55 paths, 59 operations and 54 component schemas,
  plus a Quantum Toolbox sub-specification at /qt-openapi.json. The surface covers Perceval job submission (submit-then-poll, with the circuit carried as an SDK-serialised opaque payload), a self-service Cloud Job Token lifecycle with a per-platform credit ledger, five typed Quantum Toolbox primitives (Chemistry VQE, Custom VQE, CVaR VQE, Graph DSI, Graph Isomorphism) each with a paired cost estimator, and the Entropy QRNG, whose draws return CHSH and min-entropy certification. Authentication is a single declared bearer scheme covering two distinct credentials — an account token from account.quandela.com and a Cloud Job Token minted over the API. Quandela also runs a Quantum Acceleration Program for enterprise pilots in cybersecurity, pharma, chemistry, logistics, finance, energy and aerospace, and publishes a 2024-2030 roadmap to fault-tolerant quantum computing.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quandela.png
layout: provider
modified: '2026-08-17'
name: Quandela
nav: Providers
network: true
overview: 'Quandela publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Api - Job Token API, Api - Perceval Job API, Api - Perceval Job Token API, and 3 more. Tagged areas include Quantum Computing, Photonic Quantum, Photonics, Single Photon Sources, and Quantum Hardware.


  Quandela''s developer surface includes authentication, changelog, sandbox, documentation, getting-started guide, support, pricing, and 57 more developer resources.'
plans:
- name: Quandela Plans Pricing
  plan_count: 0
  slug: quandela-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 6
  name: Quandela Rate Limits
  slug: quandela-rate-limits
score:
  band: developing
  composite: 48.8
  coverage:
    artifact_dirs: 22
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.6
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 55.3
    developer_ergonomics: 61.3
    discoverability: 74.1
    governance: 4.5
    operational_transparency: 71.1
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quandela/refs/heads/main/screenshots/quandela-2026-06-20T192405.png
security:
- kind: authentication
  name: Quandela Authentication
  slug: quandela-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Quandela Domain Security
  slug: quandela-domain-security
  summary_line: TLSv1.3 · DMARC
slug: quandela
tags:
- Quantum Computing
- Photonic Quantum
- Photonics
- Single Photon Sources
- Quantum Hardware
- Quantum Cloud
- QPU
- Perceval
- Python SDK
- Quantum Random Number Generation
- Quantum Simulation
- Variational Quantum Algorithms
- Quantum Chemistry
- Graph Algorithms
- Job Orchestration
- Open-Source
- France
website: https://www.quandela.com
---
