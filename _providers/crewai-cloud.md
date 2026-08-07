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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Crewai Cloud Agentic Access
  operation_count: 4
  slug: crewai-cloud-agentic-access
  summary_line: 4 operations · 2 acting
api_count: 6
apis:
- description: Outbound event streaming for AMP crew executions. When you kick off a crew you can supply three callback URLs — taskWebhookUrl (fired after each task completes), stepWebhookUrl (fired after each agent
  name: CrewAI AMP Webhook Streaming
  slug: crewai-amp-webhook-streaming
- description: Model Context Protocol server published by CrewAI Inc. that exposes AMP crew deployment operations and status tracking to MCP-compatible agents and IDEs. Lets Claude, Cursor, and other MCP clients lis
  name: CrewAI Enterprise MCP Server
  slug: crewai-enterprise-mcp-server
- description: Discover the input parameters this crew accepts.
  name: CrewAI Cloud Inputs API
  slug: crewai-cloud-inputs-api
- description: Launch a crew execution.
  name: CrewAI Cloud Kickoff API
  slug: crewai-cloud-kickoff-api
- description: Deliver human-in-the-loop feedback on a paused task.
  name: CrewAI Cloud Resume API
  slug: crewai-cloud-resume-api
- description: Inspect execution progress and retrieve results.
  name: CrewAI Cloud Status API
  slug: crewai-cloud-status-api
arazzos:
- description: Discover the inputs a crew expects, then launch an execution with them.
  name: CrewAI AMP Discover Inputs and Kick Off
  slug: crewai-cloud-discover-inputs-and-kickoff-workflow
- description: Discover inputs, kick off a crew, poll to completion, and return the result.
  name: CrewAI AMP Full Run With Result
  slug: crewai-cloud-full-run-with-result-workflow
- description: Launch a crew execution and poll its status until it completes or errors.
  name: CrewAI AMP Kick Off and Poll Until Complete
  slug: crewai-cloud-kickoff-and-poll-until-complete-workflow
- description: Kick off a crew, poll until it pauses for review, deliver feedback, and poll again.
  name: CrewAI AMP Kick Off With Human-in-the-Loop Review
  slug: crewai-cloud-kickoff-with-hitl-review-workflow
- description: Inspect an existing execution, deliver human feedback, then poll until it settles.
  name: CrewAI AMP Resume a Paused Execution
  slug: crewai-cloud-resume-paused-execution-workflow
artifact_total: 57
asyncapis:
- description: 'Outbound webhook events published by CrewAI AMP during crew execution. Three callback URLs can be supplied per kickoff — `taskWebhookUrl`, `stepWebhookUrl`, and `crewWebhookUrl`. AMP POSTs JSON event '
  name: CrewAI AMP Webhook Streaming
  slug: crewai-amp-webhooks-asyncapi
collections:
- collection_type: postman
  name: CrewAI AMP REST API
  slug: postman-crewai-amp-rest-api
- collection_type: open
  name: CrewAI AMP REST API
  slug: open-crewai-amp-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/crewai-cloud-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/crewai-cloud-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crewai-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crewai-cloud-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/crewai-cloud/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/crewai-cloud-discover-inputs-and-kickoff-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/crewai-cloud-full-run-with-result-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/crewai-cloud-kickoff-and-poll-until-complete-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/crewai-cloud-kickoff-with-hitl-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/crewai-cloud-resume-paused-execution-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.crewai.com
- group: start
  title: ''
  type: Portal
  url: https://www.crewai.com/enterprise
- group: start
  title: ''
  type: Signup
  url: https://app.crewai.com
- group: start
  title: ''
  type: Console
  url: https://app.crewai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.crewai.com/llms.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.crewai.com/en/enterprise/guides/deploy-to-amp
- group: docs
  title: ''
  type: APIReference
  url: https://docs.crewai.com/en/api-reference/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://docs.crewai.com/en/api-reference/introduction
- group: design
  title: ''
  type: Webhooks
  url: https://docs.crewai.com/en/enterprise/features/webhook-streaming
- group: build
  title: ''
  type: SDKs
  url: https://github.com/crewAIInc/crewai
- group: build
  title: ''
  type: SDKs
  url: https://github.com/crewAIInc/crewai-tools
- group: build
  title: ''
  type: CLI
  url: https://docs.crewai.com/en/concepts/cli
- group: build
  title: ''
  type: Tools
  url: https://docs.crewai.com/en/enterprise/features/crew-studio
- group: build
  title: ''
  type: Tools
  url: https://github.com/crewAIInc/enterprise-mcp-server
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crewAIInc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/crewai-inc
- group: company
  title: ''
  type: Blog
  url: https://blog.crewai.com
- group: operate
  title: ''
  type: Forums
  url: https://community.crewai.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crewai.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crewai.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crewai.com/legal/privacy-notice
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.crewai.com/trust
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.crewai.com/en/release-notes
- group: commercial
  title: ''
  type: Plans
  url: https://www.crewai.com/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crewai.com/pricing
- group: auth
  title: ''
  type: SecurityAndCompliance
  url: https://www.crewai.com/trust
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/sso
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/rbac
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/secrets-manager/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/secrets-manager/aws
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/secrets-manager/aws-workload-identity
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/secrets-manager/azure
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/secrets-manager/azure-workload-identity
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/secrets-manager/gcp
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/secrets-manager/gcp-workload-identity
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/traces
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/pii-trace-redactions
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/hallucination-guardrail
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/guides/capture_telemetry_logs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/automations
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/guides/automation-triggers
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/flow-hitl-management
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/agent-repositories
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/marketplace
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/features/a2a
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/guides/tool-repository
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/guides/custom-mcp-server
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/concepts/production-architecture
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crewai.com/en/enterprise/resources/frequently-asked-questions
- group: commercial
  title: ''
  type: Plans
  url: plans/crewai-cloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/crewai-cloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/crewai-cloud-finops.yml
created: '2026-05-24'
description: CrewAI Cloud (CrewAI AMP) is the managed Agent Management Platform for deploying, monitoring, scaling, and governing CrewAI multi-agent workflows in production. AMP exposes a per-crew REST API for kickoff, status, inputs, and human-in-the-loop resume operations, plus webhook streaming for task, step, and crew events. The platform ships in two deployment modes — AMP Cloud (managed, multi-tenant at app.crewai.com) and AMP Factory (self-hosted on AWS, Azure, or GCP) — and layers RBAC, SSO, secrets manager federation (AWS/Azure/GCP), agent and tool repositories, a marketplace, A2A communication, automations and triggers, traces with PII redaction, and observability exports on top of the open-source CrewAI framework.
examples:
- key_count: 2
  name: Crewai Cloud Kickoff Example
  slug: crewai-cloud-kickoff-example
- key_count: 2
  name: Crewai Cloud Resume Example
  slug: crewai-cloud-resume-example
- key_count: 2
  name: Crewai Cloud Status Example
  slug: crewai-cloud-status-example
features:
- Two deployment modes — AMP Cloud (managed at app.crewai.com) and AMP Factory (self-hosted on AWS, Azure, or GCP)
- Per-crew REST API at https://{crew-name}.crewai.com with /inputs, /kickoff, /status/{id}, and /resume endpoints
- Bearer token authentication with organization-level and user-scoped tokens issued from the dashboard Status tab
- Webhook streaming with task, step, and crew event callback URLs supplied per kickoff
- Crew Studio visual editor with AI copilot for building crews and flows without code
- GitHub integration and CrewAI CLI deployment paths to AMP
- Automations with triggers from Gmail, Google Calendar, Google Drive, OneDrive, Outlook, HubSpot, Salesforce, Slack, Microsoft Teams, and Zapier
- 40+ enterprise integrations including Salesforce, HubSpot, Stripe, Shopify, Zendesk, Jira, Linear, Asana, ClickUp, Notion, Slack, Microsoft Teams, Outlook, Gmail, Google Workspace, Microsoft 365, Box, SharePoint, and GitHub
- Flow human-in-the-loop management with /resume endpoint for approve/retry decisions
- Hallucination guardrail and PII redaction for traces
- Role-based access control (RBAC) and team management
- Single Sign-On with Microsoft Entra and Okta (OAuth2 strategy published as crewai-omniauth-okta)
- Secrets manager federation with AWS Secrets Manager, Azure Key Vault, GCP Secret Manager, plus AWS, Azure, and GCP Workload Identity (OIDC) federation
- Traces dashboard for monitoring crew runs and OpenTelemetry export for external pipelines
- Observability integrations with Arize Phoenix, Braintrust, Datadog, Galileo, Langfuse, Langtrace, MLflow, Opik, Portkey, and Weave
- Agent Repositories for sharing and reusing agents across teams
- Marketplace for discovering, installing, and governing reusable agents, tools, and crews
- A2A on AMP — agent-to-agent communication with distributed state
- Tool Repository, Custom MCP Servers, and private package registry support
- Azure OpenAI and Vertex AI with Workload Identity LLM provider setup
- React component export for embedding crews into web apps
- MCP server (crewAIInc/enterprise-mcp-server) for managing deployments from MCP-compatible IDEs and agents
- 50 free workflow executions per month on the Basic tier; $0.50 per additional execution
- Enterprise tier includes up to 30,000 free executions per month, dedicated support, 50 hours of development per month, on-site support and training
- Used by 60% of Fortune 500 companies; runs 450M+ agentic workflows per month
finops:
- name: Crewai Cloud Finops
  service_category: ''
  slug: crewai-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/crewai-cloud.png
json_schemas:
- name: CrewAI AMP Kickoff
  property_count: 5
  slug: crewai-cloud-kickoff
- name: CrewAI AMP Resume Request
  property_count: 7
  slug: crewai-cloud-resume
- name: CrewAI AMP Kickoff Status
  property_count: 0
  slug: crewai-cloud-status
json_structures:
- name: Crewai Cloud Kickoff Structure
  property_count: 0
  slug: crewai-cloud-kickoff-structure
jsonld:
- class_count: 27
  name: Crewai Cloud Context
  property_count: 10
  slug: crewai-cloud-context
layout: provider
modified: '2026-05-24'
name: CrewAI Cloud
nav: Providers
network: true
overview: 'CrewAI Cloud publishes 5 APIs on the [APIs.io](https://apis.io/) network, including CrewAI AMP Webhook Streaming, Inputs API, Kickoff API, and 2 more. Tagged areas include AI Agents, AI Agent Platform, Agent Orchestration, Multi-Agent Systems, and Agent Management Platform.


  The CrewAI Cloud catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  CrewAI Cloud''s developer surface includes authentication, developer portal, signup flow, developer console, documentation, getting-started guide, API reference, and 57 more developer resources.'
plans:
- name: Crewai Cloud Plans Pricing
  plan_count: 2
  slug: crewai-cloud-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 0
  name: Crewai Cloud Rate Limits
  slug: crewai-cloud-rate-limits
rules:
- name: CrewAI Cloud API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 4
  slug: crewai-amp-rest-api-rules
- name: CrewAI Cloud API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: crewai-cloud-asyncapi-spectral-rules
- name: CrewAI Cloud API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: crewai-cloud-jsonschema-spectral-rules
score:
  band: strong
  composite: 62.9
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 80.4
    developer_ergonomics: 71.7
    discoverability: 64.8
    governance: 20.8
    operational_transparency: 44.7
  previous_composite: 62.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crewai-cloud/refs/heads/main/screenshots/crewai-cloud-2026-06-20T175231.png
security:
- kind: authentication
  name: Crewai Cloud Authentication
  slug: crewai-cloud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Crewai Cloud Domain Security
  slug: crewai-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crewai Cloud Vulnerability Disclosure
  slug: crewai-cloud-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crewai-cloud
tags:
- AI Agents
- AI Agent Platform
- Agent Orchestration
- Multi-Agent Systems
- Agent Management Platform
- Managed Agents
- Automations
- Observability
- Human In The Loop
website: https://www.crewai.com
---
