---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Ibm Quantum Agentic Access
  operation_count: 30
  slug: ibm-quantum-agentic-access
  summary_line: 30 operations · 8 acting
api_count: 6
apis:
- description: 'Premium / Flex-tier service for discovering and invoking abstracted Qiskit Functions — pre-packaged quantum-classical workflows (e.g. circuit cutting, error-mitigation pipelines) callable through the '
  name: Qiskit Functions Catalog API
  slug: qiskit-functions-catalog-api
- description: Cloud-hosted, AI-augmented transpilation of OpenQASM 3 circuits down to IBM Quantum native gates and backend topology. Bundled with Flex and Premium plans.
  name: Qiskit Transpiler as a Service API
  slug: qiskit-transpiler-as-a-service-api
- baseURL: https://quantum.cloud.ibm.com/api
  baseurl_source: spec
  description: The Accounts API from ibm-quantum — 1 operation(s) for accounts.
  name: ibm-quantum Accounts API
  slug: ibm-quantum-accounts-api
- baseURL: https://quantum.cloud.ibm.com/api
  baseurl_source: spec
  description: The Analytics API from ibm-quantum — 4 operation(s) for analytics.
  name: ibm-quantum Analytics API
  slug: ibm-quantum-analytics-api
- baseURL: https://quantum.cloud.ibm.com/api
  baseurl_source: spec
  description: The Backends API from ibm-quantum — 5 operation(s) for backends.
  name: ibm-quantum Backends API
  slug: ibm-quantum-backends-api
- baseURL: https://quantum.cloud.ibm.com/api
  baseurl_source: spec
  description: The Instances API from ibm-quantum — 3 operation(s) for instances.
  name: ibm-quantum Instances API
  slug: ibm-quantum-instances-api
- baseURL: https://quantum.cloud.ibm.com/api
  baseurl_source: spec
  description: The Jobs API from ibm-quantum — 7 operation(s) for jobs.
  name: ibm-quantum Jobs API
  slug: ibm-quantum-jobs-api
- baseURL: https://quantum.cloud.ibm.com/api
  baseurl_source: spec
  description: The Sessions API from ibm-quantum — 3 operation(s) for sessions.
  name: ibm-quantum Sessions API
  slug: ibm-quantum-sessions-api
- baseURL: https://quantum.cloud.ibm.com/api
  baseurl_source: spec
  description: The Tags API from ibm-quantum — 1 operation(s) for tags.
  name: ibm-quantum Tags API
  slug: ibm-quantum-tags-api
- baseURL: https://quantum.cloud.ibm.com/api
  baseurl_source: spec
  description: The Versions API from ibm-quantum — 1 operation(s) for versions.
  name: ibm-quantum Versions API
  slug: ibm-quantum-versions-api
- baseURL: https://quantum.cloud.ibm.com/api
  baseurl_source: spec
  description: The Workloads API from ibm-quantum — 1 operation(s) for workloads.
  name: ibm-quantum Workloads API
  slug: ibm-quantum-workloads-api
arazzos:
- description: List recent job-mode workloads from analytics, then pull the full job record and metrics for the most recent one.
  name: IBM Quantum Audit Workloads and Drill Into Job
  slug: ibm-quantum-audit-workloads-and-drill-into-job-workflow
- description: Verify a backend is online, then gather its calibration properties and pulse defaults for circuit transpilation.
  name: IBM Quantum Backend Readiness Preflight
  slug: ibm-quantum-backend-readiness-preflight-workflow
- description: Check a job's status and cancel it only if it is still queued or running.
  name: IBM Quantum Cancel Running Job
  slug: ibm-quantum-cancel-running-job-workflow
- description: Poll a job to completion, then retrieve both its result payload and its execution logs.
  name: IBM Quantum Job Results and Logs
  slug: ibm-quantum-job-results-and-logs-workflow
- description: List recent jobs, then pull the full details and execution metrics for the most recent one.
  name: IBM Quantum List Jobs and Inspect
  slug: ibm-quantum-list-jobs-and-inspect-workflow
