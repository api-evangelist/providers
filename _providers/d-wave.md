---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: D Wave Agentic Access
  operation_count: 17
  slug: d-wave-agentic-access
  summary_line: 17 operations · 5 acting
api_count: 4
apis:
- baseURL: https://cloud.dwavesys.com/sapi/v2
  baseurl_source: declared
  description: The Account API from D-Wave — 3 operation(s) for account.
  name: D-Wave Account API
  slug: d-wave-account-api
- baseURL: https://cloud.dwavesys.com/sapi/v2
  baseurl_source: declared
  description: The Hybrid API from D-Wave — 1 operation(s) for hybrid.
  name: D-Wave Hybrid API
  slug: d-wave-hybrid-api
- baseURL: https://cloud.dwavesys.com/sapi/v2
  baseurl_source: declared
  description: The QPU API from D-Wave — 1 operation(s) for qpu.
  name: D-Wave QPU API
  slug: d-wave-qpu-api
- baseURL: https://cloud.dwavesys.com/sapi/v2
  baseurl_source: declared
  description: The Regions API from D-Wave — 2 operation(s) for regions.
  name: D-Wave Regions API
  slug: d-wave-regions-api
artifact_total: 76
collections:
- collection_type: postman
  name: D-Wave Leap Hybrid Solvers Account API
  slug: postman-d-wave-account-api
- collection_type: postman
  name: D-Wave Leap Solvers Account Hybrid API
  slug: postman-d-wave-hybrid-api
- collection_type: postman
  name: D-Wave Leap Hybrid Solvers Account Problems API
  slug: postman-d-wave-problems-api
- collection_type: postman
  name: D-Wave Leap Hybrid Solvers Account QPU API
  slug: postman-d-wave-qpu-api
- collection_type: postman
  name: D-Wave Leap Hybrid Solvers Account Regions API
  slug: postman-d-wave-regions-api
- collection_type: postman
  name: D-Wave Leap Hybrid Account Solvers API
  slug: postman-d-wave-solvers-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: D-Wave Leap Hybrid Solvers Account API
  slug: open-d-wave-account-api
- collection_type: open
  name: D-Wave Leap Solvers Account Hybrid API
  slug: open-d-wave-hybrid-api
- collection_type: open
  name: D-Wave Leap Hybrid Solvers
  slug: open-d-wave-hybrid-solvers
- collection_type: open
  name: D-Wave Leap Account API
  slug: open-d-wave-leap-account-api
- collection_type: open
  name: D-Wave Metadata API
  slug: open-d-wave-metadata-api
- collection_type: open
  name: D-Wave Leap Hybrid Solvers Account Problems API
  slug: open-d-wave-problems-api
- collection_type: open
  name: D-Wave Leap Hybrid Solvers Account QPU API
  slug: open-d-wave-qpu-api
- collection_type: open
  name: D-Wave QPU Samplers (Advantage / Advantage2)
  slug: open-d-wave-qpu-samplers
- collection_type: open
  name: D-Wave Leap Hybrid Solvers Account Regions API
  slug: open-d-wave-regions-api
- collection_type: open
  name: D-Wave Leap Hybrid Account Solvers API
  slug: open-d-wave-solvers-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/d-wave/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/d-wave-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/d-wave-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/d-wave-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/d-wave-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://www.dwavequantum.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dwavequantum.com/en/latest/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dwavequantum.com/en/industrial_optimization/index_get_started.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dwavequantum.com/en/quantum_research/index_get_started.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dwavequantum.com/en/concepts/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dwavequantum.com/build/getting-started/
- group: start
  title: ''
  type: Signup
  url: https://www.dwavequantum.com/get-started-with-d-wave/
- group: start
  title: ''
  type: Signup
  url: https://cloud.dwavesys.com/leap/signup/
- group: start
  title: ''
  type: Sandbox
  url: https://cloud.dwavesys.com/leap/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dwavesystems
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dwave-examples
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dwave-ocean-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dwave-cloud-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dwave-system
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dimod
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dwave-hybrid
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dwave-samplers
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dwave-optimization
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dwave-neal
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dwave-tabu
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dwave-greedy
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dwave-preprocessing
- group: build
  title: ''
  type: Tools
  url: https://github.com/dwavesystems/dwave-inspector
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/minorminer
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dwave-graphs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/dwave-gate
- group: build
  title: ''
  type: SDKs
  url: https://github.com/dwavesystems/penaltymodel
- group: build
  title: ''
  type: Plugins
  url: https://github.com/dwavesystems/dwave-pytorch-plugin
- group: build
  title: ''
  type: Plugins
  url: https://github.com/dwavesystems/dwave-scikit-learn-plugin
