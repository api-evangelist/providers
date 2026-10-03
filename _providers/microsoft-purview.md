---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 96
  human_in_the_loop: 1
  name: Microsoft Purview Agentic Access
  operation_count: 174
  slug: microsoft-purview-agentic-access
  summary_line: 174 operations · 96 acting · 1 human-in-the-loop
api_count: 12
apis:
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing Purview accounts
  name: Microsoft Purview Accounts API
  phrasing_intents:
  - id: createOrUpdateAccount
    intent: Create or replace a Purview account
    question: How do I provision a new Microsoft Purview account in a resource group?
  - id: getAccount
    intent: Get a Purview account's details
    question: What are the current settings and SKU of my Purview account?
  - id: updateAccount
    intent: Patch tags or properties on a Purview account
    question: How do I change only the tags on an existing Purview account without recreating it?
  - id: deleteAccount
    intent: Delete a Purview account
    question: Can I permanently remove a Purview account I no longer use?
  - id: listAccountsByResourceGroup
    intent: List Purview accounts in a resource group
    question: Which Purview accounts live in a particular resource group?
  - id: listAccountsBySubscription
    intent: List Purview accounts across a subscription
    question: What Purview accounts exist anywhere in my Azure subscription?
  - id: listAccountKeys
    intent: Retrieve a Purview account's access keys
    question: Where do I get the Atlas Kafka endpoint keys for my Purview account?
  - id: addRootCollectionAdmin
    intent: Add an admin to the root collection
    question: How do I grant someone admin rights on a Purview account's root collection?
  phrasing_ops: 9
  slug: microsoft-purview-accounts-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for approving or rejecting workflow tasks
  name: Microsoft Purview Approval API
  phrasing_intents:
  - id: approveApproval
    intent: Approve a workflow approval task
    question: What's the way to approve a pending Purview workflow approval request?
  - id: rejectApproval
    intent: Reject a workflow approval task
    question: Is it possible to turn down an approval request in a Purview workflow?
  phrasing_ops: 2
  slug: microsoft-purview-approval-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing business domains
  name: Microsoft Purview Business Domains API
  phrasing_intents:
  - id: listBusinessDomains
    intent: List business domains in the unified catalog
    question: What business domains are defined in our Purview unified catalog?
  - id: createBusinessDomain
    intent: Create a business domain
    question: How do I set up a new business domain in the unified catalog?
  - id: getBusinessDomain
    intent: Get a business domain
    question: Who owns and stewards a specific business domain?
  - id: updateBusinessDomain
    intent: Update a business domain
    question: How do I rename or re-describe an existing business domain?
  - id: deleteBusinessDomain
    intent: Delete a business domain
    question: Can I remove a business domain we no longer need?
  phrasing_ops: 5
  slug: microsoft-purview-business-domains-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing eDiscovery cases
  name: Microsoft Purview Cases API
  phrasing_intents:
  - id: listEdiscoveryCases
    intent: List eDiscovery cases
    question: What eDiscovery cases are open in our organization?
  - id: createEdiscoveryCase
    intent: Open a new eDiscovery case
    question: How do I start a new eDiscovery case for a litigation matter?
  - id: getEdiscoveryCase
    intent: Get an eDiscovery case
    question: Where can I check the status and closing details of a single eDiscovery case?
  - id: updateEdiscoveryCase
    intent: Update an eDiscovery case
    question: How do I rename an eDiscovery case or change its description?
  - id: deleteEdiscoveryCase
    intent: Delete an eDiscovery case and its data
    question: Can I delete an eDiscovery case along with everything collected in it?
  phrasing_ops: 5
  slug: microsoft-purview-cases-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing classification rules
  name: Microsoft Purview Classification Rules API
  phrasing_intents:
  - id: createOrReplaceClassificationRule
    intent: Create or replace a classification rule
    question: How do I define a custom classification rule for scanning?
  - id: getClassificationRule
    intent: Get a classification rule
    question: How is a specific custom classification rule configured?
  - id: deleteClassificationRule
    intent: Delete a classification rule
    question: Can I remove a custom classification rule I no longer want applied?
  - id: listClassificationRules
    intent: List classification rules
    question: Which classification rules are defined in my Purview account?
  phrasing_ops: 4
  slug: microsoft-purview-classification-rules-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing critical data elements
  name: Microsoft Purview Critical Data Elements API
  phrasing_intents:
  - id: listCriticalDataElements
    intent: List critical data elements
    question: Which critical data elements are tracked in our unified catalog?
  - id: createCriticalDataElement
    intent: Define a critical data element
    question: How do I mark a new critical data element in the unified catalog?
  phrasing_ops: 2
  slug: microsoft-purview-critical-data-elements-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing custodians within cases
  name: Microsoft Purview Custodians API
  phrasing_intents:
  - id: listCustodians
    intent: List custodians in an eDiscovery case
    question: Who are the custodians attached to an eDiscovery case?
  - id: createCustodian
    intent: Add a custodian to an eDiscovery case
    question: How do I add a person as a custodian to an eDiscovery case?
  phrasing_ops: 2
  slug: microsoft-purview-custodians-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing data products
  name: Microsoft Purview Data Products API
  phrasing_intents:
  - id: listDataProducts
    intent: List data products
    question: What data products are published in our unified catalog?
  - id: createDataProduct
    intent: Create a data product
    question: How do I package data assets into a new data product?
  - id: getDataProduct
    intent: Get a data product
    question: Which data assets are included in a specific data product?
  - id: updateDataProduct
    intent: Update a data product
    question: How do I add assets to a data product that already exists?
  - id: deleteDataProduct
    intent: Delete a data product
    question: Can I retire a data product from the unified catalog?
  phrasing_ops: 5
  slug: microsoft-purview-data-products-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for data profiling operations
  name: Microsoft Purview Data Profiling API
  phrasing_intents:
  - id: runDataProfiling
    intent: Start profiling a data asset
    question: How do I kick off data profiling on a table?
  - id: getDataProfilingResult
    intent: Get profiling results for a data asset
    question: What did the last data profiling run find for an asset?
  phrasing_ops: 2
  slug: microsoft-purview-data-profiling-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing data quality rules
  name: Microsoft Purview Data Quality Rules API
  phrasing_intents:
  - id: listDataQualityRules
    intent: List data quality rules
    question: What data quality rules are configured in our Purview account?
  - id: createDataQualityRule
    intent: Create a data quality rule
    question: How do I add a rule that checks data assets for quality problems?
  - id: getDataQualityRule
    intent: Get a data quality rule
    question: What expression and targets does a particular data quality rule use?
  - id: updateDataQualityRule
    intent: Update a data quality rule
    question: How do I switch off an existing data quality rule without deleting it?
  - id: deleteDataQualityRule
    intent: Delete a data quality rule
    question: Can I delete a data quality rule that no longer applies?
  phrasing_ops: 5
  slug: microsoft-purview-data-quality-rules-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for running data quality scans
  name: Microsoft Purview Data Quality Scans API
  phrasing_intents:
  - id: runDataQualityScan
    intent: Run a data quality scan
    question: Can I evaluate data quality rules against my assets on demand?
  phrasing_ops: 1
  slug: microsoft-purview-data-quality-scans-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for retrieving data quality scores
  name: Microsoft Purview Data Quality Scores API
  phrasing_intents:
  - id: listDataQualityScores
    intent: List data quality scores
    question: What are the data quality scores across our data assets?
  - id: getDataQualityScore
    intent: Get a single data quality score
    question: Where can I look up the details of one data quality score record?
  phrasing_ops: 2
  slug: microsoft-purview-data-quality-scores-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing data source registrations
  name: Microsoft Purview Data Sources API
  phrasing_intents:
  - id: createOrReplaceDataSource
    intent: Register or replace a data source
    question: How do I register a new data source for Purview to scan?
  - id: getDataSource
    intent: Get a registered data source
    question: How is a specific data source registered in Purview?
  - id: deleteDataSource
    intent: Unregister a data source
    question: Can I remove a data source registration from Purview?
  - id: listDataSources
    intent: List registered data sources
    question: Which data sources are registered in our Purview data map?
  phrasing_ops: 4
  slug: microsoft-purview-data-sources-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for searching and discovering data assets
  name: Microsoft Purview Discovery API
  phrasing_intents:
  - id: searchQuery
    intent: Search the data catalog for assets
    question: How do I find data assets in Purview by keyword?
  - id: searchSuggest
    intent: Get search suggestions for a query
    question: Can Purview suggest matching assets while I type a search?
  - id: searchAutoComplete
    intent: Autocomplete a search term
    question: How do I get autocomplete options for a search box over the catalog?
  phrasing_ops: 3
  slug: microsoft-purview-discovery-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for evaluating DLP policies on content
  name: Microsoft Purview DLP Policies API
  phrasing_intents:
  - id: evaluateDlpApplication
    intent: Check which DLP policies apply to content
    question: Which data loss prevention policies would apply to this piece of content?
  - id: processContent
    intent: Run content through the DLP pipeline
    question: How do I have Purview enforce data loss prevention on content at runtime?
  phrasing_ops: 2
  slug: microsoft-purview-dlp-policies-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing catalog entities
  name: Microsoft Purview Entity API
  phrasing_intents:
  - id: createOrUpdateEntity
    intent: Create or update a single catalog entity
    question: How do I register one data asset in the Purview catalog?
  - id: getEntityByGuid
    intent: Get an entity's full definition
    question: How can I read everything Purview knows about one asset by its GUID?
  - id: deleteEntityByGuid
    intent: Delete one entity by GUID
    question: Can I remove a single asset from the catalog using its GUID?
  - id: listEntitiesByGuids
    intent: Fetch several entities by their GUIDs
    question: Can I retrieve many assets in one call when I have a list of GUIDs?
  - id: bulkCreateOrUpdateEntities
    intent: Create or update many entities at once
    question: How do I load a batch of assets into the catalog in one request?
  - id: bulkDeleteEntities
    intent: Delete many entities at once
    question: Can I delete a whole list of assets in one call?
  - id: getEntityClassification
    intent: Get one classification on an entity
    question: Does a given asset carry a specific classification?
  - id: removeEntityClassification
    intent: Remove a classification from an entity
    question: How do I take a wrong classification off an asset?
  phrasing_ops: 19
  slug: microsoft-purview-entity-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing glossary terms, categories, and assignments
  name: Microsoft Purview Glossary API
  phrasing_intents:
  - id: listGlossaries
    intent: List all glossaries
    question: What business glossaries exist in our Purview catalog?
  - id: createGlossary
    intent: Create a glossary
    question: How do I start a new business glossary?
  - id: getGlossary
    intent: Get a glossary
    question: Where can I see the details of one glossary by its GUID?
  - id: updateGlossary
    intent: Update a glossary
    question: How do I rename a glossary or change its description?
  - id: deleteGlossary
    intent: Delete a glossary with its terms
    question: Does deleting a glossary also remove its terms and categories?
  - id: listGlossaryTerms
    intent: List the terms in a glossary
    question: What terms belong to a particular glossary?
  - id: listGlossaryCategories
    intent: List the categories in a glossary
    question: What categories organise the terms in a glossary?
  - id: createGlossaryTerm
    intent: Create a glossary term
    question: How do I add a single business term to a glossary?
  phrasing_ops: 19
  slug: microsoft-purview-glossary-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing glossary terms in the unified catalog
  name: Microsoft Purview Glossary Terms API
  phrasing_intents:
  - id: listUnifiedGlossaryTerms
    intent: List glossary terms in the unified catalog
    question: What glossary terms are defined in the Purview unified catalog?
  phrasing_ops: 1
  slug: microsoft-purview-glossary-terms-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing label policy settings
  name: Microsoft Purview Label Policy Settings API
  phrasing_intents:
  - id: getLabelPolicySettings
    intent: Read information protection label policy settings
    question: What label policy settings apply to our organization?
  phrasing_ops: 1
  slug: microsoft-purview-label-policy-settings-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing legal holds
  name: Microsoft Purview Legal Holds API
  phrasing_intents:
  - id: listLegalHolds
    intent: List legal holds in an eDiscovery case
    question: What legal holds are in place for an eDiscovery case?
  - id: createLegalHold
    intent: Place a legal hold in an eDiscovery case
    question: How do I put content on legal hold for a case?
  phrasing_ops: 2
  slug: microsoft-purview-legal-holds-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for tracking data lineage
  name: Microsoft Purview Lineage API
  phrasing_intents:
  - id: getLineageByGuid
    intent: Get lineage for an entity
    question: Where does the data in a given asset come from and where does it flow?
  - id: getLineageNextPage
    intent: Page through lineage for an entity
    question: How do I fetch the next page of lineage when an asset has many neighbours?
  - id: lineageGetByUniqueAttribute
    intent: Get lineage by type and unique attribute
    question: Can I look up lineage using an asset's type and qualified name instead of its GUID?
  phrasing_ops: 3
  slug: microsoft-purview-lineage-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing metadata policies
  name: Microsoft Purview Metadata Policy API
  phrasing_intents:
  - id: getMetadataPolicy
    intent: Get a metadata policy
    question: Who has which role on a collection according to its metadata policy?
  - id: updateMetadataPolicy
    intent: Update a metadata policy
    question: How do I change role assignments in a collection's metadata policy?
  - id: listAllMetadataPolicies
    intent: List metadata policies
    question: What metadata policies govern access across our Purview collections?
  phrasing_ops: 3
  slug: microsoft-purview-metadata-policy-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing metadata roles
  name: Microsoft Purview Metadata Roles API
  phrasing_intents:
  - id: listMetadataRoles
    intent: List metadata roles
    question: Which metadata roles can be assigned in our Purview account?
  phrasing_ops: 1
  slug: microsoft-purview-metadata-roles-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing Objectives and Key Results
  name: Microsoft Purview OKRs API
  phrasing_intents:
  - id: listOKRs
    intent: List OKRs in the unified catalog
    question: What objectives and key results are tracked in our unified catalog?
  - id: createOKR
    intent: Create an objective or key result
    question: How do I add a new objective to a business domain?
  phrasing_ops: 2
  slug: microsoft-purview-okrs-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations available on the Purview resource provider
  name: Microsoft Purview Operations API
  phrasing_intents:
  - id: listOperations
    intent: List Purview resource provider operations
    question: Which management operations does the Purview resource provider expose?
  phrasing_ops: 1
  slug: microsoft-purview-operations-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing private endpoint connections
  name: Microsoft Purview Private Endpoint Connections API
  phrasing_intents:
  - id: listPrivateEndpointConnections
    intent: List a Purview account's private endpoints
    question: Which private endpoint connections are attached to my Purview account?
  - id: getPrivateEndpointConnection
    intent: Get one private endpoint connection
    question: What is the approval state of a specific private endpoint connection?
  phrasing_ops: 2
  slug: microsoft-purview-private-endpoint-connections-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for computing protection scopes
  name: Microsoft Purview Protection Scopes API
  phrasing_intents:
  - id: computeProtectionScopes
    intent: Compute protection scopes for content
    question: Which DLP policies should my app enforce for a given user and activity?
  phrasing_ops: 1
  slug: microsoft-purview-protection-scopes-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing relationships between entities
  name: Microsoft Purview Relationship API
  phrasing_intents:
  - id: createRelationship
    intent: Create a relationship between entities
    question: How do I link two assets with a typed relationship?
  - id: updateRelationship
    intent: Update a relationship between entities
    question: How do I change the attributes of an existing relationship between assets?
  - id: getRelationship
    intent: Get a relationship
    question: What are the two ends of a given relationship?
  - id: deleteRelationship
    intent: Delete a relationship
    question: Can I remove the link between two assets?
  phrasing_ops: 4
  slug: microsoft-purview-relationship-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing retention event types
  name: Microsoft Purview Retention Event Types API
  phrasing_intents:
  - id: listRetentionEventTypes
    intent: List retention event types
    question: What retention event types are defined for event-based retention?
  - id: createRetentionEventType
    intent: Create a retention event type
    question: How do I define a new type of event that starts a retention period?
  - id: getRetentionEventType
    intent: Get a retention event type
    question: Where can I see one retention event type's details?
  - id: updateRetentionEventType
    intent: Update a retention event type
    question: How do I rename a retention event type?
  - id: deleteRetentionEventType
    intent: Delete a retention event type
    question: Can I remove a retention event type that is no longer used?
  phrasing_ops: 5
  slug: microsoft-purview-retention-event-types-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing retention events
  name: Microsoft Purview Retention Events API
  phrasing_intents:
  - id: listRetentionEvents
    intent: List retention events
    question: Which retention events have been triggered so far?
  - id: createRetentionEvent
    intent: Trigger a retention event
    question: How do I start event-based retention when something happens, like an employee leaving?
  - id: getRetentionEvent
    intent: Get a retention event
    question: What is the status of a retention event I triggered?
  - id: deleteRetentionEvent
    intent: Delete a retention event
    question: Can I delete a retention event that was triggered by mistake?
  phrasing_ops: 4
  slug: microsoft-purview-retention-events-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing retention labels
  name: Microsoft Purview Retention Labels API
  phrasing_intents:
  - id: listRetentionLabels
    intent: List retention labels
    question: What retention labels are configured in our organization?
  - id: createRetentionLabel
    intent: Create a retention label
    question: How do I create a label that keeps content for a set period?
  - id: getRetentionLabel
    intent: Get a retention label
    question: How long does a specific retention label keep content?
  - id: updateRetentionLabel
    intent: Update a retention label
    question: How do I change the retention period on an existing label?
  - id: deleteRetentionLabel
    intent: Delete a retention label
    question: Can I delete a retention label that is no longer needed?
  phrasing_ops: 5
  slug: microsoft-purview-retention-labels-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing review sets
  name: Microsoft Purview Review Sets API
  phrasing_intents:
  - id: listReviewSets
    intent: List review sets in an eDiscovery case
    question: What review sets have been created in an eDiscovery case?
  - id: createReviewSet
    intent: Create a review set in an eDiscovery case
    question: How do I create a review set to examine collected evidence?
  phrasing_ops: 2
  slug: microsoft-purview-review-sets-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for running scans and viewing scan results
  name: Microsoft Purview Scan Result API
  phrasing_intents:
  - id: runScan
    intent: Run a scan on a data source
    question: How do I start a scan of a data source right now?
  - id: cancelScan
    intent: Cancel a running scan
    question: How do I stop a scan that is taking too long?
  - id: listScanHistory
    intent: List a scan's run history
    question: When did a scan last run and did it succeed?
  phrasing_ops: 3
  slug: microsoft-purview-scan-result-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing scan rulesets
  name: Microsoft Purview Scan Rulesets API
  phrasing_intents:
  - id: createOrReplaceScanRuleset
    intent: Create or replace a scan rule set
    question: How do I create a custom scan rule set?
  - id: getScanRuleset
    intent: Get a scan rule set
    question: Which file types and classifications does a scan rule set include?
  - id: deleteScanRuleset
    intent: Delete a scan rule set
    question: Can I delete a custom scan rule set?
  - id: listScanRulesets
    intent: List scan rule sets
    question: Which scan rule sets are available in my account?
  phrasing_ops: 4
  slug: microsoft-purview-scan-rulesets-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing scan configurations
  name: Microsoft Purview Scans API
  phrasing_intents:
  - id: createOrReplaceScan
    intent: Create or replace a scan
    question: How do I set up a new scan for a registered data source?
  - id: getScan
    intent: Get a scan definition
    question: How is a particular scan of a data source configured?
  - id: deleteScan
    intent: Delete a scan
    question: Can I delete a scan from a data source?
  - id: listScansByDataSource
    intent: List scans on a data source
    question: What scans are configured for a given data source?
  phrasing_ops: 4
  slug: microsoft-purview-scans-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing eDiscovery searches
  name: Microsoft Purview Searches API
  phrasing_intents:
  - id: listEdiscoverySearches
    intent: List searches in an eDiscovery case
    question: What searches have been run inside an eDiscovery case?
  - id: createEdiscoverySearch
    intent: Create a search in an eDiscovery case
    question: How do I search mailboxes and sites for evidence within a case?
  phrasing_ops: 2
  slug: microsoft-purview-searches-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for accessing tenant-level sensitivity labels
  name: Microsoft Purview Sensitivity Labels API
  phrasing_intents:
  - id: listTenantSensitivityLabels
    intent: List sensitivity labels for the whole tenant
    question: Which sensitivity labels exist across our entire tenant?
  - id: getTenantSensitivityLabel
    intent: Get a tenant-level sensitivity label
    question: Where can I read a sensitivity label's tenant-level definition?
  - id: listSensitivityLabels
    intent: List information protection sensitivity labels
    question: What sensitivity labels are available to the organization under information protection?
  - id: getSensitivityLabel
    intent: Get an information protection sensitivity label
    question: What are the settings of one information protection label?
  - id: listUserSensitivityLabels
    intent: List sensitivity labels available to a user
    question: Which sensitivity labels can a specific user apply?
  - id: listMySensitivityLabels
    intent: List my own sensitivity labels
    question: Which sensitivity labels am I allowed to apply?
  - id: evaluateApplication
    intent: Work out which sensitivity label to apply
    question: Which sensitivity label should be applied to a document, and what actions follow?
  - id: evaluateRemoval
    intent: Work out how to remove a sensitivity label
    question: What has to happen to strip a sensitivity label from a file?
  phrasing_ops: 10
  slug: microsoft-purview-sensitivity-labels-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing scan triggers and schedules
  name: Microsoft Purview Triggers API
  phrasing_intents:
  - id: createOrReplaceTrigger
    intent: Schedule a scan with a trigger
    question: How do I schedule a scan to run on a recurrence?
  - id: getTrigger
    intent: Get a scan's schedule trigger
    question: When is a scan scheduled to run?
  - id: deleteTrigger
    intent: Delete a scan's schedule trigger
    question: Can I remove the recurring schedule from a scan?
  - id: enableTrigger
    intent: Enable a scan schedule
    question: How do I turn a paused scan schedule back on?
  - id: disableTrigger
    intent: Disable a scan schedule
    question: How do I pause scheduled scanning without deleting the schedule?
  phrasing_ops: 5
  slug: microsoft-purview-triggers-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing type definitions
  name: Microsoft Purview Type API
  phrasing_intents:
  - id: listTypeDefinitions
    intent: List all type definitions
    question: What entity, classification and relationship types are defined in the catalog?
  - id: bulkCreateTypeDefinitions
    intent: Create type definitions in bulk
    question: How do I define custom entity types for the catalog?
  - id: bulkUpdateTypeDefinitions
    intent: Update type definitions in bulk
    question: How do I change several existing type definitions at once?
  - id: bulkDeleteTypeDefinitions
    intent: Delete type definitions in bulk
    question: Can I delete several custom type definitions at once?
  - id: listTypeDefinitionHeaders
    intent: List type definition headers
    question: Is there a lightweight list of type names and categories?
  - id: getTypeDefinitionByGuid
    intent: Get a type definition by GUID
    question: How do I look up a type definition when I only have its GUID?
  - id: getTypeDefinitionByName
    intent: Get a type definition by name
    question: What attributes does a named type like azure_sql_table have?
  - id: deleteTypeDefinitionByName
    intent: Delete a type definition by name
    question: Can I delete one custom type by its name?
  phrasing_ops: 8
  slug: microsoft-purview-type-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for submitting user requests
  name: Microsoft Purview User Requests API
  phrasing_intents:
  - id: submitUserRequest
    intent: Submit a user request that triggers a workflow
    question: What's the way to submit a request that kicks off a Purview workflow?
  phrasing_ops: 1
  slug: microsoft-purview-user-requests-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing individual workflows
  name: Microsoft Purview Workflow API
  phrasing_intents:
  - id: createOrReplaceWorkflow
    intent: Create or replace a workflow
    question: How do I create an approval workflow in Purview?
  - id: getWorkflow
    intent: Get a workflow definition
    question: What triggers and actions are in a specific Purview workflow?
  - id: deleteWorkflow
    intent: Delete a workflow
    question: Can I remove a workflow that is no longer used?
  - id: validateWorkflow
    intent: Validate a workflow definition
    question: How can I check a workflow definition for errors before saving it?
  phrasing_ops: 4
  slug: microsoft-purview-workflow-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing workflow runs
  name: Microsoft Purview Workflow Run API
  phrasing_intents:
  - id: getWorkflowRun
    intent: Get a workflow run
    question: What is the status of a particular workflow run?
  - id: cancelWorkflowRun
    intent: Cancel a running workflow
    question: How do I stop a workflow run that is in progress?
  phrasing_ops: 2
  slug: microsoft-purview-workflow-run-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for managing workflow tasks
  name: Microsoft Purview Workflow Task API
  phrasing_intents:
  - id: getWorkflowTask
    intent: Get a workflow task
    question: Who is assigned to a specific workflow task?
  - id: reassignWorkflowTask
    intent: Reassign a workflow task
    question: How do I hand a workflow task over to a different person?
  phrasing_ops: 2
  slug: microsoft-purview-workflow-task-api
