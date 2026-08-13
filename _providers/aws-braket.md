---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.2
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Aws Braket Agentic Access
  operation_count: 17
  slug: aws-braket-agentic-access
  summary_line: 17 operations · 13 acting
api_count: 5
apis:
- description: Discover the QPU and simulator devices available on Amazon Braket. Returns device ARN, provider (AQT, IonQ, IQM, QuEra, Rigetti, Amazon), status (ONLINE/OFFLINE/RETIRED), queue depth, paradigm (gate-b
  name: AWS Braket Devices API
  slug: aws-braket-devices-api
- description: Tag quantum tasks, hybrid jobs, and spending limits for cost allocation, IAM ABAC, and resource organization. Tags propagate to AWS Cost Explorer and AWS Budgets and can be referenced in IAM condition
  name: AWS Braket Tags API
  slug: aws-braket-tags-api
- description: Hybrid quantum-classical job orchestration.
  name: AWS Braket HybridJobs API
  slug: aws-braket-hybridjobs-api
- description: Submit and manage quantum task executions on Amazon Braket devices.
  name: AWS Braket QuantumTasks API
  slug: aws-braket-quantumtasks-api
- description: Per-device opt-in cost controls for QPU tasks.
  name: AWS Braket SpendingLimits API
  slug: aws-braket-spendinglimits-api
artifact_total: 51
collections:
- collection_type: postman
  name: AWS Braket Devices API
  slug: postman-aws-braket-devices-api
- collection_type: postman
  name: AWS Braket Devices HybridJobs API
  slug: postman-aws-braket-hybridjobs-api
- collection_type: postman
  name: AWS Braket Devices QuantumTasks API
  slug: postman-aws-braket-quantumtasks-api
- collection_type: postman
  name: AWS Braket Devices SpendingLimits API
  slug: postman-aws-braket-spendinglimits-api
- collection_type: postman
  name: AWS Braket Devices Tags API
  slug: postman-aws-braket-tags-api
- collection_type: open
  name: AWS Braket Devices API
  slug: open-aws-braket-devices-api
- collection_type: open
  name: AWS Braket Hybrid Jobs API
  slug: open-aws-braket-hybrid-jobs-api
- collection_type: open
  name: AWS Braket Quantum Tasks API
  slug: open-aws-braket-quantum-tasks-api
- collection_type: open
  name: AWS Braket Spending Limits API
  slug: open-aws-braket-spending-limits-api
- collection_type: open
  name: AWS Braket Tags API
  slug: open-aws-braket-tags-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/aws-braket/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-braket-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-braket-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-braket-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-braket-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-braket-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/braket/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/braket/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/braket/latest/developerguide/what-is-braket.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/braket/latest/APIReference/Welcome.html
- group: other
  title: ''
  type: Regions
  url: https://docs.aws.amazon.com/braket/latest/developerguide/braket-devices.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/braket/latest/developerguide/braket-references.html
- group: docs
  title: ''
  type: Documentation
  url: https://aws.amazon.com/braket/quantum-computers/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/braket/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/braket/latest/developerguide/braket-pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/quantum-computing/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/amazon-braket
- group: build
  title: ''
  type: SDKs
  url: https://github.com/amazon-braket/amazon-braket-sdk-python
- group: docs
  title: ''
  type: Documentation
  url: https://amazon-braket-sdk-python.readthedocs.io/en/latest/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/amazon-braket/amazon-braket-schemas-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/amazon-braket/amazon-braket-default-simulator-python
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/amazon-braket/amazon-braket-examples
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/amazon-braket/amazon-braket-algorithm-library
- group: build
  title: ''
  type: Plugins
  url: https://github.com/amazon-braket/amazon-braket-pennylane-plugin-python
- group: build
  title: ''
  type: Plugins
  url: https://github.com/amazon-braket/qiskit-braket-provider
- group: build
  title: ''
  type: SDKs
  url: https://github.com/amazon-braket/Braket.jl
- group: build
  title: ''
  type: SDKs
  url: https://github.com/amazon-braket/autoqasm
- group: build
  title: ''
  type: Tools
  url: https://github.com/amazon-braket/amazon-braket-containers
- group: build
  title: ''
  type: SDKs
  url: https://docs.aws.amazon.com/cli/latest/reference/braket/
- group: build
  title: ''
  type: SDKs
  url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/braket.html
- group: build
  title: ''
  type: SDKs
  url: https://docs.aws.amazon.com/sdkfornet/v3/apidocs/items/Braket/NBraket.html
- group: build
  title: ''
  type: SDKs
  url: https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/services/braket/package-summary.html
- group: build
  title: ''
  type: SDKs
  url: https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/Braket.html
- group: build
  title: ''
  type: SDKs
  url: https://docs.aws.amazon.com/sdk-for-go/api/service/braket/
- group: build
  title: ''
  type: SDKs
  url: https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Braket.BraketClient.html
- group: build
  title: ''
  type: SDKs
  url: https://docs.aws.amazon.com/sdk-for-ruby/v3/api/Aws/Braket.html
- group: build
  title: ''
  type: SDKs
  url: https://sdk.amazonaws.com/cpp/api/LATEST/namespace_aws_1_1_braket.html
- group: docs
  title: ''
  type: Documentation
  url: https://openqasm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://pennylane.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonbraket.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: commercial
  title: ''
  type: Plans
  url: plans/aws-braket-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aws-braket-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/aws-braket-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aws-braket-vocabulary.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/aws-braket-rules.yml
created: '2026-05-25T00:00:00.000Z'
description: Amazon Braket is AWS's fully managed quantum computing service. It provides a unified API and SDK for exploring, designing, simulating, and running quantum algorithms across a single point of access to multiple third-party QPU technologies (trapped-ion, superconducting, neutral-atom) and AWS-managed cloud simulators. Braket handles device queueing, S3-backed result delivery, IAM, hybrid quantum-classical job orchestration, Braket Direct reservations, and opt-in spending limits, with native PennyLane, Qiskit, and OpenQASM 3 support.
examples:
- key_count: 2
  name: Aws Braket Create Hybrid Job Example
  slug: aws-braket-create-hybrid-job-example
- key_count: 2
  name: Aws Braket Create Quantum Task Example
  slug: aws-braket-create-quantum-task-example
- key_count: 2
  name: Aws Braket Create Spending Limit Example
  slug: aws-braket-create-spending-limit-example
- key_count: 2
  name: Aws Braket Get Device Example
  slug: aws-braket-get-device-example
features:
- Unified API for quantum hardware from AQT, IonQ, IQM, QuEra, and Rigetti
- On-demand state-vector (SV1), density-matrix (DM1), and tensor-network (TN1) cloud simulators
- Local simulators (braket_sv, braket_dm, braket_ahs) bundled in the Python SDK
- Hybrid Jobs — container-based orchestrator for variational algorithms with priority device access
- OpenQASM 3.0 program ingestion plus ProgramSet (multi-input parameter sweep) and AHS programs
- Pulse-level control via the experimentalCapabilities task field on supported devices
- Spending Limits API for opt-in per-device cost gating at CreateQuantumTask time
- Near-real-time cost tracking via braket.tracking.Tracker in the Python SDK
- Braket Direct reservations for dedicated QPU time blocks at fixed hourly rates
- PennyLane integration for quantum machine learning and variational workflows
- Qiskit-Braket provider lets Qiskit programs target Braket devices
- AutoQASM imperative quantum DSL embedded in Python
- Braket.jl experimental Julia SDK
- Available in us-east-1, us-west-1, us-west-2, eu-north-1, eu-west-2
- AWS SigV4 authentication and full IAM integration including ABAC via resource tags
- CloudWatch metrics and S3-based result delivery
- 12-month free tier with one simulator hour per month
finops:
- name: Aws Braket Finops
  service_category: Quantum Computing
  slug: aws-braket-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-braket.png
json_schemas:
- name: AWS Braket Device
  property_count: 7
  slug: aws-braket-device
- name: AWS Braket Hybrid Job
  property_count: 18
  slug: aws-braket-hybrid-job
- name: AWS Braket Quantum Task
  property_count: 0
  slug: aws-braket-quantum-task
json_structures:
- name: Aws Braket Quantum Task Structure
  property_count: 0
  slug: aws-braket-quantum-task-structure
jsonld:
- class_count: 0
  name: Aws Braket Context
  property_count: 4
  slug: aws-braket-context
layout: provider
modified: '2026-05-25'
name: AWS Braket
nav: Providers
network: true
overview: 'AWS Braket publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Devices API, Tags API, HybridJobs API, and 2 more. Tagged areas include Quantum Computing, QPU, Simulator, Hybrid Jobs, and OpenQASM.


  The AWS Braket catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AWS Braket''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, signup flow, and 42 more developer resources.'
plans:
- name: Aws Braket Plans Pricing
  plan_count: 5
  slug: aws-braket-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 0
  name: Aws Braket Rate Limits
  slug: aws-braket-rate-limits
rules:
- name: AWS Braket API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aws-braket-jsonschema-spectral-rules
- name: AWS Braket API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 3
  slug: aws-braket-rules
score:
  band: exemplar
  composite: 66.1
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 72.1
    developer_ergonomics: 60.9
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 66.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-braket/refs/heads/main/screenshots/aws-braket-2026-06-20T172752.png
security:
- kind: authentication
  name: Aws Braket Authentication
  slug: aws-braket-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws Braket Domain Security
  slug: aws-braket-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws Braket Vulnerability Disclosure
  slug: aws-braket-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws Braket Trust Center
  slug: aws-braket-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-braket
tags:
- Quantum Computing
- QPU
- Simulator
- Hybrid Jobs
- OpenQASM
- PennyLane
- Qiskit
- Quantum
website: https://aws.amazon.com/braket/
---
