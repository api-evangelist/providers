---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Tableau Agentic Access
  operation_count: 70
  slug: tableau-agentic-access
  summary_line: 70 operations · 32 acting
api_count: 25
apis:
- description: GraphQL-based API for querying metadata about Tableau content, data sources, and lineage information.
  name: Tableau Metadata API
  slug: tableau-metadata-api
- description: API for creating, reading, and updating Hyper files, which are the data files that power Tableau extracts.
  name: Tableau Hyper API
  slug: tableau-hyper-api
- description: JavaScript API for embedding Tableau visualizations in web applications with advanced interaction capabilities.
  name: Tableau Embedding API
  slug: tableau-embedding-api
- description: Python library for programmatically updating Tableau workbook and data source files.
  name: Tableau Document API
  slug: tableau-document-api
- description: Python library that wraps the Tableau REST API for easier programmatic access.
  name: Tableau Server Client (Python)
  slug: tableau-server-client-python
- description: The Tableau Extensions API allows developers to create dashboard extensions and viz extensions that users can interact with directly in Tableau, enabling integration with other applications and custom
  name: Tableau Extensions API
  slug: tableau-extensions-api
- description: The Tableau Web Data Connector (WDC) provides an SDK for building connectors to any data accessible over HTTP, allowing users to bring external data into Tableau for analysis and visualization.
  name: Tableau Web Data Connector
  slug: tableau-web-data-connector
- description: SDK for developing custom Tableau connectors using ODBC or JDBC drivers, including documentation, example files, a test harness, and a packaging tool for distribution.
  name: Tableau Connector SDK
  slug: tableau-connector-sdk
- description: The Analytics Extensions API allows integration of external analytics engines such as Python, R, MATLAB, and data science platforms with Tableau calculations for advanced analytics.
  name: Tableau Analytics Extensions API
  slug: tableau-analytics-extensions-api
- description: Tableau Webhooks enable event-driven automation by sending HTTP POST notifications to specified URLs when events occur on Tableau Server or Tableau Cloud.
  name: Tableau Webhooks
  slug: tableau-webhooks
- description: The VizQL Data Service provides a programmatic HTTP interface to query published data sources outside of Tableau visualizations, enabling headless data access from any application.
  name: Tableau VizQL Data Service
  slug: tableau-vizql-data-service
- description: The Tableau Pulse API enables programmatic creation, management, and querying of Tableau Pulse metrics and subscriptions, as well as embedding Pulse insights into web applications.
  name: Tableau Pulse API
  slug: tableau-pulse-api
- description: Sign in and sign out of Tableau Server or Tableau Cloud. You must sign in to obtain an authentication token before calling other methods.
  name: Tableau Authentication API
  slug: tableau-authentication-api
- description: Publish, query, update, delete, and download data sources. Data sources define the connection to data and can be shared across multiple workbooks.
  name: Tableau Data Sources API
  slug: tableau-data-sources-api
- description: Add and remove content items from a user's list of favorites, including workbooks, views, data sources, projects, and flows.
  name: Tableau Favorites API
  slug: tableau-favorites-api
- description: Create, update, delete, and query groups. Groups are collections of users that simplify permission management.
  name: Tableau Groups API
  slug: tableau-groups-api
- description: Query and cancel background jobs on a site, including extract refreshes, subscriptions, and flow runs.
  name: Tableau Jobs API
  slug: tableau-jobs-api
- description: Query and set permissions on content items including workbooks, data sources, projects, views, and flows.
  name: Tableau Permissions API
  slug: tableau-permissions-api
- description: Create, update, delete, and query projects. Projects are containers for organizing workbooks, data sources, and other content on a site.
  name: Tableau Projects API
  slug: tableau-projects-api
- description: Create, update, delete, and query schedules for extract refreshes and subscriptions on Tableau Server.
  name: Tableau Schedules API
  slug: tableau-schedules-api
- description: Manage sites on Tableau Server. A site is a collection of users, groups, projects, workbooks, data sources, and other resources.
  name: Tableau Sites API
  slug: tableau-sites-api
- description: Create, update, delete, and query subscriptions. Subscriptions deliver snapshots of views to users on a schedule.
  name: Tableau Subscriptions API
  slug: tableau-subscriptions-api
- description: Add, update, remove, and query users on a site. Users are individuals who can sign in to Tableau Server or Tableau Cloud.
  name: Tableau Users API
  slug: tableau-users-api
- description: Query views and download view images or data. Views are the individual sheets, dashboards, or stories within a workbook.
  name: Tableau Views API
  slug: tableau-views-api
- description: Publish, query, update, delete, and download workbooks. Workbooks contain one or more views (sheets, dashboards, or stories) and can connect to one or more data sources.
  name: Tableau Workbooks API
  slug: tableau-workbooks-api
artifact_total: 363
collections:
- collection_type: postman
  name: Tableau REST Authentication API
  slug: postman-tableau-authentication-api
- collection_type: postman
  name: Tableau REST Authentication Data Sources API
  slug: postman-tableau-data-sources-api
- collection_type: postman
  name: Tableau REST Authentication Favorites API
  slug: postman-tableau-favorites-api
