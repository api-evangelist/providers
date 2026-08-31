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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 45
  human_in_the_loop: 0
  name: Salesforce Sales Cloud Agentic Access
  operation_count: 114
  slug: salesforce-sales-cloud-agentic-access
  summary_line: 114 operations · 45 acting
api_count: 8
apis:
- description: Comprehensive SOAP-based API for enterprise integrations with full CRUD operations on Salesforce objects. Uses WSDL files to define parameters for accessing data through the API.
  name: Salesforce SOAP API
  slug: salesforce-soap-api
- description: API for retrieving, deploying, creating, updating, or deleting customization information such as custom object definitions and page layouts. Essential for managing org configuration and deployment wor
  name: Metadata API
  slug: metadata-api
- description: Push notification API using Bayeux protocol to receive near real-time updates when data changes in Salesforce. Enables event-driven integrations without polling.
  name: Streaming API
  slug: streaming-api
- description: gRPC-based API for publishing and subscribing to platform events, change data capture events, and real-time event monitoring events. Uses Apache Avro format for efficient binary event message delivery
  name: Salesforce Pub/Sub API
  slug: salesforce-pubsub-api
- description: Change event metadata and schema operations
  name: Salesforce Sales Cloud Change Events API
  slug: salesforce-sales-cloud-change-events-api
- description: Community (Experience Cloud) operations
  name: Salesforce Sales Cloud Communities API
  slug: salesforce-sales-cloud-communities-api
- description: Apex code completions
  name: Salesforce Sales Cloud Completions API
  slug: salesforce-sales-cloud-completions-api
- description: Custom Apex REST endpoints defined by @RestResource annotated classes
  name: Salesforce Sales Cloud Custom Endpoints API
  slug: salesforce-sales-cloud-custom-endpoints-api
- description: Operations for listing, describing, and refreshing dashboards
  name: Salesforce Sales Cloud Dashboards API
  slug: salesforce-sales-cloud-dashboards-api
- description: Retrieve event schema definitions
  name: Salesforce Sales Cloud Event Schema API
  slug: salesforce-sales-cloud-event-schema-api
- description: Execute anonymous Apex code
  name: Salesforce Sales Cloud Execute Anonymous API
  slug: salesforce-sales-cloud-execute-anonymous-api
- description: Individual feed item operations
  name: Salesforce Sales Cloud Feed Items API
  slug: salesforce-sales-cloud-feed-items-api
- description: Chatter feed operations
  name: Salesforce Sales Cloud Feeds API
  slug: salesforce-sales-cloud-feeds-api
- description: File sharing and management
  name: Salesforce Sales Cloud Files API
  slug: salesforce-sales-cloud-files-api
- description: Chatter group operations
  name: Salesforce Sales Cloud Groups API
  slug: salesforce-sales-cloud-groups-api
- description: Upload CSV data to ingest jobs and retrieve results
  name: Salesforce Sales Cloud Ingest Data API
  slug: salesforce-sales-cloud-ingest-data-api
- description: Create and manage bulk ingest jobs for insert, update, upsert, and delete operations
  name: Salesforce Sales Cloud Ingest Jobs API
  slug: salesforce-sales-cloud-ingest-jobs-api
- description: Page layout metadata
  name: Salesforce Sales Cloud Layouts API
  slug: salesforce-sales-cloud-layouts-api
- description: Org limits and usage information
  name: Salesforce Sales Cloud Limits API
  slug: salesforce-sales-cloud-limits-api
- description: List view metadata and records
  name: Salesforce Sales Cloud List Views API
  slug: salesforce-sales-cloud-list-views-api
- description: Lookup field search
  name: Salesforce Sales Cloud Lookups API
  slug: salesforce-sales-cloud-lookups-api
- description: Object and field metadata for UI rendering
  name: Salesforce Sales Cloud Object Info API
  slug: salesforce-sales-cloud-object-info-api
- description: Picklist field values with record type awareness
  name: Salesforce Sales Cloud Picklist Values API
  slug: salesforce-sales-cloud-picklist-values-api
- description: Process approval operations
  name: Salesforce Sales Cloud Process Approvals API
  slug: salesforce-sales-cloud-process-approvals-api
- description: SOQL query execution
  name: Salesforce Sales Cloud Query API
  slug: salesforce-sales-cloud-query-api