- baseURL: https://{account-name}.purview.azure.com
  baseurl_source: declared
  description: Operations for listing workflows
  name: Microsoft Purview Workflows API
  phrasing_intents:
  - id: listWorkflows
    intent: List all workflows
    question: What workflows are defined in our Purview account?
  phrasing_ops: 1
  slug: microsoft-purview-workflows-api
arazzos:
- description: Create a glossary term and assign it to one or more catalog entities.
  name: Microsoft Purview Assign a Glossary Term to Entities
  slug: microsoft-purview-assign-term-to-entities-workflow
- description: Create a glossary category and a term that is filed under that category.
  name: Microsoft Purview Categorize a Glossary Term
  slug: microsoft-purview-categorize-glossary-term-workflow
- description: Register a catalog entity, confirm it, then apply and verify a classification.
  name: Microsoft Purview Classify a Data Asset Entity
  slug: microsoft-purview-classify-entity-workflow
- description: Register a custom classification typedef, confirm it, then classify an entity with it.
  name: Microsoft Purview Define a Classification Type and Apply It
  slug: microsoft-purview-define-and-apply-classification-type-workflow
- description: Create a data quality rule, confirm it, then run a quality scan that evaluates it.
  name: Microsoft Purview Define a Data Quality Rule and Scan
  slug: microsoft-purview-define-rule-and-scan-quality-workflow
