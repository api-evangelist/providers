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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 66.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 60
  human_in_the_loop: 3
  name: Composio Agentic Access
  operation_count: 107
  slug: composio-agentic-access
  summary_line: 107 operations · 60 acting · 3 human-in-the-loop
api_count: 38
apis:
- description: The Account Management API from Composio — 2 operation(s) for account management.
  name: Composio Account Management API
  slug: composio-account-management-api
- description: The AI API from Composio — 1 operation(s) for ai.
  name: Composio AI API
  slug: composio-ai-api
- description: API key management
  name: Composio API Keys API
  slug: composio-api-keys-api
- description: The Applications API from Composio — 1 operation(s) for applications.
  name: Composio Applications API
  slug: composio-applications-api
- description: Authentication configuration management
  name: Composio Auth Configs API
  slug: composio-auth-configs-api
- description: Authentication related endpoints
  name: Composio Authentication API
  slug: composio-authentication-api
- description: The Categories API from Composio — 1 operation(s) for categories.
  name: Composio Categories API
  slug: composio-categories-api
- description: CLI integration endpoints
  name: Composio CLI API
  slug: composio-cli-api
- description: The CLI Authentication API from Composio — 2 operation(s) for cli authentication.
  name: Composio CLI Authentication API
  slug: composio-cli-authentication-api
- description: The Configuration API from Composio — 1 operation(s) for configuration.
  name: Composio Configuration API
  slug: composio-configuration-api
- description: Connected account management
  name: Composio Connected Accounts API
  slug: composio-connected-accounts-api
- description: The Custom API from Composio — 1 operation(s) for custom.
  name: Composio Custom API
  slug: composio-custom-api
- description: The Execution API from Composio — 1 operation(s) for execution.
  name: Composio Execution API
  slug: composio-execution-api
- description: File management
  name: Composio Files API
  slug: composio-files-api
- description: The Instances API from Composio — 2 operation(s) for instances.
  name: Composio Instances API
  slug: composio-instances-api
- description: The Integration API from Composio — 3 operation(s) for integration.
  name: Composio Integration API
  slug: composio-integration-api
- description: Logging and monitoring
  name: Composio Logs API
  slug: composio-logs-api
- description: MCP server management
  name: Composio MCP API
  slug: composio-mcp-api
- description: Endpoints to help with migration from v1 to v3
  name: Composio Migration API
  slug: composio-migration-api
- description: The Natural Language Processing API from Composio — 1 operation(s) for natural language processing.
  name: Composio Natural Language Processing API
  slug: composio-natural-language-processing-api
- description: Organization management
  name: Composio Organization API
  slug: composio-organization-api
- description: The Organization Management API from Composio — 5 operation(s) for organization management.
  name: Composio Organization Management API
  slug: composio-organization-management-api
- description: The Projects API from Composio — 6 operation(s) for projects.
  name: Composio Projects API
  slug: composio-projects-api
- description: The Proxy API from Composio — 1 operation(s) for proxy.
  name: Composio Proxy API
  slug: composio-proxy-api
- description: The Realtime API from Composio — 2 operation(s) for realtime.
  name: Composio Realtime API
  slug: composio-realtime-api
- description: The Servers API from Composio — 7 operation(s) for servers.
  name: Composio Servers API
  slug: composio-servers-api
- description: The Session API from Composio — 2 operation(s) for session.
  name: Composio Session API
  slug: composio-session-api
- description: (Labs) Tool router endpoints
  name: Composio Tool Router API
  slug: composio-tool-router-api
- description: Toolkit and tool management
  name: Composio Toolkits API
  slug: composio-toolkits-api
- description: Tool execution endpoints
  name: Composio Tools API
  slug: composio-tools-api
- description: Trigger management and execution
  name: Composio Triggers API
  slug: composio-triggers-api
- description: The Upload API from Composio — 1 operation(s) for upload.
  name: Composio Upload API
  slug: composio-upload-api
- description: The URL Generation API from Composio — 1 operation(s) for url generation.
  name: Composio URL Generation API
  slug: composio-url-generation-api
- description: User API key management
  name: Composio User API
  slug: composio-user-api
- description: The UUID Conversion API from Composio — 1 operation(s) for uuid conversion.
  name: Composio UUID Conversion API
  slug: composio-uuid-conversion-api
- description: Per-OAuth-app webhook ingress endpoints. Inbound URLs the provider posts to, plus signing secret storage and verification.
  name: Composio Webhook Endpoints API
  slug: composio-webhook-endpoints-api
- description: Webhook delivery subscriptions. Outbound URLs Composio posts trigger events to, plus signing secret rotation and event-type filters.
  name: Composio Webhook Subscriptions API
  slug: composio-webhook-subscriptions-api
- description: The x-internal API from Composio — 13 operation(s) for x-internal.
  name: Composio x-internal API
  slug: composio-x-internal-api
arazzos:
- description: Create an auth config for a toolkit, open a connection, and poll until it becomes active.
  name: Composio Connect an Account via a New Auth Config
  slug: composio-connect-account-via-auth-config-workflow
