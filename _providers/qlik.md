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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.8
  scored_at: '2026-08-11'
api_count: 69
apis:
- description: Qlik provides APIs to support automation, configuration, observability, and integration with third-party applications to incorporate Qlik Cloud capabilities directly into those applications.
  name: Qlik
  slug: qlik
- description: Manages Qlik Cloud Analytics applications, including creating, updating, copying, publishing, and deleting apps. Apps are a core part of Qlik Cloud Analytics and represent either an Analytics app or a
  name: Qlik Apps API
  slug: apps
- description: Manages user resources within Qlik Cloud tenants. Users represent clients accessing the Qlik Cloud tenant, with support for listing, creating, updating, deleting users and managing invitations.
  name: Qlik Users API
  slug: users
- description: Manages logical containers within a Qlik tenant that control access for users and groups through space roles to determine what content users can access.
  name: Qlik Spaces API
  slug: spaces
- description: Provides a list of core resources in the Qlik platform, including resources such as apps, automations, and data sets that a user has access to.
  name: Qlik Items API
  slug: items
- description: Manages API key lifecycle for authenticating with Qlik Cloud APIs, including creating, listing, and revoking API keys.
  name: Qlik API Keys API
  slug: api-keys
- description: Provides access to events emitted upon each action taken in a Qlik Cloud tenant, offering detailed access to what is happening in the tenant. Events are stored for 90 days.
  name: Qlik Audits API
  slug: audits
- description: Manages automations in Qlik Automate, which are no-code workflows connecting applications together. Supports creating, updating, deleting, and executing automations.
  name: Qlik Automations API
  slug: automations
- description: Manages connections used by automations to interact with external services and applications within Qlik Automate.
  name: Qlik Automation Connections API
  slug: automation-connections
- description: Manages connectors available for automations in Qlik Automate, providing integration capabilities with third-party services.
  name: Qlik Automation Connectors API
  slug: automation-connectors
- description: Manages AutoML dataset predictions, enabling batch prediction workflows on datasets using trained machine learning models.
  name: Qlik AutoML Dataset Predictions API
  slug: automl-predictions
- description: Manages AutoML real-time prediction deployments, enabling on-demand predictions using trained machine learning models.
  name: Qlik AutoML Real-Time Predictions API
  slug: automl-deployments
- description: Manages AI assistants within Qlik Cloud, enabling conversational analytics and natural language interactions with data.
  name: Qlik Assistants API
  slug: assistants
- description: Manages tenant-wide banner notifications displayed to users within the Qlik Cloud interface.
  name: Qlik Banners API
  slug: banners
- description: Manages branding and customization of the Qlik Cloud tenant appearance, including logos, colors, and styling.
  name: Qlik Brands API
  slug: brands
- description: Provides the framework to catalog various content a user has access to using tags, public and private collections, and favorites.
  name: Qlik Collections API
  slug: collections
- description: Manages conditions used for evaluating expressions and triggering actions within Qlik Cloud.
  name: Qlik Conditions API
  slug: conditions
- description: Manages Content Security Policy origins, controlling which external domains can interact with the Qlik Cloud tenant.
  name: Qlik CSP Origins API
  slug: csp-origins
- description: Provides CSRF tokens for securing requests to Qlik Cloud APIs against cross-site request forgery attacks.
  name: Qlik CSRF Token API
  slug: csrf-token
- description: Manages data-driven alerts that notify users when conditions in their data are met within Qlik Cloud.
  name: Qlik Data Alerts API
  slug: data-alerts
- description: Manages data assets within the Qlik Cloud catalog, providing metadata and governance for data resources.
  name: Qlik Data Assets API
  slug: data-assets
- description: Manages connections between Qlik Cloud Analytics apps and Data Integration projects and external data sources.
  name: Qlik Data Connections API
  slug: data-connections
- description: Manages credentials used by data connections to authenticate with external data sources.
  name: Qlik Data Credentials API
  slug: data-credentials
- description: Manages data files uploaded to Qlik Cloud for use in analytics applications and data integration projects.
  name: Qlik Data Files API
  slug: data-files
- description: Manages data sets within Qlik Cloud's catalog system. A data set is a member of a data asset, with support for creation, retrieval, update, and profile management.
  name: Qlik Data Sets API
  slug: data-sets
- description: Manages data source configurations for Qlik Cloud, defining the external systems from which data can be loaded.
  name: Qlik Data Sources API
  slug: data-sources
- description: Manages data stores used in Qlik Cloud for data warehousing and integration scenarios.
  name: Qlik Data Stores API
  slug: data-stores
