---
access_model:
  confidence: high
  label: Subscription entitlement · application registration then Clarivate approval
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - openapi
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 61
  human_in_the_loop: 0
  name: Clarivate Agentic Access
  operation_count: 186
  slug: clarivate-agentic-access
  summary_line: 186 operations · 61 acting
api_count: 26
apis:
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Perform User operations
  name: Clarivate Administration - User data API
  phrasing_intents:
  - id: getAdminUsers
    intent: List Converis users
    question: How do I list every user in our Converis system?
  - id: postAdminUsers
    intent: Create a Converis user
    question: How do I add a new user account to Converis with roles?
  - id: getAdminUsersByUsername
    intent: Get a Converis user by username
    question: Where do I see the account details for one Converis user?
  - id: putAdminUsersByUsername
    intent: Update a Converis user
    question: How do I change an existing Converis user's email or roles?
  - id: deleteAdminUsersByUsername
    intent: Delete a Converis user
    question: How do I remove a user and their roles from Converis?
  phrasing_ops: 5
  slug: clarivate-administration-user-data-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Perform User Delegation operations
  name: Clarivate Administration - User Delegations API
  phrasing_intents:
  - id: postAdminUsersDelegation
    intent: Create a user delegation
    question: How do I let one Converis user act in another user's role while they are away?
  - id: putAdminUsersDelegation
    intent: Update a user delegation
    question: How do I extend or change an existing role delegation?
  - id: getAdminUsersDelegation
    intent: Find user delegations
    question: How do I see which Converis users have delegated their roles to someone else?
  - id: deleteAdminUsersDelegation{delegationId}
    intent: Delete a user delegation
    question: How do I revoke a role delegation in Converis?
  phrasing_ops: 4
  slug: clarivate-administration-user-delegations-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Get audit info for actions like DOWNLOAD.
  name: Clarivate Audit Info API
  phrasing_intents:
  - id: getAuditInfo
    intent: Retrieve the Converis audit log
    question: How do I pull the audit trail of changes made in Converis?
  phrasing_ops: 1
  slug: clarivate-audit-info-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Service invalidates cache post data erasure for direct GDPR data deletion from database.
  name: Clarivate Cache Management API
  phrasing_intents:
  - id: removeUserFromCache
    intent: Evict a Converis user from the cache
    question: How do I clear a single Converis login user out of the server cache?
  - id: removePersonFromCache
    intent: Evict a person record from the cache
    question: How can I drop a person record from the Converis cache by its ID?
  phrasing_ops: 2
  slug: clarivate-cache-management-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Categories
  name: Clarivate Categories API
  phrasing_intents:
  - id: getCategories
    intent: Search JCR subject categories
    question: How do I browse the Journal Citation Reports subject categories?
  - id: getCategoriesById
    intent: Get a JCR subject category profile
    question: What does the profile of a JCR subject category include?
  - id: getCategoriesByIdReportsYearByYear
    intent: Get a category's metrics for a JCR year
    question: What was the median and aggregate impact factor of a subject category in a given year?
  - id: getCategoriesByIdCitedYearByYear
    intent: List journals citing a category in a year
    question: Which journals cite the journals in a subject category the most?
  - id: getCategoriesByIdCitingYearByYear
    intent: List journals a category cites in a year
    question: Which journals do the journals in a category cite most often?
  phrasing_ops: 5
  slug: clarivate-categories-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Access PentahoParamTokenScheduler API via HTTPS with admin credentials.
  name: Clarivate Configuration API
  phrasing_intents:
  - id: startPentahoScheduler
    intent: Start the Pentaho token cleanup scheduler
    question: How do I start the scheduler that removes Pentaho parameter tokens in Converis?
  - id: getPentahoSchedulerStatus
    intent: Check the Pentaho token scheduler status
    question: Is the Pentaho parameter token scheduler currently running in Converis?
  - id: stopPentahoScheduler
    intent: Stop the Pentaho token cleanup scheduler
    question: How do I halt the Pentaho parameter token scheduler in Converis?
  phrasing_ops: 3
  slug: clarivate-configuration-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Get the configured entity definitions
  name: Clarivate Configuration - Entity definitions API
  phrasing_intents:
  - id: getConfigEntities
    intent: List all Converis entity definitions
    question: How do I see the definitions of every entity type configured in Converis?
  - id: getConfigEntitiesByType
    intent: Get one Converis entity definition
    question: What attributes does a specific Converis entity type define?
  phrasing_ops: 2
  slug: clarivate-configuration-entity-definitions-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Get the configured entity definitions
  name: Clarivate Configuration - Link entity definitions API
  phrasing_intents:
  - id: getConfigLinkentities
    intent: List all link entity definitions
    question: How do I list every relationship type definition in Converis?
  - id: getConfigLinkentitiesByLinkType
    intent: Get one link entity definition
    question: What attributes does a particular Converis link type define?
  phrasing_ops: 2
  slug: clarivate-configuration-link-entity-definitions-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: REST endpoints for data Entities
  name: Clarivate Data Entities API
  phrasing_intents:
  - id: deleteDataEntities
    intent: Delete Converis data entities
    question: How do I remove data entity records from Converis?
  - id: optionsDataEntities
    intent: Describe supported data entity actions
    question: Which actions and request structure does the Converis data entities endpoint support?
  - id: createDataEntities
    intent: Create new Converis data entities
    question: How do I add new records such as publications to Converis programmatically?
  - id: updateDataEntities
    intent: Update existing Converis data entities
    question: How do I modify records that already exist in Converis in bulk?
  phrasing_ops: 4
  slug: clarivate-data-entities-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Get the entity data
  name: Clarivate Data - Entity API
  phrasing_intents:
  - id: getDataEntitiesByType
    intent: List all records of an entity type
    question: How do I export all records of one entity type, like publications, from Converis?
  - id: postDataEntitiesByTypeQuery
    intent: Query entity records with a filter
    question: Can I filter Converis entity records by sending a query in the request body?
  - id: getDataEntitiesByTypeById
    intent: Get one entity record
    question: How do I read a single Converis object by its type and ID?
  - id: getDataEntitiesByTypeLinkedByLinkTypeById
    intent: List records linked to an object
    question: How do I find all entities of one type linked to a specific Converis object?
  phrasing_ops: 4
  slug: clarivate-data-entity-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Download files
  name: Clarivate Data - File API
  phrasing_intents:
  - id: getDataFileByFileTypeByIdDownload
    intent: Download a Converis file
    question: How do I download a file attached in Converis?
  phrasing_ops: 1
  slug: clarivate-data-file-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Data integration uses Kettle Transformation with Servlets as output steps.
  name: Clarivate Data Integration API
  phrasing_intents:
  - id: getDataFromPdiProcess
    intent: Read output from a data integration process
    question: How do I fetch the output of a Pentaho data integration process exposed as a web service in Converis?
  - id: submitDataToPdiProcess
    intent: Send data into a data integration process
    question: How do I push data into a Converis data integration process?
  phrasing_ops: 2
  slug: clarivate-data-integration-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Get the links between entity data
  name: Clarivate Data - Link entity API
  phrasing_intents:
  - id: getDataLinkentitiesByLinkType
    intent: List all entries of a link entity type
    question: How do I list every relationship record of one link type in Converis?
  - id: postDataLinkentitiesByLinkTypeQuery
    intent: Query link entity entries with a filter
    question: Can I filter Converis link entity entries by sending a query in the body?
  - id: getEntityByName
    intent: Get a link entity by type and ID
    question: How do I read one relationship record from Converis by its link type and ID?
  - id: getDataLinkentitiesByLinkTypeLinkedByTypeById
    intent: List link entries attached to an entity
    question: How do I find all relationship records that connect to a specific Converis entity?
  phrasing_ops: 4
  slug: clarivate-data-link-entity-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Get the links between entity data
  name: Clarivate Data - Tree API
  phrasing_intents:
  - id: getDataTreeByLinkTypeRoot
    intent: Get the root node of a tree
    question: How do I find the top node of an organisation tree in Converis?
  - id: getDataTreeByLinkTypeByStartNode
    intent: Traverse a tree from a node
    question: How do I get the path from a node up to the root of a Converis tree?
  phrasing_ops: 2
  slug: clarivate-data-tree-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Derwent API API from Clarivate — 16 operation(s) for derwent api.
  name: Clarivate Derwent API
  phrasing_intents:
  - id: derwentGetDocumentImages
    intent: List a Derwent patent's image URLs (JWT route)
    question: How do I get the drawing image URLs for a Derwent patent using JWT authentication?
  - id: derwentPostDocumentImages
    intent: Batch-fetch Derwent image URLs (JWT route)
    question: Can I fetch image URLs for several Derwent patents in one POST using JWT auth?
  - id: derwentClassBrowse
    intent: Browse a patent classification hierarchy
    question: How do I see the child codes under an IPC classification code in Derwent?
  - id: derwentClassSearch
    intent: Find classification codes by keyword
    question: Which patent classification codes match a keyword like battery electrode?
  - id: derwentCombinedSearch
    intent: Run a combined Derwent patent search
    question: Can I combine several saved patent queries into one Derwent search?
  - id: derwentCorporateTree
    intent: Look up companies in the corporate tree
    question: How do I find a company's subsidiaries in the Derwent corporate tree?
  - id: postPatentsDerwentDocumentImages
    intent: Batch-fetch Derwent patent image URLs
    question: How do I get image URLs for many Derwent patents in one request?
  - id: getPatentsDerwentDocumentImagesByDocumentGuid
    intent: List image URLs for one Derwent patent
    question: Where can I get the drawings of a single Derwent patent as image URLs?
  phrasing_ops: 17
  slug: clarivate-derwent-api-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Web of Science Documents
  name: Clarivate Documents API
  phrasing_intents:
  - id: getDocuments
    intent: Search Web of Science documents
    question: How do I search Web of Science documents with the Starter API?
  - id: getDocumentsByUid
    intent: Get a document by accession number
    question: How do I look up one Web of Science document by its UID?
  phrasing_ops: 2
  slug: clarivate-documents-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Download API from Clarivate — 1 operation(s) for download.
  name: Clarivate Download API
  phrasing_intents:
  - id: postDownload
    intent: Request an LSH data export
    question: How do I start a data export download from Life Sciences & Healthcare?
  phrasing_ops: 1
  slug: clarivate-download-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The EndNote REST API API from Clarivate — 1 operation(s) for endnote rest api.
  name: Clarivate EndNote REST API
  phrasing_intents:
  - id: readLibrary
    intent: Get the user's EndNote library
    question: How do I retrieve my EndNote library object through the REST API?
  phrasing_ops: 1
  slug: clarivate-endnote-rest-api-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The feed API from Clarivate — 4 operation(s) for feed.
  name: Clarivate Feed API
  phrasing_intents:
  - id: request_package_ric_download_v1_requestPackage_post
    intent: Request a content package for download
    question: How do I start preparing a bulk download package of a content set?
  - id: check_package_status_ric_download_v1_checkPackageStatus_get
    intent: Check a download package's status
    question: How do I know when my requested content package is ready?
  - id: download_package_ric_download_v1_downloadPackage_get
    intent: Download a prepared content package
    question: How do I download the result file once my content package is ready?
  - id: get_subscriptions_info_ric_download_v1_info_get
    intent: List my content subscriptions
    question: Which content sets am I subscribed to in the feed API?
  phrasing_ops: 4
  slug: clarivate-feed-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The History API from Clarivate — 1 operation(s) for history.
  name: Clarivate History API
  phrasing_intents:
  - id: postHistory
    intent: List past LSH export requests
    question: How do I check the status of my earlier data export requests?
  phrasing_ops: 1
  slug: clarivate-history-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Integration Api API from Clarivate — 1 operation(s) for integration api.
  name: Clarivate Integration API
  phrasing_intents:
  - id: getIntegrationApiSingleOppositionById
    intent: Get a trademark opposition
    question: How do I pull one opposition record into another application?
  phrasing_ops: 1
  slug: clarivate-integration-api-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Supports integration and data supplement activities.
  name: Clarivate Integration API
  phrasing_intents:
  - id: getIdByUniqueId
    intent: Get Web of Science records by ID
    question: How do I fetch full Web of Science records when I already know their IDs?
  - id: getRecordidsByQueryId
    intent: List record IDs for a search
    question: Can I get just the IDs of the records a search returned, without full metadata?
  phrasing_ops: 2
  slug: clarivate-integration-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The IP Cases API from Clarivate — 4 operation(s) for ip cases.
  name: Clarivate IP Cases API
  phrasing_intents:
  - id: checkCaselawDocumentAvailability
    intent: Check caselaw document availability
    question: How do I check whether specific caselaw documents are available and when they were last updated?
  - id: getCaselawDocuments
    intent: Fetch several caselaw documents by GUID
    question: How do I retrieve multiple full caselaw documents at once?
  - id: getCaselawDocument
    intent: Get one full caselaw document
    question: How do I pull the full text record of a single IP court case?
  - id: searchCaselaw
    intent: Search and aggregate IP caselaw
    question: How do I search IP litigation cases and group the results?
  phrasing_ops: 4
  slug: clarivate-ip-cases-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Journals
  name: Clarivate Journals API
  phrasing_intents:
  - id: getJournals
    intent: Search JCR journals
    question: How do I search the Journal Citation Reports journal list?
  - id: getJournalsById
    intent: Get a journal profile
    question: What publisher, ISSN and open access details are in a journal's profile?
  - id: getJournalsByIdReportsYearByYear
    intent: Get a journal's metrics for a JCR year
    question: What was a journal's Journal Impact Factor in a specific year?
  - id: getJournalsByIdCitedYearByYear
    intent: List journals citing a journal in a year
    question: Which journals cite a given journal the most?
  - id: getJournalsByIdCitingYearByYear
    intent: List journals a journal cites in a year
    question: Which journals does a given journal cite most often?
  - id: getJournalsByIdHistory
    intent: Get a journal's change history
    question: Has a particular journal changed its title or details over time?
  - id: getJournalsHistoryTitle
    intent: List journal title changes by year
    question: Which journals changed their titles in a given year?
  phrasing_ops: 7
  slug: clarivate-journals-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Response in json format
  name: Clarivate JSON API
  phrasing_intents:
  - id: getDocumentLevelMetricsByInstitutionIdJson
    intent: Get my institution's document metrics as JSON
    question: How do I pull document level metrics for all of my institution's papers in a year as JSON?
  - id: getDocumentLevelMetricsByInstitutionIdRecordCountJson
    intent: Count my institution's records for a year (JSON)
    question: How many records are unified to my institution in a given year, in JSON?
  - id: getDocumentLevelMetricsByUTJson
    intent: Get document metrics for a UT (JSON)
    question: How do I get InCites metrics for one Web of Science accession number in JSON?
  - id: getCheckValidUTsJson
    intent: Find invalid UTs in a list (JSON)
    question: Which accession numbers in my list are not valid UTs, returned as JSON?
  - id: getInCitesLastUpdatedJson
    intent: Get InCites data update times (JSON)
    question: When were the InCites and Web of Science datasets last updated, in JSON?
  phrasing_ops: 5
  slug: clarivate-json-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The last-updated API from Clarivate — 1 operation(s) for last-updated.
  name: Clarivate Last Updated API
  phrasing_intents:
  - id: getLastUpdated
    intent: Get the JCR content update date
    question: When was the Journal Citation Reports content last updated?
  phrasing_ops: 1
  slug: clarivate-last-updated-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Retrieves representation of an instance of com.converis.ws.restful.pentaho.publicservice
  name: 'Clarivate Legacy API: find By Pattern API'
  phrasing_intents:
  - id: findByPattern
    intent: Find public Converis objects by pattern
    question: How do I find public Converis records whose attribute matches a text pattern?
  phrasing_ops: 1
  slug: clarivate-legacy-api-find-by-pattern-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: REST web service
  name: 'Clarivate Legacy API: get Info Object API'
  phrasing_intents:
  - id: filterInfoObjectIds
    intent: Filter public info objects to IDs
    question: How do I get only the IDs of public Converis objects matching a filter?
  - id: getFilteredInfoObjects
    intent: Get all filtered public info objects
    question: How do I retrieve every public info object that matches a filter in one call?
  - id: getFilteredInfoObjectsthroughstart
    intent: Get filtered info objects from an offset
    question: Can I skip the first results and fetch filtered info objects from a given position?
  - id: getInfoObject
    intent: Get a public info object by type and ID
    question: How do I read one public Converis object when I know its type and ID?
  - id: getFilteredInfoObjectsWithStartAndCount
    intent: Page through filtered info objects
    question: How do I page filtered info objects with both a start and a page size?
  - id: getInfoObjectDetail
    intent: Get localized detail of a public info object
    question: How do I get the detailed view of a public Converis object in a specific language?
  - id: filterInfoObjectList
    intent: List filtered info objects in a language
    question: How do I list filtered public objects with their values in a chosen language?
  phrasing_ops: 7
  slug: clarivate-legacy-api-get-info-object-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Gets the version of Legacy API
  name: 'Clarivate Legacy API: get legacy api version API'
  phrasing_intents:
  - id: getPublicApiVersion
    intent: Get the legacy public API version
    question: Which version of the Converis legacy public API is this server running?
  phrasing_ops: 1
  slug: clarivate-legacy-api-get-legacy-api-version-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: 'REST Web Service: Representation of GetRelated'
  name: 'Clarivate Legacy API: get related info objects API'
  phrasing_intents:
  - id: getRelatedEntities
    intent: List objects related to a public entity
    question: How do I find publications related to a person in Converis?
  phrasing_ops: 1
  slug: clarivate-legacy-api-get-related-info-objects-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: 'The Legacy API: get using pentaho resource API from Clarivate — 2 operation(s) for legacy api: get using pentaho resource.'
  name: 'Clarivate Legacy API: get using pentaho resource API'
  phrasing_intents:
  - id: authenticateWithPentaho
    intent: Authenticate against Pentaho reporting
    question: How do I authenticate with Pentaho from the Converis legacy API?
  - id: getEmbeddedReportInfo
    intent: Get embedded Pentaho report information
    question: How do I get the information needed to embed a Pentaho report?
  phrasing_ops: 2
  slug: clarivate-legacy-api-get-using-pentaho-resource-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: REST endpoints for link entities.
  name: Clarivate Link Entities API
  phrasing_intents:
  - id: deleteLinkEntities
    intent: Delete Converis link entities
    question: How do I remove a relationship between two Converis records?
  - id: optionsLinkEntities
    intent: Describe supported link entity actions
    question: Which actions and request structure does the link entities endpoint accept?
  - id: createLinkEntities
    intent: Create new Converis link entities
    question: How do I link a person to a publication in Converis through the API?
  - id: updateLinkEntities
    intent: Update existing Converis link entities
    question: How do I change existing relationships between records in Converis?
  phrasing_ops: 4
  slug: clarivate-link-entities-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The LSH AI Agent API from Clarivate — 1 operation(s) for lsh ai agent.
  name: Clarivate LSH AI Agent API
  phrasing_intents:
  - id: public_data_retrieval_agent_endpoint_ric_lsh_ai_agent_v1_data_retrieval_agent_post
    intent: Ask the life sciences data retrieval agent
    question: Can I ask a natural-language question to Clarivate's life sciences data agent?
  phrasing_ops: 1
  slug: clarivate-lsh-ai-agent-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Members API from Clarivate — 1 operation(s) for members.
  name: Clarivate Members API
  phrasing_intents:
  - id: getConsortiumMembers
    intent: List consortium members for a customer
    question: How do I list the member institutions of my consortium for Web of Science usage harvesting?
  phrasing_ops: 1
  slug: clarivate-members-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Newapi API from Clarivate — 1 operation(s) for newapi.
  name: Clarivate Newapi API
  phrasing_intents:
  - id: getNewapi
    intent: Call the Cortellis newapi endpoint
    question: What does the Cortellis newapi endpoint return?
  phrasing_ops: 1
  slug: clarivate-newapi-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The ontology API from Clarivate — 3 operation(s) for ontology.
  name: Clarivate Ontology API
  phrasing_intents:
  - id: get_content_set_info_c3_ai_info__contentset__get
    intent: Get metadata for a content set
    question: How do I get metadata about a C3 AI content set?
  - id: get_content_set_ontologies_c3_ai_ontology__contentset__get
    intent: List ontologies in a content set
    question: Which ontologies are available in a given content set?
  - id: get_content_set_ontology_c3_ai_ontology__contentset___ontology_name__get
    intent: Get or search an ontology's vocabulary
    question: How do I get the vocabulary terms of one ontology?
  phrasing_ops: 3
  slug: clarivate-ontology-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Patents API from Clarivate — 9 operation(s) for patents.
  name: Clarivate Patents API
  phrasing_intents:
  - id: checkPatentAbstractAvailability
    intent: Check patent abstract availability
    question: How do I check whether abstract journal entries exist for my patents and get download URLs?
  - id: checkPatentDocumentAvailability
    intent: Check patent document availability
    question: How do I find out which patent full texts are available to download?
  - id: getPatentImages
    intent: List image URLs for a patent
    question: How do I get the images of a patent document from the IP data Patents API?
  - id: getPatentDocuments
    intent: Fetch several patent documents by GUID
    question: How do I retrieve multiple full patent documents in one call?
  - id: getPatentDocument
    intent: Get one full patent document
    question: How do I pull the full JSON record of a single patent?
  - id: getPatentPdf
    intent: Download a patent PDF
    question: How do I download the PDF of a patent from the IP data Patents API?
  - id: getMatchPatentEntities
    intent: Fuzzy-match several patent field values
    question: Can I fuzzy-match a batch of messy assignee names to canonical values?
  - id: getMatchPatentEntity
    intent: Fuzzy-match one patent field value
    question: How do I find the canonical form of a single company name used in patents?
  phrasing_ops: 9
  slug: clarivate-patents-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The prediction API from Clarivate — 2 operation(s) for prediction.
  name: Clarivate Prediction API
  phrasing_intents:
  - id: get_predictions_c3_ai_prediction_get
    intent: List available AI predictions
    question: Which AI predictions do I have access to?
  - id: make_prediction_c3_ai_prediction__prediction_name__post
    intent: Run an AI prediction
    question: How do I run model inference for a specific C3 AI prediction?
  phrasing_ops: 2
  slug: clarivate-prediction-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Projects management endpoints
  name: Clarivate Projects API
  phrasing_intents:
  - id: getReports
    intent: List sequence search projects
    question: How do I see all my Derwent sequence search projects?
  - id: postReports
    intent: Create a sequence search project
    question: How do I start a new project to hold my Derwent sequence searches?
  - id: getReportsById
    intent: Show a sequence search project
    question: Where can I see the details of one sequence search project?
  - id: patchReportsById
    intent: Update a sequence search project
    question: How do I rename or edit an existing sequence search project?
  - id: deleteReportsById
    intent: Delete a sequence search project
    question: How do I remove a sequence search project I no longer need?
  phrasing_ops: 5
  slug: clarivate-projects-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Publications & Sequences information endpoints
  name: Clarivate Publications & Sequences API
  phrasing_intents:
  - id: getPatentInfoFromAllSources
    intent: Show a patent's info across all sources
    question: How do I see sequence search information for a patent from every source database?
  - id: getPatentInfo
    intent: Show a patent's info from one source
    question: How do I get a patent's sequence-search record from one specific database?
  - id: getSequenceInfo
    intent: Show sequence information by accession number
    question: How do I look up a biological sequence by its accession number?
  phrasing_ops: 3
  slug: clarivate-publications-sequences-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Reference API from Clarivate — 2 operation(s) for reference.
  name: Clarivate Reference API
  phrasing_intents:
  - id: readtypes
    intent: List all EndNote reference types
    question: Which reference types does EndNote support, like journal article or book?
  - id: read/reference
    intent: Get a reference by GUID header
    question: How do I get a reference's current state when I have its GUID but not its URI?
  - id: update/reference
    intent: Update a reference identified in the body
    question: How do I update an EndNote reference when I only have its GUID in the payload?
  - id: create/reference
    intent: Create an EndNote reference
    question: How do I add a new reference to my EndNote library?
  phrasing_ops: 4
  slug: clarivate-reference-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The References API from Clarivate — 2 operation(s) for references.
  name: Clarivate References API
  phrasing_intents:
  - id: create/references/{guid}/file
    intent: Attach a file to a reference
    question: How do I attach a PDF to an existing EndNote reference?
  - id: read/references/{guid}
    intent: Get a reference by its GUID path
    question: How do I read all fields of a specific reference by its URI?
  - id: update/references/{guid}
    intent: Update a reference at its URI
    question: How do I change bibliographic fields on a reference I address by its URI?
  phrasing_ops: 3
  slug: clarivate-references-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Reports API from Clarivate — 6 operation(s) for reports.
  name: Clarivate Reports API
  phrasing_intents:
  - id: getReports
    intent: List supported COUNTER usage reports
    question: Which COUNTER R5 reports can I harvest from Web of Science?
  - id: getPRReport
    intent: Get the Platform Master Report (PR)
    question: How do I pull the customizable COUNTER platform usage master report?
  - id: getPRP1Report
    intent: Get the PR_P1 platform usage standard view
    question: Where do I get the standard PR_P1 view of overall platform usage by metric type?
  - id: getDRReport
    intent: Get the Database Master Report (DR)
    question: How do I get a customizable COUNTER report of usage by database?
  - id: getDRD1Report
    intent: Get database search and item usage (DR_D1)
    question: Which report shows searches and item requests per database for evaluating a database?
  - id: getDRD2Report
    intent: Get database access denied report (DR_D2)
    question: How do I see when users were turned away because simultaneous-use licenses were exceeded?
  phrasing_ops: 6
  slug: clarivate-reports-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Researcher data and metrics
  name: Clarivate Researchers API
  phrasing_intents:
  - id: getResearchers
    intent: Search researcher profiles
    question: How do I search Web of Science researcher profiles?
  - id: getResearchersByRid
    intent: Get a researcher profile
    question: How do I get metrics and metadata for one researcher by ResearcherID?
  - id: getResearchersByRidPeerReviews
    intent: List a researcher's peer reviews
    question: Which peer reviews has a researcher done?
  - id: getResearchersByRidDocuments
    intent: List a researcher's publications
    question: What documents has a researcher published?
  phrasing_ops: 4
  slug: clarivate-researchers-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Supports discovery and interrogation of Web of Science data.
  name: Clarivate Search API
  phrasing_intents:
  - id: getRoot
    intent: Search Web of Science with a query string
    question: How do I run an advanced Web of Science query with a GET request and get a query ID back?
  - id: postRoot
    intent: Submit a Web of Science search in a request body
    question: Can I send a long Web of Science query as a POST body instead of URL parameters?
  - id: getQueryByQueryId
    intent: Page through results of an earlier search
    question: How do I fetch the next page of records from a search I already ran, using its query ID?
  - id: getRelated
    intent: Find records related by shared references
    question: How do I find papers that share cited references with a given Web of Science record?
  - id: getCiting
    intent: Find articles that cite a record
    question: Who has cited this Web of Science Core Collection article?
  - id: getReferences
    intent: List the references an article cites
    question: What references does a given Web of Science article cite in its bibliography?
  - id: getCategoryContextByUniqueId
    intent: Get subject category context for a document
    question: Which subject categories do a document's citing and cited references fall into?
  - id: getCitationReportByQueryId
    intent: Build a citation report for a search
    question: How do I get a citation report for the result set of a search I ran?
  phrasing_ops: 8
  slug: clarivate-search-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Search results management endpoints
  name: Clarivate Search Results API
  phrasing_intents:
  - id: getReportsByReportIdSearchResultsBySearchId
    intent: List sequence search results
    question: How do I see the hits from a sequence search in my project?
  phrasing_ops: 1
  slug: clarivate-search-results-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Searches (Antibody) API from Clarivate — 1 operation(s) for searches (antibody).
  name: Clarivate Searches (Antibody) API
  phrasing_intents:
  - id: postReportsByReportIdSearchesCdrp
    intent: Run an antibody protein (CDR) search
    question: How do I search antibody protein sequences by their CDRs in Derwent?
  phrasing_ops: 1
  slug: clarivate-searches-antibody-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Searches management endpoints
  name: Clarivate Searches API
  phrasing_intents:
  - id: getReportsByReportIdSearches
    intent: List searches in a project
    question: How do I see all the sequence searches in one project?
  - id: postReportsByReportIdSearches
    intent: Create a search in a project
    question: How do I add a generic sequence search to a project?
  - id: getReportsByReportIdSearchesById
    intent: Show a search in a project
    question: Where can I see the settings and status of one sequence search?
  - id: patchReportsByReportIdSearchesById
    intent: Update a search in a project
    question: How do I edit an existing sequence search?
  - id: deleteReportsByReportIdSearchesById
    intent: Delete a search from a project
    question: How do I remove one search from a project?
  - id: deleteReportsByReportIdSearchesDestroyBulk
    intent: Bulk delete searches in a project
    question: Can I delete many searches from a project at once?
  phrasing_ops: 6
  slug: clarivate-searches-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Searches (BestSeq) API from Clarivate — 1 operation(s) for searches (bestseq).
  name: Clarivate Searches (BestSeq) API
  phrasing_intents:
  - id: postReportsByReportIdSearchesBestseqp
    intent: Run a BestSeq protein search
    question: How do I run a BestSeq protein sequence search?
  phrasing_ops: 1
  slug: clarivate-searches-bestseq-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Searches (BLAST / SW) API from Clarivate — 2 operation(s) for searches (blast / sw).
  name: Clarivate Searches (BLAST / SW) API
  phrasing_intents:
  - id: postReportsByReportIdSearchesBlastp
    intent: Run a BLAST protein search
    question: How do I run a BLAST search on a protein sequence in Derwent?
  - id: postReportsByReportIdSearchesSwn
    intent: Run a Smith-Waterman nucleotide search
    question: How do I run a Smith-Waterman search on a nucleotide sequence?
  phrasing_ops: 2
  slug: clarivate-searches-blast-sw-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Searches (Keyword) API from Clarivate — 1 operation(s) for searches (keyword).
  name: Clarivate Searches (Keyword) API
  phrasing_intents:
  - id: postReportsByReportIdSearchesKeyword
    intent: Run a keyword full-text search
    question: How do I do a keyword full-text search across sequence records?
  phrasing_ops: 1
  slug: clarivate-searches-keyword-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Searches (Modification) API from Clarivate — 1 operation(s) for searches (modification).
  name: Clarivate Searches (Modification) API
  phrasing_intents:
  - id: postReportsByReportIdSearchesModification
    intent: Run a sequence modification search
    question: How do I search for sequences with specific modifications?
  phrasing_ops: 1
  slug: clarivate-searches-modification-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Searches (Motif) API from Clarivate — 1 operation(s) for searches (motif).
  name: Clarivate Searches (Motif) API
  phrasing_intents:
  - id: postReportsByReportIdSearchesMotifp
    intent: Run a protein motif search
    question: How do I search for a protein motif pattern in Derwent sequences?
  phrasing_ops: 1
  slug: clarivate-searches-motif-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Session information endpoints
  name: Clarivate Session Info API
  phrasing_intents:
  - id: getInfo
    intent: Get current session info
    question: How do I check who I am logged in as in Derwent Sequence Search?
  phrasing_ops: 1
  slug: clarivate-session-info-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Status API from Clarivate — 1 operation(s) for status.
  name: Clarivate Status API
  phrasing_intents:
  - id: getAPIStatus
    intent: Check the SUSHI reporting service status
    question: Is the Web of Science SUSHI usage reporting service up right now?
  phrasing_ops: 1
  slug: clarivate-status-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Trademarks API from Clarivate — 3 operation(s) for trademarks.
  name: Clarivate Trademarks API
  phrasing_intents:
  - id: getTrademarkDocuments
    intent: Fetch several trademark documents by GUID
    question: How do I retrieve multiple full trademark records in one call?
  - id: getTrademarkDocument
    intent: Get one full trademark document
    question: How do I look up a single trademark record by its GUID?
  - id: searchTrademarks
    intent: Search and aggregate trademarks
    question: How do I search trademarks and group the results?
  phrasing_ops: 3
  slug: clarivate-trademarks-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The User Space API from Clarivate — 4 operation(s) for user space.
  name: Clarivate User Space API
  phrasing_intents:
  - id: readuserAttachmentSize
    intent: Get total size of my attachments
    question: How much storage are all my EndNote attachments currently taking up?
  - id: readuserAttachmentSpace
    intent: Get my attachment storage quota
    question: How much attachment storage do I have left in EndNote?
  - id: readuserSpace
    intent: Get my overall library usage and limits
    question: How many references and attachments can I still add to my library?
  - id: readuserReferenceSpace
    intent: Get my reference count and limit
    question: How many references do I have and how many more can I add?
  phrasing_ops: 4
  slug: clarivate-user-space-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Get Converis and component versions.
  name: Clarivate Version API
  phrasing_intents:
  - id: getConverisVersion
    intent: Get the Converis version
    question: Which Converis version is this installation running?
  - id: getComponentVersion
    intent: Get a Converis component's version
    question: How do I check the version of a single Converis component?
  phrasing_ops: 2
  slug: clarivate-version-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Web of Science Reviewer Locator API API from Clarivate — 2 operation(s) for web of science reviewer locator api.
  name: Clarivate Web of Science Reviewer Locator API
  phrasing_intents:
  - id: postRoot
    intent: Request reviewer recommendations
    question: How do I find expert peer reviewers for a manuscript?
  - id: getBySearchToken
    intent: Retrieve reviewer recommendations by token
    question: How do I get the reviewer recommendations for a search I already submitted?
  phrasing_ops: 2
  slug: clarivate-web-of-science-reviewer-locator-api-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: Response in xml format
  name: Clarivate XML API
  phrasing_intents:
  - id: getDocumentLevelMetricsByInstitutionIdXml
    intent: Get my institution's document metrics as XML
    question: How do I pull document level metrics for all of my institution's papers in a year as XML?
  - id: getDocumentLevelMetricsByInstitutionIdRecordCountXml
    intent: Count my institution's records for a year (XML)
    question: How many records are unified to my institution in a given year, in XML?
  - id: getDocumentLevelMetricsByUTXml
    intent: Get document metrics for a UT (XML)
    question: How do I get InCites metrics for one Web of Science accession number in XML?
  - id: getCheckValidUTsXml
    intent: Find invalid UTs in a list (XML)
    question: Which accession numbers in my list are not valid UTs, returned as XML?
  - id: getInCitesLastUpdatedXml
    intent: Get InCites data update times (XML)
    question: When were the InCites and Web of Science datasets last updated, in XML?
  phrasing_ops: 5
  slug: clarivate-xml-api
