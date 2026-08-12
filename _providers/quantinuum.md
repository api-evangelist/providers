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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-11'
api_count: 9
apis:
- description: Nexus is Quantinuum's all-in-one quantum computing cloud platform. It brokers access to Quantinuum H-Series hardware (H1, H2, Helios) and to partner backends including IBM Quantum and Amazon Braket, m
  name: Quantinuum Nexus
  slug: nexus
- description: The Quantinuum Systems API exposes the H-Series trapped-ion (QCCD) quantum computers — System Model H1, System Model H2, and the next-generation Helios — for circuit submission. Direct communication w
  name: Quantinuum Systems (H-Series)
  slug: systems
- description: TKET is Quantinuum's optimizing quantum compiler. The Python interface `pytket` and the C++ core `tket` provide gate-level circuit construction, hardware-agnostic optimization passes, routing, and bac
  name: TKET
  slug: tket
- description: InQuanto is Quantinuum's computational quantum chemistry platform for molecular and materials simulations on near-term and fault-tolerant quantum computers. It implements VQE, quantum phase estimation
  name: InQuanto
  slug: inquanto
- description: lambeq is Quantinuum's open-source Python toolkit for Quantum Natural Language Processing (QNLP). It converts sentences into string diagrams (DisCoCat / DisCoCirc), rewrites them into parameterized qu
  name: lambeq
  slug: lambeq
- description: Guppy (`guppylang`) is Quantinuum's Pythonic quantum-classical programming language. Guppy programs compile through the HUGR hierarchical intermediate representation and target Quantinuum hardware, Se
  name: Guppy
  slug: guppy
- description: Selene is Quantinuum's plugin-extensible emulator for hybrid quantum computation. It simulates the behavior of Quantinuum H-Series hardware including mid-circuit measurement, conditional control flow,
  name: Selene
  slug: selene
- description: Quantum Origin is Quantinuum's verifiable quantum random number generation service, delivering cryptographically strong entropy seeded by quantum measurements for use in PKI, key generation, and other
  name: Quantum Origin
  slug: quantum-origin
- description: Qermit is a Python module for running error-mitigation protocols (probabilistic error cancellation, zero-noise extrapolation, Clifford data regression, dynamical decoupling, etc.) on top of the pytket
  name: Qermit
  slug: qermit
artifact_total: 30
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quantinuum-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.quantinuum.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.quantinuum.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Quantinuum
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quantinuum
- group: start
  title: ''
  type: Signup
  url: https://nexus.quantinuum.com/auth/login
- group: start
  title: ''
  type: Portal
  url: https://nexus.quantinuum.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.quantinuum.com/nexus/trainings/getting_started.html
- group: operate
  title: ''
  type: Support
  url: mailto:qcsupport@quantinuum.com
- group: company
  title: ''
  type: Blog
  url: https://www.quantinuum.com/news
- group: other
  title: ''
  type: Publications
  url: https://github.com/Quantinuum/quantinuum-publications
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Quantinuum/tket
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Quantinuum/pytket-quantinuum
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Quantinuum/pytket-qiskit
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Quantinuum/pytket-braket
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Quantinuum/pytket-cutensornet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Quantinuum/pytket-qir
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Quantinuum/qnexus
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Quantinuum/guppylang
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Quantinuum/hugr
- group: build
  title: ''
  type: SDKs
  url: https://github.com/CQCL/lambeq
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Quantinuum/Qermit
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Quantinuum/selene
- group: build
  title: ''
  type: Tools
  url: https://github.com/Quantinuum/tierkreis
- group: build
  title: ''
  type: Tools
  url: https://github.com/Quantinuum/cryptomite
- group: other
  title: ''
  type: Data
  url: https://github.com/Quantinuum/quantinuum-hardware-specifications
- group: other
  title: ''
  type: Data
  url: https://github.com/Quantinuum/quantinuum-hardware-quantum-volume
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Quantinuum/phir
created: '2026-05-24'
description: 'Quantinuum is an integrated quantum computing company formed by the 2021 merger of Honeywell Quantum Solutions and Cambridge Quantum. It builds trapped-ion (QCCD) quantum computers — the H1, H2, and Helios System Models — and develops the full software stack that runs on them: the Nexus cloud platform, the TKET quantum compiler, the InQuanto computational chemistry package, the lambeq quantum natural language processing toolkit, the Guppy quantum programming language, the Selene emulation framework, and the Quantum Origin verifiable randomness service. Programmatic access to Quantinuum systems is delivered through the Nexus platform (Python client `qnexus` plus a REST/OpenAPI surface) and via partner clouds; circuits are described in OpenQASM 2.0 and the Quantum Intermediate Representation (QIR).'
features:
- H-Series QCCD trapped-ion quantum computers (System Model H1, H2, Helios)
- All-to-all qubit connectivity with high two-qubit gate fidelity
- Mid-circuit measurement, reset, and conditional control flow
- Nexus cloud platform with project, team, role, quota, and credential management
- REST/OpenAPI surface ("Nexus OpenAPI") and `qnexus` Python client
- Backend brokerage to IBM Quantum, Amazon Braket, and other partner systems
- TKET / pytket optimizing compiler with extensive backend extensions
- TKET2 next-generation compiler built on HUGR
- Guppy Pythonic quantum-classical programming language
- InQuanto enterprise quantum chemistry package (VQE, QPE, advanced ansätze)
- lambeq QNLP toolkit (DisCoCat / DisCoCirc to quantum circuits)
- Qermit error-mitigation protocols (PEC, ZNE, CDR, dynamical decoupling)
- Selene plugin-extensible emulator for hybrid programs
- Quantum Origin verifiable QRNG cloud API and on-prem appliance
- QIR and OpenQASM 2.0 program submission formats
- PHIR (PECOS High-level Intermediate Representation) data model
- Tierkreis hybrid workflow manager
- Public hardware specifications and Quantum Volume datasets on GitHub
- Available via Microsoft Azure Quantum and NVIDIA CUDA-Q integrations
- Apache 2.0 open-source licensing for pytket, qnexus, lambeq, Guppy, Selene, Qermit
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quantinuum.png
layout: provider
modified: '2026-05-24'
name: Quantinuum
nav: Providers
network: true
overview: 'Quantinuum publishes 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Quantum Computing, Trapped Ion, Quantum Hardware, Quantum Software, and Quantum Compiler.


  Quantinuum''s developer surface includes developer portal, documentation, signup flow, getting-started guide, support, engineering blog, tooling, and 21 more developer resources.'
random_paper: 67
score:
  band: emerging
  composite: 19.8
  delta: 2.6
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 17.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quantinuum/refs/heads/main/screenshots/quantinuum-2026-06-20T192411.png
security:
- kind: domain-security
  name: Quantinuum Domain Security
  slug: quantinuum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quantinuum
tags:
- Quantum Computing
- Trapped Ion
- Quantum Hardware
- Quantum Software
- Quantum Compiler
- Quantum Chemistry
- Quantum Natural Language Processing
- Quantum Random Number Generator
- QIR
- OpenQASM
- Cloud Platform
website: https://www.quantinuum.com/
---