- description: Search the catalog, then move the discovered entities into a target collection.
  name: Microsoft Purview Move Found Entities into a Collection
  slug: microsoft-purview-move-entities-to-collection-workflow
- description: Create a Data Map entity, confirm it, move it into a collection, and classify it.
  name: Microsoft Purview Onboard an Entity into a Collection
  slug: microsoft-purview-onboard-entity-to-collection-workflow
- description: Kick off data profiling for an asset, then poll until the profiling completes.
  name: Microsoft Purview Profile a Data Asset and Poll for Results
  slug: microsoft-purview-profile-asset-and-poll-workflow
- description: Create a custom classification rule, build a scan ruleset that uses it, and confirm.
  name: Microsoft Purview Provision a Custom Scan Ruleset
  slug: microsoft-purview-provision-scan-ruleset-workflow
- description: Create a business domain, confirm it, then publish a data product under it.
  name: Microsoft Purview Publish a Data Product
  slug: microsoft-purview-publish-data-product-workflow
- description: Create a glossary, confirm it, then create a term anchored to that glossary.
  name: Microsoft Purview Publish a Glossary Term
  slug: microsoft-purview-publish-glossary-term-workflow
- description: Register a data source, configure a scan, and kick off a scan run.
  name: Microsoft Purview Register a Data Source and Launch a Scan
  slug: microsoft-purview-register-source-and-scan-workflow
