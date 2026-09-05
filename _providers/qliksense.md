---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-09-04'
api_count: 82
apis:
- description: JSON-RPC WebSocket API for interacting with the Qlik Associative Engine, creating and manipulating apps, and building visualizations.
  name: Qlik Engine API
  slug: engine-api
- description: gRPC/protobuf contract for extending the Qlik Associative Engine with external compute. A plugin implements the qlik.sse.Connector service and the engine calls out to it for scalar, aggregation and te
  name: Qlik Server-Side Extension Protocol
  slug: server-side-extension
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks
  baseurl_source: declared
  description: 'The Qlik Cloud tenant event surface: 29 AsyncAPI 3.0.0 documents covering 102 message definitions across apps, reloads, spaces, tenants, users, roles, licenses, quotas, OAuth clients, data-integration'
  name: Qlik Cloud System Events
  slug: system-events
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/ai/mcp
  baseurl_source: declared
  description: Qlik's first-party remote Model Context Protocol server, generally available since 2026-02-10 and included from the Starter plan up. It exposes Qlik Cloud analytics — datasets and data quality, data p
  name: Qlik MCP Server
  slug: mcp-server
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/analytics/apps/evaluations
  baseurl_source: declared
  description: Qlik Cloud Apps API. 7 operations published as OpenAPI 3.0.0 at https://qlik.dev/specs/rest/analytics/apps.json
  name: Qlik Apps API
  slug: analytics-apps-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/analytics/change-stores
  baseurl_source: declared
  description: Retrieve user-entered changes from write tables for export or further processing.
  name: Qlik Change stores API
  slug: analytics-change-stores-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/analytics/discovery-agent/adaptive-cards
  baseurl_source: declared
  description: Qlik Cloud Adaptive cards API. 1 operations published as OpenAPI 3.0.0 at https://qlik.dev/specs/rest/analytics/discovery-agent/adaptive-cards.json
  name: Qlik Adaptive cards API
  slug: analytics-discovery-agent-adaptive-cards-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-apps
  baseurl_source: declared
  description: Retrieve and filter on-demand generated analytics applications by type.
  name: Qlik ODAG apps API
  slug: analytics-odag-apps-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-links
  baseurl_source: declared
  description: Create, manage, and retrieve on-demand analytics generation links between selection and template applications.
  name: Qlik ODAG links API
  slug: analytics-odag-links-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-requests
  baseurl_source: declared
  description: Submit, track, and manage on-demand analytics generation requests and their generated applications.
  name: Qlik ODAG requests API
  slug: analytics-odag-requests-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/analytics/odag-settings
  baseurl_source: declared
  description: Read and configure tenant-level on-demand analytics generation settings.
  name: Qlik ODAG settings API
  slug: analytics-odag-settings-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/api-keys
  baseurl_source: declared
  description: API keys can be used by developers to gain programmatic access to the Qlik platform, acting as their own user.
  name: Qlik API keys API
  slug: api-keys-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/apps
  baseurl_source: declared
  description: Manage Qlik Sense applications including creating, updating, publishing, and deleting apps in Qlik Cloud.
  name: Qlik Apps API
  slug: apps-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/assistants
  baseurl_source: declared
  description: Assistants provide a chat interface for asking questions and getting personalized, relevant answers for Qlik Answers.
  name: Qlik Assistants API
  slug: assistants-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/audits
  baseurl_source: declared
  description: Access events emitted upon each action taken in a tenant for detailed audit logging and compliance.
  name: Qlik Audits API
  slug: audits-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/automation-connections
  baseurl_source: declared
  description: Automation Connections are used by Qlik Automate connectors during automation execution.
  name: Qlik Automation connections API
  slug: automation-connections-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/automation-connectors
  baseurl_source: declared
  description: Automation connectors let you integrate third-party services and applications into your data analytics workflows. Use this API to discover available connectors and understand billing characteristics.
  name: Qlik Automation connectors API
  slug: automation-connectors-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/automations
  baseurl_source: declared
  description: Create and manage no-code automation workflows in Qlik Automate that connect applications together.
  name: Qlik Automations API
  slug: automations-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/automl-deployments
  baseurl_source: declared
  description: Use your ML deployment to generate real-time results returned as JSON in a synchronous manner to predict future outcomes on new data.
  name: Qlik AutoML real-time predictions API
  slug: automl-deployments-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/automl-predictions
  baseurl_source: declared
  description: Use your ML deployment to generate batch data in file format to predict future outcomes on new data.
  name: Qlik AutoML dataset predictions API
  slug: automl-predictions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/banners
  baseurl_source: declared
  description: Banners display short messages at the top of the client interface to share tenant-wide information, warnings, or issues. When embedding content, banners aren't shown inside qlik-embed UIs. The only em
  name: Qlik Banners API
  slug: banners-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/brands
  baseurl_source: declared
  description: Brands allow you to apply tenant level branding across most user interfaces.
  name: Qlik Brands API
  slug: brands-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/collections
  baseurl_source: declared
  description: Collections provide the framework to catalog various content a user has access to using tags, public and private collections, and favorites.
  name: Qlik Collections API
  slug: collections-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/conditions
  baseurl_source: declared
  description: Conditions are used by features such as data alerting and subscriptions to determine when action should be taken, based on data in a Qlik app.
  name: Qlik Conditions API
  slug: conditions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/consumption/executions
  baseurl_source: declared
  description: Tracks usage of entitled features in a tenant, used for the consumption metrics in the admin console in a tenant.
  name: Qlik Entitlement consumption API
  slug: consumption-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/core/auth-settings
  baseurl_source: declared
  description: Configure and retrieve authentication settings for your Qlik Cloud tenant.
  name: Qlik Auth settings API
  slug: core-auth-settings-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/core/ip-policies
  baseurl_source: declared
  description: 'IP policies let you control which IP addresses can access your Qlik Cloud tenant. Use this API to manage allowlisting rules by creating, listing, updating, and deleting IP policies. When allowlisting '
  name: Qlik IP Policies API
  slug: core-ip-policies-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/csp-origins
  baseurl_source: declared
  description: CSP origins allow you to configure domains, or origins, that Qlik Sense client visualizations/extensions are allowed to communicate with.
  name: Qlik CSP origins API
  slug: csp-origins-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/csrf-token
  baseurl_source: declared
  description: A CSRF token is a secure random token (e.g., synchronizer token or challenge token) that is used to prevent CSRF attacks. This API retrieves the token for the current user session.
  name: Qlik CSRF token API
  slug: csrf-token-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/data-alerts
  baseurl_source: declared
  description: Supports chart sharing, chart monitoring and alerting features. The legacy sharing APIs refer to chart sharing and chart monitoring, which is a feature that allows the user to send an e-mail with an e
  name: Qlik Data alerts API
  slug: data-alerts-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/data-assets
  baseurl_source: declared
  description: Data assets are part of the catalog in Qlik Cloud. A data asset is a member of a data store, and may contain multiple data sets.
  name: Qlik Data assets API
  slug: data-assets-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/data-connections
  baseurl_source: declared
  description: Create and manage data connections to various data sources in Qlik Cloud.
  name: Qlik Data Connections API
  slug: data-connections-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/data-credentials/actions/filter-orphan
  baseurl_source: declared
  description: Data credentials are the stored credentials leveraged by the data-connections service to connect to external data sources.
  name: Qlik Data credentials API
  slug: data-credentials-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/data-files
  baseurl_source: declared
  description: Data files represent the flat file storage associated with spaces in your Qlik Cloud tenant. Each space will have a corresponding data files connection, which you can list with data-connections.
  name: Qlik Data files API
  slug: data-files-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-products
  baseurl_source: declared
  description: Data products are packages that group related datasets within a single, curated offering. Use the Data products API to create, manage, and activate data products for consumption by business users.
  name: Qlik Data products API
  slug: data-governance-data-products-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/data-governance/data-qualities/batch-computations
  baseurl_source: declared
  description: The Data qualities API enables you to assess the quality of your datasets through asynchronous computations.
  name: Qlik Data qualities API
  slug: data-governance-data-qualities-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/data-governance/trust-scores/results/data-sets/actions/filter
  baseurl_source: declared
  description: The Trust Scores API retrieves the Qlik Trust Score™ for datasets in bulk, including overall score and per-axis and per-metric breakdowns.
  name: Qlik Trust scores API
  slug: data-governance-trust-scores-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/data-qualities/computations
  baseurl_source: declared
  description: API for triggering data quality computations and retrieving global results to assess the quality of your datasets.
  name: Qlik Data qualities API
  slug: data-qualities-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/data-sets
  baseurl_source: declared
  description: Data sets are part of the catalog in Qlik Cloud. A data set is a member of a data asset.
  name: Qlik Data sets API
  slug: data-sets-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/data-sources
  baseurl_source: declared
  description: Lists data sources available on the tenant for the creation of data connections.
  name: Qlik Data sources API
  slug: data-sources-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/data-stores
  baseurl_source: declared
  description: Data stores are part of the catalog in Qlik Cloud. A data store may contain one or more data stores, which in turn may contain multiple data sets.
  name: Qlik Data stores API
  slug: data-stores-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/di-projects
  baseurl_source: declared
  description: Data integration projects are used to group and organize data tasks that move, transform, or prepare data for consumption.
  name: Qlik Data integration projects API
  slug: di-projects-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/direct-access-agents
  baseurl_source: declared
  description: API for remotely managing configuration settings of Direct Access Gateway agents.
  name: Qlik Direct Access Agents API
  slug: direct-access-agents-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/encryption/keyproviders
  baseurl_source: declared
  description: Tenants in Qlik Cloud can be encrypted with a key you provide via a supported KMS. This API allows you to configure and manage encryption keys.
  name: Qlik Encryption API
  slug: encryption-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/extensions
  baseurl_source: declared
  description: Visualization extensions is a capability in Qlik Sense which allows third-party visualizations and other presentation objects to be used in the Qlik Sense client.
  name: Qlik Extensions API
  slug: extensions-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/glossaries
  baseurl_source: declared
  description: A glossary is a collection of common and agreed upon (business) terms, typically focused on defining the meaning of data and described in terms that everyone understands.
  name: Qlik Glossaries API
  slug: glossaries-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/groups
  baseurl_source: declared
  description: Groups is the resource representing a group in the system, to which space and tenant roles can be assigned to simplify access control management.
  name: Qlik Groups API
  slug: groups-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/identity-providers
  baseurl_source: declared
  description: Identity providers define how your users authenticate to your tenant when attempting to access content.
  name: Qlik Identity providers API
  slug: identity-providers-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/items
  baseurl_source: declared
  description: Items provides a list of core resources in the Qlik platform, including resources such as apps, automations, and data sets that a user has access to.
  name: Qlik Items API
  slug: items-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/knowledgebases
  baseurl_source: declared
  description: Knowledgebases are collections of individual data sources, that are indexed for use in generating responses to user questions via Assistants for Qlik Answers.
  name: Qlik Knowledgebases API
  slug: knowledgebases-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/licenses/assignments
  baseurl_source: declared
  description: Licenses define tenant and user entitlements, and can be used in conjunction with the consumption API to get a picture of entitlement usage.
  name: Qlik Licenses API
  slug: licenses-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/lineage-graphs/impact
  baseurl_source: declared
  description: Lineage-graphs represents the lineage information for a specific Qlik item.
  name: Qlik Lineage graphs API
  slug: lineage-graphs-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/login
  baseurl_source: declared
  description: This API is used to initiate interactive logins, or to process JWT login requests.
  name: Qlik Login API
  slug: login-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/ml/deployments
  baseurl_source: declared
  description: Generate profile insights, create and manage ML experiments, deploy models, and run predictions in Qlik Cloud.
  name: Qlik Machine Learning API
  slug: ml-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/notes/settings
  baseurl_source: declared
  description: Notes provide a collaborative experience to support analytics consumption in your tenant. This API enables or disables notes.
  name: Qlik Notes API
  slug: notes-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/notifications
  baseurl_source: declared
  description: Notifications is the resource representing the various notifications that notification-prep can render
  name: Qlik Notifications API
  slug: notifications-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-clients
  baseurl_source: declared
  description: Create and manage the configuration of OAuth clients in your tenant.
  name: Qlik OAuth clients API
  slug: oauth-clients-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/oauth-tokens
  baseurl_source: declared
  description: List and revoke active OAuth tokens issued for your tenant.
  name: Qlik OAuth tokens API
  slug: oauth-tokens-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/questions/actions/ask
  baseurl_source: declared
  description: Parse natural language queries with support for language configuration, visualization generation, and conversation context.
  name: Qlik Natural Language API
  slug: natural-language-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/quotas
  baseurl_source: declared
  description: Quotas returns entitled attributes based on your license.
  name: Qlik Quotas API
  slug: quotas-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/reload-tasks
  baseurl_source: declared
  description: Reloads tasks allow you to schedule reloads of analytics applications in your tenant.
  name: Qlik Reload tasks API
  slug: reload-tasks-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/reloads
  baseurl_source: declared
  description: Trigger and manage data reload operations for Qlik Sense apps.
  name: Qlik Reload API
  slug: reloads-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/report-templates
  baseurl_source: declared
  description: Create and manage report templates for consistent report generation and distribution.
  name: Qlik Report templates API
  slug: report-templates-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/reports
  baseurl_source: declared
  description: Generate downloadable report assets from data with configurable templates and output formats.
  name: Qlik Reports API
  slug: reports-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/roles
  baseurl_source: declared
  description: Tenant roles are assigned to users or groups in the tenant, and define what permissions they have.
  name: Qlik Roles API
  slug: roles-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/scheduling/tasks
  baseurl_source: declared
  description: Qlik Cloud Tasks API. 16 operations published as OpenAPI 3.0.0 at https://qlik.dev/specs/rest/scheduling/tasks.json
  name: Qlik Tasks API
  slug: scheduling-tasks-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/sharing-tasks
  baseurl_source: declared
  description: For scheduled capabilities such as reports, data alerts, subscriptions, and more, sharing tasks defines when these tasks execute, and tie together the resource definition with any conditions on execut
  name: Qlik Sharing tasks API
  slug: sharing-tasks-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/spaces
  baseurl_source: declared
  description: Manage shared and managed spaces for collaboration and content organization in Qlik Cloud.
  name: Qlik Spaces API
  slug: spaces-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/tasks
  baseurl_source: declared
  description: API for managing tasks and task chains in Qlik Cloud. The requesting user needs the "reload" permission on the target resource to use this set of endpoints. A tenant admin can use GET /v1/tasks and DE
  name: Qlik Tasks API
  slug: tasks-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/temp-contents
  baseurl_source: declared
  description: Services such as app and data-files which may import or export larger files can opt to leverage the temporary contents service to handle these requests. Acts as a temporary file store.
  name: Qlik Temporary contents API
  slug: temp-contents-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/tenant-settings
  baseurl_source: declared
  description: Configure tenant-wide settings for security, appearance, and operational preferences.
  name: Qlik Tenant settings API
  slug: tenant-settings-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/tenants
  baseurl_source: declared
  description: Configure and manage Qlik Cloud tenants including settings, licenses, and administrative operations.
  name: Qlik Tenants API
  slug: tenants-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/themes
  baseurl_source: declared
  description: Themes enable you to customize/style the Qlik Sense client experience.
  name: Qlik Themes API
  slug: themes-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/transports/email-config
  baseurl_source: declared
  description: Transports supports configuration of the tenant-level SMTP service. For the SMTP service in Qlik Automate, review the automation-connections API.
  name: Qlik Email configuration API
  slug: transports-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/ui-config/pinned-links
  baseurl_source: declared
  description: Pinned links are administrator-defined URLs which appear for all users under the More button in the global navigation menu.
  name: Qlik Pinned links API
  slug: ui-config-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/users
  baseurl_source: declared
  description: Manage users, groups, and authentication in Qlik Cloud tenants.
  name: Qlik Users API
  slug: users-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/web-integrations
  baseurl_source: declared
  description: A web integration is a resource representing a list of whitelisted origins that can make requests to a specified tenant. It is the implementation of the CORS mechanism within Qlik Cloud.
  name: Qlik Web integrations API
  slug: web-integrations-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/web-notifications
  baseurl_source: declared
  description: Web notifications is the resource representing a user's notification
  name: Qlik Web notifications API
  slug: web-notifications-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1/webhooks
  baseurl_source: declared
  description: Create and manage webhooks to provide other applications with real-time information from Qlik Cloud events.
  name: Qlik Webhooks API
  slug: webhooks-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/workflows/automation-connections
  baseurl_source: declared
  description: Automation Connections are used by Qlik Automate connectors during automation execution.
  name: Qlik Automation connections API
  slug: workflows-automation-connections-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/workflows/automation-connectors
  baseurl_source: declared
  description: Automation connectors let you integrate third-party services and applications into your data analytics workflows. Use this API to discover available connectors and understand billing characteristics.
  name: Qlik Automation connectors API
  slug: workflows-automation-connectors-api
