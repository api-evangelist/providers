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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Sap Bi Tools Agentic Access
  operation_count: 32
  slug: sap-bi-tools-agentic-access
  summary_line: 32 operations · 11 acting
api_count: 4
apis:
- description: OData-based API for exporting fact data and master data from SAP Analytics Cloud models. Allows programmatic extraction of underlying data and metadata for integration with external systems and data p
  name: SAP Analytics Cloud Data Export API
  slug: sap-analytics-cloud-data-export-api
- description: REST API for managing content in the SAP Analytics Cloud Content Network. Enables programmatic access to get, publish, and delete private and public content items available through the Content Network
  name: SAP Analytics Cloud Content Network REST API
  slug: sap-analytics-cloud-content-network-rest-api
- description: JavaScript-based API for building interactive analytic applications in SAP Analytics Cloud Analytics Designer. Provides scripting capabilities to control widgets, data sources, planning operations, an
  name: SAP Analytics Cloud Analytics Designer API
  slug: sap-analytics-cloud-analytics-designer-api
- description: REST API for SAP BusinessObjects BI Platform for managing documents, users, and scheduling reports.
  name: SAP BusinessObjects BI Platform RESTful Web Services
  slug: sap-businessobjects-bi-platform-restful-web-services
- description: REST API for SAP BusinessObjects Web Intelligence for creating, modifying, and exporting Web Intelligence reports. Provides endpoints for report management, data provider operations, and document sche
  name: SAP BusinessObjects Web Intelligence RESTful Web Services API
  slug: sap-businessobjects-web-intelligence-restful-web-services-api
- description: REST API for working with SAP BusinessObjects BI Semantic Layer universes. Allows querying and managing universes, executing queries against semantic layer data sources, and handling prompts and conte
  name: SAP BusinessObjects BI Semantic Layer REST API
  slug: sap-businessobjects-bi-semantic-layer-rest-api
- description: RESTful API for SAP Crystal Reports for Enterprise that enables consuming and embedding Crystal Reports data in web and mobile applications. Supports retrieving report metadata, fetching data rows, se
  name: SAP Crystal Reports RESTful Web Services API
  slug: sap-crystal-reports-restful-web-services-api
- description: .NET SDK for integrating SAP Crystal Reports into Visual Studio applications. Enables developers to embed Crystal Reports into .NET web and desktop applications, programmatically create and modify rep
  name: SAP Crystal Reports .NET SDK
  slug: sap-crystal-reports-net-sdk
- description: JavaScript API for creating custom visualizations and extensions in SAP Lumira.
  name: SAP Lumira Discovery Extensions API
  slug: sap-lumira-discovery-extensions-api
- description: 'OData V4 API for browsing the SAP Datasphere catalog and consuming datasets and metadata from consumable data assets. Enables external applications to discover available spaces, access relational and '
  name: SAP Datasphere Consumption and Catalog API
  slug: sap-datasphere-consumption-and-catalog-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Administration service endpoints for discovering available namespaces and providers (models) on the SAP Analytics Cloud tenant.
  name: SAP BI Tools Administration API
  slug: sap-bi-tools-administration-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Logon and logoff endpoints for obtaining and invalidating session tokens required for all subsequent API calls.
  name: SAP BI Tools Authentication API
  slug: sap-bi-tools-authentication-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Manage calendar events and tasks used for planning workflows and scheduling in SAP Analytics Cloud.
  name: SAP BI Tools Calendars API
  slug: sap-bi-tools-calendars-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Execute CMS queries against the BI Platform repository to search for objects using CMS query language syntax.
  name: SAP BI Tools CMS Query API
  slug: sap-bi-tools-cms-query-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Manage content items in the Content Network including retrieving, publishing, and deleting both private and public content packages.
  name: SAP BI Tools Content Items API
  slug: sap-bi-tools-content-items-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Provider service endpoints for retrieving fact data from specific models. Fact data includes the transactional records with associated dimension values and measures.
  name: SAP BI Tools Fact Data API
  slug: sap-bi-tools-fact-data-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Import content items from the Content Network into the local SAP Analytics Cloud tenant.
  name: SAP BI Tools Import API
  slug: sap-bi-tools-import-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Manage BI Inbox items including viewing received reports and scheduled instances.
  name: SAP BI Tools Inbox API
  slug: sap-bi-tools-inbox-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Browse and query the CMS InfoStore repository to access documents, folders, users, groups, and other BI Platform objects.
  name: SAP BI Tools InfoStore API
  slug: sap-bi-tools-infostore-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Provider service endpoints for retrieving master data from specific model dimensions. Master data includes the dimension member lists with their attributes and hierarchies.
  name: SAP BI Tools Master Data API
  slug: sap-bi-tools-master-data-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Provider service endpoints for retrieving OData metadata documents describing the structure of models, dimensions, and measures.
  name: SAP BI Tools Metadata API
  slug: sap-bi-tools-metadata-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Browse and manage resources within the SAP Analytics Cloud file repository including stories, models, and folders.
  name: SAP BI Tools Resources API
  slug: sap-bi-tools-resources-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Schedule reports and documents for execution with configurable parameters, recurrence, and destination options.
  name: SAP BI Tools Scheduling API
  slug: sap-bi-tools-scheduling-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: Manage analytic stories including dashboards and reports. Stories are the primary visualization artifact in SAP Analytics Cloud.
  name: SAP BI Tools Stories API
  slug: sap-bi-tools-stories-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: SCIM 2.0 endpoints for managing teams and group memberships for access control in SAP Analytics Cloud.
  name: SAP BI Tools Teams API
  slug: sap-bi-tools-teams-api
