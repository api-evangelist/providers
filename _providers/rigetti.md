---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 3
  name: Rigetti Agentic Access
  operation_count: 52
  slug: rigetti-agentic-access
  summary_line: 52 operations · 17 acting · 3 human-in-the-loop
api_count: 11
apis:
- description: gRPC Translation service that compiles native Quil programs into encrypted Controller Jobs for execution on a Rigetti QPU. Operations include TranslateQuilToEncryptedControllerJob and GetQuantumProces
  name: Rigetti QCS Translation Service (gRPC)
  slug: rigetti-qcs-translation-service
- description: gRPC Controller service that executes encrypted Controller Jobs on a Rigetti QPU endpoint and returns measurement (readout) results. Operations include ExecuteControllerJob, BatchExecuteControllerJobs
  name: Rigetti QCS Controller Service (gRPC)
  slug: rigetti-qcs-controller-service
- description: The account API from Rigetti Computing — 22 operation(s) for account.
  name: Rigetti Computing account API
  slug: rigetti-account-api
- description: The authentication API from Rigetti Computing — 4 operation(s) for authentication.
  name: Rigetti Computing authentication API
  slug: rigetti-authentication-api
- description: Check for the latest SDK versions.
  name: Rigetti Computing clientApplications API
  slug: rigetti-clientapplications-api
- description: The Endpoint is the means of access to a Quantum Processor.
  name: Rigetti Computing endpoints API
  slug: rigetti-endpoints-api
- description: The Engagement is the authorization mechanism for access to the Quantum Processor.
  name: Rigetti Computing engagements API
  slug: rigetti-engagements-api
- description: The Healthcheck API from Rigetti Computing — 1 operation(s) for healthcheck.
  name: Rigetti Computing Healthcheck API
  slug: rigetti-healthcheck-api
- description: The Quantum Processor is the heart of the Rigetti services.
  name: Rigetti Computing quantumProcessors API
  slug: rigetti-quantumprocessors-api
- description: Find existing time on a Rigetti QPU and reserve it.
  name: Rigetti Computing reservations API
  slug: rigetti-reservations-api
- description: The Rigetti QCS API API from Rigetti Computing — 2 operation(s) for rigetti qcs api.
  name: Rigetti Computing Rigetti QCS API API
  slug: rigetti-rigetti-qcs-api-api
arazzos:
- description: Find an available reservation slot on a quantum processor, book it, and confirm the booking.
  name: Rigetti Book QPU Reservation
  slug: rigetti-book-qpu-reservation-workflow
- description: List a user's reservations, inspect the most relevant one, and cancel it, confirming the cancellation.
  name: Rigetti Cancel Reservation
  slug: rigetti-cancel-reservation-workflow
- description: Resolve a processor's default endpoint and create an engagement that grants credentialed access to execute on the QPU.
  name: Rigetti Create Execution Engagement
  slug: rigetti-create-execution-engagement-workflow
- description: List available QPUs, then inspect one processor's metadata, instruction set architecture, and live accessors.
  name: Rigetti Discover Quantum Processor
  slug: rigetti-discover-quantum-processor-workflow
- description: Create a private endpoint for a processor, poll until it reports healthy, then create an engagement against it.
  name: Rigetti Provision Endpoint and Engage
  slug: rigetti-provision-endpoint-and-engage-workflow
- description: Resolve the caller's identity and balance, read a processor's maintenance calendar, and surface available reservation slots before booking.
  name: Rigetti Reservation Readiness Check
  slug: rigetti-reservation-readiness-check-workflow
artifact_total: 69
collections:
- collection_type: postman
  name: Rigetti QCS API
  slug: postman-rigetti-qcs-api
- collection_type: open
  name: Rigetti QCS API
  slug: open-rigetti-qcs-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rigetti-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rigetti-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rigetti-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/rigetti-computing/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/rigetti-book-qpu-reservation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/rigetti-cancel-reservation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/rigetti-create-execution-engagement-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/rigetti-discover-quantum-processor-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/rigetti-provision-endpoint-and-engage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/rigetti-reservation-readiness-check-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.rigetti.com
