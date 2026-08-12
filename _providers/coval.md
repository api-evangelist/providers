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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 58.3
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 86
  human_in_the_loop: 0
  name: Coval Agentic Access
  operation_count: 151
  slug: coval-agentic-access
  summary_line: 151 operations · 86 acting
api_count: 25
apis:
- description: CRUD operations for AI agent configurations
  name: Coval Agents API
  slug: coval-agents-api
- description: Manage API keys for your organization
  name: Coval API Keys API
  slug: coval-api-keys-api
- description: Upload audio for evaluation and access conversation audio files
  name: Coval Audio API
  slug: coval-audio-api
- description: Submit and manage real-world conversation monitoring evaluations
  name: Coval Conversations API
  slug: coval-conversations-api
- description: Dashboard CRUD operations
  name: Coval Dashboards API
  slug: coval-dashboards-api
- description: Retrieve metric computation results for simulations
  name: Coval Metric Outputs API
  slug: coval-metric-outputs-api
- description: CRUD operations for custom evaluation metrics
  name: Coval Metrics API
  slug: coval-metrics-api
- description: Monitor evaluation event history
  name: Coval Monitor Events API
  slug: coval-monitor-events-api
- description: CRUD operations for monitor definitions
  name: Coval Monitors API
  slug: coval-monitors-api
- description: CRUD operations for agent configuration mutations
  name: Coval Mutations API
  slug: coval-mutations-api
- description: Organization-level configuration for conversation metrics — the default and conditional metrics run on conversations.
  name: Coval Organization Conversations Config API
  slug: coval-organization-conversations-config-api
- description: Persona CRUD operations
  name: Coval Personas API
  slug: coval-personas-api
- description: CRUD operations for saved multi-run reports
  name: Coval Reports API
  slug: coval-reports-api
- description: Annotation CRUD operations
  name: Coval Review Annotations API
  slug: coval-review-annotations-api
- description: Project CRUD operations
  name: Coval Review Projects API
  slug: coval-review-projects-api
- description: CRUD operations for reusable run configurations
  name: Coval Run Templates API
  slug: coval-run-templates-api
- description: Launch and manage simulation runs
  name: Coval Runs API
  slug: coval-runs-api
- description: CRUD operations for scheduled evaluations
  name: Coval Scheduled Runs API
  slug: coval-scheduled-runs-api
- description: Launch and manage individual simulation executions
  name: Coval Simulations API
  slug: coval-simulations-api
- description: CRUD operations for resource tags
  name: Coval Tags API
  slug: coval-tags-api
- description: Operations for managing test cases
  name: Coval Test Cases API
  slug: coval-test-cases-api
- description: Operations for managing test sets
  name: Coval Test Sets API
  slug: coval-test-sets-api
- description: OTLP trace ingestion for simulations and monitoring conversations.
  name: Coval Traces API
  slug: coval-traces-api
- description: CRUD operations for event webhooks
  name: Coval Webhooks API
  slug: coval-webhooks-api
- description: Dashboard widget CRUD operations
  name: Coval Widgets API
  slug: coval-widgets-api
artifact_total: 56
asyncapis:
- description: ''
  name: Coval Webhooks
  slug: coval-webhooks
collections:
- collection_type: postman
  name: Coval Agents API
  slug: postman-coval-agents-api
- collection_type: postman
  name: Coval Agents API Keys API
  slug: postman-coval-api-keys-api
- collection_type: postman
  name: Coval Agents Audio API
  slug: postman-coval-audio-api
- collection_type: postman
  name: Coval Agents Conversations API
  slug: postman-coval-conversations-api
- collection_type: postman
  name: Coval Agents Dashboards API
  slug: postman-coval-dashboards-api
- collection_type: postman
  name: Coval Agents Metric Outputs API
  slug: postman-coval-metric-outputs-api
- collection_type: postman
  name: Coval Agents Metrics API
  slug: postman-coval-metrics-api
- collection_type: postman
  name: Coval Agents Monitor Events API
  slug: postman-coval-monitor-events-api
- collection_type: postman
  name: Coval Agents Monitors API
  slug: postman-coval-monitors-api
- collection_type: postman
  name: Coval Agents Mutations API
  slug: postman-coval-mutations-api
- collection_type: postman
  name: Coval Agents Organization Conversations Config API
  slug: postman-coval-organization-conversations-config-api