- baseURL: https://{tenant}.{region}.qlikcloud.com/api/workflows/automations
  baseurl_source: declared
  description: Automations in Qlik Automate are no-code workflows which connect applications together.
  name: Qlik Automations API
  slug: workflows-automations-api
artifact_total: 149
asyncapis:
- description: ''
  name: Qliksense Asyncapi Index
  slug: qliksense-asyncapi-index
- description: ''
  name: Qliksense Webhooks
  slug: qliksense-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/qlik-oss/server-side-extension/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.qlik.com/us/products/qlik-sense
- group: start
  title: ''
  type: DeveloperPortal
  url: https://qlik.dev/
- group: start
  title: ''
  type: Portal
  url: https://qlik.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://qlik.dev/apis/
- group: docs
  title: ''
  type: APIReference
  url: https://qlik.dev/apis/rest/
- group: start
  title: ''
  type: GettingStarted
  url: https://qlik.dev/manage/get-started-first-api-call/
- group: auth
  title: ''
  type: Authentication
  url: https://qlik.dev/authenticate
- group: operate
  title: ''
  type: Support
  url: https://support.qlik.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.qlik.com/
- group: company
  title: ''
  type: Blog
  url: https://www.qlik.com/us/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qlik-oss
- group: commercial
  title: ''
  type: Pricing
  url: https://www.qlik.com/us/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.qlik.com/us/trial/qlik-cloud-analytics
