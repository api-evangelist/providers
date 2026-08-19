---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Microsoft Quantum Agentic Access
  operation_count: 27
  slug: microsoft-quantum-agentic-access
  summary_line: 27 operations · 13 acting
api_count: 8
apis:
- description: Q# is Microsoft's open-source, hardware-agnostic quantum programming language. The Modern QDK compiler is written in Rust, ships as a VS Code extension and Python package, and powers quantum.microsoft
  name: Q# Quantum Programming Language
  slug: qsharp-language
- description: Open-source post-layout physical resource estimator for fault-tolerant quantum algorithms. Compute qubit counts, T-state counts, runtime, and code-distance requirements across configurable qubit physi
  name: Microsoft Quantum Resource Estimator
  slug: resource-estimator
- description: Python SDK for submitting jobs to Azure Quantum. Supports Q#, Qiskit, Cirq, and pass-through provider input formats; manages workspaces, jobs, sessions, and target queries against the Workspace data-p
  name: Azure Quantum Python SDK
  slug: azure-quantum-python-sdk
- description: The Offerings API from Microsoft Azure Quantum — 1 operation(s) for offerings.
  name: Microsoft Azure Quantum Offerings API
  slug: microsoft-quantum-offerings-api
- description: The Operations API from Microsoft Azure Quantum — 1 operation(s) for operations.
  name: Microsoft Azure Quantum Operations API
  slug: microsoft-quantum-operations-api
- description: The Subscriptions API from Microsoft Azure Quantum — 12 operation(s) for subscriptions.
  name: Microsoft Azure Quantum Subscriptions API
  slug: microsoft-quantum-subscriptions-api
- description: The SuiteOffers API from Microsoft Azure Quantum — 1 operation(s) for suiteoffers.
  name: Microsoft Azure Quantum SuiteOffers API
  slug: microsoft-quantum-suiteoffers-api
- description: The Workspaces API from Microsoft Azure Quantum — 6 operation(s) for workspaces.
  name: Microsoft Azure Quantum Workspaces API
  slug: microsoft-quantum-workspaces-api
arazzos:
- description: Look up a job, branch on whether it is still running, cancel it, and confirm cancellation.
  name: Azure Quantum Cancel a Running Job
  slug: microsoft-quantum-cancel-running-job-workflow
- description: List provider statuses in a workspace and branch on availability before selecting a target.
  name: Azure Quantum Discover an Available Target
  slug: microsoft-quantum-discover-available-target-workflow
- description: List workspace quotas, branch on remaining headroom, and stage storage when capacity exists.
  name: Azure Quantum Quota Capacity Check
  slug: microsoft-quantum-quota-capacity-check-workflow
- description: Open a session, submit a job into it, list its jobs, then close the session.
  name: Azure Quantum Session Lifecycle
  slug: microsoft-quantum-session-lifecycle-workflow
- description: Stage input, create a quantum job, poll it to a terminal state, and read the output URI.
  name: Azure Quantum Submit Job and Retrieve Results
  slug: microsoft-quantum-submit-job-poll-results-workflow
- description: Read a workspace, branch on provisioning state, list its keys, and list provider offerings.
  name: Azure Quantum Workspace Bootstrap
  slug: microsoft-quantum-workspace-bootstrap-workflow
artifact_total: 54
collections:
- collection_type: postman
  name: Azure Quantum Workspace Services
  slug: postman-azure-quantum-data-plane-openapi
- collection_type: postman
  name: Azure Quantum Management API
  slug: postman-azure-quantum-resource-manager-openapi
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Quantum Workspace Services
  slug: open-azure-quantum-data-plane
- collection_type: open
  name: Azure Quantum Management API
  slug: open-azure-quantum-resource-manager
- collection_type: open
  name: Azure Quantum Workspace Services Offerings API
  slug: open-microsoft-quantum-offerings-api
- collection_type: open
  name: Azure Quantum Workspace Services Offerings Operations API
  slug: open-microsoft-quantum-operations-api
- collection_type: open
  name: Azure Quantum Workspace Services Offerings Subscriptions API
  slug: open-microsoft-quantum-subscriptions-api
- collection_type: open
  name: Azure Quantum Workspace Services Offerings SuiteOffers API
  slug: open-microsoft-quantum-suiteoffers-api
