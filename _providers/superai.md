---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-11'
api_count: 19
apis:
- description: Authentication operations for user authentication, authorization, and session management. Authentication endpoints handle user identity verification, token generation, and access control throughout th
  name: Super.ai auth API
  slug: superai-auth-api
- description: File download operations for retrieving files from gs:// storage URIs. When Super.AI Flows processes documents, task outputs often include file references as `gs://` URIs pointing to Google Cloud Stor
  name: Super.ai files API
  slug: superai-files-api
- description: Flow execution operations for running and monitoring workflows. Flow executions represent runtime instances of flows. When you execute a flow, a new flow execution is created with its own unique ID, s
  name: Super.ai flow-executions API
  slug: superai-flow-executions-api
- description: Flow management operations for defining and organizing workflows. Flows represent workflow definitions with tasks, dependencies, and execution logic. They serve as reusable templates that can be execu
  name: Super.ai flows API
  slug: superai-flows-api
- description: Human review task operations for creating and managing human-in-the-loop review workflows.
  name: Super.ai human-review-tasks API
  slug: superai-human-review-tasks-api
- description: 'Integration operations for connecting flows to external services and platforms. Integrations enable your workflows to interact with third-party services, databases, storage systems, and communication '
  name: Super.ai integrations API
  slug: superai-integrations-api
- description: 'Model operations for querying available AI models and their configurations. Model endpoints provide information about the AI models available through the platform. These endpoints enable discovery of '
  name: Super.ai models API
  slug: superai-models-api
- description: Organization operations for viewing credit balance and organization-scoped information.
  name: Super.ai organizations API
  slug: superai-organizations-api
- description: Plugin operations for managing integration plugin instances, OAuth flows, and webhooks.
  name: Super.ai plugins API
  slug: superai-plugins-api
- description: User profile operations for viewing and updating account information. Profile endpoints allow authenticated users to view and update their own account information and preferences. These endpoints oper
  name: Super.ai profile API
  slug: superai-profile-api
- description: Service account operations for managing programmatic API access credentials.
  name: Super.ai service-accounts API
  slug: superai-service-accounts-api
- description: Single Sign-On operations for configuring SAML-based SSO authentication.
  name: Super.ai sso API
  slug: superai-sso-api
- description: Task data operations for flow validation, schema discovery, and dynamic configuration. The task-data endpoint analyzes flow definitions to extract task output schemas, dynamic configuration options, a
  name: Super.ai task-data API
  slug: superai-task-data-api
- description: Task execution operations for tracking individual task runs within flow executions. Task executions represent individual task runs within a flow execution. Each task in a flow execution has its own ta
  name: Super.ai task-executions API
  slug: superai-task-executions-api
- description: Task executor operations for discovering available task types and their capabilities. Task executors define the available task types that can be used in flow definitions. Each executor specifies its i
  name: Super.ai task-executors API
  slug: superai-task-executors-api
- description: 'Task output operations for storing and retrieving task execution results. Task outputs store the results produced by task executions in a structured, queryable format. While task executions track the '
  name: Super.ai task-outputs API
  slug: superai-task-outputs-api
- description: Task tag operations for categorizing and organizing tasks with metadata. Task tags provide metadata and categorization for tasks within flow executions. Tags enable flexible organization, filtering, a
  name: Super.ai task-tags API
  slug: superai-task-tags-api
- description: Push data from external systems to a flow execution's waiting 'Wait for Webhook' task. A 2xx acknowledgment means the data is durably stored; identical redeliveries are idempotent.
  name: Super.ai webhook-data API
  slug: superai-webhook-data-api
- description: The worker-groups API from Super.ai — 3 operation(s) for worker-groups.
  name: Super.ai worker-groups API
  slug: superai-worker-groups-api
artifact_total: 25
asyncapis:
- description: ''
  name: Superai Flows Webhooks
  slug: superai-flows-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/superai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/superai-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.flows.super.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flows.super.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.flows.super.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flows.super.ai/quickstart
- group: company
  title: ''
  type: Blog
  url: https://super.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://super.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://flows.super.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://super.ai/terms_of_service.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://super.ai/trust/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mysuperai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.super.ai
- group: auth
  title: ''
  type: Security
  url: https://super.ai/trust/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://super.ai/trust
- group: auth
  title: ''
  type: Compliance
  url: https://super.ai/trust/compliance
- group: build
  title: ''
  type: Packages
  url: packages/superai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/superai-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/superai-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/superai-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/superai-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/superai-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/superai-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/superai-flows-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/superai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/superai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/superai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/superai-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/superai-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/superai-flows-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'super.AI is an intelligent document processing (IDP) platform that automates the extraction and processing of complex, multi-page documents such as invoices, contracts, and bills of lading, improving accuracy as users correct its output. Its developer product, SuperAI Flows, is a workflow orchestration platform for building durable, AI-powered automations through a simple REST API: design flows that orchestrate AI models, data processing, human-review tasks, and business logic, then run them synchronously via polling or asynchronously via webhooks. The API covers flows, flow executions, task executions and outputs, human review, integrations (email, storage, databases), files, models, service accounts, SSO, and organization management, with JWT bearer and service-account API-key authentication. super.AI serves financial services, insurance, logistics, shared services, and testing/inspection/certification.'
image: https://super.ai/superai-logo.webp
layout: provider
mcp_servers:
- description: ''
  name: superai-mcp.yml
  slug: superai-mcpyml
modified: '2026-07-21'
name: Super.ai
nav: Providers
network: true
overview: 'Super.ai publishes 19 APIs on the [APIs.io](https://apis.io/) network, including auth API, files API, flow-executions API, and 16 more. Tagged areas include Company, Ai Enterprise Software, Intelligent Document Processing, Document Processing, and Workflow Orchestration.


  The Super.ai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Super.ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, CLI, and 24 more developer resources.'
random_paper: 65
score:
  band: developing
  composite: 54.8
  delta: -0.6
  facets:
    commercial_clarity: 60.5
    contract_quality: 64.5
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 39.5
  previous_composite: 55.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Superai Authentication
  slug: superai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Superai Domain Security
  slug: superai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Superai Vulnerability Disclosure
  slug: superai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Superai Trust Center
  slug: superai-trust-center
  summary_line: SOC 2, GDPR
slug: superai
tags:
- Company
- Ai Enterprise Software
- Intelligent Document Processing
- Document Processing
- Workflow Orchestration
- Automation
- Human In The Loop
- Artificial Intelligence
- REST API
website: https://docs.flows.super.ai
---
