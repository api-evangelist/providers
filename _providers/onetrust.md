---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 349
  human_in_the_loop: 24
  name: Onetrust Agentic Access
  operation_count: 631
  slug: onetrust-agentic-access
  summary_line: 631 operations · 349 acting · 24 human-in-the-loop
api_count: 37
apis:
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Activity Log API from OneTrust — 1 operation(s) for activity log.
  name: OneTrust Activity Log API
  phrasing_intents:
  - id: getEventTypeFilterOptionsGET
    intent: List tracked activity event types
    question: Which user and system events does the activity log track?
  phrasing_ops: 1
  slug: onetrust-activity-log-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Applications APIs are used to manage application configurations and their associated consent experiences.
  name: OneTrust Applications API
  phrasing_intents:
  - id: createApplication
    intent: Register a mobile or CTV app for scanning
    question: How do I register a new mobile app so it can be scanned and get the consent SDK?
  - id: scanApplication
    intent: Upload an app build and start a scan
    question: How do I kick off an SDK scan by uploading my app binary?
  - id: getApplications
    intent: List registered applications
    question: Which mobile apps have I registered for consent scanning?
  - id: getApplicationBrandingAttributeList
    intent: Get an application's branding attributes
    question: What branding settings are configured for my app's consent UI?
  - id: updateApplicationBrandingAttributesForPublicApi
    intent: Update an application's branding attributes
    question: How do I change the branding of my app's consent experience?
  - id: getScans
    intent: List the scans run on an application
    question: What scans have been run against my app and what was their status?
  - id: getSingleScan
    intent: Get the result summary of one app scan
    question: What did a particular app scan find in terms of SDKs and permissions?
  - id: getScanPermissions
    intent: List permissions detected in an app scan
    question: Which device permissions did the scan detect in my app?
  phrasing_ops: 12
  slug: onetrust-applications-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Assessment Actions APIs are used to perform workflows on assessments, such as launching, approving, or creating tasks.
  name: OneTrust Assessment Actions API
  phrasing_intents:
  - id: reviewAssessmentUsingPOST
    intent: Complete an assessment review with a result
    question: Can I finish reviewing a submitted assessment and pick a result option?
  - id: createAssessmentUsingPOST_1
    intent: Launch an assessment (v2 endpoint)
    question: Can I still launch an assessment through the older v2 endpoint?
  - id: createBulkAssessmentUsingPOST
    intent: Launch assessments in bulk per inventory
    question: Can I create one assessment for each inventory item in a single request?
  - id: reassignAssessmentUsingPUT
    intent: Reassign an assessment's people or org
    question: Can I change the respondents or approvers on an assessment already in flight?
  - id: submitResponsesUsingPOST
    intent: Submit answers to assessment questions
    question: Can I post question responses to an assessment programmatically?
  - id: createAssessmentRiskUsingPOST
    intent: Flag a risk on an assessment question
    question: Can I raise a risk against a specific question on an assessment?
  - id: submitAssessmentUsingPOST
    intent: Submit an assessment for review
    question: What must be answered before an assessment can be sent for review?
  - id: createTaskUsingPOST
    intent: Create a task on an assessment
    question: Can I add a follow-up task to an assessment and assign it to someone?
  phrasing_ops: 13
  slug: onetrust-assessment-actions-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Assessment Management APIs are used to modify, link, and manage existing assessments.
  name: OneTrust Assessment Management API
  phrasing_intents:
  - id: archiveAssessmentsUsingPUT
    intent: Archive assessments
    question: How do I archive completed assessments in bulk?
  - id: addManualAssessmentLinksUsingPOST
    intent: Link assessments together
    question: How do I link one assessment to several others?
  - id: unarchiveAssessmentsUsingPUT
    intent: Unarchive assessments
    question: How do I restore archived assessments back to the Active list?
  - id: updateBasicAssessmentDetailsUsingPATCH
    intent: Edit an assessment's name, deadline or reminder
    question: How do I change an assessment's deadline or reminder?
  - id: updatePrimaryRecordUsingPUT
    intent: Set an assessment's primary record
    question: How do I set or replace the primary record an assessment is about?
  - id: softDeleteAssessmentUsingPUT
    intent: Move an assessment to the recycle bin
    question: How do I soft delete an assessment so it can still be restored?
  - id: addOrUpdateTagsUsingPUT
    intent: Replace an assessment's tags
    question: How do I tag an assessment?
  phrasing_ops: 7
  slug: onetrust-assessment-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Assessments APIs are used to retrieve assessment data and details.
  name: OneTrust Assessments API
  phrasing_intents:
  - id: getTagsUsingGET
    intent: List assessment tags
    question: What tags are available to label assessments?
  - id: getAllAssessmentBasicDetailsUsingGET
    intent: List assessments
    question: Which assessments exist in OneTrust and what stage is each in?
  - id: getAssessmentDeleteLogsUsingGET
    intent: Export the deleted-assessment audit log
    question: Who deleted an assessment and when?
  - id: getAssessmentResultsUsingGET
    intent: List assessment result options
    question: What result values can I choose when completing an assessment?
  - id: getLinkedAssessmentsInformationUsingGET
    intent: List assessments linked to a record
    question: Which assessments were copied, reassessed or triggered from a given record?
  - id: exportAssessmentUsingGET
    intent: Export full details of an assessment
    question: Can I export an assessment with its respondents, approvers, answers and risks?
  - id: getAssessmentRecordUsingGET
    intent: Get a lightweight assessment record
    question: Can I fetch just an assessment's sections, questions and responses without the risk data?
  - id: getAssessmentScoreProfilesWithQuestionBreakdownUsingGET
    intent: Get an assessment's score profiles
    question: How was an assessment scored question by question?
  phrasing_ops: 12
  slug: onetrust-assessments-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Attachments APIs are used to upload and obtain the location of files uploaded in the OneTrust Platform.
  name: OneTrust Attachments API
  phrasing_intents:
  - id: fileUpload
    intent: Upload a file to attach later
    question: How do I upload a document so I can attach it to a record?
  - id: fileLocation
    intent: Get the download URL of an uploaded file
    question: Where can I download a file I uploaded earlier?
  phrasing_ops: 2
  slug: onetrust-attachments-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Attachments V4 API from OneTrust — 1 operation(s) for attachments v4.
  name: OneTrust Attachments V4 API
  phrasing_intents:
  - id: getAttachmentDownloadTokenV4
    intent: Get a download token for an attachment
    question: How do I download an attachment's file content?
  phrasing_ops: 1
  slug: onetrust-attachments-v4-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Attribute Management APIs are used to manage attributes associated with AI Governance entities.
  name: OneTrust Attribute Management API
  phrasing_intents:
  - id: addOptionsUsingPOST
    intent: Add options to an attribute
    question: How do I add choices to a picklist attribute on AI models?
  - id: addAttributeUsingPOST
    intent: Add an attribute to a schema
    question: How do I add a custom field to the AI system or dataset schema?
  - id: disableAttributeUsingPUT
    intent: Disable a schema attribute
    question: How do I hide an attribute from AI governance forms?
  - id: enableAttributeUsingPUT
    intent: Enable a schema attribute
    question: How do I re-enable an attribute I previously disabled?
  phrasing_ops: 4
  slug: onetrust-attribute-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage and retrieve audit logs for user activities, including login history and access patterns. These endpoints help you monitor security events, track user authentication attempts, and maint
  name: OneTrust Audit Records API
  phrasing_intents:
  - id: loginHistory
    intent: Get login history for audit
    question: Who logged in to the account over the last month?
  - id: userActivity
    intent: Audit changes made to a user's profile
    question: What changes were made to a user's roles and organizations over time?
  phrasing_ops: 2
  slug: onetrust-audit-records-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage the complete audit lifecycle including creation, updates, deletion, scope assignment, and retrieval with support for approvers, auditors, and custom attributes.
  name: OneTrust Audits API
  phrasing_intents:
  - id: deleteScopeUsingDELETE
    intent: Remove a control from an audit's scope
    question: Can I take a control or control implementation out of an audit's scope?
  - id: validateAndCreateAuditUsingPOST
    intent: Create an audit
    question: What do I need to set up a new audit against a framework?
  - id: getAuditListPageUsingPOST
    intent: Search and list audits
    question: Which audits are currently set up, and who are the auditors on each?
  - id: getAuditDetailUsingGET
    intent: Get an audit
    question: Can I pull up a single audit by its ID?
  - id: validateAndUpdateAuditUsingPUT
    intent: Update an audit's auditors and approvers
    question: Can I change the auditors or approvers on an existing audit?
  - id: deleteAuditUsingDELETE
    intent: Delete an audit
    question: Is deleting an audit permanent, and what goes with it?
  - id: validateAndReassignScopesUsingPUT
    intent: Update an audit's scope
    question: Can I change which controls are in scope for an existing audit?
  phrasing_ops: 7
  slug: onetrust-audits-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage cookie consent banner configuration and behavior.
  name: OneTrust Banner API
  phrasing_intents:
  - id: get_Banner
    intent: Get cookie banner data for an app
    question: What does my app need to render the consent banner?
  phrasing_ops: 1
  slug: onetrust-banner-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Bulk Export APIs are used to extract large volumes of cookie receipts, consent receipts, and data subjects.
  name: OneTrust Bulk Export API
  phrasing_intents:
  - id: getExportRunsGET
    intent: List bulk exports
    question: What bulk exports have I run and what state are they in?
  - id: startExportRunPost
    intent: Start a bulk data export
    question: How do I export consent receipts in bulk for a date range?
  - id: getCreditsInformationGET
    intent: Check remaining bulk export credits
    question: How many bulk export credits do I have left?
  - id: getExportRunDetailsGet
    intent: Check the progress of a bulk export
    question: Is my bulk export finished yet?
  - id: cancelBulkExportDELETE
    intent: Cancel an unfinished bulk export
    question: How do I stop a bulk export that is still running?
  - id: getAttachmentDownloadCommandsGET
    intent: Get download details for a bulk export
    question: How do I download the file produced by a finished bulk export?
  - id: getPaginatedAttachmentDownloadCommandsGET
    intent: Page through download details of a large export
    question: My bulk export produced many files — how do I page through their download links?
  phrasing_ops: 7
  slug: onetrust-bulk-export-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage emission factors and emission transactions.
  name: OneTrust Carbon Management API
  phrasing_intents:
  - id: getAllEmissionFactorsBasicEntityDetails
    intent: List emission factors
    question: Which emission factors are set up for carbon accounting?
  - id: addEmissionFactor
    intent: Create an emission factor
    question: How do I add a new emission factor?
  - id: addEmissionTransaction
    intent: Record an emission transaction
    question: Can I log an emissions activity against an emission factor?
  - id: findAllByTypeAndCriteria
    intent: List emission records by type
    question: Can I filter emission records by criteria?
  phrasing_ops: 4
  slug: onetrust-carbon-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage catalog search operations with basic functionality and providing comprehensive filtering, faceting, and field selection capabilities for data asset discovery.
  name: OneTrust Catalog Search V1 API
  phrasing_intents:
  - id: externalSearch
    intent: Search the data catalog
    question: Which data assets in the catalog mention customer email?
  - id: get_v1-field-details
    intent: List catalog search fields
    question: What fields can I search or filter on in the data catalog?
  phrasing_ops: 2
  slug: onetrust-catalog-search-v1-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage catalog search operations with enhanced scalability, featuring continuation token-based pagination for handling large volumes of search results and improved performance for enterprise-s
  name: OneTrust Catalog Search V2 API
  phrasing_intents:
  - id: externalSearch-using-continuationtoken
    intent: Search the data catalog with continuation
    question: How do I page through large data catalog search results with a continuation token?
  phrasing_ops: 1
  slug: onetrust-catalog-search-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Categorizations API from OneTrust — 2 operation(s) for categorizations.
  name: OneTrust Categorizations API
  phrasing_intents:
  - id: getCategorizedCookiesUsingGET
    intent: Categorize cookies by name and host
    question: Is a given cookie on my site strictly necessary, functional or targeting?
  - id: getCategorizedCookiesWithCookieIdsUsingGET
    intent: Categorize cookies by cookie ID
    question: Can I categorize cookies when I only have their cookie IDs?
  phrasing_ops: 2
  slug: onetrust-categorizations-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Classification APIs are used to manage custom data classifiers and classification rules for Data Discovery.
  name: OneTrust Classification API
  phrasing_intents:
  - id: listDetectors
    intent: List custom data classifiers
    question: Which custom classifiers have we defined for data discovery?
  - id: createDetector
    intent: Create a custom data classifier
    question: How do I teach data discovery to recognize a new kind of sensitive data?
  - id: getDetectorByClassifierName
    intent: Get a custom classifier by name
    question: What detection rules does a given custom classifier use?
  - id: updateDetector
    intent: Update a custom classifier
    question: How do I change the definition of an existing custom classifier?
  - id: deleteDetector
    intent: Delete a custom classifier
    question: How do I remove a custom classifier we no longer use?
  phrasing_ops: 5
  slug: onetrust-classification-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Collection Points APIs are used to manage where and how consent is collected.
  name: OneTrust Collection Points API
  phrasing_intents:
  - id: getCollectionPointsUsingGET
    intent: List consent Collection Points
    question: Which Collection Points are capturing consent across my sites and forms?
  - id: createCollectionPointUsingPOST
    intent: Create a draft Collection Point
    question: How do I set up a new place to capture consent, like a web form?
  - id: getTokenUsingGET
    intent: Get the JWT for a Collection Point
    question: Where do I get the token to send consent receipts for a Collection Point?
  - id: editCollectionPointUsingPUT
    intent: Edit a draft Collection Point
    question: How do I change a Collection Point that is still in draft?
  - id: disableCollectionPointUsingPUT
    intent: Enable or disable a Collection Point
    question: How do I stop a Collection Point from collecting consent?
  phrasing_ops: 5
  slug: onetrust-collection-points-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Collection Points V2 APIs are used to manage collection points using version 2 of the API.
  name: OneTrust Collection Points V2 API
  phrasing_intents:
  - id: getCollectionPointsUsingGET_1
    intent: List collection points
    question: Which consent collection points exist, and in what versions?
  - id: createVersionUsingPOST
    intent: Create a new collection point version
    question: Can I start a new draft version of an active collection point?
  phrasing_ops: 2
  slug: onetrust-collection-points-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs for managing Consent Attachments.
  name: OneTrust Consent Attachments API
  phrasing_intents:
  - id: uploadConsentAttachments
    intent: Upload a written consent file
    question: How do I store a signed consent form as proof of consent?
  - id: downloadGivenConsentAttachments
    intent: Download one consent attachment
    question: How do I download a single consent file attached to a person?
  - id: removeGivenConsentAttachmentRefs
    intent: Remove one consent attachment
    question: How do I detach a single consent file from a data subject?
  - id: removeAllConsentAttachmentRefs
    intent: Remove all consent attachments for a person
    question: How do I clear every consent file attached to a data subject?
  - id: downloadConsentAttachments
    intent: Download all consent attachments for a person
    question: How do I get every consent file stored for one data subject?
  phrasing_ops: 5
  slug: onetrust-consent-attachments-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs for managing Consent Groups and their configurations.
  name: OneTrust Consent Groups API
  phrasing_intents:
  - id: getConsentGroupListUsingGET
    intent: List consent groups
    question: What consent groups have been set up in OneTrust?
  - id: createConsentGroupUsingPOST
    intent: Create a consent group
    question: How do I create a new consent group for households or accounts?
  - id: getConsentGroupSettingsUsingGET
    intent: Get purpose status priority scores
    question: What priority score does each purpose status have for consent groups?
  - id: updateConsentGroupSettingsUsingPUT
    intent: Update purpose status priority scores
    question: How do I change which purpose status takes precedence in a consent group hierarchy?
  - id: getConsentGroupUsingGET
    intent: Get a consent group
    question: How do I view one consent group's purpose rules and members?
  - id: addConsentGroupsToConsentGroupUsingPOST
    intent: Nest consent groups under a parent group
    question: How do I make consent groups children of a parent consent group?
  - id: unlinkConsentGroupUsingDELETE
    intent: Remove child consent groups from a parent
    question: How do I detach child consent groups from their parent group?
  - id: addDataSubjectsToConsentGroupUsingPOST
    intent: Add data subjects to a consent group
    question: How do I put individual data subjects into a consent group?
  phrasing_ops: 12
  slug: onetrust-consent-groups-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: API for optimizing consent rate.
  name: OneTrust Consent Rate Optimization API
  phrasing_intents:
  - id: CrossDeviceConsentUsingDELETE
    intent: Delete cross-device consents and receipts
    question: Can I erase cross-device consents and their receipts for certain users?
  phrasing_ops: 1
  slug: onetrust-consent-rate-optimization-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Consent Receipts APIs are used to create consent receipts from a collection point to store data subject consent.
  name: OneTrust Consent Receipts API
  phrasing_intents:
  - id: createConsentReceiptUsingPOST
    intent: Record a consent receipt from a collection point
    question: How do I record that someone just gave or withdrew consent through a collection point?
  - id: createBulkConsentReceiptUsingPOST
    intent: Import consent receipts in bulk
    question: How do I import a large backlog of consent transactions efficiently?
  - id: createIdentifiedConsentReceiptUsingPOST
    intent: Record consent for an identified data subject
    question: How do I record consent for a known user identified by email rather than a cookie?
  phrasing_ops: 3
  slug: onetrust-consent-receipts-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Contracts APIs are used to manage vendor contract operations including contract creation, updates, search functionality, contract type management, and schema configuration for comprehensive contra
  name: OneTrust Contracts API
  phrasing_intents:
  - id: createVendorContractUsingPOST
    intent: Create a vendor contract
    question: How do I record a new contract with a vendor?
  - id: getContractSchemaUsingGET
    intent: Get the contract attribute schema
    question: What custom attributes can a vendor contract have?
  - id: fetchAllContractTypesUsingGET
    intent: List contract types
    question: What contract types are available, like MSA or DPA?
  - id: searchContractByVendorAndCriteriaUsingPOST
    intent: Search a vendor's contracts
    question: What contracts do we have with a given vendor?
  - id: removeVendorContractUsingDELETE
    intent: Delete a contract
    question: How do I delete a vendor contract?
  - id: loadVendorContractByContractIdUsingGET
    intent: Get a contract
    question: When was a contract approved and who approved it?
  - id: updateVendorContractUsingPUT
    intent: Update a vendor contract
    question: How do I change the status or expiration of an existing contract?
  phrasing_ops: 7
  slug: onetrust-contracts-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to handle control implementation operations including creation, updates, entity associations, attachment management, and comprehensive search across multiple entity types.
  name: OneTrust Control Implementations API
  phrasing_intents:
  - id: findAllControlImplementationsAttributesAndOptionsByUsingPOST
    intent: Search control implementation attributes
    question: Which attributes and options can a control implementation have?
  - id: findAllControlImplementationsUsingPOST
    intent: List control implementations
    question: What control implementations exist across all my frameworks?
  - id: getControlImplementationDetailsUsingGET
    intent: Get a control implementation
    question: What framework and category does a specific control implementation belong to?
  - id: updateControlImplementationByImplementationIdUsingPUT
    intent: Update a control implementation
    question: Can I set a control implementation's status and effectiveness?
  - id: removeControlImplementationByEntityAndImplementationIdUsingDELETE
    intent: Delete a control implementation from an entity
    question: Can I remove a control implementation from a vendor or asset?
  - id: addAttachmentsToImplementationUsingPOST
    intent: Attach files to a control implementation
    question: Can I attach evidence files to a control implementation?
  - id: findAssociatedControlImplementationsUsingPOST
    intent: List control implementations for an entity
    question: Which controls are implemented on a particular vendor, asset or risk?
  phrasing_ops: 7
  slug: onetrust-control-implementations-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to create and manage relationships between controls through bulk linking operations with support for various relationship types and custom parameters.
  name: OneTrust Control Links API
  phrasing_intents:
  - id: bulkCreateLinksUsingPOST
    intent: Link a control to related controls
    question: Can I link one control to several related controls in the library?
  phrasing_ops: 1
  slug: onetrust-control-links-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage the complete control lifecycle including creation, updates, deletion, retrieval, and entity type management with framework integration and custom attributes.
  name: OneTrust Controls API
  phrasing_intents:
  - id: addControlUsingPOST
    intent: Create a control
    question: How do I add a new control to the Controls Library?
  - id: findControlsByCriteriaUsingPOST_1
    intent: Search controls
    question: What controls are in my Controls Library?
  - id: updateControlUsingPUT_1
    intent: Update a control
    question: How do I change a control's description or implementation guidance?
  - id: removeControlUsingDELETE_1
    intent: Delete a control
    question: How do I remove a control from the Controls Library?
  - id: getAllEnabledControlEntityTypesUsingGET
    intent: List control entity source types
    question: Which entity source types can controls be attached to?
  - id: getAllRelatedControlEntityTypesUsingGET
    intent: List related control entity types
    question: What entity types can be related to controls?
  phrasing_ops: 6
  slug: onetrust-controls-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Cookies APIs are used to manage cookie definitions, categories, and their properties.
  name: OneTrust Cookies API
  phrasing_intents:
  - id: getCategorizedCookies
    intent: Look up categorized cookies for a domain
    question: What category has each cookie on my domain been assigned?
  - id: bulkEditCookies
    intent: Edit scanned cookies in bulk
    question: How do I edit many existing web scan cookies at once?
  - id: bulkAddCookies
    intent: Add cookies to web scans in bulk
    question: How do I add a batch of cookies to my web scan results?
  - id: bulkDeleteCookies
    intent: Delete scanned cookies by ID or filter
    question: How do I delete scanned cookies in bulk?
  - id: getCookiesByFilter
    intent: Filter scanned cookies in a given language
    question: Which scanned cookies are third-party or long-lived in a given language view?
  - id: recategorizeCookiesByScan
    intent: Recategorize the cookies from a scan
    question: How do I rerun cookie categorization for a completed website scan?
  - id: createNewCookie
    intent: Create a single new cookie
    question: How do I create one cookie with its host, lifespan and category?
  - id: updateCookie
    intent: Update a single cookie's details
    question: How do I change the description or category of a single cookie by its cookie ID?
  phrasing_ops: 9
  slug: onetrust-cookies-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage credential operations including creation, updates, deletion, retrieval, and secure reference key management for multiple system authentication types.
  name: OneTrust Credentials API
  phrasing_intents:
  - id: getCredentials
    intent: List data discovery credentials
    question: Which credentials are configured for data discovery scans?
  - id: updateCredential
    intent: Update a credential
    question: Can I change the reference key on an existing credential?
  - id: createCredential
    intent: Create a credential
    question: How do I add a credential for a scan of a new system?
  - id: getCredentialById
    intent: Get a credential
    question: What system and reference key does a specific credential use?
  - id: deleteCredential
    intent: Delete a credential
    question: Does deleting a credential remove its reference keys too?
  phrasing_ops: 5
  slug: onetrust-credentials-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Custom Index Management API from OneTrust — 2 operation(s) for custom index management.
  name: OneTrust Custom Index Management API
  phrasing_intents:
  - id: createIndex
    intent: Start building a custom data element index
    question: How do I speed up searches on a data element with a custom index?
  - id: getIndexCreationStatus
    intent: Check the status of a custom index build
    question: Has my custom search index finished building?
  phrasing_ops: 2
  slug: onetrust-custom-index-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage and execute custom data discovery scans across specified data sources.
  name: OneTrust Custom Scan API
  phrasing_intents:
  - id: getEligibleJobsUsingGET
    intent: List pending custom connector scan jobs
    question: Which custom connector scan jobs are pending for a data source?
  - id: catalogDataUsingPOST
    intent: Submit metadata for cataloging
    question: Can a custom connector send table and column metadata to be cataloged?
  - id: classifyDataUsingPOST
    intent: Submit content for classification
    question: Can a custom connector send sample content to be classified for personal data?
  - id: updateJobStatusUsingPUT
    intent: Update a scan job's status
    question: Can my connector report that a scan job finished or failed?
  phrasing_ops: 4
  slug: onetrust-custom-scan-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Asset Attributes API from OneTrust — 2 operation(s) for data asset attributes.
  name: OneTrust Data Asset Attributes API
  phrasing_intents:
  - id: getDataAssetAttributeByName
    intent: Get a data asset attribute
    question: What does a specific data asset attribute in Attribute Manager define?
  - id: getAllDataAssetAttributeNames
    intent: List data asset attributes
    question: Which data asset attributes are defined in Attribute Manager?
  phrasing_ops: 2
  slug: onetrust-data-asset-attributes-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Asset Management API from OneTrust — 2 operation(s) for data asset management.
  name: OneTrust Data Asset Management API
  phrasing_intents:
  - id: deleteDataAssetTagAssociationsV1
    intent: Remove tags from a data asset
    question: Can I untag several tags from a data asset at once?
  - id: deleteDataAssetTermAssociationsV1
    intent: Remove glossary terms from a data asset
    question: Can I detach several glossary terms from a data asset at once?
  phrasing_ops: 2
  slug: onetrust-data-asset-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Assets APIs are used to manage data asset metadata.
  name: OneTrust Data Assets API
  phrasing_intents:
  - id: createOrUpsertDataAssetV1
    intent: Create or upsert a data asset
    question: How do I add a table or column to the data catalog under its parent?
  - id: getDataAssetV1
    intent: Get a data asset
    question: Which terms and tags are associated with a given data asset?
  - id: deleteDataAssetV1
    intent: Delete a data asset and its children
    question: Does deleting a data asset also remove its child objects?
  - id: updateDataAssetV1
    intent: Modify a data asset
    question: Can I change a data asset's owners and stewards?
  - id: createDataAssetTagAssociationsV1
    intent: Tag a data asset
    question: Can I add tags to a data asset without replacing its other details?
  - id: createDataAssetTermAssociationsV1
    intent: Link glossary terms to a data asset
    question: Can I attach business glossary terms to a data asset?
  phrasing_ops: 6
  slug: onetrust-data-assets-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage data sources including creation, retrieval, updates, deletion, and comprehensive filtering with support for multiple system types and asset integration.
  name: OneTrust Data Sources API
  phrasing_intents:
  - id: getAllUsingGET_1
    intent: List data discovery data sources
    question: Which data sources are connected for data discovery scanning?
  - id: upsertSourceSystemV3UsingPUT
    intent: Create or update a data source
    question: How do I register a new database or system for data discovery?
  - id: getDataSourceByIdUsingGET_1
    intent: Get a data source
    question: What settings does a particular data source have?
  - id: deleteSystemUsingDELETE_1
    intent: Delete a data source
    question: How do I remove a data source and its scan results?
  phrasing_ops: 4
  slug: onetrust-data-sources-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subject Access Request (DSAR) API from OneTrust — 1 operation(s) for data subject access request (dsar).
  name: OneTrust Data Subject Access Request (DSAR) API
  phrasing_intents:
  - id: post_Dsar
    intent: Submit a global opt-out request from an app
    question: How does my mobile app submit a global opt-out for a user?
  phrasing_ops: 1
  slug: onetrust-data-subject-access-request-dsar-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subject Groups APIs are used to manage groups of data subjects.
  name: OneTrust Data Subject Groups API
  phrasing_intents:
  - id: getLinkedIdentityGroupsUsingGET
    intent: List data subject groups
    question: Which Data Subject Groups exist, and how many people are in each?
  - id: createLinkedIdentityGroupUsingPOST
    intent: Create a data subject group
    question: Can I link several identifiers of the same person into one group?
  - id: getLinkedIdentityGroupUsingGET
    intent: Get a data subject group
    question: Which data subjects are inside one Data Subject Group?
  - id: updateLinkedIdentityGroupUsingPUT
    intent: Update a data subject group
    question: Can I change the primary identifier of a Data Subject Group?
  - id: deleteUsingDELETE
    intent: Delete a data subject group
    question: Can I break up a Data Subject Group I no longer need?
  phrasing_ops: 5
  slug: onetrust-data-subject-groups-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subjects V4 APIs are used to manage data subject information, preferences, and consent records.
  name: OneTrust Data Subject Groups V4 API
  phrasing_intents:
  - id: getDataSubjectGroupsListV4
    intent: List Data Subject Groups
    question: What Data Subject Groups exist for linking identities like a household?
  - id: getLinkedIdentityGroupsByDataSubjectV4
    intent: List the groups a data subject belongs to
    question: Which Data Subject Groups is a particular person part of?
  - id: createDataSubjectGroupV4
    intent: Create a Data Subject Group
    question: How do I group several data subjects so consent can be shared between them?
  - id: updateDataSubjectGroupV4
    intent: Update a Data Subject Group's members
    question: How do I add or remove people from an existing Data Subject Group?
  - id: getLinkedIdentityGroupMembersV4
    intent: List members of a Data Subject Group
    question: Who are the members of a given Data Subject Group?
  phrasing_ops: 5
  slug: onetrust-data-subject-groups-v4-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subjects APIs are used to manage individuals whose data is being processed.
  name: OneTrust Data Subjects API
  phrasing_intents:
  - id: createOrUpdateDataSubjectUsingPOST
    intent: Create or update a data subject's data elements
    question: Can I add a new data subject or update their profile fields?
  - id: mergeDataSubjectsUsingPOST
    intent: Merge duplicate data subjects
    question: Can I merge duplicate consent records for the same person into one?
  - id: getDataSubjectProfileUsingGET
    intent: List data subject consent profiles
    question: Which data subjects have been updated since a given date?
  - id: getDataSubjectPurposesByIdentifierUsingGET
    intent: List a data subject's purposes (deprecated)
    question: Is there a legacy call that returns only the purposes for one data subject?
  phrasing_ops: 4
  slug: onetrust-data-subjects-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subjects V2 APIs are used to manage data subjects using version 2 of the API.
  name: OneTrust Data Subjects V2 API
  phrasing_intents:
  - id: getDataSubjectsUsingGET
    intent: List consent data subjects
    question: Which data subjects have consent records, and what data elements do they have?
  - id: deleteDataSubjectProfilesUsingDELETE
    intent: Delete purposes from data subjects
    question: How do I remove specific consent purposes from a person's profile?
  - id: searchDataSubjectsPostUsingPOST
    intent: Search consent data subjects
    question: How do I find data subjects by a data element value like email?
  - id: deletePurposeFromDataSubjectUsingDELETE
    intent: Remove a purpose from all data subjects
    question: How do I wipe one consent purpose from everyone at scale?
  - id: DeleteDataSubjectProfileUsingDELETE
    intent: Permanently delete data subjects
    question: How do I permanently delete data subjects from consent management?
  phrasing_ops: 5
  slug: onetrust-data-subjects-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subjects V3 APIs are used to manage data subject information, preferences, and consent records.
  name: OneTrust Data Subjects V3 API
  phrasing_intents:
  - id: getV3DatasubjectProfilesUsingPOST
    intent: List data subject profiles (v3 preferences)
    question: Should new integrations avoid the v3 preferences data subject list?
  - id: getV3DatasubjectsProfileUsingGet
    intent: Get a data subject profile (v3 preferences)
    question: Can I fetch one person's profile from the v3 preferences API?
  phrasing_ops: 2
  slug: onetrust-data-subjects-v3-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Data Subjects V4 APIs are used to manage data subject information, preferences, and consent records.
  name: OneTrust Data Subjects V4 API
  phrasing_intents:
  - id: deleteDataSubjectUsingTTL
    intent: Delete a data subject
    question: Can I delete a data subject's consent profile entirely?
  - id: deletePurposeFromDataSubjectsUsingTTL
    intent: Remove purposes from a data subject
    question: Can I remove just certain purposes from a data subject without deleting them?
  - id: getDataSubjectsV4
    intent: List data subjects updated in a date range
    question: Which data subjects were updated between two dates?
  - id: getDataSubjectBasicDetailsV4
    intent: Get a data subject's basic details
    question: Can I get only a data subject's basic details, such as when it was created and last transacted?
  - id: getDataSubjectDetailsV4
    intent: Get a data subject's full consent details
    question: Can I see everything about a data subject, including purposes and email link tokens?
  - id: getAllProfilesByDataSubjectV4
    intent: List all purposes for one data subject
    question: Which purposes has a given person interacted with, and what is each status?
  - id: getDataSubjectProfilesV4
    intent: List purpose details across all data subjects
    question: What is the maximum date range for pulling purpose details across all data subjects?
  - id: getDataSubjectProfilesUnorderedV4
    intent: Bulk-pull unordered purpose details
    question: Is there a faster, unsorted way to export purpose details for all data subjects?
  phrasing_ops: 11
  slug: onetrust-data-subjects-v4-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Deduplicate Data Subjects APIs are used to merge duplicate data subject profiles.
  name: OneTrust Deduplicate Data Subjects API
  phrasing_intents:
  - id: mergeDatasubjectUsingPOST
    intent: Merge duplicate data subjects
    question: Can I merge duplicate data subjects into one consent profile?
  - id: exportduplicatedatasubject
    intent: Generate a duplicate data subjects export
    question: Can I get a spreadsheet of duplicate data subjects emailed to a user?
  - id: getPagedMergeRequestUsingGET
    intent: List scheduled duplicate exports
    question: Which scheduled exports of duplicate data subjects do I have?
  - id: scheduleMergeRequestUsingPOST
    intent: Schedule a duplicate data subjects export
    question: Can I schedule a recurring export of duplicate data subjects?
  - id: getMergeRequestUsingGET
    intent: Get a scheduled duplicate export
    question: What is the status of one scheduled duplicate export?
  - id: deleteMergeRequestUsingDELETE
    intent: Delete a scheduled duplicate export
    question: Can I stop and remove a scheduled duplicate export?
  phrasing_ops: 6
  slug: onetrust-deduplicate-data-subjects-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to retrieve a paginated list of deletion certificates.
  name: OneTrust Deletion Certificates API
  phrasing_intents:
  - id: getListOfDeletionCertificates
    intent: List deletion certificates
    question: How do I prove a data subject's consent records were deleted?
  phrasing_ops: 1
  slug: onetrust-deletion-certificates-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Document Attachments APIs are used to manage attachments on document objects such as policies, standards, procedures, and privacy notices.
  name: OneTrust Document Attachments API
  phrasing_intents:
  - id: addDocumentToPolicy
    intent: Attach files to a policy document
    question: Can I attach supporting files to a policy or procedure?
  phrasing_ops: 1
  slug: onetrust-document-attachments-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Document Gateway API provides secure document download functionality using tokens from the Document Service V4.
  name: OneTrust Document Gateway API
  phrasing_intents:
  - id: download
    intent: Download a document or attachment
    question: Can I download an attachment once I have a download token?
  phrasing_ops: 1
  slug: onetrust-document-gateway-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Documents APIs are used to manage document objects such as policies, standards, procedures, and privacy notices.
  name: OneTrust Documents API
  phrasing_intents:
  - id: createPolicy
    intent: Create a policy or standard document
    question: How do I create a new policy, standard or procedure document?
  - id: getLatestPolicies
    intent: List policy documents by type
    question: Which policies or procedures do we currently have?
  - id: getPolicy
    intent: Get a policy document
    question: What are the details of a specific policy or procedure?
  - id: getPublishedPolicyVersion
    intent: Get a document's published version as of a date
    question: Which version of a policy was in effect on a given date?
  - id: createPolicyVersions
    intent: Create a new document version
    question: How do I start a new version of an existing policy?
  phrasing_ops: 5
  slug: onetrust-documents-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Domain Data API from OneTrust — 1 operation(s) for domain data.
  name: OneTrust Domain Data API
  phrasing_intents:
  - id: domaindata
    intent: Get banner templates and vendor lists for a domain
    question: What cookie consent models and vendor lists are configured for my domain?
  phrasing_ops: 1
  slug: onetrust-domain-data-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Domains APIs are used to manage domain configurations and cookie scanning settings.
  name: OneTrust Domains API
  phrasing_intents:
  - id: deleteDomain
    intent: Delete a domain
    question: Can I remove a domain from the cookie consent setup?
  - id: createDomainGroup
    intent: Create or update a domain group (CMP v1)
    question: Can I group several URLs under one domain using the CMP v1 endpoint?
  - id: getBrandingAttributeList
    intent: Get a domain's branding attributes
    question: Which branding colors and styles are set on a domain's banner?
  - id: updateBrandingAttributesForPublicApi
    intent: Update a domain's branding attributes
    question: Can I change the branding attributes of a domain's consent banner?
  - id: scheduleScans
    intent: Schedule website scans
    question: Can I schedule cookie scans for several domains at once?
  - id: bulkCancelDomainSchedule
    intent: Cancel scheduled website scans
    question: Can I cancel scans that are already scheduled?
  - id: createDomainGroupUsingPOST
    intent: Create or update a domain group (legacy v1)
    question: Is there an older v1 domains path for creating a domain group?
  phrasing_ops: 7
  slug: onetrust-domains-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs for managing DROP records and privacy requests
  name: OneTrust DROP Management API
  phrasing_intents:
  - id: updateDropUsingPUT
    intent: Update a DROP record's status
    question: How do I update the status of a DROP deletion record?
  - id: createDropRequestUsingPOST
    intent: Open a data subject request from a DROP record
    question: How do I turn a DROP record into a data subject request?
  phrasing_ops: 2
  slug: onetrust-drop-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Engagements APIs are used to manage vendor engagement operations including creating, retrieving, updating, and searching engagements with comprehensive attribute management, status control, workfl
  name: OneTrust Engagements API
  phrasing_intents:
  - id: getEngagementSchemaUsingGET
    intent: Get the engagement attribute schema
    question: What attributes and options can I set on a vendor engagement?
  - id: loadEngagementByEngagementIdUsingGet
    intent: Get an engagement
    question: Which vendor, workflow and attributes belong to a specific engagement?
  - id: updateEngagementUsingPUT
    intent: Replace an engagement's details
    question: How do I fully update a vendor engagement's owner, dates and scope?
  - id: removeEngagementUsingDELETE
    intent: Delete an engagement
    question: How do I delete a vendor engagement I no longer need?
  - id: updateEngagementUsingPATCH
    intent: Partially update an engagement
    question: Can I change a single field on an engagement without resending the rest?
  - id: updateEngagementStatus
    intent: Change an engagement's status
    question: How do I mark a vendor engagement as active or inactive?
  - id: loadEngagementUsingGET
    intent: Search engagements
    question: Which engagements do we have with a particular vendor?
  - id: createEngagementUsingPOST
    intent: Create a vendor engagement
    question: How do I start a new engagement with a vendor?
  phrasing_ops: 8
  slug: onetrust-engagements-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Entity Management APIs are used to manage AI Governance entities.
  name: OneTrust Entity Management API
  phrasing_intents:
  - id: addEntityUsingEntityTypeIdOrEntityTypeNameUsingPOST
    intent: Create an AI governance entity
    question: How do I register a new AI model or dataset in AI Governance?
  - id: findAllByTypeIdAndCriteriaUsingPOST
    intent: Search AI entities with full details
    question: How do I get every attribute of AI models matching a query?
  - id: getEntityInformationUsingEntityTypeIdOrEntityTypeNameUsingGET
    intent: Get an AI governance entity
    question: What attributes and module does a specific AI model record have?
  - id: deleteUsingEntityTypeIdOrEntityTypeNameUsingDELETE
    intent: Delete an AI governance entity
    question: How do I delete an AI model or dataset record?
  - id: updateUsingEntityTypeIdOrEntityTypeNameUsingPATCH
    intent: Modify an AI governance entity
    question: How do I rename an AI model record or change its attributes?
  - id: findEntityBasicDetailsByTypeAndCriteriaUsingPOST
    intent: Search AI entities with basic details
    question: Can I get a lightweight list of AI governance entities matching criteria?
  phrasing_ops: 6
  slug: onetrust-entity-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Entity Type Management APIs are used to manage AI Governance entity types.
  name: OneTrust Entity Type Management API
  phrasing_intents:
  - id: findAllByTypeAndCriteriaUsingPOST_1
    intent: Search AI governance entity types
    question: What entity types exist in AI Governance, like models and datasets?
  - id: getEntityTypeInformationUsingGET_1
    intent: Get an AI governance entity type
    question: Who created an AI governance entity type and when?
  phrasing_ops: 2
  slug: onetrust-entity-type-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage risk entity types and source entity types, including retrieval of enabled entity configurations for risk associations.
  name: OneTrust Entity Types API
  phrasing_intents:
  - id: getAllEnabledRiskEntityTypesUsingGET
    intent: List entity types risks can be created from
    question: From which entity types can I create a risk?
  - id: getAllEnabledSourceEntityTypesUsingGET
    intent: List entity types usable as risk source
    question: Which entity types can be automatically set as a risk's source?
  phrasing_ops: 2
  slug: onetrust-entity-types-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Entity Workflow Management APIs are used to manage AI Governance entity workflows.
  name: OneTrust Entity Workflow Management API
  phrasing_intents:
  - id: assignStageByName
    intent: Move an AI entity to a workflow stage
    question: How do I advance an AI model record to the next workflow stage?
  phrasing_ops: 1
  slug: onetrust-entity-workflow-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage evidence collection tasks including implementation retrieval, attachment handling (files, links, notes), and comprehensive search with interval-based collection tracking.
  name: OneTrust Evidence Task Implementations API
  phrasing_intents:
  - id: findAllEvidencesBySearchCriteria_1
    intent: List evidence task implementations
    question: Which evidence tasks are assigned and what is their current interval status?
  - id: findEvidenceImplementationsById_1
    intent: Get an evidence task implementation
    question: What are the details of a specific evidence task?
  - id: addEvidenceImplementationAttachment
    intent: Attach evidence to an evidence task
    question: Can I attach a file, note or link as evidence to a task?
  phrasing_ops: 3
  slug: onetrust-evidence-task-implementations-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Geolocation Rules APIs are used to manage geographic rules that determine how consent experiences are applied based on user location.
  name: OneTrust Geolocation Rules API
  phrasing_intents:
  - id: getGeoRuleGroups
    intent: List geolocation rule groups
    question: Which geolocation rule groups are configured for cookie consent?
  - id: getGeoRuleGroupDetails
    intent: Get a geolocation rule group's rules
    question: Which regions and consent models are in a geolocation rule group?
  - id: assignEntitiesToGeoRuleGroup
    intent: Assign domains or apps to a geo rule group
    question: Can I assign several domains to a geolocation rule group at once?
  phrasing_ops: 3
  slug: onetrust-geolocation-rules-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage business glossaries, including retrieving glossary details, listing all available glossaries, and accessing glossary-specific information with associated terms and metadata.
  name: OneTrust Glossaries API
  phrasing_intents:
  - id: getAllGlossariesNames
    intent: List business glossaries
    question: Which business glossaries are defined?
  - id: getAllGlossariesByNames
    intent: Get a business glossary by name
    question: Can I look up a glossary by its name?
  phrasing_ops: 2
  slug: onetrust-glossaries-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: V2 version APIs to manage Groups.
  name: OneTrust Groups V2 API
  phrasing_intents:
  - id: listGroupsUsingGET
    intent: List SCIM role-organization groups
    question: Why does the SCIM group list show one group per role and organization pair?
  - id: getGroupResourceUsingGET
    intent: Get a SCIM v2 group
    question: Which users sit in a specific SCIM v2 group?
  - id: updateGroupMembersUsingPUT
    intent: Replace a SCIM v2 group's members
    question: Can I overwrite the full membership of a SCIM v2 group?
  - id: updateGroupMembersUsingPATCH
    intent: Patch a SCIM v2 group's members
    question: Can I add or remove a single user from a SCIM v2 group without a full replace?
  phrasing_ops: 4
  slug: onetrust-groups-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create, update, search, and manage incidents, including linking incidents to inventories, retrieving details, and tracking their lifecycle.
  name: OneTrust Incidents API
  phrasing_intents:
  - id: assignStageByName
    intent: Move an incident to its next workflow stage
    question: How do I advance a privacy incident to the next stage of its workflow?
  - id: assignStageByName_1
    intent: Move an incident's stage within a workflow type
    question: How do I change an incident's stage in a specific workflow type rather than the default?
  - id: createIncidentUsingPOST
    intent: Log a new incident in the Incident Register
    question: How do I record a new data breach in the incident register?
  - id: searchIncidentsUsingPOST
    intent: Search incidents by keyword and filters
    question: Which incidents mention a particular system or keyword?
  - id: getIncidentDetailByIncidentIdUsingGET
    intent: Get an incident with its assessments and status
    question: What is the current status of a given incident and which assessments are linked to it?
  - id: updateIncidentUsingPUT
    intent: Update an incident's details
    question: How do I record the root cause on an incident after investigation?
  - id: createInventoryLinks
    intent: Link an incident to inventory records
    question: How do I record which assets were affected by an incident?
  phrasing_ops: 7
  slug: onetrust-incidents-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Initiatives APIs are used to manage compliance initiatives for standards and frameworks.
  name: OneTrust Initiatives API
  phrasing_intents:
  - id: findAllInitiativesByFilterUsingPOST
    intent: Search initiatives
    question: What initiatives are underway in my account?
  - id: getInitiativeUsingGET
    intent: Get an initiative's details
    question: Which workflow stage is a given initiative in?
  - id: updateInitiativeUsingPUT
    intent: Update an initiative
    question: How do I change the observation window of an initiative?
  phrasing_ops: 3
  slug: onetrust-initiatives-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to retrieve Docker image tags and installation resources for worker node deployment and version management across different environments.
  name: OneTrust Installer API
  phrasing_intents:
  - id: getDockerRepositoryTagsUsingGET
    intent: List Docker image tags for a worker node
    question: Which Docker images do I need for a data discovery worker node version?
  phrasing_ops: 1
  slug: onetrust-installer-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create and manage inventory records for supported schema types (processing-activities, vendors, assets, entities).
  name: OneTrust Inventory API
  phrasing_intents:
  - id: addAttachmentsToInventoryUsingPOST
    intent: Attach documents to an inventory record
    question: How do I link existing attachments to an inventory record?
  - id: getListOfInventoriesUsingGET
    intent: List inventories of a type
    question: What assets or processing activities are in my inventory?
  - id: createInventoryUsingPOST
    intent: Create an inventory record
    question: How do I add a new asset or processing activity to my inventory?
  - id: upsertInventoryUsingPUT
    intent: Upsert an inventory by external ID
    question: How do I sync an inventory record from another system, creating it if it doesn't exist?
  - id: getListOfInventoriesByFilterCriteriaUsingPOST
    intent: Search inventories by criteria
    question: How do I find inventory records matching several attribute filters?
  - id: getInventoryByExternalIdUsingGET
    intent: Get an inventory by external ID
    question: How do I look up an inventory record using the ID from my own system?
  - id: getInventoryByIdUsingGET
    intent: Get an inventory by ID
    question: What details are stored on one inventory record?
  - id: updateInventoryUsingPUT
    intent: Update an inventory by ID
    question: How do I change fields on an existing inventory record?
  phrasing_ops: 12
  slug: onetrust-inventory-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to list, link, and unlink child inventories under a root inventory to model organizational or data-flow trees.
  name: OneTrust Inventory Hierarchies API
  phrasing_intents:
  - id: setInventoryAsParentInventoryUsingPUT
    intent: Mark an inventory as a parent
    question: How do I turn an existing inventory record into a parent so others can nest under it?
  - id: unsetInventoryAsParentInventoryUsingPUT
    intent: Stop an inventory from being a parent
    question: How do I remove parent status from an inventory record?
  - id: linkAssetInventoryToParentAssetIdUsingPOST
    intent: Nest an asset under a parent asset
    question: How do I make one asset a child of another asset?
  - id: linkLegalEntityInventoryToParentLegalEntityIdUsingPOST
    intent: Nest a legal entity under a parent legal entity
    question: How do I model a subsidiary as a child of its parent legal entity?
  - id: linkProcessingActivityInventoryToParentProcessingActivityIdUsingPOST
    intent: Nest a processing activity under a parent activity
    question: How do I group processing activities under a parent activity?
  - id: linkVendorInventoryToParentVendorIdUsingPOST
    intent: Nest a vendor under a parent vendor
    question: How do I group a vendor's affiliates under a parent vendor record?
  - id: getHierarchyForInventoryIdUsingGET
    intent: List child inventories under a root inventory
    question: What child records sit under a given root inventory?
  - id: unlinkChildInventoryFromHierarchyUsingDELETE
    intent: Remove a child inventory from a hierarchy
    question: How do I take a child record out of an inventory hierarchy?
  phrasing_ops: 8
  slug: onetrust-inventory-hierarchies-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The inventory-management-controller API from OneTrust — 3 operation(s) for inventory-management-controller.
  name: OneTrust Inventory Management Controller API
  phrasing_intents:
  - id: getInventoryIdsFromBusinessKeysUsingPOST
    intent: Resolve business keys to inventory IDs
    question: How do I translate my own business keys into OneTrust inventory IDs?
  - id: getInventoryIdentifiersUsingPOST
    intent: List inventory identifiers with filters
    question: How do I get just the identifiers of inventory records matching a search?
  - id: searchVendorsByNameOrWebsiteUsingGET
    intent: Search vendors by name or website
    question: Is a vendor already in our inventory under this name?
  phrasing_ops: 3
  slug: onetrust-inventory-management-controller-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create, update, and delete bidirectional links between inventories and to manage associations to related items (including personal data).
  name: OneTrust Inventory Relationships V1 API
  phrasing_intents:
  - id: updateInventoryAssociationUsingPUT
    intent: Update an existing link between two inventories
    question: How do I change the relation type on a link between two inventory records?
  - id: listPersonalDataAssociationsUsingGET
    intent: List personal data linked to an inventory
    question: Which personal data items are linked to this asset or processing activity?
  - id: linkPersonalDataUsingPOST
    intent: Link personal data items to an inventory
    question: How do I record that an asset processes certain personal data?
  - id: removePersonalDataAssociationsUsingDELETE
    intent: Delete personal data links from an inventory
    question: How do I unlink personal data from an inventory record?
  - id: updateRelationsUsingPUT
    intent: Link inventories to each other (PUT variant)
    question: Is there a PUT call to link an inventory to other inventories?
  - id: createRelationsUsingPOST
    intent: Link inventories to each other (POST variant)
    question: How do I create a two-way link between a vendor and an asset inventory?
  - id: deleteRelationsUsingDELETE
    intent: Delete links between inventories
    question: How do I break the link between two inventory records?
  - id: getInventoryRelationsByIdUsingGET
    intent: List an inventory's links of a given type
    question: Which vendors are linked to a given processing activity?
  phrasing_ops: 12
  slug: onetrust-inventory-relationships-v1-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Inventory Relationships V2 APIs are used to manage V2 inventory relationships.
  name: OneTrust Inventory Relationships V2 API
  phrasing_intents:
  - id: listAllInventoryRelationshipsUsingPOST
    intent: List an inventory's relationships
    question: What other inventories is a given asset or processing activity linked to?
  - id: updateInventoryRelationsUsingEntityTypeName_1
    intent: Update a relationship by entity type name
    question: Can I edit a contextual link's attributes when I only know the entity type's name?
  - id: linkOrUnlinkInventoryRelationshipsUsingRelationshipUsingPUT_1
    intent: Link personal data to a relationship by type name
    question: Can I attach or detach personal data elements on a relationship identified by entity type name?
  - id: getPersonalDataForRelationshipsUsingPOST_1
    intent: List a relationship's personal data by type name
    question: Which personal data elements are tied to a relationship, looked up by entity type name?
  - id: updateInventoryRelationsUsingEntityTypeName
    intent: Update a relationship by entity type ID
    question: Can I edit a contextual link's attributes using the entity type's ID?
  - id: linkOrUnlinkInventoryRelationshipsUsingRelationshipUsingPUT
    intent: Link personal data to a relationship by type ID
    question: I only have the numeric entity type ID — where do I add or drop data elements on that contextual link?
  - id: getPersonalDataForRelationshipsUsingPOST
    intent: List a relationship's personal data by type ID
    question: Given a contextual link and its entity type ID, what data elements does it carry?
  - id: createInventoryRelationsUsingPOST
    intent: Link inventories together
    question: Can I create a two-way link between an asset and several other inventories?
  phrasing_ops: 12
  slug: onetrust-inventory-relationships-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to define and maintain schema attributes that shape inventory data collection and validation.
  name: OneTrust Inventory Schema API
  phrasing_intents:
  - id: getAllSchemasUsingGET
    intent: List inventory schemas
    question: Which inventory schemas are defined in my tenant?
  - id: createAttributeValuesForAnAttribute
    intent: Add options to a select attribute
    question: Can I bulk-add dropdown options to a single or multi select inventory attribute?
  - id: manageAttributeOptions
    intent: Edit or deactivate an attribute option
    question: Can I rename an existing option on an inventory attribute?
  - id: getSchemaBySchemaTypeUsingGET
    intent: Get an inventory schema with hidden fields
    question: Can I fetch a schema by name including hidden attributes?
  - id: createAttributeForTheInventorySchema
    intent: Create an inventory attribute
    question: Can I add a custom attribute to the assets or vendors schema?
  - id: activateAttributesByFieldNames
    intent: Activate inventory attributes
    question: Can I re-enable attributes on a schema by their field names?
  - id: deactivateAttributesByFieldNames
    intent: Deactivate inventory attributes
    question: Can I switch off attributes on a schema by their field names?
  - id: getSchemaDetailsUsingFieldName
    intent: Get one attribute's schema details
    question: What are the settings and options of a single attribute in a schema?
  phrasing_ops: 9
  slug: onetrust-inventory-schema-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Issues APIs are used to manage issues, issue tasks, and issue relationships.
  name: OneTrust Issues API
  phrasing_intents:
  - id: getAttributesBySchemaNameUsingGET
    intent: Get an issue attribute schema
    question: What custom attributes can I set on issues?
  - id: createIssueRelationshipLinksUsingPOST
    intent: Link an issue to a related record
    question: How do I connect an issue to an asset, vendor or other record?
  - id: getIssueLinksUsingGET
    intent: List an issue's related records
    question: Which records is an issue linked to?
  - id: createIssueUsingPOST
    intent: Create an issue
    question: How do I log a new risk or compliance issue in OneTrust?
  - id: findAllIssuesByFilterUsingPOST
    intent: Search issues
    question: What open issues do we have right now?
  - id: getIssueUsingGET
    intent: Get an issue
    question: What are the full details of a specific issue?
  - id: updateIssueUsingPUT
    intent: Replace all details of an issue
    question: How do I overwrite every field of an issue in one request?
  - id: updateIssueUsingPATCH
    intent: Partially update an issue
    question: Can I change just one or two fields on an issue without resending everything?
  phrasing_ops: 9
  slug: onetrust-issues-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Jobs APIs are used to manage scheduled jobs for bulk actions.
  name: OneTrust Jobs API
  phrasing_intents:
  - id: createJobUsingPOST
    intent: Schedule a data subject bulk job
    question: Can I schedule a bulk action job across data subjects?
  phrasing_ops: 1
  slug: onetrust-jobs-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to record and retrieve user consent transactions and preferences.
  name: OneTrust Log Consent API
  phrasing_intents:
  - id: post_LogConsent
    intent: Log a user's banner or preference center consent
    question: How do I record the consent a user gave in my app's banner?
  phrasing_ops: 1
  slug: onetrust-log-consent-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Magic Link Tokens APIs are used to generate secure, one-time-use links for authentication.
  name: OneTrust Magic Link Tokens API
  phrasing_intents:
  - id: getLinkTokensUsingGET
    intent: List magic link tokens
    question: Which magic link tokens were issued to data subjects, and when do they expire?
  phrasing_ops: 1
  slug: onetrust-magic-link-tokens-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Magic Link Tokens V4 APIs are used to manage secure, time-limited tokens for data subject verification and authentication.
  name: OneTrust Magic Link Tokens V4 API
  phrasing_intents:
  - id: getEmailLinkTokenByDataSubjectV4
    intent: Get a data subject's magic link token
    question: How do I get the magic link token for one person's preference email?
  - id: getEmailLinkTokensListV4
    intent: List magic link tokens in a date range
    question: Which magic link tokens were issued last week?
  phrasing_ops: 2
  slug: onetrust-magic-link-tokens-v4-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage Metric related Information.
  name: OneTrust Metric Details API
  phrasing_intents:
  - id: fetchMetricsDetails
    intent: Get ESG metric details for a period
    question: What are the latest ESG metric values for a reporting period?
  phrasing_ops: 1
  slug: onetrust-metric-details-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Mobile App Data API from OneTrust — 1 operation(s) for mobile app data.
  name: OneTrust Mobile App Data API
  phrasing_intents:
  - id: applicationdata
    intent: Get SDK configuration for a mobile app
    question: What consent templates and vendor lists does my mobile or OTT app receive?
  phrasing_ops: 1
  slug: onetrust-mobile-app-data-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Model Management APIs are used to conduct full management of Model objects.
  name: OneTrust Model Management API
  phrasing_intents:
  - id: createModelUsingPOST
    intent: Create an AI model record
    question: How do I register a new AI model in Object Manager?
  - id: findModelBasicDetailsByQueryCriteriaUsingPOST
    intent: Search models for basic details
    question: Can I get just the basic details of models matching some criteria?
  - id: findModelsByListCriteriaUsingPOST
    intent: Search models with full details
    question: Can I search model records and get every attribute back?
  - id: getModelUsingGET
    intent: Get an AI model record
    question: What attributes are stored on a specific model record?
  - id: updateModelUsingPUT
    intent: Modify an AI model record
    question: Can I rename a model record or change its organization?
  - id: deleteModelUsingDELETE
    intent: Delete an AI model record
    question: Can I remove a model record from Object Manager?
  phrasing_ops: 6
  slug: onetrust-model-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage OAuth 2.0 authentication for secure API access. Generate access tokens using client credentials, retrieve token information, and manage API authentication for your applications.
  name: OneTrust OAuth Token API
  phrasing_intents:
  - id: GetOAuthToken
    intent: Generate an OAuth access token
    question: How do I get an access token to call the OneTrust APIs?
  phrasing_ops: 1
  slug: onetrust-oauth-token-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Object Attribute Management APIs are used to manage object attributes.
  name: OneTrust Object Attribute Management API
  phrasing_intents:
  - id: addOptionsUsingPOST
    intent: Add options to a picklist attribute
    question: How do I add new choices to a dropdown attribute on Projects or Models?
  - id: addAttributeUsingPOST
    intent: Add a new attribute to an object schema
    question: How do I add a custom field to the Project, Model or Dataset schema?
  - id: disableAttributeUsingPUT
    intent: Disable a schema attribute
    question: How do I hide an attribute from an object schema without deleting it?
  - id: enableAttributeUsingPUT
    intent: Re-enable a schema attribute
    question: How do I bring back an attribute I previously disabled?
  phrasing_ops: 4
  slug: onetrust-object-attribute-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Object Management APIs are used to manage objects created via Object Manager, including Projects, Models, and Datasets.
  name: OneTrust Object Management API
  phrasing_intents:
  - id: addEntityUsingEntityTypeIdOrEntityTypeNameUsingPOST
    intent: Create an object record
    question: Can I create a Project, Model or Dataset record in Object Manager?
  - id: findAllByTypeIdAndCriteriaUsingPOST
    intent: Search objects with full details
    question: Can I search object records and get every attribute back?
  - id: getEntityInformationUsingEntityTypeIdOrEntityTypeNameUsingGET
    intent: Get an object record
    question: Can I fetch one object record by its ID with its attributes?
  - id: deleteUsingEntityTypeIdOrEntityTypeNameUsingDELETE
    intent: Delete an object record
    question: Can I delete a Project, Model or Dataset record?
  - id: updateUsingEntityTypeIdOrEntityTypeNameUsingPATCH
    intent: Partially update an object record
    question: Can I change just a few attributes on an object record?
  - id: findEntityBasicDetailsByTypeAndCriteriaUsingPOST
    intent: Search objects for basic details
    question: Is there a lighter search that returns only basic details for objects?
  phrasing_ops: 6
  slug: onetrust-object-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Object Relationship Management APIs are used to manage relationships between objects.
  name: OneTrust Object Relationship Management API
  phrasing_intents:
  - id: createLinkRecordBetweenEntitiesUsingLinkTypeIdUsingPOST
    intent: Link two Object Manager records
    question: Can I relate a project to a model or dataset?
  - id: getLinkRecordInformationUsingLinkTypeIdUsingGET
    intent: Get a relationship record
    question: What are the details of a link between two objects?
  - id: deleteLinkRecordByIdAndTypeUsingLinkTypeIdUsingDELETE
    intent: Remove a relationship record
    question: Can I unlink a model from a project?
  phrasing_ops: 3
  slug: onetrust-object-relationship-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Object Relationship Type Management APIs are used to manage the types of relationships that can exist between objects.
  name: OneTrust Object Relationship Type Management API
  phrasing_intents:
  - id: createCustomLinkTypeUsingPOST
    intent: Create a relationship type between objects
    question: Can I define a new kind of relationship between Projects and Models?
  - id: findAllByLinkTypeAndCriteriaUsingPOST
    intent: Search relationship types
    question: Which relationship types are defined between my objects?
  - id: getLinkTypeUsingGET
    intent: Get a relationship type
    question: Can I see the details of one relationship type by ID?
  phrasing_ops: 3
  slug: onetrust-object-relationship-type-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Object Task Management APIs are used to manage tasks associated with objects.
  name: OneTrust Object Task Management API
  phrasing_intents:
  - id: createTaskUsingPOST_1
    intent: Create a task on a Project, Model or Dataset
    question: How do I assign a follow-up task on an AI model record?
  - id: findTaskUsingGET_1
    intent: Get an object task and its history
    question: Who is assigned to a task on a Project and when is it due?
  - id: updateTaskUsingPUT_1
    intent: Update an object task
    question: How do I mark an object task complete or change its status?
  phrasing_ops: 3
  slug: onetrust-object-task-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Object Type Management APIs are used to manage custom object types.
  name: OneTrust Object Type Management API
  phrasing_intents:
  - id: getEntityTypeInformationUsingGET_1
    intent: Get an object type by name
    question: Who created an object type like Models, and when, looked up by its name?
  - id: updateCustomEntityTypeUsingPATCH_1
    intent: Modify a custom object type by name
    question: How do I change the description of a custom object type when I only know its name?
  - id: enabledCustomEntityTypeUsingPUT_1
    intent: Enable a custom object type by name
    question: How do I turn on a custom object type using its name?
  - id: findAllByTypeAndCriteriaUsingPOST
    intent: Search object types
    question: What object types exist in Object Manager?
  - id: getEntityTypeInformationUsingGET
    intent: Get an object type by ID
    question: How do I look up an object type using its unique ID?
  - id: updateCustomEntityTypeUsingPATCH
    intent: Modify a custom object type by ID
    question: How do I update a custom object type's settings using its ID?
  - id: enabledCustomEntityTypeUsingPUT
    intent: Enable a custom object type by ID
    question: How do I enable a custom object type using its ID?
  phrasing_ops: 7
  slug: onetrust-object-type-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage your organizational hierarchy and structure. Create, update, and delete organizations, define parent-child relationships, and configure organization-specific settings such as default la
  name: OneTrust Organizations API
  phrasing_intents:
  - id: organizationTreeStructureUsingGET
    intent: List organizations in the hierarchy
    question: What organizations make up our OneTrust org hierarchy?
  - id: createOrganizationUsingPOST
    intent: Create an organization
    question: How do I add a new business unit to the org hierarchy?
  - id: updateOrganizationUsingPUT
    intent: Update an organization
    question: How do I rename an organization or change its default approver?
  - id: deleteOrganizationPOST
    intent: Delete an organization
    question: How do I delete an organization and keep its records?
  phrasing_ops: 4
  slug: onetrust-organizations-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to list links to personal-data items for an inventory and update advanced attributes on those associations.
  name: OneTrust Personal Data API
  phrasing_intents:
  - id: getDataCategoriesByPartialNameUsingGET
    intent: List data categories
    question: What data categories are defined in my OneTrust data mapping inventory?
  - id: createDataCategoryUsingPOST
    intent: Create a data category
    question: How do I add a new data category to data mapping automation?
  - id: getDataCategoryUsingGET
    intent: Get a data category
    question: What are the details of a specific data category by its ID?
  - id: deleteDataCategoryUsingDELETE
    intent: Delete a data category
    question: How do I remove a data category from my data inventory?
  - id: listAllDataClassificationsUsingGET
    intent: List all data classifications
    question: What data classifications exist in my data mapping setup?
  - id: createDataClassificationUsingPOST
    intent: Create a data classification
    question: How do I add a new data classification like Confidential or Restricted?
  - id: getDataClassificationUsingGET
    intent: Get a data classification
    question: How can I look up a single data classification by ID?
  - id: deleteDataClassificationUsingDELETE
    intent: Delete a data classification
    question: How do I remove a data classification I no longer use?
  phrasing_ops: 18
  slug: onetrust-personal-data-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage preference center configuration and user consent choices.
  name: OneTrust Preference Center API
  phrasing_intents:
  - id: get_Preferences
    intent: Load preference center data for an app
    question: What does my mobile app need to render the preference center?
  phrasing_ops: 1
  slug: onetrust-preference-center-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Preference Centers APIs are used to manage data subjects' preferences in a preference center.
  name: OneTrust Preference Centers API
  phrasing_intents:
  - id: getDataSubjectPurposesByIdentifierUsingGET_1
    intent: Get a data subject's preferences in a center
    question: What has a customer chosen in a particular preference center?
  - id: updatePreferencesForDataSubjectApiUsingPUT
    intent: Update a data subject's preferences in a center
    question: Can I change a customer's purpose choices in a preference center?
  - id: withdrawPreferencesApiUsingDELETE
    intent: Withdraw all consent in a preference center
    question: Can I withdraw someone's consent for every purpose in a preference center at once?
  - id: getPreferenceCenterByIdUsingGET
    intent: Get a preference center's schema
    question: What purposes, languages and settings does a preference center have?
  phrasing_ops: 4
  slug: onetrust-preference-centers-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Preference Centers V2 APIs are used to manage preference centers using version 2 of the API.
  name: OneTrust Preference Centers V2 API
  phrasing_intents:
  - id: getPreferenceCenterPageSchemaUsingGET
    intent: Get a preference center page schema
    question: What sections, purposes and data elements appear on one page of a multi-page preference center?
  - id: getPreferenceCentersUsingGET
    intent: List preference centers
    question: What preference centers have we built, and when were they published?
  - id: getRootSchemaUsingGET
    intent: Get a preference center root schema
    question: What settings, languages and pages does a multi-page preference center have?
  phrasing_ops: 3
  slug: onetrust-preference-centers-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Preferences API from OneTrust — 1 operation(s) for preferences.
  name: OneTrust Preferences API
  phrasing_intents:
  - id: getPreferencesUsingGET
    intent: Get a data subject's cross-device preferences
    question: What cross-device consent preferences has a user saved?
  phrasing_ops: 1
  slug: onetrust-preferences-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Consent Interfaces APIs are used by Consent & Preferences user interfaces to retrieve data subjects' preferences.
  name: OneTrust Preferences V2 API
  phrasing_intents:
  - id: getRealtimePreferences
    intent: Get a data subject's real-time preferences
    question: What has a given person consented to right now?
  phrasing_ops: 1
  slug: onetrust-preferences-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to list privacy notices, fetch versions for a notice, and get the notice version active on a given date/time.
  name: OneTrust Privacy Notice V2 API
  phrasing_intents:
  - id: getPrivacyNoticesUsingGET
    intent: List privacy notices
    question: Which privacy notices do we have and when were they last published?
  - id: getPrivacyNoticeVersionByPublishedDateUsingGET
    intent: Get a privacy notice as published on a date
    question: Which version of our privacy notice was live on a specific date?
  - id: getPrivacyNoticeVersionsUsingGET
    intent: List a privacy notice's versions
    question: How many versions has a privacy notice gone through?
  phrasing_ops: 3
  slug: onetrust-privacy-notice-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Project Management APIs are used to conduct full management of Project objects.
  name: OneTrust Project Management API
  phrasing_intents:
  - id: createProjectUsingPOST
    intent: Create a Project object record
    question: How do I register a new AI or data project in Object Manager?
  - id: findProjectBasicDetailsByQueryCriteriaUsingPOST
    intent: Search Projects for basic details only
    question: Can I get a lightweight list of Projects with just their basic details?
  - id: findProjectsByListCriteriaUsingPOST
    intent: Search Projects with full details
    question: How do I search Projects and get every attribute back?
  - id: getProjectUsingGET
    intent: Get one Project object
    question: What attributes are recorded on a particular Project?
  - id: updateProjectUsingPUT
    intent: Partially update a Project
    question: How do I rename a Project or change some of its attributes?
  - id: deleteProjectUsingDELETE
    intent: Delete a Project
    question: How do I delete a Project record I no longer need?
  phrasing_ops: 6
  slug: onetrust-project-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Purpose Preferences APIs are used to manage preferences related to specific data collection purposes.
  name: OneTrust Purpose Preferences API
  phrasing_intents:
  - id: getListUsingGET
    intent: List purpose preferences
    question: Which Purpose Preferences are set up, and how many options does each have?
  - id: createCustomPreferenceUsingPOST
    intent: Create a purpose preference
    question: Can I create a Purpose Preference with its own options, like topics or frequency?
  - id: editCustomPreferenceUsingPUT
    intent: Update a purpose preference
    question: Can I rename a Purpose Preference or change its options?
  - id: findByGuidUsingGET
    intent: Get a purpose preference
    question: What languages and options does one Purpose Preference have?
  phrasing_ops: 4
  slug: onetrust-purpose-preferences-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Purposes APIs are used to manage the reasons for which data is collected.
  name: OneTrust Purposes API
  phrasing_intents:
  - id: getPurposesUsingGET
    intent: List consent purposes (deprecated)
    question: Is there an older call that lists all consent purposes without grouping by version?
  - id: createPurposeUsingPOST
    intent: Create a consent purpose
    question: How do I create a new purpose for collecting consent?
  - id: createNewPurposeVersionUsingPOST
    intent: Create a new version of an active purpose
    question: Can I draft changes to a purpose that's already active without touching the live version?
  - id: editPurposeUsingPUT
    intent: Update a draft purpose
    question: Can I edit a purpose that is still in draft?
  - id: getDataSubjectsForPurposesUsingGET
    intent: List data subjects for a purpose
    question: Who has consented to a given purpose?
  - id: publishPurposeUsingPUT
    intent: Publish a draft purpose
    question: How do I make a draft purpose active?
  - id: setRetirementUsingPUT
    intent: Retire a purpose
    question: Can I schedule a purpose to be retired on a certain date?
  phrasing_ops: 7
  slug: onetrust-purposes-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Purposes V2 APIs are used to manage purposes using version 2 of the API.
  name: OneTrust Purposes V2 API
  phrasing_intents:
  - id: getGroupedPurposesV2
    intent: List purpose versions
    question: What consent purposes do we have, and which versions are published?
  - id: getPurposeDetailUsingGET
    intent: Get a purpose
    question: What preferences and attributes does a specific consent purpose have?
  phrasing_ops: 2
  slug: onetrust-purposes-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Receipts APIs are used to manage records of consent transactions.
  name: OneTrust Receipts API
  phrasing_intents:
  - id: getReceiptListUsingGET
    intent: List a data subject's receipts (deprecated)
    question: Is the old receipt list endpoint still supported?
  - id: getReceiptListDetailsUsingGET
    intent: List receipt details for a data subject
    question: Can I get the full details of every consent receipt for one person?
  - id: findReceiptUsingGET
    intent: Get a consent receipt
    question: Can I pull up a single consent receipt by its ID?
  phrasing_ops: 3
  slug: onetrust-receipts-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs for managing consent receipts (V2).
  name: OneTrust Receipts V2 API
  phrasing_intents:
  - id: getReceiptListDetailsUsingPOST
    intent: List consent receipts
    question: What consent receipts were recorded for a particular person?
  phrasing_ops: 1
  slug: onetrust-receipts-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Relationship Management APIs are used to manage relationships between AI Governance entities.
  name: OneTrust Relationship Management API
  phrasing_intents:
  - id: getRelatedEntitiesForAnEntityUsingPOST
    intent: List relationships of an AI entity
    question: Which datasets or AI systems are linked to a given model?
  - id: createLinkRecordBetweenEntitiesUsingLinkTypeIdUsingPOST
    intent: Link two AI Governance entities
    question: Can I link a model to a dataset in AI Governance?
  - id: getLinkRecordInformationUsingLinkTypeIdUsingGET
    intent: Get an AI Governance relationship
    question: Can I read the details of one relationship record between AI entities?
  - id: deleteLinkRecordByIdAndTypeUsingLinkTypeIdUsingDELETE
    intent: Remove an AI Governance relationship
    question: Can I unlink a model from a dataset?
  - id: addRelationshipBetweenEntitiesUsingPOST
    intent: Relate two inventory records
    question: Can I link an asset to a vendor or processing activity in my inventory?
  phrasing_ops: 5
  slug: onetrust-relationship-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create, search, update, and manage privacy request queues.
  name: OneTrust Request Queues API
  phrasing_intents:
  - id: createRequestQueueFromMessageUsingPOST
    intent: Create a data subject request (deprecated)
    question: Is there an older endpoint that creates a DSR without putting the web form template in the path?
  - id: bulkDeleteUsingPUT
    intent: Bulk delete data subject requests
    question: Can I permanently delete many privacy requests at once by status or date range?
  - id: getDeletionCertificateUsingGET
    intent: Get the deletion certificate for a request
    question: Where can I get proof that a deleted data subject request was actually removed?
  - id: getRequestHistoryByIdUsingGET
    intent: Get a request's audit history by internal ID
    question: Can I pull a DSR's change history using its numeric request queue ID instead of the reference ID?
  - id: searchForRequestUsingPOST
    intent: Search data subject requests by keyword
    question: Can I find a privacy request by the data subject's email address or last name?
  - id: getRequestCreationLogsUsingGET
    intent: Check creation status of an async request
    question: Did my asynchronously submitted request actually get created?
  - id: getAllRequestQueuesV2UsingGET
    intent: List data subject requests
    question: Which privacy requests are currently open in OneTrust?
  - id: addCommentsUsingPUT
    intent: Add a comment to a request
    question: Can I leave an internal-only note on a data subject request?
  phrasing_ops: 15
  slug: onetrust-request-queues-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create, update, delete, and retrieve resolution codes for privacy requests and subtasks.
  name: OneTrust Resolutions API
  phrasing_intents:
  - id: getAllV2ResolutionsUsingGET
    intent: List privacy request resolutions
    question: What resolution options can a privacy request be closed with?
  - id: addNewResolutionUsingPOST
    intent: Create a request resolution
    question: How do I add a new way to resolve data subject requests?
  - id: updateResolutionUsingPUT
    intent: Update a request resolution
    question: How do I change what an existing resolution does to a request?
  - id: deleteResolutionUsingDELETE
    intent: Delete a request resolution
    question: How do I remove a resolution option we no longer use?
  phrasing_ops: 4
  slug: onetrust-resolutions-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: V3 version APIs to manager Resources Type.
  name: OneTrust Resources V3 API
  phrasing_intents:
  - id: getResourceTypesUsingGET
    intent: List supported SCIM resources
    question: Which SCIM resources can my identity provider provision?
  - id: getResourceTypesByNameUsingGET
    intent: Get a SCIM resource type's details
    question: What schema and endpoint does the SCIM User resource use?
  phrasing_ops: 2
  slug: onetrust-resources-v3-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to share results summaries.
  name: OneTrust Results Summary API
  phrasing_intents:
  - id: shareResultsSummaryUsingPOST
    intent: Email a data discovery results summary
    question: How do I send a data subject the summary of what personal data we found?
  phrasing_ops: 1
  slug: onetrust-results-summary-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage risk workflow actions including submissions, approvals, exceptions, and stage transitions within the risk lifecycle.
  name: OneTrust Risk Actions API
  phrasing_intents:
  - id: performRiskActionUsingPUT
    intent: Perform a risk action (deprecated)
    question: Is the generic perform-risk-action endpoint still supported?
  - id: approveRiskUsingPUT
    intent: Approve a risk
    question: Can I approve a risk and set its residual risk level and score?
  - id: grantRiskExceptionUsingPUT
    intent: Grant an exception for a risk
    question: Can I grant an exception on a risk instead of remediating it?
  - id: reopenRiskUsingPUT
    intent: Reopen a risk
    question: Can a closed risk be reopened?
  - id: requestRiskExceptionUsingPUT
    intent: Request an exception for a risk
    question: Can I ask for an exception on a risk rather than grant one?
  - id: sendBackRiskUsingPUT
    intent: Send a risk back for more information
    question: Can I return a risk to its owner to gather more detail?
  - id: submitRiskUsingPUT
    intent: Submit a risk for approval
    question: Can I submit a risk so it goes to the approver?
  phrasing_ops: 7
  slug: onetrust-risk-actions-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage risk configurations, scoring settings, categories, and metadata used across the risk management system.
  name: OneTrust Risk Management API
  phrasing_intents:
  - id: createUpdateRiskUsingPUT
    intent: Create or update a risk by matching attributes
    question: Can I upsert a risk so it's created only if no matching risk exists?
  - id: changeRiskStageUsingPOST
    intent: Move a risk to a workflow stage
    question: How do I advance a risk to the next stage in its workflow?
  - id: updateRiskUsingPUT
    intent: Replace a risk's details
    question: Can I fully update a risk's name, description, owners and treatment in one call?
  - id: deleteRiskUsingDELETE
    intent: Delete a risk
    question: Can I remove a risk from the risk register?
  - id: updateRiskUsingPATCH
    intent: Partially modify a risk
    question: Can I change just a risk's deadline without resending everything?
  - id: updateRiskApproversUsingPUT
    intent: Update a risk's approvers
    question: Who can approve a risk, and can I change them?
  - id: updateRiskCategoriesUsingPUT
    intent: Update a risk's categories
    question: Can I recategorize an existing risk?
  - id: updateRiskOwnersUsingPUT
    intent: Update a risk's owners
    question: Can I reassign who owns a risk?
  phrasing_ops: 8
  slug: onetrust-risk-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage relationships between risks and other entities including threats, vulnerabilities, controls, and inventory items.
  name: OneTrust Risk Relationships API
  phrasing_intents:
  - id: addControlsToRiskUsingPOST
    intent: Add control implementations to a risk
    question: How do I attach mitigating controls to a risk?
  - id: addThreatToRisk
    intent: Set the threat on a risk
    question: How do I record which threat a risk comes from?
  - id: addVulnerabilitiesToRisk
    intent: Set the vulnerabilities on a risk
    question: How do I tie library vulnerabilities to a risk?
  phrasing_ops: 3
  slug: onetrust-risk-relationships-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage risk template retrieval operations, enabling users to access detailed risk template information including inherent and target risk levels, associated threats and vulnerabilities, contro
  name: OneTrust Risk Templates API
  phrasing_intents:
  - id: getRiskTemplateUsingGET
    intent: Get a risk template
    question: What does a specific risk template contain?
  phrasing_ops: 1
  slug: onetrust-risk-templates-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage the complete risk lifecycle including creation, updates, deletion, search, and retrieval of risk details and attributes.
  name: OneTrust Risks API
  phrasing_intents:
  - id: unlinkRisksFromEntityUsingPost
    intent: Unlink risks from an entity
    question: How do I detach risks from an asset or vendor without deleting them?
  - id: getActiveCategoriesUsingGET
    intent: List risk categories
    question: What risk categories are configured in my risk register?
  - id: getMatrixScoreSettingUsingGET
    intent: Get the risk matrix scoring configuration
    question: How are impact and probability combined into a score in my risk matrix?
  - id: getStandardScoreSettingUsingGET
    intent: Get the standard risk level configuration
    question: What score ranges define low, medium and high risk under the standard configuration?
  - id: createRiskUsingPOST
    intent: Create a risk tied to an inventory (v2)
    question: How do I log a new risk against an asset in the risk register?
  - id: getRiskPageViewUsingPOST
    intent: Search and list risks in the register
    question: Which risks in my register match a keyword?
  - id: getLinkedRisksInformationUsingPOST
    intent: List risks linked to a specific entity
    question: What risks are attached to a particular vendor or asset?
  - id: getRiskUsingGET
    intent: Get a single risk's details
    question: Who owns and approves a particular risk, and what is its status?
  phrasing_ops: 9
  slug: onetrust-risks-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to control scan job execution including creation, cancellation, status monitoring, and comprehensive job history retrieval with filtering and pagination support.
  name: OneTrust Scan Jobs API
  phrasing_intents:
  - id: createJobUsingPOST
    intent: Start a data discovery scan job
    question: How do I kick off a new discovery scan on a data source?
  - id: getScanJobsByDataSourceUsingGET_1
    intent: List scan jobs for a data source
    question: What scan jobs have run against a given data source?
  - id: getJobByIdUsingGET
    intent: Get a scan job's status and progress
    question: How far along is my scan job and has ingestion finished?
  - id: cancelJobUsingPATCH
    intent: Cancel a scan job by job ID
    question: How do I stop a pending or processing scan job using only its job ID?
  - id: getJobUsingGET_1
    intent: Get a scan job on a specific scanner
    question: How do I fetch a scan job through the scanner that ran it?
  - id: cancelScanJob
    intent: Cancel a scan job on a specific scanner
    question: How do I cancel a job running on a particular scanner?
  phrasing_ops: 6
  slug: onetrust-scan-jobs-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to handle scan profile lifecycle management including creation, updates, deletion, and retrieval with support for catalog and catalog-scan types across various system platforms.
  name: OneTrust Scan Profiles API
  phrasing_intents:
  - id: getAllUsingGET_2
    intent: List data discovery scan profiles
    question: What scan profiles are configured for data discovery?
  - id: updateV2UsingPUT
    intent: Update a scan profile
    question: How do I change the paths or settings of an existing scan profile?
  - id: createV2UsingPOST
    intent: Create a scan profile
    question: How do I define what a data discovery scan should look at on a system?
  - id: getScanProfileUsingGET_1
    intent: Get one scan profile
    question: Which paths and system does a particular scan profile cover?
  - id: deleteScanProfileUsingDELETE_1
    intent: Delete a scan profile
    question: How do I remove a scan profile that is no longer needed?
  phrasing_ops: 5
  slug: onetrust-scan-profiles-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Scans APIs are used to manage website cookie scanning operations and results.
  name: OneTrust Scans API
  phrasing_intents:
  - id: getDomainsScannedBySort
    intent: List websites in the cookie scanner
    question: Which websites are set up in the cookie scanner?
  - id: addScans
    intent: Start cookie scans for domains
    question: How do I kick off a cookie scan of my website?
  - id: archiveScans
    intent: Archive website scans
    question: Can I archive old cookie scans I no longer need?
  - id: getDomainScans
    intent: List scans for a domain
    question: What scans have run on a particular domain?
  - id: getScanDeltaDetails
    intent: List cookies added or removed since last scan
    question: Which cookies appeared or disappeared on my site since the previous scan?
  - id: getDetailedScanResultInformation
    intent: Get detailed scan results
    question: What cookies, tags and forms did a scan find on my website?
  - id: getScanResultSummary
    intent: Get a scan's summary counts
    question: How many cookies and tags did a scan find in total?
  - id: checkScansStatus
    intent: Check status of scans
    question: Are my website scans still running or finished?
  phrasing_ops: 9
  slug: onetrust-scans-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: V3 version APIs to manager Schemas.
  name: OneTrust SCIM Schemas V3 API
  phrasing_intents:
  - id: getSchemasUsingGET
    intent: List supported SCIM schemas
    question: Which SCIM schemas are supported for users and groups?
  - id: getSchemasByNameUsingGET
    intent: Get a SCIM schema
    question: What attributes does a specific SCIM schema define?
  phrasing_ops: 2
  slug: onetrust-scim-schemas-v3-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Scripts APIs are used to manage publishing of scripts to websites.
  name: OneTrust Scripts API
  phrasing_intents:
  - id: publishAppScript
    intent: Publish an app's SDK configuration
    question: Can I publish the consent SDK configuration for a mobile application?
  - id: getAppScriptDetails
    intent: Get an application's script details
    question: Where can I see the script details configured for a mobile app?
  - id: publishScriptToSite
    intent: Publish cookie script to a website (CMP v1)
    question: Can I publish my cookie consent script to a website through the CMP v1 endpoint?
  - id: getScriptForWebsite
    intent: Get a website's script (CMP v1)
    question: Can I fetch a website's consent script from the CMP v1 path?
  - id: getScriptDetails
    intent: Get script details for a domain ID
    question: Can I get script details using a domain's ID rather than its URL?
  - id: downloadScriptFile
    intent: Download a domain's script files (CMP)
    question: Can I download the published cookie script files to self-host them?
  - id: downloadToLocalUsingGet
    intent: Download a domain's script files (integration)
    question: Is there a script-integration endpoint for downloading script files locally?
  - id: getScriptForWebsiteUsingGET
    intent: Get a website's script (v2)
    question: Can I fetch a site's cookie script from the v2 websites endpoint?
  phrasing_ops: 9
  slug: onetrust-scripts-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: V3 version APIs to manager the Service Provider.
  name: OneTrust Service Provider V3 API
  phrasing_intents:
  - id: getServiceProviderConfigUsingGET
    intent: Get SCIM service provider configuration
    question: Which SCIM features are supported, like patch, filtering or bulk?
  phrasing_ops: 1
  slug: onetrust-service-provider-v3-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create, update, complete, and reprocess subtasks associated with privacy requests.
  name: OneTrust Subtasks API
  phrasing_intents:
  - id: getAllSubTaskByRefIdUsingGET
    intent: List subtasks on a request
    question: Which subtasks are attached to a specific privacy request?
  - id: createSubTaskUsingPOST
    intent: Add a subtask to a request
    question: Can I add a custom subtask to a data subject request and assign it by email?
  - id: createSubTaskFromTemplateUsingPOST
    intent: Add a subtask from a template
    question: Can I add a subtask to a request using a saved subtask template?
  - id: subtasksUsingGET
    intent: List subtasks (deprecated endpoint)
    question: Is the old list-subtasks endpoint still supported after January 2026?
  - id: getSubtaskByIDUsingGET
    intent: Get a subtask
    question: Who is assigned to a subtask and when is it due?
  - id: updateSubTaskUsingPUT
    intent: Edit a subtask's details
    question: Can I change a subtask's assignee, deadline or description?
  - id: addDataDiscoveryUsingPUT
    intent: Attach Targeted Data Discovery to a subtask
    question: Can I add Targeted Data Discovery details to a subtask?
  - id: completeSubTaskUsingPUT
    intent: Complete a subtask
    question: Can I resolve a subtask and mark it complete with a comment?
  phrasing_ops: 11
  slug: onetrust-subtasks-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create and update system credentials required for integrations, such as authentication keys and connection details.
  name: OneTrust System Credentials API
  phrasing_intents:
  - id: updateV2UsingPUT
    intent: Update a connector system credential
    question: How do I rotate the secret on an existing integration credential?
  - id: createV2UsingPOST
    intent: Create a system credential for a connector
    question: How do I store credentials for a new integration connector?
  phrasing_ops: 2
  slug: onetrust-system-credentials-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage tags for data classification, including creating new tags with various types and retrieving tag details with their associated terms.
  name: OneTrust Tags API
  phrasing_intents:
  - id: retrieveAllTagsName
    intent: List glossary tag names
    question: What tags exist in the data governance glossary?
  - id: getTagDetailsWithAssociatedTerms
    intent: Get a glossary tag
    question: What terms are associated with a particular tag?
  - id: createTagV2
    intent: Create a glossary tag
    question: How do I add a new tag to the glossary?
  phrasing_ops: 3
  slug: onetrust-tags-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to add, update, and retrieve structured or unstructured data discovery results linked to privacy requests.
  name: OneTrust Targeted Data Discovery API
  phrasing_intents:
  - id: getAllGroupAndAttachmentDetailsUsingGET
    intent: Get results for a data discovery group
    question: What personal data did targeted discovery find in one group for a request?
  - id: getAllGroupByRequestUsingGET
    intent: List data discovery groups for a request
    question: Which targeted data discovery groups exist for a subject rights request?
  - id: dataDiscoveryUpdatesUsingPOST
    intent: Add discovery results to a request
    question: How do I report what personal data a system holds back to a data subject request?
  - id: unstructuredDataDiscoveryUpdatesUsingPOST
    intent: Add unstructured discovery data points to a request
    question: How do I add unstructured data findings like documents to a subject request?
  phrasing_ops: 4
  slug: onetrust-targeted-data-discovery-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Task Management APIs are used to manage tasks associated with AI Governance entities.
  name: OneTrust Task Management API
  phrasing_intents:
  - id: createTaskUsingPOST_1
    intent: Create an AI governance task
    question: Can I create a task on an AI model, dataset or agent?
  - id: findTaskUsingGET_1
    intent: Get an AI governance task
    question: What's the assignee, deadline and activity history of a governance task?
  - id: updateTaskUsingPUT_1
    intent: Update an AI governance task
    question: Can I change the status or assignee of an AI governance task?
  phrasing_ops: 3
  slug: onetrust-task-management-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Tasks APIs are used to manage tasks, including creation, updates, and retrieval.
  name: OneTrust Tasks API
  phrasing_intents:
  - id: createTaskUsingPOST
    intent: Create a task on an issue
    question: Can I create a task on an issue and assign it by email?
  - id: getTaskByIdAndTaskTypeNameKeyUsingGET
    intent: Get a task
    question: What is the status, priority and deadline of a task?
  - id: updateTaskUsingPUT
    intent: Update a task
    question: Can I change a task's status, assignee or priority?
  phrasing_ops: 3
  slug: onetrust-tasks-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage assessment template operations including import and export functionality for cross-tenant migration, retrieval of published template listings with type-based filtering, and template del
  name: OneTrust Template API
  phrasing_intents:
  - id: getAllBasicTemplateDetailsUsingGET
    intent: List published assessment templates
    question: Which assessment templates are published?
  - id: importTemplateByIdUsingPOST
    intent: Import an assessment template
    question: How do I move a template from one tenant to another?
  - id: deleteTemplateVersionsUsingDELETE
    intent: Delete an assessment template
    question: Can I delete a template that is not used by any assessment?
  - id: exportTemplateWithBusinessKeysUsingGET
    intent: Export an assessment template
    question: Can I export a template's questions and metadata as JSON?
  phrasing_ops: 4
  slug: onetrust-template-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Templates APIs are used to manage reusable consent templates that define the structure and behavior of consent experiences.
  name: OneTrust Templates API
  phrasing_intents:
  - id: getTemplates
    intent: List cookie consent templates
    question: What cookie consent templates do we have and which version is current?
  - id: getTemplateDetails
    intent: Get a cookie consent template
    question: What banner, preference center and cookie list does a template include?
  phrasing_ops: 2
  slug: onetrust-templates-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: 'APIs to manage glossary terms, including creating new terms with custom attributes, retrieving term lists with search and pagination capabilities, accessing individual term details, and managing term '
  name: OneTrust Terms API
  phrasing_intents:
  - id: retrieveAllTerms
    intent: List or search glossary terms
    question: Which terms are in my business glossary?
  - id: getTermAttributeByName
    intent: Get a term attribute
    question: What are the details of a specific term attribute?
  - id: getAllTermAttributeNames
    intent: List term attributes
    question: Which term attributes have internal and external systems created?
  - id: retrieveTermsByName
    intent: Get a glossary term by name
    question: What's the description and type of a specific glossary term?
  - id: retrieveTermsName
    intent: List glossary term names
    question: Can I get just the names of all glossary terms?
  - id: createTermUsingPOST
    intent: Create a glossary term
    question: How do I add a new term to a glossary?
  phrasing_ops: 6
  slug: onetrust-terms-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to handle threat library operations including threat creation, modification, deletion, and comprehensive search functionality with framework and category support.
  name: OneTrust Threats API
  phrasing_intents:
  - id: addThreatUsingPOST_1
    intent: Create a threat
    question: How do I add a single new threat to the Threat Library?
  - id: findThreatsByCriteriaUsingPOST
    intent: Search threats
    question: What threats are in my Threat Library?
  - id: removeThreatUsingDELETE
    intent: Delete a threat
    question: How do I remove a threat from the Threat Library?
  - id: updateThreatsUsingPUT
    intent: Update threats in bulk
    question: How do I update attributes on several existing threats at once?
  - id: addThreatsUsingPOST
    intent: Create multiple threats
    question: How do I import many new threats into the Threat Library at once?
  phrasing_ops: 5
  slug: onetrust-threats-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Training API from OneTrust — 5 operation(s) for training.
  name: OneTrust Training API
  phrasing_intents:
  - id: listOfCoursesUsingGet
    intent: List training courses
    question: What training courses are available to assign?
  - id: enrollUsersToCourseUsingPost
    intent: Enroll users in a training course
    question: How do I assign a compliance course to a group of employees?
  - id: getStatusOfEnrollmentUsingGET
    intent: Get a user's course progress
    question: Has an employee finished their assigned course?
  - id: unEnrollUserUsingDELETE
    intent: Unenroll a user from a course
    question: Can I remove someone from a course they were assigned?
  - id: getEnrollmentDetailsUsingPOST
    intent: List course enrollment details
    question: Which users are enrolled in which courses?
  phrasing_ops: 5
  slug: onetrust-training-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Transactions APIs are used to manage consent transactions.
  name: OneTrust Transactions API
  phrasing_intents:
  - id: withdrawTransactionBehalfOfDatasubjectUsingPUT
    intent: Withdraw consent on a data subject's behalf
    question: Can an admin withdraw consent for a customer who asked by phone?
  - id: withdrawTransactionByPurposeAndIdentifierUsingGET
    intent: Withdraw a data subject's consent via link
    question: Can a data subject withdraw their own consent for one purpose through a simple GET link?
  phrasing_ops: 2
  slug: onetrust-transactions-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs for managing consent transactions.
  name: OneTrust Transactions V2 API
  phrasing_intents:
  - id: getTransactionsUsingPOST
    intent: List consent transactions
    question: Which consent transactions happened in a given date window?
  phrasing_ops: 1
  slug: onetrust-transactions-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage Universal Consent purposes and their associated metadata.
  name: OneTrust UC Purposes API
  phrasing_intents:
  - id: get_UCPurposes
    intent: Load universal consent purposes for an app
    question: What universal consent purposes should my app display?
  phrasing_ops: 1
  slug: onetrust-uc-purposes-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage user groups and their memberships. Create groups to organize users, assign permissions collectively, add or remove members, and retrieve information about existing groups and their memb
  name: OneTrust User Groups API
  phrasing_intents:
  - id: retrieveUserGroupsUsingGET
    intent: List user groups
    question: What user groups exist in my account?
  - id: createUserGroupUsingPOST
    intent: Create a user group
    question: How do I set up a new group to manage user access together?
  - id: updateUserGroupUsingPUT
    intent: Rename or redescribe a user group
    question: How do I rename an existing user group?
  - id: deleteUserGroupUsingDELETE
    intent: Delete a user group
    question: How do I get rid of a user group I no longer use?
  - id: retrieveMembersUsingGET
    intent: List members of a user group
    question: Who belongs to a given user group?
  - id: addMembersUsingPOST
    intent: Add users to a user group
    question: How do I add people to a user group?
  - id: removeMembersUsingDELETE
    intent: Remove users from a user group
    question: How do I take someone out of a user group?
  phrasing_ops: 7
  slug: onetrust-user-groups-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage user groups and their memberships. Create groups to organize users, assign permissions collectively, add or remove members, and retrieve information about existing groups and their memb
  name: OneTrust User Groups V2 API
  phrasing_intents:
  - id: getAllUserGroupWithFiltersV2
    intent: List user groups
    question: Which user groups exist in my OneTrust access settings?
  - id: createUserGroupV2
    intent: Create a user group
    question: What do I need to set up a new user group for access management?
  - id: getUserGroupByIdV2
    intent: Get a user group
    question: Where can I see the name and description of one specific user group?
  - id: updateUserGroupByIdV2
    intent: Rename or re-describe a user group
    question: Can I rename an existing user group?
  - id: deleteUserGroupByIdV2
    intent: Delete a user group
    question: Can I permanently delete a user group I no longer need?
  - id: getAccessLevelsForUserGroupByIdV2
    intent: List a user group's roles
    question: Which roles and organizations does a user group currently have?
  - id: updateAccessLevelForUserGroupByIdV2
    intent: Swap a role on a user group
    question: Can I replace one role on a user group with a different role and organization?
  - id: addAccessLevelsForUserGroupByIdV2
    intent: Add a role to a user group
    question: Can I grant an additional role to a user group for a specific organization?
  phrasing_ops: 14
  slug: onetrust-user-groups-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: V3 version APIs to manager User Groups.
  name: OneTrust User Groups V3 API
  phrasing_intents:
  - id: getGroups
    intent: List SCIM user groups
    question: Which user groups can my identity provider see over SCIM?
  - id: createGroup
    intent: Create a SCIM user group
    question: Can my identity provider create a user group through SCIM?
  - id: getGroupById
    intent: Get a SCIM user group
    question: Can I look up one SCIM user group and its members?
  - id: updateGroup
    intent: Replace a SCIM user group
    question: Can I fully replace a SCIM group's name and membership in one call?
  - id: deleteGroup
    intent: Delete a SCIM user group
    question: Can my identity provider delete a user group over SCIM?
  - id: modifyGroup
    intent: Patch a SCIM user group
    question: Can I add or remove a few members of a SCIM group without replacing it?
  phrasing_ops: 6
  slug: onetrust-user-groups-v3-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage users and their memberships and access levels.
  name: OneTrust Users V2 API
  phrasing_intents:
  - id: getAllUserDetailsV2
    intent: List all users in the account
    question: Who are all the users in my OneTrust account?
  - id: createUserV2
    intent: Create a new user in the account
    question: How do I add a new person as a user in my privacy account?
  - id: getUserV2
    intent: Get one user's account details
    question: What details are stored for a single user in my account?
  - id: updateUserV2
    intent: Update a user's name and access details
    question: How do I change a user's name or expiration date in the account?
  - id: getUserAccessLevelsV2
    intent: List the roles assigned to a user
    question: Which roles does a particular user hold?
  - id: addUserAccessLevelV2
    intent: Grant a role to a user in an organization
    question: How do I give a user an additional role?
  - id: removeUserAccessLevelV2
    intent: Remove a role from a user
    question: How do I take a role away from a user?
  - id: setUserDefaultOrganizationV2
    intent: Change a user's default organization
    question: How do I change which organization a user lands in by default?
  phrasing_ops: 14
  slug: onetrust-users-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: V3 version APIs to manager Users.
  name: OneTrust Users V3 API
  phrasing_intents:
  - id: getUsers
    intent: List SCIM users
    question: Which users are provisioned in my account over SCIM?
  - id: createUser
    intent: Provision a user via SCIM
    question: Can my identity provider create a user and give them a role?
  - id: getUserById
    intent: Get a SCIM user
    question: Which groups does a specific provisioned user belong to?
  - id: updateUser
    intent: Replace a SCIM user's attributes
    question: Can I overwrite all of a user's attributes in one SCIM call?
  - id: modifyUser
    intent: Activate, deactivate or patch a SCIM user
    question: Can I deactivate a user through SCIM?
  phrasing_ops: 5
  slug: onetrust-users-v3-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage third-party vendor information and their data processing activities.
  name: OneTrust Vendors API
  phrasing_intents:
  - id: get_Vendors
    intent: List IAB and Google vendors for a preference center
    question: Which IAB and Google vendors should my mobile preference center show?
  phrasing_ops: 1
  slug: onetrust-vendors-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to create, update, and retrieve methods for verifying a data subject's identity.
  name: OneTrust Verification Methods API
  phrasing_intents:
  - id: getAllV2VerificationMethodsUsingGET
    intent: List a request's verification methods
    question: Which identity verification methods are on a data subject request?
  - id: updateV2VerificationMethodUsingPUT
    intent: Update a verification method's status
    question: Can I mark a request's identity verification as passed or failed?
  - id: createV2VerificationMethodUsingPOST
    intent: Add a verification method to a request
    question: Can I add a new identity verification method to a request?
  - id: getAllV2VerificationMethodsByIdUsingGET
    intent: Get one verification method
    question: Can I look up a single verification method on a request by its ID?
  phrasing_ops: 4
  slug: onetrust-verification-methods-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to manage vulnerabilities in the vulnerability library including creation, updates, deletion, and retrieval with support for bulk operations and custom attributes.
  name: OneTrust Vulnerabilities API
  phrasing_intents:
  - id: addVulnerabilityUsingPOST_1
    intent: Add one vulnerability to the library
    question: How do I add a single vulnerability to the Vulnerability Library?
  - id: findVulnerabilitiesByCriteriaUsingPOST
    intent: Search the Vulnerability Library
    question: Which vulnerabilities in the library relate to a given keyword?
  - id: removeVulnerabilityUsingDELETE
    intent: Delete a vulnerability from the library
    question: How do I remove an outdated vulnerability from the library?
  - id: updateVulnerabilitiesUsingPUT
    intent: Update attributes of vulnerabilities in bulk
    question: How do I update attributes on several vulnerabilities at once?
  - id: addVulnerabilitiesUsingPOST
    intent: Add many vulnerabilities at once
    question: Can I import a batch of vulnerabilities into the library in one call?
  phrasing_ops: 5
  slug: onetrust-vulnerabilities-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: The Websites V2 API from OneTrust — 1 operation(s) for websites v2.
  name: OneTrust Websites V2 API
  phrasing_intents:
  - id: requestBulkAddDomainUsingPOST
    intent: Add websites to the scanner
    question: Can I add several websites to be scanned at once?
  - id: getDomainsScannedBySortUsingGET
    intent: List scanned websites
    question: Which websites are in the scanner and when were they last scanned?
  phrasing_ops: 2
  slug: onetrust-websites-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs used to import and export workflows in JSON format for version 2 workflows.
  name: OneTrust Workflows V2 API
  phrasing_intents:
  - id: exportWorkflowUsingGET_1
    intent: Export an integration workflow as JSON
    question: How do I back up an integration workflow to a JSON file?
  - id: importWorkflowUsingPOST_1
    intent: Import an integration workflow from JSON
    question: How do I load an integration workflow from a JSON file?
  phrasing_ops: 2
  slug: onetrust-workflows-v2-api
