---
access_model:
  confidence: medium
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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.7
  scored_at: '2026-09-02'
api_count: 3
apis:
- description: Sigma's first-party remote Model Context Protocol server. AI assistants such as Claude, ChatGPT, Codex, Cursor and Snowflake Cortex Code connect over HTTP with OAuth and can then search a Sigma organi
  name: Sigma MCP Server
  slug: sigma-mcp-server
- description: Secure embedding of Sigma workbooks, pages and individual elements into a host application. Embed URLs are signed with JSON Web Tokens carrying the viewing user's identity, team and user attributes so
  name: Sigma Embed API
  slug: sigma-embed-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The accountTypes API from Sigma Computing — 3 operation(s) for accounttypes.
  name: Sigma Computing Account Types API
  slug: sigma-computing-accounttypes-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The apiConnectors API from Sigma Computing — 2 operation(s) for apiconnectors.
  name: Sigma Computing API Connectors API
  slug: sigma-computing-apiconnectors-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The apiCredentials API from Sigma Computing — 2 operation(s) for apicredentials.
  name: Sigma Computing API Credentials API
  slug: sigma-computing-apicredentials-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Auth API from Sigma Computing — 1 operation(s) for auth.
  name: Sigma Computing Auth API
  slug: sigma-computing-auth-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Connections API from Sigma Computing — 13 operation(s) for connections.
  name: Sigma Computing Connections API
  slug: sigma-computing-connections-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Credentials API from Sigma Computing — 2 operation(s) for credentials.
  name: Sigma Computing Credentials API
  slug: sigma-computing-credentials-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The dataModels API from Sigma Computing — 16 operation(s) for datamodels.
  name: Sigma Computing Data Models API
  slug: sigma-computing-datamodels-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Datasets API from Sigma Computing — 7 operation(s) for datasets.
  name: Sigma Computing Datasets API
  slug: sigma-computing-datasets-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The deploymentPolicies API from Sigma Computing — 7 operation(s) for deploymentpolicies.
  name: Sigma Computing Deployment Policies API
  slug: sigma-computing-deploymentpolicies-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Favorites API from Sigma Computing — 3 operation(s) for favorites.
  name: Sigma Computing Favorites API
  slug: sigma-computing-favorites-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Files API from Sigma Computing — 2 operation(s) for files.
  name: Sigma Computing Files API
  slug: sigma-computing-files-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Grants API from Sigma Computing — 2 operation(s) for grants.
  name: Sigma Computing Grants API
  slug: sigma-computing-grants-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Members API from Sigma Computing — 9 operation(s) for members.
  name: Sigma Computing Members API
  slug: sigma-computing-members-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Organizations API from Sigma Computing — 4 operation(s) for organizations.
  name: Sigma Computing Organizations API
  slug: sigma-computing-organizations-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The plugins API from Sigma Computing — 2 operation(s) for plugins.
  name: Sigma Computing Plugins API
  slug: sigma-computing-plugins-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Query API from Sigma Computing — 1 operation(s) for query.
  name: Sigma Computing Query API
  slug: sigma-computing-query-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Reports API from Sigma Computing — 26 operation(s) for reports.
  name: Sigma Computing Reports API
  slug: sigma-computing-reports-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The SAML API from Sigma Computing — 5 operation(s) for saml.
  name: Sigma Computing SAML API
  slug: sigma-computing-saml-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The sharedTemplates API from Sigma Computing — 3 operation(s) for sharedtemplates.
  name: Sigma Computing Shared Templates API
  slug: sigma-computing-sharedtemplates-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The shortcuts API from Sigma Computing — 1 operation(s) for shortcuts.
  name: Sigma Computing Shortcuts API
  slug: sigma-computing-shortcuts-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The sourceSwapPolicies API from Sigma Computing — 2 operation(s) for sourceswappolicies.
  name: Sigma Computing Source Swap Policies API
  slug: sigma-computing-sourceswappolicies-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Tags API from Sigma Computing — 3 operation(s) for tags.
  name: Sigma Computing Tags API
  slug: sigma-computing-tags-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Teams API from Sigma Computing — 6 operation(s) for teams.
  name: Sigma Computing Teams API
  slug: sigma-computing-teams-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Templates API from Sigma Computing — 4 operation(s) for templates.
  name: Sigma Computing Templates API
  slug: sigma-computing-templates-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Tenants API from Sigma Computing — 6 operation(s) for tenants.
  name: Sigma Computing Tenants API
  slug: sigma-computing-tenants-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Translations API from Sigma Computing — 3 operation(s) for translations.
  name: Sigma Computing Translations API
  slug: sigma-computing-translations-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The userAttributes API from Sigma Computing — 8 operation(s) for userattributes.
  name: Sigma Computing User Attributes API
  slug: sigma-computing-userattributes-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Webhooks API from Sigma Computing — 2 operation(s) for webhooks.
  name: Sigma Computing Webhooks API
  slug: sigma-computing-webhooks-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Whoami API from Sigma Computing — 1 operation(s) for whoami.
  name: Sigma Computing Whoami API
  slug: sigma-computing-whoami-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Workbooks API from Sigma Computing — 44 operation(s) for workbooks.
  name: Sigma Computing Workbooks API
  slug: sigma-computing-workbooks-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Workspaces API from Sigma Computing — 5 operation(s) for workspaces.
  name: Sigma Computing Workspaces API
  slug: sigma-computing-workspaces-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The allowedIps API from Sigma Computing — 1 operation(s) for allowedips.
  name: Sigma Computing Allowed Ips API
  slug: sigma-computing-allowedips-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The allowedIps\:batchCreate API from Sigma Computing — 1 operation(s) for allowedips\:batchcreate.
  name: Sigma Computing Allowed Ips\:batch Create API
  slug: sigma-computing-allowedips-batchcreate-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The allowedIps\:batchDelete API from Sigma Computing — 1 operation(s) for allowedips\:batchdelete.
  name: Sigma Computing Allowed Ips\:batch Delete API
  slug: sigma-computing-allowedips-batchdelete-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The api-connectors API from Sigma Computing — 2 operation(s) for api-connectors.
  name: Sigma Computing API Connectors API
  slug: sigma-computing-api-connectors-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The api-credentials API from Sigma Computing — 2 operation(s) for api-credentials.
  name: Sigma Computing API Credentials API
  slug: sigma-computing-api-credentials-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The shared_templates API from Sigma Computing — 3 operation(s) for shared_templates.
  name: Sigma Computing Shared Templates API
  slug: sigma-computing-shared-templates-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The user-attributes API from Sigma Computing — 8 operation(s) for user-attributes.
  name: Sigma Computing User Attributes API
  slug: sigma-computing-user-attributes-api
