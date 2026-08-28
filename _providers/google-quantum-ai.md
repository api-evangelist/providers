---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Google Quantum Ai Agentic Access
  operation_count: 27
  slug: google-quantum-ai-agentic-access
  summary_line: 27 operations · 12 acting
api_count: 15
apis:
- description: Cirq is an Apache 2.0 Python framework for designing, manipulating, simulating, and executing Noisy Intermediate-Scale Quantum (NISQ) circuits. Cirq is the canonical client library for Google's Quantu
  name: Cirq
  slug: cirq
- description: qsim is a high-performance C++ state-vector simulator with a Python (qsimcirq) binding that plugs directly into Cirq. It is optimised for AVX/AVX-512, CUDA, and cuQuantum backends and is the default c
  name: qsim
  slug: qsim
- description: OpenFermion is an Apache 2.0 library for translating quantum chemistry and materials science problems (electronic structure, fermionic operators, second quantisation) into quantum circuits suitable fo
  name: OpenFermion
  slug: openfermion
- description: Stim is a fast stabilizer-circuit simulator and detector-error-model toolchain that underpins Google Quantum AI's quantum error-correction work, including the Willow surface-code experiments. It expos
  name: Stim
  slug: stim
- description: Qualtran provides abstractions (Bloqs) for expressing, decomposing, and resource-estimating fault-tolerant quantum algorithms. It is Google Quantum AI's framework for reasoning about future error-corr
  name: Qualtran
  slug: qualtran
- description: TensorFlow Quantum (TFQ) is a hybrid quantum-classical machine learning library that integrates Cirq circuits as differentiable layers inside TensorFlow/Keras pipelines. Maintained jointly by Google Q
  name: TensorFlow Quantum
  slug: tensorflow-quantum
- description: ReCirq is a research-grade collection of reproducible Cirq experiments and applications published by Google Quantum AI, covering Fermi-Hubbard simulations, quantum chemistry benchmarks, OTOC measureme
  name: ReCirq
  slug: recirq
- description: Tesseract is a search-based maximum-likelihood decoder for quantum error correction that accompanies Stim. It targets surface-code and color-code decoding workloads used in Willow-era QEC demonstratio
  name: Tesseract Decoder
  slug: tesseract-decoder
- description: Unitary is an API library for adding quantum behaviours (superposition, entanglement, measurement) into classical games and interactive software, used in Google Quantum AI's educational outreach work.
  name: Unitary
  slug: unitary
- description: Periodic device performance snapshots.
  name: Google Quantum AI Calibrations API
  slug: google-quantum-ai-calibrations-api
- description: Executions of a program against a processor or simulator backend.
  name: Google Quantum AI Jobs API
  slug: google-quantum-ai-jobs-api
- description: Quantum processing units (Willow, Sycamore-class) available to the project.
  name: Google Quantum AI Processors API
  slug: google-quantum-ai-processors-api
- description: Hardware-compatible circuits uploaded to a Google Cloud project.
  name: Google Quantum AI Programs API
  slug: google-quantum-ai-programs-api
- description: Processor time-slot reservations and budgets.
  name: Google Quantum AI Reservations API
  slug: google-quantum-ai-reservations-api
- description: Measurement results returned by completed jobs.
  name: Google Quantum AI Results API
  slug: google-quantum-ai-results-api
artifact_total: 61
collections:
- collection_type: postman
  name: Google Quantum Engine Calibrations API
  slug: postman-google-quantum-ai-calibrations-api
- collection_type: postman
  name: Google Quantum Engine Calibrations Jobs API
  slug: postman-google-quantum-ai-jobs-api
- collection_type: postman
  name: Google Quantum Engine Calibrations Processors API
  slug: postman-google-quantum-ai-processors-api
- collection_type: postman
  name: Google Quantum Engine Calibrations Programs API
  slug: postman-google-quantum-ai-programs-api
- collection_type: postman
  name: Google Quantum Engine Calibrations Reservations API
  slug: postman-google-quantum-ai-reservations-api
- collection_type: postman
  name: Google Quantum Engine Calibrations Results API
  slug: postman-google-quantum-ai-results-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Quantum Engine Calibrations API
  slug: open-google-quantum-ai-calibrations-api
- collection_type: open
  name: Google Quantum Engine Calibrations Jobs API
  slug: open-google-quantum-ai-jobs-api
- collection_type: open
  name: Google Quantum Engine Calibrations Processors API
  slug: open-google-quantum-ai-processors-api