- group: start
  title: ''
  type: Login
  url: https://login.qlik.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qlik.com/us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qlik.com/us/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qlikcloud.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://qlik.dev/changelog/
- group: other
  title: ''
  type: RSS
  url: https://qlik.dev/rss.xml
- group: build
  title: ''
  type: CLI
  url: https://qlik.dev/toolkits/qlik-cli/
- group: build
  title: ''
  type: SDKs
  url: packages/qliksense-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/qliksense-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qliksense-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/qliksense-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qliksense-llms.txt
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/qliksense-asyncapi-index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/qliksense-webhooks.yml
- group: other
  title: ''
  type: Protobuf
  url: grpc/qliksense-server-side-extension.proto
- group: other
  title: ''
  type: OpenRPC
  url: json-rpc/qliksense-qix-openrpc.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/qliksense-qtcp-project.schema.json
- group: design
  title: ''
  type: Conformance
  url: conformance/qliksense-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/qliksense-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/qliksense-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: security/qliksense-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qliksense-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qliksense-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/qliksense-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qliksense-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/qliksense-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/qliksense-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qliksense-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qliksense-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/qliksense-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/qliksense-cli.yml
- group: design
  title: ''
  type: Components
  url: components/qliksense-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qliksense-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/qliksense-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qliksense-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qliksense-finops.yml
