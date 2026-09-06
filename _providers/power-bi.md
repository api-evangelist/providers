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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.2
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Power Bi Agentic Access
  operation_count: 36
  slug: power-bi-agentic-access
  summary_line: 36 operations · 14 acting
api_count: 1
apis:
- description: Azure service that enables ISVs and developers to embed Power BI visuals, reports, and dashboards into their applications.
  name: Power BI Embedded
  slug: power-bi-embedded
- description: API for managing Power BI capacity, workspaces, and tenant settings.
  name: Power BI Management API
  slug: power-bi-management-api
- description: The Push Datasets API enables real-time data streaming by allowing applications to create push datasets and post rows of data directly into Power BI datasets.
  name: Power BI Push Datasets API
  slug: power-bi-push-datasets-api
- description: The Power BI Report Server REST API provides programmatic access to report server catalog objects such as folders, reports, KPIs, data sources, datasets, refresh plans, and subscriptions.
  name: Power BI Report Server REST API
  slug: power-bi-report-server-rest-api
- description: The Power BI Visuals API enables developers to create custom visuals that can be used in Power BI reports and dashboards, extending the built-in visualization capabilities.
  name: Power BI Visuals API
  slug: power-bi-visuals-api
- baseURL: https://api.powerbi.com
  baseurl_source: declared
  description: Manage dashboards including listing, creating, and retrieving tiles. Dashboards are single-page canvases with pinned visualizations.
  name: Power BI Dashboards API
  slug: power-bi-dashboards-api
- baseURL: https://api.powerbi.com
  baseurl_source: declared
  description: Manage datasets including creating, updating, refreshing, and deleting datasets. Datasets represent the data model behind Power BI reports.
  name: Power BI Datasets API
  slug: power-bi-datasets-api
- baseURL: https://api.powerbi.com
  baseurl_source: declared
  description: Manage on-premises data gateways and their data sources for connecting to on-premises data.
  name: Power BI Gateways API
  slug: power-bi-gateways-api
- baseURL: https://api.powerbi.com
  baseurl_source: declared
  description: Manage workspaces (groups) including listing, creating, deleting, and managing workspace users. Workspaces are containers for dashboards, reports, datasets, and dataflows.
  name: Power BI Groups API
  slug: power-bi-groups-api
- baseURL: https://api.powerbi.com
  baseurl_source: declared
  description: Import Power BI content such as PBIX files, Excel workbooks, and RDL reports into workspaces.
  name: Power BI Imports API
  slug: power-bi-imports-api
- baseURL: https://api.powerbi.com
  baseurl_source: declared
  description: Manage reports including listing, cloning, exporting, rebinding, and deleting reports. Reports are visual presentations of data from datasets.
  name: Power BI Reports API
  slug: power-bi-reports-api
arazzos:
- description: Walk from the dashboard list down to a single tile and capture the embed URL, report, and dataset it needs.
  name: Power BI Resolve a Dashboard Tile for Embedding
  slug: power-bi-dashboard-tile-embed-workflow
- description: Confirm a dataset, find the reports bound to it, delete the dependent report, and then delete the dataset.
  name: Power BI Decommission a Dataset After Clearing Dependents
  slug: power-bi-dataset-decommission-workflow
- description: Kick off an on-demand dataset refresh and poll the refresh history until it reaches a terminal state.
  name: Power BI Trigger a Dataset Refresh and Poll to Completion
  slug: power-bi-dataset-refresh-poll-workflow
- description: Walk the gateway inventory and cross-reference a dataset's datasources to prove which gateway backs it.
  name: Power BI Audit Gateway-Bound Datasources
  slug: power-bi-gateway-datasource-audit-workflow
- description: Read a dataset's mashup parameters, update them, confirm the new values, and refresh so the change takes effect.
  name: Power BI Update Dataset Parameters and Refresh
  slug: power-bi-parameter-update-refresh-workflow
- description: Upload a PBIX file into a workspace, wait for the import to finish publishing, and list the resulting reports and datasets.
  name: Power BI Import a PBIX and Poll Until Published
  slug: power-bi-pbix-import-publish-workflow