- collection_type: open
  name: Azure Quantum Workspace Services Offerings Workspaces API
  slug: open-microsoft-quantum-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-quantum-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-quantum-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-quantum-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-quantum-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-quantum-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-azure-quantum/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-quantum-cancel-running-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-quantum-discover-available-target-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-quantum-quota-capacity-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-quantum-session-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-quantum-submit-job-poll-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-quantum-workspace-bootstrap-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://quantum.microsoft.com/
- group: start
  title: ''
  type: Portal
  url: https://azure.microsoft.com/en-us/products/quantum
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/quantum/overview-azure-quantum
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/quantum/install-overview-qdk
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/quantum/qsharp-quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/rest/api/azurequantum/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/qc-target-list
- group: other
  title: ''
  type: Regions
  url: https://learn.microsoft.com/en-us/azure/quantum/provider-global-availability
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/quantum/release-notes
- group: commercial
  title: ''
  type: Pricing
  url: https://learn.microsoft.com/en-us/azure/quantum/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/azure-quantum-job-cost-billing
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/quantum/how-to-create-workspace
- group: start
  title: ''
  type: Signup
  url: https://ms.portal.azure.com/#create/Microsoft.AzureQuantum
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/free/students/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/credits
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.microsoft.com/en-us/trust-center
- group: commercial
  title: ''
  type: TermsOfService
  url: https://learn.microsoft.com/en-us/legal/azure-quantum/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: company
  title: ''
  type: Blog
  url: https://cloudblogs.microsoft.com/quantum/
- group: docs
  title: ''
  type: Documentation
  url: https://www.microsoft.com/research/research-area/quantum-computing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/MicrosoftDocs/quantum-docs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/qdk
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/qsharp-language
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/qsharp-compiler
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/qsharp-runtime
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/microsoft/QuantumLibraries
- group: build
  title: ''
  type: SDKs
  url: https://github.com/microsoft/azure-quantum-python
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/azure-quantum/
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/qsharp/
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/microsoft/Quantum
- group: learn
  title: ''
  type: Courses
  url: https://github.com/microsoft/QuantumKatas
- group: learn
  title: ''
  type: Courses
  url: https://github.com/microsoft/quantum-curriculum-samples
- group: build
  title: ''
  type: Tools
  url: https://github.com/microsoft/iqsharp
- group: build
  title: ''
  type: Tools
  url: https://github.com/microsoft/quantum-viz.js
- group: build
  title: ''
  type: Tools
  url: https://github.com/microsoft/qdk-chemistry
- group: build
  title: ''
  type: Tools
  url: https://github.com/microsoft/Quantum-NC
- group: build
  title: ''
  type: Tools
  url: https://github.com/microsoft/qmt
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/quantum
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/install-command-line-qdk
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/paths/quantum-computing-fundamentals/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/hybrid-computing-overview
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/intro-to-resource-estimation
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/quantum/quickstart-microsoft-resources-estimator
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/qsharp-overview
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/qsharp/api/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/provider-ionq
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/provider-quantinuum
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/provider-pasqal
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/provider-rigetti
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/quantum/get-started-azure-quantum
- group: operate
  title: ''
  type: Forums
  url: https://learn.microsoft.com/en-us/answers/tags/3/azure-quantum
- group: commercial
  title: ''
  type: Plans
  url: plans/microsoft-quantum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-quantum-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/microsoft-quantum-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Microsoft Azure Quantum is Microsoft's cloud quantum computing service — an open, multi-vendor platform that provides access to quantum hardware from IonQ, Quantinuum, Pasqal, and Rigetti alongside Microsoft's own Q# programming language, Quantum Development Kit (QDK), and post-layout fault-tolerant Resource Estimator. The Azure Quantum Workspace REST API exposes jobs, sessions, providers, quotas, items, and storage surfaces; the Microsoft.Quantum ARM provider handles workspace provisioning. The QDK is free and open source, ships as a VS Code extension and Python package, and supports Q#, Qiskit, Cirq, and OpenQASM. Azure Quantum Elements layers in chemistry, materials, and HPC simulation for scientific discovery, with Copilot-assisted workflows on quantum.microsoft.com.
