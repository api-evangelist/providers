---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 131
  human_in_the_loop: 3
  name: Fusio Agentic Access
  operation_count: 275
  slug: fusio-agentic-access
  summary_line: 275 operations · 131 acting · 3 human-in-the-loop
api_count: 4
apis:
- description: The Fusio Worker API enables executing API action logic in multiple programming languages by forwarding requests to external worker processes. Workers are implemented in the target language (JavaScrip
  name: Fusio Worker API
  slug: fusio-worker-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The account API from Fusio — 9 operation(s) for account.
  name: Fusio Account API
  slug: fusio-account-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The action API from Fusio — 6 operation(s) for action.
  name: Fusio Action API
  slug: fusio-action-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The agent API from Fusio — 7 operation(s) for agent.
  name: Fusio Agent API
  slug: fusio-agent-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The app API from Fusio — 5 operation(s) for app.
  name: Fusio App API
  slug: fusio-app-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The audit API from Fusio — 2 operation(s) for audit.
  name: Fusio Audit API
  slug: fusio-audit-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The authorization API from Fusio — 2 operation(s) for authorization.
  name: Fusio Authorization API
  slug: fusio-authorization-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The backup API from Fusio — 2 operation(s) for backup.
  name: Fusio Backup API
  slug: fusio-backup-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The bundle API from Fusio — 3 operation(s) for bundle.
  name: Fusio Bundle API
  slug: fusio-bundle-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The category API from Fusio — 2 operation(s) for category.
  name: Fusio Category API
  slug: fusio-category-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The config API from Fusio — 2 operation(s) for config.
  name: Fusio Config API
  slug: fusio-config-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The connection API from Fusio — 14 operation(s) for connection.
  name: Fusio Connection API
  slug: fusio-connection-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The cronjob API from Fusio — 2 operation(s) for cronjob.
  name: Fusio Cronjob API
  slug: fusio-cronjob-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The dashboard API from Fusio — 1 operation(s) for dashboard.
  name: Fusio Dashboard API
  slug: fusio-dashboard-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The event API from Fusio — 4 operation(s) for event.
  name: Fusio Event API
  slug: fusio-event-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The firewall API from Fusio — 2 operation(s) for firewall.
  name: Fusio Firewall API
  slug: fusio-firewall-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The form API from Fusio — 4 operation(s) for form.
  name: Fusio Form API
  slug: fusio-form-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The generator API from Fusio — 2 operation(s) for generator.
  name: Fusio Generator API
  slug: fusio-generator-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The grant API from Fusio — 2 operation(s) for grant.
  name: Fusio Grant API
  slug: fusio-grant-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The identity API from Fusio — 7 operation(s) for identity.
  name: Fusio Identity API
  slug: fusio-identity-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The log API from Fusio — 6 operation(s) for log.
  name: Fusio Log API
  slug: fusio-log-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The marketplace API from Fusio — 6 operation(s) for marketplace.
  name: Fusio Marketplace API
  slug: fusio-marketplace-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The operation API from Fusio — 2 operation(s) for operation.
  name: Fusio Operation API
  slug: fusio-operation-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The page API from Fusio — 4 operation(s) for page.
  name: Fusio Page API
  slug: fusio-page-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The payment API from Fusio — 2 operation(s) for payment.
  name: Fusio Payment API
  slug: fusio-payment-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The plan API from Fusio — 4 operation(s) for plan.
  name: Fusio Plan API
  slug: fusio-plan-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The rate API from Fusio — 2 operation(s) for rate.
  name: Fusio Rate API
  slug: fusio-rate-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The role API from Fusio — 2 operation(s) for role.
  name: Fusio Role API
  slug: fusio-role-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The schema API from Fusio — 4 operation(s) for schema.
  name: Fusio Schema API
  slug: fusio-schema-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The scope API from Fusio — 5 operation(s) for scope.
  name: Fusio Scope API
  slug: fusio-scope-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The sdk API from Fusio — 1 operation(s) for sdk.
  name: Fusio SDK API
  slug: fusio-sdk-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The specification API from Fusio — 3 operation(s) for specification.
  name: Fusio Specification API
  slug: fusio-specification-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The statistic API from Fusio — 17 operation(s) for statistic.
  name: Fusio Statistic API
  slug: fusio-statistic-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The System API from Fusio — 7 operation(s) for system.
  name: Fusio System API
  slug: fusio-system-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The taxonomy API from Fusio — 2 operation(s) for taxonomy.
  name: Fusio Taxonomy API
  slug: fusio-taxonomy-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The tenant API from Fusio — 1 operation(s) for tenant.
  name: Fusio Tenant API
  slug: fusio-tenant-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The test API from Fusio — 2 operation(s) for test.
  name: Fusio Test API
  slug: fusio-test-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The token API from Fusio — 4 operation(s) for token.
  name: Fusio Token API
  slug: fusio-token-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The transaction API from Fusio — 4 operation(s) for transaction.
  name: Fusio Transaction API
  slug: fusio-transaction-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The trash API from Fusio — 2 operation(s) for trash.
  name: Fusio Trash API
  slug: fusio-trash-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The trigger API from Fusio — 2 operation(s) for trigger.
  name: Fusio Trigger API
  slug: fusio-trigger-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The user API from Fusio — 3 operation(s) for user.
  name: Fusio User API
  slug: fusio-user-api
- baseURL: https://demo.fusio-project.org
  baseurl_source: declared
  description: The webhook API from Fusio — 4 operation(s) for webhook.
  name: Fusio Webhook API
  slug: fusio-webhook-api
artifact_total: 240
asyncapis:
- description: ''
  name: Fusio Webhooks
  slug: fusio-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/fusio/agentic-access/fusio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fusio-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/fusio/rules/fusio-rules.yml
  title: ''
  type: Spectral
  url: rules/fusio-rules.yml
- group: design
  href: https://artifacts.apis.io/fusio/json-ld/fusio-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/fusio-context.jsonld
- group: design
  href: https://artifacts.apis.io/fusio/vocabulary/fusio-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/fusio-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/fusio/hosts/fusio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fusio-hosts.yml
- group: build
  href: https://artifacts.apis.io/fusio/integrations/fusio-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/fusio-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/fusio/vendors/fusio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/fusio-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/fusio/finops/fusio-finops.yml
  title: ''
  type: FinOps
  url: finops/fusio-finops.yml
- group: other
  href: https://artifacts.apis.io/fusio/capabilities/fusio-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fusio-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/fusio/overlays/fusio-consumer-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fusio-consumer-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fusio/overlays/fusio-system-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fusio-system-overlay.yaml
- group: other
  href: https://artifacts.apis.io/fusio/overlays/fusio-authorization-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fusio-authorization-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.fusio-project.org/
- group: docs
  href: https://artifacts.apis.io/fusio/openapi/_original/fusio-backend.json
  title: ''
  type: OpenAPI
  url: openapi/_original/fusio-backend.json
- group: agent
  href: https://artifacts.apis.io/fusio/mcp/fusio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fusio-mcp.yml
- group: build
  href: https://artifacts.apis.io/fusio/mcp/fusio-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fusio-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/fusio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/fusio/well-known/fusio-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fusio-well-known.yml
- group: other
  href: https://artifacts.apis.io/fusio/well-known/fusio-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/fusio-api-catalog.json
- group: auth
  href: https://artifacts.apis.io/fusio/well-known/fusio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/fusio-security.txt
- group: auth
  href: https://artifacts.apis.io/fusio/security/fusio-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/fusio-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fusio/security/fusio-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fusio-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/fusio/errors/fusio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fusio-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fusio/lifecycle/fusio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fusio-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/fusio/lifecycle/fusio-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/fusio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/fusio/conformance/fusio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fusio-conformance.yml
- group: design
  href: https://artifacts.apis.io/fusio/data-model/fusio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fusio-data-model.yml
- group: design
  href: https://artifacts.apis.io/fusio/asyncapi/fusio-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/fusio-webhooks.yml
- group: build
  href: https://artifacts.apis.io/fusio/packages/fusio-packages.yml
  title: ''
  type: Packages
  url: packages/fusio-packages.yml
- group: build
  href: https://artifacts.apis.io/fusio/cli/fusio-cli.yml
  title: ''
  type: CLI
  url: cli/fusio-cli.yml
- group: design
  href: https://artifacts.apis.io/fusio/components/fusio-components.yml
  title: ''
  type: Components
  url: components/fusio-components.yml
- group: start
  href: https://artifacts.apis.io/fusio/sandbox/fusio-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/fusio-sandbox.yml
- group: other
  href: https://artifacts.apis.io/fusio/overlays/fusio-backend-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fusio-backend-overlay.yaml
- group: operate
  href: https://artifacts.apis.io/fusio/rate-limits/fusio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fusio-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fusio/plans/fusio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fusio-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/fusio/changelog/fusio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fusio-changelog.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fusio-project.org/developers
- group: docs
  title: ''
  type: APIReference
  url: https://demo.fusio-project.org/apps/redoc
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/apioo/fusio/milestones
- group: start
  title: ''
  type: Demo
  url: https://www.fusio-project.org/demo
- group: auth
  href: https://artifacts.apis.io/fusio/authentication/fusio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fusio-authentication.yml
- group: auth
  href: https://artifacts.apis.io/fusio/scopes/fusio-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fusio-scopes.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apioo/fusio/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apioo/fusio/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apioo/fusio/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apioo/fusio/blob/master/LICENSE
- group: auth
  href: https://artifacts.apis.io/fusio/security/fusio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fusio-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fusio-project.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fusio-project.org/docs/bootstrap
- group: company
  title: ''
  type: Blog
  url: https://www.fusio-project.org/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/apioo/fusio/blob/master/CHANGELOG.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apioo
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apioo/fusio
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/eMrMgwsc6e
- group: other
  title: ''
  type: Marketplace
  url: https://www.fusio-project.org/marketplace
- group: build
  title: ''
  type: SDKs
  url: https://docs.fusio-project.org/docs/backend/development/sdk
created: '2026-03-16'
description: 'Fusio is Apache-2.0, self-hosted API management from apioo (Christoph Kappestein, Germany). An operator installs it and builds APIs inside it: an operation binds an HTTP method and path to an action (SQL, HTTP, MongoDB, Elasticsearch, an LLM agent, or code running in a JavaScript, Python, Java or PHP worker) and a TypeSchema-defined request and response shape. Every instance then generates its own machine-readable contract live - OpenAPI 3.0.3, OpenRPC 1.3.0 and TypeAPI - and serves an RFC 9727 api-catalog, RFC 8414 and RFC 9728 OAuth metadata, OpenID Connect discovery and an RFC 9116 security.txt out of the box. It ships its own OAuth2 authorization server, an Angular developer portal, a rate-limiting and monetization layer, a webhook and trigger system, and an MCP server that turns every published operation into an agent tool. There is no vendor-hosted tier and no pricing: the software is the product.'
features:
- description: Route and manage incoming API requests with built-in rate limiting and authentication.
  name: API Gateway
- description: Self-service developer portal for API consumers to register, browse APIs, and manage access tokens.
  name: Developer Portal
- description: Execute API action logic in JavaScript, Python, Java, PHP, and other languages through worker processes.
  name: Multi-Language Workers
- description: Browse and install pre-built API actions and adapters from the Fusio marketplace.
  name: Marketplace
- description: Define and manage API request and response schemas using TypeSchema format.
  name: Schema Management
- description: Built-in OAuth2 server for securing APIs with token-based authentication.
  name: OAuth2 Authentication
- description: Configure per-app and per-user rate limits to protect API resources.
  name: Rate Limiting
- description: Define webhook subscriptions to notify consumers of events.
  name: Webhook Support
finops:
- has_sources: true
  method: derived
  name: Fusio Finops
  primary_unit: ''
  service_category: ''
  slug: fusio-finops
  template: true
image: /assets/icons/fusio.png
integrations:
- description: Connect to MySQL and PostgreSQL databases as data sources for API endpoints.
  name: MySQL and PostgreSQL
- description: Use MongoDB as a NoSQL data source for API endpoints.
  name: MongoDB
- description: Integrate with Elasticsearch for search-powered API endpoints.
  name: Elasticsearch
- description: Use RabbitMQ for asynchronous message processing in API workflows.
  name: RabbitMQ
- description: Deploy Fusio and worker containers using Docker and Docker Compose.
  name: Docker
json_schemas:
- name: Backend_AccountChangePassword
  property_count: 3
  slug: fusio-backend-account-change-password
- name: Backend_ActionCollection
  property_count: 4
  slug: fusio-backend-action-collection
- name: Backend_ActionCommitCollection
  property_count: 4
  slug: fusio-backend-action-commit-collection
- name: Backend_ActionExecuteRequest
  property_count: 5
  slug: fusio-backend-action-execute-request
- name: Backend_ActionExecuteResponse
  property_count: 3
  slug: fusio-backend-action-execute-response
- name: Backend_ActionIndex
  property_count: 1
  slug: fusio-backend-action-index
- name: Backend_Action
  property_count: 7
  slug: fusio-backend-action
- name: Backend_AgentCollection
  property_count: 4
  slug: fusio-backend-agent-collection
- name: Backend_AgentMessageCollection
  property_count: 4
  slug: fusio-backend-agent-message-collection
- name: Backend_Agent
  property_count: 14
  slug: fusio-backend-agent
- name: Backend_AppCollection
  property_count: 4
  slug: fusio-backend-app-collection
- name: Backend_App
  property_count: 12
  slug: fusio-backend-app
- name: Backend_AuditCollection
  property_count: 4
  slug: fusio-backend-audit-collection
- name: Backend_Audit
  property_count: 8
  slug: fusio-backend-audit
- name: Backend_BackupExport
  property_count: 1
  slug: fusio-backend-backup-export
- name: Backend_BackupImportResult
  property_count: 3
  slug: fusio-backend-backup-import-result
- name: Backend_BackupImport
  property_count: 1
  slug: fusio-backend-backup-import
- name: Backend_BundleCollection
  property_count: 4
  slug: fusio-backend-bundle-collection
- name: Backend_BundleCreate
  property_count: 8
  slug: fusio-backend-bundle-create
- name: Backend_Bundle
  property_count: 8
  slug: fusio-backend-bundle
- name: Backend_BundleUpdate
  property_count: 8
  slug: fusio-backend-bundle-update
- name: Backend_CategoryCollection
  property_count: 4
  slug: fusio-backend-category-collection
- name: Backend_CategoryCreate
  property_count: 2
  slug: fusio-backend-category-create
- name: Backend_Category
  property_count: 2
  slug: fusio-backend-category
- name: Backend_CategoryUpdate
  property_count: 2
  slug: fusio-backend-category-update
- name: Backend_ConfigCollection
  property_count: 4
  slug: fusio-backend-config-collection
- name: Backend_Config
  property_count: 5
  slug: fusio-backend-config
- name: Backend_ConfigUpdate
  property_count: 5
  slug: fusio-backend-config-update
- name: Backend_Connection
  property_count: 6
  slug: fusio-backend-connection
- name: Backend_CronjobCollection
  property_count: 4
  slug: fusio-backend-cronjob-collection
- name: Backend_CronjobCreate
  property_count: 8
  slug: fusio-backend-cronjob-create
- name: Backend_Cronjob
  property_count: 8
  slug: fusio-backend-cronjob
- name: Backend_CronjobUpdate
  property_count: 8
  slug: fusio-backend-cronjob-update
- name: Backend_Dashboard
  property_count: 9
  slug: fusio-backend-dashboard
- name: Backend_DatabaseRowCollection
  property_count: 4
  slug: fusio-backend-database-row-collection
- name: Backend_DatabaseTableCollection
  property_count: 4
  slug: fusio-backend-database-table-collection
- name: Backend_DatabaseTable
  property_count: 5
  slug: fusio-backend-database-table
- name: Backend_EventCollection
  property_count: 4
  slug: fusio-backend-event-collection
- name: Backend_EventCreate
  property_count: 5
  slug: fusio-backend-event-create
- name: Backend_Event
  property_count: 5
  slug: fusio-backend-event
- name: Backend_FirewallCollection
  property_count: 4
  slug: fusio-backend-firewall-collection
- name: Backend_FirewallCreate
  property_count: 6
  slug: fusio-backend-firewall-create
- name: Backend_Firewall
  property_count: 6
  slug: fusio-backend-firewall
- name: Backend_FirewallUpdate
  property_count: 6
  slug: fusio-backend-firewall-update
- name: Backend_FormCollection
  property_count: 4
  slug: fusio-backend-form-collection
- name: Backend_FormCreate
  property_count: 6
  slug: fusio-backend-form-create
- name: Backend_Form
  property_count: 6
  slug: fusio-backend-form
- name: Backend_GeneratorIndexProviders
  property_count: 1
  slug: fusio-backend-generator-index-providers
- name: Backend_GeneratorProviderChangelog
  property_count: 3
  slug: fusio-backend-generator-provider-changelog
- name: Backend_GeneratorProviderConfig
  property_count: 0
  slug: fusio-backend-generator-provider-config
- name: Backend_GeneratorProvider
  property_count: 4
  slug: fusio-backend-generator-provider
- name: Backend_HttpRequest
  property_count: 4
  slug: fusio-backend-http-request
- name: Backend_HttpResponse
  property_count: 3
  slug: fusio-backend-http-response
- name: Backend_IdentityCollection
  property_count: 4
  slug: fusio-backend-identity-collection
- name: Backend_IdentityIndex
  property_count: 1
  slug: fusio-backend-identity-index
- name: Backend_Identity
  property_count: 8
  slug: fusio-backend-identity
- name: Backend_LogCollection
  property_count: 4
  slug: fusio-backend-log-collection
- name: Backend_LogErrorCollection
  property_count: 4
  slug: fusio-backend-log-error-collection
- name: Backend_LogError
  property_count: 7
  slug: fusio-backend-log-error
- name: Backend_Log
  property_count: 9
  slug: fusio-backend-log
- name: Backend_OperationCollection
  property_count: 4
  slug: fusio-backend-operation-collection
- name: Backend_OperationCreate
  property_count: 18
  slug: fusio-backend-operation-create
- name: Backend_Operation
  property_count: 18
  slug: fusio-backend-operation
- name: Backend_OperationUpdate
  property_count: 18
  slug: fusio-backend-operation-update
- name: Backend_PageCollection
  property_count: 4
  slug: fusio-backend-page-collection
- name: Backend_PageCreate
  property_count: 6
  slug: fusio-backend-page-create
- name: Backend_Page
  property_count: 6
  slug: fusio-backend-page
- name: Backend_PlanCollection
  property_count: 4
  slug: fusio-backend-plan-collection
- name: Backend_PlanCreate
  property_count: 9
  slug: fusio-backend-plan-create
- name: Backend_Plan
  property_count: 9
  slug: fusio-backend-plan
- name: Backend_RateCollection
  property_count: 4
  slug: fusio-backend-rate-collection
- name: Backend_RateCreate
  property_count: 7
  slug: fusio-backend-rate-create
- name: Backend_Rate
  property_count: 7
  slug: fusio-backend-rate
- name: Backend_RateUpdate
  property_count: 7
  slug: fusio-backend-rate-update
- name: Backend_RoleCollection
  property_count: 4
  slug: fusio-backend-role-collection
- name: Backend_RoleCreate
  property_count: 4
  slug: fusio-backend-role-create
- name: Backend_Role
  property_count: 4
  slug: fusio-backend-role
- name: Backend_RoleUpdate
  property_count: 4
  slug: fusio-backend-role-update
- name: Backend_SchemaCollection
  property_count: 4
  slug: fusio-backend-schema-collection
- name: Backend_SchemaCommitCollection
  property_count: 4
  slug: fusio-backend-schema-commit-collection
- name: Backend_SchemaCreate
  property_count: 5
  slug: fusio-backend-schema-create
- name: Backend_SchemaPreviewResponse
  property_count: 1
  slug: fusio-backend-schema-preview-response
- name: Backend_Schema
  property_count: 5
  slug: fusio-backend-schema
- name: Backend_Scope
  property_count: 5
  slug: fusio-backend-scope
- name: Backend_SdkGenerate
  property_count: 2
  slug: fusio-backend-sdk-generate
- name: Backend_SdkMessage
  property_count: 3
  slug: fusio-backend-sdk-message
- name: Backend_SdkResponse
  property_count: 1
  slug: fusio-backend-sdk-response
- name: Backend_SpecificationChangelog
  property_count: 4
  slug: fusio-backend-specification-changelog
- name: Backend_SpecificationGet
  property_count: 1
  slug: fusio-backend-specification-get
- name: Backend_SpecificationPublish
  property_count: 3
  slug: fusio-backend-specification-publish
- name: Backend_StatisticChart
  property_count: 2
  slug: fusio-backend-statistic-chart
- name: Backend_StatisticCount
  property_count: 3
  slug: fusio-backend-statistic-count
- name: Backend_TaxonomyCollection
  property_count: 4
  slug: fusio-backend-taxonomy-collection
- name: Backend_TaxonomyCreate
  property_count: 3
  slug: fusio-backend-taxonomy-create
- name: Backend_TaxonomyMove
  property_count: 6
  slug: fusio-backend-taxonomy-move
- name: Backend_Taxonomy
  property_count: 3
  slug: fusio-backend-taxonomy
- name: Backend_TaxonomyUpdate
  property_count: 3
  slug: fusio-backend-taxonomy-update
- name: Backend_TestCollection
  property_count: 4
  slug: fusio-backend-test-collection
- name: Backend_Test
  property_count: 6
  slug: fusio-backend-test
- name: Backend_TokenCollection
  property_count: 4
  slug: fusio-backend-token-collection
- name: Backend_Token
  property_count: 7
  slug: fusio-backend-token
- name: Backend_TransactionCollection
  property_count: 4
  slug: fusio-backend-transaction-collection
- name: Backend_Transaction
  property_count: 9
  slug: fusio-backend-transaction
- name: Backend_TrashDataCollection
  property_count: 4
  slug: fusio-backend-trash-data-collection
- name: Backend_TrashRestore
  property_count: 1
  slug: fusio-backend-trash-restore
- name: Backend_TrashTypes
  property_count: 1
  slug: fusio-backend-trash-types
- name: Backend_TriggerCollection
  property_count: 4
  slug: fusio-backend-trigger-collection
- name: Backend_TriggerCreate
  property_count: 5
  slug: fusio-backend-trigger-create
- name: Backend_Trigger
  property_count: 5
  slug: fusio-backend-trigger
- name: Backend_TriggerUpdate
  property_count: 5
  slug: fusio-backend-trigger-update
- name: Backend_UserCollection
  property_count: 4
  slug: fusio-backend-user-collection
- name: Backend_UserCreate
  property_count: 12
  slug: fusio-backend-user-create
- name: Backend_User
  property_count: 11
  slug: fusio-backend-user
- name: Backend_UserUpdate
  property_count: 11
  slug: fusio-backend-user-update
- name: Backend_WebhookCollection
  property_count: 4
  slug: fusio-backend-webhook-collection
- name: Backend_Webhook
  property_count: 6
  slug: fusio-backend-webhook
- name: Common_FormContainer
  property_count: 1
  slug: fusio-common-form-container
- name: Common_Message
  property_count: 3
  slug: fusio-common-message
- name: Consumer_AgentCollection
  property_count: 4
  slug: fusio-consumer-agent-collection
- name: Consumer_AgentMessageCollection
  property_count: 4
  slug: fusio-consumer-agent-message-collection
- name: Consumer_Agent
  property_count: 3
  slug: fusio-consumer-agent
- name: Consumer_AppCollection
  property_count: 4
  slug: fusio-consumer-app-collection
- name: Consumer_AppCreate
  property_count: 3
  slug: fusio-consumer-app-create
- name: Consumer_App
  property_count: 10
  slug: fusio-consumer-app
- name: Consumer_AuthorizeMeta
  property_count: 3
  slug: fusio-consumer-authorize-meta
- name: Consumer_AuthorizeRequest
  property_count: 6
  slug: fusio-consumer-authorize-request
- name: Consumer_AuthorizeResponse
  property_count: 5
  slug: fusio-consumer-authorize-response
- name: Consumer_EventCollection
  property_count: 4
  slug: fusio-consumer-event-collection
- name: Consumer_Event
  property_count: 4
  slug: fusio-consumer-event
- name: Consumer_FormCollection
  property_count: 4
  slug: fusio-consumer-form-collection
- name: Consumer_Form
  property_count: 7
  slug: fusio-consumer-form
- name: Consumer_GrantCollection
  property_count: 4
  slug: fusio-consumer-grant-collection
- name: Consumer_IdentityCollection
  property_count: 4
  slug: fusio-consumer-identity-collection
- name: Consumer_LogCollection
  property_count: 4
  slug: fusio-consumer-log-collection
- name: Consumer_Log
  property_count: 9
  slug: fusio-consumer-log
- name: Consumer_PageCollection
  property_count: 4
  slug: fusio-consumer-page-collection
- name: Consumer_Page
  property_count: 5
  slug: fusio-consumer-page
- name: Consumer_PaymentCheckoutRequest
  property_count: 2
  slug: fusio-consumer-payment-checkout-request
- name: Consumer_PaymentCheckoutResponse
  property_count: 1
  slug: fusio-consumer-payment-checkout-response
- name: Consumer_PaymentPortalRequest
  property_count: 1
  slug: fusio-consumer-payment-portal-request
- name: Consumer_PaymentPortalResponse
  property_count: 1
  slug: fusio-consumer-payment-portal-response
- name: Consumer_PlanCollection
  property_count: 4
  slug: fusio-consumer-plan-collection
- name: Consumer_Plan
  property_count: 7
  slug: fusio-consumer-plan
- name: Consumer_TokenAccessToken
  property_count: 5
  slug: fusio-consumer-token-access-token
- name: Consumer_TokenCollection
  property_count: 4
  slug: fusio-consumer-token-collection
- name: Consumer_TokenCreate
  property_count: 3
  slug: fusio-consumer-token-create
- name: Consumer_Token
  property_count: 7
  slug: fusio-consumer-token
- name: Consumer_TransactionCollection
  property_count: 4
  slug: fusio-consumer-transaction-collection
- name: Consumer_Transaction
  property_count: 10
  slug: fusio-consumer-transaction
- name: Consumer_UserAccount
  property_count: 10
  slug: fusio-consumer-user-account
- name: Consumer_WebhookCollection
  property_count: 4
  slug: fusio-consumer-webhook-collection
- name: Consumer_WebhookCreate
  property_count: 3
  slug: fusio-consumer-webhook-create
- name: Consumer_Webhook
  property_count: 6
  slug: fusio-consumer-webhook
- name: MarketplaceActionCollection
  property_count: 4
  slug: fusio-marketplace-action-collection
- name: MarketplaceAction
  property_count: 12
  slug: fusio-marketplace-action
- name: MarketplaceAppCollection
  property_count: 4
  slug: fusio-marketplace-app-collection
- name: MarketplaceApp
  property_count: 13
  slug: fusio-marketplace-app
- name: MarketplaceBundleCollection
  property_count: 4
  slug: fusio-marketplace-bundle-collection
- name: MarketplaceBundle
  property_count: 11
  slug: fusio-marketplace-bundle
- name: Passthru
  property_count: 0
  slug: fusio-passthru
- name: System_About
  property_count: 14
  slug: fusio-system-about
- name: System_HealthCheck
  property_count: 2
  slug: fusio-system-health-check
- name: System_Route
  property_count: 1
  slug: fusio-system-route
- name: System_Schema
  property_count: 2
  slug: fusio-system-schema
jsonld:
- class_count: 120
  name: Fusio Context
  property_count: 156
  slug: fusio-context
layout: provider
mcp_servers:
- description: 'Fusio ships a first-party Model Context Protocol server inside the product itself. It is not a separate package or a hosted vendor endpoint: every Fusio instance can expose its own operations as MCP t'
  name: Fusio MCP Server
  slug: fusio-mcp-server
modified: '2026-09-16'
name: Fusio
nav: Providers
network: true
overview: 'Fusio publishes 43 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Action API, Agent API, and 40 more. Tagged areas include API Management, Open Source, REST API, API Gateway, and Developer Portal.


  The Fusio catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Fusio''s developer surface includes CLI, sandbox, changelog, API reference, authentication, documentation, getting-started guide, and 49 more developer resources.'
plans:
- name: Fusio Plans Pricing
  plan_count: 0
  slug: fusio-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Fusio Rate Limits
  slug: fusio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Fusio API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: fusio-rules
scopes:
- name: Fusio Scopes
  scope_count: 58
  slug: fusio-scopes
  summary_line: 58 scopes · clientCredentials/authorizationCode
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 37
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 35.6
    contract_quality: 73.5
    developer_ergonomics: 80.4
    discoverability: 73.3
    operational_transparency: 71.1
  open_source:
    applies: true
    score: 50.0
  previous_composite: 59.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 42
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/fusio/fusio-2026-06-20T181622.png
security:
- kind: authentication
  name: Fusio Authentication
  slug: fusio-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Fusio Domain Security
  slug: fusio-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Fusio Vulnerability Disclosure
  slug: fusio-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: fusio-events-and-webhooks
  slug: fusio-events-and-webhooks
- name: fusio-onboard-a-consumer
  slug: fusio-onboard-a-consumer
- name: fusio-publish-an-operation
  slug: fusio-publish-an-operation
- name: fusio-restore-a-deleted-record
  slug: fusio-restore-a-deleted-record
slug: fusio
tags:
- API Management
- Open Source
- REST API
- API Gateway
- Developer Portal
- OpenAPI
- Self-Hosted
- MCP
use_cases:
- description: Build and publish API products with documentation, authentication, and developer onboarding.
  name: API Product Building
- description: Use Fusio as an API gateway in front of microservices for unified access control.
  name: Microservices Gateway
- description: Connect to databases and external APIs to build data integration endpoints.
  name: Data Integration
- description: Build API backends that execute logic in multiple languages without managing servers.
  name: Serverless API Backend
website: https://www.fusio-project.org/
---