- collection_type: postman
  name: Tableau REST Authentication Groups API
  slug: postman-tableau-groups-api
- collection_type: postman
  name: Tableau REST Authentication Jobs API
  slug: postman-tableau-jobs-api
- collection_type: postman
  name: Tableau REST Authentication Permissions API
  slug: postman-tableau-permissions-api
- collection_type: postman
  name: Tableau REST Authentication Projects API
  slug: postman-tableau-projects-api
- collection_type: postman
  name: Tableau REST Authentication Schedules API
  slug: postman-tableau-schedules-api
- collection_type: postman
  name: Tableau REST Authentication Sites API
  slug: postman-tableau-sites-api
- collection_type: postman
  name: Tableau REST Authentication Subscriptions API
  slug: postman-tableau-subscriptions-api
- collection_type: postman
  name: Tableau REST Authentication Users API
  slug: postman-tableau-users-api
- collection_type: postman
  name: Tableau REST Authentication Views API
  slug: postman-tableau-views-api
- collection_type: postman
  name: Tableau REST Authentication Workbooks API
  slug: postman-tableau-workbooks-api
- collection_type: open
  name: Tableau REST API
  slug: open-tableau-rest-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tableau/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tableau-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tableau-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tableau-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tableau-software
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tableau.com/developer
- group: company
  title: ''
  type: Blog
  url: https://www.tableau.com/blog/developers
- group: operate
  title: ''
  type: Support
  url: https://www.tableau.com/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tableau
- group: operate
  title: ''
  type: StatusPage
  url: https://trust.tableau.com/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://help.tableau.com/current/tableau/en-us/whatsnew_all.htm
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tableau.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tableau.com/privacy
- group: start
  title: ''
  type: Signup
  url: https://www.tableau.com/products/trial
- group: start
  title: ''
  type: Login
  url: https://www.tableau.com/tableau-login-hub
- group: docs
  title: ''
  type: Documentation
  url: https://help.tableau.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/tableau
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Tableau
- group: learn
  title: ''
  type: Training
  url: https://www.tableau.com/developer/learning
- group: design
  title: ''
  type: SpectralRules
  url: rules/tableau-spectral-rules.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/tableau/tableau-mcp
created: '2024'
description: Tableau is a visual analytics platform transforming the way we use data to solve problems—empowering people and organizations to make the most of their data.
examples:
- key_count: 6
  name: Tableau Adddatasourcepermissions Example
  slug: tableau-adddatasourcepermissions-example
- key_count: 6
  name: Tableau Addfavorites Example
  slug: tableau-addfavorites-example
- key_count: 6
  name: Tableau Addtagstodatasource Example
  slug: tableau-addtagstodatasource-example
- key_count: 6
  name: Tableau Addtagstoworkbook Example
  slug: tableau-addtagstoworkbook-example
- key_count: 6
  name: Tableau Addusertogroup Example
  slug: tableau-addusertogroup-example
- key_count: 6
  name: Tableau Addusertosite Example
  slug: tableau-addusertosite-example
- key_count: 6
  name: Tableau Addworkbookpermissions Example
  slug: tableau-addworkbookpermissions-example
- key_count: 6
  name: Tableau Creategroup Example
  slug: tableau-creategroup-example
- key_count: 6
  name: Tableau Createproject Example
  slug: tableau-createproject-example
- key_count: 6
  name: Tableau Createsite Example
  slug: tableau-createsite-example
- key_count: 6
  name: Tableau Createsubscription Example
  slug: tableau-createsubscription-example
- key_count: 6
  name: Tableau Downloaddatasource Example
  slug: tableau-downloaddatasource-example
- key_count: 6
  name: Tableau Downloadworkbook Example
  slug: tableau-downloadworkbook-example
- key_count: 6
  name: Tableau Getdatasourcerevisions Example
  slug: tableau-getdatasourcerevisions-example
- key_count: 6
  name: Tableau Getfavorites Example
  slug: tableau-getfavorites-example
- key_count: 6
  name: Tableau Getgroupmembers Example
  slug: tableau-getgroupmembers-example
- key_count: 6
  name: Tableau Getrecommendationsforviews Example
  slug: tableau-getrecommendationsforviews-example
- key_count: 6
  name: Tableau Getusers Example
  slug: tableau-getusers-example
- key_count: 6
  name: Tableau Getworkbookrevisions Example
  slug: tableau-getworkbookrevisions-example
- key_count: 6
  name: Tableau Publishworkbook Example
  slug: tableau-publishworkbook-example
- key_count: 6
  name: Tableau Querydatasource Example
  slug: tableau-querydatasource-example
- key_count: 6
  name: Tableau Querydatasourceconnections Example
  slug: tableau-querydatasourceconnections-example
- key_count: 6
  name: Tableau Querydatasourcepermissions Example
  slug: tableau-querydatasourcepermissions-example
- key_count: 6
  name: Tableau Querydatasources Example
  slug: tableau-querydatasources-example
- key_count: 6
  name: Tableau Querydatasourcetags Example
  slug: tableau-querydatasourcetags-example
- key_count: 6
  name: Tableau Querydefaultworkbookpermissions Example
  slug: tableau-querydefaultworkbookpermissions-example