- description: Provision a push-mode dataset with an inline table schema and read it back to confirm the row API is enabled.
  name: Power BI Create a Push Dataset and Verify Its Schema
  slug: power-bi-push-dataset-provision-workflow
- description: Copy a report into a target workspace and repoint the copy at a different dataset, then verify the binding.
  name: Power BI Clone a Report and Rebind It to Another Dataset
  slug: power-bi-report-clone-rebind-workflow
- description: Capture a report's metadata and page structure, then download the underlying PBIX file.
  name: Power BI Export a Report for Archive
  slug: power-bi-report-export-archive-workflow
- description: List a workspace's members, downgrade an over-privileged principal, remove a departed one, and confirm the final membership.
  name: Power BI Review and Adjust Workspace Access
  slug: power-bi-workspace-access-review-workflow
- description: Find a workspace by OData filter and enumerate every dataset, report, dashboard, and import it contains.
  name: Power BI Inventory a Workspace's Content
  slug: power-bi-workspace-content-inventory-workflow
- description: Create a workspace, add a principal with a specific access right, and verify the resulting membership.
  name: Power BI Provision a Workspace and Grant Access
  slug: power-bi-workspace-provision-access-workflow
artifact_total: 261
collections:
- collection_type: postman
  name: Power BI REST Dashboards API
  slug: postman-power-bi-dashboards-api
- collection_type: postman
  name: Power BI REST Dashboards Datasets API
  slug: postman-power-bi-datasets-api
- collection_type: postman
  name: Power BI REST Dashboards Gateways API
  slug: postman-power-bi-gateways-api
- collection_type: postman
  name: Power BI REST Dashboards Groups API
  slug: postman-power-bi-groups-api
- collection_type: postman
  name: Power BI REST Dashboards Imports API
  slug: postman-power-bi-imports-api
- collection_type: postman
  name: Power BI REST Dashboards Reports API
  slug: postman-power-bi-reports-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Power BI REST Dashboards API
  slug: open-power-bi-dashboards-api
- collection_type: open
  name: Power BI REST Dashboards Datasets API
  slug: open-power-bi-datasets-api
- collection_type: open
  name: Power BI REST Dashboards Gateways API
  slug: open-power-bi-gateways-api
- collection_type: open
  name: Power BI REST Dashboards Groups API
  slug: open-power-bi-groups-api
- collection_type: open
  name: Power BI REST Dashboards Imports API
  slug: open-power-bi-imports-api
- collection_type: open
  name: Power BI REST Dashboards Reports API
  slug: open-power-bi-reports-api
- collection_type: open
  name: Power BI REST API
  slug: open-power-bi-rest-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/power-bi-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Microsoft/PowerBI-JavaScript/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Microsoft/PowerBI-JavaScript/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/microsoft/PowerBI-JavaScript/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/microsoft/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/microsoft/PowerBI-JavaScript/blob/master/CONTRIBUTING.md
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/power-bi/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/power-bi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/power-bi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/power-bi-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/power-bi-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/power-bi-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/power-bi-security.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/power-bi-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/power-bi-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/power-bi-rest-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/power-bi-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/power-bi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/power-bi-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/power-bi-scopes.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/power-bi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/power-bi-trust-center.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/power-bi-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/power-bi-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/power-bi-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/power-bi-cli.yml
- group: design
  title: ''
  type: Components
  url: components/power-bi-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/power-bi-data-model.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://community.fabric.microsoft.com/t5/Power-BI-Updates-Blog/AI-Powered-Power-BI-reporting-From-design-to-deployment-with/ba-p/5190703
- group: start
  title: ''
  type: Portal
  url: https://app.powerbi.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://powerbi.microsoft.com/en-us/developers/
- group: company
  title: ''
  type: Blog
  url: https://powerbi.microsoft.com/en-us/blog/
- group: operate
  title: ''
  type: Support
  url: https://powerbi.microsoft.com/en-us/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://powerbi.microsoft.com/en-us/status/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://powerbi.microsoft.com/en-us/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Microsoft/PowerBI-JavaScript
