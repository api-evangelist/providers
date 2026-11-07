---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 404
  human_in_the_loop: 13
  name: Dotcms Agentic Access
  operation_count: 768
  slug: dotcms-agentic-access
  summary_line: 768 operations · 404 acting · 13 human-in-the-loop
api_count: 1
apis:
- description: The dotCMS GraphQL API provides a single endpoint for querying content across all content types using a self-documenting schema. It supports Lucene-style query strings, pagination, sorting, and conten
  name: dotCMS GraphQL API
  slug: graphql
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Streaming a11y-fix agent proxy
  name: dotCMS Accessibility Agent API
  phrasing_intents:
  - id: runA11yAgentFix
    intent: Run the accessibility fix agent on a page
    question: Can dotCMS automatically fix accessibility issues on a page?
  - id: streamA11yAgentFix
    intent: Run the accessibility agent with live progress
    question: Can I watch the accessibility fix agent's progress as it runs?
  - id: stopA11yAgentRun
    intent: Stop an accessibility fix run
    question: How do I stop an accessibility fix that's still running?
  phrasing_ops: 3
  slug: dotcms-accessibility-agent-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Endpoints that perform operations related to validating accessibility in content.
  name: dotCMS Accessibility Checker API
  phrasing_intents:
  - id: getAccessibilityGuidelines
    intent: List the accessibility guidelines available
    question: Which accessibility guidelines, like WCAG levels, can content be validated against?
  - id: postValidateContent
    intent: Validate content against accessibility guidelines
    question: How do I check a piece of HTML content for accessibility problems?
  - id: a11yCheck
    intent: Scan a live page URL for accessibility issues
    question: Can I run an accessibility scan on a published page by its URL?
  - id: geoCheck
    intent: Scan a page URL for generative engine optimization
    question: How well is a page optimized for AI answer engines (GEO)?
  phrasing_ops: 4
  slug: dotcms-accessibility-checker-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: System administration and management tools
  name: dotCMS Administration API
  phrasing_intents:
  - id: getLayout_2
    intent: Call the REST example layout endpoint
    question: What does the restexample layout endpoint return for given parameters?
  - id: loadJson
    intent: Call the REST example JSON test endpoint
    question: Is there a sample endpoint that returns test JSON?
  - id: getLoggedInUser
    intent: Encode a query parameter value
    question: Can dotCMS URL-encode a value for me to use in a query string?
  - id: getEvents
    intent: Poll for system events
    question: How do I poll for dotCMS system events without websockets?
  - id: getSyncEvents
    intent: Fetch system events synchronously
    question: Is there a synchronous version of the system events feed?
  - id: getJvmInfo
    intent: Get JVM information
    question: What JVM is my dotCMS server running on?
  - id: addToolGroupToUser
    intent: Give a user a tool group
    question: How do I add a tool group (menu layout) to a user?
  - id: deleteToolGroupFromUser
    intent: Remove a tool group from a user
    question: How do I take a tool group away from a user?
  phrasing_ops: 10
  slug: dotcms-administration-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: AI-powered content generation and analysis endpoints
  name: dotCMS AI API
  phrasing_intents:
  - id: listAiProviders
    intent: List dotAI providers and their config fields
    question: Which AI providers can dotAI use and do they support chat, embeddings or images?
  - id: testAiProviderConnection
    intent: Test a dotAI provider connection
    question: How can I check that my AI provider credentials actually work before saving them?
  - id: getAiConfig
    intent: Get the AI service configuration
    question: What AI configuration is currently set for my site?
  - id: saveAiConfig
    intent: Save AI provider configuration for a site
    question: How do I save new AI provider settings for a site?
  - id: rawPrompt
    intent: Send a raw prompt to the AI without content lookup
    question: Can I send a prompt straight to the model without dotCMS adding content context?
  - id: summarizeFromContent
    intent: Generate an AI answer grounded in site content
    question: How do I get an AI summary built from content in my dotCMS embeddings index?
  - id: count_1
    intent: Count embeddings matching query-string filters
    question: How many embeddings exist for a given content type or site?
  - id: count
    intent: Count embeddings using a JSON filter body
    question: Can I count embeddings by posting a JSON search form instead of query parameters?
  phrasing_ops: 23
  slug: dotcms-ai-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: System announcements and notifications
  name: dotCMS Announcements API
  phrasing_intents:
  - id: announcements
    intent: Get the latest dotCMS announcements
    question: What product announcements are showing in my dotCMS dashboard?
  phrasing_ops: 1
  slug: dotcms-announcements-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: API token management and authentication
  name: dotCMS API Token API
  phrasing_intents:
  - id: deleteApiTokenByIdV1
    intent: Delete an API token
    question: How do I permanently delete an API token, even an expired one?
  - id: getApiTokensByUserIdV1
    intent: List a user's API tokens
    question: Which API tokens does a given user have?
  - id: getExpiringApiTokensV1
    intent: List API tokens about to expire
    question: Which API tokens will expire soon?
  - id: getJwtFromApiTokenV1
    intent: Generate a new JWT for a token
    question: How do I get a fresh JWT for an existing API token?
  - id: putGetRemoteTokenV1
    intent: Get a token for a remote dotCMS instance
    question: How do I obtain an API token from another dotCMS server?
  - id: postIssueApiTokenV1
    intent: Issue an API token
    question: How do I create a new API token for a user?
  - id: putRevokeTokenByIdV1
    intent: Revoke an API token
    question: How do I revoke a leaked API token?
  phrasing_ops: 7
  slug: dotcms-api-token-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Third-party application integration and configuration
  name: dotCMS Apps API
  phrasing_intents:
  - id: listAvailableApps
    intent: List available app integrations
    question: Which third-party app integrations are available in dotCMS?
  - id: createApp
    intent: Upload a new app descriptor
    question: How do I add a new app integration by uploading its YAML descriptor?
  - id: deleteIndividualAppSecret
    intent: Delete specific secrets of an app on a site
    question: How do I remove just one secret from an app's configuration on a site?
  - id: getAppDetail
    intent: Get an app's configuration on a site
    question: How is a particular app configured for one of my sites?
  - id: updateAppIndividualSecret
    intent: Update one secret of an app on a site
    question: How do I change a single secret value for an app on a site?
  - id: createAppSecrets
    intent: Save an app's full set of secrets on a site
    question: How do I configure an app for a site by saving all its secrets?
  - id: deleteAllAppSecrets
    intent: Remove all of an app's secrets from a site
    question: How do I wipe an app's entire configuration from one site?
  - id: getAppByKey
    intent: Get an app and the sites it's configured on
    question: Which sites have a given app configured?
  phrasing_ops: 12
  slug: dotcms-apps-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: The Authentication API from dotCMS — 6 operation(s) for authentication.
  name: dotCMS Authentication API
  phrasing_intents:
  - id: postAuthenticationV1
    intent: Log in with a username and password
    question: How do I start a session with my dotCMS login and password?
  - id: getLogInUserV1
    intent: Get the currently logged-in user
    question: Who am I logged in as right now?
  - id: forgotPassword
    intent: Send a password reset email
    question: I forgot my password; how do I get a reset link emailed?
  - id: loginForm
    intent: Get the login form configuration
    question: What languages and company details does the login screen offer?
  - id: logoutUser
    intent: Log out the current user
    question: How do I end my dotCMS session?
  - id: resetPassword
    intent: Set a new password with a reset token
    question: How do I choose a new password using the token from my reset email?
  phrasing_ops: 6
  slug: dotcms-authentication-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: File and folder browser tree operations
  name: dotCMS Browser Tree API
  phrasing_intents:
  - id: getFolderContent
    intent: Browse a folder's files, pages and subfolders
    question: How do I list what's inside a folder in the site browser, including pages and files?
  - id: getSelectFolder
    intent: Get the folder currently selected in the browser
    question: Which folder did I last select in the site browser?
  - id: selectFolder
    intent: Set the selected folder in the site browser
    question: How do I make the site browser remember a folder as selected?
  - id: loadAssetsUnder
    intent: Load the asset tree at a site's root
    question: How do I get the folders and assets at the top level of a site?
  - id: loadAssetsUnder_1
    intent: Load the asset tree under a site path
    question: How do I list assets under a specific URI path of a site?
  phrasing_ops: 5
  slug: dotcms-browser-tree-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Content bundle management and deployment
  name: dotCMS Bundle API
  phrasing_intents:
  - id: publish
    intent: Receive and publish an incoming bundle
    question: How does a receiving dotCMS server accept a pushed bundle and publish it?
  - id: deleteAll
    intent: Delete every bundle
    question: Can I wipe the entire publishing queue history of bundles in one go?
  - id: deleteAllFail
    intent: Delete all failed bundles
    question: How do I clean up only the bundles that failed to publish?
  - id: deleteAllSuccess
    intent: Delete all successfully published bundles
    question: Can I purge bundles that already published successfully?
  - id: deleteBundlesByIdentifiers
    intent: Delete specific bundles by ID
    question: Can I delete a handful of bundles by listing their IDs?
  - id: deleteBundlesOlderThan
    intent: Delete bundles older than a date
    question: Can I clean out old bundles created before a certain date?
  - id: deleteEnvironmentPushHistory
    intent: Clear push history for an environment
    question: Can I reset the push history for one publishing environment so everything pushes again?
  - id: deletePushHistory
    intent: Clear push history for an asset
    question: How do I clear the push history of a single piece of content?
  phrasing_ops: 16
  slug: dotcms-bundle-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Cache provider management and operations
  name: dotCMS Cache Management API
  phrasing_intents:
  - id: deleteMenuCache
    intent: Clear the navigation menu cache
    question: My site navigation is stale — can I clear just the menu cache?
  - id: flushAll
    intent: Flush all caches
    question: How do I flush every cache in dotCMS at once?
  - id: flushGroup
    intent: Flush one cache group for a provider
    question: Can I flush a single cache group on one cache provider?
  - id: flushObject
    intent: Evict one object from the cache
    question: Can I evict a single key from a cache group?
  - id: flushRegion
    intent: Flush a cache region across providers
    question: How do I flush one named cache region on every provider?
  - id: getCacheStats
    intent: Get cache statistics
    question: What are the cache hit and miss rates right now?
  - id: getKeys
    intent: List keys in a cache group
    question: Which keys are stored in a given cache group?
  - id: listRegions
    intent: List cache region names
    question: What cache regions exist that I could flush?
  phrasing_ops: 12
  slug: dotcms-cache-management-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Content categorization and taxonomy
  name: dotCMS Categories API
  phrasing_intents:
  - id: getCategories
    intent: List categories
    question: What top-level categories are set up in dotCMS?
  - id: updateCategory
    intent: Update an existing category
    question: How do I rename an existing category?
  - id: createCategory
    intent: Create a new category
    question: How do I add a new category to use for tagging content?
  - id: deleteCategories
    intent: Delete categories and their descendants
    question: Does deleting a category also delete all of its subcategories?
  - id: exportCategories
    intent: Export categories to CSV
    question: Can I download my category tree as a CSV?
  - id: getCategoryByIdOrKey
    intent: Get a category by ID or key
    question: How do I look up a single category by its key?
  - id: getCategoryChildren
    intent: List the children of a category
    question: What subcategories sit under a given parent category?
  - id: getCategoryHierarchy
    intent: Get parent chains for several categories
    question: Which parent categories sit above each of these category keys?
  phrasing_ops: 10
  slug: dotcms-categories-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Cluster nodes and distributed system management
  name: dotCMS Cluster Management API
  phrasing_intents:
  - id: getESConfigProperties
    intent: Get the cluster's Elasticsearch config properties
    question: What Elasticsearch configuration properties is the cluster running with?
  - id: getLicenseRepoStatus
    intent: Check the license repository status
    question: What is the current status of the cluster's license repository?
  - id: getNodesInfo
    intent: Get the status of every cluster node
    question: Which nodes are in my dotCMS cluster and are they healthy?
  - id: removeFromCluster
    intent: Remove a node from the cluster
    question: How do I take a dead server out of the cluster?
  - id: testCluster
    intent: Test cluster communication
    question: Are the cluster nodes able to talk to each other?
  phrasing_ops: 5
  slug: dotcms-cluster-management-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Endpoints for managing Container objects and their content
  name: dotCMS Containers API
  phrasing_intents:
  - id: archiveContainer
    intent: Archive a container
    question: How do I archive a single container I no longer use?
  - id: bulkArchiveContainers
    intent: Archive several containers at once
    question: Can I archive a whole list of containers in one request?
  - id: bulkDeleteContainers
    intent: Delete several containers at once
    question: Can I permanently delete a batch of containers together?
  - id: bulkPublishContainers
    intent: Publish several containers at once
    question: Is there a way to publish many containers in a single call?
  - id: bulkUnarchiveContainers
    intent: Unarchive several containers at once
    question: Can I restore a batch of archived containers in one request?
  - id: bulkUnpublishContainers
    intent: Unpublish several containers at once
    question: Can I take a set of containers offline together?
  - id: getContainerContentById
    intent: Render a contentlet inside a container
    question: How do I get the HTML a contentlet renders as inside a specific container?
  - id: getContainerContentByQueryParam
    intent: Render content in a file-based container
    question: How do I render content inside a file-asset container whose ID is a path?
  phrasing_ops: 21
  slug: dotcms-containers-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Proxy endpoints that forward analytics requests to the dot-ca-event-manager service.
  name: dotCMS Content Analytics API
  phrasing_intents:
  - id: generateSiteAuth
    intent: Generate a site key for analytics events
    question: How do I get the site key my front-end JavaScript needs to send custom analytics events?
  - id: proxyAnalyticsEventRequest
    intent: Send a custom analytics event
    question: How do I record a custom Content Analytics event from my site?
  - id: proxyAnalyticsGetRequest
    intent: Query Content Analytics data
    question: Can I query Content Analytics reports through dotCMS for a site I can read?
  phrasing_ops: 3
  slug: dotcms-content-analytics-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Endpoints for managing content and contentlets - the core data objects in dotCMS
  name: dotCMS Content API
  phrasing_intents:
  - id: getContentRelationships
    intent: Fetch content with relationships (deprecated)
    question: Is there still an old endpoint that returns a contentlet together with its relationships?
  - id: canLockContent
    intent: Check whether I can lock a contentlet
    question: Am I allowed to lock this piece of content before I start editing it?
  - id: checkContentLanguageVersions
    intent: See which languages a contentlet exists in
    question: Which languages does this piece of content already have a version in?
  - id: getContentletReferencesCount
    intent: Count references to a contentlet
    question: How many places reference this contentlet?
  - id: getContent
    intent: Retrieve a contentlet
    question: How do I fetch a single contentlet by its identifier or inode in dotCMS?
  - id: getContentletReferences
    intent: List pages and containers using a contentlet
    question: Which pages, containers and personas use this contentlet?
  - id: getContentletPushHistory
    intent: View a contentlet's push publishing history
    question: When was this contentlet last push-published to another environment?
  - id: lockContent
    intent: Lock a contentlet for editing
    question: How do I lock a contentlet so nobody else edits it while I work?
  phrasing_ops: 32
  slug: dotcms-content-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Content retrieval and manipulation endpoints
  name: dotCMS Content Delivery API
  phrasing_intents:
  - id: canLockContentLegacy
    intent: Check if a contentlet can be locked (legacy)
    question: Before editing, can I check whether I'm allowed to lock a piece of content and who holds the lock now?
  - id: getContentLegacy
    intent: Retrieve content by ID, inode or query
    question: Can I pull a contentlet by its identifier and include related content two levels deep?
  - id: singlePutContent
    intent: Create or update content via PUT (deprecated)
    question: Can the old /api/content PUT endpoint update an existing contentlet as well as create one?
  - id: singlePostContent
    intent: Create content via POST (deprecated)
    question: Can I still create new content by POSTing JSON to the old content endpoint?
  - id: indexCountContent
    intent: Count content matching a Lucene query
    question: How many contentlets match a Lucene query?
  - id: indexSearchContent
    intent: Search the content index with Lucene
    question: Can I search content with a Lucene query and get back identifiers and inodes?
  - id: lockContentLegacy
    intent: Lock a contentlet (deprecated)
    question: How do I lock content so nobody else edits it at the same time?
  - id: unlockContentLegacy
    intent: Unlock a contentlet (deprecated)
    question: How do I release a lock on content so others can edit it?
  phrasing_ops: 8
  slug: dotcms-content-delivery-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: The Content Import API from dotCMS — 11 operation(s) for content import.
  name: dotCMS Content Import API
  phrasing_intents:
  - id: getAbandonedContentImportJobs
    intent: List abandoned content import jobs
    question: Which content imports were abandoned and never finished?
  - id: getActiveContentImportJobs
    intent: List active content import jobs
    question: What content imports are running or queued right now?
  - id: cancelContentImportJob
    intent: Cancel a content import job
    question: How do I stop a CSV content import that's running?
  - id: getCanceledContentImportJobs
    intent: List canceled content import jobs
    question: Which content imports were canceled?
  - id: getCompletedContentImportJobs
    intent: List completed content import jobs
    question: Which content imports have finished running, successful or not?
  - id: getFailedContentImportJobs
    intent: List failed content import jobs
    question: Which CSV content imports failed?
  - id: getJobStatus
    intent: Get a content import job's status
    question: What's the current status of my content import?
  - id: getContentImportJobs
    intent: List all content import jobs
    question: Can I see every content import job regardless of its state?
  phrasing_ops: 12
  slug: dotcms-content-import-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Content reporting and analytics
  name: dotCMS Content Report API
  phrasing_intents:
  - id: getFolderContentReport
    intent: Report content counts by type within a folder
    question: How many items of each content type live under a folder?
  - id: getSiteContentReport
    intent: Report content counts by type across a site
    question: Which content types exist on a site and how many items each has?
  phrasing_ops: 2
  slug: dotcms-content-report-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Content type definitions and schema management
  name: dotCMS Content Type API
  phrasing_intents:
  - id: getStructuresWithWYSIWYGFields
    intent: List content types that have WYSIWYG fields
    question: Which content types include a WYSIWYG rich text field?
  - id: postContentTypeCopy
    intent: Copy an existing content type
    question: How do I create a new content type based on an existing one?
  - id: getContentType
    intent: List content types
    question: What content types are defined in my dotCMS instance?
  - id: postContentTypeCreate
    intent: Create one or more content types
    question: How do I define a new content type with its fields in one request?
  - id: getContentTypeIdVar
    intent: Get a content type and its fields
    question: What fields does my Blog content type have?
  - id: putContentTypeUpdate
    intent: Replace a content type's full definition
    question: Will fields I leave out of a content type update be removed?
  - id: deleteContentType
    intent: Delete a content type
    question: How do I delete a content type I no longer need?
  - id: postContentTypeFilter
    intent: Filter content types with paging controls
    question: Can I filter content types by name and control page size and sort order?
  phrasing_ops: 12
  slug: dotcms-content-type-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Content type field definitions and configuration
  name: dotCMS Content Type Field API
  phrasing_intents:
  - id: getFieldTypes
    intent: List available field types
    question: What kinds of fields can I add to a content type in dotCMS?
  - id: getContentTypeFieldsV1
    intent: List a content type's fields (deprecated v1)
    question: How do I get all fields of a content type through the old v1 fields endpoint?
  - id: updateContentTypeFieldsV1
    intent: Bulk update content type fields (deprecated v1)
    question: Can I update several fields of a content type at once with the legacy v1 API?
  - id: createContentTypeFieldV1
    intent: Add a field to a content type (deprecated v1)
    question: How do I add a new field to a content type with the deprecated v1 fields API?
  - id: deleteContentTypeFieldsV1
    intent: Delete several fields (deprecated v1)
    question: Can I remove multiple fields from a content type in one call with the old v1 API?
  - id: getContentTypeFieldByIdV1
    intent: Get a field by ID (deprecated v1)
    question: How do I look up one content type field by its field ID with the v1 API?
  - id: updateContentTypeFieldByIdV1
    intent: Update a field by ID (deprecated v1)
    question: How do I change one field identified by its ID using the legacy v1 API?
  - id: deleteContentTypeFieldByIdV1
    intent: Delete a field by ID (deprecated v1)
    question: How do I delete a single field by its ID with the deprecated v1 fields API?
  phrasing_ops: 36
  slug: dotcms-content-type-field-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Data integrity checking and conflict resolution
  name: dotCMS Data Integrity API
  phrasing_intents:
  - id: checkIntegrity
    intent: Start an integrity check against an endpoint
    question: How do I check data integrity between this server and a push-publishing endpoint?
  - id: checkIntegrityProcessStatus
    intent: Check an integrity check's progress
    question: Is my data integrity check still running?
  - id: discardConflicts
    intent: Discard detected integrity conflicts
    question: How do I throw away integrity conflicts without fixing them?
  - id: fixConflicts
    intent: Fix detected integrity conflicts
    question: How do I resolve the conflicts an integrity check found?
  - id: fixConflictsFromRemote
    intent: Apply conflict fixes sent by a remote server
    question: How does a remote server push integrity fixes to this one?
  - id: generateIntegrityData
    intent: Generate integrity data for comparison
    question: How do I produce this server's integrity data so another server can compare it?
  - id: getIntegrityData
    intent: Download generated integrity data
    question: How do I fetch the integrity data produced for a request?
  - id: getIntegrityResult
    intent: Get integrity check results
    question: What conflicts did the integrity check find?
  phrasing_ops: 8
  slug: dotcms-data-integrity-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: 'OAuth/OIDC and SAML authentication: per-site configuration (SYSTEM_HOST is the global default) and headless OIDC token exchange'
  name: dotCMS Dot Auth API
  phrasing_intents:
  - id: exchange
    intent: Exchange an OIDC ID token for a session-ref
    question: How do I turn an OIDC id_token into a dotCMS session for a headless app?
  - id: exchangePreflight
    intent: Preflight the token exchange endpoint for CORS
    question: Does the OIDC token exchange endpoint answer CORS preflight requests?
  - id: getDotAuthConfig
    intent: Get a site's SSO configuration
    question: What OAuth or SAML settings are stored for a site?
  - id: saveDotAuthConfig
    intent: Save a site's SSO configuration
    question: How do I configure OAuth or SAML sign-in for a specific site?
  - id: clearDotAuthConfig
    intent: Clear a site's SSO configuration
    question: How do I remove single sign-on settings from a site?
  - id: saveDotAuthHeadlessConfig
    intent: Save the headless token-exchange configuration
    question: Where do I configure headless token exchange for the whole system?
  - id: clearDotAuthHeadlessConfig
    intent: Clear the headless token-exchange configuration
    question: How do I turn off headless token exchange?
  - id: discoverDotAuthOidc
    intent: Fetch an OIDC discovery document
    question: Can dotCMS read an identity provider's openid-configuration to fill in issuer and JWKS?
  phrasing_ops: 15
  slug: dotcms-dotauth-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Backend Elasticsearch search endpoints for portlet context
  name: dotCMS Elasticsearch Content Search API
  phrasing_intents:
  - id: getLayout_4
    intent: Get the search portlet layout
    question: What does the Elasticsearch portlet layout endpoint return?
  - id: searchContentByESPost
    intent: Search content with a JSON query
    question: How do I search dotCMS content with an Elasticsearch-style JSON query?
  - id: rawSearchContentByESPost
    intent: Run a raw search query
    question: Can I get the unprocessed search engine response for a JSON query?
  phrasing_ops: 3
  slug: dotcms-elasticsearch-content-search-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Publishing environment management and configuration
  name: dotCMS Environment API
  phrasing_intents:
  - id: getEndpoints
    intent: List all push publishing endpoints
    question: Which push publishing endpoints are configured across all environments?
  - id: create
    intent: Add a push publishing endpoint
    question: How do I add a receiving server to a push publishing environment?
  - id: update
    intent: Update a push publishing endpoint
    question: How do I change the address or port of an existing push endpoint?
  - id: delete_3
    intent: Delete a push publishing endpoint
    question: How do I remove a receiving server from push publishing?
  - id: getEndpoint
    intent: Get one push publishing endpoint
    question: How do I see the settings of a single push endpoint?
  - id: getEndpointsByEnvironmentId
    intent: List endpoints in one environment
    question: Which endpoints belong to a specific push publishing environment?
  - id: loadAllEnvironments
    intent: List all push publishing environments
    question: What push publishing environments are set up?
  - id: create_1
    intent: Create a push publishing environment
    question: How do I create a new push publishing environment?
  phrasing_ops: 11
  slug: dotcms-environment-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: The Experiment API from dotCMS — 15 operation(s) for experiment.
  name: dotCMS Experiment API
  phrasing_intents:
  - id: addVariant
    intent: Add a variant to an A/B experiment
    question: How do I add another variant to an experiment I'm setting up?
  - id: archive
    intent: Archive an experiment
    question: How do I archive an experiment that's finished?
  - id: cancel
    intent: Cancel a scheduled experiment
    question: Can I cancel an experiment that is scheduled but hasn't started yet?
  - id: list
    intent: List experiments
    question: Which A/B experiments are set up in dotCMS?
  - id: create_2
    intent: Create an A/B experiment
    question: How do I set up a new A/B test on a page in dotCMS?
  - id: delete_6
    intent: Delete an experiment
    question: How do I permanently delete an experiment?
  - id: update_2
    intent: Update an experiment's settings
    question: Can I change the traffic split or goals of an existing experiment?
  - id: deleteGoal
    intent: Remove an experiment's primary goal
    question: How do I clear the primary goal of an experiment?
  phrasing_ops: 18
  slug: dotcms-experiment-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: File asset management and download operations
  name: dotCMS File Assets API
  phrasing_intents:
  - id: findResourceLink_1
    intent: Get the resource link for a file asset
    question: What is the public link to a file asset I uploaded?
  - id: getFileAssetById
    intent: Download a file asset by identifier
    question: How do I download the raw bytes of a file asset using its identifier?
  - id: getFileAssetByPath
    intent: Download a file asset by site path
    question: Can I download a file by its host and folder path, like //mysite/images/logo.png?
  - id: publishFileAsset
    intent: Upload and publish a file asset
    question: How do I upload a file and make it live immediately?
  - id: saveFileAsset
    intent: Upload a file asset as a draft
    question: Can I upload a new version of a file without changing what's live?
  phrasing_ops: 5
  slug: dotcms-file-assets-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Endpoints for managing folder structure and organization
  name: dotCMS Folders API
  phrasing_intents:
  - id: createFoldersBySiteName
    intent: Create folders by path on a site
    question: How do I create a nested folder structure on a site in one call?
  - id: deleteFoldersBySiteName
    intent: Delete folder paths on a site
    question: How do I delete several folders from a site by their paths?
  - id: findFolderById
    intent: Get a folder by ID
    question: How do I look up a folder when I only have its identifier?
  - id: findSubFoldersByPath
    intent: Find subfolders by path (deprecated)
    question: Is there an older endpoint that returns subfolders for a path I post?
  - id: loadFolderAndSubFoldersByPath
    intent: Load a folder and all its subfolders
    question: How do I get a folder along with every subfolder beneath it?
  - id: loadFolderByURI
    intent: Get a folder by site name and URI
    question: How do I find a folder from its URL path on a named site?
  - id: searchFolders
    intent: Search folders on a site
    question: Which folders on my site have a name like this?
  - id: selectFolderInFileBrowser
    intent: Select a folder in the file browser
    question: Can I set which folder is selected in my file browser session?
  phrasing_ops: 8
  slug: dotcms-folders-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Form management and processing
  name: dotCMS Forms API
  phrasing_intents:
  - id: getSuccessCallbackFunction
    intent: Get a form's success callback
    question: What JavaScript runs after a dotCMS form is submitted successfully?
  phrasing_ops: 1
  slug: dotcms-forms-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Returns the content types valid for a page based on the container/types on the layout
  name: dotCMS Get Pages Content Types API
  phrasing_intents:
  - id: getPagesContentTypes
    intent: List content types usable on a page
    question: Which content types can be added to a given page?
  phrasing_ops: 1
  slug: dotcms-getpagescontenttypes-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Health management and monitoring endpoints for administrative dashboards
  name: dotCMS Health API
  phrasing_intents:
  - id: getHealthCheck
    intent: Get the result of one health check
    question: Is the database health check passing right now?
  - id: getHealthCheckNames
    intent: List the registered health checks
    question: Which health checks are registered on my dotCMS server?
  - id: getLivenessHealth
    intent: Get detailed liveness health
    question: Is the dotCMS application alive, with details per critical component?
  - id: getOverallHealth
    intent: Get the full health report
    question: What is the overall health of my dotCMS instance across all checks?
  - id: getReadinessHealth
    intent: Get readiness health for traffic
    question: Is this dotCMS node ready to receive traffic yet?
  - id: getSystemStatus
    intent: Get a quick alive and ready summary
    question: Can I get a simple yes or no on whether dotCMS is alive and ready?
  - id: refreshHealthCheck
    intent: Force a refresh of one health check
    question: Can I rerun a single health check right now instead of waiting for the cache?
  - id: refreshHealthChecks
    intent: Force a refresh of all health checks
    question: How do I rerun every health check after a configuration change?
  phrasing_ops: 8
  slug: dotcms-health-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Language management and localization
  name: dotCMS Internationalization API
  phrasing_intents:
  - id: list_7
    intent: Get a system i18n resource bundle
    question: Where do I load the translated UI strings for a system resource in a given language?
  - id: updateLanguage
    intent: Update a language
    question: Can I change the country code on a language I already added?
  - id: deleteLanguage
    intent: Delete a language
    question: How do I remove a language I no longer publish content in?
  - id: get_8
    intent: Get a language by numeric ID
    question: Which language does a given language ID refer to?
  - id: getAllMessages
    intent: Get all message keys for a language
    question: Can I pull every translation key and message for one language?
  - id: getDefaultLanguage
    intent: Get the default language
    question: What is the default content language on this dotCMS instance?
  - id: getFromLanguageTag
    intent: Look up a language by locale tag
    question: Can I find a configured language using a tag like en-US?
  - id: saveFromLanguageTag
    intent: Add a language from a locale tag
    question: Can I add a new language just by giving its locale tag?
  phrasing_ops: 14
  slug: dotcms-internationalization-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: JavaScript execution and server-side scripting
  name: dotCMS Java Script API
  phrasing_intents:
  - id: get
    intent: Call a scripted JS endpoint's GET handler
    question: How do I call a server-side JavaScript endpoint I've set up in a dotCMS folder?
  - id: putMultipart
    intent: Send a multipart PUT to a scripted JS endpoint
    question: Can I PUT multipart form data to a custom JavaScript endpoint folder?
  - id: postMultipart
    intent: Send a multipart POST to a scripted JS endpoint
    question: How do I POST a file upload to a server-side JavaScript endpoint?
  - id: delete_1
    intent: Call a scripted JS endpoint's DELETE handler
    question: Can I trigger the DELETE logic of a custom JavaScript endpoint folder?
  - id: patchMultipart
    intent: Send a multipart PATCH to a scripted JS endpoint
    question: Can I PATCH multipart data to a server-side JavaScript endpoint folder?
  - id: get_1
    intent: Call a scripted JS endpoint's GET handler on a sub-path
    question: Can I pass an extra path segment when calling a custom JavaScript endpoint?
  - id: putMultipart_1
    intent: Send a multipart PUT to a scripted JS endpoint sub-path
    question: Can I PUT multipart data to a sub-path of a custom JavaScript endpoint?
  - id: postMultipart_1
    intent: Send a multipart POST to a scripted JS endpoint sub-path
    question: How do I POST a multipart form to a sub-path of a custom JavaScript endpoint?
  phrasing_ops: 18
  slug: dotcms-javascript-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Endpoints for managing background jobs and job queues
  name: dotCMS Job Queue API
  phrasing_intents:
  - id: getAbandonedJobs
    intent: List abandoned background jobs
    question: Which background jobs were abandoned and never finished?
  - id: getActiveJobs
    intent: List active jobs across all queues
    question: What jobs are running right now across every queue?
  - id: getActiveJobsByQueue
    intent: List active jobs in one queue
    question: Which jobs are active in a particular job queue?
  - id: cancelJobQueueJob
    intent: Cancel a background job
    question: How do I cancel a queued or running background job?
  - id: getCanceledJobs
    intent: List canceled jobs
    question: Which jobs have been canceled?
  - id: getCompletedJobs
    intent: List completed jobs
    question: Which background jobs have completed, whatever their outcome?
  - id: createJobWithFormData
    intent: Queue a job with an uploaded file
    question: How do I submit a background job that needs a file upload, like a CSV import?
  - id: createJobWithJson
    intent: Queue a job with JSON parameters
    question: How do I start a background job by posting JSON parameters to a queue?
  phrasing_ops: 14
  slug: dotcms-job-queue-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Language configuration and management
  name: dotCMS Language API
  phrasing_intents:
  - id: getI18nMessages
    intent: Get i18n messages for a locale (v1)
    question: Can I get translated UI strings for specific message keys in a given locale?
  - id: listLanguages
    intent: List all configured languages (v1)
    question: What languages are set up on my dotCMS instance, keyed by language code?
  phrasing_ops: 2
  slug: dotcms-language-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: The Layout API from dotCMS — 1 operation(s) for layout.
  name: dotCMS Layout API
  phrasing_intents:
  - id: getLayout
    intent: Get a back-end admin layout
    question: Can I load the portlet layout of a dotCMS admin screen?
  phrasing_ops: 1
  slug: dotcms-layout-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: License management and validation
  name: dotCMS License API
  phrasing_intents:
  - id: applyLicense
    intent: Apply a license key
    question: How do I activate dotCMS by pasting in license text?
  - id: delete_5
    intent: Delete a license from the pack
    question: Can I remove a license from the uploaded license pack?
  - id: freeLicense
    intent: Free a license from a server
    question: How do I release a license from a server so another node can use it?
  - id: getAll_1
    intent: List all licenses
    question: Which licenses are in the pack and which servers are using them?
  - id: pickLicense
    intent: Pick a license for this server
    question: Can I choose a specific license from the pack for this server?
  - id: putZipFile
    intent: Upload a license pack zip
    question: How do I upload a zip file of cluster licenses?
  - id: requestLicense
    intent: Generate a license request code
    question: How do I get the request code needed to obtain a license for this server?
  - id: resetLicense
    intent: Reset the server's license
    question: Can I reset this server's license back to an unlicensed state?
  phrasing_ops: 8
  slug: dotcms-license-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: System maintenance and administration operations
  name: dotCMS Maintenance API
  phrasing_intents:
  - id: deleteContentlets
    intent: Permanently bulk delete contentlets by identifier
    question: How do I permanently destroy a batch of contentlets without sending them to the trash?
  - id: deletePushedAssets
    intent: Clear all push publishing history records
    question: How can I wipe the pushed assets table so everything looks never pushed?
  - id: deleteSystemJob
    intent: Remove a Quartz scheduler job by group and name
    question: How do I remove an orphaned Quartz scheduler job that errored after an upgrade?
  - id: downloadAssets
    intent: Download a zip of the site's asset files
    question: Can I download just the assets folder from my dotCMS instance as an archive?
  - id: downloadClusterLogFile
    intent: Download a log file collected from the cluster
    question: How do I pull a log file gathered from all cluster nodes?
  - id: downloadDb
    intent: Download a database dump
    question: How do I download a full dump of the dotCMS database?
  - id: downloadLogFile
    intent: Download a single server log file
    question: How can I download one of this server's log files by its name?
  - id: downloadStarter
    intent: Download a starter site without assets
    question: How do I export a starter package that contains data but no asset files?
  phrasing_ops: 26
  slug: dotcms-maintenance-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Site navigation tree endpoints
  name: dotCMS Navigation API
  phrasing_intents:
  - id: getMenus
    intent: Get the back-end admin menus
    question: Which admin menu sections and portlets can the current user see?
  - id: getNavigationTree
    intent: Get the site navigation tree from a folder
    question: How do I build my site's menu from folders marked show on menu?
  phrasing_ops: 2
  slug: dotcms-navigation-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: User notifications and alerts management
  name: dotCMS Notifications API
  phrasing_intents:
  - id: delete_7
    intent: Delete several notifications
    question: How do I clear a batch of notifications at once?
  - id: delete_8
    intent: Delete a notification
    question: How do I dismiss one notification permanently?
  - id: getNewNotificationsCount
    intent: Count unread notifications
    question: How many new notifications do I have?
  - id: getNotifications
    intent: List notifications
    question: What notifications have I received?
  - id: markAsRead
    intent: Mark all notifications as read
    question: How do I mark my notifications as read?
  phrasing_ops: 5
  slug: dotcms-notifications-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: OSGi plugin management and dynamic deployment
  name: dotCMS OSGi Plugins API
  phrasing_intents:
  - id: getInstalledBundles
    intent: List installed OSGi bundles (legacy endpoint)
    question: Is there an older path-parameter endpoint for listing installed OSGi bundles?
  - id: processBundle
    intent: Process a bundle's exports (legacy endpoint)
    question: Can I trigger export processing for a bundle using the legacy OSGi route?
  - id: updateBundles
    intent: Upload plugin bundles (legacy endpoint)
    question: Is there a legacy multipart endpoint for uploading OSGi plugins?
  - id: deploy
    intent: Deploy an uploaded plugin JAR
    question: How do I deploy a plugin JAR that's already been uploaded?
  - id: getAvailablePlugis
    intent: List plugins available to deploy
    question: Which plugin JARs are sitting in the upload folder waiting to be deployed?
  - id: getExtraPackages
    intent: View the OSGi extra packages list
    question: Which extra Java packages does dotCMS export to OSGi plugins?
  - id: modifyExtraPackages
    intent: Change the OSGi extra packages list
    question: How do I expose an additional Java package to my OSGi plugins?
  - id: getInstalledBundles_1
    intent: List installed OSGi bundles
    question: Which plugins are installed in the OSGi framework and what state are they in?
  phrasing_ops: 15
  slug: dotcms-osgi-plugins-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Page rendering, layout management, and content operations
  name: dotCMS Page API
  phrasing_intents:
  - id: addContentToPage
    intent: Replace which content sits in a page's containers
    question: How do I set exactly which contentlets appear in each container on a page?
  - id: checkPageLanguageVersions
    intent: Check which languages a page exists in
    question: Which languages is this page already translated into?
  - id: checkPagePermission
    intent: Check a user's permission on a page
    question: Can the current user edit or publish a given page path?
  - id: copyPageContent
    intent: Copy a contentlet placed on a page
    question: Can I duplicate a single contentlet that's already placed on a page?
  - id: deepCopyPage
    intent: Deep copy a page and all its content
    question: How do I clone a page along with copies of every contentlet on it?
  - id: findAvailablePageActions
    intent: Find workflow actions available for a page
    question: What workflow actions can I take on the page at a given path?
  - id: getPageContentTree
    intent: Get a page's container-to-content structure
    question: Which contentlets are placed in which containers on this page?
  - id: getPageRenderVersions
    intent: Compare a page's live and preview versions
    question: Does my page have unpublished changes compared to the live version?
  phrasing_ops: 18
  slug: dotcms-page-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Permission management and access control
  name: dotCMS Permissions API
  phrasing_intents:
  - id: getAssetPermissions
    intent: Get permissions on an asset
    question: Which roles have access to this folder or page?
  - id: updateAssetPermissions
    intent: Replace all permissions on an asset
    question: How do I overwrite every permission on an asset?
  - id: getByContentlet
    intent: Get permissions on a contentlet
    question: Who can read, edit or publish this piece of content?
  - id: getByContentletGroupByType
    intent: Get contentlet permissions grouped by type
    question: Can I see a contentlet's roles grouped by READ, WRITE and PUBLISH?
  - id: getPermissionMetadata
    intent: List available permission levels and scopes
    question: What permission levels and scopes can I assign in dotCMS?
  - id: getPermissionsByPermissionType
    intent: Map permissions by permission type for a user
    question: Which permissionable types does a user have a given permission on?
  - id: getRolePermissions
    intent: Get a role's permissions across sites and folders
    question: Where does a role have permissions defined?
  - id: getUserPermissions
    intent: Get a user's individual permissions
    question: What can a specific user access through their own role?
  phrasing_ops: 11
  slug: dotcms-permissions-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Content personalization and persona management
  name: dotCMS Personalization API
  phrasing_intents:
  - id: personalizePageContainers
    intent: Personalize a page for a persona
    question: How do I create a persona-specific version of a page's content?
  - id: personalizePageContainers_1
    intent: Remove a persona personalization from a page
    question: Can I delete a persona's custom version of a page?
  - id: getLayout_5
    intent: Get the personas layout (legacy)
    question: Is there a legacy endpoint for the personas portlet layout?
  - id: list_11
    intent: List personas for a site
    question: Which personas are defined for a given site?
  phrasing_ops: 4
  slug: dotcms-personalization-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Content persona management and targeting
  name: dotCMS Personas API
  phrasing_intents:
  - id: list_1
    intent: List personas for the current site
    question: What personas are defined for my site?
  - id: self
    intent: Get a persona
    question: How do I look up one persona's details by its identifier?
  phrasing_ops: 2
  slug: dotcms-personas-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Portlet management and administration
  name: dotCMS Portlets API
  phrasing_intents:
  - id: getLayout_1
    intent: Get a portlet's layout (legacy)
    question: Where does the legacy portlet layout endpoint get the screen layout for a portlet?
  - id: layoutGet
    intent: Render a legacy portlet via GET
    question: Can I load a legacy portlet's content with a plain GET?
  - id: layoutPost
    intent: Submit to a legacy portlet via POST
    question: How do I post a form submission to a legacy portlet?
  - id: addContentPortletToLayout
    intent: Add a custom portlet to a layout
    question: How do I put a custom content portlet into a menu layout?
  - id: deleteCustomPortlet
    intent: Delete a custom content portlet
    question: How do I delete a custom content portlet I created?
  - id: deletePersonalPortlet
    intent: Remove a portlet from my own layout
    question: Can I remove a portlet from just my personal menu?
  - id: deletePortletForRole
    intent: Remove a portlet from a role's layout
    question: How do I take a portlet away from everyone in a particular role?
  - id: doesUserHaveAccessToPortlet
    intent: Check if I can access a portlet
    question: Does the current user have access to a given portlet?
  phrasing_ops: 12
  slug: dotcms-portlets-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Push publishing job management endpoints
  name: dotCMS Publishing API
  phrasing_intents:
  - id: get_2
    intent: Get the publishing audit for a bundle
    question: What does the publishing audit log say about a specific bundle?
  - id: getAll
    intent: List all publishing audit records
    question: Can I pull every publishing audit record at once?
  - id: deleteAssetsByIdentifiers
    intent: Remove assets from the publish queue
    question: How do I take queued assets out of the publish queue?
  - id: addAssetsToBundle
    intent: Add assets to a bundle
    question: How do I add content to a push publishing bundle?
  - id: removeAssetsFromBundle
    intent: Remove assets from an unpushed bundle
    question: Can I take items back out of a bundle before it's pushed?
  - id: getPublishingJobDetails
    intent: Get a publishing job's details
    question: Why did my publishing job fail on one endpoint?
  - id: deletePublishingJob
    intent: Delete a publishing job
    question: How do I remove one bundle from the publishing queue?
  - id: listPublishingJobs
    intent: List publishing jobs
    question: Which push publishing jobs are queued or done?
  phrasing_ops: 16
  slug: dotcms-publishing-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Content relationship management
  name: dotCMS Relationships API
  phrasing_intents:
  - id: getCardinality
    intent: List relationship cardinality options
    question: What cardinalities can a content relationship have, like one-to-many?
  - id: getOneSidedRelationships
    intent: List one-sided relationships for a content type
    question: Which relationships are defined on only one side of a content type?
  phrasing_ops: 2
  slug: dotcms-relationships-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: User role and permission management
  name: dotCMS Roles API
  phrasing_intents:
  - id: loadRoleByIdLegacy
    intent: Load full role details (legacy endpoint)
    question: How did the old admin UI load a role's full properties by id?
  - id: loadRolesByNameLegacy
    intent: Filter the role tree by name (legacy endpoint)
    question: Can I get a role tree trimmed to leaves whose name contains some text on the old API?
  - id: loadRoleChildrenLegacy
    intent: Lazy-load a role's children (legacy endpoint)
    question: How does the deprecated API return the first-level children of a role?
  - id: loadRootRoles
    intent: List the top-level roles
    question: What are the root roles in my dotCMS role hierarchy?
  - id: createRole
    intent: Create a new role
    question: How do I create a new role under an existing parent role?
  - id: addUserToRole
    intent: Grant a role to a user
    question: How do I give a user a role directly?
  - id: checkUserRoles
    intent: Check if a user holds any of given roles
    question: Does this user belong to at least one of these roles?
  - id: loadRoleByRoleId
    intent: Get a role by its id
    question: How do I look up a single role by id on the v1 API?
  phrasing_ops: 19
  slug: dotcms-roles-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Business rules and conditional logic management
  name: dotCMS Rules Engine API
  phrasing_intents:
  - id: getLayout_3
    intent: Load the rules engine portlet layout
    question: Where does the dotCMS admin UI get the layout for the rules engine screen?
  - id: list_2
    intent: List the rules defined on a site
    question: Which personalization rules are configured on one of my sites?
  - id: add
    intent: Create a new rule on a site
    question: Can I create a rule that fires on every page request for a site?
  - id: self_1
    intent: Get a single rule by ID
    question: How can I look up one specific rule and its settings on a site?
  - id: update_3
    intent: Update an existing rule
    question: Can I rename or re-prioritize a rule that already exists?
  - id: remove
    intent: Delete a rule from a site
    question: How do I permanently remove a rule from the rules engine?
  - id: add_1
    intent: Add an action to a rule
    question: How do I attach an actionlet to a rule so it does something when it fires?
  - id: self_2
    intent: Get a rule action by ID
    question: Which actionlet and parameters does a given rule action use?
  phrasing_ops: 26
  slug: dotcms-rules-engine-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: SAML SSO authentication and integration
  name: dotCMS SAML Authentication API
  phrasing_intents:
  - id: doLogin
    intent: Start a SAML single sign-on login
    question: How do I send a user to the identity provider's login screen for SAML SSO?
  - id: processLogin
    intent: Handle the SAML login callback
    question: Where does the identity provider post the SAML assertion after a user signs in?
  - id: logoutGet
    intent: Log out of SAML via GET
    question: How do I start a SAML logout from a browser link?
  - id: logoutPost
    intent: Handle a SAML logout callback via POST
    question: Where does the identity provider POST its logout callback?
  - id: metadata
    intent: Get the SAML service provider metadata
    question: Where do I get the SP metadata XML to register dotCMS with my identity provider?
  phrasing_ops: 5
  slug: dotcms-saml-authentication-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Elasticsearch index management and operations
  name: dotCMS Search Index API
  phrasing_intents:
  - id: activateIndex
    intent: Activate a search index
    question: How do I make a newly built index the live one content search uses?
  - id: clearIndex
    intent: Clear all documents from an index
    question: Can I empty an index of all its documents without deleting the index itself?
  - id: closeIndex
    intent: Close a search index
    question: Can I close an index I'm not using right now?
  - id: createIndex
    intent: Create a new search index
    question: How do I create a fresh Elasticsearch index for content?
  - id: deactivateIndex
    intent: Deactivate a search index
    question: Can I stop an index from being the active one without deleting it?
  - id: downloadRemainingRecordsAsCsv
    intent: Download records that failed to index
    question: Which content items failed during the last reindex?
  - id: deleteFailedRecords
    intent: Clear the failed reindex records
    question: How do I clear out the list of records that failed to reindex?
  - id: modIndex
    intent: Run an action on a named index
    question: Can I open, close or activate an index by name with a single endpoint?
  phrasing_ops: 19
  slug: dotcms-search-index-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Site management, lifecycle, and configuration endpoints
  name: dotCMS Site API
  phrasing_intents:
  - id: archiveSite
    intent: Archive a site
    question: How do I archive a site I no longer use in dotCMS?
  - id: copySite
    intent: Create a new site by copying another
    question: Can I clone an existing site with its templates, containers and folders?
  - id: getSites
    intent: List sites I can access
    question: Which sites do I have access to?
  - id: updateSite
    intent: Update a site's properties
    question: How do I change an existing site's aliases or SEO keywords?
  - id: createSite
    intent: Create a new site
    question: How do I add a new site with its own hostname?
  - id: getCurrentSite
    intent: Get the site selected in my session
    question: Which site am I currently working in?
  - id: getDefaultSite
    intent: Get the system default site
    question: Which site is marked as the default in dotCMS?
  - id: getSiteById
    intent: Get a site's details
    question: How do I get the full details of a site from its identifier?
  phrasing_ops: 20
  slug: dotcms-site-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: System-level operations and Redis management
  name: dotCMS System API
  phrasing_intents:
  - id: getShutdownStatus
    intent: Check request-draining shutdown status
    question: Is the server currently draining requests before shutdown?
  - id: longRunningRequest
    intent: Start a long-running test request
    question: Can I simulate a slow request to test graceful shutdown draining?
  - id: simulateActiveRequests
    intent: Simulate concurrent active requests
    question: Can I simulate many in-flight requests to test shutdown draining?
  - id: get_5
    intent: Read a Redis key
    question: How do I read a value stored in dotCMS's Redis by key?
  - id: delete_10
    intent: Delete a Redis key
    question: Can I remove a plain value key from Redis through the API?
  - id: getHash
    intent: Read a Redis hash
    question: How do I read all fields of a Redis hash?
  - id: deleteHash
    intent: Delete a Redis hash
    question: Can I delete an entire Redis hash through the API?
  - id: echo
    intent: Echo a message through Redis
    question: Can I send a test message through Redis and get it back?
  phrasing_ops: 13
  slug: dotcms-system-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: System configuration and company settings
  name: dotCMS System Configuration API
  phrasing_intents:
  - id: deleteEndpoint
    intent: Delete a push publishing endpoint (legacy)
    question: How do I remove a push publishing endpoint through the older config API?
  - id: deleteEnvironment
    intent: Delete a publishing environment (legacy)
    question: Can I delete a whole push publishing environment?
  - id: regenerateKey
    intent: Regenerate the company key (legacy endpoint)
    question: Is there an older config endpoint for rotating the company security key?
  - id: saveCompanyAuthTypeInfo
    intent: Set the login auth type (legacy)
    question: Can the older config API switch logins between email address and user ID?
  - id: saveCompanyBasicInfo
    intent: Save company basic info (legacy)
    question: Can I update the company's street address and city through the older config API?
  - id: saveCompanyLocaleInfo
    intent: Save company language and time zone (legacy)
    question: Can the legacy config API change the system's default time zone?
  - id: saveCompanyLogo
    intent: Upload the company logo (legacy)
    question: How do I upload a new company logo file?
  - id: getCompanyConfig
    intent: Get company branding and settings
    question: What branding colors and logos is my dotCMS instance currently using?
  phrasing_ops: 23
  slug: dotcms-system-configuration-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: System logging configuration and management
  name: dotCMS System Logging API
  phrasing_intents:
  - id: getLoggers
    intent: List loggers and their levels
    question: Which loggers are configured and at what level?
  - id: changeLoggerLevel
    intent: Change a logger's level
    question: How do I turn on debug logging for one class without a restart?
  - id: getLogger
    intent: Get one logger's level
    question: What level is a particular logger set to?
  phrasing_ops: 3
  slug: dotcms-system-logging-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: System monitoring and health checks
  name: dotCMS System Monitoring API
  phrasing_intents:
  - id: heavyCheck
    intent: Run a full system health check
    question: Is my dotCMS instance passing its deeper health check?
  - id: ready
    intent: Check if the server is ready
    question: Is the server ready to take traffic yet?
  phrasing_ops: 2
  slug: dotcms-system-monitoring-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Storage providers and data replication management
  name: dotCMS System Storage API
  phrasing_intents:
  - id: hello
    intent: Ping the storage service
    question: Is the dotCMS storage API responding?
  - id: replicateStorages
    intent: Replicate one storage to another
    question: How do I copy binaries from one storage provider to another in the chain?
  phrasing_ops: 2
  slug: dotcms-system-storage-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Legacy tag management endpoints (deprecated - use v2 TagResource instead)
  name: dotCMS Tag (v1) API
  phrasing_intents:
  - id: getTagsV1
    intent: List or search tags (v1, deprecated)
    question: How do I list all tags or search them by name on the old v1 tags API?
  - id: updateTagV1
    intent: Rename a tag or change its site (v1)
    question: How do I rename an existing tag using the v1 tags API?
  - id: addTagV1
    intent: Create tags (v1, deprecated)
    question: How do I create a new tag with the v1 tags API?
  - id: deleteTagV1
    intent: Delete a tag by id (v1)
    question: How do I delete a tag through the deprecated v1 API?
  - id: findTagsByInodeV1
    intent: Get the tags attached to an inode (v1)
    question: Which tags are attached to a particular content version (inode)?
  - id: deleteTagInodesByInodeV1
    intent: Unlink all tags from an inode (v1)
    question: How do I strip every tag off a content version at once?
  - id: getTagsByNameOrIdV1
    intent: Look up tags by exact name or id (v1)
    question: How do I fetch a tag when I know its exact name or UUID?
  - id: getTagsByUserIdV1
    intent: List tags owned by a user (v1)
    question: Which tags are owned by a specific user?
  phrasing_ops: 10
  slug: dotcms-tag-v1-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Content tagging and labeling
  name: dotCMS Tags API
  phrasing_intents:
  - id: listTags
    intent: List or search tags
    question: Which tags contain the word market?
  - id: createTags
    intent: Create one or more tags
    question: How do I create several tags in a single request?
  - id: bulkDeleteTags
    intent: Delete several tags at once
    question: Can I delete a batch of tags by their IDs in one call?
  - id: deleteTag
    intent: Delete a single tag
    question: How do I delete one tag by its ID?
  - id: getTagsByInode
    intent: Get the tags on a content item
    question: What tags are attached to this piece of content?
  - id: deleteTagInodeAssociations
    intent: Remove all tags from a content item
    question: Can I strip every tag off a piece of content without deleting the tags?
  - id: downloadTagImportTemplate
    intent: Download the CSV template for tag imports
    question: What format does a tag import CSV need to be in?
  - id: exportTags
    intent: Export tags to CSV or JSON
    question: Can I export all my tags to a CSV file?
  phrasing_ops: 13
  slug: dotcms-tags-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Server log file monitoring and real-time viewing
  name: dotCMS Tail Log API
  phrasing_intents:
  - id: getLogs
    intent: Tail a server log file
    question: How do I tail a dotCMS log file from the API?
  - id: listLogFiles
    intent: List available log files
    question: Which log files can I tail?
  phrasing_ops: 2
  slug: dotcms-taillog-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Template CRUD, publish, archive, and layout management endpoints
  name: dotCMS Template API
  phrasing_intents:
  - id: archiveTemplates
    intent: Archive templates in bulk
    question: How do I archive several page templates at once?
  - id: copyTemplate
    intent: Copy a template
    question: How do I duplicate an existing page template?
  - id: listTemplates
    intent: List templates
    question: Which page templates can I use on my site?
  - id: updateTemplate
    intent: Update an existing template
    question: How do I change the layout or body of a template that already exists?
  - id: createTemplate
    intent: Create a new template
    question: How do I create a new page template in dotCMS?
  - id: deleteTemplates
    intent: Delete templates in bulk
    question: Can I permanently delete templates that pages no longer use?
  - id: fetchTemplateImage
    intent: Get a template's thumbnail image info
    question: Which image is attached to a template as its preview?
  - id: getLiveTemplateById
    intent: Get the live version of a template
    question: What does the published version of a template contain?
  phrasing_ops: 14
  slug: dotcms-template-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Template design and management
  name: dotCMS Templates API
  phrasing_intents:
  - id: get_6
    intent: Run a scripted endpoint's GET Velocity file
    question: How do I call the get.vtl script in one of my scripting API folders?
  - id: putMultipart_2
    intent: Send a multipart PUT to a scripted endpoint
    question: How do I PUT files as multipart form data to a Velocity endpoint folder?
  - id: postMultipart_2
    intent: Send a multipart POST to a scripted endpoint
    question: How do I POST a form with files to one of my Velocity scripting folders?
  - id: delete_11
    intent: Run a scripted endpoint's DELETE Velocity file
    question: How do I trigger the delete.vtl script of a custom Velocity endpoint?
  - id: patchMultipart_2
    intent: Send a multipart PATCH to a scripted endpoint
    question: How do I PATCH a scripting endpoint folder with multipart data?
  - id: get_7
    intent: Run a scripted GET with an extra path segment
    question: Can my Velocity GET endpoint read an id from a sub-path after the folder?
  - id: putMultipart_3
    intent: Multipart PUT to a scripted endpoint sub-path
    question: How do I PUT multipart data to a specific item path under a Velocity endpoint?
  - id: postMultipart_3
    intent: Multipart POST to a scripted endpoint sub-path
    question: How do I POST files to a sub-path of a custom Velocity endpoint?
  phrasing_ops: 18
  slug: dotcms-templates-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Temporary file upload and management for content creation
  name: dotCMS Temporary Files API
  phrasing_intents:
  - id: createTempFileFromUrl
    intent: Create a temporary file from a URL
    question: Can I pull a file from a remote URL into dotCMS to attach to content?
  - id: uploadTempFileMultipart
    intent: Upload temporary files
    question: How do I upload files from my computer to use when creating content?
  phrasing_ops: 2
  slug: dotcms-temporary-files-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: The TestResource API from dotCMS — 2 operation(s) for testresource.
  name: dotCMS Test Resource API
  phrasing_intents:
  - id: getDocumentCount
    intent: Call the test GET resource
    question: Is there a test GET endpoint I can hit to check the REST layer works?
  - id: saveTest
    intent: Call the test POST resource
    question: Is there a test POST endpoint for trying out form submissions?
  phrasing_ops: 2
  slug: dotcms-testresource-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Theme browsing and management
  name: dotCMS Theme API
  phrasing_intents:
  - id: findThemeById
    intent: Get a theme by ID
    question: What are the details of the theme a template is using?
  - id: findThemes
    intent: List a site's themes
    question: Which themes are available on one of my sites?
  phrasing_ops: 2
  slug: dotcms-theme-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Provides business intelligence metrics for dashboard usage
  name: dotCMS Usage API
  phrasing_intents:
  - id: getSummary
    intent: Get the usage dashboard summary
    question: How much content, how many sites and users does my dotCMS instance have?
  phrasing_ops: 1
  slug: dotcms-usage-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: User account management and administration
  name: dotCMS Users API
  phrasing_intents:
  - id: getLoggedInUserLegacy
    intent: Get the logged-in user (deprecated endpoint)
    question: Is there an older endpoint that returns the logged-in user's email and role ID?
  - id: activateUser
    intent: Activate a user account
    question: How do I re-enable a user who was deactivated?
  - id: updateUser
    intent: Update another user's account
    question: Can an admin change another user's name, email and roles in one request?
  - id: createUser
    intent: Create a new user
    question: How do I add a new editor to dotCMS with a password and roles?
  - id: deactivateUser
    intent: Deactivate a user account
    question: Can I block a user from logging in without deleting their account?
  - id: findUser
    intent: Look up a user by ID
    question: What details are stored for a specific user?
  - id: deleteUser
    intent: Delete a user and reassign their content
    question: When I delete a user, what happens to the content they own?
  - id: filterUsers
    intent: Search and filter users
    question: How can I find all users who have a particular role?
  phrasing_ops: 13
  slug: dotcms-users-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Endpoints for managing content variants
  name: dotCMS Variants API
  phrasing_intents:
  - id: addVariant_1
    intent: Create a content variant
    question: How do I create a content variant for A/B testing?
  - id: promoteVariant_1
    intent: Promote a variant to default
    question: How do I make a winning variant the live default content?
  - id: bringBack
    intent: Restore an older version
    question: How do I roll content back to a previous version?
  - id: deleteVersion
    intent: Delete a specific version
    question: How do I delete one old version from an item's history?
  - id: findVersionable
    intent: Look up a version by inode or identifier
    question: How do I look up a versioned item by inode or identifier?
  phrasing_ops: 5
  slug: dotcms-variants-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Web asset management and operations
  name: dotCMS Web Assets API
  phrasing_intents:
  - id: archiveAsset
    intent: Archive a file asset
    question: How do I make a file inactive without deleting it?
  - id: updateFolder
    intent: Update or rename a folder
    question: How do I rename an existing folder by its path?
  - id: createFolder
    intent: Create a folder at a path
    question: How do I create a new folder at a specific site path?
  - id: deleteAsset
    intent: Permanently delete a file asset
    question: How do I permanently delete a file by its path?
  - id: deleteFolder
    intent: Permanently delete a folder and its contents
    question: How do I delete a folder along with everything inside it?
  - id: download
    intent: Download a file asset
    question: How do I download a file's binary content by its path?
  - id: saveUpdateAsset
    intent: Upload or replace a file asset
    question: How do I upload a new file to a specific path?
  - id: getAssetsInfo
    intent: Get a file or folder's metadata by path
    question: What metadata does a file or folder at a path have?
  phrasing_ops: 8
  slug: dotcms-web-assets-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Widget development and rendering
  name: dotCMS Widgets API
  phrasing_intents:
  - id: getWidget
    intent: Render a widget
    question: How do I fetch the rendered output of a widget?
  phrasing_ops: 1
  slug: dotcms-widgets-api