- key_count: 6
  name: Tableau Querygroups Example
  slug: tableau-querygroups-example
- key_count: 6
  name: Tableau Queryjob Example
  slug: tableau-queryjob-example
- key_count: 6
  name: Tableau Queryjobs Example
  slug: tableau-queryjobs-example
- key_count: 6
  name: Tableau Queryprojects Example
  slug: tableau-queryprojects-example
- key_count: 6
  name: Tableau Queryschedules Example
  slug: tableau-queryschedules-example
- key_count: 6
  name: Tableau Querysite Example
  slug: tableau-querysite-example
- key_count: 6
  name: Tableau Querysites Example
  slug: tableau-querysites-example
- key_count: 6
  name: Tableau Querysubscription Example
  slug: tableau-querysubscription-example
- key_count: 6
  name: Tableau Querysubscriptions Example
  slug: tableau-querysubscriptions-example
- key_count: 6
  name: Tableau Queryuser Example
  slug: tableau-queryuser-example
- key_count: 6
  name: Tableau Queryviewbyid Example
  slug: tableau-queryviewbyid-example
- key_count: 6
  name: Tableau Queryviewdata Example
  slug: tableau-queryviewdata-example
- key_count: 6
  name: Tableau Queryviewimage Example
  slug: tableau-queryviewimage-example
- key_count: 6
  name: Tableau Queryviewpdf Example
  slug: tableau-queryviewpdf-example
- key_count: 6
  name: Tableau Queryviewpreviewimage Example
  slug: tableau-queryviewpreviewimage-example
- key_count: 6
  name: Tableau Queryviewsforsite Example
  slug: tableau-queryviewsforsite-example
- key_count: 6
  name: Tableau Queryviewsforworkbook Example
  slug: tableau-queryviewsforworkbook-example
- key_count: 6
  name: Tableau Queryworkbook Example
  slug: tableau-queryworkbook-example
- key_count: 6
  name: Tableau Queryworkbookconnections Example
  slug: tableau-queryworkbookconnections-example
- key_count: 6
  name: Tableau Queryworkbookpermissions Example
  slug: tableau-queryworkbookpermissions-example
- key_count: 6
  name: Tableau Queryworkbookpreviewimage Example
  slug: tableau-queryworkbookpreviewimage-example
- key_count: 6
  name: Tableau Queryworkbooksforsite Example
  slug: tableau-queryworkbooksforsite-example
- key_count: 6
  name: Tableau Queryworkbooksforuser Example
  slug: tableau-queryworkbooksforuser-example
- key_count: 6
  name: Tableau Queryworkbooktags Example
  slug: tableau-queryworkbooktags-example
- key_count: 1
  name: Tableau Rest Add Favorite Request Example
  slug: tableau-rest-add-favorite-request-example
- key_count: 0
  name: Tableau Rest Add Permissions Request Example
  slug: tableau-rest-add-permissions-request-example
- key_count: 1
  name: Tableau Rest Add User Request Example
  slug: tableau-rest-add-user-request-example
- key_count: 6
  name: Tableau Rest Connection Example
  slug: tableau-rest-connection-example
- key_count: 1
  name: Tableau Rest Connection List Response Example
  slug: tableau-rest-connection-list-response-example
- key_count: 1
  name: Tableau Rest Create Group Request Example
  slug: tableau-rest-create-group-request-example
- key_count: 1
  name: Tableau Rest Create Project Request Example
  slug: tableau-rest-create-project-request-example
- key_count: 1
  name: Tableau Rest Create Site Request Example
  slug: tableau-rest-create-site-request-example
- key_count: 1
  name: Tableau Rest Create Subscription Request Example
  slug: tableau-rest-create-subscription-request-example
- key_count: 15
  name: Tableau Rest Data Source Example
  slug: tableau-rest-data-source-example
- key_count: 1
  name: Tableau Rest Data Source List Response Example
  slug: tableau-rest-data-source-list-response-example
- key_count: 0
  name: Tableau Rest Data Source Response Example
  slug: tableau-rest-data-source-response-example
- key_count: 1
  name: Tableau Rest Error Response Example
  slug: tableau-rest-error-response-example
- key_count: 1
  name: Tableau Rest Favorites Response Example
  slug: tableau-rest-favorites-response-example
- key_count: 6
  name: Tableau Rest Group Example
  slug: tableau-rest-group-example
- key_count: 1
  name: Tableau Rest Group List Response Example
  slug: tableau-rest-group-list-response-example
- key_count: 0
  name: Tableau Rest Group Response Example
  slug: tableau-rest-group-response-example
- key_count: 13
  name: Tableau Rest Job Example
  slug: tableau-rest-job-example
- key_count: 1
  name: Tableau Rest Job List Response Example
  slug: tableau-rest-job-list-response-example
- key_count: 0
  name: Tableau Rest Job Response Example
  slug: tableau-rest-job-response-example
- key_count: 3
  name: Tableau Rest Pagination Example
  slug: tableau-rest-pagination-example
- key_count: 1
  name: Tableau Rest Permission Example
  slug: tableau-rest-permission-example
- key_count: 1
  name: Tableau Rest Permission List Response Example
  slug: tableau-rest-permission-list-response-example