- baseURL: https://app.onetrust.com
  baseurl_source: declared
  description: APIs to handle audit workpaper operations including testing results, sampling outcomes, interview findings, control assessments, and workpaper attribute management.
  name: OneTrust Workpapers API
  phrasing_intents:
  - id: getAuditWorkpaperListViewUsingPOST
    intent: Search audit workpapers
    question: Which audit workpapers mention a specific control or keyword?
  - id: editWorkpaperDetailsUsingPOST
    intent: Record results on an audit workpaper
    question: How do I record testing results on an audit workpaper?
  - id: getWorkpaperResultUsingGET
    intent: Get a workpaper's results and attributes
    question: What were the testing, sampling and interview results on a workpaper?
  - id: getWorkpaperBasicDetailInformationUsingGET
    intent: Get the control details of a workpaper
    question: Which control is an audit workpaper testing?
  phrasing_ops: 4
  slug: onetrust-workpapers-api
artifact_total: 154
asyncapis:
- description: ''
  name: Onetrust Webhooks
  slug: onetrust-webhooks
common:
- group: other
  href: https://artifacts.apis.io/onetrust/capabilities/onetrust-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/onetrust-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-ai-governance-ai-governance-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-ai-governance-ai-governance-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-platform-global-activity-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-global-activity-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-consent-and-preferences-consent-interfaces-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-consent-interfaces-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-consent-and-preferences-consent-management-platform-cmp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-consent-management-platform-cmp-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-consent-and-preferences-consent-receipts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-consent-receipts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-consent-and-preferences-cookie-consent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-cookie-consent-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-consent-and-preferences-cookie-consent-swagger-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-cookie-consent-swagger-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-consent-and-preferences-cookie-domain-data-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-cookie-domain-data-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-consent-and-preferences-cross-device-consent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-cross-device-consent-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-consent-and-preferences-mobile-app-consent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-mobile-app-consent-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-consent-and-preferences-policy-and-notice-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-policy-and-notice-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-consent-and-preferences-universal-consent-and-preference-management-oas-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-consent-and-preferences-universal-consent-and-preference-management-oas-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-data-use-governance-data-catalog-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-data-use-governance-data-catalog-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-data-use-governance-data-discovery-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-data-use-governance-data-discovery-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-data-use-governance-data-discovery-worker-node-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-data-use-governance-data-discovery-worker-node-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-esg-program-reporting-and-disclosures-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-esg-program-reporting-and-disclosures-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-platform-access-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-access-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-platform-bulk-export-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-bulk-export-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-platform-documents-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-documents-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-platform-integrations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-integrations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-platform-inventory-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-inventory-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-platform-object-manager-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-object-manager-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-platform-task-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-task-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-platform-user-provisioning-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-platform-user-provisioning-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-privacy-automation-assessment-automation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-privacy-automation-assessment-automation-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-privacy-automation-data-mapping-automation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-privacy-automation-data-mapping-automation-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-privacy-automation-data-mapping-automation-swagger-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-privacy-automation-data-mapping-automation-swagger-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-privacy-automation-data-subject-request-dsr-automation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-privacy-automation-data-subject-request-dsr-automation-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-privacy-automation-incident-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-privacy-automation-incident-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-the-trust-intelligence-platform-document-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-the-trust-intelligence-platform-document-gateway-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-tech-risk-and-compliance-audit-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-tech-risk-and-compliance-audit-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-tech-risk-and-compliance-compliance-automation-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-tech-risk-and-compliance-compliance-automation-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-tech-risk-and-compliance-enterprise-policy-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-tech-risk-and-compliance-enterprise-policy-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-tech-risk-and-compliance-issues-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-tech-risk-and-compliance-issues-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-tech-risk-and-compliance-it-risk-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-tech-risk-and-compliance-it-risk-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-tech-risk-and-compliance-training-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-tech-risk-and-compliance-training-overlay.yaml