- baseURL: https://demo.dotcms.com/api
  baseurl_source: declared
  description: Endpoints that perform operations related to workflows.
  name: dotCMS Workflow API
  phrasing_intents:
  - id: reportIssue
    intent: Report a UI bug to the upstream issue tracker
    question: Can I file a bug about the dotCMS admin UI straight from my instance?
  - id: addSeparatorAction
    intent: Add a separator to a workflow step's action list
    question: Can I insert a visual separator between workflow actions in a step?
  - id: postAddWorkflowStep
    intent: Add a new step to a workflow scheme
    question: How do I add a new stage like Legal Review to an existing workflow?
  - id: postCopyScheme
    intent: Duplicate a workflow scheme
    question: Can I clone an existing workflow scheme to use as a starting point?
  - id: getWorkflowActionByActionId
    intent: Get a workflow action by its ID
    question: How can I see the full configuration of a single workflow action?
  - id: putSaveActionsByWorkflowActionForm
    intent: Update an existing workflow action
    question: Can I rename a workflow action or change which step it moves content to?
  - id: deleteWorkflowActionByActionId
    intent: Delete a workflow action from every step
    question: How do I remove a workflow action completely, from all steps it appears in?
  - id: getWorkflowActionByStepActionId
    intent: Check whether an action belongs to a step
    question: Can I confirm a specific workflow action is attached to a particular step?
  phrasing_ops: 57
  slug: dotcms-workflow-api