- group: start
  title: ''
  type: Signup
  url: https://qcs.rigetti.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rigetti.com/qcs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.rigetti.com/qcs/getting-started/installation-and-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rigetti.com/qcs/guides/the-rigetti-qcs-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.api.qcs.rigetti.com/
- group: auth
  title: ''
  type: Authentication
  url: https://qcs.rigetti.com/auth/token
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rigetti.com/qcs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rigetti.com/novera
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rigetti.com/foundry
- group: operate
  title: ''
  type: Support
  url: mailto:support@rigetti.com
- group: operate
  title: ''
  type: Support
  url: https://rigetti.zendesk.com
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.rigetti.com/qcs/troubleshooting
- group: company
  title: ''
  type: Blog
  url: https://www.rigetti.com/blog
- group: company
  title: ''
  type: Press
  url: https://investors.rigetti.com/news-events/news-releases
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/rigetti
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rigetti/pyquil
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rigetti/qcs-sdk-rust
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rigetti/qcs-sdk-rust/tree/main/crates/python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rigetti/qcs-sdk-c
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rigetti/qcs-api-client-rust
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rigetti/qcs-api-client-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rigetti/quil-rs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rigetti/qiskit-rigetti
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rigetti/pyquil-for-azure-quantum
- group: build
  title: ''
  type: SDKs
  url: https://github.com/rigetti/qcs-sdk-qir
- group: build
  title: ''
  type: Tools
  url: https://github.com/rigetti/qcs-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/rigetti/quilc
- group: build
  title: ''
  type: Tools
  url: https://github.com/rigetti/qvm
- group: build
  title: ''
  type: Tools
  url: https://github.com/rigetti/rpcq
- group: build
  title: ''
  type: Tools
  url: https://github.com/rigetti/rigetti-resource-estimation
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/rigetti/forest-tutorials
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/rigetti/grove
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/rigetti/forest-benchmarking
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/rigetti/qcs-paper
- group: other
  title: ''
  type: ProtocolBuffers
  url: https://github.com/rigetti/qcs-api-client-rust/tree/main/qcs-api-client-grpc/proto
- group: docs
  title: ''
  type: Specification
  url: https://github.com/quil-lang/quil
- group: docs
  title: ''
  type: Documentation
  url: https://pyquil.readthedocs.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rs/qcs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rigetti.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rigetti.com/terms-of-service
- group: commercial
  title: ''
  type: Plans
  url: plans/rigetti-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rigetti-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/rigetti-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rigetti-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/rigetti-context.jsonld
created: '2026-05-24'
description: Rigetti Computing (Nasdaq, RGTI) is a Berkeley, California-based quantum computing company building superconducting quantum processors and the full-stack software needed to program and operate them. Founded in 2013 by Chad Rigetti, the company designs, manufactures, and operates multi-chip superconducting QPUs at its Fab-1 in Fremont, CA and offers cloud-based access through Quantum Cloud Services (QCS). Rigetti also sells the Novera QPU (9-qubit) for on-premises customers and provides Quantum Foundry Services for custom development. The current generation system Cepheus-1-108Q (107 qubits, deployed April 2026) is accessed via a hybrid REST + gRPC API surface, programmed using the open Quil instruction language, the pyQuil Python library, and the multi-language qcs-sdk (Rust core with Python bindings). Rigetti's hardware is also available indirectly through AWS Braket, Microsoft Azure Quantum, and as a Qiskit provider via qiskit-rigetti.
features:
- Cepheus-1-108Q superconducting QPU (107 qubits) with 99.84% 1Q gate fidelity and 98.77% 2Q CZ gate fidelity
- Novera 9-qubit QPU for on-premises deployment with dilution refrigerator
- Hybrid REST + gRPC API surface — OpenAPI 3.0 HTTP API for management + gRPC for translation and execution
- OAuth2 / JWT (Okta) authentication with 24-hour access tokens
- Quil — open quantum instruction language with classical control flow and hybrid quantum-classical programs
- Translation service compiles native Quil programs to encrypted Controller Jobs server-side
- Controller service executes batched jobs on a QPU endpoint and returns readout results
- Reservation system for time-boxed exclusive QPU access via /v1/reservations and FindAvailableReservations
- Engagement-based access control — short-lived QPU access tokens scoped to a quantum processor endpoint
- Group / user billing with metered invoices and upcoming-invoice preview
- pyQuil 4.x Python library with Jupyter notebook tutorials and Forest SDK integration
- qcs-sdk multi-language SDK (Rust core + Python and C bindings)
- QVM (Quantum Virtual Machine) and quilc (Quil compiler) for local simulation and compilation
- QIR (Quantum Intermediate Representation) compiler via qcs-sdk-qir
- Qiskit provider via qiskit-rigetti
- Azure Quantum and AWS Braket third-party provider integrations
- Rigetti Resource Estimation (RRE) tool for fault-tolerant algorithm resource analysis
- Quantum Foundry Services for custom QPU development and partner programs
- Publicly traded on Nasdaq (RGTI) with quarterly SEC disclosures
finops:
- name: Rigetti Finops
  service_category: Compute - Quantum
  slug: rigetti-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rigetti.png