created: '2024-01-15'
description: 'Qlik Sense and Qlik Cloud from Qlik Parent, Inc. — a business intelligence, data integration and AI analytics platform. Qlik publishes one of the broadest machine-readable API surfaces in the analytics market: 78 OpenAPI 3.0.0 documents covering 681 REST operations, 29 AsyncAPI 3.0.0 event documents carrying CloudEvents 1.0 payloads, an OpenRPC 1.0.0 document for the QIX Associative Engine WebSocket API, 39 JSON Schemas for Qlik Talend Cloud declarative pipelines, and a proto3 gRPC contract for the engine''s Server-Side Extension protocol. It also ships a generally-available remote MCP server at <tenant>/api/ai/mcp and maintains a public Agent Skills hub. Every API is tenant-scoped to https://{tenant}.{region}.qlikcloud.com and authenticated with an API key, an OAuth 2.0 token or a signed JWT.'
features:
- description: Qlik's unique Associative Engine enables dynamic data exploration without predefined queries or drill paths.
  name: Associative Engine
- description: Comprehensive REST API coverage for all Qlik Cloud resources including apps, data, users, and automation.
  name: 50+ REST APIs
- description: AutoML, natural language queries, and AI assistants for data-driven insights.
  name: AI-Powered Analytics
- description: Build automation workflows connecting Qlik with external applications without coding.
  name: No-Code Automation