- baseURL: https://api.clarivate.com
  baseurl_source: declared
  description: The Graph QL API from Clarivate — 1 operation(s) for graph ql.
  name: Clarivate Graph QL API
  phrasing_intents:
  - id: postGraphql
    intent: Run a GraphQL query over LSH content
    question: Can I query several Clarivate life sciences content sets with one GraphQL request?
  phrasing_ops: 1
  slug: clarivate-graph-ql-api
artifact_total: 176
collections:
- collection_type: open
  name: Clarivate Web of Science Starter Documents API
  slug: open-clarivate-documents-api
- collection_type: open
  name: Clarivate Web of Science Starter Documents Journals API
  slug: open-clarivate-journals-api
- collection_type: open
  name: Clarivate Web of Science Starter API
  slug: open-clarivate
common:
- group: auth
  href: https://artifacts.apis.io/clarivate/scopes/clarivate-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/clarivate-scopes.yml
- group: design
  href: https://artifacts.apis.io/clarivate/vocabulary/clarivate-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clarivate-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/clarivate/hosts/clarivate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clarivate-hosts.yml
- group: other
  href: https://artifacts.apis.io/clarivate/vendors/clarivate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clarivate-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/clarivate/finops/clarivate-finops.yml
  title: ''
  type: FinOps
  url: finops/clarivate-finops.yml
