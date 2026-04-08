---
aid: qliksense
url: https://raw.githubusercontent.com/api-evangelist/qliksense/refs/heads/main/apis.yml
apis:
- name: Qlik Engine API
  description: JSON-RPC WebSocket API for interacting with the Qlik Associative Engine, creating and manipulating apps, and building visualizations.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/json-rpc/qix
  baseURL: wss://your-tenant.qlikcloud.com/app/
  tags:
  - Analytics
  - Business Intelligence
  - JSON-RPC
  - WebSocket
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/json-rpc/qix
  - type: OpenAPI
    url: https://qlik.dev/apis/json-rpc/qix/schema
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
    url: https://community.qlik.com/
- name: Qlik Repository API
  description: REST API for managing Qlik Sense repository entities including apps, streams, users, and security rules.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://help.qlik.com/en-US/sense-developer/APIs/RepositoryServiceAPI/
  baseURL: https://your-server:4242/qrs/
  tags:
  - Administration
  - Management
  - Repository
  - REST
  properties:
  - type: Documentation
    url: https://help.qlik.com/en-US/sense-developer/APIs/RepositoryServiceAPI/
  - type: API Reference
    url: https://help.qlik.com/en-US/sense-developer/APIs/RepositoryServiceAPI/index.html
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
    url: https://community.qlik.com/
- name: Qlik Cloud Platform API
  description: REST APIs for Qlik Cloud services including tenants, users, spaces, apps, and data connections.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest
  baseURL: https://your-tenant.qlikcloud.com/api/v1/
  tags:
  - Cloud
  - Platform
  - REST
  - SaaS
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest
  - type: OpenAPI
    url: https://qlik.dev/apis/rest/apps/openapi.json
  - type: Authentication
    url: https://qlik.dev/authenticate
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
    url: https://community.qlik.com/