- key_count: 9
  name: Tableau Rest Project Example
  slug: tableau-rest-project-example
- key_count: 1
  name: Tableau Rest Project List Response Example
  slug: tableau-rest-project-list-response-example
- key_count: 0
  name: Tableau Rest Project Response Example
  slug: tableau-rest-project-response-example
- key_count: 1
  name: Tableau Rest Publish Workbook Request Example
  slug: tableau-rest-publish-workbook-request-example
- key_count: 6
  name: Tableau Rest Revision Example
  slug: tableau-rest-revision-example
- key_count: 1
  name: Tableau Rest Revision List Response Example
  slug: tableau-rest-revision-list-response-example
- key_count: 11
  name: Tableau Rest Schedule Example
  slug: tableau-rest-schedule-example
- key_count: 1
  name: Tableau Rest Schedule List Response Example
  slug: tableau-rest-schedule-list-response-example
- key_count: 1
  name: Tableau Rest Sign In Request Example
  slug: tableau-rest-sign-in-request-example
- key_count: 1
  name: Tableau Rest Sign In Response Example
  slug: tableau-rest-sign-in-response-example
- key_count: 13
  name: Tableau Rest Site Example
  slug: tableau-rest-site-example
- key_count: 1
  name: Tableau Rest Site List Response Example
  slug: tableau-rest-site-list-response-example
- key_count: 0
  name: Tableau Rest Site Response Example
  slug: tableau-rest-site-response-example
- key_count: 11
  name: Tableau Rest Subscription Example
  slug: tableau-rest-subscription-example
- key_count: 1
  name: Tableau Rest Subscription List Response Example
  slug: tableau-rest-subscription-list-response-example
- key_count: 0
  name: Tableau Rest Subscription Response Example
  slug: tableau-rest-subscription-response-example
- key_count: 1
  name: Tableau Rest Tag Example
  slug: tableau-rest-tag-example
- key_count: 1
  name: Tableau Rest Tag List Request Example
  slug: tableau-rest-tag-list-request-example
- key_count: 1
  name: Tableau Rest Tag List Response Example
  slug: tableau-rest-tag-list-response-example
- key_count: 1
  name: Tableau Rest Update Data Source Request Example
  slug: tableau-rest-update-data-source-request-example
- key_count: 1
  name: Tableau Rest Update Group Request Example
  slug: tableau-rest-update-group-request-example
- key_count: 1
  name: Tableau Rest Update Project Request Example
  slug: tableau-rest-update-project-request-example
- key_count: 1
  name: Tableau Rest Update Site Request Example
  slug: tableau-rest-update-site-request-example
- key_count: 1
  name: Tableau Rest Update Subscription Request Example
  slug: tableau-rest-update-subscription-request-example
- key_count: 1
  name: Tableau Rest Update User Request Example
  slug: tableau-rest-update-user-request-example
- key_count: 1
  name: Tableau Rest Update Workbook Request Example
  slug: tableau-rest-update-workbook-request-example
- key_count: 10
  name: Tableau Rest User Example
  slug: tableau-rest-user-example
- key_count: 1
  name: Tableau Rest User List Response Example
  slug: tableau-rest-user-list-response-example
- key_count: 0
  name: Tableau Rest User Response Example
  slug: tableau-rest-user-response-example
- key_count: 12
  name: Tableau Rest View Example
  slug: tableau-rest-view-example
- key_count: 1
  name: Tableau Rest View List Response Example
  slug: tableau-rest-view-list-response-example
- key_count: 0
  name: Tableau Rest View Response Example
  slug: tableau-rest-view-response-example
- key_count: 16
  name: Tableau Rest Workbook Example
  slug: tableau-rest-workbook-example
- key_count: 1
  name: Tableau Rest Workbook List Response Example
  slug: tableau-rest-workbook-list-response-example
- key_count: 0
  name: Tableau Rest Workbook Response Example
  slug: tableau-rest-workbook-response-example
- key_count: 6
  name: Tableau Signin Example
  slug: tableau-signin-example
- key_count: 6
  name: Tableau Switchsite Example
  slug: tableau-switchsite-example
- key_count: 6
  name: Tableau Updatedatasource Example
  slug: tableau-updatedatasource-example
- key_count: 6
  name: Tableau Updategroup Example
  slug: tableau-updategroup-example
- key_count: 6
  name: Tableau Updateproject Example
  slug: tableau-updateproject-example
- key_count: 6
  name: Tableau Updatesite Example
  slug: tableau-updatesite-example
- key_count: 6
  name: Tableau Updatesubscription Example
  slug: tableau-updatesubscription-example
- key_count: 6
  name: Tableau Updateuser Example
  slug: tableau-updateuser-example
- key_count: 6
  name: Tableau Updateworkbook Example
  slug: tableau-updateworkbook-example
features:
- description: Publish, query, update, delete, and download data sources that define connections to data shared across workbooks.
  name: Data Source Management
- description: Publish, query, update, delete, and download workbooks containing views, dashboards, and stories.
  name: Workbook Management
- description: Create, configure, and manage Tableau Server and Cloud sites with full lifecycle control.
  name: Site Administration