- group: other
  href: https://artifacts.apis.io/clarivate/capabilities/clarivate-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/clarivate-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-ipdata-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-ipdata-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-converisreadapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-converisreadapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-dss-search-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-dss-search-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-wos-journal-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-wos-journal-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-endnote-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-endnote-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-legacy-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-legacy-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-converis-additional-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-converis-additional-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-incites-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-incites-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-wos-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-wos-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-sushi-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-sushi-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-cud-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-cud-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-ric-ai-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-ric-ai-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-cddi-counter-five-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-cddi-counter-five-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-ric-download-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-ric-download-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-wos-researcher-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-wos-researcher-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-wos-starter-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-wos-starter-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-woslite-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-woslite-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-lsh-download-ext-client-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-lsh-download-ext-client-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-wosrl-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-wosrl-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-cortellis-api-collection-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-cortellis-api-collection-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-patentmonitor-innography-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-patentmonitor-innography-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-reviewer-connect-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-reviewer-connect-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-ric-agent-hub-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-ric-agent-hub-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-ric-searchretrieve-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-ric-searchretrieve-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-sushi-status-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-sushi-status-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/clarivate/overlays/clarivate-twa-riskmark-integration-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/clarivate-twa-riskmark-integration-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://clarivate.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.clarivate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.clarivate.com/apis