- description: Create and manage bulk query jobs for extracting large data sets
  name: Salesforce Sales Cloud Query Jobs API
  slug: salesforce-sales-cloud-query-jobs-api
- description: Retrieve results from completed query jobs
  name: Salesforce Sales Cloud Query Results API
  slug: salesforce-sales-cloud-query-results-api
- description: Recently viewed items
  name: Salesforce Sales Cloud Recently Viewed API
  slug: salesforce-sales-cloud-recently-viewed-api
- description: Complete record page data including layout and metadata
  name: Salesforce Sales Cloud Record UI API
  slug: salesforce-sales-cloud-record-ui-api
- description: Record CRUD operations with UI metadata
  name: Salesforce Sales Cloud Records API
  slug: salesforce-sales-cloud-records-api
- description: Asynchronous report execution and results retrieval
  name: Salesforce Sales Cloud Report Instances API
  slug: salesforce-sales-cloud-report-instances-api
- description: Report type metadata and discovery
  name: Salesforce Sales Cloud Report Types API
  slug: salesforce-sales-cloud-report-types-api
- description: Operations for listing, describing, and running reports
  name: Salesforce Sales Cloud Reports API
  slug: salesforce-sales-cloud-reports-api
- description: Available REST resources for a given API version
  name: Salesforce Sales Cloud Resources API
  slug: salesforce-sales-cloud-resources-api
- description: Execute Apex tests
  name: Salesforce Sales Cloud Run Tests API
  slug: salesforce-sales-cloud-run-tests-api
- description: SOSL search execution
  name: Salesforce Sales Cloud Search API
  slug: salesforce-sales-cloud-search-api
- description: Operations on Salesforce standard and custom objects
  name: Salesforce Sales Cloud SObject API
  slug: salesforce-sales-cloud-sobject-api
- description: Bulk CRUD on collections of same-type records
  name: Salesforce Sales Cloud SObject Collections API
  slug: salesforce-sales-cloud-sobject-collections-api
- description: Metadata description of sObjects
  name: Salesforce Sales Cloud SObject Describe API
  slug: salesforce-sales-cloud-sobject-describe-api
- description: CRUD operations on individual sObject records
  name: Salesforce Sales Cloud SObject Rows API
  slug: salesforce-sales-cloud-sobject-rows-api
- description: Tab metadata
  name: Salesforce Sales Cloud Tabs API
  slug: salesforce-sales-cloud-tabs-api
- description: Theme information
  name: Salesforce Sales Cloud Themes API
  slug: salesforce-sales-cloud-themes-api
- description: Execute SOQL queries against Tooling API objects
  name: Salesforce Sales Cloud Tooling Query API
  slug: salesforce-sales-cloud-tooling-query-api
- description: Metadata about Tooling API sObjects
  name: Salesforce Sales Cloud Tooling SObject Describe API
  slug: salesforce-sales-cloud-tooling-sobject-describe-api
- description: CRUD operations on Tooling API sObjects
  name: Salesforce Sales Cloud Tooling SObjects API
  slug: salesforce-sales-cloud-tooling-sobjects-api
- description: User profile and photo operations
  name: Salesforce Sales Cloud Users API
  slug: salesforce-sales-cloud-users-api
arazzos:
- description: Resolve an Account by name, then pull its related Contacts and open Opportunities.
  name: Salesforce Sales Cloud Account 360 Enrichment
  slug: salesforce-sales-cloud-account-360-enrichment-workflow
- description: Create an Account and its child Contacts in one tree call, then read the Account back.
  name: Salesforce Sales Cloud Account Tree With Contacts
  slug: salesforce-sales-cloud-account-tree-with-contacts-workflow
- description: Create a batch of Accounts in one collection call, then verify the count with SOQL.
  name: Salesforce Sales Cloud Bulk Import Accounts
  slug: salesforce-sales-cloud-bulk-import-accounts-workflow
- description: Move an Opportunity to Closed Won, then read it back and log a follow-up Task.
  name: Salesforce Sales Cloud Close Opportunity Won
  slug: salesforce-sales-cloud-close-opportunity-won-workflow
- description: Capture a Lead, then realize the conversion by creating Account, Contact, and Opportunity records.
  name: Salesforce Sales Cloud Create And Convert Lead
  slug: salesforce-sales-cloud-create-and-convert-lead-workflow