- group: build
  title: Developer Samples
  type: GitHubRepository
  url: https://github.com/microsoft/PowerBI-Developer-Samples
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-power-bi/
- group: other
  title: ''
  type: X
  url: https://twitter.com/MSPowerBI
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/mspowerbi
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/power-bi/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.powerbi.com/signupredirect?pbi_source=web
- group: start
  title: ''
  type: Login
  url: https://app.powerbi.com/signin
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/power-bi/fundamentals/whats-new
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/powerbi
- group: design
  title: ''
  type: JSONLD
  url: json-ld/power-bi-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/power-bi-dataset-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/power-bi-report-schema.json
- group: build
  title: .NET SDK
  type: SDKs
  url: https://github.com/microsoft/PowerBI-CSharp
- group: design
  title: ''
  type: Arazzo
  url: arazzo/power-bi-dataset-refresh-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/power-bi-push-dataset-provision-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/power-bi-parameter-update-refresh-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/power-bi-report-clone-rebind-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/power-bi-workspace-provision-access-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/power-bi-pbix-import-publish-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/power-bi-workspace-content-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/power-bi-gateway-datasource-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/power-bi-dashboard-tile-embed-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/power-bi-report-export-archive-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/power-bi-dataset-decommission-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/power-bi-workspace-access-review-workflow.yml
created: '2024'
description: Microsoft Power BI is a business analytics service that delivers insights to enable fast, informed decisions. It provides interactive visualizations and business intelligence capabilities with an interface simple enough for end users to create their own reports and dashboards.
examples:
- key_count: 6
  name: Power Bi Addgroupuser Example
  slug: power-bi-addgroupuser-example
- key_count: 6
  name: Power Bi Clonereport Example
  slug: power-bi-clonereport-example
- key_count: 6
  name: Power Bi Createdashboard Example
  slug: power-bi-createdashboard-example
- key_count: 6
  name: Power Bi Createdataset Example
  slug: power-bi-createdataset-example
- key_count: 6
  name: Power Bi Creategroup Example
  slug: power-bi-creategroup-example
- key_count: 6
  name: Power Bi Createimportingroup Example
  slug: power-bi-createimportingroup-example
- key_count: 6
  name: Power Bi Deletedataset Example
  slug: power-bi-deletedataset-example
- key_count: 6
  name: Power Bi Deletegroup Example
  slug: power-bi-deletegroup-example
- key_count: 6
  name: Power Bi Deletegroupuser Example
  slug: power-bi-deletegroupuser-example
- key_count: 6
  name: Power Bi Deletereport Example
  slug: power-bi-deletereport-example
- key_count: 6
  name: Power Bi Exportreport Example
  slug: power-bi-exportreport-example
- key_count: 6
  name: Power Bi Getdashboard Example
  slug: power-bi-getdashboard-example
- key_count: 6
  name: Power Bi Getdashboards Example
  slug: power-bi-getdashboards-example
- key_count: 6
  name: Power Bi Getdashboardsingroup Example
  slug: power-bi-getdashboardsingroup-example
- key_count: 6
  name: Power Bi Getdataset Example
  slug: power-bi-getdataset-example
- key_count: 6
  name: Power Bi Getdatasets Example
  slug: power-bi-getdatasets-example
- key_count: 6
  name: Power Bi Getdatasetsingroup Example
  slug: power-bi-getdatasetsingroup-example
- key_count: 6
  name: Power Bi Getdatasources Example
  slug: power-bi-getdatasources-example
- key_count: 6
  name: Power Bi Getgateway Example
  slug: power-bi-getgateway-example
- key_count: 6
  name: Power Bi Getgatewaydatasources Example
  slug: power-bi-getgatewaydatasources-example
- key_count: 6
  name: Power Bi Getgateways Example
  slug: power-bi-getgateways-example
- key_count: 6
  name: Power Bi Getgroups Example
  slug: power-bi-getgroups-example
- key_count: 6
  name: Power Bi Getgroupusers Example
  slug: power-bi-getgroupusers-example
- key_count: 6
  name: Power Bi Getimportsingroup Example
  slug: power-bi-getimportsingroup-example
- key_count: 6
  name: Power Bi Getpages Example
  slug: power-bi-getpages-example
- key_count: 6
  name: Power Bi Getparameters Example
  slug: power-bi-getparameters-example
- key_count: 6
  name: Power Bi Getrefreshhistory Example
  slug: power-bi-getrefreshhistory-example