- description: Create an entity, then create a relationship linking it to another entity.
  name: Microsoft Purview Relate Two Catalog Entities
  slug: microsoft-purview-relate-entities-workflow
- description: Launch a scan run, then poll scan history until the run reaches a terminal state.
  name: Microsoft Purview Run a Scan and Poll to Completion
  slug: microsoft-purview-run-and-poll-scan-workflow
- description: Configure a scan, attach a recurring trigger, enable it, and confirm the schedule.
  name: Microsoft Purview Schedule a Recurring Scan
  slug: microsoft-purview-schedule-recurring-scan-workflow
- description: Search the catalog, read the top hit, and apply a classification to it.
  name: Microsoft Purview Search and Classify a Found Asset
  slug: microsoft-purview-search-and-classify-workflow
- description: Search for an asset, read its entity, then walk its lineage graph with pagination.
  name: Microsoft Purview Trace Data Asset Lineage
  slug: microsoft-purview-trace-asset-lineage-workflow
artifact_total: 279
collections:
- collection_type: postman
  name: Microsoft Purview Account API
  slug: postman-microsoft-purview-account
- collection_type: postman
  name: Microsoft Purview Catalog API
  slug: postman-microsoft-purview-catalog
- collection_type: postman
  name: Microsoft Purview Data Map API
  slug: postman-microsoft-purview-data-map