- description: Create a Contact, then read it back by id to confirm the persisted field values.
  name: Salesforce Sales Cloud Create Then Retrieve Contact
  slug: salesforce-sales-cloud-create-then-retrieve-contact-workflow
- description: Find an unconverted Lead by email via SOQL, then delete the matched record.
  name: Salesforce Sales Cloud Delete Stale Lead
  slug: salesforce-sales-cloud-delete-stale-lead-workflow
- description: Describe an sObject to confirm it is creatable, then create a record of that type.
  name: Salesforce Sales Cloud Describe Then Create Record
  slug: salesforce-sales-cloud-describe-then-create-record-workflow
- description: Find an Account by SOQL, then create a follow-up Task linked to it.
  name: Salesforce Sales Cloud Log Task On Account
  slug: salesforce-sales-cloud-log-task-on-account-workflow
- description: Create an Account, attach a primary Contact, then open an Opportunity against it.
  name: Salesforce Sales Cloud New Customer Onboarding
  slug: salesforce-sales-cloud-new-customer-onboarding-workflow
- description: Open an Opportunity, then attach a Contact to it as an OpportunityContactRole.
  name: Salesforce Sales Cloud Opportunity With Contact Role
  slug: salesforce-sales-cloud-opportunity-with-contact-role-workflow
- description: Run a large SOQL query, then page to the next batch when the first is not complete.
  name: Salesforce Sales Cloud Paginated SOQL Export
  slug: salesforce-sales-cloud-paginated-soql-export-workflow
- description: Find an Account with a SOQL query, then patch the matched record's fields.
  name: Salesforce Sales Cloud Query Then Update Account
  slug: salesforce-sales-cloud-query-then-update-account-workflow
- description: Look up a Contact and a target Account by SOQL, then move the Contact under that Account.
  name: Salesforce Sales Cloud Reparent Contact To Account
  slug: salesforce-sales-cloud-reparent-contact-to-account-workflow
- description: Find a Contact by email, then create a calendar Event linked to that Contact.
  name: Salesforce Sales Cloud Schedule Event With Contact
  slug: salesforce-sales-cloud-schedule-event-with-contact-workflow
- description: Run a SOSL search across objects, then fetch the full record for the top hit.
  name: Salesforce Sales Cloud Search Then Retrieve Record
  slug: salesforce-sales-cloud-search-then-retrieve-record-workflow
- description: Create an Opportunity, then submit that record into its approval process.
  name: Salesforce Sales Cloud Submit Opportunity For Approval
  slug: salesforce-sales-cloud-submit-opportunity-for-approval-workflow
- description: Upsert an Account on an external ID field, then attach a Contact to it.
  name: Salesforce Sales Cloud Upsert Account By External ID
  slug: salesforce-sales-cloud-upsert-account-by-external-id-workflow
artifact_total: 202
collections:
- collection_type: postman
  name: Salesforce Sales Cloud Salesforce Analytics REST API
  slug: postman-salesforce-sales-cloud-analytics-api
- collection_type: postman
  name: Salesforce Sales Cloud Salesforce Apex REST API
  slug: postman-salesforce-sales-cloud-apex-rest-api
- collection_type: postman
  name: Salesforce Sales Cloud Salesforce Bulk API 2.0
  slug: postman-salesforce-sales-cloud-bulk-api
- collection_type: postman
  name: Salesforce Sales Cloud Salesforce Change Data Capture API
  slug: postman-salesforce-sales-cloud-change-data-capture-api
- collection_type: postman
  name: Salesforce Sales Cloud Salesforce Composite API
  slug: postman-salesforce-sales-cloud-composite-api
- collection_type: postman
  name: Salesforce Sales Cloud Salesforce Connect REST API
  slug: postman-salesforce-sales-cloud-connect-api
- collection_type: postman
  name: Salesforce Sales Cloud Salesforce GraphQL API
  slug: postman-salesforce-sales-cloud-graphql-api
- collection_type: postman
  name: Salesforce Sales Cloud Salesforce Platform Events API
  slug: postman-salesforce-sales-cloud-platform-events-api
- collection_type: postman
  name: Salesforce Sales Cloud Salesforce REST API
  slug: postman-salesforce-sales-cloud-rest-api
- collection_type: postman
  name: Salesforce Sales Cloud Salesforce Tooling API
  slug: postman-salesforce-sales-cloud-tooling-api