- description: Find a user's active trigger by name and disable it.
  name: Composio Disable an Active Trigger
  slug: composio-disable-active-trigger-workflow
- description: Browse toolkits, list the tools they expose, and execute one tool for a user.
  name: Composio Discover and Execute a Tool
  slug: composio-discover-and-execute-tool-workflow
- description: Resolve a user's active connected account for a toolkit and execute a tool against it.
  name: Composio Execute a Tool on a User's Connected Account
  slug: composio-execute-tool-on-connected-account-workflow
- description: Pick an existing auth config and mint a hosted OAuth link for a user, then wait for the account to connect.
  name: Composio Generate a Hosted Auth Link
  slug: composio-hosted-auth-link-workflow
- description: Turn a plain-English instruction into tool arguments and execute the tool.
  name: Composio Natural Language Tool Execution
  slug: composio-natural-language-tool-execution-workflow
- description: Create an auth config, stand up an MCP server bound to it, and create a per-user MCP instance.
  name: Composio Provision an MCP Server
  slug: composio-provision-mcp-server-workflow
- description: Detect an expired connected account and refresh its authentication, then confirm it is active again.
  name: Composio Refresh a Connected Account
  slug: composio-refresh-connected-account-workflow
- description: Discover a trigger type, create a trigger instance on a connected account, and confirm it is active.
  name: Composio Set Up a Trigger
  slug: composio-setup-trigger-workflow
- description: Open a tool router session, inspect its toolkits, and mint an auth link for an unconnected toolkit.
  name: Composio Tool Router Connect a Toolkit
  slug: composio-tool-router-connect-toolkit-workflow
- description: Open a tool router session, search for a tool by use case, and execute it.
  name: Composio Tool Router Session
  slug: composio-tool-router-session-workflow
artifact_total: 100
collections:
- collection_type: postman
  name: Composio Platform API
  slug: postman-composio-openapi-original
- collection_type: open
  name: Composio Platform API
  slug: open-composio-openapi-original
common:
- group: build
  title: ''
  type: Packages
  url: packages/composio-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/composio-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/composio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/composio-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/composio-llms-full.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/composio-openapi-original-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/composio-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/composio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/composio-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/composio-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/composio-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/composio-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/composio-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/composio-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/composio-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/composio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/composio-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/composio/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/composio-connect-account-via-auth-config-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/composio-disable-active-trigger-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/composio-discover-and-execute-tool-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/composio-execute-tool-on-connected-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/composio-hosted-auth-link-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/composio-natural-language-tool-execution-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/composio-provision-mcp-server-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/composio-refresh-connected-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/composio-setup-trigger-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/composio-tool-router-connect-toolkit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/composio-tool-router-session-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/composiohq
- group: start
  title: ''
  type: Portal
  url: https://app.composio.dev/dashboard
- group: docs
  title: ''
  type: Documentation
  url: https://docs.composio.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.composio.dev/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.composio.dev/reference
- group: docs
  title: ''
  type: OpenAPI
  url: https://backend.composio.dev/api/v3/openapi.json
- group: auth
  title: ''
  type: Authentication
  url: https://docs.composio.dev/faq/api_key/api_key
- group: company
  title: ''
  type: Blog
  url: https://composio.dev/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.composio.dev
- group: commercial
  title: ''
  type: Pricing
  url: https://composio.dev/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.composio.dev/docs/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://composio.dev/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://composio.dev/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ComposioHQ
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/ComposioHQ/composio
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/ComposioHQ/composio
- group: build
  title: ''
  type: Node.js SDK
  url: https://www.npmjs.com/package/@composio/client
- group: start
  title: ''
  type: Signup
  url: https://app.composio.dev/dashboard
- group: start
  title: ''
  type: Agent Sign Up
  url: https://agents.composio.dev
- group: build
  title: ''
  type: Toolkits Catalog
  url: https://composio.dev/toolkits
- group: design
  title: ''
  type: JSONLD
  url: json-ld/composio-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/composio-tool-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/composio-toolkit-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/composio-connected-account-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.composio.dev/llms.txt
created: '2026-03-03'
description: Composio is an agent execution platform that bridges AI decision-making and real-world action across 1000+ apps through just-in-time tool calls, secure delegated auth, sandboxed environments, an MCP gateway, parallel execution, and context-aware sessions. Developers get managed OAuth, a tool router for runtime tool discovery, webhook triggers, and a CLI so agents turn intent into action without custom integration work.
examples:
- key_count: 6
  name: Composio Patchauthconfigsbynanoid Example
  slug: composio-patchauthconfigsbynanoid-example
- key_count: 6
  name: Composio Patchconnectedaccountsbynanoid Example
  slug: composio-patchconnectedaccountsbynanoid-example
- key_count: 6
  name: Composio Patchmcpbyid Example
  slug: composio-patchmcpbyid-example
- key_count: 6
  name: Composio Patchorgprojectconfig Example
  slug: composio-patchorgprojectconfig-example
- key_count: 6
  name: Composio Postclicodactfailures Example
  slug: composio-postclicodactfailures-example
- key_count: 6
  name: Composio Postfilesuploadrequest Example
  slug: composio-postfilesuploadrequest-example