- collection_type: postman
  name: Coval Agents Personas API
  slug: postman-coval-personas-api
- collection_type: postman
  name: Coval Agents Reports API
  slug: postman-coval-reports-api
- collection_type: postman
  name: Coval Agents Review Annotations API
  slug: postman-coval-review-annotations-api
- collection_type: postman
  name: Coval Agents Review Projects API
  slug: postman-coval-review-projects-api
- collection_type: postman
  name: Coval Agents Run Templates API
  slug: postman-coval-run-templates-api
- collection_type: postman
  name: Coval Agents Runs API
  slug: postman-coval-runs-api
- collection_type: postman
  name: Coval Agents Scheduled Runs API
  slug: postman-coval-scheduled-runs-api
- collection_type: postman
  name: Coval Agents Simulations API
  slug: postman-coval-simulations-api
- collection_type: postman
  name: Coval Agents Tags API
  slug: postman-coval-tags-api
- collection_type: postman
  name: Coval Agents Test Cases API
  slug: postman-coval-test-cases-api
- collection_type: postman
  name: Coval Agents Test Sets API
  slug: postman-coval-test-sets-api
- collection_type: postman
  name: Coval Agents Traces API
  slug: postman-coval-traces-api
- collection_type: postman
  name: Coval Agents Webhooks API
  slug: postman-coval-webhooks-api
- collection_type: postman
  name: Coval Agents Widgets API
  slug: postman-coval-widgets-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/coval-agents-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/coval/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.coval.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coval.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.coval.ai/api-reference/v1/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coval.ai/cli/overview
- group: company
  title: ''
  type: Blog
  url: https://www.coval.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coval.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.coval.dev/login
- group: start
  title: ''
  type: Login
  url: https://app.coval.dev/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coval.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coval.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://forms.gle/frTn8eCHkcTfw67p8
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coval-ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coval.dev
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.coval.ai/changelog
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.oneleet.com/coval
- group: auth
  title: ''
  type: Compliance
  url: https://trust.oneleet.com/coval
- group: auth
  title: ''
  type: Authentication
  url: authentication/coval-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coval-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/coval-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/coval-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/coval-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coval-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coval-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coval-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coval-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coval-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coval-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coval-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coval-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coval-webhooks.yml
created: '2026-07-17'
description: Coval is the deployment-readiness platform for voice and chat AI agents. Teams simulate thousands of realistic conversation scenarios before launch, monitor real production calls, and improve reliability with metrics and human review. Coval supports inbound/outbound voice, standard chat, chat over WebSocket, chat A2A (JSON-RPC), voice-to-voice models (OpenAI Realtime, Gemini Live), SMS, Pipecat, and LiveKit agents. Its v1 REST API, TypeScript and Python SDKs, Homebrew CLI, and hosted MCP server let developers connect agents, define personas and test sets, launch simulation runs, ingest production conversations and OpenTelemetry traces, define deterministic/statistical/ML/LLM-judge metrics, and route critical calls to human reviewers. Coval is backed by General Catalyst and is SOC 2 Type II, GDPR, and HIPAA compliant.
image: https://www.coval.ai/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: coval-mcp.yml
  slug: coval-mcpyml
modified: '2026-07-18'
name: Coval
nav: Providers
network: true
overview: 'Coval publishes 25 APIs on the [APIs.io](https://apis.io/) network, including Agents API, API Keys API, Audio API, and 22 more. Tagged areas include Company, AI Agents, Voice AI, Testing, and Evaluation.


  The Coval catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coval''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 26 more developer resources.'
random_paper: 69
score:
  band: strong
  composite: 61.5
  delta: -1.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 72.3
    developer_ergonomics: 79.9
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 44.7
  previous_composite: 63.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coval/refs/heads/main/screenshots/coval-2026-07-25T210531.png
security:
- kind: authentication
  name: Coval Authentication
  slug: coval-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Coval Domain Security
  slug: coval-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Coval Trust Center
  slug: coval-trust-center
  summary_line: SOC 2 Type II, GDPR, HIPAA
slug: coval
tags:
- Company
- AI Agents
- Voice AI
- Testing
- Evaluation
- Simulation
- Observability
- Conversational AI
- LLM
- Quality Assurance
website: https://docs.coval.ai
---