- collection_type: postman
  name: Salesforce Sales Cloud Salesforce User Interface API
  slug: postman-salesforce-sales-cloud-ui-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST API
  slug: open-salesforce-sales-cloud-analytics-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Apex REST API
  slug: open-salesforce-sales-cloud-apex-rest-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Bulk API 2.0
  slug: open-salesforce-sales-cloud-bulk-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Change Data Capture API
  slug: open-salesforce-sales-cloud-change-data-capture-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events API
  slug: open-salesforce-sales-cloud-change-events-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Communities API
  slug: open-salesforce-sales-cloud-communities-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Completions API
  slug: open-salesforce-sales-cloud-completions-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Composite API
  slug: open-salesforce-sales-cloud-composite-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Composite Batch API
  slug: open-salesforce-sales-cloud-composite-batch-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Composite Graph API
  slug: open-salesforce-sales-cloud-composite-graph-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Connect REST API
  slug: open-salesforce-sales-cloud-connect-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Custom Endpoints API
  slug: open-salesforce-sales-cloud-custom-endpoints-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Dashboards API
  slug: open-salesforce-sales-cloud-dashboards-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Event Schema API
  slug: open-salesforce-sales-cloud-event-schema-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Execute Anonymous API
  slug: open-salesforce-sales-cloud-execute-anonymous-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Feed Items API
  slug: open-salesforce-sales-cloud-feed-items-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Feeds API
  slug: open-salesforce-sales-cloud-feeds-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Files API
  slug: open-salesforce-sales-cloud-files-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events GraphQL API
  slug: open-salesforce-sales-cloud-graphql-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Groups API
  slug: open-salesforce-sales-cloud-groups-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Ingest Data API
  slug: open-salesforce-sales-cloud-ingest-data-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Ingest Jobs API
  slug: open-salesforce-sales-cloud-ingest-jobs-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Layouts API
  slug: open-salesforce-sales-cloud-layouts-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Limits API
  slug: open-salesforce-sales-cloud-limits-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events List Views API
  slug: open-salesforce-sales-cloud-list-views-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Lookups API
  slug: open-salesforce-sales-cloud-lookups-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Object Info API
  slug: open-salesforce-sales-cloud-object-info-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Picklist Values API
  slug: open-salesforce-sales-cloud-picklist-values-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Platform Events API
  slug: open-salesforce-sales-cloud-platform-events-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Process Approvals API
  slug: open-salesforce-sales-cloud-process-approvals-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Query API
  slug: open-salesforce-sales-cloud-query-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Query Jobs API
  slug: open-salesforce-sales-cloud-query-jobs-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Query Results API
  slug: open-salesforce-sales-cloud-query-results-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Recently Viewed API
  slug: open-salesforce-sales-cloud-recently-viewed-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Record UI API
  slug: open-salesforce-sales-cloud-record-ui-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Records API
  slug: open-salesforce-sales-cloud-records-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Report Instances API
  slug: open-salesforce-sales-cloud-report-instances-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Report Types API
  slug: open-salesforce-sales-cloud-report-types-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Reports API
  slug: open-salesforce-sales-cloud-reports-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Resources API
  slug: open-salesforce-sales-cloud-resources-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce REST API
  slug: open-salesforce-sales-cloud-rest-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Run Tests API
  slug: open-salesforce-sales-cloud-run-tests-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Search API
  slug: open-salesforce-sales-cloud-search-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events SObject API
  slug: open-salesforce-sales-cloud-sobject-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events SObject Collections API
  slug: open-salesforce-sales-cloud-sobject-collections-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events SObject Describe API
  slug: open-salesforce-sales-cloud-sobject-describe-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events SObject Rows API
  slug: open-salesforce-sales-cloud-sobject-rows-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events SObject Tree API
  slug: open-salesforce-sales-cloud-sobject-tree-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Tabs API
  slug: open-salesforce-sales-cloud-tabs-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Themes API
  slug: open-salesforce-sales-cloud-themes-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Tooling API
  slug: open-salesforce-sales-cloud-tooling-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Tooling Query API
  slug: open-salesforce-sales-cloud-tooling-query-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Tooling SObject Describe API
  slug: open-salesforce-sales-cloud-tooling-sobject-describe-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Tooling SObjects API
  slug: open-salesforce-sales-cloud-tooling-sobjects-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce User Interface API
  slug: open-salesforce-sales-cloud-ui-api