- group: docs
  title: ''
  type: APIReference
  url: https://developer.clarivate.com/apis
- group: other
  title: ''
  type: APICatalog
  url: https://developer.clarivate.com/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.clarivate.com/help/application
- group: auth
  href: https://artifacts.apis.io/clarivate/authentication/clarivate-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clarivate-authentication.yml
- group: auth
  title: ''
  type: APIKeys
  url: https://developer.clarivate.com/help/api-access#key_access
- group: start
  title: ''
  type: SignUp
  url: https://developer.clarivate.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.clarivate.com/
- group: company
  title: ''
  type: Blog
  url: https://clarivate.com/news/
- group: company
  title: ''
  type: Newsroom
  url: https://clarivate.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clarivate
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clarivate
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clarivate.com/legal-center/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clarivate.com/privacy-center/
- group: commercial
  title: ''
  type: InterfaceLicense
  url: https://clarivate.com/wp-content/uploads/dlm_uploads/2019/08/End-User-Terms.pdf
- group: commercial
  href: https://artifacts.apis.io/clarivate/plans/clarivate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clarivate-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/clarivate/rate-limits/clarivate-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clarivate-rate-limits.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clarivate.com/
- group: operate
  href: https://artifacts.apis.io/clarivate/changelog/clarivate-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clarivate-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://clarivate.com/academia-government/release-notes/wos-apis/