- key_count: 6
  name: Power Bi Getreport Example
  slug: power-bi-getreport-example
- key_count: 6
  name: Power Bi Getreports Example
  slug: power-bi-getreports-example
- key_count: 6
  name: Power Bi Getreportsingroup Example
  slug: power-bi-getreportsingroup-example
- key_count: 6
  name: Power Bi Gettile Example
  slug: power-bi-gettile-example
- key_count: 6
  name: Power Bi Gettiles Example
  slug: power-bi-gettiles-example
- key_count: 6
  name: Power Bi Rebindreport Example
  slug: power-bi-rebindreport-example
- key_count: 6
  name: Power Bi Refreshdataset Example
  slug: power-bi-refreshdataset-example
- key_count: 3
  name: Power Bi Rest Clone Report Request Example
  slug: power-bi-rest-clone-report-request-example
- key_count: 5
  name: Power Bi Rest Column Example
  slug: power-bi-rest-column-example
- key_count: 1
  name: Power Bi Rest Create Dashboard Request Example
  slug: power-bi-rest-create-dashboard-request-example
- key_count: 4
  name: Power Bi Rest Create Dataset Request Example
  slug: power-bi-rest-create-dataset-request-example
- key_count: 1
  name: Power Bi Rest Create Group Request Example
  slug: power-bi-rest-create-group-request-example
- key_count: 6
  name: Power Bi Rest Dashboard Example
  slug: power-bi-rest-dashboard-example
- key_count: 2
  name: Power Bi Rest Dashboard List Example
  slug: power-bi-rest-dashboard-list-example
- key_count: 14
  name: Power Bi Rest Dataset Example
  slug: power-bi-rest-dataset-example
- key_count: 2
  name: Power Bi Rest Dataset List Example
  slug: power-bi-rest-dataset-list-example
- key_count: 4
  name: Power Bi Rest Datasource Example
  slug: power-bi-rest-datasource-example
- key_count: 2
  name: Power Bi Rest Datasource List Example
  slug: power-bi-rest-datasource-list-example
- key_count: 1
  name: Power Bi Rest Error Response Example
  slug: power-bi-rest-error-response-example
- key_count: 6
  name: Power Bi Rest Gateway Datasource Example
  slug: power-bi-rest-gateway-datasource-example
- key_count: 2
  name: Power Bi Rest Gateway Datasource List Example
  slug: power-bi-rest-gateway-datasource-list-example
- key_count: 5
  name: Power Bi Rest Gateway Example
  slug: power-bi-rest-gateway-example
- key_count: 2
  name: Power Bi Rest Gateway List Example
  slug: power-bi-rest-gateway-list-example
- key_count: 7
  name: Power Bi Rest Group Example
  slug: power-bi-rest-group-example
- key_count: 2
  name: Power Bi Rest Group List Example
  slug: power-bi-rest-group-list-example
- key_count: 6
  name: Power Bi Rest Group User Example
  slug: power-bi-rest-group-user-example
- key_count: 2
  name: Power Bi Rest Group User List Example
  slug: power-bi-rest-group-user-list-example
- key_count: 7
  name: Power Bi Rest Import Example
  slug: power-bi-rest-import-example
- key_count: 2
  name: Power Bi Rest Import List Example
  slug: power-bi-rest-import-list-example
- key_count: 4
  name: Power Bi Rest Measure Example
  slug: power-bi-rest-measure-example
- key_count: 3
  name: Power Bi Rest Page Example
  slug: power-bi-rest-page-example
- key_count: 2
  name: Power Bi Rest Page List Example
  slug: power-bi-rest-page-list-example
- key_count: 5
  name: Power Bi Rest Parameter Example
  slug: power-bi-rest-parameter-example
- key_count: 2
  name: Power Bi Rest Parameter List Example
  slug: power-bi-rest-parameter-list-example
- key_count: 1
  name: Power Bi Rest Rebind Report Request Example
  slug: power-bi-rest-rebind-report-request-example
- key_count: 7
  name: Power Bi Rest Refresh Example
  slug: power-bi-rest-refresh-example
- key_count: 2
  name: Power Bi Rest Refresh List Example
  slug: power-bi-rest-refresh-list-example