- collection_type: open
  name: Salesforce Sales Cloud Salesforce Analytics REST Change Events Users API
  slug: open-salesforce-sales-cloud-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/salesforce-sales-cloud-capability-edges.yml
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/salesforce/
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesforce-sales-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesforce-sales-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salesforce-sales-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salesforce-sales-cloud-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/salesforce-sales-cloud/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-account-360-enrichment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-account-tree-with-contacts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-bulk-import-accounts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-close-opportunity-won-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-create-and-convert-lead-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-create-then-retrieve-contact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-delete-stale-lead-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-describe-then-create-record-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-log-task-on-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-new-customer-onboarding-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-opportunity-with-contact-role-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-paginated-soql-export-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-query-then-update-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-reparent-contact-to-account-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-schedule-event-with-contact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-search-then-retrieve-record-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-submit-opportunity-for-approval-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/salesforce-sales-cloud-upsert-account-by-external-id-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/salesforcesalescloud
- group: start
  title: ''
  type: Portal
  url: https://developer.salesforce.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.salesforce.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart.htm
- group: auth
  title: ''
  type: Authentication
  url: https://help.salesforce.com/s/articleView?id=sf.remoteaccess_authenticate.htm
- group: company
  title: ''
  type: Blog
  url: https://developer.salesforce.com/blogs
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesforce.com/
- group: operate
  title: ''
  type: Support
  url: https://help.salesforce.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesforce.com/company/legal/agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesforce.com/company/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/salesforce
- group: operate
  title: ''
  type: Community
  url: https://trailhead.salesforce.com/en/trailblazercommunity
- group: company
  title: ''
  type: Website
  url: https://www.salesforce.com/products/sales-cloud/
- group: start
  title: ''
  type: Login
  url: https://login.salesforce.com/
- group: start
  title: ''
  type: Signup
  url: https://developer.salesforce.com/signup
- group: build
  title: ''
  type: SDKs
  url: https://developer.salesforce.com/tools/sdk
- group: start
  title: ''
  type: Console
  url: https://workbench.developerforce.com/
- group: learn
  title: ''
  type: Trailhead Learning
  url: https://trailhead.salesforce.com/en/content/learn/modules/api_basics
- group: other
  title: ''
  type: API Limits
  url: https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm
- group: build
  title: ''
  type: API Library
  url: https://developer.salesforce.com/docs/apis
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/salesforce-developers/workspace/salesforce-developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/rest_rns.htm
- group: docs
  title: ''
  type: SOQL and SOSL Reference
  url: https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_soql_sosl_intro.htm
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/salesforce-sales-cloud-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/salesforce-sales-cloud-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/salesforce-sales-cloud-vocabulary.yml
- group: docs
  title: Account Schema
  type: JSONSchema
  url: json-schema/salesforce-sales-cloud-account-schema.json
- group: docs
  title: Contact Schema
  type: JSONSchema
  url: json-schema/salesforce-sales-cloud-contact-schema.json
- group: docs
  title: Lead Schema
  type: JSONSchema
  url: json-schema/salesforce-sales-cloud-lead-schema.json
- group: docs
  title: Opportunity Schema
  type: JSONSchema
  url: json-schema/salesforce-sales-cloud-opportunity-schema.json
- group: docs
  title: Task Schema
  type: JSONSchema
  url: json-schema/salesforce-sales-cloud-task-schema.json
- group: docs
  title: Case Schema
  type: JSONSchema
  url: json-schema/salesforce-sales-cloud-case-schema.json
- group: docs
  title: Campaign Schema
  type: JSONSchema
  url: json-schema/salesforce-sales-cloud-campaign-schema.json
created: '2024-01-15'
description: Enterprise CRM platform providing sales automation, customer relationship management, and business intelligence capabilities through REST and SOAP APIs.
examples:
- key_count: 7
  name: Salesforce Sales Cloud Create Opportunity Example
  slug: salesforce-sales-cloud-create-opportunity-example
- key_count: 7
  name: Salesforce Sales Cloud Soql Query Example
  slug: salesforce-sales-cloud-soql-query-example
finops:
- name: Salesforce Sales Cloud Finops
  service_category: CRM
  slug: salesforce-sales-cloud-finops