- group: design
  href: https://artifacts.apis.io/clarivate/lifecycle/clarivate-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clarivate-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/clarivate/lifecycle/clarivate-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/clarivate-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/clarivate/conventions/clarivate-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clarivate-conventions.yml
- group: design
  href: https://artifacts.apis.io/clarivate/errors/clarivate-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clarivate-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clarivate/data-model/clarivate-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clarivate-data-model.yml
- group: design
  href: https://artifacts.apis.io/clarivate/conformance/clarivate-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clarivate-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://clarivate.com/trust-center/security-compliance/
- group: auth
  href: https://artifacts.apis.io/clarivate/security/clarivate-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clarivate-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://clarivate.com/trust-center/
- group: auth
  href: https://artifacts.apis.io/clarivate/security/clarivate-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/clarivate-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clarivate/security/clarivate-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clarivate-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clarivate/security/clarivate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clarivate-domain-security.yml
- group: build
  href: https://artifacts.apis.io/clarivate/packages/clarivate-packages.yml
  title: ''
  type: Packages
  url: packages/clarivate-packages.yml
- group: build
  href: https://artifacts.apis.io/clarivate/packages/clarivate-packages.yml
  title: ''
  type: SDKs
  url: packages/clarivate-packages.yml
- group: agent
  href: https://artifacts.apis.io/clarivate/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/clarivate/mcp/clarivate-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/clarivate-mcp.yml
