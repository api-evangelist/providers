---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: Aquila is QuEra's 256-qubit neutral-atom quantum computer, the first publicly accessible neutral-atom QPU. It runs Analog Hamiltonian Simulation (AHS) programs and is accessed programmatically through
  name: QuEra Aquila on AWS Braket
  slug: quera-aquila-aws-braket
- description: Gemini-class is QuEra's gate-model neutral-atom quantum computer with 260 Rubidium-87 physical qubits, all-to-all connectivity across two operational zones (storage and entanglement), and Dynamic Qubi
  name: QuEra Gemini Neutral-Atom Quantum Computer
  slug: quera-gemini-system
- description: Bloqade Analog (pip install bloqade-analog) is QuEra's Python SDK for writing, simulating, and submitting analog Hamiltonian programs to QuEra neutral-atom QPUs. It provides a hardware-first programmi
  name: Bloqade Analog Python SDK
  slug: bloqade-analog-sdk
- description: Bloqade Circuit is the gate-model eDSL component of the Bloqade family, built on the Bloqade Core eDSL infrastructure (Apache-2.0). It targets logical/gate-model programs for neutral-atom hardware suc
  name: Bloqade Circuit Python SDK
  slug: bloqade-circuit-sdk
- description: Bloqade.jl is QuEra's Julia package for quantum computation and quantum simulation based on the neutral-atom architecture. It is emulation-first, supporting large analog Hamiltonian simulations on CPU
  name: Bloqade.jl Julia SDK
  slug: bloqade-jl-sdk
- description: Kirin (Kernel Intermediate Representation Infrastructure) is QuEra's Python compiler framework that underpins the Bloqade Core and Bloqade Circuit eDSLs. It provides a typed IR for quantum kernels wit
  name: Kirin Kernel IR Infrastructure
  slug: kirin-ir
- description: 'tsim is QuEra''s open-source fast universal quantum circuit sampler for QEC based on ZX stabilizer rank decomposition. Released April 2026 alongside the paper "Tsim: Fast Universal Simulator for Quantu'
  name: tsim Universal QEC Simulator
  slug: tsim
- description: Bloqade Shuttle is the SDK for simulating and running neutral-atom programs with explicit atom movement; Bloqade Lanes is the atom-shuttle compiler for fixed-lane architectures; Bloqade Decoders provi
  name: Bloqade Shuttle and Lanes Compilation SDKs
  slug: bloqade-shuttle-lanes
artifact_total: 24
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quera-computing-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.quera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bloqade.quera.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/braket/latest/developerguide/braket-devices.html
- group: docs
  title: ''
  type: Documentation
  url: https://aws.amazon.com/braket/quantum-computers/quera/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/QuEraComputing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quera-computing-inc
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/QuEraComputing/QuEra-braket-examples
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/bloqade-analog/
- group: company
  title: ''
  type: Blog
  url: https://www.quera.com/blog
- group: build
  title: ''
  type: SDKs
  url: https://github.com/QuEraComputing/Bloqade.jl
- group: build
  title: ''
  type: SDKs
  url: https://github.com/QuEraComputing/bloqade-circuit
- group: build
  title: ''
  type: SDKs
  url: https://github.com/QuEraComputing/kirin
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/QuEraComputing/tsim
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/braket/pricing/
- group: operate
  title: ''
  type: Contact
  url: https://www.quera.com/contact
- group: company
  title: ''
  type: News
  url: https://www.quera.com/news
created: '2026-05-25T00:00:00.000Z'
description: QuEra Computing is a Boston-based neutral-atom quantum computing company (founded 2018) that operates Aquila, a 256-qubit Analog Hamiltonian Simulation QPU available publicly through Amazon Braket, and Gemini-class, a 260-qubit gate-model neutral-atom system used for fault-tolerant logical-qubit research with Harvard and MIT. QuEra has no native public REST API; developers submit programs to Aquila through the AWS Braket task API using QuEra's Bloqade SDKs (bloqade-analog for Python hardware submission, Bloqade.jl for Julia emulation, bloqade-circuit for gate-model programs), built on the Kirin compiler IR. Additional open-source tools include tsim (QEC circuit sampling), bloqade-shuttle, bloqade-lanes, and bloqade-decoders for the Dynamic Qubit Array compilation stack.
features:
- Aquila — 256-qubit neutral-atom Analog Hamiltonian Simulation QPU available on AWS Braket in us-east-1
- AWS Braket device ARN arn:aws:braket:us-east-1::device/qpu/quera/Aquila
- Aquila on-demand pricing $0.30 per task and $0.01 per shot through AWS Braket
- Gemini-class — 260-qubit gate-model neutral-atom system with Dynamic Qubit Array (DQA) shuttling and all-to-all connectivity
- Reported Gemini fidelities 99.9% (global 1-qubit), 99.7% (local 1-qubit), 99.2% (2-qubit), SPAM 99.7%
- Fault-tolerant magic-state distillation demonstrated on Gemini with Harvard and MIT (color codes d=3, d=5)
- Bloqade Analog Python SDK (pip install bloqade-analog) — hardware-first AHS submission to Aquila
- Bloqade.jl Julia SDK — emulation-first analog quantum simulation on CPU/GPU
- Bloqade Circuit + Bloqade Core — gate-model eDSL targeting Gemini-class hardware
- Kirin — Python kernel IR infrastructure powering the Bloqade eDSL family
- tsim — open-source ZX stabilizer-rank QEC circuit sampler (April 2026)
- Bloqade Shuttle, Bloqade Lanes, Bloqade Decoders — atom-shuttling compilation and QEC decoder integrations
- Premium Cloud Access program with priority bookings and direct QuEra scientist support
- On-premise deployment option for enterprise and national HPC sites
- No public QuEra-operated REST API — programmatic access is via AWS Braket task API and Bloqade SDKs
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quera-computing.png
layout: provider
modified: '2026-05-25'
name: QuEra Computing
nav: Providers
network: true
overview: 'QuEra Computing publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Quantum Computing, Neutral Atom, Analog Hamiltonian Simulation, AWS Braket, and Aquila.


  QuEra Computing''s developer surface includes developer portal, documentation, getting-started guide, engineering blog, pricing, product news, and 11 more developer resources.'
random_paper: 29
score:
  band: emerging
  composite: 18.4
  delta: -2.3
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 20.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Quera Computing Domain Security
  slug: quera-computing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quera-computing
tags:
- Quantum Computing
- Neutral Atom
- Analog Hamiltonian Simulation
- AWS Braket
- Aquila
- Gemini
- Fault Tolerance
- Quantum Error Correction
- Bloqade
- Hardware
website: https://www.quera.com/
---
