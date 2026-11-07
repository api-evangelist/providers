---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 74.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 76
  human_in_the_loop: 0
  name: Doit Agentic Access
  operation_count: 168
  slug: doit-agentic-access
  summary_line: 168 operations · 76 acting
api_count: 1
apis:
- description: Official DoiT Model Context Protocol server. A remote Streamable HTTP endpoint at https://mcp.doit.com/mcp authenticated with OAuth 2.0 against console.doit.com, plus a local stdio server published to
  name: DoiT MCP Server
  slug: doit-mcp-server
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Find DoiT account managers assigned to your organization.
  name: DoiT Account Team API
  phrasing_intents:
  - id: listAccountTeam
    intent: See my assigned account managers
    question: Who are the account managers assigned to my organization at DoiT?
  phrasing_ops: 1
  slug: doit-accountteam-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Notifications triggered when cloud costs exceed defined thresholds or meet specific conditions.
  name: DoiT Alerts API
  phrasing_intents:
  - id: listAlerts
    intent: List cost alerts
    question: Which cost alerts have been set up in our account?
  - id: createAlert
    intent: Create a cost alert
    question: How do I get notified when cloud spend crosses a threshold?
  - id: getAlert
    intent: Retrieve an alert
    question: How do I see the settings of one alert?
  - id: deleteAlert
    intent: Delete an alert
    question: How do I remove an alert I no longer need?
  - id: updateAlert
    intent: Update an existing alert
    question: How do I change the threshold on an alert I already created?
  phrasing_ops: 5
  slug: doit-alerts-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Define how costs are distributed across your organization.
  name: DoiT Allocations API
  phrasing_intents:
  - id: listAllocations
    intent: List cost allocations
    question: What allocations are defined for splitting our cloud costs?
  - id: createAllocation
    intent: Create a cost allocation
    question: How do I group cloud costs by team or project with an allocation?
  - id: getAllocation
    intent: Retrieve an allocation
    question: How do I see the rules behind one allocation?
  - id: deleteAllocation
    intent: Delete an allocation
    question: How do I get rid of an allocation we stopped using?
  - id: updateAllocation
    intent: Update an existing allocation
    question: How do I change the rules of an allocation I already have?
  phrasing_ops: 5
  slug: doit-allocations-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Custom notes added to cost data to provide contextual information.
  name: DoiT Annotations API
  phrasing_intents:
  - id: listAnnotations
    intent: List annotations
    question: Which notes have been added to our cost reports?
  - id: createAnnotation
    intent: Add an annotation to reports
    question: How do I mark an event like a migration on my cost charts?
  - id: getAnnotation
    intent: Retrieve an annotation
    question: How do I read one annotation's text and timestamp?
  - id: deleteAnnotation
    intent: Delete an annotation
    question: How do I remove a note from my cost charts?
  - id: updateAnnotation
    intent: Edit an existing annotation
    question: How do I fix the text or time on an annotation already added?
  phrasing_ops: 5
  slug: doit-annotations-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Monitor cost spikes in your cloud environment.
  name: DoiT Anomalies API
  phrasing_intents:
  - id: listAnomalies
    intent: List cost anomalies
    question: Were there any cost anomalies detected recently?
  - id: getAnomaly
    intent: Retrieve a cost anomaly
    question: How do I see the full details of one spend anomaly?
  phrasing_ops: 2
  slug: doit-anomalies-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage cloud resources or services in your cloud environment.
  name: DoiT Assets API
  phrasing_intents:
  - id: createAsset
    intent: Create a billing asset
    question: How do I create a new account asset through DoiT?
  - id: idOfAssets
    intent: List billing assets
    question: Which billing accounts and subscriptions does DoiT manage for us?
  - id: getAsset
    intent: Retrieve an asset
    question: How do I see the full details of one asset?
  - id: idOfAsset
    intent: Change license count on a subscription
    question: How do I add or remove Workspace licenses?
  phrasing_ops: 4
  slug: doit-assets-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: User authentication.
  name: DoiT Auth API
  phrasing_intents:
  - id: validate
    intent: Check which user an API key belongs to
    question: How can I confirm which email and domain my API key is authenticated as?
  phrasing_ops: 1
  slug: doit-auth-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Interact with Ava, DoiT's AI-powered cloud assistant.
  name: DoiT Ava API
  phrasing_intents:
  - id: askAvaStreaming
    intent: Ask Ava with a streamed answer
    question: Can I stream Ava's answer as it is generated?
  - id: askAvaSync
    intent: Ask Ava and wait for the full answer
    question: How do I ask Ava a question and get one complete response back?
  - id: avaFeedback
    intent: Rate an Ava answer
    question: How do I tell DoiT whether an Ava answer was helpful?
  - id: deleteAvaConversation
    intent: Delete an Ava conversation
    question: How do I delete a conversation I had with Ava?
  phrasing_ops: 4
  slug: doit-ava-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage AWS billing-transfer mappings between distributors and resellers and between resellers and end customers, and list program management accounts.
  name: DoiT Billing Transfer API
  phrasing_intents:
  - id: createBillingTransferResellerHandshakes
    intent: Map resellers to a distributor PMA
    question: As a distributor, how do I map resellers for AWS billing transfer?
  - id: listBillingTransferProgramManagementAccounts
    intent: List program management accounts
    question: Which program management accounts do I have, and which resellers are under each?
  - id: createBillingTransferEndCustomerMappings
    intent: Map end-customer accounts to tenants
    question: As a reseller, how do I map end-customer AWS accounts to their DoiT tenant?
  - id: getBillingTransferProgramManagementAccountsStatus
    intent: Poll PMA IAM status
    question: Is the IAM setup on my program management accounts complete yet?
  - id: listBillingTransferEndCustomers
    intent: List end-customers by distributor and reseller PMA
    question: Which end-customer accounts are mapped under a reseller and distributor PMA pair?
  - id: listBillingTransferEndCustomersByReseller
    intent: List end-customers by reseller PMA only
    question: Can I list a reseller's end customers without knowing the distributor PMA?
  - id: listBillingTransferResellerAccounts
    intent: List my reseller PMA nodes
    question: Which reseller program management accounts do I own?
  - id: listBillingTransferResellerAccountsWithTenants
    intent: List reseller PMA nodes with tenants
    question: Can I see each reseller node together with its connected end-customer tenants?
  phrasing_ops: 8
  slug: doit-billing-transfer-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: AI-generated budget recommendations you can accept (link to a budget you created) or dismiss.
  name: DoiT Budget Suggestions API
  phrasing_intents:
  - id: listBudgetSuggestions
    intent: List AI budget suggestions
    question: Has DoiT suggested any budgets for us?
  - id: acceptBudgetSuggestion
    intent: Accept a budget suggestion
    question: How do I accept a suggested budget once I've created it?
  - id: dismissBudgetSuggestion
    intent: Dismiss a budget suggestion
    question: How do I hide a budget suggestion I don't want?
  phrasing_ops: 3
  slug: doit-budget-suggestions-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Track actual cloud spend against planned spend.
  name: DoiT Budgets API
  phrasing_intents:
  - id: listBudgets
    intent: List budgets
    question: What budgets do we have for cloud spend?
  - id: createBudget
    intent: Create a budget
    question: How do I set a monthly cloud spend budget?
  - id: getBudget
    intent: Check a budget's utilization
    question: How much of a budget have we used so far?
  - id: deleteBudget
    intent: Delete a budget
    question: How do I delete a budget we no longer track?
  - id: updateBudget
    intent: Update an existing budget
    question: How do I raise the amount on a budget I already have?
  phrasing_ops: 5
  slug: doit-budgets-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage cloud provider connections and check feature availability for connected accounts.
  name: DoiT Cloud Connect API
  phrasing_intents:
  - id: getCloudConnectSupportedFeatures
    intent: Check feature permissions for a connected account
    question: Which features are permitted for a cloud account connected to DoiT?
  - id: createAccountRole
    intent: Connect an AWS account role
    question: How do I connect an AWS account to DoiT with an IAM role?
  - id: getAwsAccount
    intent: Get a connected AWS account
    question: What role and S3 bucket is configured for a connected AWS account?
  - id: deleteAccountRole
    intent: Disconnect an AWS account role
    question: How do I disconnect an AWS account from DoiT?
  - id: updateAwsFeature
    intent: Change enabled features on an AWS account
    question: How do I enable more features on an already connected AWS account?
  phrasing_ops: 5
  slug: doit-cloud-connect-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Cloud Diagrams visualize your cloud infrastructure and resource relationships.
  name: DoiT Cloud Diagrams API
  phrasing_intents:
  - id: findCloudDiagrams
    intent: Find diagrams containing given resources
    question: Which cloud diagrams include a particular resource?
  - id: getCloudDiagramsStats
    intent: Get diagram activity stats for a period
    question: How active were our cloud diagrams over the last month?
  - id: getCloudDiagramComponents
    intent: Get diagrams and their components
    question: How do I pull the full component data for a diagram?
  - id: searchCloudDiagrams
    intent: Search diagrams and components by text
    question: Can I search across my diagrams for a component by name or property value?
  - id: getStatussheetComponents
    intent: Get specific components from a layer
    question: How do I fetch particular nodes or links from one diagram layer?
  - id: exportCloudDiagramJson
    intent: Export a diagram layer as JSON
    question: Can I export a whole diagram to JSON?
  - id: getCloudDiagramCostSnapshot
    intent: Get costs for a diagram layer
    question: How much did the infrastructure in a diagram cost over a date range?
  - id: listCloudDiagramLayerSnapshots
    intent: List saved snapshots of a layer
    question: What snapshots have been saved for a diagram layer?
  phrasing_ops: 12
  slug: doit-cloud-diagrams-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Service disruptions and outages from cloud providers.
  name: DoiT Cloud Incidents API
  phrasing_intents:
  - id: listKnownIssues
    intent: List cloud incidents
    question: Are there any active Google Cloud or Amazon Web Services incidents right now?
  - id: getKnownIssue
    intent: Retrieve a cloud incident
    question: How do I get the details of a specific cloud incident?
  phrasing_ops: 2
  slug: doit-cloud-incidents-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage CloudFlow.
  name: DoiT Cloud Flow API
  phrasing_intents:
  - id: triggerCloudflowWebhook
    intent: Trigger a webhook CloudFlow
    question: How do I start a published CloudFlow from an external system?
  - id: refineCloudFlow
    intent: Refine an existing CloudFlow with a prompt
    question: Can I change an existing CloudFlow by describing what I want in plain English?
  - id: buildCloudFlow
    intent: Build a new CloudFlow from a prompt
    question: Can I generate a brand new automation flow just by describing it?
  - id: listCloudflows
    intent: List CloudFlows
    question: What automation flows do we have in CloudFlow?
  - id: listCloudflowTemplates
    intent: List CloudFlow templates
    question: Which ready-made templates can I base a new flow on?
  - id: getCloudflowTemplate
    intent: Get one CloudFlow template
    question: What does a particular CloudFlow template do?
  phrasing_ops: 6
  slug: doit-cloudflow-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: View and manage commitment contracts with DoiT.
  name: DoiT Commitment Manager API
  phrasing_intents:
  - id: listCommitments
    intent: List cloud commitments
    question: What cloud commitments do we have tracked in DoiT?
  - id: getCommitment
    intent: Retrieve a commitment
    question: How do I see the details of a single commitment?
  phrasing_ops: 2
  slug: doit-commitment-manager-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage cloud provider connections used in CloudFlow workflows (AWS and GCP).
  name: DoiT Connections API
  phrasing_intents:
  - id: listCloudflowConnections
    intent: List cloud connections
    question: Which cloud provider connections are set up for CloudFlow?
  - id: createCloudflowConnection
    intent: Create a cloud connection
    question: How do I connect a cloud account for CloudFlow to use?
  - id: getCloudflowConnection
    intent: Retrieve a connection
    question: How do I see one connection's configuration?
  - id: updateCloudflowConnection
    intent: Update a connection
    question: How do I disable a connection without deleting it?
  - id: deleteCloudflowConnection
    intent: Delete a connection
    question: Why can't I delete a connection that flows still use?
  phrasing_ops: 5
  slug: doit-connections-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage contract templates for PartnerOps resellers (T1/T2).
  name: DoiT Contract Templates API
  phrasing_intents:
  - id: listContractTemplates
    intent: List contract templates
    question: Which contract templates does our tenant own?
  - id: createContractTemplate
    intent: Create a contract template
    question: How do I create a reusable contract template?
  - id: getContractTemplate
    intent: Retrieve a contract template
    question: How do I see the terms in one contract template?
  - id: updateContractTemplate
    intent: Update a contract template
    question: How do I change the eligibility dates on a template?
  - id: archiveContractTemplate
    intent: Archive a contract template
    question: Does archiving a template affect contracts already created from it?
  phrasing_ops: 5
  slug: doit-contract-templates-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: List and manage tenant-scoped contracts as a T1/T2 PartnerOps caller.
  name: DoiT Contracts API
  phrasing_intents:
  - id: listContracts
    intent: List a customer's contracts
    question: Which contracts does a given customer hold?
  - id: createContract
    intent: Create a draft contract
    question: How do I create a new draft contract for a customer?
  - id: getContract
    intent: Retrieve a contract
    question: How do I see the details of a specific customer contract?
  - id: updateContract
    intent: Save a new version of a contract
    question: How do I change the end date on an existing contract?
  - id: activateContract
    intent: Activate a draft contract
    question: How do I make a draft contract live?
  - id: cancelContract
    intent: Cancel a contract
    question: How do I end an active contract since it can't be deleted?
  phrasing_ops: 6
  slug: doit-contracts-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: View available dimensions for analysis.
  name: DoiT Dimensions API
  phrasing_intents:
  - id: getDimensions
    intent: Retrieve a dimension by type and key
    question: How do I look up one dimension by its type and key?
  - id: listDimensions
    intent: List dimensions
    question: Which dimensions can I use in Cloud Analytics?
  phrasing_ops: 2
  slug: doit-dimensions-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Organize Cloud Analytics resources (reports, allocations) into folders.
  name: DoiT Folders API
  phrasing_intents:
  - id: listFolders
    intent: List Cloud Analytics folders
    question: What folders do we have for organizing reports?
  - id: createFolder
    intent: Create a folder
    question: How do I make a folder to organize reports and allocations?
  - id: getFolder
    intent: Retrieve a folder
    question: How do I see one folder's details?
  - id: updateFolder
    intent: Rename or move a folder
    question: How do I rename an existing folder?
  - id: deleteFolder
    intent: Delete a folder
    question: What happens to reports when I delete their folder?
  phrasing_ops: 5
  slug: doit-folders-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage cloud insights representing recommendations and findings for cloud resources.
  name: DoiT Insights API
  phrasing_intents:
  - id: getInsightResults
    intent: List optimization insights
    question: What cost savings opportunities has DoiT found for us?
  - id: postInsightResults
    intent: Create or update insights in bulk
    question: Can I push many custom insights in a single request?
  - id: deleteInsightResults
    intent: Delete insights by key in bulk
    question: How do I remove every insight with a given key from my batch source?
  - id: getInsightResult
    intent: Retrieve one insight summary
    question: How do I see the savings summary for a single insight?
  - id: postInsightResult
    intent: Create or update a single insight
    question: How do I publish one custom insight for a source?
  - id: deleteInsightResult
    intent: Delete a single insight
    question: How do I permanently delete one insight I created via the API?
  - id: updateInsightStatus
    intent: Acknowledge or dismiss an insight
    question: How do I mark an insight as acknowledged or dismissed?
  - id: getInsightResourceResults
    intent: List affected resources for an insight
    question: Which individual cloud resources does an insight apply to?
  phrasing_ops: 9
  slug: doit-insights-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Access your current and historical billing documents.
  name: DoiT Invoices API
  phrasing_intents:
  - id: listInvoices
    intent: List invoices
    question: Where can I see all of our DoiT invoices?
  - id: getInvoice
    intent: Retrieve an invoice
    question: How do I get the full details of one invoice?
  phrasing_ops: 2
  slug: doit-invoices-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Create and manage labels to organize and categorize your cloud resources.
  name: DoiT Labels API
  phrasing_intents:
  - id: listLabels
    intent: List labels
    question: Which labels exist for organizing our reports?
  - id: createLabel
    intent: Create a label
    question: How do I create a colored label for tagging reports?
  - id: getLabel
    intent: Retrieve a label
    question: How do I see a single label's name and color?
  - id: deleteLabel
    intent: Delete a label
    question: How do I delete a label we no longer use?
  - id: updateLabel
    intent: Rename or recolor a label
    question: How do I rename an existing label?
  - id: getLabelAssignments
    intent: See what a label is assigned to
    question: Which reports and objects carry a particular label?
  - id: assignObjectsToLabel
    intent: Assign or unassign objects to a label
    question: How do I tag several reports with a label at once?
  phrasing_ops: 7
  slug: doit-labels-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Organizations help you segment data by your company or team structure.
  name: DoiT Organizations API
  phrasing_intents:
  - id: listOrganizations
    intent: List organizations
    question: Which organizations exist in my DoiT account?
  phrasing_ops: 1
  slug: doit-organizations-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: PerfectScale for Commitments (AWS) — commitment inventory, recommendations, and planned purchases.
  name: DoiT PerfectScale for Commitments AWS API
  phrasing_intents:
  - id: listAwsOrganizations
    intent: List AWS organizations with commitment stats
    question: Which AWS Organizations are onboarded for commitment management?
  - id: getAwsOrganization
    intent: Get an AWS organization overview
    question: How is commitment coverage trending for one AWS organization?
  - id: listAwsMemberAccounts
    intent: List member accounts in an organization
    question: Which member accounts in an organization have commitment coverage?
  - id: getAwsMemberAccount
    intent: Get a member account overview
    question: How is one member account doing on commitment savings?
  - id: listAwsSavingsPlans
    intent: List Savings Plans for an organization
    question: Which Savings Plans does an organization have?
  - id: listAwsReservedInstances
    intent: List Reserved Instances for an organization
    question: Which Reserved Instances does an organization hold?
  - id: listAwsRecommendations
    intent: List commitment purchase recommendations
    question: What commitments should an organization buy?
  - id: getAwsRecommendation
    intent: Get one service recommendation in detail
    question: What analysis backs the recommendation for a specific service?
  phrasing_ops: 10
  slug: doit-perfectscale-for-commitments-aws-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Metadata about supported cloud providers.
  name: DoiT Platforms API
  phrasing_intents:
  - id: listPlatforms
    intent: List support platforms
    question: Which platforms can I open a DoiT support request against?
  phrasing_ops: 1
  slug: doit-platforms-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Metadata about cloud services and offerings.
  name: DoiT Products API
  phrasing_intents:
  - id: listProducts
    intent: List support products for a platform
    question: Which products can I pick when filing a support request?
  phrasing_ops: 1
  slug: doit-products-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage Cloud Analytics reports and get reports data in JSON format.
  name: DoiT Reports API
  phrasing_intents:
  - id: listReports
    intent: List Cloud Analytics reports
    question: Which cost reports do I have access to?
  - id: createReport
    intent: Create and save a report
    question: How do I save a new cost report?
  - id: query
    intent: Run an ad hoc cost query
    question: Can I run a cost query without saving it as a report?
  - id: getReport
    intent: Get a report's results
    question: How do I get the numbers from a saved report?
  - id: deleteReport
    intent: Delete a report
    question: How do I delete a saved report?
  - id: updateReport
    intent: Update a saved report
    question: How do I change the configuration of an existing report?
  - id: getReportConfig
    intent: Get a report's configuration
    question: What settings and filters does a report use?
  phrasing_ops: 7
  slug: doit-reports-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage user permissions and access levels in your organization.
  name: DoiT Roles API
  phrasing_intents:
  - id: listRoles
    intent: List user roles
    question: What roles can I assign to users in DoiT?
  phrasing_ops: 1
  slug: doit-roles-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Monitor cloud service quota usage across connected accounts and projects.
  name: DoiT Service Quotas API
  phrasing_intents:
  - id: listServiceQuotas
    intent: Check cloud service quota usage
    question: How close am I to my cloud service quota limits?
  phrasing_ops: 1
  slug: doit-service-quotas-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: The Settings API from DoiT — 3 operation(s) for settings.
  name: DoiT Settings API
  phrasing_intents:
  - id: listCustomThemes
    intent: List custom color themes
    question: Which custom color themes are defined for our account?
  - id: createCustomTheme
    intent: Create a custom color theme
    question: How do I create a chart color theme in our brand colors?
  - id: getCustomTheme
    intent: Retrieve a custom theme
    question: How do I see the colors in one custom theme?
  - id: updateCustomTheme
    intent: Edit a custom theme
    question: How do I change the colors in an existing theme?
  - id: deleteCustomTheme
    intent: Delete a custom theme
    question: How do I delete a color theme we don't use?
  - id: getActiveTheme
    intent: See my active theme
    question: Which color theme am I currently using?
  - id: setActiveTheme
    intent: Switch my active theme
    question: How do I switch to a different color theme?
  phrasing_ops: 7
  slug: doit-settings-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage permissions associated with specified Cloud Analytics resources.
  name: DoiT Sharing API
  phrasing_intents:
  - id: getResourcePermission
    intent: See who can access a report, budget or alert
    question: Who has access to a particular Cloud Analytics report or budget?
  - id: updateResourcePermission
    intent: Change sharing on a Cloud Analytics resource
    question: How do I share a report or budget with my colleagues?
  phrasing_ops: 2
  slug: doit-sharing-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Create and manage support tickets with DoiT.
  name: DoiT Support Requests API
  phrasing_intents:
  - id: listTickets
    intent: List support requests
    question: What support tickets have we opened with DoiT?
  - id: createTicket
    intent: Open a support request
    question: How do I open a new support ticket?
  - id: getTicket
    intent: Get a support request
    question: How do I check the details of one support ticket?
  - id: updateTicket
    intent: Change a request's status or assignee
    question: How do I close or reopen a support ticket?
  - id: listTicketComments
    intent: Read comments on a request
    question: What replies have been posted on my ticket?
  - id: createTicketComment
    intent: Comment on a support request
    question: How do I reply to an open support ticket?
  - id: listTicketTags
    intent: List tags on a request
    question: Which tags are on a given support ticket?
  - id: addTicketTags
    intent: Add tags to a request
    question: How do I tag a support ticket?
  phrasing_ops: 9
  slug: doit-support-requests-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Browse the catalogue of read-only CloudFlow templates (blueprints) used to create flows.
  name: DoiT Templates API
  phrasing_intents:
  - id: listCloudflowTemplates
    intent: Browse CloudFlow templates
    question: What CloudFlow blueprints are available to start from?
  - id: getCloudflowTemplate
    intent: Retrieve a CloudFlow template
    question: How do I see what a specific CloudFlow blueprint contains?
  phrasing_ops: 2
  slug: doit-templates-api
