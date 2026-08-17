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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Temporal Agentic Access
  operation_count: 19
  slug: temporal-agentic-access
  summary_line: 19 operations · 9 acting
api_count: 7
apis:
- description: The Temporal Server Frontend API provides gRPC services for interacting with the Temporal Server, including WorkflowService for managing workflow executions, OperatorService for cluster operations, an
  name: Temporal Server Frontend API
  slug: server-frontend-api
- description: The API Keys API from Temporal — 2 operation(s) for api keys.
  name: Temporal API Keys API
  slug: temporal-api-keys-api
- description: The Async Operations API from Temporal — 1 operation(s) for async operations.
  name: Temporal Async Operations API
  slug: temporal-async-operations-api
- description: The Namespaces API from Temporal — 3 operation(s) for namespaces.
  name: Temporal Namespaces API
  slug: temporal-namespaces-api
- description: The Regions API from Temporal — 1 operation(s) for regions.
  name: Temporal Regions API
  slug: temporal-regions-api
- description: The Service Accounts API from Temporal — 2 operation(s) for service accounts.
  name: Temporal Service Accounts API
  slug: temporal-service-accounts-api
- description: The Users API from Temporal — 2 operation(s) for users.
  name: Temporal Users API
  slug: temporal-users-api
arazzos:
- description: List a Service Account's API keys and load the detail of one of them.
  name: Temporal Audit API Keys for an Owner
  slug: temporal-audit-api-keys-for-owner-workflow
- description: Verify a Namespace exists, delete it, then confirm it is gone.
  name: Temporal Delete a Namespace and Confirm Removal
  slug: temporal-delete-namespace-workflow
- description: Read a User to confirm it exists, delete it, then verify it is gone.
  name: Temporal Deprovision a User and Confirm Removal
  slug: temporal-deprovision-user-workflow
- description: Page through Namespaces to find one by name, then load its full detail record.
  name: Temporal Find a Namespace by Name and Load Its Details
  slug: temporal-find-namespace-by-name-workflow
- description: Create a Service Account, read it back, then issue an API key owned by it.
  name: Temporal Issue an API Key for a New Service Account
  slug: temporal-issue-service-account-key-workflow
- description: Confirm a region is available, create a Namespace there, then poll until provisioning finishes.
  name: Temporal Provision a Namespace in a Validated Region
  slug: temporal-provision-namespace-in-region-workflow
- description: Create a Temporal Cloud Namespace and poll its async operation until it finishes.
  name: Temporal Provision a Namespace and Wait Until Ready
  slug: temporal-provision-namespace-workflow
- description: Create a User, then page Users to confirm the new account appears.
  name: Temporal Provision a User and Verify Membership
  slug: temporal-provision-user-workflow
- description: Read the owner of an existing key, mint a replacement key, then revoke the old one.
  name: Temporal Rotate an API Key for an Owner
  slug: temporal-rotate-api-key-workflow
- description: Poll a Temporal Cloud async operation until it leaves the pending state, branching on outcome.
  name: Temporal Track an Async Operation to Completion
  slug: temporal-track-async-operation-workflow
- description: Read a Namespace, update its spec using the current resourceVersion, then confirm the change.
  name: Temporal Update a Namespace With Optimistic Concurrency
  slug: temporal-update-namespace-workflow
artifact_total: 94
collections:
- collection_type: postman
  name: Temporal Cloud Operations API
  slug: postman-cloud-ops-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Temporal Cloud Operations API
  slug: open-cloud-ops-api
- collection_type: open
  name: Temporal Cloud Operations API Keys API
  slug: open-temporal-api-keys-api
- collection_type: open
  name: Temporal Cloud Operations API Keys Async Operations API
  slug: open-temporal-async-operations-api
- collection_type: open
  name: Temporal Cloud Operations API Keys Namespaces API
  slug: open-temporal-namespaces-api
- collection_type: open
  name: Temporal Cloud Operations API Keys Regions API
  slug: open-temporal-regions-api
- collection_type: open
  name: Temporal Cloud Operations API Keys Service Accounts API
  slug: open-temporal-service-accounts-api
- collection_type: open
  name: Temporal Cloud Operations API Keys Users API
  slug: open-temporal-users-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/temporal-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/temporal-cloud-ops-api-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/temporalio/api/blob/main/LICENSE
- group: build
  title: ''
  type: Packages
  url: packages/temporal-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/temporal-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/temporal-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/temporal-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/temporal-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/temporal-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/temporal-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/temporal-sandbox.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/temporal-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/temporal-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/temporal-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/temporal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/temporal-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/temporal/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/temporal-audit-api-keys-for-owner-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/temporal-delete-namespace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/temporal-deprovision-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/temporal-find-namespace-by-name-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/temporal-issue-service-account-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/temporal-provision-namespace-in-region-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/temporal-provision-namespace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/temporal-provision-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/temporal-rotate-api-key-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/temporal-track-async-operation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/temporal-update-namespace-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/temporal-technologies