- key_count: 6
  name: Composio Postlabstoolroutersession Example
  slug: composio-postlabstoolroutersession-example
- key_count: 6
  name: Composio Postmcpservers Example
  slug: composio-postmcpservers-example
- key_count: 6
  name: Composio Postmcpserversbyserveridinstances Example
  slug: composio-postmcpserversbyserveridinstances-example
- key_count: 6
  name: Composio Postmcpserverscustom Example
  slug: composio-postmcpserverscustom-example
- key_count: 6
  name: Composio Postmcpserversgenerate Example
  slug: composio-postmcpserversgenerate-example
- key_count: 6
  name: Composio Postorgownerprojectnew Example
  slug: composio-postorgownerprojectnew-example
- key_count: 6
  name: Composio Posttoolroutersession Example
  slug: composio-posttoolroutersession-example
finops:
- name: Composio Finops
  service_category: AI Tooling / Integrations
  slug: composio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/composio.png
json_schemas:
- name: AuthConfigListResponse
  property_count: 1
  slug: composio-authconfiglistresponse
- name: AuthConfigResponse
  property_count: 5
  slug: composio-authconfigresponse
- name: Composio Connected Account
  property_count: 6
  slug: composio-connected-account
- name: ConnectedAccountListResponse
  property_count: 2
  slug: composio-connectedaccountlistresponse
- name: ConnectedAccountResponse
  property_count: 4
  slug: composio-connectedaccountresponse
- name: CreateAuthConfigRequest
  property_count: 4
  slug: composio-createauthconfigrequest
- name: CreateConnectedAccountRequest
  property_count: 3
  slug: composio-createconnectedaccountrequest
- name: CreateTriggerRequest
  property_count: 4
  slug: composio-createtriggerrequest
- name: DeprecatedToolkitInfo
  property_count: 1
  slug: composio-deprecatedtoolkitinfo
- name: Error
  property_count: 1
  slug: composio-error
- name: ErrorResponse
  property_count: 3
  slug: composio-errorresponse
- name: ExecuteToolRequest
  property_count: 2
  slug: composio-executetoolrequest
- name: ExecuteToolResponse
  property_count: 3
  slug: composio-executetoolresponse
- name: PatchConnectedAccountBody
  property_count: 3
  slug: composio-patchconnectedaccountbody
- name: SessionResponse
  property_count: 2
  slug: composio-sessionresponse
- name: Composio Tool
  property_count: 6
  slug: composio-tool
- name: Composio Toolkit
  property_count: 7
  slug: composio-toolkit
- name: ToolkitListResponse
  property_count: 2
  slug: composio-toolkitlistresponse
- name: ToolkitResponse
  property_count: 7
  slug: composio-toolkitresponse
- name: ToolListResponse
  property_count: 2
  slug: composio-toollistresponse
- name: ToolRouterToolkitsListResponse
  property_count: 5
  slug: composio-toolroutertoolkitslistresponse
- name: ToolsPaginated
  property_count: 5
  slug: composio-toolspaginated
- name: TriggerListResponse
  property_count: 1
  slug: composio-triggerlistresponse
- name: TriggerResponse
  property_count: 6
  slug: composio-triggerresponse
json_structures:
- name: Composio Structure
  property_count: 0
  slug: composio-structure
jsonld:
- class_count: 0
  name: Composio Context
  property_count: 7
  slug: composio-context
layout: provider
mcp_servers:
- description: ''
  name: composio-mcp.yml
  slug: composio-mcpyml
modified: '2026-06-20'
name: Composio
nav: Providers
network: true
overview: 'Composio publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Account Management API, AI API, API Keys API, and 35 more. Tagged areas include AI Agents, Authentication, Integrations, MCP, and OAuth.


  The Composio catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Composio''s developer surface includes changelog, CLI, authentication, developer portal, documentation, getting-started guide, API reference, and 47 more developer resources.'
plans:
- name: Composio Plans Pricing
  plan_count: 4
  slug: composio-plans-pricing
random_paper: 63
rate_limits:
- limit_count: 5
  name: Composio Rate Limits
  slug: composio-rate-limits
rules:
- name: Composio API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: composio-jsonschema-spectral-rules
- name: Composio API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: composio-rules
score:
  band: exemplar
  composite: 70.3
  delta: -0.7
  facets:
    commercial_clarity: 71.1
    contract_quality: 61.4
    developer_ergonomics: 73.9
    discoverability: 87.0
    governance: 69.8
    operational_transparency: 68.4
  previous_composite: 71.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 38
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/composio/refs/heads/main/screenshots/composio-2026-06-20T174834.png
security:
- kind: authentication
  name: Composio Authentication
  slug: composio-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Composio Domain Security
  slug: composio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Composio Vulnerability Disclosure
  slug: composio-vulnerability-disclosure
  summary_line: disclosure policy published
slug: composio
tags:
- AI Agents
- Authentication
- Integrations
- MCP
- OAuth
- Sandbox
- Tools
- Triggers
- Unified_API
- Webhooks
website: https://app.composio.dev/dashboard
---