- key_count: 5
  name: Power Bi Rest Refresh Request Example
  slug: power-bi-rest-refresh-request-example
- key_count: 6
  name: Power Bi Rest Relationship Example
  slug: power-bi-rest-relationship-example
- key_count: 10
  name: Power Bi Rest Report Example
  slug: power-bi-rest-report-example
- key_count: 2
  name: Power Bi Rest Report List Example
  slug: power-bi-rest-report-list-example
- key_count: 4
  name: Power Bi Rest Table Example
  slug: power-bi-rest-table-example
- key_count: 9
  name: Power Bi Rest Tile Example
  slug: power-bi-rest-tile-example
- key_count: 2
  name: Power Bi Rest Tile List Example
  slug: power-bi-rest-tile-list-example
- key_count: 1
  name: Power Bi Rest Update Parameters Request Example
  slug: power-bi-rest-update-parameters-request-example
- key_count: 6
  name: Power Bi Updategroupuser Example
  slug: power-bi-updategroupuser-example
- key_count: 6
  name: Power Bi Updateparameters Example
  slug: power-bi-updateparameters-example
features:
- description: Create and share interactive dashboards with real-time data visualizations and drill-down capabilities.
  name: Interactive Dashboards
- description: Ask questions about your data in plain English and get instant visualizations with Q&A.
  name: Natural Language Queries
- description: Connect to hundreds of data sources including databases, cloud services, files, and streaming data.
  name: Data Connectivity
- description: Embed Power BI reports and dashboards into custom applications using REST APIs and JavaScript SDK.
  name: Embedded Analytics
- description: Create pixel-perfect, print-ready reports designed for printing or PDF generation.
  name: Paginated Reports
- description: Push real-time data to dashboards with streaming datasets and live tile updates.
  name: Real-Time Streaming
- description: Control data access at the row level based on user identity and roles.
  name: Row-Level Security
- description: Self-service data preparation with Power Query Online for creating reusable data transformation logic.
  name: Dataflows
finops:
- name: Power Bi Finops
  service_category: Analytics
  slug: power-bi-finops
image: https://powerbi.microsoft.com/pictures/shared/social/social-default-image.png
integrations:
- description: View and interact with Power BI reports directly within Microsoft Teams channels and chats.
  name: Microsoft Teams
- description: Analyze Power BI datasets in Excel with connected tables and PivotTables.
  name: Excel
- description: Embed Power BI reports in SharePoint Online pages for enterprise-wide distribution.
  name: SharePoint
- description: Connect to Azure Synapse workspaces for big data analytics and data warehousing.
  name: Azure Synapse Analytics
- description: Pre-built analytics templates and data connectors for Dynamics 365 business applications.
  name: Dynamics 365
- description: Trigger automated workflows based on Power BI data alerts and refresh events.
  name: Power Automate
- description: Enterprise authentication and authorization with Azure AD for secure API access.
  name: Azure Active Directory
- description: Connect to Salesforce data with native connectors for CRM analytics and reporting.
  name: Salesforce
json_schemas:
- name: CloneReportRequest
  property_count: 3
  slug: power-bi-clonereportrequest
- name: Column
  property_count: 5
  slug: power-bi-column
- name: CreateDashboardRequest
  property_count: 1
  slug: power-bi-createdashboardrequest
- name: CreateDatasetRequest
  property_count: 4
  slug: power-bi-createdatasetrequest
- name: CreateGroupRequest
  property_count: 1
  slug: power-bi-creategrouprequest
- name: Dashboard
  property_count: 6
  slug: power-bi-dashboard
- name: DashboardList
  property_count: 2
  slug: power-bi-dashboardlist
- name: Power BI Dataset
  property_count: 18
  slug: power-bi-dataset
- name: DatasetList
  property_count: 2
  slug: power-bi-datasetlist
- name: Datasource
  property_count: 4
  slug: power-bi-datasource
- name: DatasourceList
  property_count: 2
  slug: power-bi-datasourcelist
- name: ErrorResponse
  property_count: 1
  slug: power-bi-errorresponse
- name: Gateway
  property_count: 5
  slug: power-bi-gateway
