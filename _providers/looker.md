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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Looker Agentic Access
  operation_count: 29
  slug: looker-agentic-access
  summary_line: 29 operations · 13 acting
api_count: 10
apis:
- description: API for programmatically managing LookML projects, models, and views.
  name: LookML API
  slug: lookml
- description: The Looker Action API enables developers to define custom actions, or destinations, to which Looker can send query results, dashboard results, or user interactions via a webhook-like API.
  name: Looker Action API
  slug: action
- description: The Looker Embed SDK is a JavaScript library for embedding Looker content such as dashboards, Looks, Explores, reports, and extensions into web applications, with support for signed SSO and cookieless
  name: Looker Embed SDK
  slug: embed-sdk
- description: The Looker Extension Framework provides APIs and SDKs for building custom extensions that run inside the Looker UI, with access to the Looker API, Looker components library, and the Embed SDK.
  name: Looker Extension Framework API
  slug: extension-framework
- description: The Looker (Google Cloud core) REST API provides management capabilities for Looker instances running on Google Cloud, including instance lifecycle management, backups, and operations.
  name: Looker (Google Cloud core) API
  slug: google-cloud-core
- description: Authentication endpoints for obtaining and managing API access tokens using client credentials.
  name: Looker Auth API
  slug: looker-auth-api
- description: Manage dashboards, which are collections of tiles displaying visualizations from queries. Dashboards support filters, layouts, and can be shared across the organization.
  name: Looker Dashboard API
  slug: looker-dashboard-api
- description: Manage Looks, which are saved queries with visualizations. A Look contains a query definition and visualization configuration that can be shared, scheduled, and embedded.
  name: Looker Look API
  slug: looker-look-api
- description: Create and run queries against your Looker models. Queries define the fields, filters, sorts, and limits used to retrieve data from the underlying database through LookML models.
  name: Looker Query API
  slug: looker-query-api
- description: Manage Looker users including creating, updating, and retrieving user accounts, credentials, roles, and sessions.
  name: Looker User API
  slug: looker-user-api
artifact_total: 135
collections:
- collection_type: postman
  name: Looker Auth API
  slug: postman-looker-auth-api
- collection_type: postman
  name: Looker Auth Dashboard API
  slug: postman-looker-dashboard-api
- collection_type: postman
  name: Looker Auth Look API
  slug: postman-looker-look-api
- collection_type: postman
  name: Looker Auth Query API
  slug: postman-looker-query-api
- collection_type: postman
  name: Looker Auth User API
  slug: postman-looker-user-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Looker API
  slug: open-looker-api
- collection_type: open
  name: Looker Auth API
  slug: open-looker-auth-api
- collection_type: open
  name: Looker Auth Dashboard API
  slug: open-looker-dashboard-api
- collection_type: open
  name: Looker Auth Look API
  slug: open-looker-look-api
- collection_type: open
  name: Looker Auth Query API
  slug: open-looker-query-api
- collection_type: open
  name: Looker Auth User API
  slug: open-looker-user-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/looker-open-source/actions/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/looker-open-source/actions/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/looker-open-source/actions/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/looker-open-source/actions/blob/master/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/looker/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/looker-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/looker-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/looker-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/looker
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.looker.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/looker-open-source
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/looker/docs/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.looker.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://looker.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://looker.com/terms
- group: build
  title: ''
  type: SDKs
  url: https://docs.cloud.google.com/looker/docs/api-sdk
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/looker-open-source/sdk-codegen/blob/main/CHANGELOG.md
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://docs.cloud.google.com/looker/docs/release-notes
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/looker/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloud.google.com/looker/docs/api-getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.cloud.google.com/looker/docs/api-auth
- group: learn
  title: ''
  type: Tutorials
  url: https://developers.looker.com/api/tutorials/interactive-api-docs-whats-next/
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/looker-dashboard-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/looker-context.jsonld
created: '2024-01-01'
description: Looker is a business intelligence and data analytics platform that enables organizations to explore, analyze, and share real-time business analytics.
examples:
- key_count: 4
  name: Looker Access Token Example
  slug: looker-access-token-example
- key_count: 6
  name: Looker Credentials Api3 Example
  slug: looker-credentials-api3-example
- key_count: 5
  name: Looker Credentials Email Example
  slug: looker-credentials-email-example
- key_count: 14
  name: Looker Dashboard Element Example
  slug: looker-dashboard-element-example
- key_count: 28
  name: Looker Dashboard Example
  slug: looker-dashboard-example
- key_count: 13
  name: Looker Dashboard Filter Example
  slug: looker-dashboard-filter-example
- key_count: 7
  name: Looker Dashboard Layout Component Example
  slug: looker-dashboard-layout-component-example
- key_count: 7
  name: Looker Dashboard Layout Example
  slug: looker-dashboard-layout-example
- key_count: 2
  name: Looker Error Response Example
  slug: looker-error-response-example
- key_count: 7
  name: Looker Folder Base Example
  slug: looker-folder-base-example