- collection_type: postman
  name: Microsoft Purview Data Quality API
  slug: postman-microsoft-purview-data-quality
- collection_type: postman
  name: Microsoft Purview Data Security and Governance API
  slug: postman-microsoft-purview-data-security-governance
- collection_type: postman
  name: Microsoft Purview eDiscovery API
  slug: postman-microsoft-purview-ediscovery
- collection_type: postman
  name: Microsoft Purview Information Protection API
  slug: postman-microsoft-purview-information-protection
- collection_type: postman
  name: Microsoft Purview Metadata Policies API
  slug: postman-microsoft-purview-metadata-policies
- collection_type: postman
  name: Microsoft Purview Records Management API
  slug: postman-microsoft-purview-records-management
- collection_type: postman
  name: Microsoft Purview Scanning API
  slug: postman-microsoft-purview-scanning
- collection_type: postman
  name: Microsoft Purview Unified Catalog API
  slug: postman-microsoft-purview-unified-catalog
- collection_type: postman
  name: Microsoft Purview Workflow API
  slug: postman-microsoft-purview-workflow
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Purview Account API
  slug: open-microsoft-purview-account
- collection_type: open
  name: Microsoft Purview Account Accounts API
  slug: open-microsoft-purview-accounts-api
- collection_type: open
  name: Microsoft Purview Account Accounts Approval API
  slug: open-microsoft-purview-approval-api
- collection_type: open
  name: Microsoft Purview Account Accounts Business Domains API
  slug: open-microsoft-purview-business-domains-api
- collection_type: open
  name: Microsoft Purview Account Accounts Cases API
  slug: open-microsoft-purview-cases-api
- collection_type: open
  name: Microsoft Purview Catalog API
  slug: open-microsoft-purview-catalog
- collection_type: open
  name: Microsoft Purview Account Accounts Classification Rules API
  slug: open-microsoft-purview-classification-rules-api
- collection_type: open
  name: Microsoft Purview Account Accounts Critical Data Elements API
  slug: open-microsoft-purview-critical-data-elements-api
- collection_type: open
  name: Microsoft Purview Account Accounts Custodians API
  slug: open-microsoft-purview-custodians-api
- collection_type: open
  name: Microsoft Purview Data Map API
  slug: open-microsoft-purview-data-map
- collection_type: open
  name: Microsoft Purview Account Accounts Data Products API
  slug: open-microsoft-purview-data-products-api
- collection_type: open
  name: Microsoft Purview Account Accounts Data Profiling API
  slug: open-microsoft-purview-data-profiling-api
- collection_type: open
  name: Microsoft Purview Account Accounts Data Quality Rules API
  slug: open-microsoft-purview-data-quality-rules-api
- collection_type: open
  name: Microsoft Purview Account Accounts Data Quality Scans API
  slug: open-microsoft-purview-data-quality-scans-api
- collection_type: open
  name: Microsoft Purview Account Accounts Data Quality Scores API
  slug: open-microsoft-purview-data-quality-scores-api
- collection_type: open
  name: Microsoft Purview Data Quality API
  slug: open-microsoft-purview-data-quality
- collection_type: open
  name: Microsoft Purview Data Security and Governance API
  slug: open-microsoft-purview-data-security-governance
- collection_type: open
  name: Microsoft Purview Account Accounts Data Sources API
  slug: open-microsoft-purview-data-sources-api
- collection_type: open
  name: Microsoft Purview Account Accounts Discovery API
  slug: open-microsoft-purview-discovery-api
- collection_type: open
  name: Microsoft Purview Account Accounts DLP Policies API
  slug: open-microsoft-purview-dlp-policies-api
- collection_type: open
  name: Microsoft Purview eDiscovery API
  slug: open-microsoft-purview-ediscovery
- collection_type: open
  name: Microsoft Purview Account Accounts Entity API
  slug: open-microsoft-purview-entity-api
- collection_type: open
  name: Microsoft Purview Account Accounts Glossary API
  slug: open-microsoft-purview-glossary-api
- collection_type: open
  name: Microsoft Purview Account Accounts Glossary Terms API
  slug: open-microsoft-purview-glossary-terms-api
- collection_type: open
  name: Microsoft Purview Information Protection API
  slug: open-microsoft-purview-information-protection
- collection_type: open
  name: Microsoft Purview Account Accounts Label Policy Settings API
  slug: open-microsoft-purview-label-policy-settings-api
- collection_type: open
  name: Microsoft Purview Account Accounts Legal Holds API
  slug: open-microsoft-purview-legal-holds-api
- collection_type: open
  name: Microsoft Purview Account Accounts Lineage API
  slug: open-microsoft-purview-lineage-api
- collection_type: open
  name: Microsoft Purview Metadata Policies API
  slug: open-microsoft-purview-metadata-policies
- collection_type: open
  name: Microsoft Purview Account Accounts Metadata Policy API
  slug: open-microsoft-purview-metadata-policy-api
- collection_type: open
  name: Microsoft Purview Account Accounts Metadata Roles API
  slug: open-microsoft-purview-metadata-roles-api
- collection_type: open
  name: Microsoft Purview Account Accounts OKRs API
  slug: open-microsoft-purview-okrs-api
- collection_type: open
  name: Microsoft Purview Account Accounts Operations API
  slug: open-microsoft-purview-operations-api
- collection_type: open
  name: Microsoft Purview Account Accounts Private Endpoint Connections API
  slug: open-microsoft-purview-private-endpoint-connections-api
- collection_type: open
  name: Microsoft Purview Account Accounts Protection Scopes API
  slug: open-microsoft-purview-protection-scopes-api
- collection_type: open
  name: Microsoft Purview Records Management API
  slug: open-microsoft-purview-records-management
- collection_type: open
  name: Microsoft Purview Account Accounts Relationship API
  slug: open-microsoft-purview-relationship-api
- collection_type: open
  name: Microsoft Purview Account Accounts Retention Event Types API
  slug: open-microsoft-purview-retention-event-types-api
- collection_type: open
  name: Microsoft Purview Account Accounts Retention Events API
  slug: open-microsoft-purview-retention-events-api
- collection_type: open
  name: Microsoft Purview Account Accounts Retention Labels API
  slug: open-microsoft-purview-retention-labels-api
- collection_type: open
  name: Microsoft Purview Account Accounts Scan Result API
  slug: open-microsoft-purview-scan-result-api
- collection_type: open
  name: Microsoft Purview Account Accounts Scan Rulesets API
  slug: open-microsoft-purview-scan-rulesets-api