- group: start
  title: ''
  type: Portal
  url: https://temporal.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.temporal.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.temporal.io/cloud/get-started
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.temporal.io/quickstarts
- group: build
  title: ''
  type: SDKs
  url: https://docs.temporal.io/develop
- group: build
  title: ''
  type: CLI
  url: https://docs.temporal.io/cli
- group: commercial
  title: ''
  type: Pricing
  url: https://temporal.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://temporal.io/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://temporal.io/change-log
- group: operate
  title: ''
  type: StatusPage
  url: https://status.temporal.io
- group: auth
  title: ''
  type: Security
  url: https://temporal.io/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://temporal.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://temporal.io/global-privacy-policy
- group: start
  title: ''
  type: Login
  url: https://cloud.temporal.io/login
- group: start
  title: ''
  type: Signup
  url: https://docs.temporal.io/cloud/get-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/temporalio
- group: learn
  title: ''
  type: Training
  url: https://learn.temporal.io/
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/temporalio/skill-temporal-developer
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.temporal.io/llms.txt
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-03-03'
description: Temporal is an open-source durable execution platform for building reliable long-running distributed workflows and microservices.
examples:
- key_count: 5
  name: Cloud Ops Api Key Example
  slug: cloud-ops-api-key-example
- key_count: 7
  name: Cloud Ops Async Operation Example
  slug: cloud-ops-async-operation-example
- key_count: 1
  name: Cloud Ops Create Api Key Request Example
  slug: cloud-ops-create-api-key-request-example
- key_count: 1
  name: Cloud Ops Create Namespace Request Example
  slug: cloud-ops-create-namespace-request-example
- key_count: 2
  name: Cloud Ops Create Namespace Response Example
  slug: cloud-ops-create-namespace-response-example
- key_count: 1
  name: Cloud Ops Create Service Account Request Example
  slug: cloud-ops-create-service-account-request-example
- key_count: 1
  name: Cloud Ops Create User Request Example
  slug: cloud-ops-create-user-request-example
- key_count: 8
  name: Cloud Ops Namespace Example
  slug: cloud-ops-namespace-example
- key_count: 3
  name: Cloud Ops Region Example
  slug: cloud-ops-region-example
- key_count: 5
  name: Cloud Ops Service Account Example
  slug: cloud-ops-service-account-example
- key_count: 2
  name: Cloud Ops Update Namespace Request Example
  slug: cloud-ops-update-namespace-request-example
- key_count: 6
  name: Cloud Ops User Example
  slug: cloud-ops-user-example
features:
- description: Automatically persists workflow state and resumes execution after failures, ensuring long-running processes complete reliably.
  name: Durable Execution
- description: Create and manage isolated namespaces for organizing workflows with independent retention policies and access controls.
  name: Namespace Management
- description: Manage users, service accounts, and API keys for fine-grained access control to Temporal Cloud resources.
  name: User and Access Management
- description: Deploy workflows across multiple cloud regions for low-latency execution and disaster recovery.
  name: Multi-Region Deployment
- description: Safely deploy workflow code changes with built-in versioning that prevents breaking running executions.
  name: Workflow Versioning
- description: Query and filter workflow executions using custom search attributes for operational visibility and debugging.
  name: Visibility and Search
- description: Secure namespace communication with mutual TLS certificate-based authentication and codec server encryption.
  name: mTLS Authentication
- description: Track the status of long-running control plane operations like namespace creation and configuration changes.
  name: Async Operations
finops:
- name: Temporal Finops
  service_category: API
  slug: temporal-finops
image: /assets/icons/temporal.png
integrations:
- description: Native Go client library for building Temporal workflows and activities with full type safety.
  name: Go SDK
- description: TypeScript/JavaScript SDK for building Temporal workflows in Node.js with async/await patterns.
  name: TypeScript SDK
- description: Python SDK for building Temporal workflows with native async support and type hints.
  name: Python SDK
- description: Java SDK for building Temporal workflows with annotation-based workflow and activity definitions.
  name: Java SDK
- description: .NET SDK for building Temporal workflows in C# with strong typing and async patterns.
  name: .NET SDK
json_schemas:
- name: ApiKey
  property_count: 5
  slug: cloud-ops-api-key
- name: AsyncOperation
  property_count: 7
  slug: cloud-ops-async-operation
- name: CreateApiKeyRequest
  property_count: 1
  slug: cloud-ops-create-api-key-request