- group: agent
  href: https://artifacts.apis.io/clarivate/agentic-access/clarivate-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clarivate-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/clarivate/json-ld/clarivate-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clarivate-context.jsonld
- group: design
  href: https://artifacts.apis.io/clarivate/rules/clarivate-rules.yml
  title: ''
  type: Spectral
  url: rules/clarivate-rules.yml
- group: docs
  href: https://artifacts.apis.io/clarivate/graphql/clarivate-graphql.yml
  title: ''
  type: X-GraphQLGated
  url: graphql/clarivate-graphql.yml
created: '2024-12-16'
description: Clarivate is a global information services company providing data, insights and analytics across academia and government, life sciences and healthcare, and intellectual property. It publishes 26 machine-readable API contracts through one developer portal at developer.clarivate.com, each fetchable at developer.clarivate.com/apis/<api>/swagger, and serves them through a single gateway at api.clarivate.com. The estate spans Web of Science publication and citation data, Journal Citation Reports metrics, InCites benchmarking, Derwent patent and trademark intelligence, Converis research information management, Cortellis life sciences intelligence, and COUNTER R5 usage reporting over NISO SUSHI. Access is by API key or OAuth 2.0 client credentials, issued per registered application; every plan but the Web of Science Starter Free Trial is entitled from an institutional subscription and approved by Clarivate.
finops:
- has_sources: true
  method: derived
  name: Clarivate Finops
  primary_unit: ''
  service_category: ''
  slug: clarivate-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clarivate.png