- group: other
  href: https://artifacts.apis.io/onetrust/overlays/onetrust-third-party-management-third-party-risk-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/onetrust-third-party-management-third-party-risk-management-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.onetrust.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.onetrust.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.onetrust.com/onetrust/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.onetrust.com/onetrust/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.onetrust.com/onetrust/reference/quick-start-guide
- group: operate
  title: ''
  type: Support
  url: https://my.onetrust.com/s/
- group: company
  title: ''
  type: Blog
  url: https://www.onetrust.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/onetrust-oss
- group: commercial
  title: ''
  type: Pricing
  url: https://www.onetrust.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.onetrust.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.onetrust.com/privacy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/onetrust
- group: operate
  title: ''
  type: StatusPage
  url: https://my.onetrust.com/s/system-status
- group: operate
  href: https://artifacts.apis.io/onetrust/lifecycle/onetrust-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/onetrust-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/onetrust/lifecycle/onetrust-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/onetrust-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/onetrust/changelog/onetrust-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/onetrust-changelog.yml
- group: auth
  href: https://artifacts.apis.io/onetrust/authentication/onetrust-authentication.yml
  title: ''
  type: Authentication
  url: authentication/onetrust-authentication.yml
- group: auth
  href: https://artifacts.apis.io/onetrust/scopes/onetrust-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/onetrust-scopes.yml
