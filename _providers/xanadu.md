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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 10
apis:
- description: PennyLane is the cross-platform Python framework for quantum computing, quantum machine learning, and quantum chemistry maintained by Xanadu. It provides automatic differentiation of hybrid quantum-cl
  name: PennyLane
  slug: pennylane
- description: Catalyst is a JIT compiler for hybrid quantum-classical programs written in PennyLane. Built on MLIR, it lowers PennyLane circuits to native machine code with quantum control flow, dynamic shapes, and
  name: Catalyst
  slug: catalyst
- description: Lightning is the family of high-performance state-vector and tensor-network quantum simulators written in C++ for PennyLane. Includes lightning.qubit (CPU), lightning.gpu (CUDA), lightning.kokkos (mul
  name: PennyLane Lightning
  slug: pennylane-lightning
- description: Strawberry Fields is Xanadu's full-stack Python library for designing, simulating, and optimizing continuous-variable (CV) photonic quantum circuits. It ships Gaussian, Fock, TensorFlow, and Bosonic b
  name: Strawberry Fields
  slug: strawberry-fields
- description: MrMustard is a differentiable quantum-optics simulator that bridges phase space and Fock space with pluggable NumPy and JAX backends. It performs fast exact Fock-amplitude computation for Gaussian com
  name: MrMustard
  slug: mrmustard
- description: The Walrus is a Python/C++ library for the fast calculation of hafnians, loop hafnians, and multidimensional Hermite polynomials — the linear-algebra primitives behind Gaussian boson sampling and phot
  name: The Walrus
  slug: thewalrus
- description: Blackbird is Xanadu's quantum assembly language and intermediate representation for continuous-variable photonic quantum computation. It is used to program Xanadu's photonic hardware (X-series, Boreal
  name: Blackbird
  slug: blackbird
- description: PennyLane plugin that integrates IBM's Qiskit framework and IBM Q hardware as PennyLane devices for differentiable quantum programming. Apache-2.0.
  name: PennyLane-Qiskit Plugin
  slug: pennylane-qiskit
- description: FlamingPy is Xanadu's cross-platform Python library for efficient simulation of error correction in fault-tolerant photonic quantum computers, with a variety of pluggable decoder backends. Apache-2.0.
  name: FlamingPy
  slug: flamingpy
- description: Xanadu Cloud Client (xcc) is the Python API and CLI that historically connected users to Xanadu's photonic quantum cloud (Borealis, X-series). Xanadu's Quantum Cloud was retired in January 2026 and th
  name: Xanadu Cloud Client
  slug: xanadu-cloud-client
artifact_total: 37
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xanadu-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://xanadu.ai
- group: start
  title: ''
  type: Portal
  url: https://pennylane.ai
- group: docs
  title: ''
  type: Documentation
  url: https://xanadu.ai/about
- group: company
  title: ''
  type: Blog
  url: https://xanadu.ai/blog
- group: company
  title: ''
  type: Blog
  url: https://pennylane.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://xanadu.ai/careers
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/XanaduAI
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PennyLaneAI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/xanadu-quantum-technologies
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/XanaduAI
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/XanaduAI
- group: operate
  title: ''
  type: Forums
  url: https://discuss.pennylane.ai/
- group: learn
  title: ''
  type: Training
  url: https://pennylane.ai/qml/
- group: learn
  title: ''
  type: Training
  url: https://pennylane.ai/codebook
- group: build
  title: ''
  type: CodeExamples
  url: https://pennylane.ai/qml/demonstrations/
- group: build
  title: ''
  type: Plugins
  url: https://pennylane.ai/plugins
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.pennylane.ai/en/stable/development/release_notes.html
- group: commercial
  title: ''
  type: License
  url: https://github.com/PennyLaneAI/pennylane/blob/master/LICENSE
created: '2026-05-24T00:00:00.000Z'
description: Xanadu is a Toronto-based photonic quantum computing company building cloud-accessible continuous- variable quantum processors based on squeezed states of light. Founded in 2016 by Christian Weedbrook and listed on TSX/Nasdaq (XNDU), Xanadu demonstrated a 50-million-fold Gaussian-boson-sampling speedup with Borealis in 2022 and published modular networked photonic quantum computing in Nature in 2025. Beyond hardware, Xanadu is one of the most prolific open-source contributors in quantum software — it maintains PennyLane (the de-facto cross-platform quantum ML framework), Strawberry Fields, MrMustard, The Walrus, Blackbird, Catalyst, Lightning, and FlamingPy, all under Apache-2.0. Xanadu's own Quantum Cloud was retired in January 2026; the company's developer surface is now centered entirely on its open-source stack and integrations with third-party QPUs.
features:
- description: Continuous-variable photonic quantum processors based on squeezed states of light, including the Borealis Gaussian-boson-sampling device and the Aurora modular system targeting fault-tolerant scaling.
  name: Photonic Quantum Hardware
- description: Hardware-agnostic Python framework for differentiable quantum programming across PyTorch, JAX, TensorFlow, and NumPy with first-class quantum machine learning and quantum chemistry support.
  name: PennyLane Open-Source Framework
- description: Plugins connect PennyLane to IBM Qiskit, AWS Braket, Google Cirq, IonQ, Rigetti, Microsoft QDK, Quantinuum/Honeywell, Qulacs, and Xanadu's own Strawberry Fields.
  name: Plugin Ecosystem
- description: C++ state-vector and tensor-network simulators with CPU, CUDA GPU, Kokkos, and tensor backends for laptop-to-HPC quantum circuit simulation.
  name: Lightning High-Performance Simulators
- description: MLIR-based just-in-time compiler that lowers PennyLane hybrid quantum-classical programs to native code with quantum control flow and end-to-end differentiation.
  name: Catalyst JIT Compiler
- description: Strawberry Fields, MrMustard, The Walrus, Blackbird, and FlamingPy provide continuous-variable simulation, differentiable optics, Gaussian-boson-sampling primitives, an assembly DSL, and fault-tolerant error-correction tooling.
  name: Photonic Software Stack
- description: Interactive Xanadu Quantum Codebook plus the pennylane.ai/qml hub with hundreds of research demos covering quantum machine learning, chemistry, and algorithms.
  name: Quantum Codebook and QML Hub
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/xanadu.png
integrations:
- description: PennyLane-Qiskit plugin exposes IBM Q hardware and Qiskit simulators as PennyLane devices.
  name: IBM Qiskit / IBM Quantum
- description: PennyLane plugin for Amazon Braket lets PennyLane circuits run against Braket-managed simulators and partner QPUs.
  name: AWS Braket
- description: PennyLane-Cirq plugin integrates Google's Cirq simulators.
  name: Google Cirq
- description: PennyLane-IonQ plugin targets IonQ trapped-ion simulators and hardware.
  name: IonQ
- description: PennyLane-Rigetti plugin connects to Rigetti Forest QPUs and the QVM.
  name: Rigetti
- description: PennyLane-Honeywell plugin targets Quantinuum's trapped-ion systems.
  name: Quantinuum / Honeywell
- description: PennyLane-qsharp plugin connects PennyLane to the Microsoft QDK simulators.
  name: Microsoft Quantum Development Kit
- description: PennyLane-Qulacs plugin provides access to the Qulacs simulator.
  name: Qulacs
- description: First-class differentiable interfaces for every major Python ML framework.
  name: PyTorch / JAX / TensorFlow / NumPy
- description: Lightning GPU and Lightning Tensor leverage NVIDIA cuQuantum for accelerated simulation.
  name: NVIDIA cuQuantum
json_schemas:
- name: PennyLane Device
  property_count: 9
  slug: pennylane-device
jsonld:
- class_count: 0
  name: Xanadu Context
  property_count: 3
  slug: xanadu-context
layout: provider
modified: '2026-05-24'
name: Xanadu
nav: Providers
network: true
overview: 'Xanadu publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Quantum Computing, Photonic Quantum Computing, Quantum Machine Learning, Continuous Variable, and Open Source.


  The Xanadu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Xanadu''s developer surface includes developer portal, documentation, engineering blog, YouTube channel, training material, code examples, release notes, and 12 more developer resources.'
random_paper: 29
rules:
- name: Xanadu API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: xanadu-jsonschema-spectral-rules
score:
  band: emerging
  composite: 29.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 20.8
    developer_ergonomics: 19.6
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 29.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/xanadu/refs/heads/main/screenshots/xanadu-2026-06-20T201650.png
security:
- kind: domain-security
  name: Xanadu Domain Security
  slug: xanadu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: xanadu
tags:
- Quantum Computing
- Photonic Quantum Computing
- Quantum Machine Learning
- Continuous Variable
- Open Source
- Python
- PennyLane
- Strawberry Fields
- Toronto
use_cases:
- description: Train hybrid quantum-classical models with automatic differentiation against simulators and real QPUs through a single PennyLane API.
  name: Quantum Machine Learning Research
- description: Run variational quantum eigensolver and chemistry workflows via pennylane.qchem, including ground state, excited state, and dynamics simulations.
  name: Quantum Chemistry
- description: Design continuous-variable algorithms — Gaussian boson sampling, graph optimization, molecular vibronic spectra — in Strawberry Fields and MrMustard.
  name: Photonic Algorithm Research
- description: Use FlamingPy to simulate and benchmark photonic fault-tolerant quantum-computing architectures and decoders.
  name: Fault-Tolerant Architecture Studies
- description: Run large state-vector and tensor-network simulations on multi-GPU and multi-node clusters with Lightning + Catalyst.
  name: HPC-Scale Quantum Simulation
- description: Teach undergraduates and researchers quantum computing through the Xanadu Quantum Codebook, QHack, and the pennylane.ai demo library.
  name: Quantum Education
website: https://xanadu.ai
---