graphqls:
- description: Query Salesforce data using GraphQL, allowing clients to request exactly the fields they need in a single request. Reduces payload size and supports aggregation across object relationships.
  name: Salesforce Sales Cloud GraphQL API
  slug: salesforce-sales-cloud-graphql
image: https://www.salesforce.com/content/dam/web/en_us/www/images/salesforce-logo.svg
json_schemas:
- name: Salesforce Account
  property_count: 52
  slug: salesforce-sales-cloud-account
- name: ApiError
  property_count: 2
  slug: salesforce-sales-cloud-apierror
- name: Salesforce Campaign
  property_count: 32
  slug: salesforce-sales-cloud-campaign
- name: Salesforce Case
  property_count: 36
  slug: salesforce-sales-cloud-case
- name: ChangeEventMessage
  property_count: 3
  slug: salesforce-sales-cloud-changeeventmessage
- name: ChatterGroup
  property_count: 7
  slug: salesforce-sales-cloud-chattergroup
- name: Comment
  property_count: 4
  slug: salesforce-sales-cloud-comment
- name: Community
  property_count: 17
  slug: salesforce-sales-cloud-community
- name: CompositeBatchRequest
  property_count: 2
  slug: salesforce-sales-cloud-compositebatchrequest
- name: CompositeBatchResponse
  property_count: 2
  slug: salesforce-sales-cloud-compositebatchresponse
- name: CompositeGraphRequest
  property_count: 1
  slug: salesforce-sales-cloud-compositegraphrequest
- name: CompositeGraphResponse
  property_count: 1
  slug: salesforce-sales-cloud-compositegraphresponse
- name: CompositeRequest
  property_count: 3
  slug: salesforce-sales-cloud-compositerequest
- name: CompositeResponse
  property_count: 1
  slug: salesforce-sales-cloud-compositeresponse
- name: Salesforce Contact
  property_count: 57
  slug: salesforce-sales-cloud-contact
- name: CreateIngestJobRequest
  property_count: 7
  slug: salesforce-sales-cloud-createingestjobrequest
- name: CreateQueryJobRequest
  property_count: 4
  slug: salesforce-sales-cloud-createqueryjobrequest
- name: CreateRecordResult
  property_count: 3
  slug: salesforce-sales-cloud-createrecordresult
- name: Dashboard
  property_count: 7
  slug: salesforce-sales-cloud-dashboard
- name: DashboardListItem
  property_count: 6
  slug: salesforce-sales-cloud-dashboardlistitem
- name: ErrorResponse
  property_count: 0
  slug: salesforce-sales-cloud-errorresponse
- name: FeedElement
  property_count: 10
  slug: salesforce-sales-cloud-feedelement
- name: FeedElementInput
  property_count: 3
  slug: salesforce-sales-cloud-feedelementinput
- name: FeedElementPage
  property_count: 3
  slug: salesforce-sales-cloud-feedelementpage
- name: FieldDescribe
  property_count: 56
  slug: salesforce-sales-cloud-fielddescribe
- name: FileReference
  property_count: 9
  slug: salesforce-sales-cloud-filereference
- name: GraphQLError
  property_count: 4
  slug: salesforce-sales-cloud-graphqlerror
- name: GraphQLErrorResponse
  property_count: 1
  slug: salesforce-sales-cloud-graphqlerrorresponse
- name: GraphQLRequest
  property_count: 3
  slug: salesforce-sales-cloud-graphqlrequest
- name: GraphQLResponse
  property_count: 2
  slug: salesforce-sales-cloud-graphqlresponse
- name: IngestJobInfo
  property_count: 21
  slug: salesforce-sales-cloud-ingestjobinfo
- name: Salesforce Lead
  property_count: 52
  slug: salesforce-sales-cloud-lead
- name: MessageBody
  property_count: 1
  slug: salesforce-sales-cloud-messagebody
- name: ObjectInfo
  property_count: 19
  slug: salesforce-sales-cloud-objectinfo
- name: Salesforce Opportunity
  property_count: 38
  slug: salesforce-sales-cloud-opportunity
- name: PicklistValue
  property_count: 4
  slug: salesforce-sales-cloud-picklistvalue
- name: PublishResult
  property_count: 3
  slug: salesforce-sales-cloud-publishresult