- description: Add, update, and remove users and groups with role-based access control for content permissions.
  name: User and Group Management
- description: Query and set granular permissions on workbooks, data sources, projects, views, and flows.
  name: Permission Management
- description: Create and manage schedules for extract refreshes and subscriptions for automated content delivery.
  name: Schedule and Subscription Management
- description: Embed Tableau visualizations in web applications with interactive filtering and full API control.
  name: Embedded Analytics
- description: Query metadata about content, data sources, and data lineage using the GraphQL-based Metadata API.
  name: Metadata and Lineage
- description: Build custom connectors using ODBC or JDBC drivers to bring any data source into Tableau.
  name: Custom Connectors
- description: Enable event-driven automation with HTTP POST notifications when events occur on Tableau Server or Cloud.
  name: Webhooks
finops:
- name: Tableau Finops
  service_category: Analytics & Business Intelligence
  slug: tableau-finops
graphqls:
- description: The Tableau Metadata API is a GraphQL-based API introduced in Tableau 2019.3 that enables querying of metadata about Tableau Server and Tableau Cloud content, data assets, and data lineage. It provide
  name: Tableau GraphQL API
  slug: tableau-graphql
image: https://www.tableau.com/sites/default/files/tableau_logo_800.png
integrations:
- description: Native integration with Salesforce CRM for unified analytics across sales, service, and marketing data.
  name: Salesforce
- description: Share Tableau visualizations and receive metric alerts directly in Slack channels.
  name: Slack
- description: Extend Tableau calculations with Python and R scripts through the Analytics Extensions API.
  name: Python and R
- description: Optimized connector for Snowflake data warehouse with live query and extract support.
  name: Snowflake
- description: Connect to Google BigQuery for large-scale data analytics and visualization.
  name: Google BigQuery
json_schemas:
- name: AddFavoriteRequest
  property_count: 1
  slug: tableau-addfavoriterequest
- name: AddPermissionsRequest
  property_count: 1
  slug: tableau-addpermissionsrequest
- name: AddUserRequest
  property_count: 1
  slug: tableau-adduserrequest
- name: Connection
  property_count: 6
  slug: tableau-connection
- name: ConnectionListResponse
  property_count: 1
  slug: tableau-connectionlistresponse
- name: CreateGroupRequest
  property_count: 1
  slug: tableau-creategrouprequest
- name: CreateProjectRequest
  property_count: 1
  slug: tableau-createprojectrequest
- name: CreateSiteRequest
  property_count: 1
  slug: tableau-createsiterequest
- name: CreateSubscriptionRequest
  property_count: 1
  slug: tableau-createsubscriptionrequest
- name: DataSource
  property_count: 15
  slug: tableau-datasource
- name: DataSourceListResponse
  property_count: 2
  slug: tableau-datasourcelistresponse
- name: DataSourceResponse
  property_count: 1
  slug: tableau-datasourceresponse
- name: ErrorResponse
  property_count: 1
  slug: tableau-errorresponse
- name: FavoritesResponse
  property_count: 1
  slug: tableau-favoritesresponse
- name: Group
  property_count: 6
  slug: tableau-group
- name: GroupListResponse
  property_count: 2
  slug: tableau-grouplistresponse
- name: GroupResponse
  property_count: 1
  slug: tableau-groupresponse
- name: Job
  property_count: 13
  slug: tableau-job
- name: JobListResponse
  property_count: 2
  slug: tableau-joblistresponse
- name: JobResponse
  property_count: 1
  slug: tableau-jobresponse
- name: Pagination
  property_count: 3
  slug: tableau-pagination
- name: Permission
  property_count: 1
  slug: tableau-permission
- name: PermissionListResponse
  property_count: 2
  slug: tableau-permissionlistresponse
- name: Project
  property_count: 9
  slug: tableau-project
- name: ProjectListResponse
  property_count: 2
  slug: tableau-projectlistresponse
- name: ProjectResponse
  property_count: 1
  slug: tableau-projectresponse
- name: PublishWorkbookRequest
  property_count: 1
  slug: tableau-publishworkbookrequest
- name: AddFavoriteRequest
  property_count: 1
  slug: tableau-rest-add-favorite-request
- name: AddPermissionsRequest
  property_count: 0
  slug: tableau-rest-add-permissions-request
- name: AddUserRequest
  property_count: 1
  slug: tableau-rest-add-user-request
- name: ConnectionListResponse
  property_count: 1
  slug: tableau-rest-connection-list-response
- name: Connection
  property_count: 6
  slug: tableau-rest-connection
- name: CreateGroupRequest
  property_count: 1
  slug: tableau-rest-create-group-request
- name: CreateProjectRequest
  property_count: 1
  slug: tableau-rest-create-project-request
- name: CreateSiteRequest
  property_count: 1
  slug: tableau-rest-create-site-request
- name: CreateSubscriptionRequest
  property_count: 1
  slug: tableau-rest-create-subscription-request
- name: DataSourceListResponse
  property_count: 1
  slug: tableau-rest-data-source-list-response
- name: DataSourceResponse
  property_count: 0
  slug: tableau-rest-data-source-response