- collection_type: open
  name: Google Quantum Engine Calibrations Programs API
  slug: open-google-quantum-ai-programs-api
- collection_type: open
  name: Google Quantum Engine Calibrations Reservations API
  slug: open-google-quantum-ai-reservations-api
- collection_type: open
  name: Google Quantum Engine Calibrations Results API
  slug: open-google-quantum-ai-results-api
- collection_type: open
  name: Google Quantum Engine API
  slug: open-quantum-engine-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-quantum-ai/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-quantum-ai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-quantum-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-quantum-ai-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-quantum-ai-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://quantumai.google/
- group: docs
  title: ''
  type: Documentation
  url: https://quantumai.google/cirq
- group: docs
  title: ''
  type: Documentation
  url: https://quantumai.google/software
- group: docs
  title: ''
  type: Documentation
  url: https://quantumai.google/cirq/google/engine
- group: docs
  title: ''
  type: Documentation
  url: https://quantumai.google/cirq/google/concepts
- group: docs
  title: ''
  type: Documentation
  url: https://quantumai.google/cirq/google/access
- group: start
  title: ''
  type: GettingStarted
  url: https://quantumai.google/cirq/start/install
- group: start
  title: ''
  type: GettingStarted
  url: https://quantumai.google/cirq/start/start
- group: start
  title: ''
  type: GettingStarted
  url: https://quantumai.google/cirq/start/basics
- group: docs
  title: ''
  type: Documentation
  url: https://quantumai.google/reference/python/cirq/all_symbols
- group: docs
  title: ''
  type: Documentation
  url: https://quantumai.google/reference/python/cirq_google
- group: docs
  title: ''
  type: Documentation
  url: https://quantumai.google/qsim
- group: docs
  title: ''
  type: Documentation
  url: https://quantumai.google/openfermion
- group: docs
  title: ''
  type: Documentation
  url: https://quantumai.google/quantumcomputer
- group: docs
  title: ''
  type: Documentation
  url: https://quantumai.google/roadmap
- group: docs
  title: ''
  type: Documentation
  url: https://quantumai.google/research
- group: start
  title: ''
  type: Signup
  url: https://quantumai.google/willowearlyaccess
- group: learn
  title: ''
  type: Training
  url: https://quantumai.google/learn/map
- group: learn
  title: ''
  type: Training
  url: https://quantumai.google/learn
- group: company
  title: ''
  type: Blog
  url: https://blog.google/technology/google-deepmind/google-quantum-ai/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/googlequantumai
- group: learn
  title: ''
  type: VideoChannel
  url: https://www.youtube.com/@GoogleQuantumAI
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quantumlib
- group: build
  title: ''
  type: SDKs
  url: https://github.com/quantumlib/Cirq
- group: build
  title: ''
  type: SDKs
  url: https://github.com/quantumlib/qsim
- group: build
  title: ''
  type: SDKs
  url: https://github.com/quantumlib/OpenFermion
- group: build
  title: ''
  type: SDKs
  url: https://github.com/quantumlib/Stim
- group: build
  title: ''
  type: SDKs
  url: https://github.com/quantumlib/qualtran
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/quantumlib/ReCirq
- group: build
  title: ''
  type: Tools
  url: https://github.com/quantumlib/tesseract-decoder
- group: build
  title: ''
  type: SDKs
  url: https://github.com/quantumlib/unitary
- group: build
  title: ''
  type: Tools
  url: https://github.com/quantumlib/chromobius
- group: build
  title: ''
  type: SDKs
  url: https://github.com/quantumlib/TypedUnits
- group: build
  title: ''
  type: SDKs
  url: https://github.com/tensorflow/quantum
- group: build
  title: ''
  type: PackageURL
  url: https://pypi.org/project/cirq/
- group: build
  title: ''
  type: PackageURL
  url: https://pypi.org/project/cirq-google/
- group: build
  title: ''
  type: PackageURL
  url: https://pypi.org/project/qsimcirq/
- group: build
  title: ''
  type: PackageURL
  url: https://pypi.org/project/openfermion/
- group: build
  title: ''
  type: PackageURL
  url: https://pypi.org/project/stim/
- group: operate
  title: ''
  type: Forums
  url: https://groups.google.com/g/cirq
- group: operate
  title: ''
  type: Forums
  url: https://quantumcomputing.stackexchange.com/questions/tagged/cirq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/quantumlib/Cirq/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/quantumlib/Cirq/blob/main/LICENSE
- group: learn
  title: ''
  type: Courses
  url: https://www.coursera.org/learn/quantum-error-correction