examples:
- key_count: 3
  name: Azure Quantum Provider Status Example
  slug: azure-quantum-provider-status-example
- key_count: 3
  name: Azure Quantum Submit Job Example
  slug: azure-quantum-submit-job-example
features:
- Azure Quantum Workspace — managed cloud control plane for submitting and tracking quantum jobs across multiple hardware providers
- Q# programming language — open-source, hardware-agnostic quantum DSL with a modern Rust-based compiler
- Microsoft Quantum Development Kit (QDK) — free, open-source SDK with VS Code extension, Python package, Jupyter widgets, and language service
- Microsoft Quantum Resource Estimator — fault-tolerant resource estimation with configurable qubit parameters, QEC codes, and error budgets
- Multi-provider hardware access — IonQ (trapped ion, 25–36 qubits), Quantinuum (trapped ion, H2 series 20–32 qubits), Pasqal (neutral atom, 100 qubits), Rigetti (superconducting, 108 qubits)
- Built-in support for Qiskit, Cirq, OpenQASM in addition to Q#
- Sessions API for low-latency hybrid quantum-classical workflows
- Azure Quantum Credits program — USD 500 in free provider credits for new workspaces
- Azure Quantum Elements — chemistry, materials, and HPC simulation stack (Generative Chemistry, Accelerated DFT) integrated with the quantum platform
- Copilot in Microsoft Quantum — AI-assisted Q# code generation and chemistry workflows on quantum.microsoft.com
- Azure CLI `az quantum` extension for workspace and job management from the terminal
- ARM resource manager API for Infrastructure-as-Code provisioning
- Storage SAS URI delegation for direct blob upload of job inputs/outputs
- TypeSpec-defined OpenAPI specs published to Azure/azure-rest-api-specs
- Azure-native integrations (RBAC, Entra ID, Storage, Monitor) and per-region provider availability
finops:
- name: Microsoft Quantum Finops
  service_category: Quantum Computing
  slug: microsoft-quantum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-quantum.png
json_schemas:
- name: AzureQuantumJob
  property_count: 21
  slug: azure-quantum-job
- name: AzureQuantumProviderStatus
  property_count: 3
  slug: azure-quantum-provider-status
- name: AzureQuantumSession
  property_count: 11
  slug: azure-quantum-session
jsonld:
- class_count: 0
  name: Microsoft Quantum Context
  property_count: 7
  slug: microsoft-quantum-context
layout: provider
modified: '2026-05-25'
name: Microsoft Azure Quantum
nav: Providers
network: true
overview: 'Microsoft Azure Quantum publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Offerings API, Operations API, Subscriptions API, and 2 more. Tagged areas include Quantum, Quantum Computing, Azure, Microsoft, and Q#.


  The Microsoft Azure Quantum catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Azure Quantum''s developer surface includes authentication, developer portal, documentation, getting-started guide, changelog, pricing, signup flow, and 65 more developer resources.'
plans:
- name: Microsoft Quantum Plans Pricing
  plan_count: 9
  slug: microsoft-quantum-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 8
  name: Microsoft Quantum Rate Limits
  slug: microsoft-quantum-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Microsoft Azure Quantum API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-quantum-jsonschema-spectral-rules
scopes:
- name: Microsoft Quantum Scopes
  scope_count: 2
  slug: microsoft-quantum-scopes
  summary_line: 2 scopes · clientCredentials/implicit
score:
  band: strong
  composite: 62.3
  delta: -5.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 9.8
    contract_quality: 52.3
    developer_ergonomics: 71.4
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 68.4
  previous_composite: 67.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-quantum/refs/heads/main/screenshots/microsoft-quantum-2026-06-20T185529.png
security:
- kind: authentication
  name: Microsoft Quantum Authentication
  slug: microsoft-quantum-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Microsoft Quantum Domain Security
  slug: microsoft-quantum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Quantum Vulnerability Disclosure
  slug: microsoft-quantum-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-quantum
tags:
- Quantum
- Quantum Computing
- Azure
- Microsoft
- Q#
- QDK
- Resource Estimation
- IonQ
- Quantinuum
- Pasqal
- Rigetti
- Hybrid Quantum
- Fault Tolerance
website: https://quantum.microsoft.com/
---