- group: design
  href: https://artifacts.apis.io/onetrust/conventions/onetrust-conventions.yml
  title: ''
  type: Conventions
  url: conventions/onetrust-conventions.yml
- group: design
  href: https://artifacts.apis.io/onetrust/errors/onetrust-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/onetrust-problem-types.yml
- group: design
  href: https://artifacts.apis.io/onetrust/data-model/onetrust-data-model.yml
  title: ''
  type: DataModel
  url: data-model/onetrust-data-model.yml
- group: operate
  href: https://artifacts.apis.io/onetrust/rate-limits/onetrust-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/onetrust-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/onetrust/plans/onetrust-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/onetrust-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/onetrust/finops/onetrust-finops.yml
  title: ''
  type: FinOps
  url: finops/onetrust-finops.yml
- group: build
  href: https://artifacts.apis.io/onetrust/packages/onetrust-packages.yml
  title: ''
  type: Packages
  url: packages/onetrust-packages.yml
- group: build
  href: https://artifacts.apis.io/onetrust/packages/onetrust-packages.yml
  title: ''
  type: SDKs
  url: packages/onetrust-packages.yml
- group: design
  href: https://artifacts.apis.io/onetrust/components/onetrust-components.yml
  title: ''
  type: Components
  url: components/onetrust-components.yml