artifact_total: 49
asyncapis:
- description: ''
  name: Sigma Computing Webhooks
  slug: sigma-computing-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/sigmacomputing/embed-sdk/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.sigmacomputing.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.sigmacomputing.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.sigmacomputing.com/docs/get-started-with-sigmas-api
- group: docs
  title: ''
  type: APIReference
  url: https://help.sigmacomputing.com/reference/get-started-sigma-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sigmacomputing.com/reference/get-started-sigma-api
- group: operate
  title: ''
  type: Support
  url: https://help.sigmacomputing.com/docs/sigma-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.sigmacomputing.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sigmacomputing.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sigmacomputing
- group: start
  title: ''
  type: SignUp
  url: https://www.sigmacomputing.com/go/free-trial
- group: start
  title: ''
  type: Login
  url: https://app.sigmacomputing.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sigmacomputing.com/company/contact-us
- group: commercial
  title: ''
  type: Plans
  url: plans/sigma-computing-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sigmacomputing.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sigmacomputing.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sigmacomputing.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sigma-computing-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sigma-computing-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.sigmacomputing.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sigma-computing-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sigmacomputing.com/product/vdp
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sigma-computing-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sigma-computing-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/sigma-computing-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sigma-computing-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sigma-computing-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sigma-computing-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sigma-computing-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/sigma-computing-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/sigma-computing-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sigma-computing-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/sigma-computing-cli.yml
- group: design
  title: ''
  type: Components
  url: components/sigma-computing-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sigma-computing-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sigma-computing-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/sigma-computing-api-catalog.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sigma-computing-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/sigma-computing-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sigma-computing-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sigma-computing-rate-limits.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sigma-computing-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sigma-computing-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sigma-computing-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sigma-computing-rest-api-overlay.yaml
created: '2026-08-27'
description: Sigma Computing is a warehouse-first analytics and business-application platform. Instead of extracting data into its own store, Sigma queries the customer's cloud data warehouse live — Snowflake, Databricks, BigQuery, Redshift, Amazon Athena, PostgreSQL and ClickHouse — and puts a spreadsheet-style interface, governed data models, input tables with write-back, pixel-perfect paginated reports, embedded white-label analytics and AI agents on top of it. The developer surface is a 274-operation REST API (OpenAPI 3.1) covering workbooks, data models, reports, connections, members, teams, workspaces, permissions, user attributes, tenants, templates and API connectors; a first-party Rust CLI generated from that same OpenAPI; a remote OAuth-protected MCP server that lets AI assistants search, describe and query governed data in natural language; JavaScript embed and plugin SDKs; and three Apache-2.0 agent skills Sigma publishes for Claude Code, Cursor, Codex and Snowflake Cortex Code.
image: https://cdn.sanity.io/images/9i48iita/production/2fcbd9fc0f6c54c2bc25877917e563fe805ad864-1200x630.png
layout: provider
mcp_servers:
- description: Sigma ships a first-party remote MCP server that lets an AI assistant search the organization for workbooks, data models and warehouse tables, describe their columns and semantics, and run governed qu
  name: Sigma MCP Server
  slug: sigma-mcp-server
modified: '2026-08-27'
name: Sigma Computing
nav: Providers
network: true
overview: 'Sigma Computing publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Account Types API, API Connectors API, API Credentials API, and 35 more. Tagged areas include Business Intelligence, Analytics, Embedded Analytics, Data Modeling, and Data Warehouse.


  The Sigma Computing catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sigma Computing''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 39 more developer resources.'
plans:
- name: Sigma Computing Plans Pricing
  plan_count: 0
  slug: sigma-computing-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 6
  name: Sigma Computing Rate Limits
  slug: sigma-computing-rate-limits
scopes:
- name: Sigma Computing Scopes
  scope_count: 0
  slug: sigma-computing-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 67.3
  coverage:
    artifact_dirs: 24
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.9
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 65.1
    developer_ergonomics: 85.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 92.1
  previous_composite: 66.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 38
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sigma-computing/refs/heads/main/screenshots/sigma-computing-2026-09-02T155428.png
security:
- kind: authentication
  name: Sigma Computing Authentication
  slug: sigma-computing-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Sigma Computing Domain Security
  slug: sigma-computing-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sigma Computing Vulnerability Disclosure
  slug: sigma-computing-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Sigma Computing Trust Center
  slug: sigma-computing-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO/IEC 27701, HIPAA, GDPR, CCPA, EU-US Data Privacy Framework
slug: sigma-computing
tags:
- Business Intelligence
- Analytics
- Embedded Analytics
- Data Modeling
- Data Warehouse
- Reporting
- Spreadsheets
- MCP
- AI Agents
- Snowflake
- Databricks
- Data Governance
website: https://www.sigmacomputing.com/
---