- baseURL: https://api.doit.com
  baseurl_source: declared
  description: Manage users who have access to the DoiT platform.
  name: DoiT Users API
  phrasing_intents:
  - id: listUsers
    intent: List users in the organization
    question: Who has access to our DoiT organization, including pending invites?
  - id: deleteUser
    intent: Delete a user
    question: How do I remove someone from our organization?
  - id: updateUser
    intent: Update a user's profile or role
    question: How do I change a user's role?
  - id: inviteUser
    intent: Invite a new user
    question: How do I invite a teammate to DoiT?
  - id: resendInvite
    intent: Resend a pending invite
    question: How do I resend an invitation that expired?
  - id: cancelInvite
    intent: Cancel a pending invite
    question: How do I revoke an invitation that hasn't been accepted?
  phrasing_ops: 6
  slug: doit-users-api
- baseURL: https://mcp.doit.com/mcp
  baseurl_source: declared
  description: Explain month-over-month changes in invoiced cloud costs.
  name: DoiT Billing Explainer API
  slug: doit-billing-explainer-api
- baseURL: https://mcp.doit.com/mcp
  baseurl_source: declared
  description: Beta. Read-only access to Composer recipes and their results. A recipe evaluates your cloud resources against a set of conditions; each result is a finding on one affected resource, and published reci
  name: DoiT Composer Insights (Beta) API
  slug: doit-composer-insights-beta-api