- description: Manages data quality assessments and profiles for data assets within Qlik Cloud.
  name: Qlik Data Qualities API
  slug: data-qualities
- description: Manages data integration projects for building data pipelines and transformation workflows within Qlik Cloud.
  name: Qlik Data Integration Projects API
  slug: di-projects
- description: Manages Direct Access Agents that provide secure connectivity between Qlik Cloud and on-premises data sources.
  name: Qlik Direct Access Agents API
  slug: direct-access-agents
- description: Manages encryption keys and configurations for securing data at rest within Qlik Cloud.
  name: Qlik Encryption API
  slug: encryption
- description: Tracks and reports on entitlement consumption metrics for Qlik Cloud license usage.
  name: Qlik Entitlement Consumption API
  slug: consumption
- description: Manages visualization extensions in Qlik Sense, allowing third-party visualizations and other presentation objects to be used in the Qlik Sense client.
  name: Qlik Extensions API
  slug: extensions
- description: Manages business glossaries for defining and sharing terminology and definitions across the Qlik Cloud tenant.
  name: Qlik Glossaries API
  slug: glossaries
- description: Manages groups within Qlik Cloud to which space and tenant roles can be assigned to simplify access control management.
  name: Qlik Groups API
  slug: groups
- description: Manages identity provider configurations for Qlik Cloud, enabling integration with external authentication systems.
  name: Qlik Identity Providers API
  slug: identity-providers
- description: Manages knowledge bases used by Qlik AI assistants and natural language features for conversational analytics.
  name: Qlik Knowledgebases API
  slug: knowledgebases
- description: Manages tenant and user license entitlements in Qlik Cloud, including assignments, consumption tracking, and auto-assignment configuration.
  name: Qlik Licenses API
  slug: licenses
- description: Manages data lineage graph visualizations that trace the origin and transformation of data across Qlik Cloud resources.
  name: Qlik Lineage Graphs API
  slug: lineage-graphs
- description: Manages login flows and session management for accessing Qlik Cloud.
  name: Qlik Login API
  slug: login
- description: Manages machine learning experiments, models, and deployments within Qlik Cloud for predictive analytics.
  name: Qlik Machine Learning API
  slug: ml
- description: Enables natural language question and answer interactions with data in Qlik Cloud analytics applications.
  name: Qlik Natural Language API
  slug: questions
- description: Manages notes and annotations attached to Qlik Cloud analytics content for collaboration and documentation.
  name: Qlik Notes API
  slug: notes
- description: Manages notification preferences and delivery for Qlik Cloud events and alerts.
  name: Qlik Notifications API
  slug: notifications
- description: Manages OAuth 2.0 authorization flows for secure authentication with Qlik Cloud APIs.
  name: Qlik OAuth API
  slug: oauth
- description: Manages OAuth client registrations for applications integrating with Qlik Cloud through OAuth 2.0.
  name: Qlik OAuth Clients API
  slug: oauth-clients
- description: Lists and revokes active OAuth tokens for managing authenticated sessions in Qlik Cloud.
  name: Qlik OAuth Tokens API
  slug: oauth-tokens
- description: Returns OAuth 2.0 metadata related to the tenant, including authorization endpoint, token endpoint, and supported grant types.
  name: Qlik OAuth Well-Known Configuration API
  slug: well-known
- description: Returns entitled attributes based on the license, providing information about resource limits and usage quotas.
  name: Qlik Quotas API
  slug: quotas
- description: Manages scheduled reload tasks for analytics applications, enabling automated data refresh on defined schedules.
  name: Qlik Reload Tasks API
  slug: reload-tasks
- description: Triggers and manages app data reloads to refresh analytics application data via REST API instead of only through the JSON-RPC WebSocket API.
  name: Qlik Reloads API
  slug: reloads
- description: Manages report templates that define the structure and formatting of generated reports from Qlik analytics data.
  name: Qlik Report Templates API
  slug: report-templates
- description: Generates downloadable report assets from data in analytics applications, supporting multiple output formats including Excel, PDF, PowerPoint, HTML, and images.
  name: Qlik Reports API
  slug: reports
- description: Manages tenant roles that are assigned to users or groups to control permissions and access within Qlik Cloud.
  name: Qlik Roles API
  slug: roles
- description: Manages sharing tasks for distributing analytics content and reports to recipients within Qlik Cloud.
  name: Qlik Sharing Tasks API
  slug: sharing-tasks