artifact_total: 87
asyncapis:
- description: ''
  name: Dotcms Event Surface
  slug: dotcms-event-surface
common:
- group: commercial
  href: https://artifacts.apis.io/dotcms/finops/dotcms-finops.yml
  title: ''
  type: FinOps
  url: finops/dotcms-finops.yml
- group: other
  href: https://artifacts.apis.io/dotcms/capabilities/dotcms-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dotcms-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/dotcms/overlays/dotcms-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dotcms-rest-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.dotcms.com/
- group: auth
  href: https://artifacts.apis.io/dotcms/security/dotcms-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dotcms-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/dotcms/agentic-access/dotcms-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dotcms-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/dotcms/security/dotcms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dotcms-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/dotcms/authentication/dotcms-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dotcms-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dotCMS
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dotcms
- group: agent
  title: ''
  type: LlmsText
  url: https://dev.dotcms.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.dotcms.com/blog
- group: build
  href: https://artifacts.apis.io/dotcms/packages/dotcms-packages.yml
  title: ''
  type: Packages
  url: packages/dotcms-packages.yml
- group: build
  href: https://artifacts.apis.io/dotcms/packages/dotcms-packages.yml
  title: ''
  type: SDKs
  url: packages/dotcms-packages.yml
- group: build
  href: https://artifacts.apis.io/dotcms/cli/dotcms-cli.yml
  title: ''
  type: CLI
  url: cli/dotcms-cli.yml