- description: Event-driven architecture with webhooks for real-time notifications on platform events.
  name: Real-Time Webhooks
- description: Deploy Qlik Cloud across AWS, Azure, and GCP regions with global availability.
  name: Multi-Cloud Deployment
finops:
- name: Qliksense Finops
  service_category: API
  slug: qliksense-finops
image: /assets/icons/qliksense.png
integrations:
- description: Direct connectivity for analytics on Snowflake cloud data warehouse.
  name: Snowflake
- description: Integration with Databricks lakehouse for large-scale analytics workloads.
  name: Databricks
- description: Enterprise data connectivity for SAP ERP, BW, and HANA data sources.
  name: SAP
- description: CRM data integration for sales analytics and pipeline management.
  name: Salesforce
- description: Collaboration integration for sharing analytics insights and alerts in Slack.
  name: Slack
- description: Embed analytics and receive notifications within Microsoft Teams.
  name: Microsoft Teams
json_schemas:
- name: New Task Defaults Configuration
  property_count: 14
  slug: qliksense-qtcp-newtaskdefaults.schema
- name: Common Task Settings Definitions
  property_count: 0
  slug: qliksense-qtcp-newtaskdefaults.settings.common.schema
- name: Defaults for new Datamart Task
  property_count: 8
  slug: qliksense-qtcp-newtaskdefaults.settings.datamart.schema