- key_count: 18
  name: Looker Look Example
  slug: looker-look-example
- key_count: 2
  name: Looker Look Model Example
  slug: looker-look-model-example
- key_count: 6
  name: Looker Model Set Example
  slug: looker-model-set-example
- key_count: 6
  name: Looker Permission Set Example
  slug: looker-permission-set-example
- key_count: 22
  name: Looker Query Example
  slug: looker-query-example
- key_count: 6
  name: Looker Role Example
  slug: looker-role-example
- key_count: 14
  name: Looker Session Example
  slug: looker-session-example
- key_count: 6
  name: Looker Space Base Example
  slug: looker-space-base-example
- key_count: 25
  name: Looker User Example
  slug: looker-user-example
- key_count: 13
  name: Looker Write Dashboard Example
  slug: looker-write-dashboard-example
- key_count: 7
  name: Looker Write Look With Query Example
  slug: looker-write-look-with-query-example
- key_count: 16
  name: Looker Write Query Example
  slug: looker-write-query-example
- key_count: 5
  name: Looker Write User Example
  slug: looker-write-user-example
features:
- description: Enable business users to explore data, build visualizations, and create dashboards without SQL knowledge using LookML models.
  name: Self-Service Analytics
- description: Define reusable data models in LookML that provide a semantic layer between databases and end-user analytics.
  name: Data Modeling with LookML
- description: Embed interactive dashboards, reports, and data explorations directly into web applications using SSO and cookieless authentication.
  name: Embedded Analytics
- description: Schedule and deliver reports and dashboards via email, Slack, S3, or custom action destinations.
  name: Scheduled Reports
- description: Build webhook-based actions to send query results to any external destination or trigger workflows.
  name: Custom Actions
- description: Programmatically manage users, roles, dashboards, queries, and platform settings through the Looker API.
  name: API-Driven Administration
finops:
- name: Looker Finops
  service_category: Business Intelligence
  slug: looker-finops
image: https://looker.com/assets/img/images/logos/looker-logo.png
integrations:
- description: Native optimized connector for querying and analyzing data in Google BigQuery data warehouse.
  name: Google BigQuery
- description: High-performance connector for Snowflake cloud data warehouse with push-down query optimization.
  name: Snowflake
- description: Native connector for querying and visualizing data in Amazon Redshift data warehouse.
  name: Amazon Redshift
- description: Deliver scheduled reports and dashboard snapshots to Slack channels with interactive query capabilities.
  name: Slack
- description: Export query results and dashboard data directly to Google Sheets for collaborative analysis.
  name: Google Sheets
- description: Connect to Salesforce data for CRM analytics and combine with other data sources for unified views.
  name: Salesforce
json_schemas:
- name: AccessToken
  property_count: 4
  slug: looker-access-token
- name: AccessToken
  property_count: 4
  slug: looker-accesstoken
- name: CredentialsApi3
  property_count: 6
  slug: looker-credentials-api3
- name: CredentialsEmail
  property_count: 5
  slug: looker-credentials-email
- name: CredentialsApi3
  property_count: 6
  slug: looker-credentialsapi3
- name: CredentialsEmail
  property_count: 5
  slug: looker-credentialsemail
- name: DashboardElement
  property_count: 14
  slug: looker-dashboard-element
- name: DashboardFilter
  property_count: 13
  slug: looker-dashboard-filter
- name: DashboardLayoutComponent
  property_count: 7
  slug: looker-dashboard-layout-component
- name: DashboardLayout
  property_count: 7
  slug: looker-dashboard-layout
- name: Dashboard
  property_count: 28
  slug: looker-dashboard
- name: DashboardElement
  property_count: 16
  slug: looker-dashboardelement
- name: DashboardFilter
  property_count: 13
  slug: looker-dashboardfilter
- name: DashboardLayout
  property_count: 7
  slug: looker-dashboardlayout
- name: DashboardLayoutComponent
  property_count: 7
  slug: looker-dashboardlayoutcomponent
- name: ErrorResponse
  property_count: 2
  slug: looker-error-response
- name: ErrorResponse
  property_count: 2
  slug: looker-errorresponse
- name: FolderBase
  property_count: 7
  slug: looker-folder-base
- name: FolderBase
  property_count: 7
  slug: looker-folderbase
- name: LookModel
  property_count: 2
  slug: looker-look-model
- name: Look
  property_count: 18
  slug: looker-look
- name: LookModel
  property_count: 2
  slug: looker-lookmodel
- name: ModelSet
  property_count: 6
  slug: looker-model-set
- name: ModelSet
  property_count: 6
  slug: looker-modelset
- name: PermissionSet
  property_count: 6
  slug: looker-permission-set
- name: PermissionSet
  property_count: 6
  slug: looker-permissionset
- name: Query
  property_count: 22
  slug: looker-query
- name: Role
  property_count: 6
  slug: looker-role
- name: Session
  property_count: 14
  slug: looker-session
- name: SpaceBase
  property_count: 6
  slug: looker-space-base