- baseURL: https://api.sapanalytics.cloud
  baseurl_source: declared
  description: SCIM 2.0 endpoints for managing user accounts, provisioning, and deprovisioning in SAP Analytics Cloud.
  name: SAP BI Tools Users API
  slug: sap-bi-tools-users-api
arazzos:
- description: Log on, run a complex CMS query via POST, then drill into the first matching object and list its children.
  name: SAP BI Tools CMS Query Drilldown
  slug: sap-bi-tools-cms-query-drilldown-workflow
- description: Create a SAP Analytics Cloud user via SCIM 2.0, then create a team that includes the new user as a member.
  name: SAP BI Tools Create a SAC Team With a Member
  slug: sap-bi-tools-create-team-with-member-workflow
- description: Discover export namespaces and providers, read a model's master data overview, then pull a named dimension's master data.
  name: SAP BI Tools Export Dimension Master Data
  slug: sap-bi-tools-export-dimension-master-data-workflow
- description: Discover a SAC export model, read its OData metadata, and pull a filtered, paged page of fact data.
  name: SAP BI Tools Export Model Fact Data
  slug: sap-bi-tools-export-model-fact-data-workflow
- description: Discover a public content item in the Content Network and import it into a target folder, branching on the import outcome.
  name: SAP BI Tools Import a Content Network Item
  slug: sap-bi-tools-import-content-item-workflow
- description: List SAP Analytics Cloud stories and retrieve the first story's full detail including the models it uses.
  name: SAP BI Tools List and Inspect a SAC Story
  slug: sap-bi-tools-list-and-inspect-story-workflow
- description: Log on to the BI Platform, list the children of a folder, and read the metadata of the first document found.
  name: SAP BI Tools Logon and Browse a Folder
  slug: sap-bi-tools-logon-browse-folder-workflow
- description: Look up a SAP Analytics Cloud user by userName via SCIM 2.0 and create the user when no match exists.
  name: SAP BI Tools Provision a SAC User
  slug: sap-bi-tools-provision-scim-user-workflow
- description: Publish a local resource to the SAP Analytics Cloud Content Network and confirm it by reading the published item back.
  name: SAP BI Tools Publish a Content Network Item
  slug: sap-bi-tools-publish-content-item-workflow
- description: Log on, find documents with a CMS query, schedule the first match for immediate execution, and confirm the instance.
  name: SAP BI Tools Query and Schedule a Document
  slug: sap-bi-tools-query-and-schedule-document-workflow
- description: Find a private content item by type, delete it from the Content Network, and confirm it is gone.
  name: SAP BI Tools Retire a Content Network Item
  slug: sap-bi-tools-retire-content-item-workflow
- description: Log on, schedule a document for immediate execution, then poll the BI Inbox until the completed instance is delivered.
  name: SAP BI Tools Schedule and Poll the BI Inbox
  slug: sap-bi-tools-schedule-and-poll-inbox-workflow
- description: Open a BI Platform session, read the InfoStore root and its top-level folders, then cleanly log off.
  name: SAP BI Tools Session Lifecycle
  slug: sap-bi-tools-session-lifecycle-workflow