- group: start
  href: https://artifacts.apis.io/onetrust/sandbox/onetrust-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/onetrust-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/onetrust/mcp/onetrust-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/onetrust-mcp.yml
- group: build
  href: https://artifacts.apis.io/onetrust/mcp/onetrust-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/onetrust-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/onetrust/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/onetrust/agentic-access/onetrust-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/onetrust-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/onetrust/llms/onetrust-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/onetrust-llms.txt
- group: agent
  href: https://artifacts.apis.io/onetrust/well-known/onetrust-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/onetrust-well-known.yml
- group: other
  href: https://artifacts.apis.io/onetrust/well-known/onetrust-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/onetrust-api-catalog.json
- group: design
  href: https://artifacts.apis.io/onetrust/asyncapi/onetrust-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/onetrust-webhooks.yml
- group: design
  href: https://artifacts.apis.io/onetrust/conformance/onetrust-conformance.yml
  title: ''
  type: Conformance
  url: conformance/onetrust-conformance.yml
- group: auth
  href: https://artifacts.apis.io/onetrust/conformance/onetrust-conformance.yml
  title: ''
  type: Compliance
  url: conformance/onetrust-conformance.yml
- group: auth
  href: https://artifacts.apis.io/onetrust/security/onetrust-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/onetrust-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/onetrust/security/onetrust-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/onetrust-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/onetrust/security/onetrust-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/onetrust-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/onetrust/security/onetrust-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/onetrust-domain-security.yml