- baseURL: https://mcp.doit.com/mcp
  baseurl_source: declared
  description: Manage explicit, named groups of downstream customers and the users scoped to them.
  name: DoiT Customer Groups API
  slug: doit-customer-groups-api
- baseURL: https://mcp.doit.com/mcp
  baseurl_source: declared
  description: Read and update your organization's general settings.
  name: DoiT Customers API
  slug: doit-customers-api
- baseURL: https://mcp.doit.com/mcp
  baseurl_source: declared
  description: Manage country-based access to tenants in your customer hierarchy.
  name: DoiT Geographic Access API
  slug: doit-geographic-access-api
- baseURL: https://mcp.doit.com/mcp
  baseurl_source: declared
  description: Evaluate current GCP commitments, plan and automate purchases, and optimize cloud costs with PerfectScale for Commitments.
  name: DoiT PerfectScale for Commitments GCP API
  slug: doit-perfectscale-for-commitments-gcp-api
- baseURL: https://mcp.doit.com/mcp
  baseurl_source: declared
  description: Cloud-agnostic PerfectScale for Commitments resources — commitment policies shared by AWS and GCP.
  name: DoiT PerfectScale for Commitments General API
  slug: doit-perfectscale-for-commitments-general-api
- baseURL: https://mcp.doit.com/mcp
  baseurl_source: declared
  description: Manage non-human identities whose API tokens call the DoiT API with a fixed set of permissions.
  name: DoiT Service Accounts API
  slug: doit-service-accounts-api