- description: Discover the live API version, then list accessible backends and check one backend's status using that version.
  name: IBM Quantum Negotiate Version and List Backends
  slug: ibm-quantum-negotiate-version-and-list-backends-workflow
- description: Read a session's state, toggle whether it accepts new jobs, and confirm the change.
  name: IBM Quantum Pause Session and Confirm
  slug: ibm-quantum-pause-session-and-confirm-workflow
- description: List accessible backends, inspect a chosen backend's configuration, and submit a job to it.
  name: IBM Quantum Select Backend and Submit Job
  slug: ibm-quantum-select-backend-and-submit-job-workflow
- description: Open a Qiskit Runtime session, run a job inside it, then close the session.
  name: IBM Quantum Session Run and Close
  slug: ibm-quantum-session-run-and-close-workflow
- description: Submit a Qiskit Runtime primitive job, poll until it reaches a terminal state, and fetch the final result.
  name: IBM Quantum Submit Job and Poll Results
  slug: ibm-quantum-submit-job-and-poll-results-workflow
- description: Replace a job's tags, confirm the change on the job, and search the tag catalog for one of them.
  name: IBM Quantum Tag Job and Verify
  slug: ibm-quantum-tag-job-and-verify-workflow
- description: Check instance usage and remaining limit before submitting a job, skipping submission when the limit is reached.
  name: IBM Quantum Usage-Aware Job Submission
  slug: ibm-quantum-usage-aware-job-submission-workflow
artifact_total: 83
collections:
- collection_type: postman
  name: Qiskit Runtime Analytics API
  slug: postman-ibm-quantum-runtime-analytics
- collection_type: postman
  name: Qiskit Runtime Backends API
  slug: postman-ibm-quantum-runtime-backends
- collection_type: postman
  name: Qiskit Runtime Instances API
  slug: postman-ibm-quantum-runtime-instances
- collection_type: postman
  name: Qiskit Runtime Jobs API
  slug: postman-ibm-quantum-runtime-jobs
- collection_type: postman
  name: Qiskit Runtime Sessions API
  slug: postman-ibm-quantum-runtime-sessions
- collection_type: postman
  name: Qiskit Runtime Versions API
  slug: postman-ibm-quantum-runtime-versions
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qiskit Runtime Analytics Accounts API
  slug: open-ibm-quantum-accounts-api
- collection_type: open
  name: Qiskit Runtime Accounts Analytics API
  slug: open-ibm-quantum-analytics-api
- collection_type: open
  name: Qiskit Runtime Analytics Accounts Backends API
  slug: open-ibm-quantum-backends-api
- collection_type: open
  name: Qiskit Runtime Analytics Accounts Instances API
  slug: open-ibm-quantum-instances-api
- collection_type: open
  name: Qiskit Runtime Analytics Accounts Jobs API
  slug: open-ibm-quantum-jobs-api
- collection_type: open
  name: Qiskit Runtime Analytics API
  slug: open-ibm-quantum-runtime-analytics
- collection_type: open
  name: Qiskit Runtime Backends API
  slug: open-ibm-quantum-runtime-backends
- collection_type: open
  name: Qiskit Runtime Instances API
  slug: open-ibm-quantum-runtime-instances
- collection_type: open
  name: Qiskit Runtime Jobs API
  slug: open-ibm-quantum-runtime-jobs
- collection_type: open
  name: Qiskit Runtime Sessions API
  slug: open-ibm-quantum-runtime-sessions
- collection_type: open
  name: Qiskit Runtime Versions API
  slug: open-ibm-quantum-runtime-versions
- collection_type: open
  name: Qiskit Runtime Analytics Accounts Sessions API
  slug: open-ibm-quantum-sessions-api
- collection_type: open
  name: Qiskit Runtime Analytics Accounts Tags API
  slug: open-ibm-quantum-tags-api
- collection_type: open
  name: Qiskit Runtime Analytics Accounts Versions API
  slug: open-ibm-quantum-versions-api