- group: design
  href: https://artifacts.apis.io/dotcms/components/dotcms-components.yml
  title: ''
  type: Components
  url: components/dotcms-components.yml
- group: agent
  href: https://artifacts.apis.io/dotcms/well-known/dotcms-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dotcms-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://www.dotcms.com/.well-known/api-catalog
- group: auth
  href: https://artifacts.apis.io/dotcms/well-known/dotcms-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dotcms-security.txt
- group: agent
  href: https://artifacts.apis.io/dotcms/mcp/dotcms-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dotcms-mcp.yml
- group: build
  href: https://artifacts.apis.io/dotcms/mcp/dotcms-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dotcms-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dotcms/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/dotcms/llms/dotcms-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dotcms-llms.txt
- group: design
  href: https://artifacts.apis.io/dotcms/conformance/dotcms-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dotcms-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dotcms.com/product/security-compliance
- group: auth
  href: https://artifacts.apis.io/dotcms/security/dotcms-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dotcms-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://dev.dotcms.com/docs/manage/access-and-security/security-and-privacy/responsible-disclosure-policy
- group: design
  href: https://artifacts.apis.io/dotcms/lifecycle/dotcms-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dotcms-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://dev.dotcms.com/docs/reference/releases/product-versions/release-support-lifecycle
- group: operate
  href: https://artifacts.apis.io/dotcms/changelog/dotcms-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dotcms-changelog.yml