- name: DataSource
  property_count: 15
  slug: tableau-rest-data-source
- name: ErrorResponse
  property_count: 1
  slug: tableau-rest-error-response
- name: FavoritesResponse
  property_count: 1
  slug: tableau-rest-favorites-response
- name: GroupListResponse
  property_count: 1
  slug: tableau-rest-group-list-response
- name: GroupResponse
  property_count: 0
  slug: tableau-rest-group-response
- name: Group
  property_count: 6
  slug: tableau-rest-group
- name: JobListResponse
  property_count: 1
  slug: tableau-rest-job-list-response
- name: JobResponse
  property_count: 0
  slug: tableau-rest-job-response
- name: Job
  property_count: 13
  slug: tableau-rest-job
- name: Pagination
  property_count: 3
  slug: tableau-rest-pagination
- name: PermissionListResponse
  property_count: 1
  slug: tableau-rest-permission-list-response
- name: Permission
  property_count: 1
  slug: tableau-rest-permission
- name: ProjectListResponse
  property_count: 1
  slug: tableau-rest-project-list-response
- name: ProjectResponse
  property_count: 0
  slug: tableau-rest-project-response
- name: Project
  property_count: 9
  slug: tableau-rest-project
- name: PublishWorkbookRequest
  property_count: 1
  slug: tableau-rest-publish-workbook-request
- name: RevisionListResponse
  property_count: 1
  slug: tableau-rest-revision-list-response
- name: Revision
  property_count: 6
  slug: tableau-rest-revision
- name: ScheduleListResponse
  property_count: 1
  slug: tableau-rest-schedule-list-response
- name: Schedule
  property_count: 11
  slug: tableau-rest-schedule
- name: SignInRequest
  property_count: 1
  slug: tableau-rest-sign-in-request
- name: SignInResponse
  property_count: 1
  slug: tableau-rest-sign-in-response
- name: SiteListResponse
  property_count: 1
  slug: tableau-rest-site-list-response
- name: SiteResponse
  property_count: 0
  slug: tableau-rest-site-response
- name: Site
  property_count: 13
  slug: tableau-rest-site
- name: SubscriptionListResponse
  property_count: 1
  slug: tableau-rest-subscription-list-response
- name: SubscriptionResponse
  property_count: 0
  slug: tableau-rest-subscription-response
- name: Subscription
  property_count: 11
  slug: tableau-rest-subscription
- name: TagListRequest
  property_count: 1
  slug: tableau-rest-tag-list-request
- name: TagListResponse
  property_count: 1
  slug: tableau-rest-tag-list-response
- name: Tag
  property_count: 1
  slug: tableau-rest-tag
- name: UpdateDataSourceRequest
  property_count: 1
  slug: tableau-rest-update-data-source-request
- name: UpdateGroupRequest
  property_count: 1
  slug: tableau-rest-update-group-request
- name: UpdateProjectRequest
  property_count: 1
  slug: tableau-rest-update-project-request
- name: UpdateSiteRequest
  property_count: 1
  slug: tableau-rest-update-site-request
- name: UpdateSubscriptionRequest
  property_count: 1
  slug: tableau-rest-update-subscription-request
- name: UpdateUserRequest
  property_count: 1
  slug: tableau-rest-update-user-request
- name: UpdateWorkbookRequest
  property_count: 1
  slug: tableau-rest-update-workbook-request
- name: UserListResponse
  property_count: 1
  slug: tableau-rest-user-list-response
- name: UserResponse
  property_count: 0
  slug: tableau-rest-user-response
- name: User
  property_count: 10
  slug: tableau-rest-user
- name: ViewListResponse
  property_count: 1
  slug: tableau-rest-view-list-response
- name: ViewResponse
  property_count: 0
  slug: tableau-rest-view-response
- name: View
  property_count: 12
  slug: tableau-rest-view
- name: WorkbookListResponse
  property_count: 1
  slug: tableau-rest-workbook-list-response
- name: WorkbookResponse
  property_count: 0
  slug: tableau-rest-workbook-response
- name: Workbook
  property_count: 16
  slug: tableau-rest-workbook
- name: Revision
  property_count: 6
  slug: tableau-revision
- name: RevisionListResponse
  property_count: 2
  slug: tableau-revisionlistresponse
- name: Schedule
  property_count: 11
  slug: tableau-schedule
- name: ScheduleListResponse
  property_count: 2
  slug: tableau-schedulelistresponse
- name: SignInRequest
  property_count: 1
  slug: tableau-signinrequest
- name: SignInResponse
  property_count: 1
  slug: tableau-signinresponse
- name: Site
  property_count: 13
  slug: tableau-site
- name: SiteListResponse
  property_count: 2
  slug: tableau-sitelistresponse
- name: SiteResponse
  property_count: 1
  slug: tableau-siteresponse
- name: Subscription
  property_count: 11
  slug: tableau-subscription
- name: SubscriptionListResponse
  property_count: 2
  slug: tableau-subscriptionlistresponse
- name: SubscriptionResponse
  property_count: 1
  slug: tableau-subscriptionresponse
- name: Tag
  property_count: 1
  slug: tableau-tag
- name: TagListRequest
  property_count: 1
  slug: tableau-taglistrequest