- group: build
  title: ''
  type: Plugins
  url: https://github.com/dwavesystems/dwave-qiskit-plugin
- group: build
  title: ''
  type: Tools
  url: https://github.com/dwavesystems/ocean-docker
- group: build
  title: ''
  type: Tools
  url: https://github.com/dwavesystems/ocean-devcontainer
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/dwavesystems/leapide-docs
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dwave-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dwave-examples/template
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dwave-examples/simple-ocean-programs
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dwave-examples/hybrid-computing-notebook
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dwave-examples/pegasus-notebook
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dwave-examples/reverse-annealing-notebook
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dwave-examples/factoring-notebook
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/dwave-examples/feature-selection-notebook
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/dwave-ocean-sdk/
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/dwave-cloud-client/
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/dwave-system/
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/dimod/
- group: start
  title: ''
  type: Portal
  url: https://www.dwavequantum.com/solutions-and-products/cloud-platform/
- group: start
  title: ''
  type: Portal
  url: https://www.dwavequantum.com/solutions-and-products/systems/
- group: start
  title: ''
  type: Portal
  url: https://www.dwavequantum.com/solutions-and-products/professional-services/
- group: company
  title: ''
  type: Blog
  url: https://www.dwavequantum.com/learn/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dwavequantum.com/learn/resource-library/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dwavequantum.com/learn/featured-applications/
- group: operate
  title: ''
  type: Forums
  url: https://support.dwavesys.com/hc/en-us/community/topics
- group: operate
  title: ''
  type: Support
  url: https://support.dwavesys.com/hc/en-us
- group: operate
  title: ''
  type: Support
  url: https://www.dwavequantum.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dwavequantum.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dwavequantum.com/legal/terms/
- group: docs
  title: ''
  type: Documentation
  url: https://www.dwavequantum.com/legal/patent-notice/
- group: docs
  title: ''
  type: Documentation
  url: https://investor.dwavequantum.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/d-wave-systems
- group: company
  title: ''
  type: Twitter
  url: https://x.com/dwavequantum
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@dwavequantum
- group: commercial
  title: ''
  type: Plans
  url: https://plans/d-wave-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://rate-limits/d-wave-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://finops/d-wave-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/d-wave-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/d-wave-rules.yml
created: '2026-05-25T00:00:00.000Z'
description: 'D-Wave Quantum Inc. (NYSE: QBTS) is the leader in commercial quantum annealing computing and developer of the Advantage and Advantage2 quantum systems. D-Wave''s Leap quantum cloud service provides real-time access to D-Wave QPUs and to the Leap hybrid solver family (BQM, CQM, DQM, NL) capable of solving industrial optimization problems with up to ~2 million variables and constraints. The open-source Ocean SDK — dimod, dwave-system, dwave-cloud-client, dwave-hybrid, dwave-samplers, dwave-optimization, minorminer, dwave-inspector, and 40+ companion packages — provides the canonical developer experience, with the underlying Solver API (SAPI) exposed as a versioned REST interface for solver discovery, problem submission, status polling, answer retrieval, and cancellation. Companion APIs include the Metadata API for region discovery and the Leap Account API for OAuth-based project and token management.'
examples:
- key_count: 2
  name: D Wave Cqm Problem Example
  slug: d-wave-cqm-problem-example
- key_count: 2
  name: D Wave Leap Projects Example
  slug: d-wave-leap-projects-example
- key_count: 2
  name: D Wave List Regions Example
  slug: d-wave-list-regions-example
- key_count: 2
  name: D Wave List Solvers Example
  slug: d-wave-list-solvers-example
- key_count: 2
  name: D Wave Problem Status Example
  slug: d-wave-problem-status-example
- key_count: 2
  name: D Wave Qpu Ising Example
  slug: d-wave-qpu-ising-example
- key_count: 2
  name: D Wave Submit Problem Example
  slug: d-wave-submit-problem-example