- group: start
  href: https://artifacts.apis.io/dotcms/sandbox/dotcms-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/dotcms-sandbox.yml
- group: design
  href: https://artifacts.apis.io/dotcms/asyncapi/dotcms-event-surface.yml
  title: ''
  type: Webhooks
  url: asyncapi/dotcms-event-surface.yml
- group: commercial
  href: https://artifacts.apis.io/dotcms/plans/dotcms-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dotcms-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dotcms/rate-limits/dotcms-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dotcms-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.dotcms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.dotcms.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.dotcms.com/docs/build/apis/rest-apis/api-playground
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.dotcms.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://community.dotcms.com/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.dotcms.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dotcms.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dotcms.com/bsl
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dev.dotcms.com/docs/manage/access-and-security/security-and-privacy/privacy-policy
created: '2025-01-08'
description: 'dotCMS is a Java-based visual headless content management system aimed at compliance-led enterprises, deployable as SaaS (dotCMS Cloud), on premise, or as a managed service. It covers content modelling, authoring, workflow, multi-site management, personalization, experiments and content analytics, and pairs headless delivery with a Universal Visual Editor so authors can edit content in place inside a React, Angular or Next.js front end. Every dotCMS instance serves its own first-party OpenAPI 3.0.1 at /api/openapi.json — 592 paths and 754 operations across 71 tags, covering content, content types, workflow, publishing, sites, roles, permissions and dotAI — alongside a GraphQL endpoint at /api/v1/graphql. dotCMS also ships an early agent surface: a first-party MCP server, two published Agent Skills, an RFC 9727 API catalog and markdown content negotiation. It is certified to ISO/IEC 27001, ISO/IEC 42001 (AI management), SOC 2 Type II and TX-RAMP Level II.'
finops:
- has_sources: true
  method: derived
  name: Dotcms Finops
  primary_unit: ''
  service_category: ''
  slug: dotcms-finops
  template: true