- name: TagListResponse
  property_count: 1
  slug: tableau-taglistresponse
- name: UpdateDataSourceRequest
  property_count: 1
  slug: tableau-updatedatasourcerequest
- name: UpdateGroupRequest
  property_count: 1
  slug: tableau-updategrouprequest
- name: UpdateProjectRequest
  property_count: 1
  slug: tableau-updateprojectrequest
- name: UpdateSiteRequest
  property_count: 1
  slug: tableau-updatesiterequest
- name: UpdateSubscriptionRequest
  property_count: 1
  slug: tableau-updatesubscriptionrequest
- name: UpdateUserRequest
  property_count: 1
  slug: tableau-updateuserrequest
- name: UpdateWorkbookRequest
  property_count: 1
  slug: tableau-updateworkbookrequest
- name: User
  property_count: 10
  slug: tableau-user
- name: UserListResponse
  property_count: 2
  slug: tableau-userlistresponse
- name: UserResponse
  property_count: 1
  slug: tableau-userresponse
- name: View
  property_count: 12
  slug: tableau-view
- name: ViewListResponse
  property_count: 2
  slug: tableau-viewlistresponse
- name: ViewResponse
  property_count: 1
  slug: tableau-viewresponse
- name: Tableau Workbook
  property_count: 18
  slug: tableau-workbook
- name: WorkbookListResponse
  property_count: 2
  slug: tableau-workbooklistresponse
- name: WorkbookResponse
  property_count: 1
  slug: tableau-workbookresponse
json_structures:
- name: Tableau Rest Add Favorite Request Structure
  property_count: 1
  slug: tableau-rest-add-favorite-request-structure
- name: Tableau Rest Add Permissions Request Structure
  property_count: 0
  slug: tableau-rest-add-permissions-request-structure
- name: Tableau Rest Add User Request Structure
  property_count: 1
  slug: tableau-rest-add-user-request-structure
- name: Tableau Rest Connection List Response Structure
  property_count: 1
  slug: tableau-rest-connection-list-response-structure
- name: Tableau Rest Connection Structure
  property_count: 6
  slug: tableau-rest-connection-structure
- name: Tableau Rest Create Group Request Structure
  property_count: 1
  slug: tableau-rest-create-group-request-structure
- name: Tableau Rest Create Project Request Structure
  property_count: 1
  slug: tableau-rest-create-project-request-structure
- name: Tableau Rest Create Site Request Structure
  property_count: 1
  slug: tableau-rest-create-site-request-structure
- name: Tableau Rest Create Subscription Request Structure
  property_count: 1
  slug: tableau-rest-create-subscription-request-structure
- name: Tableau Rest Data Source List Response Structure
  property_count: 1
  slug: tableau-rest-data-source-list-response-structure
- name: Tableau Rest Data Source Response Structure
  property_count: 0
  slug: tableau-rest-data-source-response-structure
- name: Tableau Rest Data Source Structure
  property_count: 15
  slug: tableau-rest-data-source-structure
- name: Tableau Rest Error Response Structure
  property_count: 1
  slug: tableau-rest-error-response-structure
- name: Tableau Rest Favorites Response Structure
  property_count: 1
  slug: tableau-rest-favorites-response-structure
- name: Tableau Rest Group List Response Structure
  property_count: 1
  slug: tableau-rest-group-list-response-structure
- name: Tableau Rest Group Response Structure
  property_count: 0
  slug: tableau-rest-group-response-structure
- name: Tableau Rest Group Structure
  property_count: 6
  slug: tableau-rest-group-structure
- name: Tableau Rest Job List Response Structure
  property_count: 1
  slug: tableau-rest-job-list-response-structure
- name: Tableau Rest Job Response Structure
  property_count: 0
  slug: tableau-rest-job-response-structure
- name: Tableau Rest Job Structure
  property_count: 13
  slug: tableau-rest-job-structure
- name: Tableau Rest Pagination Structure
  property_count: 3
  slug: tableau-rest-pagination-structure
- name: Tableau Rest Permission List Response Structure
  property_count: 1
  slug: tableau-rest-permission-list-response-structure
- name: Tableau Rest Permission Structure
  property_count: 1
  slug: tableau-rest-permission-structure
- name: Tableau Rest Project List Response Structure
  property_count: 1
  slug: tableau-rest-project-list-response-structure
- name: Tableau Rest Project Response Structure
  property_count: 0
  slug: tableau-rest-project-response-structure
- name: Tableau Rest Project Structure
  property_count: 9
  slug: tableau-rest-project-structure
- name: Tableau Rest Publish Workbook Request Structure
  property_count: 1
  slug: tableau-rest-publish-workbook-request-structure
- name: Tableau Rest Revision List Response Structure
  property_count: 1
  slug: tableau-rest-revision-list-response-structure
- name: Tableau Rest Revision Structure
  property_count: 6
  slug: tableau-rest-revision-structure
- name: Tableau Rest Schedule List Response Structure
  property_count: 1
  slug: tableau-rest-schedule-list-response-structure
- name: Tableau Rest Schedule Structure
  property_count: 11
  slug: tableau-rest-schedule-structure
