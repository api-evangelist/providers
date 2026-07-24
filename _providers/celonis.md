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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 75.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 33
  human_in_the_loop: 5
  name: Celonis Agentic Access
  operation_count: 78
  slug: celonis-agentic-access
  summary_line: 78 operations · 33 acting · 5 human-in-the-loop
api_count: 17
apis:
- description: The Agents - Conversation API from Celonis — 1 operation(s) for agents - conversation.
  name: Celonis Agents - Conversation API
  slug: celonis-agents-conversation-api
- description: 'The Beta: OData Protocol API from Celonis — 3 operation(s) for beta: odata protocol.'
  name: 'Celonis Beta: OData Protocol API'
  slug: celonis-beta-odata-protocol-api
- description: 'The Beta: Semantics for 3P AI Agents API from Celonis — 4 operation(s) for beta: semantics for 3p ai agents.'
  name: 'Celonis Beta: Semantics for 3P AI Agents API'
  slug: celonis-beta-semantics-for-3p-ai-agents-api
- description: The Data API from Celonis — 2 operation(s) for data.
  name: Celonis Data API
  slug: celonis-data-api
- description: The Job Execution API is used to trigger, stop, and track job executions.
  name: Celonis Job Execution API
  slug: celonis-job-execution-api
- description: The Job Execution Group API retrieves job execution groups.
  name: Celonis Job Execution Group API
  slug: celonis-job-execution-group-api
- description: Allows you to query the Login History for a team and export it for use with external monitoring tools to capture and monitor platform login events.
  name: Celonis Login History API API
  slug: celonis-login-history-api-api
- description: Allows you to query and export a list of all members assigned to a Celonis Platform team.
  name: Celonis Members API API
  slug: celonis-members-api-api
- description: The Notebook API is used to create, read, update, and delete notebooks.
  name: Celonis Notebook API
  slug: celonis-notebook-api
- description: The Notebook Executions API is used to trigger, stop, and track notebook executions.
  name: Celonis Notebook Execution API
  slug: celonis-notebook-execution-api
- description: The Notebook Resources API configures notebook resource such as CPU, memory, storage, and gpu.
  name: Celonis Notebook Resources API
  slug: celonis-notebook-resources-api
- description: OpenAPI endpoints for calling tools configured in the Agent Tools (MCP) Asset.
  name: Celonis OpenAPI Tool Calling API
  slug: celonis-openapi-tool-calling-api
- description: Export all permissions for the team as a JSON file.
  name: Celonis Permissions Export API API
  slug: celonis-permissions-export-api-api
- description: The Schedule API is used to create, read, update, and delete schedules.
  name: Celonis Schedule API
  slug: celonis-schedule-api
- description: The Schema API from Celonis — 6 operation(s) for schema.
  name: Celonis Schema API
  slug: celonis-schema-api
- description: The Subscriptions API from Celonis — 8 operation(s) for subscriptions.
  name: Celonis Subscriptions API
  slug: celonis-subscriptions-api
- description: The Triggers API from Celonis — 2 operation(s) for triggers.
  name: Celonis Triggers API
  slug: celonis-triggers-api
artifact_total: 24
asyncapis:
- description: ''
  name: Celonis Subscription Webhooks
  slug: celonis-subscription-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.celonis.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.celonis.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.celonis.com/celonis-apis/get-started-with-celonis-apis/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.celonis.com/celonis-apis/get-started-with-celonis-apis/
- group: operate
  title: ''
  type: Support
  url: https://community.celonis.com/
- group: company
  title: ''
  type: Blog
  url: https://www.celonis.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/celonis
- group: commercial
  title: ''
  type: Pricing
  url: https://www.celonis.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://signup.celonis.com/ui/sign-up/get-started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.celonis.com/legal/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.celonis.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/celonis-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/celonis-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/celonis-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/celonis-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/celonis-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/celonis-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/celonis-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/celonis-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/celonis-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/celonis-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/celonis-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/celonis-subscription-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/celonis-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.celonis.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/celonis-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/celonis-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/celonis-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.celonis.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/celonis-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/celonis-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/celonis-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/celonis-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.celonis.com
created: '2026-07-17'
description: Celonis is the process intelligence and process mining company. Its cloud platform ingests event data from enterprise systems, builds Knowledge Models of how business processes actually run, and surfaces KPIs, bottlenecks and automation opportunities. For developers Celonis publishes a Developer Center with REST APIs across Process Intelligence (Knowledge Model, AI Agent, Event Subscription), data ingestion and push, Machine Learning Workbench, Team, Permissions and SCIM, plus an official hosted Agent Tools (MCP) server, the PyCelonis Python SDK and the content-cli. Auth is via OAuth 2.0 (recommended) or API keys, with page-based pagination, x-ratelimit signaling and OData-style querying on the Knowledge Model API.
image: https://delivery-p141552-e1488202.adobeaemcloud.com/adobe/assets/urn:aaid:aem:df855fa1-2c83-4a48-8cad-536a7d5cb952/as/Meta_Image.png
layout: provider
mcp_servers:
- description: ''
  name: celonis-mcp.yml
  slug: celonis-mcpyml
modified: '2026-07-18'
name: Celonis
nav: Providers
network: true
overview: 'Celonis publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Agents - Conversation API, Beta: OData Protocol API, Beta: Semantics for 3P AI Agents API, and 14 more. Tagged areas include Company, Automation, Process Mining, Process Intelligence, and Data.


  The Celonis catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Celonis'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 28 more developer resources.'
random_paper: 35
scopes:
- name: Celonis Scopes
  scope_count: 2
  slug: celonis-scopes
  summary_line: 2 scopes
score:
  band: strong
  composite: 62.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.4
    developer_ergonomics: 87.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 62.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Celonis Authentication
  slug: celonis-authentication
  summary_line: oauth2/http/apiKey · 4 schemes
- kind: domain-security
  name: Celonis Domain Security
  slug: celonis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Celonis Trust Center
  slug: celonis-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR, CSA STAR
slug: celonis
tags:
- Company
- Automation
- Process Mining
- Process Intelligence
- Data
- Analytics
- Machine Learning
- AI Agents
- Enterprise
website: https://www.celonis.com
---