- name: Defaults for new File Based Knowledge Mart Task
  property_count: 7
  slug: qliksense-qtcp-newtaskdefaults.settings.filebasedknowledgemart.schema
- name: Defaults for new Knowledge Mart Task
  property_count: 9
  slug: qliksense-qtcp-newtaskdefaults.settings.knowledgemart.schema
- name: Defaults for new Lakehouse Storage Task
  property_count: 5
  slug: qliksense-qtcp-newtaskdefaults.settings.lakehousestorage.schema
- name: Defaults for new Lake Landing Task
  property_count: 3
  slug: qliksense-qtcp-newtaskdefaults.settings.lakelanding.schema
- name: Defaults for new Landing Task
  property_count: 5
  slug: qliksense-qtcp-newtaskdefaults.settings.landing.schema
- name: Defaults for new QVD Storage Task
  property_count: 2
  slug: qliksense-qtcp-newtaskdefaults.settings.qvdstorage.schema
- name: Defaults for new Registered Data Task
  property_count: 4
  slug: qliksense-qtcp-newtaskdefaults.settings.registereddata.schema
- name: Defaults for new Replicate Landing Task
  property_count: 3
  slug: qliksense-qtcp-newtaskdefaults.settings.replicatelanding.schema
- name: Defaults for new Storage Task
  property_count: 8
  slug: qliksense-qtcp-newtaskdefaults.settings.storage.schema
- name: Defaults for new Streaming Lake Landing Task
  property_count: 4
  slug: qliksense-qtcp-newtaskdefaults.settings.streaminglakelanding.schema
- name: Defaults for new Streaming Transform Task
  property_count: 5
  slug: qliksense-qtcp-newtaskdefaults.settings.streamingtransform.schema
- name: Defaults for new Transform Task
  property_count: 9
  slug: qliksense-qtcp-newtaskdefaults.settings.transform.schema
- name: Project Configuration
  property_count: 2
  slug: qliksense-qtcp-project.schema
- name: Task Dataset Configuration
  property_count: 4
  slug: qliksense-qtcp-task.dataset.schema
- name: Task Model Configuration
  property_count: 2
  slug: qliksense-qtcp-task.model.schema
- name: Task Schedule Configuration
  property_count: 2
  slug: qliksense-qtcp-task.schedule.schema
- name: Task Configuration
  property_count: 0
  slug: qliksense-qtcp-task.schema
- name: Common Task Settings Definitions
  property_count: 0
  slug: qliksense-qtcp-task.settings.common.schema
- name: Datamart Task Settings
  property_count: 7
  slug: qliksense-qtcp-task.settings.datamart.schema
- name: File Based Knowledge Mart Task Settings
  property_count: 14
  slug: qliksense-qtcp-task.settings.filebasedknowledgemart.schema
- name: Knowledge Mart Task Settings
  property_count: 15
  slug: qliksense-qtcp-task.settings.knowledgemart.schema
- name: Lakehouse Mirror Task Settings
  property_count: 6
  slug: qliksense-qtcp-task.settings.lakehousemirror.schema