- group: commercial
  title: ''
  type: Plans
  url: plans/google-quantum-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/google-quantum-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/google-quantum-ai-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Google Quantum AI is Google's quantum-computing research and engineering arm, building superconducting quantum processors (most recently the Willow chip with below-threshold quantum error correction) and the open software stack that runs on them. The team operates the Quantum Computing Service via the Quantum Engine API (quantum.googleapis.com, v1alpha1), accessed primarily through the cirq-google Python client. Google Quantum AI also stewards a portfolio of Apache 2.0 open-source quantum software — Cirq, qsim, OpenFermion, Stim, Qualtran, TensorFlow Quantum, ReCirq, Tesseract, and Unitary — published under the quantumlib GitHub organisation, plus the Willow Early Access Program for sponsored researcher access to current hardware.
examples:
- key_count: 2
  name: Quantum Engine Create Job Example
  slug: quantum-engine-create-job-example
- key_count: 2
  name: Quantum Engine Create Program Example
  slug: quantum-engine-create-program-example
- key_count: 2
  name: Quantum Engine List Processors Example
  slug: quantum-engine-list-processors-example
features:
- Willow superconducting quantum processor with below-threshold quantum error correction
- Quantum Engine REST/gRPC API (quantum.googleapis.com, v1alpha1) for program, job, processor, reservation, and calibration management
- cirq-google as the canonical client (QuantumEngineServiceClient) wrapping the gRPC service
- Cirq Python framework v1.6.x for NISQ circuit design, simulation, and execution
- qsim high-performance state-vector simulator with CUDA + cuQuantum acceleration
- OpenFermion for quantum chemistry and materials simulation
- Stim stabilizer simulator and Tesseract decoder for surface-code QEC
- Qualtran for fault-tolerant algorithm authoring and resource estimation
- TensorFlow Quantum for hybrid quantum-classical machine learning
- ReCirq library of reproducible research experiments
- Willow Early Access Program for sponsored researcher access to the latest hardware
- Google Cloud IAM / Application Default Credentials for authentication
- Cirq integrations for AQT, IonQ, Pasqal, and Rigetti via dedicated subpackages
- Quantum Virtual Machine (QVM) including the willow_pink target for noise-aware local simulation
- Coursera "Quantum Error Correction" course produced with Google Quantum AI
- Unitary game-development library for educational quantum applications
- All Google Quantum AI open-source software is Apache 2.0 licensed
finops:
- name: Google Quantum Ai Finops
  service_category: Quantum Computing
  slug: google-quantum-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-quantum-ai.png
json_schemas:
- name: QuantumJob
  property_count: 9
  slug: google-quantum-ai-quantum-job
- name: QuantumProgram
  property_count: 7
  slug: google-quantum-ai-quantum-program
jsonld:
- class_count: 27
  name: Google Quantum Ai Context
  property_count: 5
  slug: google-quantum-ai-context
layout: provider
modified: '2026-05-25'
name: Google Quantum AI
nav: Providers
network: true
overview: 'Google Quantum AI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Calibrations API, Jobs API, Processors API, and 3 more. Tagged areas include Quantum Computing, Quantum, Hardware, NISQ, and Error Correction.


  The Google Quantum AI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Quantum AI''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, training material, engineering blog, and 48 more developer resources.'
plans:
- name: Google Quantum Ai Plans Pricing
  plan_count: 3
  slug: google-quantum-ai-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Google Quantum Ai Rate Limits
  slug: google-quantum-ai-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Quantum AI API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-quantum-ai-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Google Quantum AI API Rules
  rule_count: 9
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 4
  slug: google-quantum-ai-rules
scopes:
- name: Google Quantum Ai Scopes
  scope_count: 1
  slug: google-quantum-ai-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 59.3
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 13.6
    contract_quality: 69.4
    developer_ergonomics: 71.4
    discoverability: 64.8
    governance: 13.6
    operational_transparency: 36.8
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-quantum-ai/refs/heads/main/screenshots/google-quantum-ai-2026-06-20T182227.png
security:
- kind: authentication
  name: Google Quantum Ai Authentication
  slug: google-quantum-ai-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Quantum Ai Domain Security
  slug: google-quantum-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: google-quantum-ai
tags:
- Quantum Computing
- Quantum
- Hardware
- NISQ
- Error Correction
- Willow
- Sycamore
- Cirq
- Quantum Engine
- Superconducting Qubits
- Google Cloud
website: https://quantumai.google/
---