integrations:
- Amazon Braket (Rigetti as third-party QPU provider)
- Microsoft Azure Quantum (Rigetti as third-party QPU provider)
- Google Cirq with rigetti.* hardware module
- Qiskit (via qiskit-rigetti provider)
- OpenFermion (via forest-openfermion plugin)
- QIR Alliance (via qcs-sdk-qir compiler)
- Quil-lang ecosystem (quilc, qvm, quil-rs, libquil)
- Okta (OAuth2 identity provider)
json_schemas:
- name: Rigetti Quantum Processor
  property_count: 10
  slug: rigetti-quantum-processor
- name: Rigetti QCS Reservation
  property_count: 10
  slug: rigetti-reservation
jsonld:
- class_count: 36
  name: Rigetti Context
  property_count: 0
  slug: rigetti-context
layout: provider
modified: '2026-05-24'
name: Rigetti Computing
nav: Providers
network: true
overview: 'Rigetti Computing publishes 9 APIs on the [APIs.io](https://apis.io/) network, including account API, authentication API, clientApplications API, and 6 more. Tagged areas include Quantum Computing, Superconducting Qubits, Quantum Cloud Services, QCS, and QPU.


  The Rigetti Computing catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Rigetti Computing''s developer surface includes authentication, developer portal, signup flow, documentation, getting-started guide, pricing, support, and 49 more developer resources.'
plans:
- name: Rigetti Plans Pricing
  plan_count: 6
  slug: rigetti-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 3
  name: Rigetti Rate Limits
  slug: rigetti-rate-limits
rules:
- name: Rigetti Computing API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rigetti-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 66.5
  delta: -4.3
  facets:
    commercial_clarity: 71.1
    contract_quality: 72.8
    developer_ergonomics: 65.2
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 70.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rigetti/refs/heads/main/screenshots/rigetti-2026-06-20T193115.png
security:
- kind: authentication
  name: Rigetti Authentication
  slug: rigetti-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Rigetti Domain Security
  slug: rigetti-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rigetti
solutions:
- Quantum Cloud Services (QCS) — managed cloud access to Rigetti QPUs
- Novera QPU — on-premises 9-qubit superconducting system
- Quantum Foundry Services — custom quantum hardware development
tags:
- Quantum Computing
- Superconducting Qubits
- Quantum Cloud Services
- QCS
- QPU
- Quil
- pyQuil
- NISQ
- Fault-Tolerant Quantum Computing
- Quantum-Classical Hybrid
- Public Company
use_cases:
- Quantum algorithm research and benchmarking on real superconducting hardware
- Variational Quantum Eigensolver (VQE) and Quantum Approximate Optimization Algorithm (QAOA) workloads
- Hybrid quantum-classical machine learning experiments
- Quantum chemistry simulation via OpenFermion + forest-openfermion plugin
- Quantum characterization, verification, and validation (QCVV) using forest-benchmarking
- QPU calibration and Instruction Set Architecture introspection for low-level control
- Academic and government research access (MIT, NASA, Oxford Instruments, Standard Chartered, Edinburgh)
- On-premises quantum computing via Novera QPU for national labs and corporate R&D
- Custom QPU co-design through Quantum Foundry Services
- Multi-cloud quantum access through AWS Braket and Azure Quantum
website: https://www.rigetti.com
---