- name: QueryJobInfo
  property_count: 16
  slug: salesforce-sales-cloud-queryjobinfo
- name: QueryResult
  property_count: 4
  slug: salesforce-sales-cloud-queryresult
- name: RecordRepresentation
  property_count: 11
  slug: salesforce-sales-cloud-recordrepresentation
- name: ReportFilter
  property_count: 5
  slug: salesforce-sales-cloud-reportfilter
- name: ReportInstance
  property_count: 6
  slug: salesforce-sales-cloud-reportinstance
- name: ReportListItem
  property_count: 5
  slug: salesforce-sales-cloud-reportlistitem
- name: ReportMetadata
  property_count: 23
  slug: salesforce-sales-cloud-reportmetadata
- name: ReportResults
  property_count: 7
  slug: salesforce-sales-cloud-reportresults
- name: SaveResult
  property_count: 3
  slug: salesforce-sales-cloud-saveresult
- name: SearchResult
  property_count: 1
  slug: salesforce-sales-cloud-searchresult
- name: SObjectDescribe
  property_count: 33
  slug: salesforce-sales-cloud-sobjectdescribe
- name: SObjectDescribeBrief
  property_count: 24
  slug: salesforce-sales-cloud-sobjectdescribebrief
- name: SObjectRecord
  property_count: 2
  slug: salesforce-sales-cloud-sobjectrecord
- name: SObjectTreeRecord
  property_count: 1
  slug: salesforce-sales-cloud-sobjecttreerecord
- name: Salesforce Task
  property_count: 30
  slug: salesforce-sales-cloud-task
- name: UserDetail
  property_count: 17
  slug: salesforce-sales-cloud-userdetail
- name: UserSummary
  property_count: 8
  slug: salesforce-sales-cloud-usersummary
json_structures:
- name: Salesforce Sales Cloud Account Structure
  property_count: 0
  slug: salesforce-sales-cloud-account-structure
- name: Salesforce Sales Cloud Opportunity Structure
  property_count: 0
  slug: salesforce-sales-cloud-opportunity-structure
- name: Salesforce Sales Cloud Structure
  property_count: 0
  slug: salesforce-sales-cloud-structure
jsonld:
- class_count: 2
  name: Salesforce Sales Cloud Context
  property_count: 11
  slug: salesforce-sales-cloud-context
layout: provider
modified: '2026-08-21'
name: Salesforce Sales Cloud
nav: Providers
network: true
overview: 'Salesforce Sales Cloud publishes 42 APIs on the [APIs.io](https://apis.io/) network, including Change Events API, Communities API, Completions API, and 39 more. Tagged areas include Cloud, CRM, Customer Management, Enterprise, and Sales.


  The Salesforce Sales Cloud catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Salesforce Sales Cloud''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, signup flow, and 51 more developer resources.'
plans:
- name: Salesforce Sales Cloud Plans Pricing
  plan_count: 1
  slug: salesforce-sales-cloud-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Salesforce Sales Cloud Rate Limits
  slug: salesforce-sales-cloud-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: Salesforce Sales Cloud API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: salesforce-sales-cloud-jsonschema-spectral-rules
- effective_rule_count: 10
  extends: []
  name: Salesforce Sales Cloud API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 4
  slug: salesforce-sales-cloud-rules
scopes:
- name: Salesforce Sales Cloud Scopes
  scope_count: 4
  slug: salesforce-sales-cloud-scopes
  summary_line: 4 scopes · authorizationCode/clientCredentials
score:
  band: developing
  composite: 51.5
  coverage:
    artifact_dirs: 21
    catalog_gap: 69.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 25.0
    contract_quality: 68.8
    developer_ergonomics: 76.2
    discoverability: 48.1
    governance: 25.0
    operational_transparency: 23.7
  previous_composite: 51.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 48
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesforce-sales-cloud/refs/heads/main/screenshots/salesforce-sales-cloud-2026-06-20T193350.png
security:
- kind: authentication
  name: Salesforce Sales Cloud Authentication
  slug: salesforce-sales-cloud-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Salesforce Sales Cloud Domain Security
  slug: salesforce-sales-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: salesforce-sales-cloud
tags:
- Cloud
- CRM
- Customer Management
- Enterprise
- Sales
website: https://www.salesforce.com/products/sales-cloud/
---