- name: SpaceBase
  property_count: 6
  slug: looker-spacebase
- name: User
  property_count: 25
  slug: looker-user
- name: WriteDashboard
  property_count: 13
  slug: looker-write-dashboard
- name: WriteLookWithQuery
  property_count: 7
  slug: looker-write-look-with-query
- name: WriteQuery
  property_count: 16
  slug: looker-write-query
- name: WriteUser
  property_count: 5
  slug: looker-write-user
- name: WriteDashboard
  property_count: 13
  slug: looker-writedashboard
- name: WriteLookWithQuery
  property_count: 8
  slug: looker-writelookwithquery
- name: WriteQuery
  property_count: 16
  slug: looker-writequery
- name: WriteUser
  property_count: 5
  slug: looker-writeuser
json_structures:
- name: Looker Access Token Structure
  property_count: 4
  slug: looker-access-token-structure
- name: Looker Credentials Api3 Structure
  property_count: 6
  slug: looker-credentials-api3-structure
- name: Looker Credentials Email Structure
  property_count: 5
  slug: looker-credentials-email-structure
- name: Looker Dashboard Element Structure
  property_count: 14
  slug: looker-dashboard-element-structure
- name: Looker Dashboard Filter Structure
  property_count: 13
  slug: looker-dashboard-filter-structure
- name: Looker Dashboard Layout Component Structure
  property_count: 7
  slug: looker-dashboard-layout-component-structure
- name: Looker Dashboard Layout Structure
  property_count: 7
  slug: looker-dashboard-layout-structure
- name: Looker Dashboard Structure
  property_count: 28
  slug: looker-dashboard-structure
- name: Looker Error Response Structure
  property_count: 2
  slug: looker-error-response-structure
- name: Looker Folder Base Structure
  property_count: 7
  slug: looker-folder-base-structure
- name: Looker Look Model Structure
  property_count: 2
  slug: looker-look-model-structure
- name: Looker Look Structure
  property_count: 18
  slug: looker-look-structure
- name: Looker Model Set Structure
  property_count: 6
  slug: looker-model-set-structure
- name: Looker Permission Set Structure
  property_count: 6
  slug: looker-permission-set-structure
- name: Looker Query Structure
  property_count: 22
  slug: looker-query-structure
- name: Looker Role Structure
  property_count: 6
  slug: looker-role-structure
- name: Looker Session Structure
  property_count: 14
  slug: looker-session-structure
- name: Looker Space Base Structure
  property_count: 6
  slug: looker-space-base-structure
- name: Looker Structure
  property_count: 0
  slug: looker-structure
- name: Looker User Structure
  property_count: 25
  slug: looker-user-structure
- name: Looker Write Dashboard Structure
  property_count: 13
  slug: looker-write-dashboard-structure
- name: Looker Write Look With Query Structure
  property_count: 7
  slug: looker-write-look-with-query-structure
- name: Looker Write Query Structure
  property_count: 16
  slug: looker-write-query-structure
- name: Looker Write User Structure
  property_count: 5
  slug: looker-write-user-structure
jsonld:
- class_count: 0
  name: Looker Context
  property_count: 0
  slug: looker-context
layout: provider
modified: '2026-05-19'
name: Looker
nav: Providers
network: true
overview: 'Looker publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Dashboard API, Look API, and 2 more. Tagged areas include Analytics, BI Platform, Business Intelligence, Data Analytics, and Data Visualization.


  The Looker catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Looker''s developer surface includes authentication, support, changelog, release notes, pricing, getting-started guide, and 18 more developer resources.'
plans:
- name: Looker Plans Pricing
  plan_count: 7
  slug: looker-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 8
  name: Looker Rate Limits
  slug: looker-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Looker API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: looker-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Looker API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 8
  slug: looker-spectral-rules
score:
  band: developing
  composite: 41.3
  delta: -13.2
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 9.8
    contract_quality: 67.0
    developer_ergonomics: 35.7
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 34.2
  previous_composite: 54.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/looker/refs/heads/main/screenshots/looker-2026-06-20T184712.png
security:
- kind: authentication
  name: Looker Authentication
  slug: looker-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Looker Domain Security
  slug: looker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: looker
tags:
- Analytics
- BI Platform
- Business Intelligence
- Data Analytics
- Data Visualization
use_cases:
- description: Build real-time executive dashboards aggregating KPIs from multiple data sources for leadership visibility.
  name: Executive Dashboards
- description: Embed analytics into SaaS products to provide customers with self-service reporting and data exploration.
  name: Customer-Facing Analytics
- description: Monitor data quality, usage patterns, and access controls across the organization through audit reports.
  name: Data Governance Reporting
- description: Analyze campaign performance, attribution, and ROI across marketing channels with unified data models.
  name: Marketing Performance Analytics
- description: Track operational metrics and KPIs in real time with automated alerting and scheduled report delivery.
  name: Operational Monitoring
website: https://developers.looker.com/
---