- name: GatewayDatasource
  property_count: 6
  slug: power-bi-gatewaydatasource
- name: GatewayDatasourceList
  property_count: 2
  slug: power-bi-gatewaydatasourcelist
- name: GatewayList
  property_count: 2
  slug: power-bi-gatewaylist
- name: Group
  property_count: 7
  slug: power-bi-group
- name: GroupList
  property_count: 2
  slug: power-bi-grouplist
- name: GroupUser
  property_count: 6
  slug: power-bi-groupuser
- name: GroupUserList
  property_count: 2
  slug: power-bi-groupuserlist
- name: Import
  property_count: 7
  slug: power-bi-import
- name: ImportList
  property_count: 2
  slug: power-bi-importlist
- name: Measure
  property_count: 4
  slug: power-bi-measure
- name: Page
  property_count: 3
  slug: power-bi-page
- name: PageList
  property_count: 2
  slug: power-bi-pagelist
- name: Parameter
  property_count: 5
  slug: power-bi-parameter
- name: ParameterList
  property_count: 2
  slug: power-bi-parameterlist
- name: RebindReportRequest
  property_count: 1
  slug: power-bi-rebindreportrequest
- name: Refresh
  property_count: 7
  slug: power-bi-refresh
- name: RefreshList
  property_count: 2
  slug: power-bi-refreshlist
- name: RefreshRequest
  property_count: 5
  slug: power-bi-refreshrequest
- name: Relationship
  property_count: 6
  slug: power-bi-relationship
- name: Power BI Report
  property_count: 17
  slug: power-bi-report
- name: ReportList
  property_count: 2
  slug: power-bi-reportlist
- name: CloneReportRequest
  property_count: 3
  slug: power-bi-rest-clone-report-request
- name: Column
  property_count: 5
  slug: power-bi-rest-column
- name: CreateDashboardRequest
  property_count: 1
  slug: power-bi-rest-create-dashboard-request
- name: CreateDatasetRequest
  property_count: 4
  slug: power-bi-rest-create-dataset-request
- name: CreateGroupRequest
  property_count: 1
  slug: power-bi-rest-create-group-request
- name: DashboardList
  property_count: 2
  slug: power-bi-rest-dashboard-list
- name: Dashboard
  property_count: 6
  slug: power-bi-rest-dashboard
- name: DatasetList
  property_count: 2
  slug: power-bi-rest-dataset-list
- name: Dataset
  property_count: 14
  slug: power-bi-rest-dataset
- name: DatasourceList
  property_count: 2
  slug: power-bi-rest-datasource-list
- name: Datasource
  property_count: 4
  slug: power-bi-rest-datasource
- name: ErrorResponse
  property_count: 1
  slug: power-bi-rest-error-response
- name: GatewayDatasourceList
  property_count: 2
  slug: power-bi-rest-gateway-datasource-list
- name: GatewayDatasource
  property_count: 6
  slug: power-bi-rest-gateway-datasource
- name: GatewayList
  property_count: 2
  slug: power-bi-rest-gateway-list
- name: Gateway
  property_count: 5
  slug: power-bi-rest-gateway
- name: GroupList
  property_count: 2
  slug: power-bi-rest-group-list
- name: Group
  property_count: 7
  slug: power-bi-rest-group
- name: GroupUserList
  property_count: 2
  slug: power-bi-rest-group-user-list
- name: GroupUser
  property_count: 6
  slug: power-bi-rest-group-user
- name: ImportList
  property_count: 2
  slug: power-bi-rest-import-list
- name: Import
  property_count: 7
  slug: power-bi-rest-import
- name: Measure
  property_count: 4
  slug: power-bi-rest-measure
- name: PageList
  property_count: 2
  slug: power-bi-rest-page-list
- name: Page
  property_count: 3
  slug: power-bi-rest-page
- name: ParameterList
  property_count: 2
  slug: power-bi-rest-parameter-list
- name: Parameter
  property_count: 5
  slug: power-bi-rest-parameter
- name: RebindReportRequest
  property_count: 1
  slug: power-bi-rest-rebind-report-request
- name: RefreshList
  property_count: 2
  slug: power-bi-rest-refresh-list