- description: Find a SAC story, fetch its detail, then list MODEL resources from the file repository to cross-reference its data sources.
  name: SAP BI Tools Story and Resource Cross-Reference
  slug: sap-bi-tools-story-resource-crossref-workflow
artifact_total: 100
collections:
- collection_type: postman
  name: SAP BI Tools SAP Analytics Cloud API
  slug: postman-sap-analytics-cloud-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud API
  slug: open-sap-analytics-cloud-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Content Network REST API
  slug: open-sap-analytics-cloud-content-network-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Data Export API
  slug: open-sap-analytics-cloud-data-export-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration API
  slug: open-sap-bi-tools-administration-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Authentication API
  slug: open-sap-bi-tools-authentication-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Calendars API
  slug: open-sap-bi-tools-calendars-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration CMS Query API
  slug: open-sap-bi-tools-cms-query-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Content Items API
  slug: open-sap-bi-tools-content-items-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Fact Data API
  slug: open-sap-bi-tools-fact-data-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Import API
  slug: open-sap-bi-tools-import-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Inbox API
  slug: open-sap-bi-tools-inbox-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration InfoStore API
  slug: open-sap-bi-tools-infostore-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Master Data API
  slug: open-sap-bi-tools-master-data-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Metadata API
  slug: open-sap-bi-tools-metadata-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Resources API
  slug: open-sap-bi-tools-resources-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Scheduling API
  slug: open-sap-bi-tools-scheduling-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Stories API
  slug: open-sap-bi-tools-stories-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Teams API
  slug: open-sap-bi-tools-teams-api
- collection_type: open
  name: SAP BI Tools SAP Analytics Cloud Administration Users API
  slug: open-sap-bi-tools-users-api
- collection_type: open
  name: SAP BI Tools SAP BusinessObjects BI Platform RESTful Web Services
  slug: open-sap-businessobjects-bi-platform-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/SAP-samples/analytics-cloud-export-api-wrapper/issues
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/sap/
- group: commercial
  title: ''
  type: License
  url: https://github.com/SAP-samples/analytics-cloud-export-api-wrapper/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-bi-tools-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-bi-tools-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-bi-tools-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-bi-tools-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sap-bi-tools-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sap-bi-tools/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-cms-query-drilldown-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-create-team-with-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-export-dimension-master-data-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-export-model-fact-data-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-import-content-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-list-and-inspect-story-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-logon-browse-folder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-provision-scim-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-publish-content-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-query-and-schedule-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-retire-content-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-schedule-and-poll-inbox-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-session-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-bi-tools-story-resource-crossref-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://api.sap.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.sap.com/topics/business-technology-platform..html
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/SAP_ANALYTICS_CLOUD
- group: auth
  title: ''
  type: Authentication
  url: https://help.sap.com/docs/authentication
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sap.com/about/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sap.com/about/trust-center/cloud-service-status.html
- group: operate
  title: ''
  type: Support
  url: https://support.sap.com
- group: operate
  title: ''
  type: Community
  url: https://community.sap.com
- group: company
  title: ''
  type: Blog
  url: https://community.sap.com/t5/application-development-and-automation-blog-posts/bg-p/application-developmentblog-board
- group: learn
  title: ''
  type: Learning
  url: https://learning.sap.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://pages.community.sap.com/topics/cloud-analytics/product-updates
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SAP
- group: company
  title: ''
  type: Website
  url: https://www.sap.com
- group: start
  title: ''
  type: Signup
  url: https://developers.sap.com
- group: build
  title: ''
  type: SDKs
  url: https://developers.sap.com/topics/cloud-sdk.html
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/sap-analytics-cloud-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/sap-analytics-cloud-content-network-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/sap-analytics-cloud-data-export-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/sap-businessobjects-bi-platform-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sap-bi-tools-story-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sap-bi-tools-user-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/sap-bi-tools-content-item-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sap-bi-tools-story-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/sap-bi-tools-user-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sap-bi-tools-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sap-bi-tools-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/sap-bi-tools-rules.yml
created: '2024-01-20'
description: Collection of SAP Business Intelligence tools and APIs for analytics, reporting, and data visualization.
examples:
- key_count: 2
  name: Sap Bi Tools Get Fact Data Example
  slug: sap-bi-tools-get-fact-data-example
- key_count: 4
  name: Sap Bi Tools List Users Example
  slug: sap-bi-tools-list-users-example