- collection_type: open
  name: Qiskit Runtime Analytics Accounts Workloads API
  slug: open-ibm-quantum-workloads-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ibm-quantum-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ibm-quantum-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ibm-quantum-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ibm-quantum-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/ibm-quantum/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ibm-quantum-audit-workloads-and-drill-into-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ibm-quantum-backend-readiness-preflight-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ibm-quantum-cancel-running-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ibm-quantum-job-results-and-logs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ibm-quantum-list-jobs-and-inspect-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ibm-quantum-negotiate-version-and-list-backends-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ibm-quantum-pause-session-and-confirm-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ibm-quantum-select-backend-and-submit-job-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ibm-quantum-session-run-and-close-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ibm-quantum-submit-job-and-poll-results-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ibm-quantum-tag-job-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/ibm-quantum-usage-aware-job-submission-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.ibm.com/quantum
- group: start
  title: ''
  type: Portal
  url: https://quantum.cloud.ibm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://quantum.cloud.ibm.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://quantum.cloud.ibm.com/docs/api/qiskit-runtime-rest
- group: docs
  title: ''
  type: OpenAPI
  url: https://quantum.cloud.ibm.com/api/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://quantum.cloud.ibm.com/docs/en/guides/plans-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ibm.com/quantum/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.quantum.ibm.com/start
- group: start
  title: ''
  type: Sandbox
  url: https://quantum.cloud.ibm.com/composer
- group: learn
  title: ''
  type: Training
  url: https://quantum.cloud.ibm.com/learning
- group: operate
  title: ''
  type: Community
  url: https://www.ibm.com/quantum/network
- group: company
  title: ''
  type: Blog
  url: https://www.ibm.com/quantum/blog
- group: other
  title: ''
  type: Research
  url: https://research.ibm.com/quantum-computing
- group: operate
  title: ''
  type: StatusPage
  url: https://cloud.ibm.com/status
- group: start
  title: ''
  type: Signup
  url: https://cloud.ibm.com/registration
- group: auth
  title: ''
  type: Authentication
  url: https://www.ibm.com/cloud/iam
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ibm.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ibm.com/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.ibm.com/trust
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Qiskit
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qiskit-community
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Qiskit/qiskit
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Qiskit/qiskit-ibm-runtime
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Qiskit/qiskit-ibm-runtime-c
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Qiskit/qiskit-ibm-catalog
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Qiskit/qiskit-aer
- group: build
  title: ''
  type: Tools
  url: https://github.com/Qiskit/qiskit-serverless
- group: build
  title: ''
  type: Tools
  url: https://github.com/Qiskit/qiskit-fermions
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Qiskit/ecosystem
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/Qiskit/documentation
- group: build
  title: ''
  type: Package
  url: https://pypi.org/project/qiskit/
- group: build
  title: ''
  type: Package
  url: https://pypi.org/project/qiskit-ibm-runtime/
- group: operate
  title: ''
  type: Forums
  url: https://qisk.it/join-slack
- group: operate
  title: ''
  type: Forums
  url: https://stackoverflow.com/questions/tagged/qiskit
- group: commercial
  title: ''
  type: Plans
  url: plans/ibm-quantum-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ibm-quantum-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ibm-quantum-finops.yml
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/ibm-quantum-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ibm-quantum-vocabulary.yml
created: '2026-05-25'
description: IBM Quantum is IBM's quantum computing program — the operator of the IBM Quantum Platform (quantum.cloud.ibm.com), the publisher of the open-source Qiskit SDK, and the provider of the Qiskit Runtime REST API for submitting Sampler and Estimator primitive jobs to 100+ qubit Heron-generation QPUs and managed simulators. The platform combines an Apache-2.0 software stack (Qiskit, qiskit-ibm-runtime, qiskit-ibm-catalog, Qiskit Aer, Qiskit Serverless, Qiskit Functions) with a tiered access model (Open / Pay-As-You-Go / Flex / Premium / On-Premises) and is the longest-running commercial quantum computing API surface in the industry.
examples:
- key_count: 2
  name: Ibm Quantum Create Sampler Job Example
  slug: ibm-quantum-create-sampler-job-example
