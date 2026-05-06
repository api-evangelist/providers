---
aid: qlik
name: Qlik
description: APIs for Qlik's analytics and data integration platform.
type: Index
position: Consumer
access: 3rd-Party
image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
tags: []
created: '2025-02-24'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/qlik/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: qlik:qlik
    name: Qlik
    description: Qlik provides APIs to support automation, configuration, observability, and integration with third-party applications to incorporate Qlik Cloud capabilities directly into those applications.
    humanURL: https://qlik.dev/apis/
    baseURL: https://{tenant}.{region}.qlikcloud.com/api/v1
    tags: []
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/
      - type: GettingStarted
        url: https://qlik.dev/get-started
  - aid: qlik:apps
    name: Qlik Apps API
    description: Manages Qlik Cloud Analytics applications, including creating, updating, copying, publishing, and deleting apps. Apps are a core part of Qlik Cloud Analytics and represent either an Analytics app or a script.
    humanURL: https://qlik.dev/apis/rest/apps/
    tags:
      - Analytics
      - Applications
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/apps/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/apps.json
  - aid: qlik:users
    name: Qlik Users API
    description: Manages user resources within Qlik Cloud tenants. Users represent clients accessing the Qlik Cloud tenant, with support for listing, creating, updating, deleting users and managing invitations.
    humanURL: https://qlik.dev/apis/rest/users/
    tags:
      - Users
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/users/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/users.json
  - aid: qlik:spaces
    name: Qlik Spaces API
    description: Manages logical containers within a Qlik tenant that control access for users and groups through space roles to determine what content users can access.
    humanURL: https://qlik.dev/apis/rest/spaces/
    tags:
      - Access Control
      - Spaces
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/spaces/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/spaces.json
  - aid: qlik:items
    name: Qlik Items API
    description: Provides a list of core resources in the Qlik platform, including resources such as apps, automations, and data sets that a user has access to.
    humanURL: https://qlik.dev/apis/rest/items/
    tags:
      - Items
      - Resources
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/items/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/items.json
  - aid: qlik:api-keys
    name: Qlik API Keys API
    description: Manages API key lifecycle for authenticating with Qlik Cloud APIs, including creating, listing, and revoking API keys.
    humanURL: https://qlik.dev/apis/rest/api-keys/
    tags:
      - API Keys
      - Authentication
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/api-keys/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/api-keys.json
  - aid: qlik:audits
    name: Qlik Audits API
    description: Provides access to events emitted upon each action taken in a Qlik Cloud tenant, offering detailed access to what is happening in the tenant. Events are stored for 90 days.
    humanURL: https://qlik.dev/apis/rest/audits/
    tags:
      - Audits
      - Events
      - Observability
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/audits/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/audits.json
  - aid: qlik:automations
    name: Qlik Automations API
    description: Manages automations in Qlik Automate, which are no-code workflows connecting applications together. Supports creating, updating, deleting, and executing automations.
    humanURL: https://qlik.dev/apis/rest/automations/
    tags:
      - Automations
      - Workflows
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/automations/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/automations.json
  - aid: qlik:automation-connections
    name: Qlik Automation Connections API
    description: Manages connections used by automations to interact with external services and applications within Qlik Automate.
    humanURL: https://qlik.dev/apis/rest/automation-connections/
    tags:
      - Automations
      - Connections
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/automation-connections/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/automation-connections.json
  - aid: qlik:automation-connectors
    name: Qlik Automation Connectors API
    description: Manages connectors available for automations in Qlik Automate, providing integration capabilities with third-party services.
    humanURL: https://qlik.dev/apis/rest/automation-connectors/
    tags:
      - Automations
      - Connectors
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/automation-connectors/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/automation-connectors.json
  - aid: qlik:automl-predictions
    name: Qlik AutoML Dataset Predictions API
    description: Manages AutoML dataset predictions, enabling batch prediction workflows on datasets using trained machine learning models.
    humanURL: https://qlik.dev/apis/rest/automl-predictions/
    tags:
      - Machine Learning
      - Predictions
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/automl-predictions/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/automl-predictions.json
  - aid: qlik:automl-deployments
    name: Qlik AutoML Real-Time Predictions API
    description: Manages AutoML real-time prediction deployments, enabling on-demand predictions using trained machine learning models.
    humanURL: https://qlik.dev/apis/rest/automl-deployments/
    tags:
      - Machine Learning
      - Predictions
      - Real-Time
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/automl-deployments/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/automl-deployments.json
  - aid: qlik:assistants
    name: Qlik Assistants API
    description: Manages AI assistants within Qlik Cloud, enabling conversational analytics and natural language interactions with data.
    humanURL: https://qlik.dev/apis/rest/assistants/
    tags:
      - AI
      - Assistants
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/assistants/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/assistants.json
  - aid: qlik:banners
    name: Qlik Banners API
    description: Manages tenant-wide banner notifications displayed to users within the Qlik Cloud interface.
    humanURL: https://qlik.dev/apis/rest/banners/
    tags:
      - Banners
      - Notifications
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/banners/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/banners.json
  - aid: qlik:brands
    name: Qlik Brands API
    description: Manages branding and customization of the Qlik Cloud tenant appearance, including logos, colors, and styling.
    humanURL: https://qlik.dev/apis/rest/brands/
    tags:
      - Branding
      - Customization
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/brands/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/brands.json
  - aid: qlik:collections
    name: Qlik Collections API
    description: Provides the framework to catalog various content a user has access to using tags, public and private collections, and favorites.
    humanURL: https://qlik.dev/apis/rest/collections/
    tags:
      - Catalog
      - Collections
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/collections/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/collections.json
  - aid: qlik:conditions
    name: Qlik Conditions API
    description: Manages conditions used for evaluating expressions and triggering actions within Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/conditions/
    tags:
      - Conditions
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/conditions/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/conditions.json
  - aid: qlik:csp-origins
    name: Qlik CSP Origins API
    description: Manages Content Security Policy origins, controlling which external domains can interact with the Qlik Cloud tenant.
    humanURL: https://qlik.dev/apis/rest/csp-origins/
    tags:
      - Content Security Policy
      - Security
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/csp-origins/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/csp-origins.json
  - aid: qlik:csrf-token
    name: Qlik CSRF Token API
    description: Provides CSRF tokens for securing requests to Qlik Cloud APIs against cross-site request forgery attacks.
    humanURL: https://qlik.dev/apis/rest/csrf-token/
    tags:
      - CSRF
      - Security
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/csrf-token/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/csrf-token.json
  - aid: qlik:data-alerts
    name: Qlik Data Alerts API
    description: Manages data-driven alerts that notify users when conditions in their data are met within Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/data-alerts/
    tags:
      - Alerts
      - Data
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-alerts/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/data-alerts.json
  - aid: qlik:data-assets
    name: Qlik Data Assets API
    description: Manages data assets within the Qlik Cloud catalog, providing metadata and governance for data resources.
    humanURL: https://qlik.dev/apis/rest/data-assets/
    tags:
      - Catalog
      - Data Assets
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-assets/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/data-assets.json
  - aid: qlik:data-connections
    name: Qlik Data Connections API
    description: Manages connections between Qlik Cloud Analytics apps and Data Integration projects and external data sources.
    humanURL: https://qlik.dev/apis/rest/data-connections/
    tags:
      - Data Connections
      - Integration
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-connections/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/data-connections.json
  - aid: qlik:data-credentials
    name: Qlik Data Credentials API
    description: Manages credentials used by data connections to authenticate with external data sources.
    humanURL: https://qlik.dev/apis/rest/data-credentials/
    tags:
      - Credentials
      - Data
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-credentials/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/data-credentials.json
  - aid: qlik:data-files
    name: Qlik Data Files API
    description: Manages data files uploaded to Qlik Cloud for use in analytics applications and data integration projects.
    humanURL: https://qlik.dev/apis/rest/data-files/
    tags:
      - Data Files
      - Upload
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-files/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/data-files.json
  - aid: qlik:data-sets
    name: Qlik Data Sets API
    description: Manages data sets within Qlik Cloud's catalog system. A data set is a member of a data asset, with support for creation, retrieval, update, and profile management.
    humanURL: https://qlik.dev/apis/rest/data-sets/
    tags:
      - Catalog
      - Data Sets
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-sets/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/data-sets.json
  - aid: qlik:data-sources
    name: Qlik Data Sources API
    description: Manages data source configurations for Qlik Cloud, defining the external systems from which data can be loaded.
    humanURL: https://qlik.dev/apis/rest/data-sources/
    tags:
      - Data Sources
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-sources/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/data-sources.json
  - aid: qlik:data-stores
    name: Qlik Data Stores API
    description: Manages data stores used in Qlik Cloud for data warehousing and integration scenarios.
    humanURL: https://qlik.dev/apis/rest/data-stores/
    tags:
      - Data Stores
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-stores/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/data-stores.json
  - aid: qlik:data-qualities
    name: Qlik Data Qualities API
    description: Manages data quality assessments and profiles for data assets within Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/data-qualities/
    tags:
      - Data Quality
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-qualities/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/data-qualities.json
  - aid: qlik:di-projects
    name: Qlik Data Integration Projects API
    description: Manages data integration projects for building data pipelines and transformation workflows within Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/di-projects/
    tags:
      - Data Integration
      - Projects
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/di-projects/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/di-projects.json
  - aid: qlik:direct-access-agents
    name: Qlik Direct Access Agents API
    description: Manages Direct Access Agents that provide secure connectivity between Qlik Cloud and on-premises data sources.
    humanURL: https://qlik.dev/apis/rest/direct-access-agents/
    tags:
      - Agents
      - Direct Access
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/direct-access-agents/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/direct-access-agents.json
  - aid: qlik:encryption
    name: Qlik Encryption API
    description: Manages encryption keys and configurations for securing data at rest within Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/encryption/
    tags:
      - Encryption
      - Security
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/encryption/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/encryption.json
  - aid: qlik:consumption
    name: Qlik Entitlement Consumption API
    description: Tracks and reports on entitlement consumption metrics for Qlik Cloud license usage.
    humanURL: https://qlik.dev/apis/rest/consumption/
    tags:
      - Consumption
      - Licensing
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/consumption/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/consumption.json
  - aid: qlik:extensions
    name: Qlik Extensions API
    description: Manages visualization extensions in Qlik Sense, allowing third-party visualizations and other presentation objects to be used in the Qlik Sense client.
    humanURL: https://qlik.dev/apis/rest/extensions/
    tags:
      - Extensions
      - Visualizations
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/extensions/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/extensions.json
  - aid: qlik:glossaries
    name: Qlik Glossaries API
    description: Manages business glossaries for defining and sharing terminology and definitions across the Qlik Cloud tenant.
    humanURL: https://qlik.dev/apis/rest/glossaries/
    tags:
      - Glossaries
      - Governance
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/glossaries/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/glossaries.json
  - aid: qlik:groups
    name: Qlik Groups API
    description: Manages groups within Qlik Cloud to which space and tenant roles can be assigned to simplify access control management.
    humanURL: https://qlik.dev/apis/rest/groups/
    tags:
      - Access Control
      - Groups
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/groups/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/groups.json
  - aid: qlik:identity-providers
    name: Qlik Identity Providers API
    description: Manages identity provider configurations for Qlik Cloud, enabling integration with external authentication systems.
    humanURL: https://qlik.dev/apis/rest/identity-providers/
    tags:
      - Authentication
      - Identity Providers
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/identity-providers/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/identity-providers.json
  - aid: qlik:knowledgebases
    name: Qlik Knowledgebases API
    description: Manages knowledge bases used by Qlik AI assistants and natural language features for conversational analytics.
    humanURL: https://qlik.dev/apis/rest/knowledgebases/
    tags:
      - AI
      - Knowledge Bases
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/knowledgebases/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/knowledgebases.json
  - aid: qlik:licenses
    name: Qlik Licenses API
    description: Manages tenant and user license entitlements in Qlik Cloud, including assignments, consumption tracking, and auto-assignment configuration.
    humanURL: https://qlik.dev/apis/rest/licenses/
    tags:
      - Licenses
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/licenses/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/licenses.json
  - aid: qlik:lineage-graphs
    name: Qlik Lineage Graphs API
    description: Manages data lineage graph visualizations that trace the origin and transformation of data across Qlik Cloud resources.
    humanURL: https://qlik.dev/apis/rest/lineage-graphs/
    tags:
      - Data Lineage
      - Governance
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/lineage-graphs/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/lineage-graphs.json
  - aid: qlik:login
    name: Qlik Login API
    description: Manages login flows and session management for accessing Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/login/
    tags:
      - Authentication
      - Login
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/login/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/login.json
  - aid: qlik:ml
    name: Qlik Machine Learning API
    description: Manages machine learning experiments, models, and deployments within Qlik Cloud for predictive analytics.
    humanURL: https://qlik.dev/apis/rest/ml/
    tags:
      - Machine Learning
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/ml/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/ml.json
  - aid: qlik:questions
    name: Qlik Natural Language API
    description: Enables natural language question and answer interactions with data in Qlik Cloud analytics applications.
    humanURL: https://qlik.dev/apis/rest/questions/
    tags:
      - AI
      - Natural Language
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/questions/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/questions.json
  - aid: qlik:notes
    name: Qlik Notes API
    description: Manages notes and annotations attached to Qlik Cloud analytics content for collaboration and documentation.
    humanURL: https://qlik.dev/apis/rest/notes/
    tags:
      - Collaboration
      - Notes
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/notes/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/notes.json
  - aid: qlik:notifications
    name: Qlik Notifications API
    description: Manages notification preferences and delivery for Qlik Cloud events and alerts.
    humanURL: https://qlik.dev/apis/rest/notifications/
    tags:
      - Notifications
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/notifications/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/notifications.json
  - aid: qlik:oauth
    name: Qlik OAuth API
    description: Manages OAuth 2.0 authorization flows for secure authentication with Qlik Cloud APIs.
    humanURL: https://qlik.dev/apis/rest/oauth/
    tags:
      - Authentication
      - OAuth
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/oauth/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/oauth.json
  - aid: qlik:oauth-clients
    name: Qlik OAuth Clients API
    description: Manages OAuth client registrations for applications integrating with Qlik Cloud through OAuth 2.0.
    humanURL: https://qlik.dev/apis/rest/oauth-clients/
    tags:
      - Clients
      - OAuth
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/oauth-clients/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/oauth-clients.json
  - aid: qlik:oauth-tokens
    name: Qlik OAuth Tokens API
    description: Lists and revokes active OAuth tokens for managing authenticated sessions in Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/oauth-tokens/
    tags:
      - OAuth
      - Tokens
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/oauth-tokens/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/oauth-tokens.json
  - aid: qlik:well-known
    name: Qlik OAuth Well-Known Configuration API
    description: Returns OAuth 2.0 metadata related to the tenant, including authorization endpoint, token endpoint, and supported grant types.
    humanURL: https://qlik.dev/apis/rest/.well-known/
    tags:
      - Configuration
      - OAuth
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/.well-known/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/.well-known.json
  - aid: qlik:quotas
    name: Qlik Quotas API
    description: Returns entitled attributes based on the license, providing information about resource limits and usage quotas.
    humanURL: https://qlik.dev/apis/rest/quotas/
    tags:
      - Licensing
      - Quotas
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/quotas/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/quotas.json
  - aid: qlik:reload-tasks
    name: Qlik Reload Tasks API
    description: Manages scheduled reload tasks for analytics applications, enabling automated data refresh on defined schedules.
    humanURL: https://qlik.dev/apis/rest/reload-tasks/
    tags:
      - Reloads
      - Scheduling
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/reload-tasks/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/reload-tasks.json
  - aid: qlik:reloads
    name: Qlik Reloads API
    description: Triggers and manages app data reloads to refresh analytics application data via REST API instead of only through the JSON-RPC WebSocket API.
    humanURL: https://qlik.dev/apis/rest/reloads/
    tags:
      - Data Refresh
      - Reloads
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/reloads/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/reloads.json
  - aid: qlik:report-templates
    name: Qlik Report Templates API
    description: Manages report templates that define the structure and formatting of generated reports from Qlik analytics data.
    humanURL: https://qlik.dev/apis/rest/report-templates/
    tags:
      - Reports
      - Templates
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/report-templates/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/report-templates.json
  - aid: qlik:reports
    name: Qlik Reports API
    description: Generates downloadable report assets from data in analytics applications, supporting multiple output formats including Excel, PDF, PowerPoint, HTML, and images.
    humanURL: https://qlik.dev/apis/rest/reports/
    tags:
      - Reports
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/reports/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/reports.json
  - aid: qlik:roles
    name: Qlik Roles API
    description: Manages tenant roles that are assigned to users or groups to control permissions and access within Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/roles/
    tags:
      - Access Control
      - Roles
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/roles/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/roles.json
  - aid: qlik:sharing-tasks
    name: Qlik Sharing Tasks API
    description: Manages sharing tasks for distributing analytics content and reports to recipients within Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/sharing-tasks/
    tags:
      - Distribution
      - Sharing
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/sharing-tasks/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/sharing-tasks.json
  - aid: qlik:tasks
    name: Qlik Tasks API
    description: Manages general task scheduling and execution within Qlik Cloud for orchestrating platform operations.
    humanURL: https://qlik.dev/apis/rest/tasks/
    tags:
      - Scheduling
      - Tasks
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/tasks/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/tasks.json
  - aid: qlik:temp-contents
    name: Qlik Temporary Contents API
    description: Manages temporary content storage for file uploads and transient data within Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/temp-contents/
    tags:
      - Temporary Storage
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/temp-contents/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/temp-contents.json
  - aid: qlik:tenants
    name: Qlik Tenants API
    description: Manages Qlik Cloud tenant configurations, settings, and metadata.
    humanURL: https://qlik.dev/apis/rest/tenants/
    tags:
      - Tenants
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/tenants/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/tenants.json
  - aid: qlik:tenant-settings
    name: Qlik Tenant Settings API
    description: Manages tenant-level configuration settings for customizing the behavior of the Qlik Cloud platform.
    humanURL: https://qlik.dev/apis/rest/tenant-settings/
    tags:
      - Settings
      - Tenants
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/tenant-settings/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/tenant-settings.json
  - aid: qlik:themes
    name: Qlik Themes API
    description: Manages themes for customizing the styling and appearance of the Qlik Sense client experience, including uploading, downloading, and managing theme archives.
    humanURL: https://qlik.dev/apis/rest/themes/
    tags:
      - Customization
      - Themes
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/themes/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/themes.json
  - aid: qlik:transports
    name: Qlik Email Configuration API
    description: Manages email transport configuration for sending notifications and reports from Qlik Cloud.
    humanURL: https://qlik.dev/apis/rest/transports/
    tags:
      - Configuration
      - Email
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/transports/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/transports.json
  - aid: qlik:ui-config
    name: Qlik Pinned Links API
    description: Manages administrator-defined pinned links displayed in the Qlik Cloud interface for quick access to resources.
    humanURL: https://qlik.dev/apis/rest/ui-config/
    tags:
      - Links
      - UI Configuration
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/ui-config/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/ui-config.json
  - aid: qlik:web-integrations
    name: Qlik Web Integrations API
    description: Manages web integration configurations that allow external websites to embed and interact with Qlik Cloud content.
    humanURL: https://qlik.dev/apis/rest/web-integrations/
    tags:
      - Embedding
      - Web Integrations
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/web-integrations/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/web-integrations.json
  - aid: qlik:web-notifications
    name: Qlik Web Notifications API
    description: Manages web-based push notifications for real-time updates within the Qlik Cloud user interface.
    humanURL: https://qlik.dev/apis/rest/web-notifications/
    tags:
      - Notifications
      - Web
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/web-notifications/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/web-notifications.json
  - aid: qlik:webhooks
    name: Qlik Webhooks API
    description: Manages webhooks for providing real-time event information from Qlik Cloud to external applications, with delivery history tracking.
    humanURL: https://qlik.dev/apis/rest/webhooks/
    tags:
      - Events
      - Webhooks
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/webhooks/
      - type: OpenAPI
        url: https://qlik.dev/specs/rest/webhooks.json
  - aid: qlik:ip-policies
    name: Qlik IP Policies API
    description: Manages IP restriction policies for controlling network access to the Qlik Cloud tenant.
    humanURL: https://qlik.dev/apis/rest/core/ip-policies/
    tags:
      - IP Policies
      - Security
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/core/ip-policies/
  - aid: qlik:change-stores
    name: Qlik Change Stores API
    description: Manages change store configurations for tracking and storing changes in analytics data.
    humanURL: https://qlik.dev/apis/rest/analytics/change-stores/
    tags:
      - Analytics
      - Change Tracking
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/analytics/change-stores/
  - aid: qlik:data-products
    name: Qlik Data Products API
    description: Manages data products within the Qlik data governance framework, enabling the packaging and sharing of curated data assets.
    humanURL: https://qlik.dev/apis/rest/data-governance/data-products/
    tags:
      - Data Products
      - Governance
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/rest/data-governance/data-products/
  - aid: qlik:qix
    name: Qlik Engine JSON-RPC API
    description: The JSON-RPC API over WebSocket that enables interaction with the Qlik Associative Engine for Qlik Sense applications, providing session-based access to app data models, objects, and calculations.
    humanURL: https://qlik.dev/apis/json-rpc/qix/
    tags:
      - Engine
      - JSON-RPC
      - WebSocket
    properties:
      - type: Documentation
        url: https://qlik.dev/apis/json-rpc/qix/
      - type: OpenRPC
        url: https://qlik.dev/specs/json-rpc/qix.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - url: https://qlik.dev
    type: DeveloperPortal
  - url: https://qlik.dev/authenticate
    type: Authentication
  - url: https://qlik.dev/get-started
    type: GettingStarted
  - url: https://qlik.dev/toolkits/qlik-api/
    type: SDK
  - url: https://qlik.dev/toolkits/qlik-cli/
    type: CLI
  - url: https://qlik.dev/apis/rest/
    type: Documentation
  - url: https://qlik.dev/apis/rest/rate-limiting/
    type: RateLimits
  - url: https://qlik.dev/examples/
    type: CodeExamples
  - url: https://qlik.dev/changelog/
    type: ChangeLog
  - url: https://github.com/qlik-oss
    type: GitHubOrganization
  - url: https://status.qlikcloud.com/
    type: StatusPage
  - url: https://community.qlik.com/t5/Qlik-Design-Blog/bg-p/qlik-design-blog
    type: Blog
  - url: https://community.qlik.com
    type: Community
  - url: https://support.qlik.com
    type: Support
  - url: https://www.qlik.com/us/legal/license-terms
    type: TermsOfService
  - url: https://www.qlik.com/us/legal/privacy
    type: PrivacyPolicy
  - url: https://www.qlik.com/us/products/qlik-cloud
    type: Features
  - url: https://www.qlik.com/us/solutions
    type: UseCases
  - url: https://www.qlik.com/us/products/technology-partners
    type: Integrations
---