- baseURL: https://mcp.doit.com/mcp
  baseurl_source: declared
  description: Link and manage shared-payer account mappings for PartnerOps resellers (T2), reassigning AWS accounts under a shared payer to T3 end customers.
  name: DoiT Shared Payers API
  slug: doit-shared-payers-api
- baseURL: https://mcp.doit.com/mcp
  baseurl_source: declared
  description: 'Start a Cloud Intelligence trial for an organization that is not yet a DoiT customer. These operations require no API key: they are rate limited, idempotent, and provision nothing until the organizati'
  name: DoiT Signup API
  slug: doit-signup-api
- baseURL: https://mcp.doit.com/mcp
  baseurl_source: declared
  description: 'Beta. Read precomputed current-month cloud spend and forecast metrics. Widget results are refreshed in the background; reading a widget returns the latest cached result and never starts a synchronous '
  name: DoiT Widgets (Beta) API
  slug: doit-widgets-beta-api
- baseURL: https://mcp.doit.com/mcp
  baseurl_source: declared
  description: Ingest third-party cost, usage, and metric-based data for analysis.
  name: DoiT Data Hub API
  phrasing_intents:
  - id: datahubEventsCSVFile
    intent: Upload cost events from a CSV file
    question: Can I load custom cost data into DataHub from a CSV file?
  - id: datahubEvents
    intent: Send a batch of JSON events to DataHub
    question: How do I push custom billing events to DataHub as JSON?
  - id: deleteDatahubEventsByFilter
    intent: Delete specific DataHub events
    question: How do I remove bad events I sent to DataHub?
  - id: listDatahubDatasets
    intent: List DataHub datasets
    question: Which DataHub datasets do we have?
  - id: createDatahubDataset
    intent: Create a DataHub dataset
    question: How do I set up a new dataset for custom cost events?
  - id: deleteDatahubDatasets
    intent: Delete several datasets at once
    question: Can I delete multiple DataHub datasets in one call?
  - id: getDatahubDataset
    intent: Retrieve a dataset
    question: How do I see the details of one DataHub dataset?
  - id: deleteDatahubDataset
    intent: Delete a single dataset
    question: How do I delete just one DataHub dataset by name?
  phrasing_ops: 9
  slug: doit-data-hub-api