created: '2026-05-08'
description: OneTrust is an enterprise trust, privacy, and AI-governance platform. Its developer portal publishes 37 downloadable OpenAPI definitions covering roughly 631 operations across Universal Consent & Preference Management, Cookie Consent / CMP, Consent Receipts, Data Subject Request (DSR) Automation, Assessment Automation (PIA/DPIA), Data Mapping, Data Catalog and Data Discovery, Incident Management, IT & Security Risk Management, Audit Management, Issues Management, Enterprise Policy Management, Compliance Automation, Third-Party Risk Management, ESG Program Reporting, AI Governance, and the shared platform services (Access Management, SCIM 2.0 User Provisioning, Object Manager, Inventory, Bulk Export, Documents, Integrations, Task Management, Global Activity). Every API is authorized with OAuth 2.0 client credentials against a per-tenant environment host, and the portal also serves an RFC 9727 /.well-known/api-catalog, an llms.txt, and a public remote MCP server.
finops:
- has_sources: true
  method: derived
  name: Onetrust Finops
  primary_unit: ''
  service_category: ''
  slug: onetrust-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/onetrust.png
layout: provider
mcp_servers:
- description: OneTrust hosts a public remote MCP server on its developer portal. It is documented on a dedicated "MCP Server" page in the API reference, requires no authentication headers, and answered a live tools
  name: OneTrust Developer Portal MCP Server
  slug: onetrust-developer-portal-mcp-server