- name: Lakehouse Storage Task Settings
  property_count: 6
  slug: qliksense-qtcp-task.settings.lakehousestorage.schema
- name: Lake Landing Task Configuration (Replication)
  property_count: 21
  slug: qliksense-qtcp-task.settings.lakelanding.schema
- name: Landing Task Settings
  property_count: 19
  slug: qliksense-qtcp-task.settings.landing.schema
- name: QVD Storage Task Settings
  property_count: 3
  slug: qliksense-qtcp-task.settings.qvdstorage.schema
- name: Registered Data Task Settings
  property_count: 9
  slug: qliksense-qtcp-task.settings.registereddata.schema
- name: Replicate Landing Task Settings
  property_count: 2
  slug: qliksense-qtcp-task.settings.replicatelanding.schema
- name: Replication Task Configuration (Replication)
  property_count: 17
  slug: qliksense-qtcp-task.settings.replication.schema
- name: Storage Task Settings
  property_count: 8
  slug: qliksense-qtcp-task.settings.storage.schema
- name: Streaming Lake Landing Task Settings
  property_count: 3
  slug: qliksense-qtcp-task.settings.streaminglakelanding.schema
- name: Streaming Transform Task Settings
  property_count: 5
  slug: qliksense-qtcp-task.settings.streamingtransform.schema
- name: Transform Task Settings
  property_count: 7
  slug: qliksense-qtcp-task.settings.transform.schema
- name: Task SourceSelection Configuration
  property_count: 6
  slug: qliksense-qtcp-task.sourceselection.schema
- name: Task transformation data flow Configuration
  property_count: 6
  slug: qliksense-qtcp-task.transformationdataflow.schema
- name: Task transformation Configuration
  property_count: 2
  slug: qliksense-qtcp-task.transformationrules.schema
layout: provider
mcp_servers:
- description: Qlik ships a first-party REMOTE MCP server as part of Qlik Cloud. It reached general availability on 2026-02-10 and is listed as an included capability from the Starter plan upward on https://www.qlik
  name: Qlik MCP Server
  slug: qlik-mcp-server
modified: '2026-08-29'
name: Qlik Sense APIs
nav: Providers
network: true
overview: 'Qlik Sense APIs publishes 80 APIs on the [APIs.io](https://apis.io/) network, including Qlik Cloud System Events, Qlik MCP Server, Qlik Apps API, and 77 more. Tagged areas include Agents, Analytics, Artificial Intelligence, Business Intelligence, and Cloud.


  The Qlik Sense APIs catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Qlik Sense APIs'' developer surface includes developer portal, documentation, API reference, getting-started guide, authentication, support, engineering blog, and 44 more developer resources.'
plans:
- name: Qliksense Plans Pricing
  plan_count: 5
  slug: qliksense-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 3
  name: Qliksense Rate Limits
  slug: qliksense-rate-limits
scopes:
- name: Qliksense Scopes
  scope_count: 0
  slug: qliksense-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 66.8
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 55.1
    developer_ergonomics: 78.6
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 76.3
  previous_composite: 66.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 56
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/screenshots/qliksense-2026-06-20T192343.png
security:
- kind: authentication
  name: Qliksense Authentication
  slug: qliksense-authentication
  summary_line: 8 schemes
- kind: domain-security
  name: Qliksense Domain Security
  slug: qliksense-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Qliksense Vulnerability Disclosure
  slug: qliksense-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Qliksense Trust Center
  slug: qliksense-trust-center
  summary_line: qlik, qlik_cloud_government, talend_cloud
slug: qliksense
tags:
- Agents
- Analytics
- Artificial Intelligence
- Business Intelligence
- Cloud
- Data Integration
- Data Visualization
- Embedded Analytics
- Enterprise
- Machine-Learning
use_cases:
- description: Embed interactive Qlik visualizations and dashboards in custom web applications.
  name: Embedded Analytics
- description: Automate data integration and transformation workflows using APIs and automation connectors.
  name: Data Pipeline Automation
- description: Enable business users to create and share analytics apps through the platform APIs.
  name: Self-Service BI
- description: Generate predictive analytics and natural language insights using ML and NLP APIs.
  name: AI-Powered Insights
- description: Manage multiple Qlik Cloud tenants programmatically for SaaS and enterprise deployments.
  name: Multi-Tenant Management
website: https://www.qlik.com/us/products/qlik-sense
---