artifact_total: 65
asyncapis:
- description: ''
  name: Doit Events
  slug: doit-events
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/doitintl/doit-mcp-server/blob/main/LICENSE
- group: other
  href: https://artifacts.apis.io/doit/capabilities/doit-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/doit-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/doit/agentic-access/doit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/doit-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/doit/security/doit-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/doit-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/doit/security/doit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/doit-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/doit/security/doit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.doit.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.doit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.doit.com/docs/start
- group: docs
  title: ''
  type: APIReference
  url: https://developer.doit.com/reference/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.doit.com/docs/start
- group: operate
  title: ''
  type: Support
  url: https://help.doit.com/
- group: company
  title: ''
  type: Blog
  url: https://www.doit.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.doit.com/blog/feed
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/doitintl
- group: commercial
  title: ''
  type: Pricing
  url: https://www.doit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.doit.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doit.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.doit.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.doit.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.doit.com/changelog
- group: agent
  href: https://artifacts.apis.io/doit/llms/doit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doit-llms.txt
- group: build
  href: https://artifacts.apis.io/doit/packages/doit-packages.yml
  title: ''
  type: Packages
  url: packages/doit-packages.yml
- group: build
  href: https://artifacts.apis.io/doit/packages/doit-packages.yml
  title: ''
  type: SDKs
  url: packages/doit-packages.yml