- name: CreateNamespaceRequest
  property_count: 1
  slug: cloud-ops-create-namespace-request
- name: CreateNamespaceResponse
  property_count: 2
  slug: cloud-ops-create-namespace-response
- name: CreateServiceAccountRequest
  property_count: 1
  slug: cloud-ops-create-service-account-request
- name: CreateUserRequest
  property_count: 1
  slug: cloud-ops-create-user-request
- name: Namespace
  property_count: 8
  slug: cloud-ops-namespace
- name: Region
  property_count: 3
  slug: cloud-ops-region
- name: ServiceAccount
  property_count: 5
  slug: cloud-ops-service-account
- name: UpdateNamespaceRequest
  property_count: 2
  slug: cloud-ops-update-namespace-request
- name: User
  property_count: 6
  slug: cloud-ops-user
json_structures:
- name: Cloud Ops Api Key Structure
  property_count: 5
  slug: cloud-ops-api-key-structure
- name: Cloud Ops Async Operation Structure
  property_count: 7
  slug: cloud-ops-async-operation-structure
- name: Cloud Ops Create Api Key Request Structure
  property_count: 1
  slug: cloud-ops-create-api-key-request-structure
- name: Cloud Ops Create Namespace Request Structure
  property_count: 1
  slug: cloud-ops-create-namespace-request-structure
- name: Cloud Ops Create Namespace Response Structure
  property_count: 2
  slug: cloud-ops-create-namespace-response-structure
- name: Cloud Ops Create Service Account Request Structure
  property_count: 1
  slug: cloud-ops-create-service-account-request-structure
- name: Cloud Ops Create User Request Structure
  property_count: 1
  slug: cloud-ops-create-user-request-structure
- name: Cloud Ops Namespace Structure
  property_count: 8
  slug: cloud-ops-namespace-structure
- name: Cloud Ops Region Structure
  property_count: 3
  slug: cloud-ops-region-structure
- name: Cloud Ops Service Account Structure
  property_count: 5
  slug: cloud-ops-service-account-structure
- name: Cloud Ops Update Namespace Request Structure
  property_count: 2
  slug: cloud-ops-update-namespace-request-structure
- name: Cloud Ops User Structure
  property_count: 6
  slug: cloud-ops-user-structure
jsonld:
- class_count: 0
  name: Cloud Ops Context
  property_count: 0
  slug: cloud-ops-context
layout: provider
mcp_servers:
- description: ''
  name: temporal-mcp.yml
  slug: temporal-mcpyml
modified: '2026-06-20'
name: Temporal
nav: Providers
network: true
overview: 'Temporal publishes 6 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Async Operations API, Namespaces API, and 3 more. Tagged areas include ProCode_API_Composition and Workflows.


  The Temporal catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Temporal''s developer surface includes changelog, CLI, sandbox, authentication, developer portal, documentation, getting-started guide, and 42 more developer resources.'
plans:
- name: Temporal Plans Pricing
  plan_count: 3
  slug: temporal-plans-pricing
random_paper: 123
rate_limits:
- limit_count: 5
  name: Temporal Rate Limits
  slug: temporal-rate-limits
rules:
- name: Temporal API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: temporal-jsonschema-spectral-rules
- name: Temporal API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 6
  slug: temporal-spectral-rules
score:
  band: exemplar
  composite: 66.4
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 63.4
    developer_ergonomics: 73.9
    discoverability: 64.8
    governance: 69.8
    operational_transparency: 55.3
  previous_composite: 66.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/temporal/refs/heads/main/screenshots/temporal-2026-06-20T195103.png
security:
- kind: authentication
  name: Temporal Authentication
  slug: temporal-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Temporal Domain Security
  slug: temporal-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Temporal Vulnerability Disclosure
  slug: temporal-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Temporal Trust Center
  slug: temporal-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR
skill_count: 1
skills:
- name: temporal-developer
  slug: temporal-developer
slug: temporal
tags:
- ProCode_API_Composition
- Workflows
use_cases:
- description: Coordinate complex multi-service transactions with automatic retries, compensation logic, and timeout handling.
  name: Microservice Orchestration
- description: Build reliable ETL and data processing pipelines that handle failures gracefully and resume from the last checkpoint.
  name: Data Pipeline Processing
- description: Automate end-to-end order processing including payment, inventory, shipping, and notification steps with guaranteed completion.
  name: Order Fulfillment Workflows
- description: Orchestrate cloud infrastructure deployment and configuration management with durable state tracking.
  name: Infrastructure Provisioning
- description: Manage recurring billing cycles, subscription renewals, and payment processing with long-running timer-based workflows.
  name: Subscription and Billing Management
website: https://temporal.io/
---