- collection_type: open
  name: Microsoft Purview Scanning API
  slug: open-microsoft-purview-scanning
- collection_type: open
  name: Microsoft Purview Account Accounts Scans API
  slug: open-microsoft-purview-scans-api
- collection_type: open
  name: Microsoft Purview Account Accounts Searches API
  slug: open-microsoft-purview-searches-api
- collection_type: open
  name: Microsoft Purview Account Accounts Sensitivity Labels API
  slug: open-microsoft-purview-sensitivity-labels-api
- collection_type: open
  name: Microsoft Purview Account Accounts Triggers API
  slug: open-microsoft-purview-triggers-api
- collection_type: open
  name: Microsoft Purview Account Accounts Type API
  slug: open-microsoft-purview-type-api
- collection_type: open
  name: Microsoft Purview Unified Catalog API
  slug: open-microsoft-purview-unified-catalog
- collection_type: open
  name: Microsoft Purview Account Accounts User Requests API
  slug: open-microsoft-purview-user-requests-api
- collection_type: open
  name: Microsoft Purview Account Accounts Workflow API
  slug: open-microsoft-purview-workflow-api
- collection_type: open
  name: Microsoft Purview Account Accounts Workflow Run API
  slug: open-microsoft-purview-workflow-run-api
- collection_type: open
  name: Microsoft Purview Account Accounts Workflow Task API
  slug: open-microsoft-purview-workflow-task-api
- collection_type: open
  name: Microsoft Purview Workflow API
  slug: open-microsoft-purview-workflow
- collection_type: open
  name: Microsoft Purview Account Accounts Workflows API
  slug: open-microsoft-purview-workflows-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/plans/microsoft-purview-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-purview-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/capabilities/microsoft-purview-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-purview-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/agentic-access/microsoft-purview-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-purview-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/security/microsoft-purview-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-purview-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/security/microsoft-purview-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-purview-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/authentication/microsoft-purview-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-purview-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/scopes/microsoft-purview-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-purview-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/packages/microsoft-purview-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-purview-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/well-known/microsoft-purview-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-purview-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/mcp/microsoft-purview-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-purview-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/llms/microsoft-purview-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-purview-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/conformance/microsoft-purview-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-purview-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/errors/microsoft-purview-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-purview-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/lifecycle/microsoft-purview-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-purview-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/conventions/microsoft-purview-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-purview-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/data-model/microsoft-purview-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-purview-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/cli/microsoft-purview-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-purview-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/changelog/microsoft-purview-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-purview-changelog.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/overlays/microsoft-purview-account-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-account-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/overlays/microsoft-purview-catalog-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-catalog-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/overlays/microsoft-purview-data-map-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-data-map-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/overlays/microsoft-purview-data-quality-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-data-quality-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/overlays/microsoft-purview-data-security-governance-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-data-security-governance-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/overlays/microsoft-purview-ediscovery-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-ediscovery-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/overlays/microsoft-purview-information-protection-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-information-protection-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/overlays/microsoft-purview-metadata-policies-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-metadata-policies-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/overlays/microsoft-purview-records-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-records-management-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/overlays/microsoft-purview-scanning-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-scanning-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/overlays/microsoft-purview-unified-catalog-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-unified-catalog-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/overlays/microsoft-purview-workflow-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-purview-workflow-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-purview/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-assign-term-to-entities-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-assign-term-to-entities-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-categorize-glossary-term-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-categorize-glossary-term-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-classify-entity-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-classify-entity-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-define-and-apply-classification-type-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-define-and-apply-classification-type-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-define-rule-and-scan-quality-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-define-rule-and-scan-quality-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-move-entities-to-collection-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-move-entities-to-collection-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-onboard-entity-to-collection-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-onboard-entity-to-collection-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-profile-asset-and-poll-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-profile-asset-and-poll-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-provision-scan-ruleset-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-provision-scan-ruleset-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-publish-data-product-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-publish-data-product-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-publish-glossary-term-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-publish-glossary-term-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-register-source-and-scan-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-register-source-and-scan-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-relate-entities-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-relate-entities-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-run-and-poll-scan-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-run-and-poll-scan-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-schedule-recurring-scan-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-schedule-recurring-scan-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-search-and-classify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-search-and-classify-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/arazzo/microsoft-purview-trace-asset-lineage-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-purview-trace-asset-lineage-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://purview.microsoft.com
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/purview/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/purview/use-azure-purview-studio
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/purview/data-gov-api-rest-data-plane
- group: docs
  title: ''
  type: Reference
  url: https://learn.microsoft.com/en-us/rest/api/purview/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/purview/data-gov-python-sdk
- group: other
  title: ''
  type: Best Practices
  url: https://learn.microsoft.com/en-us/purview/concept-best-practices-accounts
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/purview/whats-new
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/microsoft-purview-blog/bg-p/MicrosoftPurviewBlog
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/en-us/answers/topics/azure-purview.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/purview
- group: operate
  title: ''
  type: Community
  url: https://techcommunity.microsoft.com/t5/microsoft-purview/ct-p/MicrosoftPurview
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/security/business/microsoft-purview
- group: start
  title: ''
  type: Login
  url: https://purview.microsoft.com
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/en-us/products/purview/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/json-ld/microsoft-purview-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-purview-context.jsonld
created: 2024-01-15 00:00:00+00:00
description: Microsoft Purview is a comprehensive data governance service that helps organizations discover, catalog, classify, and manage their data estate across on-premises, multi-cloud, and SaaS environments.
finops:
- name: Microsoft Purview Finops
  service_category: Compliance / Data Governance
  slug: microsoft-purview-finops
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2021/04/Microsoft-Purview-logo.png
json_schemas:
- name: AccessKeys
  property_count: 2
  slug: microsoft-purview-accesskeys
- name: Microsoft Purview Account
  property_count: 8
  slug: microsoft-purview-account
- name: AccountEndpoints
  property_count: 3
  slug: microsoft-purview-accountendpoints
- name: AccountList
  property_count: 3
  slug: microsoft-purview-accountlist
- name: AccountProperties
  property_count: 11
  slug: microsoft-purview-accountproperties
- name: AccountSku
  property_count: 2
  slug: microsoft-purview-accountsku
- name: AccountUpdateParameters
  property_count: 3
  slug: microsoft-purview-accountupdateparameters
- name: AtlasClassification
  property_count: 8
  slug: microsoft-purview-atlasclassification
- name: AtlasClassifications
  property_count: 6
  slug: microsoft-purview-atlasclassifications
- name: AtlasEntitiesWithExtInfo
  property_count: 2
  slug: microsoft-purview-atlasentitieswithextinfo
- name: AtlasEntity
  property_count: 19
  slug: microsoft-purview-atlasentity
- name: AtlasEntityHeader
  property_count: 11
  slug: microsoft-purview-atlasentityheader
- name: AtlasEntityHeaders
  property_count: 1
  slug: microsoft-purview-atlasentityheaders
- name: AtlasEntityWithExtInfo
  property_count: 2
  slug: microsoft-purview-atlasentitywithextinfo
- name: AtlasGlossary
  property_count: 9
  slug: microsoft-purview-atlasglossary
- name: AtlasGlossaryCategory
  property_count: 9
  slug: microsoft-purview-atlasglossarycategory