- group: agent
  href: https://artifacts.apis.io/doit/well-known/doit-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doit-well-known.yml
- group: agent
  href: https://artifacts.apis.io/doit/mcp/doit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/doit-mcp.yml
- group: build
  href: https://artifacts.apis.io/doit/mcp/doit-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/doit-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/doit/overlays/doit-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/doit-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/doit/conformance/doit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doit-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.doit.com/
- group: design
  href: https://artifacts.apis.io/doit/errors/doit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/doit-problem-types.yml
- group: design
  href: https://artifacts.apis.io/doit/lifecycle/doit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/doit-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.doit.com/docs/availability-matrix
- group: auth
  href: https://artifacts.apis.io/doit/scopes/doit-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/doit-scopes.yml
- group: auth
  href: https://artifacts.apis.io/doit/authentication/doit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/doit-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://help.doit.com/docs/vendor-information/bug-bounty-program
- group: design
  href: https://artifacts.apis.io/doit/conventions/doit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/doit-conventions.yml
- group: design
  href: https://artifacts.apis.io/doit/conventions/doit-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/doit-conventions.yml
- group: operate
  href: https://artifacts.apis.io/doit/changelog/doit-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/doit-changelog.yml
- group: build
  href: https://artifacts.apis.io/doit/cli/doit-cli.yml
  title: ''
  type: CLI
  url: cli/doit-cli.yml