json_schemas:
- name: ArrayOfDates
  property_count: 0
  slug: clarivate-array-of-dates
- name: ArrayOfRecords
  property_count: 0
  slug: clarivate-array-of-records
- name: ArrayOfUTs
  property_count: 0
  slug: clarivate-array-of-uts
- name: CategoriesCited
  property_count: 2
  slug: clarivate-categories-cited
- name: CategoriesCiting
  property_count: 2
  slug: clarivate-categories-citing
- name: CategoryContextResponse
  property_count: 1
  slug: clarivate-category-context-response
- name: CategoryContextResponseXML
  property_count: 4
  slug: clarivate-category-context-response-xml
- name: CategoryList
  property_count: 2
  slug: clarivate-category-list
- name: CategoryRecord
  property_count: 6
  slug: clarivate-category-record
- name: CategoryReports
  property_count: 10
  slug: clarivate-category-reports
- name: CheckPackageStatusResult
  property_count: 4
  slug: clarivate-check-package-status-result
- name: CitationReportResponse
  property_count: 0
  slug: clarivate-citation-report-response
- name: combined_search_request_derwent_api
  property_count: 1
  slug: clarivate-combined-search-request-derwent-api
- name: ContentSetInfoResponse
  property_count: 2
  slug: clarivate-content-set-info-response
- name: ContentSetOntologiesResponse
  property_count: 2
  slug: clarivate-content-set-ontologies-response
- name: ContentSetOntologyResponse
  property_count: 2
  slug: clarivate-content-set-ontology-response
- name: COUNTER_database_report
  property_count: 2
  slug: clarivate-counter-database-report
- name: COUNTER_platform_report
  property_count: 2
  slug: clarivate-counter-platform-report
- name: DefaultResponse
  property_count: 5
  slug: clarivate-default-response
- name: doc_idmapping_request_derwent_api
  property_count: 1
  slug: clarivate-doc-idmapping-request-derwent-api
- name: document_availability_request_caselaw
  property_count: 2
  slug: clarivate-document-availability-request-caselaw
- name: document_availability_request_patent
  property_count: 3
  slug: clarivate-document-availability-request-patent
- name: document_by_ids_request_derwent_api
  property_count: 1
  slug: clarivate-document-by-ids-request-derwent-api
- name: document_by_pns_request_derwent_api
  property_count: 1
  slug: clarivate-document-by-pns-request-derwent-api
- name: Document
  property_count: 10
  slug: clarivate-document
- name: DocumentsList
  property_count: 2
  slug: clarivate-documents-list
- name: EntityDataList
  property_count: 5
  slug: clarivate-entity-data-list
- name: EntityData
  property_count: 13
  slug: clarivate-entity-data
- name: EntityDefinitionList
  property_count: 5
  slug: clarivate-entity-definition-list
- name: EntityDefinition
  property_count: 11
  slug: clarivate-entity-definition
- name: GraphQLQuery
  property_count: 1
  slug: clarivate-graph-qlquery
- name: GraphQLResponse
  property_count: 1
  slug: clarivate-graph-qlresponse
- name: JournalHistoryRecord
  property_count: 5
  slug: clarivate-journal-history-record
- name: JournalRecord
  property_count: 14
  slug: clarivate-journal-record
- name: JournalReports
  property_count: 10
  slug: clarivate-journal-reports
- name: JournalTitleYear
  property_count: 2
  slug: clarivate-journal-title-year
- name: JournalsCited
  property_count: 2
  slug: clarivate-journals-cited
- name: JournalsCiting
  property_count: 2
  slug: clarivate-journals-citing
- name: JsonApiPaginationMeta
  property_count: 2
  slug: clarivate-json-api-pagination-meta
- name: LinkEntityDataList
  property_count: 5
  slug: clarivate-link-entity-data-list
- name: LinkEntityData
  property_count: 11
  slug: clarivate-link-entity-data
- name: LinkEntityDefinitionList
  property_count: 5
  slug: clarivate-link-entity-definition-list
- name: LinkEntityDefinition
  property_count: 7
  slug: clarivate-link-entity-definition
- name: MakePredictionRequest
  property_count: 3
  slug: clarivate-make-prediction-request
- name: MakePredictionResponse
  property_count: 2
  slug: clarivate-make-prediction-response
- name: match_patent
  property_count: 1
  slug: clarivate-match-patent
- name: match_response_patent
  property_count: 2
  slug: clarivate-match-response-patent
- name: PaginationLinks
  property_count: 5
  slug: clarivate-pagination-links
- name: PaginationMeta
  property_count: 4
  slug: clarivate-pagination-meta
- name: Patent
  property_count: 5
  slug: clarivate-patent
- name: PeerReviewList
  property_count: 2
  slug: clarivate-peer-review-list
- name: PredictionsResponse
  property_count: 2
  slug: clarivate-predictions-response