- name: Tableau Rest Sign In Request Structure
  property_count: 1
  slug: tableau-rest-sign-in-request-structure
- name: Tableau Rest Sign In Response Structure
  property_count: 1
  slug: tableau-rest-sign-in-response-structure
- name: Tableau Rest Site List Response Structure
  property_count: 1
  slug: tableau-rest-site-list-response-structure
- name: Tableau Rest Site Response Structure
  property_count: 0
  slug: tableau-rest-site-response-structure
- name: Tableau Rest Site Structure
  property_count: 13
  slug: tableau-rest-site-structure
- name: Tableau Rest Subscription List Response Structure
  property_count: 1
  slug: tableau-rest-subscription-list-response-structure
- name: Tableau Rest Subscription Response Structure
  property_count: 0
  slug: tableau-rest-subscription-response-structure
- name: Tableau Rest Subscription Structure
  property_count: 11
  slug: tableau-rest-subscription-structure
- name: Tableau Rest Tag List Request Structure
  property_count: 1
  slug: tableau-rest-tag-list-request-structure
- name: Tableau Rest Tag List Response Structure
  property_count: 1
  slug: tableau-rest-tag-list-response-structure
- name: Tableau Rest Tag Structure
  property_count: 1
  slug: tableau-rest-tag-structure
- name: Tableau Rest Update Data Source Request Structure
  property_count: 1
  slug: tableau-rest-update-data-source-request-structure
- name: Tableau Rest Update Group Request Structure
  property_count: 1
  slug: tableau-rest-update-group-request-structure
- name: Tableau Rest Update Project Request Structure
  property_count: 1
  slug: tableau-rest-update-project-request-structure
- name: Tableau Rest Update Site Request Structure
  property_count: 1
  slug: tableau-rest-update-site-request-structure
- name: Tableau Rest Update Subscription Request Structure
  property_count: 1
  slug: tableau-rest-update-subscription-request-structure
- name: Tableau Rest Update User Request Structure
  property_count: 1
  slug: tableau-rest-update-user-request-structure
- name: Tableau Rest Update Workbook Request Structure
  property_count: 1
  slug: tableau-rest-update-workbook-request-structure
- name: Tableau Rest User List Response Structure
  property_count: 1
  slug: tableau-rest-user-list-response-structure
- name: Tableau Rest User Response Structure
  property_count: 0
  slug: tableau-rest-user-response-structure
- name: Tableau Rest User Structure
  property_count: 10
  slug: tableau-rest-user-structure
- name: Tableau Rest View List Response Structure
  property_count: 1
  slug: tableau-rest-view-list-response-structure
- name: Tableau Rest View Response Structure
  property_count: 0
  slug: tableau-rest-view-response-structure
- name: Tableau Rest View Structure
  property_count: 12
  slug: tableau-rest-view-structure
- name: Tableau Rest Workbook List Response Structure
  property_count: 1
  slug: tableau-rest-workbook-list-response-structure
- name: Tableau Rest Workbook Response Structure
  property_count: 0
  slug: tableau-rest-workbook-response-structure
- name: Tableau Rest Workbook Structure
  property_count: 16
  slug: tableau-rest-workbook-structure
- name: Tableau Structure
  property_count: 0
  slug: tableau-structure
jsonld:
- class_count: 0
  name: Tableau Context
  property_count: 14
  slug: tableau-context
- class_count: 0
  name: Tableau Rest Context
  property_count: 0
  slug: tableau-rest-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Tableau
nav: Providers
network: true
overview: 'Tableau publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Data Sources API, Favorites API, and 10 more. Tagged areas include Analytics, Business Intelligence, Dashboards, and Data Visualization.


  The Tableau catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Tableau''s developer surface includes authentication, engineering blog, support, release notes, signup flow, documentation, Stack Overflow tag, and 14 more developer resources.'
plans:
- name: Tableau Plans Pricing
  plan_count: 4
  slug: tableau-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 6
  name: Tableau Rate Limits
  slug: tableau-rate-limits
rules:
- name: Tableau API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: tableau-jsonschema-spectral-rules
- name: Tableau API Rules
  rule_count: 15
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 6
  slug: tableau-spectral-rules
score:
  band: strong
  composite: 57.2
  delta: -8.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 74.1
    developer_ergonomics: 47.8
    discoverability: 63.0
    governance: 58.3
    operational_transparency: 44.7
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tableau/refs/heads/main/screenshots/tableau-2026-06-20T194845.png
security:
- kind: authentication
  name: Tableau Authentication
  slug: tableau-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tableau Domain Security
  slug: tableau-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tableau
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Visualization
use_cases:
- description: Automate the creation and distribution of business reports and dashboards across organizations.
  name: Enterprise Reporting
- description: Embed interactive visualizations and analytics directly into customer-facing applications.
  name: Embedded Analytics
- description: Track data lineage, manage permissions, and enforce data policies across the analytics platform.
  name: Data Governance
- description: Enable business users to explore data and create visualizations without IT involvement.
  name: Self-Service Analytics
- description: Programmatically migrate workbooks, data sources, and configurations between Tableau environments.
  name: Content Migration
website: https://www.tableau.com/developer
---