- group: design
  href: https://artifacts.apis.io/doit/data-model/doit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/doit-data-model.yml
- group: design
  href: https://artifacts.apis.io/doit/asyncapi/doit-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/doit-events.yml
- group: commercial
  href: https://artifacts.apis.io/doit/plans/doit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doit-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/doit/rate-limits/doit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/doit-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/doit/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/doit/skills/doit-mcp-setup.md
  title: ''
  type: AgentSkill
  url: skills/doit-mcp-setup.md
- group: agent
  href: https://artifacts.apis.io/doit/skills/doit-mcp-reporting.md
  title: ''
  type: AgentSkill
  url: skills/doit-mcp-reporting.md
- group: agent
  href: https://artifacts.apis.io/doit/skills/doit-mcp-anomaly-investigation.md
  title: ''
  type: AgentSkill
  url: skills/doit-mcp-anomaly-investigation.md
- group: agent
  href: https://artifacts.apis.io/doit/skills/doit-mcp-api.md
  title: ''
  type: AgentSkill
  url: skills/doit-mcp-api.md
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/doitintl
- group: docs
  href: https://artifacts.apis.io/doit/openapi/_original/doit-openapi-original.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/doit-openapi-original.yml
- group: operate
  title: ''
  type: ChangeLogRSS
  url: https://developer.doit.com/changelog.rss