- key_count: 2
  name: Ibm Quantum Create Session Example
  slug: ibm-quantum-create-session-example
- key_count: 2
  name: Ibm Quantum List Backends Example
  slug: ibm-quantum-list-backends-example
features:
- 100+ qubit IBM Quantum processing units (Heron r2 generation) accessible via Qiskit Runtime
- Sampler primitive — circuit sampling for distribution-level results
- Estimator primitive — expectation value evaluation for observables
- Sessions for grouping primitive jobs with priority backend access
- Error suppression and mitigation (dynamical decoupling, ZNE, PEC, readout mitigation, noise-aware compilation)
- Qiskit SDK 2.x — open-source Python + Rust + C quantum circuit framework
- qiskit-ibm-runtime Python client for the REST API
- Qiskit C API for low-level integration in C/Rust applications
- Qiskit Functions — pre-packaged quantum-classical workflows on Flex and Premium
- Qiskit Transpiler as a Service — AI-augmented cloud transpilation
- Qiskit Serverless — distributed quantum + classical execution
- Qiskit Aer — high-performance noisy simulator
- IBM Quantum Composer — drag-and-drop circuit builder
- OpenQASM 2 and OpenQASM 3 program input
- Date-based API versioning via the IBM-API-Version header
- Global and EU-DE regional endpoints
- IBM Cloud IAM bearer authentication, Service-CRN per instance
- Five access plans — Open (free), Pay-As-You-Go, Flex, Premium, On-Premises
- 10 free minutes / 28-day rolling window on Open Plan, with an opt-in 180-minute / 12-month bonus
- Analytics endpoints for FinOps reporting per instance
- Apache 2.0 license across Qiskit core, qiskit-ibm-runtime, qiskit-ibm-catalog, ecosystem repos
- Active ecosystem registry of community Qiskit-compatible projects
finops:
- name: Ibm Quantum Finops
  service_category: ''
  slug: ibm-quantum-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ibm-quantum.png
json_schemas:
- name: IBM Quantum Backend
  property_count: 18
  slug: ibm-quantum-backend
- name: IBM Quantum Runtime Job
  property_count: 0
  slug: ibm-quantum-job
- name: IBM Quantum Runtime Session
  property_count: 13
  slug: ibm-quantum-session
jsonld:
- class_count: 0
  name: Ibm Quantum Context
  property_count: 8
  slug: ibm-quantum-context
layout: provider
modified: '2026-05-25'
name: IBM Quantum
nav: Providers
network: true
overview: 'IBM Quantum publishes 9 APIs on the [APIs.io](https://apis.io/) network, including ibm-quantum Accounts API, ibm-quantum Analytics API, ibm-quantum Backends API, and 6 more.


  The IBM Quantum catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  IBM Quantum''s developer surface includes authentication, developer portal, documentation, pricing, getting-started guide, sandbox, training material, and 49 more developer resources.'
plans:
- name: Ibm Quantum Plans Pricing
  plan_count: 5
  slug: ibm-quantum-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Ibm Quantum Rate Limits
  slug: ibm-quantum-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: IBM Quantum API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: ibm-quantum-jsonschema-spectral-rules
- effective_rule_count: 45
  extends:
  - spectral:oas
  name: IBM Quantum API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 2
  slug: ibm-quantum-rules
score:
  band: strong
  composite: 65.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 81.5
    catalog_earned_first_party: 0.0
    catalog_gap: 33.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 28.8
    contract_quality: 70.9
    developer_ergonomics: 65.5
    discoverability: 55.6
    governance: 28.8
    operational_transparency: 52.6
  previous_composite: 65.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    note: provider declares no identity tags; regime could not be determined
    undetermined: true
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ibm-quantum/refs/heads/main/screenshots/ibm-quantum-2026-06-20T183130.png
security:
- kind: authentication
  name: Ibm Quantum Authentication
  slug: ibm-quantum-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Ibm Quantum Domain Security
  slug: ibm-quantum-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ibm Quantum Vulnerability Disclosure
  slug: ibm-quantum-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: ibm-quantum
website: https://www.ibm.com/quantum
---