- description: Manages general task scheduling and execution within Qlik Cloud for orchestrating platform operations.
  name: Qlik Tasks API
  slug: tasks
- description: Manages temporary content storage for file uploads and transient data within Qlik Cloud.
  name: Qlik Temporary Contents API
  slug: temp-contents
- description: Manages Qlik Cloud tenant configurations, settings, and metadata.
  name: Qlik Tenants API
  slug: tenants
- description: Manages tenant-level configuration settings for customizing the behavior of the Qlik Cloud platform.
  name: Qlik Tenant Settings API
  slug: tenant-settings
- description: Manages themes for customizing the styling and appearance of the Qlik Sense client experience, including uploading, downloading, and managing theme archives.
  name: Qlik Themes API
  slug: themes
- description: Manages email transport configuration for sending notifications and reports from Qlik Cloud.
  name: Qlik Email Configuration API
  slug: transports
- description: Manages administrator-defined pinned links displayed in the Qlik Cloud interface for quick access to resources.
  name: Qlik Pinned Links API
  slug: ui-config
- description: Manages web integration configurations that allow external websites to embed and interact with Qlik Cloud content.
  name: Qlik Web Integrations API
  slug: web-integrations
- description: Manages web-based push notifications for real-time updates within the Qlik Cloud user interface.
  name: Qlik Web Notifications API
  slug: web-notifications
- description: Manages webhooks for providing real-time event information from Qlik Cloud to external applications, with delivery history tracking.
  name: Qlik Webhooks API
  slug: webhooks
- description: Manages IP restriction policies for controlling network access to the Qlik Cloud tenant.
  name: Qlik IP Policies API
  slug: ip-policies
- description: Manages change store configurations for tracking and storing changes in analytics data.
  name: Qlik Change Stores API
  slug: change-stores
- description: Manages data products within the Qlik data governance framework, enabling the packaging and sharing of curated data assets.
  name: Qlik Data Products API
  slug: data-products
- description: The JSON-RPC API over WebSocket that enables interaction with the Qlik Associative Engine for Qlik Sense applications, providing session-based access to app data models, objects, and calculations.
  name: Qlik Engine JSON-RPC API
  slug: qix
artifact_total: 74
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qlik-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qlik
- group: start
  title: ''
  type: DeveloperPortal
  url: https://qlik.dev
- group: auth
  title: ''
  type: Authentication
  url: https://qlik.dev/authenticate
- group: start
  title: ''
  type: GettingStarted
  url: https://qlik.dev/get-started
- group: build
  title: ''
  type: SDKs
  url: https://qlik.dev/toolkits/qlik-api/
- group: build
  title: ''
  type: CLI
  url: https://qlik.dev/toolkits/qlik-cli/
- group: docs
  title: ''
  type: Documentation
  url: https://qlik.dev/apis/rest/
- group: operate
  title: ''
  type: RateLimits
  url: https://qlik.dev/apis/rest/rate-limiting/
- group: build
  title: ''
  type: CodeExamples
  url: https://qlik.dev/examples/
- group: operate
  title: ''
  type: ChangeLog
  url: https://qlik.dev/changelog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qlik-oss
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qlikcloud.com/
- group: company
  title: ''
  type: Blog
  url: https://community.qlik.com/t5/Qlik-Design-Blog/bg-p/qlik-design-blog
- group: operate
  title: ''
  type: Community
  url: https://community.qlik.com
- group: operate
  title: ''
  type: Support
  url: https://support.qlik.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.qlik.com/us/legal/license-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.qlik.com/us/legal/privacy
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/qlik-oss/qlik-mcp-registry
created: '2025-02-24'
description: APIs for Qlik's analytics and data integration platform.
finops:
- name: Qlik Finops
  service_category: API
  slug: qlik-finops
image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Qlik
nav: Providers
network: true
overview: 'Qlik publishes 64 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Users API, Spaces API, and 61 more.


  Qlik''s developer surface includes authentication, getting-started guide, CLI, documentation, code examples, changelog, engineering blog, and 12 more developer resources.'
plans:
- name: Qlik Plans Pricing
  plan_count: 3
  slug: qlik-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 5
  name: Qlik Rate Limits
  slug: qlik-rate-limits
score:
  band: thin
  composite: 39.4
  delta: -7.8
  facets:
    commercial_clarity: 36.8
    contract_quality: 32.3
    developer_ergonomics: 67.4
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 47.2
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/screenshots/qlik-2026-06-20T192340.png
security:
- kind: domain-security
  name: Qlik Domain Security
  slug: qlik-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: qlik
website: https://qlik.dev
---