- name: Project
  property_count: 3
  slug: clarivate-project
- name: PublicAgentMessageResponse
  property_count: 6
  slug: clarivate-public-agent-message-response
- name: PublicAgentRequest
  property_count: 2
  slug: clarivate-public-agent-request
- name: PublicAgentSuccessResponse
  property_count: 7
  slug: clarivate-public-agent-success-response
- name: records_request_caselaw
  property_count: 2
  slug: clarivate-records-request-caselaw
- name: records_request_patent
  property_count: 2
  slug: clarivate-records-request-patent
- name: records_request_trademark
  property_count: 2
  slug: clarivate-records-request-trademark
- name: ReferenceResponseXML
  property_count: 2
  slug: clarivate-reference-response-xml
- name: referencetype
  property_count: 2
  slug: clarivate-referencetype
- name: RequestPackageInput
  property_count: 6
  slug: clarivate-request-package-input
- name: RequestPackageResult
  property_count: 1
  slug: clarivate-request-package-result
- name: ResearcherDocument
  property_count: 2
  slug: clarivate-researcher-document
- name: ResearcherList
  property_count: 2
  slug: clarivate-researcher-list
- name: ResearcherRecord
  property_count: 8
  slug: clarivate-researcher-record
- name: Response
  property_count: 5
  slug: clarivate-response
- name: RetrieveResponseXML
  property_count: 1
  slug: clarivate-retrieve-response-xml
- name: roalibrary
  property_count: 6
  slug: clarivate-roalibrary
- name: roareference
  property_count: 8
  slug: clarivate-roareference
- name: search_by_ids_request_derwent_api
  property_count: 1
  slug: clarivate-search-by-ids-request-derwent-api
- name: search_by_pns_request_derwent_api
  property_count: 1
  slug: clarivate-search-by-pns-request-derwent-api
- name: SearchCreateParams
  property_count: 0
  slug: clarivate-search-create-params
- name: SearchInput
  property_count: 7
  slug: clarivate-search-input
- name: search_request_caselaw
  property_count: 7
  slug: clarivate-search-request-caselaw
- name: search_request_patent
  property_count: 7
  slug: clarivate-search-request-patent
- name: search_request_trademark
  property_count: 7
  slug: clarivate-search-request-trademark
- name: SearchResult
  property_count: 32
  slug: clarivate-search-result
- name: Search
  property_count: 3
  slug: clarivate-search
- name: SearchUpdateParams
  property_count: 1
  slug: clarivate-search-update-params
- name: Sequence
  property_count: 5
  slug: clarivate-sequence
- name: SessionInfo
  property_count: 1
  slug: clarivate-session-info
- name: SingleOppositionResponse
  property_count: 3
  slug: clarivate-single-opposition-response
- name: SubscriptionsInfoResult
  property_count: 1
  slug: clarivate-subscriptions-info-result
- name: SUSHI_consortium_member_list
  property_count: 4
  slug: clarivate-sushi-consortium-member-list
- name: SUSHI_report_list
  property_count: 5
  slug: clarivate-sushi-report-list
- name: SUSHI_service_status
  property_count: 5
  slug: clarivate-sushi-service-status
- name: uri
  property_count: 7
  slug: clarivate-uri
- name: UserDelegationList
  property_count: 5
  slug: clarivate-user-delegation-list
- name: UserDelegation
  property_count: 5
  slug: clarivate-user-delegation
- name: UserList
  property_count: 5
  slug: clarivate-user-list
- name: User
  property_count: 11
  slug: clarivate-user
- name: userspaceresource
  property_count: 9
  slug: clarivate-userspaceresource
- name: WosSearchResponse
  property_count: 2
  slug: clarivate-wos-search-response
- name: WosSearchResponseXML
  property_count: 2
  slug: clarivate-wos-search-response-xml
- name: WosShortSearchResponse
  property_count: 2
  slug: clarivate-wos-short-search-response
jsonld:
- class_count: 14
  name: Clarivate Context
  property_count: 0
  slug: clarivate-context
layout: provider
modified: '2026-09-05'
name: Clarivate
nav: Providers
network: true
overview: 'Clarivate publishes 61 API contracts indexed on the [APIs.io](https://apis.io/) network, including Administration - User data API, Administration - User Delegations API, Audit Info API, and 58 more. Tagged areas include Analytics, Bibliometrics, Citations, Data, and Drug Pipeline.


  The Clarivate catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clarivate''s developer surface includes documentation, API reference, getting-started guide, authentication, signup flow, support, engineering blog, and 67 more developer resources.'
plans:
- name: Clarivate Plans Pricing
  plan_count: 13
  slug: clarivate-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 13
  name: Clarivate Rate Limits
  slug: clarivate-rate-limits
rules:
- authorship: unmarked
  effective_rule_count: 47
  extends:
  - spectral:oas
  name: Clarivate API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: clarivate-rules
scopes:
- name: Clarivate Scopes
  scope_count: 0
  slug: clarivate-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 73.5
  coverage:
    artifact_dirs: 34
    catalog_earned: 86.0
    catalog_earned_first_party: 24.0
    catalog_gap: 29.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 81.6
    contract_governance: 33.3
    contract_quality: 67.6
    developer_ergonomics: 66.1
    discoverability: 83.9
    operational_transparency: 84.2
  previous_composite: 72.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 95.3
      total: 64
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 41.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/clarivate/clarivate-2026-06-20T174437.png
security:
- kind: authentication
  name: Clarivate Authentication
  slug: clarivate-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Clarivate Domain Security
  slug: clarivate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clarivate Vulnerability Disclosure
  slug: clarivate-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Clarivate Trust Center
  slug: clarivate-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, ISO/IEC 27032, ISO 22301, SOC 2 Type II, PCI DSS (SAQ A / A-EP / D / C-VT by product), FedRAMP, TX-RAMP (Level 1), StateRAMP (Moderate), AZ-RAMP, GDPR, Spain ENS (Esquema Nacional de Seguridad)
skill_count: 5
skills:
- name: clarivate-counter-sushi-harvest
  slug: clarivate-counter-sushi-harvest
- name: clarivate-derwent-patent-search
  slug: clarivate-derwent-patent-search
- name: clarivate-wos-document-lookup
  slug: clarivate-wos-document-lookup
- name: clarivate-wos-journal-metrics
  slug: clarivate-wos-journal-metrics
- name: clarivate-wos-researcher-profile
  slug: clarivate-wos-researcher-profile
slug: clarivate
tags:
- Analytics
- Bibliometrics
- Citations
- Data
- Drug Pipeline
- Insights
- Intellectual Property
- Life Sciences
- Patents
- Publications
- Research
- Scholarly Communication
website: https://clarivate.com/
---
