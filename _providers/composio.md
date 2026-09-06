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
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 60
  human_in_the_loop: 3
  name: Composio Agentic Access
  operation_count: 107
  slug: composio-agentic-access
  summary_line: 107 operations · 60 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: Authentication configuration management
  name: Composio Auth Configs API
  slug: composio-auth-configs-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: Authentication related endpoints
  name: Composio Authentication API
  slug: composio-authentication-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: CLI integration endpoints
  name: Composio CLI API
  slug: composio-cli-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: The CLI Authentication API from Composio — 2 operation(s) for cli authentication.
  name: Composio CLI Authentication API
  slug: composio-cli-authentication-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: Connected account management
  name: Composio Connected Accounts API
  slug: composio-connected-accounts-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: File management
  name: Composio Files API
  slug: composio-files-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: Logging and monitoring
  name: Composio Logs API
  slug: composio-logs-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: MCP server management
  name: Composio MCP API
  slug: composio-mcp-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: Endpoints to help with migration from v1 to v3
  name: Composio Migration API
  slug: composio-migration-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: The Organization Management API from Composio — 5 operation(s) for organization management.
  name: Composio Organization Management API
  slug: composio-organization-management-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: The Projects API from Composio — 6 operation(s) for projects.
  name: Composio Projects API
  slug: composio-projects-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: (Labs) Tool router endpoints
  name: Composio Tool Router API
  slug: composio-tool-router-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: Toolkit and tool management
  name: Composio Toolkits API
  slug: composio-toolkits-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: Tool execution endpoints
  name: Composio Tools API
  slug: composio-tools-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: Trigger management and execution
  name: Composio Triggers API
  slug: composio-triggers-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: Per-OAuth-app webhook ingress endpoints. Inbound URLs the provider posts to, plus signing secret storage and verification.
  name: Composio Webhook Endpoints API
  slug: composio-webhook-endpoints-api
- baseURL: https://backend.composio.dev/api/v3
  baseurl_source: declared
  description: Webhook delivery subscriptions. Outbound URLs Composio posts trigger events to, plus signing secret rotation and event-type filters.
  name: Composio Webhook Subscriptions API
  slug: composio-webhook-subscriptions-api
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
artifact_total: 118
collections:
- collection_type: postman
  name: Composio Platform API
  slug: postman-composio-openapi-original
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Composio Platform Account Management API
  slug: open-composio-account-management-api
- collection_type: open
  name: Composio Platform Account Management AI API
  slug: open-composio-ai-api
- collection_type: open
  name: Composio Platform Account Management API Keys API
  slug: open-composio-api-keys-api
- collection_type: open
  name: Composio Platform Account Management Applications API
  slug: open-composio-applications-api
- collection_type: open
  name: Composio Platform Account Management Auth Configs API
  slug: open-composio-auth-configs-api
- collection_type: open
  name: Composio Platform Account Management Authentication API
  slug: open-composio-authentication-api
- collection_type: open
  name: Composio Platform Account Management Categories API
  slug: open-composio-categories-api
- collection_type: open
  name: Composio Platform Account Management CLI API
  slug: open-composio-cli-api
- collection_type: open
  name: Composio Platform Account Management CLI Authentication API
  slug: open-composio-cli-authentication-api
- collection_type: open
  name: Composio Platform Account Management Configuration API
  slug: open-composio-configuration-api
- collection_type: open
  name: Composio Platform Account Management Connected Accounts API
  slug: open-composio-connected-accounts-api
- collection_type: open
  name: Composio Platform Account Management Custom API
  slug: open-composio-custom-api
- collection_type: open
  name: Composio Platform Account Management Execution API
  slug: open-composio-execution-api
- collection_type: open
  name: Composio Platform Account Management Files API
  slug: open-composio-files-api
- collection_type: open
  name: Composio Platform Account Management Instances API
  slug: open-composio-instances-api
- collection_type: open
  name: Composio Platform Account Management Integration API
  slug: open-composio-integration-api