finops:
- name: Sap Bi Tools Finops
  service_category: Business Intelligence / Reporting
  slug: sap-bi-tools-finops
json_schemas:
- name: CalendarEvent
  property_count: 7
  slug: sap-bi-tools-calendarevent
- name: SAP Analytics Cloud Content Item
  property_count: 9
  slug: sap-bi-tools-content-item
- name: ContentItem
  property_count: 9
  slug: sap-bi-tools-contentitem
- name: ContentItemPublish
  property_count: 4
  slug: sap-bi-tools-contentitempublish
- name: ImportOptions
  property_count: 2
  slug: sap-bi-tools-importoptions
- name: ImportResult
  property_count: 2
  slug: sap-bi-tools-importresult
- name: InfoStoreCollection
  property_count: 2
  slug: sap-bi-tools-infostorecollection
- name: InfoStoreEntry
  property_count: 9
  slug: sap-bi-tools-infostoreentry
- name: LogonRequest
  property_count: 3
  slug: sap-bi-tools-logonrequest
- name: LogonResponse
  property_count: 1
  slug: sap-bi-tools-logonresponse
- name: ModelReference
  property_count: 3
  slug: sap-bi-tools-modelreference
- name: ODataCollection
  property_count: 2
  slug: sap-bi-tools-odatacollection
- name: Provider
  property_count: 3
  slug: sap-bi-tools-provider
- name: ProviderCollection
  property_count: 2
  slug: sap-bi-tools-providercollection
- name: Resource
  property_count: 8
  slug: sap-bi-tools-resource
- name: ScheduleRequest
  property_count: 2
  slug: sap-bi-tools-schedulerequest
- name: ScheduleResponse
  property_count: 2
  slug: sap-bi-tools-scheduleresponse
- name: ScimGroup
  property_count: 3
  slug: sap-bi-tools-scimgroup
- name: ScimListResponse
  property_count: 4
  slug: sap-bi-tools-scimlistresponse
- name: ScimUser
  property_count: 8
  slug: sap-bi-tools-scimuser
- name: SAP Analytics Cloud Story
  property_count: 9
  slug: sap-bi-tools-story
- name: SAP Analytics Cloud User
  property_count: 8
  slug: sap-bi-tools-user
json_structures:
- name: Sap Bi Tools Story Structure
  property_count: 0
  slug: sap-bi-tools-story-structure
- name: Sap Bi Tools Structure
  property_count: 0
  slug: sap-bi-tools-structure
- name: Sap Bi Tools User Structure
  property_count: 0
  slug: sap-bi-tools-user-structure
jsonld:
- class_count: 26
  name: Sap Bi Tools Context
  property_count: 4
  slug: sap-bi-tools-context
layout: provider
modified: '2026-08-21'
name: SAP BI Tools
nav: Providers
network: true
overview: 'SAP BI Tools publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Administration API, Authentication API, Calendars API, and 13 more. Tagged areas include Analytics, Business Intelligence, Data Visualization, Reporting, and SAP.


  The SAP BI Tools catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SAP BI Tools'' developer surface includes authentication, developer portal, getting-started guide, documentation, support, engineering blog, changelog, and 44 more developer resources.'
plans:
- name: Sap Bi Tools Plans Pricing
  plan_count: 1
  slug: sap-bi-tools-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 1
  name: Sap Bi Tools Rate Limits
  slug: sap-bi-tools-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: SAP BI Tools API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sap-bi-tools-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: SAP BI Tools API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 2
    warn: 7
  slug: sap-bi-tools-rules
scopes:
- name: Sap Bi Tools Scopes
  scope_count: 0
  slug: sap-bi-tools-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.5
    catalog_earned_first_party: 0.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 68.6
    developer_ergonomics: 46.4
    discoverability: 53.7
    governance: 28.8
    operational_transparency: 39.5
  previous_composite: 49.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-bi-tools/refs/heads/main/screenshots/sap-bi-tools-2026-06-20T193416.png
security:
- kind: authentication
  name: Sap Bi Tools Authentication
  slug: sap-bi-tools-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Sap Bi Tools Domain Security
  slug: sap-bi-tools-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Bi Tools Vulnerability Disclosure
  slug: sap-bi-tools-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-bi-tools
tags:
- Analytics
- Business Intelligence
- Data Visualization
- Reporting
- SAP
website: https://www.sap.com
---