graphqls:
- description: The dotCMS GraphQL API provides a single endpoint for querying content across all content types using a self-documenting schema. It supports Lucene-style query strings, pagination, sorting, and conten
  name: dotCMS GraphQL API
  slug: dotcms-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dotcms.png
layout: provider
mcp_servers:
- description: dotCMS ships a first-party MCP server. It is distributed as an npm package run over stdio — there is no hosted endpoint an agent can POST to — and its source lives inside the open-source dotCMS/core m
  name: dotCMS MCP Server
  slug: dotcms
modified: '2026-09-06'
name: dotCMS
nav: Providers
network: true
overview: 'dotCMS publishes 73 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accessibility Agent API, Accessibility Checker API, Administration API, and 70 more. Tagged areas include CMS, Content, Content Management, Headless CMS, and Digital Experience.


  The dotCMS catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  dotCMS''s developer surface includes authentication, engineering blog, CLI, changelog, sandbox, documentation, API reference, and 36 more developer resources.'
plans:
- name: Dotcms Plans Pricing
  plan_count: 4
  slug: dotcms-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Dotcms Rate Limits
  slug: dotcms-rate-limits
rules:
- authorship: generated
  effective_rule_count: 84
  extends:
  - spectral:oas
  name: dotCMS API Rules
  rule_count: 43
  severity_counts:
    error: 24
    hint: 0
    info: 2
    warn: 17
  slug: dotcms-rules
