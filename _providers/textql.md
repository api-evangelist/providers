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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.6
  scored_at: '2026-09-16'
api_count: 15
apis:
- description: TextQL's hosted, remote Model Context Protocol server. Any MCP-compatible client — Claude, Claude Code, Cursor, Windsurf, ChatGPT, Microsoft Copilot — points at the endpoint, authorizes once over OAut
  name: Ana MCP Server
  slug: textql-ana-mcp-server
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The AgentService API from TextQL — 13 operation(s) for agentservice.
  name: TextQL Agent Service API
  slug: textql-agentservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Mint and revoke scoped platform API keys
  name: TextQL API Keys API
  slug: textql-api-keys-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: 'AppService manages data apps: the generative app execution primitive. An app is agent-authored single-file HTML/JS/CSS executing in a CSP sandbox, fed a snapshot of its declared data sources. First-cl'
  name: TextQL App Service API
  slug: textql-appservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The AuditLogService API from TextQL — 11 operation(s) for auditlogservice.
  name: TextQL Audit Log Service API
  slug: textql-auditlogservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Review, approve, and deny Ontology changes
  name: TextQL Changes API
  slug: textql-changes-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Create and manage AI chat sessions
  name: TextQL Chat API
  slug: textql-chat-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The ChatService API from TextQL — 38 operation(s) for chatservice.
  name: TextQL Chat Service API
  slug: textql-chatservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: List available data connectors
  name: TextQL Connectors API
  slug: textql-connectors-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The ConnectorService API from TextQL — 17 operation(s) for connectorservice.
  name: TextQL Connector Service API
  slug: textql-connectorservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The DashboardService API from TextQL — 24 operation(s) for dashboardservice.
  name: TextQL Dashboard Service API
  slug: textql-dashboardservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The DatasetService API from TextQL — 14 operation(s) for datasetservice.
  name: TextQL Dataset Service API
  slug: textql-datasetservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The MCPService API from TextQL — 7 operation(s) for mcpservice.
  name: TextQL MCP Service API
  slug: textql-mcpservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The Members API from TextQL — 5 operation(s) for members.
  name: TextQL Members API
  slug: textql-members-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The MetricsExportService API from TextQL — 5 operation(s) for metricsexportservice.
  name: TextQL Metrics Export Service API
  slug: textql-metricsexportservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The ObservabilityService API from TextQL — 30 operation(s) for observabilityservice.
  name: TextQL Observability Service API
  slug: textql-observabilityservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The OntologyManagementService API from TextQL — 69 operation(s) for ontologymanagementservice.
  name: TextQL Ontology Management Service API
  slug: textql-ontologymanagementservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Create, configure, and run automated playbooks
  name: TextQL Playbooks API
  slug: textql-playbooks-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The PlaybookService API from TextQL — 39 operation(s) for playbookservice.
  name: TextQL Playbook Service API
  slug: textql-playbookservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The PowerBIService API from TextQL — 10 operation(s) for powerbiservice.
  name: TextQL Power BI Service API
  slug: textql-powerbiservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The Roles API from TextQL — 2 operation(s) for roles.
  name: TextQL Roles API
  slug: textql-roles-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SandboxAdminService API from TextQL — 9 operation(s) for sandboxadminservice.
  name: TextQL Sandbox Admin Service API
  slug: textql-sandboxadminservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SandboxCapabilityService API from TextQL — 6 operation(s) for sandboxcapabilityservice.
  name: TextQL Sandbox Capability Service API
  slug: textql-sandboxcapabilityservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SandboxExecService API from TextQL — 5 operation(s) for sandboxexecservice.
  name: TextQL Sandbox Exec Service API
  slug: textql-sandboxexecservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SandboxQueryService API from TextQL — 2 operation(s) for sandboxqueryservice.
  name: TextQL Sandbox Query Service API
  slug: textql-sandboxqueryservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Manage Python sandbox environments for code execution
  name: TextQL Sandcastles API
  slug: textql-sandcastles-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The ScimService API from TextQL — 6 operation(s) for scimservice.
  name: TextQL SCIM Service API
  slug: textql-scimservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SecretService API from TextQL — 5 operation(s) for secretservice.
  name: TextQL Secret Service API
  slug: textql-secretservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SettingsService API from TextQL — 7 operation(s) for settingsservice.
  name: TextQL Settings Service API
  slug: textql-settingsservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The SlackService API from TextQL — 8 operation(s) for slackservice.
  name: TextQL Slack Service API
  slug: textql-slackservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The TableauService API from TextQL — 13 operation(s) for tableauservice.
  name: TextQL Tableau Service API
  slug: textql-tableauservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: The TeamsService API from TextQL — 8 operation(s) for teamsservice.
  name: TextQL Teams Service API
  slug: textql-teamsservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Platform Agent Service - External API for triggering agent webhooks
  name: TextQL Textql.rpc.platform.Agent Service API
  slug: textql-textql-rpc-platform-agentservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Platform API Access Key Service - External API for managing API access keys
  name: TextQL Textql.rpc.platform.Api Access Key Service API
  slug: textql-textql-rpc-platform-apiaccesskeyservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Platform Chat Service - External API for chat management
  name: TextQL Textql.rpc.platform.Chat Service API
  slug: textql-textql-rpc-platform-chatservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Platform Connector Service - External API for connector management
  name: TextQL Textql.rpc.platform.Connector Service API
  slug: textql-textql-rpc-platform-connectorservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Platform Playbook Service - External API for playbook management
  name: TextQL Textql.rpc.platform.Playbook Service API
  slug: textql-textql-rpc-platform-playbookservice-api