- name: RefreshRequest
  property_count: 5
  slug: power-bi-rest-refresh-request
- name: Refresh
  property_count: 7
  slug: power-bi-rest-refresh
- name: Relationship
  property_count: 6
  slug: power-bi-rest-relationship
- name: ReportList
  property_count: 2
  slug: power-bi-rest-report-list
- name: Report
  property_count: 10
  slug: power-bi-rest-report
- name: Table
  property_count: 4
  slug: power-bi-rest-table
- name: TileList
  property_count: 2
  slug: power-bi-rest-tile-list
- name: Tile
  property_count: 9
  slug: power-bi-rest-tile
- name: UpdateParametersRequest
  property_count: 1
  slug: power-bi-rest-update-parameters-request
- name: Table
  property_count: 4
  slug: power-bi-table
- name: Tile
  property_count: 9
  slug: power-bi-tile
- name: TileList
  property_count: 2
  slug: power-bi-tilelist
- name: UpdateParametersRequest
  property_count: 1
  slug: power-bi-updateparametersrequest
json_structures:
- name: Power Bi Rest Clone Report Request Structure
  property_count: 3
  slug: power-bi-rest-clone-report-request-structure
- name: Power Bi Rest Column Structure
  property_count: 5
  slug: power-bi-rest-column-structure
- name: Power Bi Rest Create Dashboard Request Structure
  property_count: 1
  slug: power-bi-rest-create-dashboard-request-structure
- name: Power Bi Rest Create Dataset Request Structure
  property_count: 4
  slug: power-bi-rest-create-dataset-request-structure
- name: Power Bi Rest Create Group Request Structure
  property_count: 1
  slug: power-bi-rest-create-group-request-structure
- name: Power Bi Rest Dashboard List Structure
  property_count: 2
  slug: power-bi-rest-dashboard-list-structure
- name: Power Bi Rest Dashboard Structure
  property_count: 6
  slug: power-bi-rest-dashboard-structure
- name: Power Bi Rest Dataset List Structure
  property_count: 2
  slug: power-bi-rest-dataset-list-structure
- name: Power Bi Rest Dataset Structure
  property_count: 14
  slug: power-bi-rest-dataset-structure
- name: Power Bi Rest Datasource List Structure
  property_count: 2
  slug: power-bi-rest-datasource-list-structure
- name: Power Bi Rest Datasource Structure
  property_count: 4
  slug: power-bi-rest-datasource-structure
- name: Power Bi Rest Error Response Structure
  property_count: 1
  slug: power-bi-rest-error-response-structure
- name: Power Bi Rest Gateway Datasource List Structure
  property_count: 2
  slug: power-bi-rest-gateway-datasource-list-structure
- name: Power Bi Rest Gateway Datasource Structure
  property_count: 6
  slug: power-bi-rest-gateway-datasource-structure
- name: Power Bi Rest Gateway List Structure
  property_count: 2
  slug: power-bi-rest-gateway-list-structure
- name: Power Bi Rest Gateway Structure
  property_count: 5
  slug: power-bi-rest-gateway-structure
- name: Power Bi Rest Group List Structure
  property_count: 2
  slug: power-bi-rest-group-list-structure
- name: Power Bi Rest Group Structure
  property_count: 7
  slug: power-bi-rest-group-structure
- name: Power Bi Rest Group User List Structure
  property_count: 2
  slug: power-bi-rest-group-user-list-structure
- name: Power Bi Rest Group User Structure
  property_count: 6
  slug: power-bi-rest-group-user-structure
- name: Power Bi Rest Import List Structure
  property_count: 2
  slug: power-bi-rest-import-list-structure
- name: Power Bi Rest Import Structure
  property_count: 7
  slug: power-bi-rest-import-structure
- name: Power Bi Rest Measure Structure
  property_count: 4
  slug: power-bi-rest-measure-structure
- name: Power Bi Rest Page List Structure
  property_count: 2
  slug: power-bi-rest-page-list-structure
- name: Power Bi Rest Page Structure
  property_count: 3
  slug: power-bi-rest-page-structure
- name: Power Bi Rest Parameter List Structure
  property_count: 2
  slug: power-bi-rest-parameter-list-structure