created: '2026-08-12'
description: DoiT International is a cloud and FinOps technology company behind DoiT Cloud Intelligence, an intent-aware FinOps platform that unifies cost, usage and savings data across AWS, Google Cloud, Azure, Kubernetes and 40+ other clouds and SaaS providers. The DoiT Platform API at api.doit.com gives programmatic access to Cloud Analytics reports, allocations, budgets, alerts, anomalies, invoices, assets, DataHub ingestion, CloudFlow automation, cloud incidents, support requests, insights and its Ava AI assistant, published as a single OpenAPI 3.0.1 contract. DoiT also ships an official remote MCP server at mcp.doit.com, a generated dci CLI, a Terraform provider, a Grafana plugin, and an open-source Agent Skills plugin for agentic FinOps workflows.
finops:
- has_sources: true
  method: derived
  name: Doit Finops
  primary_unit: ''
  service_category: ''
  slug: doit-finops
  template: true
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.doit.com; 90 tools listed.
  name: DoiT MCP Server
  slug: doit
modified: '2026-09-16'
name: DoiT
nav: Providers
network: true
overview: 'DoiT publishes 49 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Team API, Alerts API, Allocations API, and 46 more. Tagged areas include Company, FinOps, Cloud Cost Management, Cloud Intelligence, and Cost Optimization.


  The DoiT catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  DoiT''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 46 more developer resources.'
plans:
- name: Doit Plans Pricing
  plan_count: 9
  slug: doit-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: Doit Rate Limits
  slug: doit-rate-limits
rules:
- authorship: generated
  effective_rule_count: 104
  extends:
  - spectral:oas
  name: DoiT API Rules
  rule_count: 63
  severity_counts:
    error: 43
    hint: 0
    info: 3
    warn: 17
  slug: doit-rules
scopes:
- name: Doit Scopes
  scope_count: 4
  slug: doit-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: exemplar
  composite: 72.3
  coverage:
    artifact_dirs: 31
    catalog_earned: 61.5
    catalog_earned_first_party: 20.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 63.5
    developer_ergonomics: 73.8
    discoverability: 75.0
    operational_transparency: 61.8
  previous_composite: 70.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 55.8
      total: 86
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 37.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/doit/doit-2026-08-17T080051.png
security:
- kind: authentication
  name: Doit Authentication
  slug: doit-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Doit Domain Security
  slug: doit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Doit Vulnerability Disclosure
  slug: doit-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Doit Trust Center
  slug: doit-trust-center
  summary_line: SOC 2 Type 2, SOC 3, ISO 27001, ISO 27001:2022, GDPR, CCPA, ICO registered, EU-US Data Privacy Framework
skill_count: 4
skills:
- name: doit-mcp-anomaly-investigation
  slug: doit-mcp-anomaly-investigation
- name: doit-mcp-api
  slug: doit-mcp-api
- name: doit-mcp-reporting
  slug: doit-mcp-reporting
- name: doit-mcp-setup
  slug: doit-mcp-setup
slug: doit
tags:
- Company
- FinOps
- Cloud Cost Management
- Cloud Intelligence
- Cost Optimization
- Multi-Cloud
- Kubernetes
- Analytics
- MCP
- Artificial Intelligence
website: https://www.doit.com/
---