- baseURL: https://app.textql.com/v2
  baseurl_source: declared
  description: Platform Sandbox Service - External API for creating and managing Python sandbox environments
  name: TextQL Textql.rpc.platform.Sandbox Service API
  slug: textql-textql-rpc-platform-sandboxservice-api
- baseURL: https://app.textql.com/mcp
  baseurl_source: declared
  description: RBAC service for managing roles, permissions, and access control
  name: TextQL RBAC Service API
  slug: textql-rbac-service-api
artifact_total: 48
asyncapis:
- description: ''
  name: Textql Webhooks
  slug: textql-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/overlays/textql-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/textql-v2-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/overlays/textql-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/textql-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/overlays/textql-platform-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/textql-platform-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://textql.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.textql.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.textql.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.textql.com/api-reference/v2/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.textql.com/core/get-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://textql.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TextQLLabs
- group: commercial
  title: ''
  type: Pricing
  url: https://textql.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.textql.com/
- group: start
  title: ''
  type: Login
  url: https://app.textql.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.textql.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.textql.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/security/textql-trust-center.yml
  title: ''
  type: Compliance
  url: security/textql-trust-center.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.textql.com/product/changelog
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/a2a/textql-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/textql-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/llms/textql-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/textql-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/well-known/textql-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/textql-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/well-known/textql-openid-configuration.json
  title: ''
  type: OpenIDConnectDiscovery
  url: well-known/textql-openid-configuration.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/packages/textql-packages.yml
  title: ''
  type: Packages
  url: packages/textql-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/packages/textql-packages.yml
  title: ''
  type: SDKs
  url: packages/textql-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/lifecycle/textql-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/textql-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/lifecycle/textql-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/textql-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/security/textql-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/textql-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/plans/textql-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/textql-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/rate-limits/textql-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/textql-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/conformance/textql-conformance.yml
  title: ''
  type: Conformance
  url: conformance/textql-conformance.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/changelog/textql-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/textql-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/components/textql-components.yml
  title: ''
  type: Components
  url: components/textql-components.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/cli/textql-cli.yml
  title: ''
  type: CLI
  url: cli/textql-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/conventions/textql-conventions.yml
  title: ''
  type: Conventions
  url: conventions/textql-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/data-model/textql-data-model.yml
  title: ''
  type: DataModel
  url: data-model/textql-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/authentication/textql-authentication.yml
  title: ''
  type: Authentication
  url: authentication/textql-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/scopes/textql-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/textql-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/errors/textql-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/textql-problem-types.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/mcp/textql-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/textql-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/mcp/textql-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/textql-tool-crosswalk.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/asyncapi/textql-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/textql-webhooks.yml
- group: operate
  title: ''
  type: Support
  url: mailto:support@textql.com
created: '2026-08-30'
description: TextQL is an enterprise AI data platform built around Ana, an AI data scientist that connects to a company's warehouses, databases, BI tools and SaaS APIs and answers questions in plain language. Ana writes SQL, runs Python in a managed gVisor sandbox, searches the web, and produces charts, dashboards, scheduled reports (Playbooks) and long-running monitors (Agents) on top of a governed Ontology semantic layer. TextQL ships a public REST platform API in two generations — a v1 Connect-RPC surface and a REST-native v2 — plus an OAuth-authorized remote MCP server that exposes Ana to Claude, Cursor, ChatGPT, Copilot and any MCP-compatible client. First-party TypeScript and Python SDKs, embeddable iframe surfaces for Ana, dashboards and data apps, SAML/OIDC single sign-on with SCIM 2.0 provisioning, and self-hosted Helm deployment into a customer VPC round out the developer surface.
image: https://raw.githubusercontent.com/api-evangelist/textql/main/images/textql-og-card.png
layout: provider
mcp_servers:
- description: ''
  name: Ana MCP Server
  slug: ana-mcp-server
modified: '2026-08-30'
name: TextQL
nav: Providers
network: true
overview: 'TextQL publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Agent Service API, API Keys API, App Service API, and 35 more. Tagged areas include Company, Artificial Intelligence, Analytics, Business Intelligence, and Data.


  The TextQL catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TextQL''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, changelog, and 35 more developer resources.'
plans:
- name: Textql Plans Pricing
  plan_count: 3
  slug: textql-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Textql Rate Limits
  slug: textql-rate-limits
scopes:
- name: Textql Scopes
  scope_count: 0
  slug: textql-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 66.9
  coverage:
    artifact_dirs: 25
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 57.2
    developer_ergonomics: 78.6
    discoverability: 57.4
    operational_transparency: 42.1
  previous_composite: 67.6
  provenance:
    conformance: first-party
    contracts:
      callable: 84.2
      derived: 0
      marker_coverage: 0.0
      total: 38
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://raw.githubusercontent.com/api-evangelist/textql/refs/heads/main/screenshots/textql-2026-09-02T163306.png
security:
- kind: authentication
  name: Textql Authentication
  slug: textql-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Textql Domain Security
  slug: textql-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Textql Vulnerability Disclosure
  slug: textql-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Textql Trust Center
  slug: textql-trust-center
  summary_line: SOC 2 Type II, HIPAA, GDPR, SOX
slug: textql
tags:
- Company
- Artificial Intelligence
- Analytics
- Business Intelligence
- Data
- Agents
- MCP
- Semantic Layer
- Text-to-SQL
- Data Warehouse
- Enterprise
website: https://textql.com/
---