modified: '2026-08-27'
name: OneTrust
nav: Providers
network: true
overview: 'OneTrust publishes 138 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activity Log API, Applications API, Assessment Actions API, and 135 more. Tagged areas include Privacy, GRC, Compliance, Consent, and Third-Party Risk Management.


  The OneTrust catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  OneTrust''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 73 more developer resources.'
plans:
- name: Onetrust Plans Pricing
  plan_count: 1
  slug: onetrust-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 12
  name: Onetrust Rate Limits
  slug: onetrust-rate-limits
rules:
- authorship: generated
  effective_rule_count: 116
  extends:
  - spectral:oas
  name: OneTrust API Rules
  rule_count: 75
  severity_counts:
    error: 39
    hint: 0
    info: 7
    warn: 29
  slug: onetrust-rules
scopes:
- name: Onetrust Scopes
  scope_count: 51
  slug: onetrust-scopes
  summary_line: 51 scopes · clientCredentials
score:
  band: exemplar
  composite: 77.1
  coverage:
    artifact_dirs: 33
    catalog_earned: 64.5
    catalog_earned_first_party: 20.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.8
  facets:
    access_clarity: 47.4
    contract_governance: 31.8
    contract_quality: 65.9
    developer_ergonomics: 70.8
    discoverability: 80.0
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 73.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 63.0
      derived: 0
      marker_coverage: 0.0
      total: 146
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 100.0
screenshot: https://apis.io/screenshots/onetrust/onetrust-2026-06-20T190718.png
security:
- kind: authentication
  name: Onetrust Authentication
  slug: onetrust-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Onetrust Domain Security
  slug: onetrust-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Onetrust Vulnerability Disclosure
  slug: onetrust-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Onetrust Trust Center
  slug: onetrust-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 4
skills:
- name: onetrust-fulfill-dsr-request
  slug: onetrust-fulfill-dsr-request
- name: onetrust-provision-users-scim
  slug: onetrust-provision-users-scim
- name: onetrust-record-consent
  slug: onetrust-record-consent
- name: onetrust-scan-and-publish-cookie-consent
  slug: onetrust-scan-and-publish-cookie-consent
slug: onetrust
tags:
- Privacy
- GRC
- Compliance
- Consent
- Third-Party Risk Management
- AI Governance
- Data Governance
- Risk Management
- Data Discovery
- ESG
- Security
- SCIM
website: https://www.onetrust.com/
---