- name: Qlik Apps API
  description: Manage Qlik Sense applications including creating, updating, publishing, and deleting apps.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/apps
  baseURL: https://your-tenant.qlikcloud.com/api/v1/apps
  tags:
  - Applications
  - Apps
  - Cloud
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/apps
  - type: OpenAPI
    url: https://qlik.dev/apis/rest/apps/openapi.json
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Users API
  description: Manage users, groups, and authentication in Qlik Sense.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/users
  baseURL: https://your-tenant.qlikcloud.com/api/v1/users
  tags:
  - Authentication
  - Identity
  - REST
  - Users
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/users
  - type: OpenAPI
    url: https://qlik.dev/apis/rest/users/openapi.json
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Data Connections API
  description: Create and manage data connections to various data sources.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/data-connections
  baseURL: https://your-tenant.qlikcloud.com/api/v1/data-connections
  tags:
  - Connections
  - Data
  - Integration
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/data-connections
  - type: OpenAPI
    url: https://qlik.dev/apis/rest/data-connections/openapi.json
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Spaces API
  description: Manage shared and managed spaces for collaboration and content organization.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/spaces
  baseURL: https://your-tenant.qlikcloud.com/api/v1/spaces
  tags:
  - Collaboration
  - Organization
  - REST
  - Spaces
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/spaces
  - type: OpenAPI
    url: https://qlik.dev/apis/rest/spaces/openapi.json
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Reload API
  description: Trigger and manage data reload operations for Qlik Sense apps.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/reloads
  baseURL: https://your-tenant.qlikcloud.com/api/v1/reloads
  tags:
  - Data
  - ETL
  - Reload
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/reloads
  - type: OpenAPI
    url: https://qlik.dev/apis/rest/reloads/openapi.json
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Tenants API
  description: Configure and manage Qlik Cloud tenants, the highest level of logical container supporting key tenant settings.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/tenants
  baseURL: https://your-tenant.qlikcloud.com/api/v1/tenants
  tags:
  - Administration
  - Configuration
  - REST
  - Tenants
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/tenants
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Items API
  description: List and manage core resources in the Qlik platform including apps, automations, and data sets that a user has access to.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/items
  baseURL: https://your-tenant.qlikcloud.com/api/v1/items
  tags:
  - Catalog
  - Items
  - Resources
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/items
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Collections API
  description: Catalog content using tags, public and private collections, and favorites for organizing resources users have access to.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/collections
  baseURL: https://your-tenant.qlikcloud.com/api/v1/collections
  tags:
  - Catalog
  - Collections
  - Organization
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/collections
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Automations API
  description: Create and manage no-code automation workflows in Qlik Automate that connect applications together.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/automations
  baseURL: https://your-tenant.qlikcloud.com/api/v1/automations
  tags:
  - Automations
  - No-Code
  - REST
  - Workflows
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/automations
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Webhooks API
  description: Create and manage webhooks to provide other applications with real-time information from Qlik Cloud events.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/webhooks
  baseURL: https://your-tenant.qlikcloud.com/api/v1/webhooks
  tags:
  - Events
  - Real-Time
  - REST
  - Webhooks
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/webhooks
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Themes API
  description: Manage custom themes to style and customize the Qlik Sense client experience.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/themes
  baseURL: https://your-tenant.qlikcloud.com/api/v1/themes
  tags:
  - Customization
  - REST
  - Styling
  - Themes
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/themes
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Extensions API
  description: Manage visualization extensions that allow third-party visualizations and presentation objects in Qlik Sense.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/extensions
  baseURL: https://your-tenant.qlikcloud.com/api/v1/extensions
  tags:
  - Customization
  - Extensions
  - REST
  - Visualizations
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/extensions
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Brands API
  description: Manage custom branding assets for applying brand identity to a Qlik Cloud tenant.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/brands
  baseURL: https://your-tenant.qlikcloud.com/api/v1/brands
  tags:
  - Branding
  - Brands
  - Customization
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/brands
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Groups API
  description: Manage groups to which space and tenant roles can be assigned for simplified access control management.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/groups
  baseURL: https://your-tenant.qlikcloud.com/api/v1/groups
  tags:
  - Access Control
  - Groups
  - Identity
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/groups
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Roles API
  description: Manage tenant roles assigned to users or groups that define permissions in the tenant.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/roles
  baseURL: https://your-tenant.qlikcloud.com/api/v1/roles
  tags:
  - Access Control
  - Permissions
  - REST
  - Roles
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/roles
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Licenses API
  description: Manage tenant and user license entitlements and track consumption usage.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/licenses
  baseURL: https://your-tenant.qlikcloud.com/api/v1/licenses
  tags:
  - Administration
  - Entitlements
  - Licenses
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/licenses
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik API Keys API
  description: Configure and manage API keys for authenticating with Qlik Cloud tenant APIs.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/api-keys
  baseURL: https://your-tenant.qlikcloud.com/api/v1/api-keys
  tags:
  - API Keys
  - Authentication
  - REST
  - Security
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/api-keys
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Audits API
  description: Access events emitted upon each action taken in a tenant for detailed audit logging.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/audits
  baseURL: https://your-tenant.qlikcloud.com/api/v1/audits
  tags:
  - Audits
  - Compliance
  - Logging
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/audits
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Quotas API
  description: Track usage and manage quotas for entitled features in a Qlik Cloud tenant.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/quotas
  baseURL: https://your-tenant.qlikcloud.com/api/v1/quotas
  tags:
  - Limits
  - Quotas
  - REST
  - Usage
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/quotas
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Data Files API
  description: Manage flat file storage associated with spaces in a Qlik Cloud tenant.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/data-files
  baseURL: https://your-tenant.qlikcloud.com/api/v1/data-files
  tags:
  - Data
  - Data Files
  - REST
  - Storage
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/data-files
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Data Sets API
  description: Manage and catalog data sets within Qlik Cloud for analytics and data integration.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/data-sets
  baseURL: https://your-tenant.qlikcloud.com/api/v1/data-sets
  tags:
  - Catalog
  - Data
  - Data Sets
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/data-sets
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Data Sources API
  description: List and manage data sources available for use in Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/data-sources
  baseURL: https://your-tenant.qlikcloud.com/api/v1/data-sources
  tags:
  - Data
  - Data Sources
  - Integration
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/data-sources
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Data Stores API
  description: Manage data stores for data integration and storage in Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/data-stores
  baseURL: https://your-tenant.qlikcloud.com/api/v1/data-stores
  tags:
  - Data Integration
  - Data Stores
  - REST
  - Storage
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/data-stores
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Data Credentials API
  description: Manage credentials used for authenticating with data sources in Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/data-credentials
  baseURL: https://your-tenant.qlikcloud.com/api/v1/data-credentials
  tags:
  - Authentication
  - Credentials
  - Data
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/data-credentials
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Data Alerts API
  description: Create and manage alerts that trigger notifications when conditions in a data set are fulfilled.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/data-alerts
  baseURL: https://your-tenant.qlikcloud.com/api/v1/data-alerts
  tags:
  - Alerts
  - Monitoring
  - Notifications
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/data-alerts
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Data Assets API
  description: Manage and catalog data assets within Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/data-assets
  baseURL: https://your-tenant.qlikcloud.com/api/v1/data-assets
  tags:
  - Catalog
  - Data
  - Data Assets
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/data-assets
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Data Qualities API
  description: Programmatically compute and retrieve data quality results for data sets in Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/data-qualities
  baseURL: https://your-tenant.qlikcloud.com/api/v1/data-qualities
  tags:
  - Data
  - Data Quality
  - REST
  - Validation
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/data-qualities
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Data Products API
  description: Create and manage data products for organizing and sharing curated data in Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/data-products
  baseURL: https://your-tenant.qlikcloud.com/api/v1/data-products
  tags:
  - Data Products
  - Data Sharing
  - Governance
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/data-products
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Data Integration Projects API
  description: Group and organize data tasks that move, transform, or prepare data for consumption including pipelines and replication flows.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/di-projects
  baseURL: https://your-tenant.qlikcloud.com/api/v1/di-projects
  tags:
  - Data Integration
  - ETL
  - Pipelines
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/di-projects
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Reports API
  description: Generate downloadable report assets from data with configurable templates and output formats.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/reports
  baseURL: https://your-tenant.qlikcloud.com/api/v1/reports
  tags:
  - Documents
  - Export
  - Reports
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/reports
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Report Templates API
  description: Manage report templates used for generating formatted reports in Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/report-templates
  baseURL: https://your-tenant.qlikcloud.com/api/v1/report-templates
  tags:
  - Documents
  - Reports
  - REST
  - Templates
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/report-templates
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Sharing Tasks API
  description: Define scheduled execution of capabilities such as reports, data alerts, and subscriptions with configurable conditions.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/sharing-tasks
  baseURL: https://your-tenant.qlikcloud.com/api/v1/sharing-tasks
  tags:
  - REST
  - Scheduling
  - Sharing
  - Tasks
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/sharing-tasks
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Conditions API
  description: Manage conditions used by data alerting and subscriptions to determine when actions should be taken based on app data.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/conditions
  baseURL: https://your-tenant.qlikcloud.com/api/v1/conditions
  tags:
  - Alerting
  - Conditions
  - REST
  - Rules
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/conditions
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Notes API
  description: Create and manage collaborative notes within Qlik Cloud for team communication.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/notes
  baseURL: https://your-tenant.qlikcloud.com/api/v1/notes
  tags:
  - Collaboration
  - Communication
  - Notes
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/notes
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Glossaries API
  description: Manage business glossaries for defining and standardizing terminology across Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/glossaries
  baseURL: https://your-tenant.qlikcloud.com/api/v1/glossaries
  tags:
  - Glossaries
  - Governance
  - REST
  - Terminology
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/glossaries
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Natural Language API
  description: Parse natural language queries with support for language configuration, visualization generation, and conversation context.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/questions
  baseURL: https://your-tenant.qlikcloud.com/api/v1/questions
  tags:
  - AI
  - Natural Language
  - NLP
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/questions
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Notifications API
  description: Manage notifications and notification settings for Qlik Cloud users.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/notifications
  baseURL: https://your-tenant.qlikcloud.com/api/v1/notifications
  tags:
  - Alerts
  - Communication
  - Notifications
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/notifications
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Web Notifications API
  description: Manage web-based notification delivery for Qlik Cloud users.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/web-notifications
  baseURL: https://your-tenant.qlikcloud.com/api/v1/web-notifications
  tags:
  - Notifications
  - Real-Time
  - REST
  - Web
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/web-notifications
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Web Integrations API
  description: Manage web integrations for embedding Qlik Cloud content in external web applications.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/web-integrations
  baseURL: https://your-tenant.qlikcloud.com/api/v1/web-integrations
  tags:
  - Embedding
  - Integration
  - REST
  - Web Integrations
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/web-integrations
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Identity Providers API
  description: Configure and manage identity providers for authentication in Qlik Cloud tenants.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/identity-providers
  baseURL: https://your-tenant.qlikcloud.com/api/v1/identity-providers
  tags:
  - Authentication
  - Identity Providers
  - REST
  - SSO
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/identity-providers
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik OAuth Clients API
  description: Create and manage OAuth client configurations for secure third-party application authentication.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/oauth-clients
  baseURL: https://your-tenant.qlikcloud.com/api/v1/oauth-clients
  tags:
  - Authentication
  - OAuth
  - REST
  - Security
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/oauth-clients
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik OAuth Tokens API
  description: Manage OAuth tokens for authenticated access to Qlik Cloud resources.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/oauth-tokens
  baseURL: https://your-tenant.qlikcloud.com/api/v1/oauth-tokens
  tags:
  - Authentication
  - OAuth
  - REST
  - Tokens
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/oauth-tokens
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik OAuth API
  description: Manage OAuth authorization flows and token exchange for Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/oauth
  baseURL: https://your-tenant.qlikcloud.com/oauth
  tags:
  - Authentication
  - Authorization
  - OAuth
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/oauth
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik CSP Origins API
  description: Manage Content Security Policy origins for controlling which domains can embed Qlik Cloud content.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/csp-origins
  baseURL: https://your-tenant.qlikcloud.com/api/v1/csp-origins
  tags:
  - CSP
  - Embedding
  - REST
  - Security
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/csp-origins
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik CSRF Token API
  description: Generate CSRF tokens required when calling Qlik REST APIs in a browser context.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/csrf-token
  baseURL: https://your-tenant.qlikcloud.com/api/v1/csrf-token
  tags:
  - Authentication
  - CSRF
  - REST
  - Security
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/csrf-token
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Encryption API
  description: Configure and manage encryption keys for tenant-level data encryption in Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/encryption
  baseURL: https://your-tenant.qlikcloud.com/api/v1/encryption
  tags:
  - Encryption
  - Keys
  - REST
  - Security
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/encryption
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Lineage Graphs API
  description: Retrieve lineage information for specific Qlik items to understand data provenance and dependencies.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/lineage-graphs
  baseURL: https://your-tenant.qlikcloud.com/api/v1/lineage-graphs
  tags:
  - Data Governance
  - Lineage
  - Provenance
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/lineage-graphs
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Machine Learning API
  description: Generate profile insights to analyze data sets, create and manage ML experiments, deploy models, and run predictions.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/ml
  baseURL: https://your-tenant.qlikcloud.com/api/v1/ml
  tags:
  - AI
  - Machine Learning
  - Predictions
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/ml
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik AutoML Dataset Predictions API
  description: Run batch predictions on data sets using deployed AutoML models.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/automl-predictions
  baseURL: https://your-tenant.qlikcloud.com/api/v1/automl-predictions
  tags:
  - AutoML
  - Machine Learning
  - Predictions
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/automl-predictions
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik AutoML Real-Time Predictions API
  description: Run real-time predictions using deployed AutoML models for immediate scoring.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/automl-deployments
  baseURL: https://your-tenant.qlikcloud.com/api/v1/automl-deployments
  tags:
  - AutoML
  - Predictions
  - Real-Time
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/automl-deployments
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Assistants API
  description: Manage AI assistants providing chat interfaces powered by Qlik Answers for natural language data exploration.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/assistants
  baseURL: https://your-tenant.qlikcloud.com/api/v1/assistants
  tags:
  - AI
  - Assistants
  - Chat
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/assistants
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Knowledgebases API
  description: Manage collections of data sources indexed for generating responses to user questions via Qlik Answers assistants.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/knowledgebases
  baseURL: https://your-tenant.qlikcloud.com/api/v1/knowledgebases
  tags:
  - AI
  - Data Sources
  - Knowledgebases
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/knowledgebases
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Tasks API
  description: Manage and schedule task execution for various Qlik Cloud operations.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/tasks
  baseURL: https://your-tenant.qlikcloud.com/api/v1/tasks
  tags:
  - Operations
  - REST
  - Scheduling
  - Tasks
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/tasks
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Reload Tasks API
  description: Manage scheduled reload tasks for automating data refreshes in Qlik Cloud apps.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/reload-tasks
  baseURL: https://your-tenant.qlikcloud.com/api/v1/reload-tasks
  tags:
  - Data Refresh
  - Reload Tasks
  - REST
  - Scheduling
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/reload-tasks
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Temporary Contents API
  description: Manage temporary file storage used by services like apps and data-files for importing and exporting larger files.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/temp-contents
  baseURL: https://your-tenant.qlikcloud.com/api/v1/temp-contents
  tags:
  - Files
  - Import
  - REST
  - Temporary Storage
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/temp-contents
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Tenant Settings API
  description: Manage tenant-level configuration settings for Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/tenant-settings
  baseURL: https://your-tenant.qlikcloud.com/api/v1/tenant-settings
  tags:
  - Administration
  - Configuration
  - REST
  - Settings
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/tenant-settings
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Entitlement Consumption API
  description: Track consumption metrics and usage of entitled features within a Qlik Cloud tenant.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/consumption
  baseURL: https://your-tenant.qlikcloud.com/api/v1/consumption
  tags:
  - Consumption
  - Metrics
  - REST
  - Usage
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/consumption
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Direct Access Agents API
  description: Manage direct access agents for connecting to on-premises data sources from Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/direct-access-agents
  baseURL: https://your-tenant.qlikcloud.com/api/v1/direct-access-agents
  tags:
  - Connectivity
  - Direct Access
  - On-Premises
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/direct-access-agents
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Email Configuration API
  description: Configure tenant-level email and SMTP service settings for Qlik Cloud notifications.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/transports
  baseURL: https://your-tenant.qlikcloud.com/api/v1/transports
  tags:
  - Configuration
  - Email
  - REST
  - SMTP
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/transports
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Banners API
  description: Manage banners displayed to users within a Qlik Cloud tenant.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/banners
  baseURL: https://your-tenant.qlikcloud.com/api/v1/banners
  tags:
  - Administration
  - Banners
  - Communication
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/banners
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Pinned Links API
  description: Manage pinned links for quick access to resources within a Qlik Cloud tenant.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/pinned-links
  baseURL: https://your-tenant.qlikcloud.com/api/v1/pinned-links
  tags:
  - Customization
  - Links
  - Navigation
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/pinned-links
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik IP Policies API
  description: Manage IP allowlisting rules to control access to Qlik Cloud tenant resources.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/ip-policies
  baseURL: https://your-tenant.qlikcloud.com/api/v1/ip-policies
  tags:
  - Access Control
  - IP Policies
  - REST
  - Security
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/ip-policies
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Change Stores API
  description: Manage change data capture stores for tracking data changes in Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/change-stores
  baseURL: https://your-tenant.qlikcloud.com/api/v1/change-stores
  tags:
  - Change Data Capture
  - Data
  - REST
  - Tracking
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/change-stores
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Automation Connections API
  description: Manage connections used by automations to integrate with external applications.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/automation-connections
  baseURL: https://your-tenant.qlikcloud.com/api/v1/automation-connections
  tags:
  - Automations
  - Connections
  - Integration
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/automation-connections
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Automation Connectors API
  description: Manage connectors available for use in Qlik automation workflows.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/automation-connectors
  baseURL: https://your-tenant.qlikcloud.com/api/v1/automation-connectors
  tags:
  - Automations
  - Connectors
  - Integration
  - REST
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/automation-connectors
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
- name: Qlik Login API
  description: Manage login flows and authentication sessions for Qlik Cloud.
  image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
  humanURL: https://qlik.dev/apis/rest/login
  baseURL: https://your-tenant.qlikcloud.com/login
  tags:
  - Authentication
  - Login
  - REST
  - Sessions
  properties:
  - type: Documentation
    url: https://qlik.dev/apis/rest/login
  contact:
  - FN: Qlik Developer Support
    email: developer@qlik.com
name: Qlik Sense APIs
tags:
- Analytics
- Business Intelligence
- Cloud
- Data Visualization
- Enterprise
type: Contract
image: https://www.qlik.com/us/-/media/images/qlik/global/qlik-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of APIs for Qlik Sense, a business intelligence and visual analytics platform.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