- name: Power Bi Rest Parameter Structure
  property_count: 5
  slug: power-bi-rest-parameter-structure
- name: Power Bi Rest Rebind Report Request Structure
  property_count: 1
  slug: power-bi-rest-rebind-report-request-structure
- name: Power Bi Rest Refresh List Structure
  property_count: 2
  slug: power-bi-rest-refresh-list-structure
- name: Power Bi Rest Refresh Request Structure
  property_count: 5
  slug: power-bi-rest-refresh-request-structure
- name: Power Bi Rest Refresh Structure
  property_count: 7
  slug: power-bi-rest-refresh-structure
- name: Power Bi Rest Relationship Structure
  property_count: 6
  slug: power-bi-rest-relationship-structure
- name: Power Bi Rest Report List Structure
  property_count: 2
  slug: power-bi-rest-report-list-structure
- name: Power Bi Rest Report Structure
  property_count: 10
  slug: power-bi-rest-report-structure
- name: Power Bi Rest Table Structure
  property_count: 4
  slug: power-bi-rest-table-structure
- name: Power Bi Rest Tile List Structure
  property_count: 2
  slug: power-bi-rest-tile-list-structure
- name: Power Bi Rest Tile Structure
  property_count: 9
  slug: power-bi-rest-tile-structure
- name: Power Bi Rest Update Parameters Request Structure
  property_count: 1
  slug: power-bi-rest-update-parameters-request-structure
- name: Power Bi Structure
  property_count: 0
  slug: power-bi-structure
jsonld:
- class_count: 0
  name: Power Bi Context
  property_count: 15
  slug: power-bi-context
- class_count: 0
  name: Power Bi Rest Context
  property_count: 0
  slug: power-bi-rest-context
layout: provider
modified: '2026-06-20'
name: Power BI
nav: Providers
network: true
overview: 'Power BI publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Dashboards API, Datasets API, Gateways API, and 3 more. Tagged areas include Analytics, Business Intelligence, Dashboards, Data Analysis, and Reporting.


  The Power BI catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Power BI''s developer surface includes authentication, sandbox, changelog, CLI, developer portal, engineering blog, support, and 56 more developer resources.'
plans:
- name: Power Bi Plans Pricing
  plan_count: 5
  slug: power-bi-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Power Bi Rate Limits
  slug: power-bi-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Power BI API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: power-bi-jsonschema-spectral-rules
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Power BI API Rules
  rule_count: 16
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 7
  slug: power-bi-spectral-rules
scopes:
- name: Power Bi Scopes
  scope_count: 17
  slug: power-bi-scopes
  summary_line: 17 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 66.8
  coverage:
    artifact_dirs: 34
    catalog_earned: 58.5
    catalog_earned_first_party: 0.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 72.8
    developer_ergonomics: 96.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 55.3
  previous_composite: 66.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/power-bi/refs/heads/main/screenshots/power-bi-2026-06-20T192022.png
security:
- kind: authentication
  name: Power Bi Authentication
  slug: power-bi-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Power Bi Domain Security
  slug: power-bi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Power Bi Vulnerability Disclosure
  slug: power-bi-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Power Bi Trust Center
  slug: power-bi-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, ISO 27701, PCI DSS, HIPAA / HITECH, HITRUST, FedRAMP, GDPR, CSA STAR
slug: power-bi
tags:
- Analytics
- Business Intelligence
- Dashboards
- Data Analysis
- Reporting
- Visualization
use_cases:
- description: Provide C-suite executives with real-time KPI dashboards for data-driven decision making.
  name: Executive Dashboards
- description: Track sales performance, pipeline metrics, and revenue forecasting with interactive reports.
  name: Sales Analytics
- description: Automate financial reporting with scheduled refreshes and pixel-perfect paginated reports.
  name: Financial Reporting
- description: Embed Power BI visualizations into SaaS applications to provide analytics to end customers.
  name: Embedded Analytics for ISVs
- description: Visualize real-time IoT sensor data with streaming datasets and live dashboard tiles.
  name: IoT Monitoring
- description: Analyze workforce metrics, retention rates, and employee engagement across the organization.
  name: HR Analytics
website: https://powerbi.microsoft.com/en-us/developers/
---