score:
  band: exemplar
  composite: 73.4
  coverage:
    artifact_dirs: 34
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 78.9
    contract_governance: 31.8
    contract_quality: 49.9
    developer_ergonomics: 85.7
    discoverability: 81.7
    operational_transparency: 50.0
  previous_composite: 72.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 10.0
      derived: 0
      marker_coverage: 90.0
      total: 80
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 72.2
screenshot: https://apis.io/screenshots/dotcms/dotcms-2026-06-20T180201.png
security:
- kind: authentication
  name: Dotcms Authentication
  slug: dotcms-authentication
  summary_line: http/apiKey-as-bearer/session · 5 schemes
- kind: domain-security
  name: Dotcms Domain Security
  slug: dotcms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dotcms Vulnerability Disclosure
  slug: dotcms-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Dotcms Trust Center
  slug: dotcms-trust-center
  summary_line: ISO/IEC 27001:2022, ISO/IEC 42001:2023, SOC 2 Type II, TX-RAMP Level II, CSA CAIQ
skill_count: 2
skills:
- name: dotcms-best-practices
  slug: dotcms-best-practices
- name: dotcms-create-sites
  slug: dotcms-create-sites
slug: dotcms
tags:
- CMS
- Content
- Content Management
- Headless CMS
- Digital Experience
- Content Delivery
- Workflows
- GraphQL
- MCP
- Java
website: https://www.dotcms.com/
---