- collection_type: open
  name: Composio Platform Account Management Logs API
  slug: open-composio-logs-api
- collection_type: open
  name: Composio Platform Account Management MCP API
  slug: open-composio-mcp-api
- collection_type: open
  name: Composio Platform Account Management Migration API
  slug: open-composio-migration-api
- collection_type: open
  name: Composio Platform Account Management Natural Language Processing API
  slug: open-composio-natural-language-processing-api
- collection_type: open
  name: Composio Platform API
  slug: open-composio-openapi-original
- collection_type: open
  name: Composio Platform Account Management Organization API
  slug: open-composio-organization-api
- collection_type: open
  name: Composio Platform Account Management Organization Management API
  slug: open-composio-organization-management-api
- collection_type: open
  name: Composio Platform Account Management Projects API
  slug: open-composio-projects-api
- collection_type: open
  name: Composio Platform Account Management Proxy API
  slug: open-composio-proxy-api
- collection_type: open
  name: Composio Platform Account Management Realtime API
  slug: open-composio-realtime-api
- collection_type: open
  name: Composio Platform Account Management Servers API
  slug: open-composio-servers-api
- collection_type: open
  name: Composio Platform Account Management Session API
  slug: open-composio-session-api
- collection_type: open
  name: Composio Platform Account Management Tool Router API
  slug: open-composio-tool-router-api
- collection_type: open
  name: Composio Platform Account Management Toolkits API
  slug: open-composio-toolkits-api
- collection_type: open
  name: Composio Platform Account Management Tools API
  slug: open-composio-tools-api
- collection_type: open
  name: Composio Platform Account Management Triggers API
  slug: open-composio-triggers-api
- collection_type: open
  name: Composio Platform Account Management Upload API
  slug: open-composio-upload-api
- collection_type: open
  name: Composio Platform Account Management URL Generation API
  slug: open-composio-url-generation-api
- collection_type: open
  name: Composio Platform Account Management User API
  slug: open-composio-user-api
- collection_type: open
  name: Composio Platform Account Management UUID Conversion API
  slug: open-composio-uuid-conversion-api
- collection_type: open
  name: Composio Platform Account Management Webhook Endpoints API
  slug: open-composio-webhook-endpoints-api
- collection_type: open
  name: Composio Platform Account Management Webhook Subscriptions API
  slug: open-composio-webhook-subscriptions-api
- collection_type: open
  name: Composio Platform Account Management x-internal API
  slug: open-composio-x-internal-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ComposioHQ/composio/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/ComposioHQ/composio/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/ComposioHQ/composio/blob/next/.github/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/ComposioHQ/composio/blob/next/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/ComposioHQ/composio/blob/next/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/ComposioHQ/composio/blob/next/LICENSE
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
- description: 'Composio exposes its 1000+ toolkits over the Model Context Protocol as a hosted, per-session MCP server. The recommended path is the Tool Router: create a session with `mcp: true` and read the hosted '
  name: Composio MCP Server
  slug: composio-mcp-server
modified: '2026-06-20'
name: Composio
nav: Providers
network: true
overview: 'Composio publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Auth Configs API, Authentication API, CLI API, and 14 more. Tagged areas include AI Agents, Authentication, Integration, MCP, and Sandbox.


  The Composio catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Composio''s developer surface includes changelog, CLI, authentication, developer portal, documentation, getting-started guide, API reference, and 53 more developer resources.'
plans:
- name: Composio Plans Pricing
  plan_count: 4
  slug: composio-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Composio Rate Limits
  slug: composio-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Composio API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: composio-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Composio API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 5
  slug: composio-rules
score:
  band: strong
  composite: 54.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 55.5
    catalog_earned_first_party: 0.0
    catalog_gap: 59.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 59.5
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  open_source:
    applies: true
    score: 65.0
  previous_composite: 54.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- Integration
- MCP
- Sandbox
- Tools
- Triggers
- Unified-API
- Webhook
website: https://app.composio.dev/dashboard
---