- name: AtlasGlossaryHeader
  property_count: 3
  slug: microsoft-purview-atlasglossaryheader
- name: AtlasGlossaryTerm
  property_count: 13
  slug: microsoft-purview-atlasglossaryterm
- name: AtlasLineageInfo
  property_count: 8
  slug: microsoft-purview-atlaslineageinfo
- name: AtlasObjectId
  property_count: 3
  slug: microsoft-purview-atlasobjectid
- name: AtlasRelatedCategoryHeader
  property_count: 5
  slug: microsoft-purview-atlasrelatedcategoryheader
- name: AtlasRelatedObjectId
  property_count: 8
  slug: microsoft-purview-atlasrelatedobjectid
- name: AtlasRelatedTermHeader
  property_count: 7
  slug: microsoft-purview-atlasrelatedtermheader
- name: AtlasRelationship
  property_count: 15
  slug: microsoft-purview-atlasrelationship
- name: AtlasRelationshipWithExtInfo
  property_count: 2
  slug: microsoft-purview-atlasrelationshipwithextinfo
- name: AtlasTermAssignmentHeader
  property_count: 9
  slug: microsoft-purview-atlastermassignmentheader
- name: AtlasTermCategorizationHeader
  property_count: 5
  slug: microsoft-purview-atlastermcategorizationheader
- name: AtlasTypeDef
  property_count: 13
  slug: microsoft-purview-atlastypedef
- name: AtlasTypeDefHeader
  property_count: 3
  slug: microsoft-purview-atlastypedefheader
- name: AtlasTypesDef
  property_count: 7
  slug: microsoft-purview-atlastypesdef
- name: AttributeMatcher
  property_count: 5
  slug: microsoft-purview-attributematcher
- name: AttributeRule
  property_count: 4
  slug: microsoft-purview-attributerule
- name: AuthorityTemplate
  property_count: 2
  slug: microsoft-purview-authoritytemplate
- name: AutoCompleteRequest
  property_count: 3
  slug: microsoft-purview-autocompleterequest
- name: AutoCompleteResult
  property_count: 1
  slug: microsoft-purview-autocompleteresult
- name: AutoCompleteResultValue
  property_count: 2
  slug: microsoft-purview-autocompleteresultvalue
- name: BusinessDomain
  property_count: 9
  slug: microsoft-purview-businessdomain
- name: BusinessDomainList
  property_count: 2
  slug: microsoft-purview-businessdomainlist
- name: CategoryTemplate
  property_count: 2
  slug: microsoft-purview-categorytemplate
- name: CheckNameAvailabilityRequest
  property_count: 2
  slug: microsoft-purview-checknameavailabilityrequest
- name: CheckNameAvailabilityResult
  property_count: 3
  slug: microsoft-purview-checknameavailabilityresult
- name: CitationTemplate
  property_count: 4
  slug: microsoft-purview-citationtemplate
- name: Microsoft Purview Classification
  property_count: 8
  slug: microsoft-purview-classification
- name: ClassificationResult
  property_count: 3
  slug: microsoft-purview-classificationresult
- name: ClassificationRule
  property_count: 4
  slug: microsoft-purview-classificationrule
- name: ClassificationRuleList
  property_count: 3
  slug: microsoft-purview-classificationrulelist
- name: ClassificationRulePattern
  property_count: 2
  slug: microsoft-purview-classificationrulepattern
- name: CollectionAdminUpdate
  property_count: 1
  slug: microsoft-purview-collectionadminupdate
- name: CollectionReference
  property_count: 2
  slug: microsoft-purview-collectionreference
- name: ColumnProfile
  property_count: 10
  slug: microsoft-purview-columnprofile
- name: ConnectedVia
  property_count: 2
  slug: microsoft-purview-connectedvia
- name: ContentInfo
  property_count: 4
  slug: microsoft-purview-contentinfo
- name: CriticalDataElement
  property_count: 8
  slug: microsoft-purview-criticaldataelement
- name: CriticalDataElementList
  property_count: 2
  slug: microsoft-purview-criticaldataelementlist
- name: Microsoft Purview Data Source
  property_count: 4
  slug: microsoft-purview-data-source
- name: DataProduct
  property_count: 9
  slug: microsoft-purview-dataproduct
- name: DataProductList
  property_count: 2
  slug: microsoft-purview-dataproductlist
- name: DataQualityRule
  property_count: 11
  slug: microsoft-purview-dataqualityrule
- name: DataQualityRuleList
  property_count: 2
  slug: microsoft-purview-dataqualityrulelist
- name: DataQualityScanRequest
  property_count: 2
  slug: microsoft-purview-dataqualityscanrequest
- name: DataQualityScanResult
  property_count: 3
  slug: microsoft-purview-dataqualityscanresult
- name: DataQualityScore
  property_count: 7
  slug: microsoft-purview-dataqualityscore
- name: DataQualityScoreList
  property_count: 2
  slug: microsoft-purview-dataqualityscorelist
- name: DataSource
  property_count: 5
  slug: microsoft-purview-datasource
- name: DataSourceList
  property_count: 3
  slug: microsoft-purview-datasourcelist
- name: DecisionRule
  property_count: 3
  slug: microsoft-purview-decisionrule
- name: DepartmentTemplate
  property_count: 2
  slug: microsoft-purview-departmenttemplate
- name: DlpAction
  property_count: 3
  slug: microsoft-purview-dlpaction
- name: DlpMatchedRule
  property_count: 6
  slug: microsoft-purview-dlpmatchedrule
- name: DowngradeJustification
  property_count: 2
  slug: microsoft-purview-downgradejustification
- name: EdiscoveryCase
  property_count: 10
  slug: microsoft-purview-ediscoverycase
- name: EdiscoveryCustodian
  property_count: 8
  slug: microsoft-purview-ediscoverycustodian
- name: EdiscoveryHoldPolicy
  property_count: 9
  slug: microsoft-purview-ediscoveryholdpolicy
- name: EdiscoveryReviewSet
  property_count: 4
  slug: microsoft-purview-ediscoveryreviewset
- name: EdiscoverySearch
  property_count: 8
  slug: microsoft-purview-ediscoverysearch
- name: Microsoft Purview Atlas Entity
  property_count: 19
  slug: microsoft-purview-entity
- name: EntityMutationResponse
  property_count: 3
  slug: microsoft-purview-entitymutationresponse
- name: FilePlanReferenceTemplate
  property_count: 2
  slug: microsoft-purview-fileplanreferencetemplate
- name: Microsoft Purview Glossary Term
  property_count: 17
  slug: microsoft-purview-glossary-term
- name: GlossaryTermList
  property_count: 2
  slug: microsoft-purview-glossarytermlist
- name: GovernanceContact
  property_count: 3
  slug: microsoft-purview-governancecontact
- name: Identity
  property_count: 4
  slug: microsoft-purview-identity
- name: IdentitySet
  property_count: 3
  slug: microsoft-purview-identityset
- name: InformationProtectionAction
  property_count: 1
  slug: microsoft-purview-informationprotectionaction
- name: InformationProtectionPolicySetting
  property_count: 5
  slug: microsoft-purview-informationprotectionpolicysetting
- name: KeyValuePair
  property_count: 2
  slug: microsoft-purview-keyvaluepair
