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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-24'
api_count: 13
apis:
- description: Official Python SDK for the QUA pulse-level programming language. Provides the QuantumMachinesManager client, qua DSL (program, declare, play, measure, wait, save, stream_processing, math, casting, ra
  name: qm-qua Python SDK
  slug: qm-qua-python-sdk
- description: Cloud-hosted OPX simulator distributed as the qm-saas Python package. Allows developers to author and validate QUA programs without physical OPX hardware; mirrors the qm-qua client surface against a m
  name: qm-saas Cloud Simulator
  slug: qm-saas
- description: High-level libraries and reference experiments built over QUA. Covers superconducting, semiconductor, NV, and other qubit modalities with ready-to-run calibration scripts and example sequences.
  name: QUA Libraries (qua-libs)
  slug: qua-libs
- description: Toolbox of Python utilities for QUA experiments — analog filters, mixer calibration, plotting, calibration helpers, and integrations with common lab instruments. Distributed on PyPI as qualang-tools.
  name: py-qua-tools
  slug: py-qua-tools
- description: 'Framework for abstracting and managing quantum programming environments on top of QUA. Provides an object model for qubits, resonators, pulses, and configuration; serializes to JSON and generates QUA '
  name: Quantum Abstract Machine (QUAM)
  slug: quam
- description: Builder tool for generating QUAM state from hardware wiring and configuration inputs.
  name: QUAM Builder
  slug: quam-builder
- description: User-programmable calibration software for large-scale quantum computers. Orchestrates calibration graphs (calibration nodes and their dependencies) on top of QUA/QUAM.
  name: QUAlibrate
  slug: qualibrate
- description: TypeScript front-end web application for running and visualizing QUAlibrate calibration graphs.
  name: QUAlibrate App
  slug: qualibrate-app
- description: Core Python library that defines the calibration node and graph abstractions used by QUAlibrate.
  name: QUAlibrate Core
  slug: qualibrate-core
- description: Execution service that runs QUAlibrate calibration nodes and graphs.
  name: QUAlibrate Runner
  slug: qualibrate-runner
- description: Configuration management package for QUAlibrate deployments.
  name: QUAlibrate Config
  slug: qualibrate-config
- description: Collection of calibration graph building blocks (qubit spectroscopy, Rabi, T1, T2, readout calibration, etc.) for QUAlibrate.
  name: QUAlibration Libraries
  slug: qualibration-libs
- description: Interactive dashboards (Plotly Dash / Streamlit) for visualizing QUA experiment results and live data streams.
  name: QUA Dashboards
  slug: qua-dashboards
artifact_total: 14
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/quantum-machines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.quantum-machines.co
- group: docs
  title: ''
  type: Documentation
  url: https://docs.quantum-machines.co/latest/
- group: other
  title: ''
  type: QOP
  url: https://www.quantum-machines.co/products/qop/
- group: other
  title: ''
  type: OPX1000
  url: https://www.quantum-machines.co/products/opx1000/
- group: other
  title: ''
  type: OPXPlus
  url: https://www.quantum-machines.co/products/opx/
- group: other
  title: ''
  type: Octave
  url: https://www.quantum-machines.co/products/octave/
- group: other
  title: ''
  type: QUA
  url: https://docs.quantum-machines.co/latest/docs/Introduction/qua_overview/
- group: other
  title: ''
  type: QUAlibrate
  url: https://qua-platform.github.io/qualibrate/
- group: build
  title: ''
  type: PythonSDK
  url: https://pypi.org/project/qm-qua/
- group: other
  title: ''
  type: CloudSimulator
  url: https://pypi.org/project/qm-saas/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/qua-platform
- group: company
  title: ''
  type: Blog
  url: https://www.quantum-machines.co/blog/
- group: company
  title: ''
  type: News
  url: https://www.quantum-machines.co/news/
- group: other
  title: ''
  type: Customers
  url: https://www.quantum-machines.co/customers/
- group: company
  title: ''
  type: Partners
  url: https://www.quantum-machines.co/partners/
- group: other
  title: ''
  type: Company
  url: https://www.quantum-machines.co/about/
- group: company
  title: ''
  type: Careers
  url: https://www.quantum-machines.co/careers/
- group: operate
  title: ''
  type: Contact
  url: https://www.quantum-machines.co/contact/
- group: operate
  title: ''
  type: Support
  url: https://www.quantum-machines.co/support/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quantum-machines/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/QM_quantum
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@QuantumMachines
created: '2026-05-24'
description: Quantum Machines is a Tel Aviv, Israel-based quantum control company that builds the Quantum Orchestration Platform (QOP) — a unified hardware and software stack for controlling quantum processors at the pulse level. Its hardware portfolio centers on the OPX+ and OPX1000 controllers, which are built around a custom Pulse Processing Unit (PPU) architecture that executes classical control and real-time feedback alongside arbitrary waveform generation, with sub-microsecond classical-quantum round trips and 160 ns active reset latency. The platform is programmed in QUA, the company's domain-specific pulse-level language, exposed to developers through the qm-qua Python SDK and an extensive open-source ecosystem under the qua-platform GitHub organization (QUAlibrate, QUAM, qua-libs, py-qua-tools, qua-dashboards). Quantum Machines also ships peripheral hardware including the Octave up/down converter (to 18 GHz), QDAC-II ultra-low-noise DACs, QSwitch, QBox, and the QCage/QBoard/QFilter
  cryogenic line. The platform is qubit-modality agnostic, supporting superconducting, semiconductor spin, trapped-ion, neutral-atom, and color-center systems, and is used by university labs (MIT, Caltech, Harvard, Princeton, Weizmann) and quantum startups (Alice & Bob, Diraq, EeroQ). Quantum Machines has partnered with NVIDIA on the DGX Quantum hybrid quantum-classical compute platform and acquired the Delft-based QHarbor Bioscience team as a European R&D hub. Quantum Machines does not currently publish a public REST API, OpenAPI specification, or self-service developer signup; the QOP control surface is reached exclusively via the qm-qua Python SDK against an OPX/OPX1000 controller (hardware or qm-saas cloud simulator).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quantum-machines.png
layout: provider
modified: '2026-05-24'
name: Quantum Machines
nav: Providers
network: true
overview: 'Quantum Machines publishes 13 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Quantum Computing, Quantum Control, Pulse Level Programming, QUA, and OPX.


  Quantum Machines'' developer surface includes documentation, GitHub presence, engineering blog, product news, support, YouTube channel, and 17 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 10.5
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/quantum-machines/refs/heads/main/screenshots/quantum-machines-2026-06-20T192413.png
security:
- kind: domain-security
  name: Quantum Machines Domain Security
  slug: quantum-machines-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: quantum-machines
tags:
- Quantum Computing
- Quantum Control
- Pulse Level Programming
- QUA
- OPX
- OPX1000
- QOP
- Quantum Orchestration Platform
- Pulse Processing Unit
- Real Time Feedback
- Arbitrary Waveform Generation
- Superconducting Qubits
- Trapped Ions
- Neutral Atoms
- Color Centers
- Cryogenic Electronics
- Hardware
- Israel
website: https://www.quantum-machines.co
---