features:
- Advantage2 — next-generation annealing quantum computer with Zephyr topology and improved coherence
- Advantage — 5,000+ qubit Pegasus-topology annealing QPU available via Leap cloud
- Leap quantum cloud service — real-time access, 99.9% uptime, subsecond response for many workloads
- Hybrid solvers — BQM, CQM, DQM, NL families supporting up to ~2 million variables and constraints
- NL (Nonlinear) solver — flagship Industrial Optimization solver for general nonlinear formulations
- CQM (Constrained Quadratic Model) solver — equality and inequality constraints, mixed integer support
- Direct QPU access — Ising / QUBO sampling with annealing schedule, num_reads, reverse annealing, h_gain
- Solver API (SAPI) — REST interface for solver discovery, problem submission, status, answer retrieval
- Metadata API — region discovery for routing to correct regional SAPI cluster (na-west, eu-central, etc.)
- Leap Account API — OAuth-based project listing and SAPI token retrieval
- Ocean SDK — Python open-source SDK covering dimod, dwave-system, dwave-cloud-client, hybrid, samplers
- dwave-cloud-client — low-level SAPI REST client; submit_problem, list_solvers, regions, account
- dimod — shared API and data model for QUBO / Ising / CQM / DQM / NL samplers
- dwave-system — DWaveSampler, EmbeddingComposite, LeapHybridSampler family for application code
- dwave-hybrid — asynchronous decomposition framework for building hybrid quantum-classical workflows
- dwave-samplers / dwave-neal / dwave-tabu / dwave-greedy — classical reference solvers and baselines
- dwave-optimization — C++ engine for nonlinear models powering the NL solver workflow
- dwave-preprocessing — common BQM preprocessing techniques (roof duality, fix variables, scale, normalize)
- dwave-inspector — interactive problem inspector for visualizing embeddings and chains
- minorminer — heuristic minor-embedding from logical to physical qubit graph (Pegasus / Zephyr / Chimera)
- dwave-graphs — Chimera, Pegasus, and Zephyr graph generators and algorithms
- dwave-gate — gate-model quantum circuit construction and state-vector simulator
- PyTorch plugin — quantum-classical hybrid ML with PyTorch
- scikit-learn plugin — quantum-classical hybrid solving plugged into scikit-learn pipelines
- Qiskit plugin — D-Wave Ocean plugin for IBM Qiskit interoperability
- Leap IDE — browser-based Jupyter / VS Code environment preconfigured for Ocean development
- 60+ reference applications at github.com/dwave-examples (scheduling, routing, packing, ML, finance, science)
- Five problem types — ising, qubo, bqm, cqm, dqm, nl — with qp / bq / ref encoding formats
- Problem lifecycle — PENDING > IN_PROGRESS > COMPLETED | FAILED | CANCELLED with bulk status polling
- Binary-ref answer downloads using SAPI-token auth for large hybrid answers
- Versioned vendor media types (`application/vnd.dwave.sapi.*+json;version~=3.0`) for API evolution
- D-Wave Launch Program — professional services for quantum onboarding
- Publicly traded as NYSE: QBTS
finops:
- name: D Wave Finops
  service_category: ''
  slug: d-wave-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/d-wave.png
json_schemas:
- name: D-Wave Constrained Quadratic Model (CQM)
  property_count: 3
  slug: d-wave-cqm-model
- name: D-Wave Problem Answer
  property_count: 9
  slug: d-wave-problem-answer
- name: D-Wave Problem Job
  property_count: 5
  slug: d-wave-problem
- name: D-Wave QPU Properties
  property_count: 16
  slug: d-wave-qpu-properties
- name: D-Wave Solver Configuration
  property_count: 5
  slug: d-wave-solver-configuration
jsonld:
- class_count: 36
  name: D Wave Context
  property_count: 0
  slug: d-wave-context
layout: provider
modified: '2026-05-25'
name: D-Wave
nav: Providers
network: true
overview: 'D-Wave publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Hybrid API, QPU API, and 1 more. Tagged areas include Quantum Computing, Quantum Annealing, Optimization, Hybrid Quantum-Classical, and Ising.


  The D-Wave catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  D-Wave''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, sandbox, tooling, and 64 more developer resources.'
plans:
- name: D Wave Plans Pricing
  plan_count: 3
  slug: d-wave-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: D Wave Rate Limits
  slug: d-wave-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: D-Wave API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: d-wave-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: D-Wave API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 6
  slug: d-wave-rules
scopes:
- name: D Wave Scopes
  scope_count: 1
  slug: d-wave-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 62.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 94.5
    catalog_earned_first_party: 0.0
    catalog_gap: 20.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 28.8
    contract_quality: 67.7
    developer_ergonomics: 75.0
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 36.8
  previous_composite: 62.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/d-wave/refs/heads/main/screenshots/d-wave-2026-06-20T175418.png
security:
- kind: authentication
  name: D Wave Authentication
  slug: d-wave-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: D Wave Domain Security
  slug: d-wave-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: d-wave
tags:
- Quantum Computing
- Quantum Annealing
- Optimization
- Hybrid Quantum-Classical
- Ising
- QUBO
- Industrial Optimization
- Sampling
- Leap
- Ocean SDK
- SAPI
website: https://www.dwavequantum.com
---