- name: LabelingOptions
  property_count: 2
  slug: microsoft-purview-labelingoptions
- name: LineageRelation
  property_count: 3
  slug: microsoft-purview-lineagerelation
- name: MetadataPolicy
  property_count: 4
  slug: microsoft-purview-metadatapolicy
- name: MetadataPolicyList
  property_count: 2
  slug: microsoft-purview-metadatapolicylist
- name: MetadataRole
  property_count: 4
  slug: microsoft-purview-metadatarole
- name: MetadataRoleList
  property_count: 2
  slug: microsoft-purview-metadatarolelist
- name: MoveEntitiesRequest
  property_count: 1
  slug: microsoft-purview-moveentitiesrequest
- name: OKR
  property_count: 9
  slug: microsoft-purview-okr
- name: OKRList
  property_count: 2
  slug: microsoft-purview-okrlist
- name: Operation
  property_count: 4
  slug: microsoft-purview-operation
- name: OperationList
  property_count: 3
  slug: microsoft-purview-operationlist
- name: OperationResponse
  property_count: 2
  slug: microsoft-purview-operationresponse
- name: ParentRelation
  property_count: 3
  slug: microsoft-purview-parentrelation
- name: PrivateEndpointConnection
  property_count: 4
  slug: microsoft-purview-privateendpointconnection
- name: PrivateEndpointConnectionList
  property_count: 3
  slug: microsoft-purview-privateendpointconnectionlist
- name: ProfilingRequest
  property_count: 2
  slug: microsoft-purview-profilingrequest
- name: ProfilingResult
  property_count: 5
  slug: microsoft-purview-profilingresult
- name: ProtectionScope
  property_count: 4
  slug: microsoft-purview-protectionscope
- name: RecurrenceSchedule
  property_count: 4
  slug: microsoft-purview-recurrenceschedule
- name: ResourceLink
  property_count: 2
  slug: microsoft-purview-resourcelink
- name: Microsoft Purview Retention Label
  property_count: 12
  slug: microsoft-purview-retention-label
- name: RetentionEvent
  property_count: 11
  slug: microsoft-purview-retentionevent
- name: RetentionEventType
  property_count: 7
  slug: microsoft-purview-retentioneventtype
- name: RetentionLabel
  property_count: 17
  slug: microsoft-purview-retentionlabel
- name: RuleResult
  property_count: 5
  slug: microsoft-purview-ruleresult
- name: Microsoft Purview Scan
  property_count: 4
  slug: microsoft-purview-scan
- name: ScanList
  property_count: 3
  slug: microsoft-purview-scanlist
- name: ScanResult
  property_count: 13
  slug: microsoft-purview-scanresult
- name: ScanResultList
  property_count: 3
  slug: microsoft-purview-scanresultlist
- name: ScanRuleset
  property_count: 4
  slug: microsoft-purview-scanruleset
- name: ScanRulesetList
  property_count: 3
  slug: microsoft-purview-scanrulesetlist
- name: SearchFacetItem
  property_count: 3
  slug: microsoft-purview-searchfacetitem
- name: SearchRequest
  property_count: 6
  slug: microsoft-purview-searchrequest
- name: SearchResult
  property_count: 3
  slug: microsoft-purview-searchresult
- name: SearchResultValue
  property_count: 15
  slug: microsoft-purview-searchresultvalue
- name: Microsoft Purview Sensitivity Label
  property_count: 11
  slug: microsoft-purview-sensitivity-label
- name: SensitivityLabel
  property_count: 10
  slug: microsoft-purview-sensitivitylabel
- name: SuggestRequest
  property_count: 3
  slug: microsoft-purview-suggestrequest
- name: SuggestResult
  property_count: 1
  slug: microsoft-purview-suggestresult
- name: TermSearchResultValue
  property_count: 3
  slug: microsoft-purview-termsearchresultvalue
- name: TimeBoundary
  property_count: 3
  slug: microsoft-purview-timeboundary
- name: Trigger
  property_count: 3
  slug: microsoft-purview-trigger
- name: TriggerRecurrence
  property_count: 6
  slug: microsoft-purview-triggerrecurrence
- name: UserRequestPayload
  property_count: 2
  slug: microsoft-purview-userrequestpayload
- name: UserRequestResponse
  property_count: 2
  slug: microsoft-purview-userrequestresponse
- name: ValidationResult
  property_count: 1
  slug: microsoft-purview-validationresult
- name: Workflow
  property_count: 6
  slug: microsoft-purview-workflow
- name: WorkflowCreateOrUpdateCommand
  property_count: 5
  slug: microsoft-purview-workflowcreateorupdatecommand
- name: WorkflowList
  property_count: 2
  slug: microsoft-purview-workflowlist
- name: WorkflowRun
  property_count: 10
  slug: microsoft-purview-workflowrun
- name: WorkflowTask
  property_count: 12
  slug: microsoft-purview-workflowtask
- name: WorkflowTrigger
  property_count: 3
  slug: microsoft-purview-workflowtrigger
json_structures:
- name: Microsoft Purview Structure
  property_count: 0
  slug: microsoft-purview-structure
jsonld:
- class_count: 0
  name: Microsoft Purview Context
  property_count: 19
  slug: microsoft-purview-context
layout: provider
mcp_servers:
- description: First-party Microsoft MCP server for Purview Data Lifecycle Management diagnostics. Local stdio server (TypeScript, @modelcontextprotocol/sdk) that authenticates to Exchange Online with MSAL interacti
  name: Microsoft Purview MCP Server
  slug: microsoft-purview-mcp-server
modified: '2026-06-20'
name: Microsoft Purview
nav: Providers
network: true
overview: 'Microsoft Purview publishes 44 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Approval API, Business Domains API, and 41 more. Tagged areas include Compliance, Data Catalog, Data Classification, Data Governance, and Data Loss Prevention.


  The Microsoft Purview catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Purview''s developer surface includes authentication, CLI, changelog, developer portal, documentation, getting-started guide, engineering blog, and 60 more developer resources.'
plans:
- name: Microsoft Purview Plans Pricing
  plan_count: 10
  slug: microsoft-purview-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Microsoft Purview Rate Limits
  slug: microsoft-purview-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Microsoft Purview API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-purview-jsonschema-spectral-rules
scopes:
- name: Microsoft Purview Scopes
  scope_count: 8
  slug: microsoft-purview-scopes
  summary_line: 8 scopes · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 67.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 64.3
    catalog_earned_first_party: 12.0
    catalog_gap: 50.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 71.1
    contract_governance: 14.4
    contract_quality: 63.4
    developer_ergonomics: 72.6
    discoverability: 75.0
    operational_transparency: 42.1
  previous_composite: 66.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 44
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: fedramp
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-purview/refs/heads/main/screenshots/microsoft-purview-2026-08-17T124207.png
security:
- kind: authentication
  name: Microsoft Purview Authentication
  slug: microsoft-purview-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Purview Domain Security
  slug: microsoft-purview-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Purview Vulnerability Disclosure
  slug: microsoft-purview-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-purview
tags:
- Compliance
- Data Catalog
- Data Classification
- Data Governance
- Data Loss Prevention
- Information Protection
website: https://www.microsoft.com/en-us/security/business/microsoft-purview
---
