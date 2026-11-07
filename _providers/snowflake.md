---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
  band: agent-native
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
    event_surface_described: true
    idempotency: documented
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 276
  human_in_the_loop: 14
  name: Snowflake Agentic Access
  operation_count: 408
  slug: snowflake-agentic-access
  summary_line: 408 operations · 276 acting · 14 human-in-the-loop
api_count: 84
apis:
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The Snowflake Artifact Repository API is a REST API that you can use to access, update, and perform certain actions on Artifact Repository resources in a Snowflake database.
  name: Snowflake Artifact Repository API
  phrasing_intents:
  - id: listArtifactRepositories
    intent: List artifact repositories in a schema
    question: Which artifact repositories are defined in this schema?
  - id: createArtifactRepository
    intent: Create an artifact repository
    question: How do I register a package repository so functions can install packages from it?
  - id: fetchArtifactRepository
    intent: Get an artifact repository
    question: What type and API integration does a specific artifact repository use?
  - id: deleteArtifactRepository
    intent: Delete an artifact repository
    question: How do I remove an artifact repository?
  - id: createOrAlterArtifactRepository
    intent: Create or update an artifact repository
    question: Can I change the API integration an existing artifact repository uses?
  - id: renameArtifactRepository
    intent: Rename or move an artifact repository
    question: How do I rename an artifact repository?
  phrasing_ops: 6
  slug: snowflake-artifact-repository-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The Snowflake Cortex Embed API is a REST API that performs LLM embedding for input text, similar to the Snowflake Cortex EMBED_TEXT functions.
  name: Cortex Embed API
  phrasing_intents:
  - id: embed
    intent: Generate text embeddings
    question: How do I turn text into vector embeddings with Snowflake Cortex?
  phrasing_ops: 1
  slug: cortex-embed-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The Snowflake Network Rule API is a REST API that you can use to access, update, and perform certain actions on Network Rule resources in a Snowflake database.
  name: Snowflake Network Rule API
  phrasing_intents:
  - id: listNetworkRules
    intent: List network rules in a schema
    question: Which network rules are defined in this schema?
  - id: createNetworkRule
    intent: Create a network rule
    question: How do I group a set of IP addresses or hosts into a network rule?
  - id: fetchNetworkRule
    intent: Describe a network rule
    question: What values, type and mode does this network rule contain?
  - id: deleteNetworkRule
    intent: Delete a network rule
    question: How do I drop a network rule?
  phrasing_ops: 4
  slug: snowflake-network-rule-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The Snowflake Password Policy API is a REST API that you can use to access, update, and perform certain actions on Password Policy resources in a Snowflake database.
  name: Snowflake Password Policy API
  phrasing_intents:
  - id: listPasswordPolicies
    intent: List password policies in a schema
    question: Which password policies are defined in this schema?
  - id: createPasswordPolicy
    intent: Create a password policy
    question: How do I require a minimum password length and special characters for users?
  - id: fetchPasswordPolicy
    intent: Describe a password policy
    question: What length, complexity and lockout rules does this password policy enforce?
  - id: deletePasswordPolicy
    intent: Delete a password policy
    question: How do I drop a password policy?
  - id: renamePasswordPolicy
    intent: Rename or move a password policy
    question: How do I rename a password policy?
  - id: setTags
    intent: Set tags on a password policy
    question: How do I tag a password policy?
  - id: unsetTags
    intent: Remove tags from a password policy
    question: Can I remove tags from a password policy?
  - id: getTags
    intent: Get the tags assigned to a password policy
    question: Which tags are assigned to this password policy?
  phrasing_ops: 8
  slug: snowflake-password-policy-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The Snowflake Secret API is a REST API that you can use to access, update, and perform certain actions on Secret resources in a Snowflake database.
  name: Snowflake Secret API
  phrasing_intents:
  - id: listSecrets
    intent: List secrets in a schema
    question: Which secret objects are stored in this schema?
  - id: createSecret
    intent: Create a secret
    question: How do I store a credential as a secret object for integrations to use?
  - id: fetchSecret
    intent: Get the details of a secret
    question: What type and owner does a particular secret have?
  - id: deleteSecret
    intent: Delete a secret
    question: How do I delete a secret that's no longer used?
  phrasing_ops: 4
  slug: snowflake-secret-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The Snowflake Sequence API is a REST API that you can use to access, update, and perform certain actions on Sequence resources in a Snowflake database.
  name: Snowflake Sequence API
  phrasing_intents:
  - id: listSequences
    intent: List sequences in a schema
    question: Which sequences are defined in this schema?
  - id: createSequence
    intent: Create a sequence
    question: How do I create a sequence that starts at a specific number?
  - id: fetchSequence
    intent: Get the details of a sequence
    question: What start value and increment does a particular sequence use?
  - id: deleteSequence
    intent: Drop a sequence
    question: How do I drop a sequence I no longer need?
  - id: cloneSequence
    intent: Clone a sequence
    question: Can I copy an existing sequence into another schema?
  - id: renameSequence
    intent: Rename or move a sequence
    question: Can I rename a sequence without recreating it?
  phrasing_ops: 6
  slug: snowflake-sequence-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The Snowflake Spark Connect API is a REST API that enables execution of Spark workloads on Snowflake infrastructure through REST endpoints.
  name: Snowflake Spark Connect API
  phrasing_intents:
  - id: executePlan
    intent: Execute a Spark Connect query plan
    question: How do I run a Spark DataFrame plan against Snowflake through Spark Connect?
  - id: analyzePlan
    intent: Analyze a Spark query plan for metadata
    question: Can I get the schema of a Spark query without running it?
  - id: config
    intent: Get or update Spark session configuration
    question: How do I read or change Spark configuration values for my Spark Connect session?
  - id: addArtifacts
    intent: Upload artifacts to a Spark session
    question: How do I add JARs or Python files to a Spark Connect session?
  - id: artifactStatus
    intent: Check status of session artifacts
    question: Have the artifacts I uploaded to the Spark session already landed?
  - id: interrupt
    intent: Interrupt running Spark executions
    question: How do I stop a Spark Connect job that is still running?
  - id: reattachExecute
    intent: Reattach to a Spark execution
    question: My Spark result stream dropped before ResultComplete; how do I resume it?
  - id: releaseExecute
    intent: Release a reattachable Spark execution
    question: How do I free server resources held by a reattachable Spark execution?
  phrasing_ops: 10
  slug: snowflake-spark-connect-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The Snowflake Streamlit API is a REST API that you can use to access, update, and perform certain actions on Streamlit application resources in a Snowflake database.
  name: Snowflake Streamlit API
  phrasing_intents:
  - id: listStreamlits
    intent: List Streamlit apps in a schema
    question: Which Streamlit apps exist in this Snowflake schema?
  - id: createStreamlit
    intent: Create or replace a Streamlit app
    question: How do I deploy a new Streamlit app inside a Snowflake schema?
  - id: fetchStreamlit
    intent: Get details of a Streamlit app
    question: What version and configuration is a particular Streamlit app running?
  - id: deleteStreamlit
    intent: Delete a Streamlit app
    question: How do I remove a Streamlit app from Snowflake?
  - id: undropStreamlit
    intent: Restore a deleted Streamlit app
    question: Can I bring back a Streamlit app I deleted by accident?
  - id: renameStreamlit
    intent: Rename or move a Streamlit app
    question: How do I give a Streamlit app a new name?
  - id: addLiveVersionStreamlit
    intent: Add a live version to a Streamlit app
    question: How do I make a specific version of a Streamlit the live one users see?
  - id: commitStreamlit
    intent: Commit a Streamlit's live version to Git
    question: How do I commit the live version of a Git-connected Streamlit?
  phrasing_ops: 16
  slug: snowflake-streamlit-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The Snowflake Tag API is a REST API that you can use to access, update, and perform certain actions on Tag resources in a Snowflake database.
  name: Snowflake Tag API
  phrasing_intents:
  - id: listTags
    intent: List tag definitions in a schema
    question: Which governance tags are defined in this schema?
  - id: createTag
    intent: Create a tag
    question: How do I create a tag that only accepts a fixed list of values?
  - id: fetchTag
    intent: Get the definition of a tag
    question: What allowed values and propagation setting does a particular tag have?
  - id: deleteTag
    intent: Drop a tag
    question: How do I drop a tag we no longer use?
  - id: createOrAlterTag
    intent: Create or update a tag definition
    question: Can I change an existing tag's allowed values by resending its definition?
  - id: undropTag
    intent: Restore a dropped tag
    question: Can I bring back a tag I dropped by mistake?
  - id: renameTag
    intent: Rename or move a tag
    question: Can I rename a tag without recreating it?
  phrasing_ops: 7
  slug: snowflake-tag-api
- description: The Snowflake Cortex Agents API is a REST API that you can use to create, manage, and interact with Cortex Agent objects in a Snowflake account.
  name: Cortex Agents API
  slug: cortex-agents-api
- description: The Snowpipe REST API provides REST endpoints for defining the list of files to ingest and fetching reports of the load history for continuous data loading into Snowflake.
  name: Snowpipe REST API
  slug: snowpipe-rest-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The account API from Snowflake — 3 operation(s) for account.
  name: Snowflake Account API
  phrasing_intents:
  - id: listAccounts
    intent: List accounts in the organization
    question: Which Snowflake accounts exist in my organization?
  - id: createAccount
    intent: Create an account in the organization
    question: How do I create a new account in my organization with an admin user?
  - id: deleteAccount
    intent: Drop an account
    question: How do I drop an account from my organization?
  - id: UndropAccount
    intent: Restore a dropped account
    question: Can I recover an account I dropped while it's still in its grace period?
  phrasing_ops: 4
  slug: snowflake-account-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The alert API from Snowflake — 4 operation(s) for alert.
  name: Snowflake Alert API
  phrasing_intents:
  - id: listAlerts
    intent: List alerts in a schema
    question: Which alerts are defined in this schema?
  - id: createAlert
    intent: Create an alert
    question: How do I get notified when a query condition becomes true on a schedule?
  - id: fetchAlert
    intent: Describe a single alert
    question: What condition, schedule and action does this alert use?
  - id: deleteAlert
    intent: Delete an alert
    question: How do I drop an alert I no longer need?
  - id: cloneAlert
    intent: Clone an alert into a schema
    question: Can I copy an existing alert into another database and schema?
  - id: executeAlert
    intent: Run an alert now
    question: Can I evaluate an alert immediately instead of waiting for its schedule?
  - id: setTags
    intent: Set tags on an alert
    question: How do I tag an alert?
  - id: unsetTags
    intent: Remove tags from an alert
    question: Can I remove tags from an alert?
  phrasing_ops: 9
  slug: snowflake-alert-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The api-integration API from Snowflake — 2 operation(s) for api-integration.
  name: Snowflake API Integration API
  phrasing_intents:
  - id: listAPIIntegrations
    intent: List API integrations
    question: Which API integrations are configured in my Snowflake account?
  - id: createAPIIntegration
    intent: Create an API integration
    question: How do I set up an API integration so Snowflake can call an external endpoint?
  - id: fetchAPIIntegration
    intent: Get an API integration
    question: What allowed prefixes and hook does a given API integration use?
  - id: createOrAlterAPIIntegration
    intent: Create or update an API integration
    question: Can I change the allowed prefixes on an existing API integration?
  - id: deleteAPIIntegration
    intent: Delete an API integration
    question: How do I remove an API integration I no longer use?
  - id: setTags
    intent: Set tags on an API integration
    question: How do I attach tags to an API integration?
  - id: unsetTags
    intent: Remove tags from an API integration
    question: How can I remove a tag from an API integration?
  - id: getTags
    intent: Get tag assignments for an API integration
    question: Which tags are assigned to an API integration?
  phrasing_ops: 8
  slug: snowflake-api-integration-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The catalog-integration API from Snowflake — 2 operation(s) for catalog-integration.
  name: Snowflake Catalog Integration API
  phrasing_intents:
  - id: listCatalogIntegrations
    intent: List catalog integrations
    question: Which external Iceberg catalog integrations are set up in my account?
  - id: createCatalogIntegration
    intent: Create a catalog integration
    question: How do I connect Snowflake to an external Iceberg catalog?
  - id: fetchCatalogIntegration
    intent: Get a catalog integration
    question: What catalog and table format does a specific catalog integration use?
  - id: deleteCatalogIntegration
    intent: Delete a catalog integration
    question: How do I remove a catalog integration I no longer need?
  - id: setTags
    intent: Set tags on a catalog integration
    question: How do I attach tags to a catalog integration?
  - id: unsetTags
    intent: Remove tags from a catalog integration
    question: How can I remove a tag from a catalog integration?
  - id: getTags
    intent: Get tag assignments for a catalog integration
    question: Which tags are assigned to a catalog integration?
  phrasing_ops: 7
  slug: snowflake-catalog-integration-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The compute-pool API from Snowflake — 6 operation(s) for compute-pool.
  name: Snowflake Compute Pool API
  phrasing_intents:
  - id: listComputePools
    intent: List compute pools in the account
    question: Which compute pools exist in my Snowflake account?
  - id: createComputePool
    intent: Create a compute pool
    question: How do I create a compute pool for running container services?
  - id: fetchComputePool
    intent: Get the details of a compute pool
    question: How many active and idle nodes does a specific compute pool have?
  - id: createOrAlterComputePool
    intent: Create or update a compute pool definition
    question: Can I resize an existing compute pool by sending its full definition?
  - id: deleteComputePool
    intent: Delete a compute pool
    question: How do I drop a compute pool I'm finished with?
  - id: resumeComputePool
    intent: Resume a suspended compute pool
    question: How do I start a suspended compute pool again?
  - id: suspendComputePool
    intent: Suspend an active compute pool
    question: How do I suspend a compute pool so it stops consuming credits?
  - id: stopAllServicesInComputePoolDeprecated
    intent: Stop all services in a pool (legacy endpoint)
    question: Is the old :stopallservices endpoint still available for stopping a pool's services?
  phrasing_ops: 13
  slug: snowflake-compute-pool-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The cortex-analyst API from Snowflake — 4 operation(s) for cortex-analyst.
  name: Snowflake Cortex Analyst API
  phrasing_intents:
  - id: sendFeedback
    intent: Rate a Cortex Analyst response
    question: How do I tell Cortex Analyst an answer was wrong?
  - id: sendMessage
    intent: Ask Cortex Analyst a data question
    question: Can I ask a plain-English question about my data and get SQL back?
  - id: generateVerifiedQuerySuggestions
    intent: Suggest verified queries for a semantic model
    question: Can Cortex Analyst propose verified queries to add to my semantic model?
  - id: fastGeneration
    intent: Generate or improve a semantic model quickly
    question: Can I get real-time suggestions to improve a semantic model?
  - id: preSelection
    intent: Pick relevant tables for semantic model generation
    question: Which tables should go into a new semantic model given my source data?
  - id: generateFiltersAndMetricsSuggestions
    intent: Suggest filters, facts and metrics for a model
    question: What metrics and filters could I add to my semantic view?
  - id: listAgenticOptimizations
    intent: List agentic optimization runs for a model
    question: Which agentic optimization runs have been done on my semantic model?
  - id: getAgenticOptimization
    intent: Check an agentic optimization run's status
    question: Is my agentic optimization run finished yet?
  phrasing_ops: 9
  slug: snowflake-cortex-analyst-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The cortex-inference API from Snowflake — 2 operation(s) for cortex-inference.
  name: Snowflake Cortex Inference API
  phrasing_intents:
  - id: getModels
    intent: List the LLMs available to this session
    question: Which large language models can I call from Cortex in my current session?
  - id: cortexLLMInferenceComplete
    intent: Generate an LLM text completion
    question: How do I send a chat prompt to an LLM through Cortex and get a completion back?
  phrasing_ops: 2
  slug: snowflake-cortex-inference-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The cortex search service API from Snowflake — 5 operation(s) for cortex search service.
  name: Snowflake cortex search service API
  phrasing_intents:
  - id: deleteCortexSearchService
    intent: Delete a Cortex Search service
    question: How do I drop a Cortex Search service I no longer use?
  - id: fetchCortexSearchService
    intent: Get the details of a Cortex Search service
    question: What search column, target lag and indexing state does my Cortex Search service have?
  - id: listCortexSearchServices
    intent: List Cortex Search services in a schema
    question: Which Cortex Search services exist in this schema?
  - id: createCortexSearchService
    intent: Create a Cortex Search service
    question: How do I build a Cortex Search service over a table's text column?
  - id: queryCortexSearchService
    intent: Run a search query against a Cortex Search service
    question: How do I get ranked search results from my Cortex Search service?
  - id: suggestCortexSearchService
    intent: Get autocomplete suggestions from a search service
    question: Can Cortex Search give me type-ahead suggestions for a partial query?
  - id: suspendCortexSearchService
    intent: Suspend indexing or serving on a search service
    question: Can I pause indexing on a Cortex Search service but keep serving queries?
  - id: resumeCortexSearchService
    intent: Resume indexing or serving on a search service
    question: How do I turn a suspended Cortex Search service back on?
  phrasing_ops: 9
  slug: snowflake-cortex-search-service-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The database API from Snowflake — 12 operation(s) for database.
  name: Snowflake Database API
  phrasing_intents:
  - id: listDatabases
    intent: List the databases I can access
    question: Which Snowflake databases does my role have access to?
  - id: createDatabase
    intent: Create a new database
    question: How do I create a new database through the REST API?
  - id: createDatabaseFromShare
    intent: Create a database from a data share
    question: How can I turn a data share someone gave me into a database I can query?
  - id: createDatabaseFromShareDeprecated
    intent: Create a database from a share (legacy endpoint)
    question: Is there an older from_share endpoint that puts the database name in the URL path?
  - id: cloneDatabase
    intent: Clone an existing database
    question: How do I make a zero-copy clone of one of my databases?
  - id: fetchDatabase
    intent: Get the details of a database
    question: What are the owner, retention time and other properties of a specific database?
  - id: createOrAlterDatabase
    intent: Create or update a database definition
    question: Can I change an existing database's properties by sending its full definition?
  - id: deleteDatabase
    intent: Drop a database
    question: How do I drop a database I no longer need?
  phrasing_ops: 18
  slug: snowflake-database-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The database-role API from Snowflake — 7 operation(s) for database-role.
  name: Snowflake Database Role API
  phrasing_intents:
  - id: listDatabaseRoles
    intent: List database roles in a database
    question: Which database roles are defined in this Snowflake database?
  - id: createDatabaseRole
    intent: Create a database role
    question: How do I create a role scoped to a single database?
  - id: deleteDatabaseRole
    intent: Delete a database role
    question: How do I remove a database role I no longer need?
  - id: cloneDatabaseRole
    intent: Clone a database role
    question: Can I create a new database role by copying an existing one?
  - id: listGrants
    intent: List privileges granted to a database role
    question: What privileges does a database role currently hold?
  - id: grantPrivileges
    intent: Grant privileges to a database role
    question: How do I give a database role SELECT on a table?
  - id: revokeGrants
    intent: Revoke privileges from a database role
    question: How do I take away a privilege a database role already has?
  - id: listFutureGrants
    intent: List future grants on a database role
    question: Which future grants apply to a database role for objects not yet created?
  phrasing_ops: 13
  slug: snowflake-database-role-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The dynamic-table API from Snowflake — 10 operation(s) for dynamic-table.
  name: Snowflake Dynamic Table API
  phrasing_intents:
  - id: listDynamicTables
    intent: List dynamic tables in a schema
    question: Which dynamic tables exist in this schema?
  - id: createDynamicTable
    intent: Create a dynamic table
    question: How do I create a dynamic table that refreshes from a query automatically?
  - id: fetchDynamicTable
    intent: Get the details of a dynamic table
    question: What query, target lag and scheduling state does a given dynamic table have?
  - id: deleteDynamicTable
    intent: Drop a dynamic table
    question: How do I drop a dynamic table I no longer need?
  - id: cloneDynamicTable
    intent: Clone a dynamic table
    question: Can I copy a dynamic table into another schema or database?
  - id: undropDynamicTable
    intent: Restore a dropped dynamic table
    question: Can I recover a dynamic table I dropped by mistake?
  - id: suspendDynamicTable
    intent: Pause refreshes on a dynamic table
    question: How do I stop a dynamic table from refreshing for a while?
  - id: resumeDynamicTable
    intent: Resume refreshes on a dynamic table
    question: How do I turn scheduled refreshes back on for a suspended dynamic table?
  phrasing_ops: 15
  slug: snowflake-dynamic-table-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The event-table API from Snowflake — 3 operation(s) for event-table.
  name: Snowflake Event Table API
  phrasing_intents:
  - id: listEventTables
    intent: List event tables in a schema
    question: Which event tables exist in this schema for logs and traces?
  - id: createEventTable
    intent: Create an event table
    question: How do I create an event table to collect logs and trace events?
  - id: fetchEventTable
    intent: Get the details of an event table
    question: What columns, row count and retention does a given event table have?
  - id: deleteEventTable
    intent: Drop an event table
    question: How do I drop an event table I no longer need?
  - id: renameEventTable
    intent: Rename an event table
    question: Can I rename an event table without recreating it?
  - id: setTags
    intent: Attach tags to an event table
    question: How do I apply governance tags to an event table?
  - id: unsetTags
    intent: Remove tags from an event table
    question: How do I remove a tag from an event table?
  - id: getTags
    intent: Show the tags assigned to an event table
    question: Which tags are assigned to this event table?
  phrasing_ops: 8
  slug: snowflake-event-table-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The external-volume API from Snowflake — 3 operation(s) for external-volume.
  name: Snowflake External Volume API
  phrasing_intents:
  - id: listExternalVolumes
    intent: List external volumes
    question: Which external volumes are configured for my Iceberg tables?
  - id: createExternalVolume
    intent: Create an external volume
    question: How do I point Snowflake at my own cloud storage for Iceberg data?
  - id: fetchExternalVolume
    intent: Get an external volume
    question: What storage locations does a specific external volume use?
  - id: deleteExternalVolume
    intent: Delete an external volume
    question: How do I remove an external volume?
  - id: undropExternalVolume
    intent: Restore a dropped external volume
    question: I dropped an external volume by mistake; can I bring it back?
  phrasing_ops: 5
  slug: snowflake-external-volume-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The function API from Snowflake — 3 operation(s) for function.
  name: Snowflake Function API
  phrasing_intents:
  - id: listFunctions
    intent: List user functions in a schema
    question: Which user-defined functions exist in this schema?
  - id: createFunction
    intent: Create a function
    question: How do I define a new function in a Snowflake schema?
  - id: fetchFunction
    intent: Describe a function
    question: What signature and return type does a specific function have?
  - id: deleteFunction
    intent: Delete a function
    question: How do I drop a function with a specific argument signature?
  - id: executeFunction
    intent: Execute a function
    question: Can I call a Snowflake function over REST and get its result?
  - id: setTags
    intent: Set tags on a function
    question: How do I attach tags to a function?
  - id: unsetTags
    intent: Remove tags from a function
    question: How can I remove a tag from a function?
  - id: getTags
    intent: Get tag assignments for a function
    question: Which tags are assigned to a function?
  phrasing_ops: 8
  slug: snowflake-function-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The grant API from Snowflake — 7 operation(s) for grant.
  name: Snowflake Grant API
  phrasing_intents:
  - id: grantPrivilege
    intent: Grant privileges on one object to a role or user
    question: How do I give a role SELECT on a specific table?
  - id: grantGroupPrivilege
    intent: Grant privileges on all or future objects in a scope
    question: How do I grant a role access to all tables in a schema, including ones created later?
  - id: revokePrivilege
    intent: Revoke a privilege on one object
    question: How do I take SELECT on a single table away from a role?
  - id: revokePrivilegeGrantOption
    intent: Revoke only the grant option on one object
    question: Can I stop a role from re-granting a privilege while letting it keep the privilege itself?
  - id: revokeGroupPrivilege
    intent: Revoke a privilege on all or future objects
    question: How do I undo a future grant on all tables in a schema?
  - id: revokeGroupPrivilegeGrantOption
    intent: Revoke the grant option on all or future objects
    question: Can I remove the grant option from a future grant but leave the privilege in place?
  - id: listGrantsTo
    intent: List privileges granted to a role or user
    question: What roles and privileges has a given role or user been granted?
  phrasing_ops: 7
  slug: snowflake-grant-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The iceberg-table API from Snowflake — 14 operation(s) for iceberg-table.
  name: Snowflake Iceberg Table API
  phrasing_intents:
  - id: listIcebergTables
    intent: List Iceberg tables in a schema
    question: Which Apache Iceberg tables can I see in this Snowflake schema?
  - id: createSnowflakeManagedIcebergTable
    intent: Create a Snowflake-managed Iceberg table
    question: How do I define a new empty Iceberg table that uses Snowflake as its catalog?
  - id: createSnowflakeManagedIcebergTableAsSelect
    intent: Create a managed Iceberg table from a query
    question: Can I build a managed Iceberg table directly from the results of a SELECT query?
  - id: createUnmanagedIcebergTableFromAWSGlueCatalog
    intent: Register an Iceberg table from AWS Glue
    question: How can Snowflake read an Iceberg table that is catalogued in AWS Glue?
  - id: createUnmanagedIcebergTableFromDelta
    intent: Create an Iceberg table from Delta files
    question: Can I expose existing Delta Lake files in Snowflake as an Iceberg table?
  - id: createUnmanagedIcebergTableFromIcebergFiles
    intent: Create an Iceberg table from metadata files
    question: How can I load an Iceberg table into Snowflake from a metadata.json file in object storage?
  - id: createUnmanagedIcebergTableFromIcebergRest
    intent: Register an Iceberg table from a REST catalog
    question: Can Snowflake query a table that lives in an Iceberg REST catalog?
  - id: fetchIcebergTable
    intent: Describe an Iceberg table
    question: What are the columns and settings of a specific Iceberg table?
  phrasing_ops: 19
  slug: snowflake-iceberg-table-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The image-repository API from Snowflake — 3 operation(s) for image-repository.
  name: Snowflake Image Repository API
  phrasing_intents:
  - id: listImageRepositories
    intent: List image repositories in a schema
    question: Which container image repositories exist in this schema?
  - id: createImageRepository
    intent: Create an image repository
    question: How do I create a registry repository to push my container images into?
  - id: fetchImageRepository
    intent: Get the details of an image repository
    question: What's the repository URL I should push images to for a given image repository?
  - id: deleteImageRepository
    intent: Delete an image repository
    question: How do I delete an image repository I no longer use?
  - id: listImagesInRepository
    intent: List images stored in a repository
    question: Which container images have been pushed to this repository?
  - id: setTags
    intent: Attach tags to an image repository
    question: How do I apply governance tags to an image repository?
  - id: unsetTags
    intent: Remove tags from an image repository
    question: How do I remove a tag from an image repository?
  - id: getTags
    intent: Show the tags assigned to an image repository
    question: Which tags are assigned to this image repository?
  phrasing_ops: 8
  slug: snowflake-image-repository-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The managed-account API from Snowflake — 2 operation(s) for managed-account.
  name: Snowflake Managed Account API
  phrasing_intents:
  - id: listManagedAccounts
    intent: List managed reader accounts
    question: Which managed reader accounts have I created for data consumers?
  - id: createManagedAccount
    intent: Create a managed reader account
    question: How do I create a reader account for a consumer who isn't a Snowflake customer?
  - id: deleteManagedAccount
    intent: Delete a managed reader account
    question: What happens to the objects inside a reader account when I remove it?
  phrasing_ops: 3
  slug: snowflake-managed-account-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The network-policy API from Snowflake — 2 operation(s) for network-policy.
  name: Snowflake Network Policy API
  phrasing_intents:
  - id: listNetworkPolicies
    intent: List network policies
    question: Which network policies are defined in my account?
  - id: createNetworkPolicy
    intent: Create a network policy
    question: How do I restrict logins to a set of allowed IP addresses?
  - id: fetchNetworkPolicy
    intent: Describe a network policy
    question: What IPs and rules does this network policy allow or block?
  - id: deleteNetworkPolicy
    intent: Delete a network policy
    question: How do I drop a network policy?
  - id: setTags
    intent: Set tags on a network policy
    question: How do I tag a network policy?
  - id: unsetTags
    intent: Remove tags from a network policy
    question: Can I remove tags from a network policy?
  - id: getTags
    intent: Get the tags assigned to a network policy
    question: Which tags are assigned to this network policy?
  phrasing_ops: 7
  slug: snowflake-network-policy-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The notebook API from Snowflake — 6 operation(s) for notebook.
  name: Snowflake Notebook API
  phrasing_intents:
  - id: listNotebooks
    intent: List notebooks in a schema
    question: Which notebooks exist in this schema?
  - id: createNotebook
    intent: Create a notebook
    question: How do I create a notebook from a file already sitting in a stage?
  - id: fetchNotebook
    intent: Describe a single notebook
    question: What warehouse, versions and main file does this notebook have?
  - id: deleteNotebook
    intent: Delete a notebook
    question: How do I drop a notebook I no longer need?
  - id: executeNotebook
    intent: Run a notebook
    question: Can I run a notebook end to end without opening it?
  - id: renameNotebook
    intent: Rename or move a notebook
    question: How do I rename a notebook?
  - id: addLiveVersionNotebook
    intent: Add a LIVE version to a notebook
    question: Can I create an editable LIVE version of a notebook from its last version?
  - id: commitNotebook
    intent: Commit a notebook's LIVE version
    question: How do I commit my notebook changes to its connected Git repository?
  phrasing_ops: 11
  slug: snowflake-notebook-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The notification-integration API from Snowflake — 2 operation(s) for notification-integration.
  name: Snowflake Notification Integration API
  phrasing_intents:
  - id: listNotificationIntegrations
    intent: List notification integrations
    question: Which notification integrations exist in my Snowflake account?
  - id: createNotificationIntegration
    intent: Create a notification integration
    question: How do I set up an integration so Snowflake can send notifications to a queue, webhook or email?
  - id: fetchNotificationIntegration
    intent: Get a notification integration
    question: Where does a particular notification integration send its messages?
  - id: deleteNotificationIntegration
    intent: Delete a notification integration
    question: How do I remove a notification integration?
  - id: setTags
    intent: Set tags on a notification integration
    question: How do I attach tags to a notification integration?
  - id: unsetTags
    intent: Remove tags from a notification integration
    question: How can I remove a tag from a notification integration?
  - id: getTags
    intent: Get tag assignments for a notification integration
    question: Which tags are assigned to a notification integration?
  phrasing_ops: 7
  slug: snowflake-notification-integration-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The pipe API from Snowflake — 3 operation(s) for pipe.
  name: Snowflake Pipe API
  phrasing_intents:
  - id: listPipes
    intent: List Snowpipe pipes in a schema
    question: Which Snowpipe pipes are defined in this schema?
  - id: createPipe
    intent: Create a Snowpipe pipe
    question: How do I set up continuous loading from a stage with a pipe?
  - id: fetchPipe
    intent: Get a pipe's definition
    question: What COPY statement does a particular pipe run?
  - id: deletePipe
    intent: Delete a pipe
    question: How do I remove a Snowpipe pipe?
  - id: refreshPipe
    intent: Refresh a pipe to load staged files
    question: Can I make a pipe pick up files already sitting in the stage?
  - id: setTags
    intent: Set tags on a pipe
    question: How do I attach tags to a pipe?
  - id: unsetTags
    intent: Remove tags from a pipe
    question: How can I remove a tag from a pipe?
  - id: getTags
    intent: Get tag assignments for a pipe
    question: Which tags are assigned to a pipe?
  phrasing_ops: 8
  slug: snowflake-pipe-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The procedure API from Snowflake — 3 operation(s) for procedure.
  name: Snowflake Procedure API
  phrasing_intents:
  - id: listProcedures
    intent: List stored procedures in a schema
    question: Which stored procedures are defined in this schema?
  - id: createProcedure
    intent: Create a stored procedure
    question: How do I create a stored procedure with its arguments, return type and language?
  - id: fetchProcedure
    intent: Get the definition of a stored procedure
    question: What arguments, return type and body does a particular procedure have?
  - id: deleteProcedure
    intent: Drop a stored procedure
    question: How do I drop a stored procedure I no longer need?
  - id: callProcedure
    intent: Call a stored procedure
    question: How do I execute a stored procedure over REST and get its result back?
  - id: setTags
    intent: Attach tags to a stored procedure
    question: How do I apply governance tags to a stored procedure?
  - id: unsetTags
    intent: Remove tags from a stored procedure
    question: How do I remove a tag from a stored procedure?
  - id: getTags
    intent: Show the tags assigned to a stored procedure
    question: Which tags are assigned to this stored procedure?
  phrasing_ops: 8
  slug: snowflake-procedure-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The result API from Snowflake — 1 operation(s) for result.
  name: Snowflake Result API
  phrasing_intents:
  - id: fetchResult
    intent: Check an async request's status or fetch its result
    question: How do I check whether a long-running REST request has finished?
  phrasing_ops: 1
  slug: snowflake-result-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The role API from Snowflake — 8 operation(s) for role.
  name: Snowflake Role API
  phrasing_intents:
  - id: listRoles
    intent: List account roles
    question: Which roles exist in my Snowflake account?
  - id: createRole
    intent: Create a role
    question: How do I create a new account role for a team?
  - id: deleteRole
    intent: Drop a role
    question: How do I drop a role nobody uses anymore?
  - id: listGrants
    intent: List privileges granted to a role
    question: What privileges does this role currently hold?
  - id: grantPrivileges
    intent: Grant privileges on an object to a role
    question: How do I give a role SELECT on a table?
  - id: revokeGrants
    intent: Revoke privileges from a role
    question: Can I take a privilege away from a role?
  - id: listGrantsOf
    intent: List who has been granted a role
    question: Which users and roles have been granted this role?
  - id: listGrantsOn
    intent: List grants on a role object
    question: What privileges have been granted on the role itself, such as ownership?
  phrasing_ops: 14
  slug: snowflake-role-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The schema API from Snowflake — 4 operation(s) for schema.
  name: Snowflake Schema API
  phrasing_intents:
  - id: listSchemas
    intent: List schemas in a database
    question: Which schemas can I access in this database?
  - id: createSchema
    intent: Create a schema
    question: How do I create a new schema in a database?
  - id: cloneSchema
    intent: Clone a schema
    question: Can I zero-copy clone a whole schema into another database?
  - id: undropSchema
    intent: Restore a dropped schema
    question: Can I recover a schema I dropped by accident?
  - id: fetchSchema
    intent: Describe a single schema
    question: What retention, owner and settings does this schema have?
  - id: createOrAlterSchema
    intent: Create or alter a schema with a full definition
    question: Can I change a schema's settings by resubmitting its complete definition?
  - id: deleteSchema
    intent: Drop a schema
    question: How do I drop a schema?
  - id: setTags
    intent: Set tags on a schema
    question: How do I tag a schema?
  phrasing_ops: 10
  slug: snowflake-schema-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The service API from Snowflake — 13 operation(s) for service.
  name: Snowflake Service API
  phrasing_intents:
  - id: listServices
    intent: List container services in a schema
    question: Which Snowpark Container Services services are running in this schema?
  - id: createService
    intent: Create a container service
    question: How do I deploy a long-running service on a compute pool from a spec?
  - id: executeJobService
    intent: Run a one-off job service
    question: How do I run a batch job in a container that exits when it's done?
  - id: fetchService
    intent: Get the details of a service
    question: What compute pool, instance counts and DNS name does a given service have?
  - id: createOrAlterService
    intent: Create or update a service definition
    question: Can I change a running service's spec by resubmitting its full property set?
  - id: deleteService
    intent: Delete a service
    question: How do I tear down a container service I no longer need?
  - id: fetchServiceLogs
    intent: Read a service container's logs
    question: How can I see the log output of a specific container in my service?
  - id: fetchServiceStatus
    intent: Check a service's status
    question: Is my container service running, pending or failed right now?
  phrasing_ops: 16
  slug: snowflake-service-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The stage API from Snowflake — 4 operation(s) for stage.
  name: Snowflake Stage API
  phrasing_intents:
  - id: listStages
    intent: List stages in a schema
    question: Which internal and external stages exist in this schema?
  - id: createStage
    intent: Create an internal or external stage
    question: How do I create an external stage pointing at a cloud storage URL?
  - id: fetchStage
    intent: Describe a stage
    question: What URL, encryption and integration does this stage use?
  - id: deleteStage
    intent: Delete a stage
    question: How do I drop a stage?
  - id: listFiles
    intent: List the files in a stage
    question: What files are sitting in this stage right now?
  - id: getPresignedUrl
    intent: Get a presigned URL for a staged file
    question: How can I get a temporary URL to upload or download a file in a stage?
  phrasing_ops: 6
  slug: snowflake-stage-api
- baseURL: https://{account}.snowflakecomputing.com
  baseurl_source: declared
  description: The statements API from Snowflake — 3 operation(s) for statements.
  name: Snowflake Statements API
  phrasing_intents:
  - id: submitStatement
    intent: Run a SQL statement
    question: How do I run a SQL query against Snowflake over REST?
  - id: getStatementStatus
    intent: Check a statement's status and fetch results
    question: Has my asynchronous SQL statement finished running?
  - id: cancelStatement
    intent: Cancel a running SQL statement
    question: How do I stop a long-running SQL statement I submitted?
  phrasing_ops: 3
  slug: snowflake-statements-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The stream API from Snowflake — 3 operation(s) for stream.
  name: Snowflake Stream API
  phrasing_intents:
  - id: listStreams
    intent: List streams in a schema
    question: Which change-data-capture streams exist in this schema?
  - id: createStream
    intent: Create a change-tracking stream
    question: How do I track inserts, updates and deletes on a table with a stream?
  - id: fetchStream
    intent: Describe a stream
    question: What table does this stream track, and is it stale?
  - id: deleteStream
    intent: Delete a stream
    question: How do I drop a stream I no longer consume?
  - id: cloneStream
    intent: Clone a stream into a schema
    question: Can I copy a stream into another database and schema?
  - id: setTags
    intent: Set tags on a stream
    question: How do I tag a stream?
  - id: unsetTags
    intent: Remove tags from a stream
    question: Can I remove tags from a stream?
  - id: getTags
    intent: Get the tags assigned to a stream
    question: Which tags are assigned to this stream?
  phrasing_ops: 8
  slug: snowflake-stream-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The table API from Snowflake — 16 operation(s) for table.
  name: Snowflake Table API
  phrasing_intents:
  - id: listTables
    intent: List the tables in a schema
    question: Which tables exist in this Snowflake schema?
  - id: createTable
    intent: Create a new table
    question: How do I create a new table with defined columns in a schema?
  - id: createTableAsSelectDeprecated
    intent: Create a table from a query (legacy endpoint)
    question: Is there an older as_select endpoint that names the new table in the URL path?
  - id: createTableAsSelect
    intent: Create a table from a SELECT query result
    question: Can I turn the output of a SELECT statement into a brand-new table?
  - id: createTableUsingTemplateDeprecated
    intent: Create a table from staged file templates (legacy)
    question: Is there an older using_template endpoint that takes the table name in the path?
  - id: createTableUsingTemplate
    intent: Create a table from templates in staged files
    question: Can I create a table whose columns are inferred from files sitting in a stage?
  - id: fetchTable
    intent: Describe a single table
    question: What columns, clustering and retention settings does this table have?
  - id: createOrAlterTable
    intent: Create or alter a table with a full definition
    question: Can I alter an existing table by resubmitting its whole definition?
  phrasing_ops: 22
  slug: snowflake-table-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The task API from Snowflake — 10 operation(s) for task.
  name: Snowflake Task API
  phrasing_intents:
  - id: listTasks
    intent: List the tasks in a schema
    question: Which scheduled tasks are defined in this schema?
  - id: createTask
    intent: Create a scheduled task
    question: How do I schedule a SQL statement to run on a cron schedule?
  - id: fetchTask
    intent: Describe a single task
    question: What schedule, warehouse and SQL does this task use?
  - id: createOrAlterTask
    intent: Create or alter a task with a full definition
    question: Can I change an existing task's schedule by resending its whole definition?
  - id: deleteTask
    intent: Drop a task
    question: How do I drop a task I no longer want scheduled?
  - id: executeTask
    intent: Run a task immediately
    question: Can I trigger a task right now without waiting for its schedule?
  - id: resumeTask
    intent: Resume a suspended task
    question: How do I restart a task that is currently suspended?
  - id: suspendTask
    intent: Suspend a running task
    question: Can I pause a task so it stops firing on its schedule?
  phrasing_ops: 16
  slug: snowflake-task-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The user API from Snowflake — 4 operation(s) for user.
  name: Snowflake User API
  phrasing_intents:
  - id: createUser
    intent: Create a user
    question: How do I add a new user with a default role and warehouse?
  - id: listUsers
    intent: List users in the account
    question: Who are all the users in my Snowflake account?
  - id: fetchUser
    intent: Get a user's details
    question: What default role, warehouse and last login does a particular user have?
  - id: deleteUser
    intent: Delete a user
    question: How do I remove a user who has left the company?
  - id: createOrAlterUser
    intent: Create or update a user
    question: Can I update an existing user's properties by sending the full user definition?
  - id: listGrants
    intent: List roles granted to a user
    question: Which roles has a given user been granted?
  - id: grant
    intent: Grant a role to a user
    question: How do I give a user a role?
  - id: revokeGrants
    intent: Revoke a role from a user
    question: How do I take a role away from a user?
  phrasing_ops: 11
  slug: snowflake-user-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The user-defined-function API from Snowflake — 3 operation(s) for user-defined-function.
  name: Snowflake User Defined Function API
  phrasing_intents:
  - id: createUserDefinedFunction
    intent: Create a user-defined function
    question: How do I create a custom function with its own arguments and return type?
  - id: listUserDefinedFunctions
    intent: List user-defined functions in a schema
    question: Which UDFs are defined in this schema?
  - id: fetchUserDefinedFunction
    intent: Describe a user-defined function
    question: What arguments, return type and language does this UDF use?
  - id: deleteUserDefinedFunction
    intent: Drop a user-defined function
    question: How do I drop a UDF I no longer use?
  - id: executeUserDefinedFunction
    intent: Call a user-defined function
    question: Can I invoke a UDF directly over REST and get its result?
  - id: renameUserDefinedFunction
    intent: Rename or move a user-defined function
    question: How do I rename a UDF?
  - id: setTags
    intent: Set tags on a user-defined function
    question: How do I tag a UDF?
  - id: unsetTags
    intent: Remove tags from a user-defined function
    question: Can I remove tags from a UDF?
  phrasing_ops: 9
  slug: snowflake-user-defined-function-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The view API from Snowflake — 2 operation(s) for view.
  name: Snowflake View API
  phrasing_intents:
  - id: listViews
    intent: List views in a schema
    question: Which views are defined in this schema?
  - id: createView
    intent: Create a view
    question: How do I save a SELECT query as a reusable view?
  - id: fetchView
    intent: Describe a view
    question: What query and columns define this view?
  - id: deleteView
    intent: Delete a view
    question: How do I drop a view?
  - id: setTags
    intent: Set tags on a view
    question: How do I tag a view?
  - id: unsetTags
    intent: Remove tags from a view
    question: Can I remove tags from a view?
  - id: getTags
    intent: Get the tags assigned to a view
    question: Which tags are assigned to this view?
  phrasing_ops: 7
  slug: snowflake-view-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The warehouse API from Snowflake — 9 operation(s) for warehouse.
  name: Snowflake Warehouse API
  phrasing_intents:
  - id: createWarehouse
    intent: Create a virtual warehouse
    question: How do I spin up a new compute warehouse?
  - id: listWarehouses
    intent: List virtual warehouses
    question: Which virtual warehouses exist in my Snowflake account?
  - id: fetchWarehouse
    intent: Describe a warehouse
    question: What size and state is a particular warehouse in right now?
  - id: deleteWarehouse
    intent: Drop a warehouse
    question: How do I permanently remove a virtual warehouse?
  - id: createOrAlterWarehouse
    intent: Create or alter a warehouse with full settings
    question: Can I change an existing warehouse's settings by sending its full definition?
  - id: resumeWarehouse
    intent: Resume a suspended warehouse
    question: How do I bring a suspended warehouse back to running?
  - id: suspendWarehouse
    intent: Suspend a running warehouse
    question: How do I stop a warehouse from burning credits when idle?
  - id: renameWarehouse
    intent: Rename a warehouse
    question: How do I give an existing warehouse a new name?
  phrasing_ops: 15
  slug: snowflake-warehouse-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The Snowflake Cortex Messages API is a REST API that performs LLM text completion inference using the Cortex Messages (Anthropic-compatible) request format.
  name: Cortex Messages API
  phrasing_intents:
  - id: cortexGenericAnthropicMessages
    intent: Generate text with the Cortex Messages API
    question: How do I send a chat prompt to an LLM through Cortex using the Messages request format?
  phrasing_ops: 1
  slug: snowflake-cortex-generic-anthropic-api
- baseURL: https://org-account.snowflakecomputing.com
  baseurl_source: declared
  description: The Snowflake Cortex Chat Completions API is a REST API that performs LLM text completion inference using the Cortex Chat Completions (OpenAI-compatible) request format.
  name: Cortex Chat Completions API
  phrasing_intents:
  - id: cortexGenericOpenAIChatCompletions
    intent: Run a chat completion on Cortex
    question: Can I call Snowflake Cortex LLMs using the Chat Completions request format?
  phrasing_ops: 1
  slug: snowflake-cortex-generic-openai-api
arazzos:
- description: Submit a SQL statement asynchronously, then cancel its execution by handle.
  name: Snowflake Cancel a Running SQL Statement
  slug: snowflake-cancel-running-statement-workflow
- description: Clone an existing database into a new database, then describe the clone to confirm it.
  name: Snowflake Clone a Database and Verify
  slug: snowflake-clone-database-and-verify-workflow
- description: Create an alert with a condition and action, describe it, then execute it on demand.
  name: Snowflake Create and Execute an Alert
  slug: snowflake-create-and-execute-alert-workflow
- description: Create a task, resume it from its initial suspended state, then run it once on demand.
  name: Snowflake Create, Resume, and Execute a Task
  slug: snowflake-create-and-execute-task-workflow
- description: Create a dynamic table from a query, describe it, then trigger a manual refresh.
  name: Snowflake Create, Verify, and Refresh a Dynamic Table
  slug: snowflake-create-and-refresh-dynamic-table-workflow
- description: Create a pipe with a COPY statement, describe it, then trigger a refresh to ingest files.
  name: Snowflake Create, Verify, and Refresh a Pipe
  slug: snowflake-create-and-refresh-pipe-workflow
- description: Create a virtual warehouse and then describe it to confirm its settings.
  name: Snowflake Create and Verify Warehouse
  slug: snowflake-create-and-verify-warehouse-workflow
- description: Create a database, describe it to confirm, then create a schema inside it.
  name: Snowflake Create Database, Verify, and Add Schema
  slug: snowflake-create-database-and-schema-workflow
- description: Create a role, grant privileges on a securable to it, then list its grants to confirm.
  name: Snowflake Create Role and Grant Privileges
  slug: snowflake-create-role-and-grant-privileges-workflow
- description: Create a schema in an existing database, add a table, then describe the table.
  name: Snowflake Create Schema and Table
  slug: snowflake-create-schema-and-table-workflow
- description: Create a named stage, describe it to confirm, then list the files staged in it.
  name: Snowflake Create Stage, Verify, and List Files
  slug: snowflake-create-stage-and-list-files-workflow
- description: Create a table, create a stream that tracks changes to it, then describe the stream.
  name: Snowflake Create a Table and a Change Stream On It
  slug: snowflake-create-stream-on-table-workflow
- description: Run a CREATE TABLE DDL statement, then run an INSERT statement against it.
  name: Snowflake Create Table and Insert Rows via SQL
  slug: snowflake-create-table-and-insert-via-sql-workflow
- description: Create a user, grant a role to the user, then list the user's grants to confirm.
  name: Snowflake Create User and Grant Role
  slug: snowflake-create-user-and-grant-role-workflow
- description: Create a database, create a schema inside it, then create a table inside that schema.
  name: Snowflake Provision Database, Schema, and Table
  slug: snowflake-provision-database-schema-table-workflow
- description: Resume a suspended warehouse and confirm it is running by describing it.
  name: Snowflake Resume Warehouse and Verify State
  slug: snowflake-resume-warehouse-and-verify-workflow
- description: Submit a SQL statement asynchronously and check its execution status by handle.
  name: Snowflake Submit Asynchronous SQL Statement
  slug: snowflake-submit-async-sql-statement-workflow
- description: Submit a SQL statement for execution, poll its status, then fetch the result set.
  name: Snowflake Submit SQL Statement and Poll for Results
  slug: snowflake-submit-sql-statement-and-poll-workflow
- description: Create a warehouse, describe it to confirm, then suspend it to stop billing.
  name: Snowflake Warehouse Create, Verify, and Suspend Lifecycle
  slug: snowflake-warehouse-lifecycle-workflow
artifact_total: 1393
asyncapis:
- description: ''
  name: Snowflake Webhooks
  slug: snowflake-webhooks
collections:
- collection_type: postman
  name: Snowflake Account API
  slug: postman-account
- collection_type: postman
  name: Snowflake Alert API
  slug: postman-alert
- collection_type: postman
  name: Snowflake API Integration API
  slug: postman-api-integration
- collection_type: postman
  name: Snowflake Artifact Repository API
  slug: postman-artifact-repository
- collection_type: postman
  name: Snowflake Catalog Integration API
  slug: postman-catalog-integration
- collection_type: postman
  name: Snowflake Compute Pools API
  slug: postman-compute-pool
- collection_type: postman
  name: Cortex Analyst API
  slug: postman-cortex-analyst
- collection_type: postman
  name: Cortex Embed API
  slug: postman-cortex-embed
- collection_type: postman
  name: Cortex Messages API
  slug: postman-cortex-generic-anthropic
- collection_type: postman
  name: Cortex Chat Completions API
  slug: postman-cortex-generic-openai
- collection_type: postman
  name: Cortex Inference API
  slug: postman-cortex-inference
- collection_type: postman
  name: Cortex Search REST API
  slug: postman-cortex-search-service
- collection_type: postman
  name: Snowflake Database Role API
  slug: postman-database-role
- collection_type: postman
  name: Snowflake Database API
  slug: postman-database
- collection_type: postman
  name: Snowflake Dynamic Table API
  slug: postman-dynamic-table
- collection_type: postman
  name: Snowflake Event Table API
  slug: postman-event-table
- collection_type: postman
  name: Snowflake External Volume API
  slug: postman-external-volume
- collection_type: postman
  name: Snowflake Function API
  slug: postman-function
- collection_type: postman
  name: Snowflake Grant API
  slug: postman-grant
- collection_type: postman
  name: Snowflake Iceberg Table API
  slug: postman-iceberg-table
- collection_type: postman
  name: Snowflake Image Repository API
  slug: postman-image-repository
- collection_type: postman
  name: Snowflake Managed Account API
  slug: postman-managed-account
- collection_type: postman
  name: Snowflake Network Policy API
  slug: postman-network-policy
- collection_type: postman
  name: Snowflake Network Rule API
  slug: postman-network-rule
- collection_type: postman
  name: Snowflake Notebook API
  slug: postman-notebook
- collection_type: postman
  name: Snowflake Notification Integration API
  slug: postman-notification-integration
- collection_type: postman
  name: Snowflake Password Policy API
  slug: postman-password-policy
- collection_type: postman
  name: Snowflake Pipe API
  slug: postman-pipe
- collection_type: postman
  name: Snowflake Procedure API
  slug: postman-procedure
- collection_type: postman
  name: Snowflake Result API
  slug: postman-result
- collection_type: postman
  name: Snowflake Role API
  slug: postman-role
- collection_type: postman
  name: Snowflake Schema API
  slug: postman-schema
- collection_type: postman
  name: Snowflake Secret API
  slug: postman-secret
- collection_type: postman
  name: Snowflake Sequence API
  slug: postman-sequence
- collection_type: postman
  name: Snowflake Services API
  slug: postman-service
- collection_type: postman
  name: Snowflake SQL REST API
  slug: postman-snowflake-sql-rest-api
- collection_type: postman
  name: Snowflake Spark Connect API
  slug: postman-spark-connect
- collection_type: postman
  name: Snowflake SQL API
  slug: postman-sqlapi
- collection_type: postman
  name: Snowflake Stage API
  slug: postman-stage
- collection_type: postman
  name: Snowflake Stream API
  slug: postman-stream
- collection_type: postman
  name: Snowflake Streamlit API
  slug: postman-streamlit
- collection_type: postman
  name: Snowflake Table API
  slug: postman-table
- collection_type: postman
  name: Snowflake Tag API
  slug: postman-tag
- collection_type: postman
  name: Snowflake Task API
  slug: postman-task
- collection_type: postman
  name: Snowflake User Defined Function API
  slug: postman-user-defined-function
- collection_type: postman
  name: Snowflake User API
  slug: postman-user
- collection_type: postman
  name: Snowflake View API
  slug: postman-view
- collection_type: postman
  name: Snowflake Warehouse API
  slug: postman-warehouse
- collection_type: open
  name: Snowflake Account API
  slug: open-snowflake-account-api
- collection_type: open
  name: Snowflake Alert API
  slug: open-snowflake-alert-api
- collection_type: open
  name: Snowflake API Integration API
  slug: open-snowflake-api-integration-api
- collection_type: open
  name: Snowflake Artifact Repository API
  slug: open-snowflake-artifact-repository-api
- collection_type: open
  name: Snowflake Catalog Integration API
  slug: open-snowflake-catalog-integration-api
- collection_type: open
  name: Snowflake Compute Pool API
  slug: open-snowflake-compute-pool-api
- collection_type: open
  name: Snowflake Cortex Analyst API
  slug: open-snowflake-cortex-analyst-api
- collection_type: open
  name: Cortex Embed API
  slug: open-snowflake-cortex-embed-api
- collection_type: open
  name: Cortex Messages Cortex Generic Anthropic API
  slug: open-snowflake-cortex-generic-anthropic-api
- collection_type: open
  name: Cortex Chat Completions Cortex Generic Openai API
  slug: open-snowflake-cortex-generic-openai-api
- collection_type: open
  name: Snowflake Cortex Inference API
  slug: open-snowflake-cortex-inference-api
- collection_type: open
  name: Snowflake cortex search service API
  slug: open-snowflake-cortex-search-service-api
- collection_type: open
  name: Snowflake Database API
  slug: open-snowflake-database-api
- collection_type: open
  name: Snowflake Database Role API
  slug: open-snowflake-database-role-api
- collection_type: open
  name: Snowflake Dynamic Table API
  slug: open-snowflake-dynamic-table-api
- collection_type: open
  name: Snowflake Event Table API
  slug: open-snowflake-event-table-api
- collection_type: open
  name: Snowflake External Volume API
  slug: open-snowflake-external-volume-api
- collection_type: open
  name: Snowflake Function API
  slug: open-snowflake-function-api
- collection_type: open
  name: Snowflake Grant API
  slug: open-snowflake-grant-api
- collection_type: open
  name: Snowflake Iceberg Table API
  slug: open-snowflake-iceberg-table-api
- collection_type: open
  name: Snowflake Image Repository API
  slug: open-snowflake-image-repository-api
- collection_type: open
  name: Snowflake Managed Account API
  slug: open-snowflake-managed-account-api
- collection_type: open
  name: Snowflake Network Policy API
  slug: open-snowflake-network-policy-api
- collection_type: open
  name: Snowflake Network Rule API
  slug: open-snowflake-network-rule-api
- collection_type: open
  name: Snowflake Notebook API
  slug: open-snowflake-notebook-api
- collection_type: open
  name: Snowflake Notification Integration API
  slug: open-snowflake-notification-integration-api
- collection_type: open
  name: Snowflake Password Policy API
  slug: open-snowflake-password-policy-api
- collection_type: open
  name: Snowflake Pipe API
  slug: open-snowflake-pipe-api
- collection_type: open
  name: Snowflake Procedure API
  slug: open-snowflake-procedure-api
- collection_type: open
  name: Snowflake Result API
  slug: open-snowflake-result-api
- collection_type: open
  name: Snowflake Role API
  slug: open-snowflake-role-api
- collection_type: open
  name: Snowflake Schema API
  slug: open-snowflake-schema-api
- collection_type: open
  name: Snowflake Secret API
  slug: open-snowflake-secret-api
- collection_type: open
  name: Snowflake Sequence API
  slug: open-snowflake-sequence-api
- collection_type: open
  name: Snowflake Service API
  slug: open-snowflake-service-api
- collection_type: open
  name: Snowflake Spark Connect API
  slug: open-snowflake-spark-connect-api
- collection_type: open
  name: Snowflake Stage API
  slug: open-snowflake-stage-api
- collection_type: open
  name: Snowflake Statements API
  slug: open-snowflake-statements-api
- collection_type: open
  name: Snowflake Stream API
  slug: open-snowflake-stream-api
- collection_type: open
  name: Snowflake Streamlit API
  slug: open-snowflake-streamlit-api
- collection_type: open
  name: Snowflake Table API
  slug: open-snowflake-table-api
- collection_type: open
  name: Snowflake Tag API
  slug: open-snowflake-tag-api
- collection_type: open
  name: Snowflake Task API
  slug: open-snowflake-task-api
- collection_type: open
  name: Snowflake User API
  slug: open-snowflake-user-api
- collection_type: open
  name: Snowflake User Defined Function API
  slug: open-snowflake-user-defined-function-api
- collection_type: open
  name: Snowflake View API
  slug: open-snowflake-view-api
- collection_type: open
  name: Snowflake Warehouse API
  slug: open-snowflake-warehouse-api
common:
- group: design
  href: https://artifacts.apis.io/snowflake/rules/snowflake-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/snowflake-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/snowflake/rules/snowflake-rules.yml
  title: ''
  type: Spectral
  url: rules/snowflake-rules.yml
- group: design
  href: https://artifacts.apis.io/snowflake/rules/snowflake-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/snowflake-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/snowflake/json-ld/snowflake-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/snowflake-context.jsonld
- group: design
  href: https://artifacts.apis.io/snowflake/json-ld/common-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/common-context.jsonld
- group: design
  href: https://artifacts.apis.io/snowflake/vocabulary/snowflake-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/snowflake-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/snowflake/hosts/snowflake-hosts.yml
  title: ''
  type: Hosts
  url: hosts/snowflake-hosts.yml
- group: other
  href: https://artifacts.apis.io/snowflake/vendors/snowflake-vendors.yml
  title: ''
  type: Vendors
  url: vendors/snowflake-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.snowflake.com/en/news/
- group: auth
  href: https://artifacts.apis.io/snowflake/security/snowflake-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snowflake-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/snowflake/scopes/snowflake-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/snowflake-scopes.yml
- group: auth
  href: https://artifacts.apis.io/snowflake/authentication/snowflake-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snowflake-authentication.yml
- group: build
  href: https://artifacts.apis.io/snowflake/packages/snowflake-packages.yml
  title: ''
  type: Packages
  url: packages/snowflake-packages.yml
- group: build
  href: https://artifacts.apis.io/snowflake/packages/snowflake-packages.yml
  title: ''
  type: SDKs
  url: packages/snowflake-packages.yml
- group: agent
  href: https://artifacts.apis.io/snowflake/well-known/snowflake-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/snowflake-well-known.yml
- group: auth
  href: https://artifacts.apis.io/snowflake/well-known/snowflake-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/snowflake-security.txt
- group: agent
  href: https://artifacts.apis.io/snowflake/mcp/snowflake-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/snowflake-mcp.yml
- group: build
  href: https://artifacts.apis.io/snowflake/mcp/snowflake-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/snowflake-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/snowflake/llms/snowflake-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snowflake-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.snowflake.com/llms.txt
- group: design
  href: https://artifacts.apis.io/snowflake/conformance/snowflake-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snowflake-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.snowflake.com/
- group: design
  href: https://artifacts.apis.io/snowflake/errors/snowflake-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/snowflake-problem-types.yml
- group: design
  href: https://artifacts.apis.io/snowflake/lifecycle/snowflake-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/snowflake-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.snowflake.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.snowflake.com/en/release-notes/behavior-change-policy
- group: design
  href: https://artifacts.apis.io/snowflake/conventions/snowflake-conventions.yml
  title: ''
  type: Conventions
  url: conventions/snowflake-conventions.yml
- group: design
  href: https://artifacts.apis.io/snowflake/conventions/snowflake-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/snowflake-conventions.yml
- group: start
  href: https://artifacts.apis.io/snowflake/sandbox/snowflake-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/snowflake-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/snowflake/changelog/snowflake-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/snowflake-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.snowflake.com/en/release-notes/overview
- group: build
  href: https://artifacts.apis.io/snowflake/cli/snowflake-cli.yml
  title: ''
  type: CLI
  url: cli/snowflake-cli.yml
- group: build
  title: ''
  type: CLI
  url: https://docs.snowflake.com/en/developer-guide/snowflake-cli/index
- group: design
  href: https://artifacts.apis.io/snowflake/data-model/snowflake-data-model.yml
  title: ''
  type: DataModel
  url: data-model/snowflake-data-model.yml
- group: design
  href: https://artifacts.apis.io/snowflake/asyncapi/snowflake-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/snowflake-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/snowflake/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/snowflake/plans/snowflake-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/snowflake-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/snowflake/rate-limits/snowflake-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/snowflake-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/snowflake/security/snowflake-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/snowflake-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/snowflake/security/snowflake-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/snowflake-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/snowflake/security/snowflake-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/snowflake-trust-center.yml
- group: agent
  href: https://artifacts.apis.io/snowflake/agentic-access/snowflake-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/snowflake-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/snowflake/capabilities/snowflake-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/snowflake-capability-edges.yml
- group: design
  href: https://artifacts.apis.io/snowflake/rules/snowflake-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/snowflake-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/snowflake/vocabulary/snowflake-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/snowflake-vocabulary.yaml
- group: commercial
  href: https://artifacts.apis.io/snowflake/finops/snowflake-finops.yml
  title: ''
  type: FinOps
  url: finops/snowflake-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.snowflake.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.snowflake.com/en/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snowflake.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.snowflake.com/en/developer-guide/snowflake-rest-api/snowflake-rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://quickstarts.snowflake.com/
- group: operate
  title: ''
  type: Support
  url: https://www.snowflake.com/en/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.snowflake.com/
- group: company
  title: ''
  type: Blog
  url: https://www.snowflake.com/en/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snowflakedb
- group: commercial
  title: ''
  type: Pricing
  url: https://www.snowflake.com/en/pricing-options/
- group: start
  title: ''
  type: SignUp
  url: https://signup.snowflake.com/
- group: start
  title: ''
  type: Login
  url: https://app.snowflake.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.snowflake.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.snowflake.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.snowflake.com/en/developer-guide/sql-api/authenticating
- group: design
  title: ''
  type: Versioning
  url: https://docs.snowflake.com/en/release-notes/behavior-change-policy
- group: other
  title: ''
  type: Drivers
  url: https://docs.snowflake.com/en/developer-guide/drivers
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-cancel-running-statement-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-cancel-running-statement-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-clone-database-and-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-clone-database-and-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-create-and-execute-alert-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-create-and-execute-alert-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-create-and-execute-task-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-create-and-execute-task-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-create-and-refresh-dynamic-table-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-create-and-refresh-dynamic-table-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-create-and-refresh-pipe-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-create-and-refresh-pipe-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-create-and-verify-warehouse-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-create-and-verify-warehouse-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-create-database-and-schema-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-create-database-and-schema-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-create-role-and-grant-privileges-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-create-role-and-grant-privileges-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-create-schema-and-table-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-create-schema-and-table-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-create-stage-and-list-files-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-create-stage-and-list-files-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-create-stream-on-table-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-create-stream-on-table-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-create-table-and-insert-via-sql-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-create-table-and-insert-via-sql-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-create-user-and-grant-role-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-create-user-and-grant-role-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-provision-database-schema-table-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-provision-database-schema-table-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-resume-warehouse-and-verify-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-resume-warehouse-and-verify-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-submit-async-sql-statement-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-submit-async-sql-statement-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-submit-sql-statement-and-poll-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-submit-sql-statement-and-poll-workflow.yml
- group: design
  href: https://artifacts.apis.io/snowflake/arazzo/snowflake-warehouse-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/snowflake-warehouse-lifecycle-workflow.yml
created: '2025-06-05'
description: Snowflake is a cloud-based data platform delivering data warehousing, data lakes, data engineering, data science and data application development as a single managed service across AWS, Azure and Google Cloud. Its developer surface is a 47-document OpenAPI corpus over /api/v2 covering databases, schemas, tables, Iceberg and dynamic tables, warehouses, tasks, pipes, streams, roles and grants, plus a SQL API for arbitrary statements and a Cortex family for AI inference, semantic analytics and retrieval. Snowflake also serves a SCIM 2.0 identity endpoint, an Apache Iceberg REST Catalog, and an account-hosted Model Context Protocol server that exposes Cortex tools to agents under Snowflake RBAC.
examples:
- key_count: 37
  name: Account Account Example
  slug: account-account-example
- key_count: 1
  name: Alert Alert Clone Example
  slug: alert-alert-clone-example
- key_count: 11
  name: Alert Alert Example
  slug: alert-alert-example
- key_count: 2
  name: Alert Cron Schedule Example
  slug: alert-cron-schedule-example
- key_count: 1
  name: Alert Minutes Schedule Example
  slug: alert-minutes-schedule-example
- key_count: 2
  name: Alert Point Of Time Example
  slug: alert-point-of-time-example
- key_count: 1
  name: Alert Point Of Time Offset Example
  slug: alert-point-of-time-offset-example
- key_count: 1
  name: Alert Point Of Time Statement Example
  slug: alert-point-of-time-statement-example
- key_count: 1
  name: Alert Point Of Time Timestamp Example
  slug: alert-point-of-time-timestamp-example
- key_count: 1
  name: Alert Schedule Example
  slug: alert-schedule-example
- key_count: 1
  name: Api Integration Api Hook Example
  slug: api-integration-api-hook-example
- key_count: 6
  name: Api Integration Api Integration Example
  slug: api-integration-api-integration-example
- key_count: 0
  name: Api Integration Api Key Example
  slug: api-integration-api-key-example
- key_count: 2
  name: Api Integration Aws Hook Example
  slug: api-integration-aws-hook-example
- key_count: 3
  name: Api Integration Azure Hook Example
  slug: api-integration-azure-hook-example
- key_count: 3
  name: Api Integration Git Hook Example
  slug: api-integration-git-hook-example
- key_count: 2
  name: Api Integration Google Cloud Hook Example
  slug: api-integration-google-cloud-hook-example
- key_count: 1
  name: Catalog Integration Catalog Example
  slug: catalog-integration-catalog-example
- key_count: 7
  name: Catalog Integration Catalog Integration Example
  slug: catalog-integration-catalog-integration-example
- key_count: 4
  name: Catalog Integration Glue Example
  slug: catalog-integration-glue-example
- key_count: 3
  name: Catalog Integration O Auth Example
  slug: catalog-integration-o-auth-example
- key_count: 0
  name: Catalog Integration Object Store Example
  slug: catalog-integration-object-store-example
- key_count: 1
  name: Catalog Integration Polaris Example
  slug: catalog-integration-polaris-example
- key_count: 1
  name: Catalog Integration Rest Authentication Example
  slug: catalog-integration-rest-authentication-example
- key_count: 2
  name: Catalog Integration Rest Config Example
  slug: catalog-integration-rest-config-example
- key_count: 0
  name: Common Downstream Lag Example
  slug: common-downstream-lag-example
- key_count: 4
  name: Common Error Response Example
  slug: common-error-response-example
- key_count: 0
  name: Common Identifier Example
  slug: common-identifier-example
- key_count: 6
  name: Common Parameter Example
  slug: common-parameter-example
- key_count: 2
  name: Common Point Of Time Example
  slug: common-point-of-time-example
- key_count: 1
  name: Common Point Of Time Offset Example
  slug: common-point-of-time-offset-example
- key_count: 1
  name: Common Point Of Time Statement Example
  slug: common-point-of-time-statement-example
- key_count: 1
  name: Common Point Of Time Timestamp Example
  slug: common-point-of-time-timestamp-example
- key_count: 3
  name: Common Success Accepted Response Example
  slug: common-success-accepted-response-example
- key_count: 1
  name: Common Success Response Example
  slug: common-success-response-example
- key_count: 1
  name: Common Target Lag Example
  slug: common-target-lag-example
- key_count: 1
  name: Common User Defined Lag Example
  slug: common-user-defined-lag-example
- key_count: 21
  name: Compute Pool Compute Pool Example
  slug: compute-pool-compute-pool-example
- key_count: 0
  name: Cortex Analyst Confidence Example
  slug: cortex-analyst-confidence-example
- key_count: 2
  name: Cortex Analyst Generate Verified Query Suggestions Request Example
  slug: cortex-analyst-generate-verified-query-suggestions-request-example
- key_count: 3
  name: Cortex Analyst Generate Verified Query Suggestions Response Example
  slug: cortex-analyst-generate-verified-query-suggestions-response-example
- key_count: 0
  name: Cortex Analyst Message Content Chart Object Example
  slug: cortex-analyst-message-content-chart-object-example
- key_count: 2
  name: Cortex Analyst Message Content Delta Example
  slug: cortex-analyst-message-content-delta-example
- key_count: 0
  name: Cortex Analyst Message Content Delta Sql Object Example
  slug: cortex-analyst-message-content-delta-sql-object-example
- key_count: 0
  name: Cortex Analyst Message Content Delta Suggestions Object Example
  slug: cortex-analyst-message-content-delta-suggestions-object-example
- key_count: 0
  name: Cortex Analyst Message Content Delta Text Object Example
  slug: cortex-analyst-message-content-delta-text-object-example
- key_count: 1
  name: Cortex Analyst Message Content Example
  slug: cortex-analyst-message-content-example
- key_count: 0
  name: Cortex Analyst Message Content Results Object Example
  slug: cortex-analyst-message-content-results-object-example
- key_count: 0
  name: Cortex Analyst Message Content Sql Object Example
  slug: cortex-analyst-message-content-sql-object-example
- key_count: 0
  name: Cortex Analyst Message Content Suggestions Object Example
  slug: cortex-analyst-message-content-suggestions-object-example
- key_count: 0
  name: Cortex Analyst Message Content Text Object Example
  slug: cortex-analyst-message-content-text-object-example
- key_count: 2
  name: Cortex Analyst Message Object Example
  slug: cortex-analyst-message-object-example
- key_count: 3
  name: Cortex Analyst Semantic Model Object Example
  slug: cortex-analyst-semantic-model-object-example
- key_count: 1
  name: Cortex Analyst Semantic Model Selection Example
  slug: cortex-analyst-semantic-model-selection-example
- key_count: 3
  name: Cortex Analyst Send Feedback Request Example
  slug: cortex-analyst-send-feedback-request-example
- key_count: 10
  name: Cortex Analyst Send Message Request Example
  slug: cortex-analyst-send-message-request-example
- key_count: 3
  name: Cortex Analyst Send Message Response Example
  slug: cortex-analyst-send-message-response-example
- key_count: 3
  name: Cortex Analyst Status Update Example
  slug: cortex-analyst-status-update-example
- key_count: 3
  name: Cortex Analyst Streaming Error Example
  slug: cortex-analyst-streaming-error-example
- key_count: 2
  name: Cortex Analyst Suggestion Delta Example
  slug: cortex-analyst-suggestion-delta-example
- key_count: 2
  name: Cortex Analyst Token Info Example
  slug: cortex-analyst-token-info-example
- key_count: 5
  name: Cortex Analyst Verified Query Example
  slug: cortex-analyst-verified-query-example
- key_count: 1
  name: Cortex Analyst Verified Query Suggestion Example
  slug: cortex-analyst-verified-query-suggestion-example
- key_count: 1
  name: Cortex Analyst Warning Example
  slug: cortex-analyst-warning-example
- key_count: 1
  name: Cortex Analyst Warnings Example
  slug: cortex-analyst-warnings-example
- key_count: 13
  name: Cortex Inference Complete Request Example
  slug: cortex-inference-complete-request-example
- key_count: 1
  name: Cortex Inference Get Models Request Example
  slug: cortex-inference-get-models-request-example
- key_count: 1
  name: Cortex Inference Get Models Response Example
  slug: cortex-inference-get-models-response-example
- key_count: 2
  name: Cortex Inference Guardrails Config Example
  slug: cortex-inference-guardrails-config-example
- key_count: 2
  name: Cortex Inference Non Streaming Complete Response Example
  slug: cortex-inference-non-streaming-complete-response-example
- key_count: 1
  name: Cortex Inference Streaming Complete Response Data Event Example
  slug: cortex-inference-streaming-complete-response-data-event-example
- key_count: 0
  name: Cortex Inference Streaming Complete Response Delta Example
  slug: cortex-inference-streaming-complete-response-delta-example
- key_count: 0
  name: Cortex Inference Streaming Complete Response Example
  slug: cortex-inference-streaming-complete-response-example
- key_count: 0
  name: Cortex Search Service Column Example
  slug: cortex-search-service-column-example
- key_count: 2
  name: Cortex Search Service Column Query Example
  slug: cortex-search-service-column-query-example
- key_count: 14
  name: Cortex Search Service Cortex Search Service Example
  slug: cortex-search-service-cortex-search-service-example
- key_count: 5
  name: Cortex Search Service Functions Example
  slug: cortex-search-service-functions-example
- key_count: 1
  name: Cortex Search Service Numeric Boost Example
  slug: cortex-search-service-numeric-boost-example
- key_count: 6
  name: Cortex Search Service Query Request Example
  slug: cortex-search-service-query-request-example
- key_count: 2
  name: Cortex Search Service Query Response Example
  slug: cortex-search-service-query-response-example
- key_count: 3
  name: Cortex Search Service Query Similarity Boost Example
  slug: cortex-search-service-query-similarity-boost-example
- key_count: 0
  name: Cortex Search Service Reranker Example
  slug: cortex-search-service-reranker-example
- key_count: 0
  name: Cortex Search Service Scheduling State Example
  slug: cortex-search-service-scheduling-state-example
- key_count: 0
  name: Cortex Search Service Scoring Config Example
  slug: cortex-search-service-scoring-config-example
- key_count: 1
  name: Cortex Search Service Text Boost Example
  slug: cortex-search-service-text-boost-example
- key_count: 3
  name: Cortex Search Service Time Decay Example
  slug: cortex-search-service-time-decay-example
- key_count: 1
  name: Cortex Search Service Vector Boost Example
  slug: cortex-search-service-vector-boost-example
- key_count: 3
  name: Cortex Search Service Weights Example
  slug: cortex-search-service-weights-example
- key_count: 1
  name: Database Account Identifiers Example
  slug: database-account-identifiers-example
- key_count: 0
  name: Database Database Clone Example
  slug: database-database-clone-example
- key_count: 22
  name: Database Database Example
  slug: database-database-example
- key_count: 0
  name: Database Database From Share Example
  slug: database-database-from-share-example
- key_count: 2
  name: Database Role Containing Scope Example
  slug: database-role-containing-scope-example
- key_count: 1
  name: Database Role Database Role Clone Example
  slug: database-role-database-role-clone-example
- key_count: 8
  name: Database Role Database Role Example
  slug: database-role-database-role-example
- key_count: 5
  name: Database Role Grant Example
  slug: database-role-grant-example
- key_count: 4
  name: Database Role Securable Example
  slug: database-role-securable-example
- key_count: 2
  name: Dynamic Table Dynamic Table Clone Example
  slug: dynamic-table-dynamic-table-clone-example
- key_count: 3
  name: Dynamic Table Dynamic Table Column Example
  slug: dynamic-table-dynamic-table-column-example
- key_count: 21
  name: Dynamic Table Dynamic Table Example
  slug: dynamic-table-dynamic-table-example
- key_count: 9
  name: Event Table Event Table Column Example
  slug: event-table-event-table-column-example
- key_count: 19
  name: Event Table Event Table Example
  slug: event-table-event-table-example
- key_count: 2
  name: External Volume Encryption Example
  slug: external-volume-encryption-example
- key_count: 7
  name: External Volume External Volume Example
  slug: external-volume-external-volume-example
- key_count: 2
  name: External Volume Storage Location Azure Example
  slug: external-volume-storage-location-azure-example
- key_count: 2
  name: External Volume Storage Location Example
  slug: external-volume-storage-location-example
- key_count: 1
  name: External Volume Storage Location Gcs Example
  slug: external-volume-storage-location-gcs-example
- key_count: 3
  name: External Volume Storage Location S3 Example
  slug: external-volume-storage-location-s3-example
- key_count: 3
  name: External Volume Storage Location S3 Gov Example
  slug: external-volume-storage-location-s3-gov-example
- key_count: 3
  name: Function Function Argument Example
  slug: function-function-argument-example
- key_count: 0
  name: Function Function Arguments Example
  slug: function-function-arguments-example
- key_count: 9
  name: Function Function Example
  slug: function-function-example
- key_count: 2
  name: Function Service Function Example
  slug: function-service-function-example
- key_count: 9
  name: Grant Grant Example
  slug: grant-grant-example
- key_count: 3
  name: Iceberg Table Constraint Example
  slug: iceberg-table-constraint-example
- key_count: 2
  name: Iceberg Table Convert To Managed Iceberg Table Request Example
  slug: iceberg-table-convert-to-managed-iceberg-table-request-example
- key_count: 2
  name: Iceberg Table Foreign Key Example
  slug: iceberg-table-foreign-key-example
- key_count: 6
  name: Iceberg Table Iceberg Table As Select Example
  slug: iceberg-table-iceberg-table-as-select-example
- key_count: 1
  name: Iceberg Table Iceberg Table Clone Example
  slug: iceberg-table-iceberg-table-clone-example
- key_count: 5
  name: Iceberg Table Iceberg Table Column Example
  slug: iceberg-table-iceberg-table-column-example
- key_count: 25
  name: Iceberg Table Iceberg Table Example
  slug: iceberg-table-iceberg-table-example
- key_count: 8
  name: Iceberg Table Iceberg Table From Aws Glue Catalog Example
  slug: iceberg-table-iceberg-table-from-aws-glue-catalog-example
- key_count: 6
  name: Iceberg Table Iceberg Table From Delta Example
  slug: iceberg-table-iceberg-table-from-delta-example
- key_count: 6
  name: Iceberg Table Iceberg Table From Iceberg Files Example
  slug: iceberg-table-iceberg-table-from-iceberg-files-example
- key_count: 8
  name: Iceberg Table Iceberg Table From Iceberg Rest Example
  slug: iceberg-table-iceberg-table-from-iceberg-rest-example
- key_count: 5
  name: Iceberg Table Iceberg Table Like Example
  slug: iceberg-table-iceberg-table-like-example
- key_count: 0
  name: Iceberg Table Primary Key Example
  slug: iceberg-table-primary-key-example
- key_count: 1
  name: Iceberg Table Refresh Iceberg Table Request Example
  slug: iceberg-table-refresh-iceberg-table-request-example
- key_count: 0
  name: Iceberg Table Unique Key Example
  slug: iceberg-table-unique-key-example
- key_count: 5
  name: Image Repository Image Example
  slug: image-repository-image-example
- key_count: 4
  name: Image Repository Image Repository Example
  slug: image-repository-image-repository-example
- key_count: 10
  name: Managed Account Managed Account Example
  slug: managed-account-managed-account-example
- key_count: 9
  name: Network Policy Network Policy Example
  slug: network-policy-network-policy-example
- key_count: 24
  name: Notebook Notebook Example
  slug: notebook-notebook-example
- key_count: 5
  name: Notebook Version Details Example
  slug: notebook-version-details-example
- key_count: 3
  name: Notification Integration Notification Email Example
  slug: notification-integration-notification-email-example
- key_count: 1
  name: Notification Integration Notification Hook Example
  slug: notification-integration-notification-hook-example
- key_count: 4
  name: Notification Integration Notification Integration Example
  slug: notification-integration-notification-integration-example
- key_count: 4
  name: Notification Integration Notification Queue Aws Sns Outbound Example
  slug: notification-integration-notification-queue-aws-sns-outbound-example
- key_count: 4
  name: Notification Integration Notification Queue Azure Event Grid Inbound Example
  slug: notification-integration-notification-queue-azure-event-grid-inbound-example
- key_count: 4
  name: Notification Integration Notification Queue Azure Event Grid Outbound Example
  slug: notification-integration-notification-queue-azure-event-grid-outbound-example
- key_count: 2
  name: Notification Integration Notification Queue Gcp Pubsub Inbound Example
  slug: notification-integration-notification-queue-gcp-pubsub-inbound-example
- key_count: 2
  name: Notification Integration Notification Queue Gcp Pubsub Outbound Example
  slug: notification-integration-notification-queue-gcp-pubsub-outbound-example
- key_count: 3
  name: Notification Integration Notification Webhook Example
  slug: notification-integration-notification-webhook-example
- key_count: 3
  name: Notification Integration Webhook Secret Example
  slug: notification-integration-webhook-secret-example
- key_count: 15
  name: Pipe Pipe Example
  slug: pipe-pipe-example
- key_count: 3
  name: Procedure Argument Example
  slug: procedure-argument-example
- key_count: 4
  name: Procedure Base Language Example
  slug: procedure-base-language-example
- key_count: 3
  name: Procedure Call Argument Example
  slug: procedure-call-argument-example
- key_count: 1
  name: Procedure Call Argument List Example
  slug: procedure-call-argument-list-example
- key_count: 2
  name: Procedure Column Type Example
  slug: procedure-column-type-example
- key_count: 2
  name: Procedure Function Language Example
  slug: procedure-function-language-example
- key_count: 3
  name: Procedure Java Function Example
  slug: procedure-java-function-example
- key_count: 0
  name: Procedure Java Script Function Example
  slug: procedure-java-script-function-example
- key_count: 14
  name: Procedure Procedure Example
  slug: procedure-procedure-example
- key_count: 2
  name: Procedure Python Function Example
  slug: procedure-python-function-example
- key_count: 2
  name: Procedure Return Data Type Example
  slug: procedure-return-data-type-example
- key_count: 1
  name: Procedure Return Table Example
  slug: procedure-return-table-example
- key_count: 1
  name: Procedure Return Type Example
  slug: procedure-return-type-example
- key_count: 1
  name: Procedure Scala Function Example
  slug: procedure-scala-function-example
- key_count: 0
  name: Procedure Sql Function Example
  slug: procedure-sql-function-example
- key_count: 2
  name: Role Containing Scope Example
  slug: role-containing-scope-example
- key_count: 5
  name: Role Grant Example
  slug: role-grant-example
- key_count: 5
  name: Role Grant Of Example
  slug: role-grant-of-example
- key_count: 9
  name: Role Grant On Example
  slug: role-grant-on-example
- key_count: 10
  name: Role Role Example
  slug: role-role-example
- key_count: 4
  name: Role Securable Example
  slug: role-securable-example
- key_count: 0
  name: Schema Schema Clone Example
  slug: schema-schema-clone-example
- key_count: 24
  name: Schema Schema Example
  slug: schema-schema-example
- key_count: 5
  name: Service Grant Of Example
  slug: service-grant-of-example
- key_count: 5
  name: Service Job Service Example
  slug: service-job-service-example
- key_count: 10
  name: Service Service Container Example
  slug: service-service-container-example
- key_count: 6
  name: Service Service Endpoint Example
  slug: service-service-endpoint-example
- key_count: 0
  name: Service Service Example
  slug: service-service-example
- key_count: 6
  name: Service Service Instance Example
  slug: service-service-instance-example
- key_count: 3
  name: Service Service Role Example
  slug: service-service-role-example
- key_count: 6
  name: Service Service Role Grant To Example
  slug: service-service-role-grant-to-example
- key_count: 1
  name: Service Service Spec Example
  slug: service-service-spec-example
- key_count: 1
  name: Service Service Spec Inline Text Example
  slug: service-service-spec-inline-text-example
- key_count: 2
  name: Service Service Spec Stage File Example
  slug: service-service-spec-stage-file-example
- key_count: 6
  name: Snowflake Callprocedure Example
  slug: snowflake-callprocedure-example
- key_count: 6
  name: Snowflake Cancelstatement Example
  slug: snowflake-cancelstatement-example
- key_count: 6
  name: Snowflake Clonealert Example
  slug: snowflake-clonealert-example
- key_count: 6
  name: Snowflake Clonedatabase Example
  slug: snowflake-clonedatabase-example
- key_count: 6
  name: Snowflake Clonedatabaserole Example
  slug: snowflake-clonedatabaserole-example
- key_count: 6
  name: Snowflake Clonedynamictable Example
  slug: snowflake-clonedynamictable-example
- key_count: 6
  name: Snowflake Cloneschema Example
  slug: snowflake-cloneschema-example
- key_count: 6
  name: Snowflake Clonesnowflakemanagedicebergtable Example
  slug: snowflake-clonesnowflakemanagedicebergtable-example
- key_count: 6
  name: Snowflake Clonestream Example
  slug: snowflake-clonestream-example
- key_count: 6
  name: Snowflake Clonetable Example
  slug: snowflake-clonetable-example
- key_count: 6
  name: Snowflake Converttomanagedicebergtable Example
  slug: snowflake-converttomanagedicebergtable-example
- key_count: 6
  name: Snowflake Cortexllminferencecomplete Example
  slug: snowflake-cortexllminferencecomplete-example
- key_count: 6
  name: Snowflake Createaccount Example
  slug: snowflake-createaccount-example
- key_count: 6
  name: Snowflake Createalert Example
  slug: snowflake-createalert-example
- key_count: 6
  name: Snowflake Createapiintegration Example
  slug: snowflake-createapiintegration-example
- key_count: 6
  name: Snowflake Createcatalogintegration Example
  slug: snowflake-createcatalogintegration-example
- key_count: 6
  name: Snowflake Createcomputepool Example
  slug: snowflake-createcomputepool-example
- key_count: 6
  name: Snowflake Createcortexsearchservice Example
  slug: snowflake-createcortexsearchservice-example
- key_count: 6
  name: Snowflake Createdatabase Example
  slug: snowflake-createdatabase-example
- key_count: 6
  name: Snowflake Createdatabasefromshare Example
  slug: snowflake-createdatabasefromshare-example
- key_count: 6
  name: Snowflake Createdatabaserole Example
  slug: snowflake-createdatabaserole-example
- key_count: 6
  name: Snowflake Createdynamictable Example
  slug: snowflake-createdynamictable-example
- key_count: 6
  name: Snowflake Createeventtable Example
  slug: snowflake-createeventtable-example
- key_count: 6
  name: Snowflake Createexternalvolume Example
  slug: snowflake-createexternalvolume-example
- key_count: 6
  name: Snowflake Createfunction Example
  slug: snowflake-createfunction-example
- key_count: 6
  name: Snowflake Createimagerepository Example
  slug: snowflake-createimagerepository-example
- key_count: 6
  name: Snowflake Createmanagedaccount Example
  slug: snowflake-createmanagedaccount-example
- key_count: 6
  name: Snowflake Createnetworkpolicy Example
  slug: snowflake-createnetworkpolicy-example
- key_count: 6
  name: Snowflake Createnotebook Example
  slug: snowflake-createnotebook-example
- key_count: 6
  name: Snowflake Createnotificationintegration Example
  slug: snowflake-createnotificationintegration-example
- key_count: 6
  name: Snowflake Createoralterapiintegration Example
  slug: snowflake-createoralterapiintegration-example
- key_count: 6
  name: Snowflake Createoraltercomputepool Example
  slug: snowflake-createoraltercomputepool-example
- key_count: 6
  name: Snowflake Createoralterdatabase Example
  slug: snowflake-createoralterdatabase-example
- key_count: 6
  name: Snowflake Createoralterschema Example
  slug: snowflake-createoralterschema-example
- key_count: 6
  name: Snowflake Createoralterservice Example
  slug: snowflake-createoralterservice-example
- key_count: 6
  name: Snowflake Createoraltertable Example
  slug: snowflake-createoraltertable-example
- key_count: 6
  name: Snowflake Createoraltertask Example
  slug: snowflake-createoraltertask-example
- key_count: 6
  name: Snowflake Createoralteruser Example
  slug: snowflake-createoralteruser-example
- key_count: 6
  name: Snowflake Createoralterwarehouse Example
  slug: snowflake-createoralterwarehouse-example
- key_count: 6
  name: Snowflake Createpipe Example
  slug: snowflake-createpipe-example
- key_count: 6
  name: Snowflake Createprocedure Example
  slug: snowflake-createprocedure-example
- key_count: 6
  name: Snowflake Createrole Example
  slug: snowflake-createrole-example
- key_count: 6
  name: Snowflake Createschema Example
  slug: snowflake-createschema-example
- key_count: 6
  name: Snowflake Createservice Example
  slug: snowflake-createservice-example
- key_count: 6
  name: Snowflake Createsnowflakemanagedicebergtable Example
  slug: snowflake-createsnowflakemanagedicebergtable-example
- key_count: 6
  name: Snowflake Createsnowflakemanagedicebergtableasselect Example
  slug: snowflake-createsnowflakemanagedicebergtableasselect-example
- key_count: 6
  name: Snowflake Createsnowflakemanagedicebergtablelike Example
  slug: snowflake-createsnowflakemanagedicebergtablelike-example
- key_count: 6
  name: Snowflake Createstage Example
  slug: snowflake-createstage-example
- key_count: 6
  name: Snowflake Createstream Example
  slug: snowflake-createstream-example
- key_count: 6
  name: Snowflake Createtable Example
  slug: snowflake-createtable-example
- key_count: 6
  name: Snowflake Createtableasselect Example
  slug: snowflake-createtableasselect-example
- key_count: 6
  name: Snowflake Createtableasselectdeprecated Example
  slug: snowflake-createtableasselectdeprecated-example
- key_count: 6
  name: Snowflake Createtablelike Example
  slug: snowflake-createtablelike-example
- key_count: 6
  name: Snowflake Createtableusingtemplate Example
  slug: snowflake-createtableusingtemplate-example
- key_count: 6
  name: Snowflake Createtask Example
  slug: snowflake-createtask-example
- key_count: 6
  name: Snowflake Createunmanagedicebergtablefromawsgluecatalog Example
  slug: snowflake-createunmanagedicebergtablefromawsgluecatalog-example
- key_count: 6
  name: Snowflake Createunmanagedicebergtablefromdelta Example
  slug: snowflake-createunmanagedicebergtablefromdelta-example
- key_count: 6
  name: Snowflake Createunmanagedicebergtablefromicebergfiles Example
  slug: snowflake-createunmanagedicebergtablefromicebergfiles-example
- key_count: 6
  name: Snowflake Createunmanagedicebergtablefromicebergrest Example
  slug: snowflake-createunmanagedicebergtablefromicebergrest-example
- key_count: 6
  name: Snowflake Createuser Example
  slug: snowflake-createuser-example
- key_count: 6
  name: Snowflake Createuserdefinedfunction Example
  slug: snowflake-createuserdefinedfunction-example
- key_count: 6
  name: Snowflake Createview Example
  slug: snowflake-createview-example
- key_count: 6
  name: Snowflake Createwarehouse Example
  slug: snowflake-createwarehouse-example
- key_count: 6
  name: Snowflake Disabledatabasefailover Example
  slug: snowflake-disabledatabasefailover-example
- key_count: 6
  name: Snowflake Disabledatabasereplication Example
  slug: snowflake-disabledatabasereplication-example
- key_count: 6
  name: Snowflake Enabledatabasefailover Example
  slug: snowflake-enabledatabasefailover-example
- key_count: 6
  name: Snowflake Enabledatabasereplication Example
  slug: snowflake-enabledatabasereplication-example
- key_count: 6
  name: Snowflake Executefunction Example
  slug: snowflake-executefunction-example
- key_count: 6
  name: Snowflake Executejobservice Example
  slug: snowflake-executejobservice-example
- key_count: 6
  name: Snowflake Fetchalert Example
  slug: snowflake-fetchalert-example
- key_count: 6
  name: Snowflake Fetchapiintegration Example
  slug: snowflake-fetchapiintegration-example
- key_count: 6
  name: Snowflake Fetchcatalogintegration Example
  slug: snowflake-fetchcatalogintegration-example
- key_count: 6
  name: Snowflake Fetchcomputepool Example
  slug: snowflake-fetchcomputepool-example
- key_count: 6
  name: Snowflake Fetchcortexsearchservice Example
  slug: snowflake-fetchcortexsearchservice-example
- key_count: 6
  name: Snowflake Fetchdatabase Example
  slug: snowflake-fetchdatabase-example
- key_count: 6
  name: Snowflake Fetchdynamictable Example
  slug: snowflake-fetchdynamictable-example
- key_count: 6
  name: Snowflake Fetcheventtable Example
  slug: snowflake-fetcheventtable-example
- key_count: 6
  name: Snowflake Fetchexternalvolume Example
  slug: snowflake-fetchexternalvolume-example
- key_count: 6
  name: Snowflake Fetchfunction Example
  slug: snowflake-fetchfunction-example
- key_count: 6
  name: Snowflake Fetchicebergtable Example
  slug: snowflake-fetchicebergtable-example
- key_count: 6
  name: Snowflake Fetchimagerepository Example
  slug: snowflake-fetchimagerepository-example
- key_count: 6
  name: Snowflake Fetchnetworkpolicy Example
  slug: snowflake-fetchnetworkpolicy-example
- key_count: 6
  name: Snowflake Fetchnotebook Example
  slug: snowflake-fetchnotebook-example
- key_count: 6
  name: Snowflake Fetchnotificationintegration Example
  slug: snowflake-fetchnotificationintegration-example
- key_count: 6
  name: Snowflake Fetchpipe Example
  slug: snowflake-fetchpipe-example
- key_count: 6
  name: Snowflake Fetchprocedure Example
  slug: snowflake-fetchprocedure-example
- key_count: 6
  name: Snowflake Fetchresult Example
  slug: snowflake-fetchresult-example
- key_count: 6
  name: Snowflake Fetchschema Example
  slug: snowflake-fetchschema-example
- key_count: 6
  name: Snowflake Fetchservice Example
  slug: snowflake-fetchservice-example
- key_count: 6
  name: Snowflake Fetchservicelogs Example
  slug: snowflake-fetchservicelogs-example
- key_count: 6
  name: Snowflake Fetchservicestatus Example
  slug: snowflake-fetchservicestatus-example
- key_count: 6
  name: Snowflake Fetchstage Example
  slug: snowflake-fetchstage-example
- key_count: 6
  name: Snowflake Fetchstream Example
  slug: snowflake-fetchstream-example
- key_count: 6
  name: Snowflake Fetchtable Example
  slug: snowflake-fetchtable-example
- key_count: 6
  name: Snowflake Fetchtask Example
  slug: snowflake-fetchtask-example
- key_count: 6
  name: Snowflake Fetchtaskdependents Example
  slug: snowflake-fetchtaskdependents-example
- key_count: 6
  name: Snowflake Fetchuser Example
  slug: snowflake-fetchuser-example
- key_count: 6
  name: Snowflake Fetchuserdefinedfunction Example
  slug: snowflake-fetchuserdefinedfunction-example
- key_count: 6
  name: Snowflake Fetchview Example
  slug: snowflake-fetchview-example
- key_count: 6
  name: Snowflake Fetchwarehouse Example
  slug: snowflake-fetchwarehouse-example
- key_count: 6
  name: Snowflake Generateverifiedquerysuggestions Example
  slug: snowflake-generateverifiedquerysuggestions-example
- key_count: 6
  name: Snowflake Getcompletegraphs Example
  slug: snowflake-getcompletegraphs-example
- key_count: 6
  name: Snowflake Getcompletegraphsdeprecated Example
  slug: snowflake-getcompletegraphsdeprecated-example
- key_count: 6
  name: Snowflake Getcurrentgraphs Example
  slug: snowflake-getcurrentgraphs-example
- key_count: 6
  name: Snowflake Getcurrentgraphsdeprecated Example
  slug: snowflake-getcurrentgraphsdeprecated-example
- key_count: 6
  name: Snowflake Getmodels Example
  slug: snowflake-getmodels-example
- key_count: 6
  name: Snowflake Getpresignedurl Example
  slug: snowflake-getpresignedurl-example
- key_count: 6
  name: Snowflake Getscopedtoken Example
  slug: snowflake-getscopedtoken-example
- key_count: 6
  name: Snowflake Getstatementstatus Example
  slug: snowflake-getstatementstatus-example
- key_count: 6
  name: Snowflake Grant Example
  slug: snowflake-grant-example
- key_count: 6
  name: Snowflake Grantfutureprivileges Example
  slug: snowflake-grantfutureprivileges-example
- key_count: 6
  name: Snowflake Grantgroupprivilege Example
  slug: snowflake-grantgroupprivilege-example
- key_count: 6
  name: Snowflake Grantprivilege Example
  slug: snowflake-grantprivilege-example
- key_count: 6
  name: Snowflake Grantprivileges Example
  slug: snowflake-grantprivileges-example
- key_count: 6
  name: Snowflake Listaccounts Example
  slug: snowflake-listaccounts-example
- key_count: 6
  name: Snowflake Listalerts Example
  slug: snowflake-listalerts-example
- key_count: 6
  name: Snowflake Listapiintegrations Example
  slug: snowflake-listapiintegrations-example
- key_count: 6
  name: Snowflake Listcatalogintegrations Example
  slug: snowflake-listcatalogintegrations-example
- key_count: 6
  name: Snowflake Listcomputepools Example
  slug: snowflake-listcomputepools-example
- key_count: 6
  name: Snowflake Listcortexsearchservices Example
  slug: snowflake-listcortexsearchservices-example
- key_count: 6
  name: Snowflake Listdatabaseroles Example
  slug: snowflake-listdatabaseroles-example
- key_count: 6
  name: Snowflake Listdatabases Example
  slug: snowflake-listdatabases-example
- key_count: 6
  name: Snowflake Listdynamictables Example
  slug: snowflake-listdynamictables-example
- key_count: 6
  name: Snowflake Listeventtables Example
  slug: snowflake-listeventtables-example
- key_count: 6
  name: Snowflake Listexternalvolumes Example
  slug: snowflake-listexternalvolumes-example
- key_count: 6
  name: Snowflake Listfiles Example
  slug: snowflake-listfiles-example
- key_count: 6
  name: Snowflake Listfunctions Example
  slug: snowflake-listfunctions-example
- key_count: 6
  name: Snowflake Listfuturegrants Example
  slug: snowflake-listfuturegrants-example
- key_count: 6
  name: Snowflake Listgrants Example
  slug: snowflake-listgrants-example
- key_count: 6
  name: Snowflake Listgrantsof Example
  slug: snowflake-listgrantsof-example
- key_count: 6
  name: Snowflake Listgrantson Example
  slug: snowflake-listgrantson-example
- key_count: 6
  name: Snowflake Listgrantsto Example
  slug: snowflake-listgrantsto-example
- key_count: 6
  name: Snowflake Listicebergtables Example
  slug: snowflake-listicebergtables-example
- key_count: 6
  name: Snowflake Listimagerepositories Example
  slug: snowflake-listimagerepositories-example
- key_count: 6
  name: Snowflake Listimagesinrepository Example
  slug: snowflake-listimagesinrepository-example
- key_count: 6
  name: Snowflake Listmanagedaccounts Example
  slug: snowflake-listmanagedaccounts-example
- key_count: 6
  name: Snowflake Listnetworkpolicies Example
  slug: snowflake-listnetworkpolicies-example
- key_count: 6
  name: Snowflake Listnotebooks Example
  slug: snowflake-listnotebooks-example
- key_count: 6
  name: Snowflake Listnotificationintegrations Example
  slug: snowflake-listnotificationintegrations-example
- key_count: 6
  name: Snowflake Listpipes Example
  slug: snowflake-listpipes-example
- key_count: 6
  name: Snowflake Listprocedures Example
  slug: snowflake-listprocedures-example
- key_count: 6
  name: Snowflake Listroles Example
  slug: snowflake-listroles-example
- key_count: 6
  name: Snowflake Listschemas Example
  slug: snowflake-listschemas-example
- key_count: 6
  name: Snowflake Listservicecontainers Example
  slug: snowflake-listservicecontainers-example
- key_count: 6
  name: Snowflake Listserviceinstances Example
  slug: snowflake-listserviceinstances-example
- key_count: 6
  name: Snowflake Listservicerolegrantsof Example
  slug: snowflake-listservicerolegrantsof-example
- key_count: 6
  name: Snowflake Listservicerolegrantsto Example
  slug: snowflake-listservicerolegrantsto-example
- key_count: 6
  name: Snowflake Listserviceroles Example
  slug: snowflake-listserviceroles-example
- key_count: 6
  name: Snowflake Listservices Example
  slug: snowflake-listservices-example
- key_count: 6
  name: Snowflake Liststages Example
  slug: snowflake-liststages-example
- key_count: 6
  name: Snowflake Liststreams Example
  slug: snowflake-liststreams-example
- key_count: 6
  name: Snowflake Listtables Example
  slug: snowflake-listtables-example
- key_count: 6
  name: Snowflake Listtasks Example
  slug: snowflake-listtasks-example
- key_count: 6
  name: Snowflake Listuserdefinedfunctions Example
  slug: snowflake-listuserdefinedfunctions-example
- key_count: 6
  name: Snowflake Listusers Example
  slug: snowflake-listusers-example
- key_count: 6
  name: Snowflake Listviews Example
  slug: snowflake-listviews-example
- key_count: 6
  name: Snowflake Listwarehouses Example
  slug: snowflake-listwarehouses-example
- key_count: 6
  name: Snowflake Querycortexsearchservice Example
  slug: snowflake-querycortexsearchservice-example
- key_count: 6
  name: Snowflake Refreshicebergtable Example
  slug: snowflake-refreshicebergtable-example
- key_count: 6
  name: Snowflake Renamewarehouse Example
  slug: snowflake-renamewarehouse-example
- key_count: 6
  name: Snowflake Revokefuturegrants Example
  slug: snowflake-revokefuturegrants-example
- key_count: 6
  name: Snowflake Revokegrants Example
  slug: snowflake-revokegrants-example
- key_count: 6
  name: Snowflake Sendfeedback Example
  slug: snowflake-sendfeedback-example
- key_count: 6
  name: Snowflake Sendmessage Example
  slug: snowflake-sendmessage-example
- key_count: 6
  name: Snowflake Showserviceendpoints Example
  slug: snowflake-showserviceendpoints-example
- key_count: 2
  name: Snowflake Sql Rest Bind Variable Example
  slug: snowflake-sql-rest-bind-variable-example
- key_count: 5
  name: Snowflake Sql Rest Cancel Status Example
  slug: snowflake-sql-rest-cancel-status-example
- key_count: 6
  name: Snowflake Sql Rest Column Definition Example
  slug: snowflake-sql-rest-column-definition-example
- key_count: 4
  name: Snowflake Sql Rest Execution Stats Example
  slug: snowflake-sql-rest-execution-stats-example
- key_count: 3
  name: Snowflake Sql Rest Partition Info Example
  slug: snowflake-sql-rest-partition-info-example
- key_count: 6
  name: Snowflake Sql Rest Query Failure Status Example
  slug: snowflake-sql-rest-query-failure-status-example
- key_count: 6
  name: Snowflake Sql Rest Query Status Example
  slug: snowflake-sql-rest-query-status-example
- key_count: 7
  name: Snowflake Sql Rest Result Set Example
  slug: snowflake-sql-rest-result-set-example
- key_count: 5
  name: Snowflake Sql Rest Result Set Meta Data Example
  slug: snowflake-sql-rest-result-set-meta-data-example
- key_count: 13
  name: Snowflake Sql Rest Session Parameters Example
  slug: snowflake-sql-rest-session-parameters-example
- key_count: 7
  name: Snowflake Sql Rest Statement Request Example
  slug: snowflake-sql-rest-statement-request-example
- key_count: 6
  name: Snowflake Submitstatement Example
  slug: snowflake-submitstatement-example
- key_count: 5
  name: Sqlapi Cancel Status Example
  slug: sqlapi-cancel-status-example
- key_count: 6
  name: Sqlapi Query Failure Status Example
  slug: sqlapi-query-failure-status-example
- key_count: 6
  name: Sqlapi Query Status Example
  slug: sqlapi-query-status-example
- key_count: 9
  name: Sqlapi Result Set Example
  slug: sqlapi-result-set-example
- key_count: 4
  name: Stage Aws Credentials Example
  slug: stage-aws-credentials-example
- key_count: 1
  name: Stage Azure Credentials Example
  slug: stage-azure-credentials-example
- key_count: 1
  name: Stage Credentials Example
  slug: stage-credentials-example
- key_count: 1
  name: Stage File Transfer Material Example
  slug: stage-file-transfer-material-example
- key_count: 1
  name: Stage Presigned Url Request Example
  slug: stage-presigned-url-request-example
- key_count: 13
  name: Stage Stage Example
  slug: stage-stage-example
- key_count: 4
  name: Stage Stage File Example
  slug: stage-stage-file-example
- key_count: 2
  name: Stream Point Of Time Example
  slug: stream-point-of-time-example
- key_count: 1
  name: Stream Point Of Time Offset Example
  slug: stream-point-of-time-offset-example
- key_count: 1
  name: Stream Point Of Time Statement Example
  slug: stream-point-of-time-statement-example
- key_count: 1
  name: Stream Point Of Time Stream Example
  slug: stream-point-of-time-stream-example
- key_count: 1
  name: Stream Point Of Time Timestamp Example
  slug: stream-point-of-time-timestamp-example
- key_count: 2
  name: Stream Stream Clone Example
  slug: stream-stream-clone-example
- key_count: 13
  name: Stream Stream Example
  slug: stream-stream-example
- key_count: 4
  name: Stream Stream Source Example
  slug: stream-stream-source-example
- key_count: 1
  name: Stream Stream Source External Table Example
  slug: stream-stream-source-external-table-example
- key_count: 0
  name: Stream Stream Source Stage Example
  slug: stream-stream-source-stage-example
- key_count: 2
  name: Stream Stream Source Table Example
  slug: stream-stream-source-table-example
- key_count: 3
  name: Stream Stream Source View Example
  slug: stream-stream-source-view-example
- key_count: 3
  name: Table Constraint Example
  slug: table-constraint-example
- key_count: 2
  name: Table Foreign Key Example
  slug: table-foreign-key-example
- key_count: 0
  name: Table Primary Key Example
  slug: table-primary-key-example
- key_count: 3
  name: Table Table As Select Example
  slug: table-table-as-select-example
- key_count: 0
  name: Table Table Clone Example
  slug: table-table-clone-example
- key_count: 10
  name: Table Table Column Example
  slug: table-table-column-example
- key_count: 25
  name: Table Table Example
  slug: table-table-example
- key_count: 1
  name: Table Table Like Example
  slug: table-table-like-example
- key_count: 1
  name: Table Table Using Template Example
  slug: table-table-using-template-example
- key_count: 0
  name: Table Unique Key Example
  slug: table-unique-key-example
- key_count: 2
  name: Task Cron Schedule Example
  slug: task-cron-schedule-example
- key_count: 1
  name: Task Minutes Schedule Example
  slug: task-minutes-schedule-example
- key_count: 25
  name: Task Task Example
  slug: task-task-example
- key_count: 14
  name: Task Task Run Example
  slug: task-task-run-example
- key_count: 1
  name: Task Task Schedule Example
  slug: task-task-schedule-example
- key_count: 2
  name: User Containing Scope Example
  slug: user-containing-scope-example
- key_count: 3
  name: User Defined Function Argument Example
  slug: user-defined-function-argument-example
- key_count: 3
  name: User Defined Function Base Language Example
  slug: user-defined-function-base-language-example
- key_count: 2
  name: User Defined Function Column Type Example
  slug: user-defined-function-column-type-example
- key_count: 3
  name: User Defined Function Function Language Example
  slug: user-defined-function-function-language-example
- key_count: 4
  name: User Defined Function Java Function Example
  slug: user-defined-function-java-function-example
- key_count: 0
  name: User Defined Function Java Script Function Example
  slug: user-defined-function-java-script-function-example
- key_count: 3
  name: User Defined Function Python Function Example
  slug: user-defined-function-python-function-example
- key_count: 2
  name: User Defined Function Return Data Type Example
  slug: user-defined-function-return-data-type-example
- key_count: 1
  name: User Defined Function Return Table Example
  slug: user-defined-function-return-table-example
- key_count: 1
  name: User Defined Function Return Type Example
  slug: user-defined-function-return-type-example
- key_count: 2
  name: User Defined Function Scala Function Example
  slug: user-defined-function-scala-function-example
- key_count: 0
  name: User Defined Function Sql Function Example
  slug: user-defined-function-sql-function-example
- key_count: 18
  name: User Defined Function User Defined Function Example
  slug: user-defined-function-user-defined-function-example
- key_count: 4
  name: User Grant Example
  slug: user-grant-example
- key_count: 3
  name: User Securable Example
  slug: user-securable-example
- key_count: 40
  name: User User Example
  slug: user-user-example
- key_count: 3
  name: View View Column Example
  slug: view-view-column-example
- key_count: 12
  name: View View Example
  slug: view-view-example
- key_count: 36
  name: Warehouse Warehouse Example
  slug: warehouse-warehouse-example
finops:
- has_sources: true
  method: derived
  name: Snowflake Finops
  primary_unit: ''
  service_category: ''
  slug: snowflake-finops
  template: true
image: https://www.snowflake.com/wp-content/themes/snowflake/assets/img/brand-guidelines/logo-sno-blue-example.svg
json_schemas:
- name: Account
  property_count: 37
  slug: account-account
- name: AlertClone
  property_count: 1
  slug: alert-alert-clone
- name: Alert
  property_count: 11
  slug: alert-alert
- name: CronSchedule
  property_count: 2
  slug: alert-cron-schedule
- name: MinutesSchedule
  property_count: 1
  slug: alert-minutes-schedule
- name: PointOfTimeOffset
  property_count: 1
  slug: alert-point-of-time-offset
- name: PointOfTime
  property_count: 2
  slug: alert-point-of-time
- name: PointOfTimeStatement
  property_count: 1
  slug: alert-point-of-time-statement
- name: PointOfTimeTimestamp
  property_count: 1
  slug: alert-point-of-time-timestamp
- name: Schedule
  property_count: 1
  slug: alert-schedule
- name: ApiHook
  property_count: 1
  slug: api-integration-api-hook
- name: ApiIntegration
  property_count: 6
  slug: api-integration-api-integration
- name: ApiKey
  property_count: 0
  slug: api-integration-api-key
- name: AwsHook
  property_count: 2
  slug: api-integration-aws-hook
- name: AzureHook
  property_count: 3
  slug: api-integration-azure-hook
- name: GitHook
  property_count: 3
  slug: api-integration-git-hook
- name: GoogleCloudHook
  property_count: 2
  slug: api-integration-google-cloud-hook
- name: ArtifactRepository
  property_count: 9
  slug: artifact-repository-artifact-repository
- name: CatalogIntegration
  property_count: 7
  slug: catalog-integration-catalog-integration
- name: Catalog
  property_count: 1
  slug: catalog-integration-catalog
- name: Glue
  property_count: 4
  slug: catalog-integration-glue
- name: OAuth
  property_count: 3
  slug: catalog-integration-o-auth
- name: ObjectStore
  property_count: 0
  slug: catalog-integration-object-store
- name: Polaris
  property_count: 1
  slug: catalog-integration-polaris
- name: RestAuthentication
  property_count: 1
  slug: catalog-integration-rest-authentication
- name: RestConfig
  property_count: 2
  slug: catalog-integration-rest-config
- name: DownstreamLag
  property_count: 0
  slug: common-downstream-lag
- name: ErrorResponse
  property_count: 4
  slug: common-error-response
- name: Identifier
  property_count: 0
  slug: common-identifier
- name: Parameter
  property_count: 6
  slug: common-parameter
- name: PointOfTimeOffset
  property_count: 1
  slug: common-point-of-time-offset
- name: PointOfTime
  property_count: 2
  slug: common-point-of-time
- name: PointOfTimeStatement
  property_count: 1
  slug: common-point-of-time-statement
- name: PointOfTimeTimestamp
  property_count: 1
  slug: common-point-of-time-timestamp
- name: SuccessAcceptedResponse
  property_count: 3
  slug: common-success-accepted-response
- name: SuccessResponse
  property_count: 1
  slug: common-success-response
- name: TargetLag
  property_count: 1
  slug: common-target-lag
- name: UserDefinedLag
  property_count: 1
  slug: common-user-defined-lag
- name: ComputePool
  property_count: 21
  slug: compute-pool-compute-pool
- name: Confidence
  property_count: 0
  slug: cortex-analyst-confidence
- name: GenerateVerifiedQuerySuggestionsRequest
  property_count: 2
  slug: cortex-analyst-generate-verified-query-suggestions-request
- name: GenerateVerifiedQuerySuggestionsResponse
  property_count: 3
  slug: cortex-analyst-generate-verified-query-suggestions-response
- name: MessageContentChartObject
  property_count: 0
  slug: cortex-analyst-message-content-chart-object
- name: MessageContentDelta
  property_count: 2
  slug: cortex-analyst-message-content-delta
- name: MessageContentDeltaSqlObject
  property_count: 0
  slug: cortex-analyst-message-content-delta-sql-object
- name: MessageContentDeltaSuggestionsObject
  property_count: 0
  slug: cortex-analyst-message-content-delta-suggestions-object
- name: MessageContentDeltaTextObject
  property_count: 0
  slug: cortex-analyst-message-content-delta-text-object
- name: MessageContentResultsObject
  property_count: 0
  slug: cortex-analyst-message-content-results-object
- name: MessageContent
  property_count: 1
  slug: cortex-analyst-message-content
- name: MessageContentSqlObject
  property_count: 0
  slug: cortex-analyst-message-content-sql-object
- name: MessageContentSuggestionsObject
  property_count: 0
  slug: cortex-analyst-message-content-suggestions-object
- name: MessageContentTextObject
  property_count: 0
  slug: cortex-analyst-message-content-text-object
- name: MessageObject
  property_count: 2
  slug: cortex-analyst-message-object
- name: SemanticModelObject
  property_count: 3
  slug: cortex-analyst-semantic-model-object
- name: SemanticModelSelection
  property_count: 1
  slug: cortex-analyst-semantic-model-selection
- name: SendFeedbackRequest
  property_count: 3
  slug: cortex-analyst-send-feedback-request
- name: SendMessageRequest
  property_count: 10
  slug: cortex-analyst-send-message-request
- name: SendMessageResponse
  property_count: 3
  slug: cortex-analyst-send-message-response
- name: StatusUpdate
  property_count: 3
  slug: cortex-analyst-status-update
- name: StreamingError
  property_count: 3
  slug: cortex-analyst-streaming-error
- name: SuggestionDelta
  property_count: 2
  slug: cortex-analyst-suggestion-delta
- name: TokenInfo
  property_count: 2
  slug: cortex-analyst-token-info
- name: VerifiedQuery
  property_count: 5
  slug: cortex-analyst-verified-query
- name: VerifiedQuerySuggestion
  property_count: 1
  slug: cortex-analyst-verified-query-suggestion
- name: Warning
  property_count: 1
  slug: cortex-analyst-warning
- name: Warnings
  property_count: 1
  slug: cortex-analyst-warnings
- name: EmbedRequest
  property_count: 3
  slug: cortex-embed-embed-request
- name: EmbedResponse
  property_count: 4
  slug: cortex-embed-embed-response
- name: CompleteRequest
  property_count: 13
  slug: cortex-inference-complete-request
- name: GetModelsRequest
  property_count: 1
  slug: cortex-inference-get-models-request
- name: GetModelsResponse
  property_count: 1
  slug: cortex-inference-get-models-response
- name: GuardrailsConfig
  property_count: 2
  slug: cortex-inference-guardrails-config
- name: NonStreamingCompleteResponse
  property_count: 2
  slug: cortex-inference-non-streaming-complete-response
- name: StreamingCompleteResponseDataEvent
  property_count: 1
  slug: cortex-inference-streaming-complete-response-data-event
- name: StreamingCompleteResponseDelta
  property_count: 0
  slug: cortex-inference-streaming-complete-response-delta
- name: StreamingCompleteResponse
  property_count: 0
  slug: cortex-inference-streaming-complete-response
- name: ColumnQuery
  property_count: 2
  slug: cortex-search-service-column-query
- name: Column
  property_count: 0
  slug: cortex-search-service-column
- name: CortexSearchService
  property_count: 14
  slug: cortex-search-service-cortex-search-service
- name: Functions
  property_count: 5
  slug: cortex-search-service-functions
- name: NumericBoost
  property_count: 1
  slug: cortex-search-service-numeric-boost
- name: QueryRequest
  property_count: 6
  slug: cortex-search-service-query-request
- name: QueryResponse
  property_count: 2
  slug: cortex-search-service-query-response
- name: QuerySimilarityBoost
  property_count: 3
  slug: cortex-search-service-query-similarity-boost
- name: Reranker
  property_count: 0
  slug: cortex-search-service-reranker
- name: SchedulingState
  property_count: 0
  slug: cortex-search-service-scheduling-state
- name: ScoringConfig
  property_count: 0
  slug: cortex-search-service-scoring-config
- name: TextBoost
  property_count: 1
  slug: cortex-search-service-text-boost
- name: TimeDecay
  property_count: 3
  slug: cortex-search-service-time-decay
- name: VectorBoost
  property_count: 1
  slug: cortex-search-service-vector-boost
- name: Weights
  property_count: 3
  slug: cortex-search-service-weights
- name: AccountIdentifiers
  property_count: 1
  slug: database-account-identifiers
- name: DatabaseClone
  property_count: 0
  slug: database-database-clone
- name: DatabaseFromShare
  property_count: 0
  slug: database-database-from-share
- name: Database
  property_count: 22
  slug: database-database
- name: ContainingScope
  property_count: 2
  slug: database-role-containing-scope
- name: DatabaseRoleClone
  property_count: 1
  slug: database-role-database-role-clone
- name: DatabaseRole
  property_count: 8
  slug: database-role-database-role
- name: Grant
  property_count: 5
  slug: database-role-grant
- name: Securable
  property_count: 4
  slug: database-role-securable
- name: DynamicTableClone
  property_count: 2
  slug: dynamic-table-dynamic-table-clone
- name: DynamicTableColumn
  property_count: 3
  slug: dynamic-table-dynamic-table-column
- name: DynamicTable
  property_count: 21
  slug: dynamic-table-dynamic-table
- name: EventTableColumn
  property_count: 9
  slug: event-table-event-table-column
- name: EventTable
  property_count: 19
  slug: event-table-event-table
- name: Encryption
  property_count: 2
  slug: external-volume-encryption
- name: ExternalVolume
  property_count: 7
  slug: external-volume-external-volume
- name: StorageLocationAzure
  property_count: 2
  slug: external-volume-storage-location-azure
- name: StorageLocationGcs
  property_count: 1
  slug: external-volume-storage-location-gcs
- name: StorageLocationS3Gov
  property_count: 3
  slug: external-volume-storage-location-s3-gov
- name: StorageLocationS3
  property_count: 3
  slug: external-volume-storage-location-s3
- name: StorageLocation
  property_count: 2
  slug: external-volume-storage-location
- name: FunctionArgument
  property_count: 3
  slug: function-function-argument
- name: FunctionArguments
  property_count: 0
  slug: function-function-arguments
- name: Function
  property_count: 9
  slug: function-function
- name: ServiceFunction
  property_count: 2
  slug: function-service-function
- name: Grant
  property_count: 9
  slug: grant-grant
- name: Constraint
  property_count: 3
  slug: iceberg-table-constraint
- name: ConvertToManagedIcebergTableRequest
  property_count: 2
  slug: iceberg-table-convert-to-managed-iceberg-table-request
- name: ForeignKey
  property_count: 2
  slug: iceberg-table-foreign-key
- name: IcebergTableAsSelect
  property_count: 6
  slug: iceberg-table-iceberg-table-as-select
- name: IcebergTableClone
  property_count: 1
  slug: iceberg-table-iceberg-table-clone
- name: IcebergTableColumn
  property_count: 5
  slug: iceberg-table-iceberg-table-column
- name: IcebergTableFromAWSGlueCatalog
  property_count: 8
  slug: iceberg-table-iceberg-table-from-aws-glue-catalog
- name: IcebergTableFromDelta
  property_count: 6
  slug: iceberg-table-iceberg-table-from-delta
- name: IcebergTableFromIcebergFiles
  property_count: 6
  slug: iceberg-table-iceberg-table-from-iceberg-files
- name: IcebergTableFromIcebergRest
  property_count: 8
  slug: iceberg-table-iceberg-table-from-iceberg-rest
- name: IcebergTableLike
  property_count: 5
  slug: iceberg-table-iceberg-table-like
- name: IcebergTable
  property_count: 25
  slug: iceberg-table-iceberg-table
- name: PrimaryKey
  property_count: 0
  slug: iceberg-table-primary-key
- name: RefreshIcebergTableRequest
  property_count: 1
  slug: iceberg-table-refresh-iceberg-table-request
- name: UniqueKey
  property_count: 0
  slug: iceberg-table-unique-key
- name: ImageRepository
  property_count: 4
  slug: image-repository-image-repository
- name: Image
  property_count: 5
  slug: image-repository-image
- name: ManagedAccount
  property_count: 10
  slug: managed-account-managed-account
- name: NetworkPolicy
  property_count: 9
  slug: network-policy-network-policy
- name: NetworkRule
  property_count: 10
  slug: network-rule-network-rule
- name: Notebook
  property_count: 24
  slug: notebook-notebook
- name: VersionDetails
  property_count: 5
  slug: notebook-version-details
- name: NotificationEmail
  property_count: 3
  slug: notification-integration-notification-email
- name: NotificationHook
  property_count: 1
  slug: notification-integration-notification-hook
- name: NotificationIntegration
  property_count: 4
  slug: notification-integration-notification-integration
- name: NotificationQueueAwsSnsOutbound
  property_count: 4
  slug: notification-integration-notification-queue-aws-sns-outbound
- name: NotificationQueueAzureEventGridInbound
  property_count: 4
  slug: notification-integration-notification-queue-azure-event-grid-inbound
- name: NotificationQueueAzureEventGridOutbound
  property_count: 4
  slug: notification-integration-notification-queue-azure-event-grid-outbound
- name: NotificationQueueGcpPubsubInbound
  property_count: 2
  slug: notification-integration-notification-queue-gcp-pubsub-inbound
- name: NotificationQueueGcpPubsubOutbound
  property_count: 2
  slug: notification-integration-notification-queue-gcp-pubsub-outbound
- name: NotificationWebhook
  property_count: 3
  slug: notification-integration-notification-webhook
- name: WebhookSecret
  property_count: 3
  slug: notification-integration-webhook-secret
- name: PasswordPolicy
  property_count: 18
  slug: password-policy-password-policy
- name: Pipe
  property_count: 15
  slug: pipe-pipe
- name: Argument
  property_count: 3
  slug: procedure-argument
- name: BaseLanguage
  property_count: 4
  slug: procedure-base-language
- name: CallArgumentList
  property_count: 1
  slug: procedure-call-argument-list
- name: CallArgument
  property_count: 3
  slug: procedure-call-argument
- name: ColumnType
  property_count: 2
  slug: procedure-column-type
- name: FunctionLanguage
  property_count: 2
  slug: procedure-function-language
- name: JavaFunction
  property_count: 3
  slug: procedure-java-function
- name: JavaScriptFunction
  property_count: 0
  slug: procedure-java-script-function
- name: Procedure
  property_count: 14
  slug: procedure-procedure
- name: PythonFunction
  property_count: 2
  slug: procedure-python-function
- name: ReturnDataType
  property_count: 2
  slug: procedure-return-data-type
- name: ReturnTable
  property_count: 1
  slug: procedure-return-table
- name: ReturnType
  property_count: 1
  slug: procedure-return-type
- name: ScalaFunction
  property_count: 1
  slug: procedure-scala-function
- name: SQLFunction
  property_count: 0
  slug: procedure-sql-function
- name: ContainingScope
  property_count: 2
  slug: role-containing-scope
- name: GrantOf
  property_count: 5
  slug: role-grant-of
- name: GrantOn
  property_count: 9
  slug: role-grant-on
- name: Grant
  property_count: 5
  slug: role-grant
- name: Role
  property_count: 10
  slug: role-role
- name: Securable
  property_count: 4
  slug: role-securable
- name: SchemaClone
  property_count: 0
  slug: schema-schema-clone
- name: Schema
  property_count: 24
  slug: schema-schema
- name: Secret
  property_count: 8
  slug: secret-secret
- name: Sequence
  property_count: 10
  slug: sequence-sequence
- name: GrantOf
  property_count: 5
  slug: service-grant-of
- name: JobService
  property_count: 5
  slug: service-job-service
- name: ServiceContainer
  property_count: 10
  slug: service-service-container
- name: ServiceEndpoint
  property_count: 6
  slug: service-service-endpoint
- name: ServiceInstance
  property_count: 6
  slug: service-service-instance
- name: ServiceRoleGrantTo
  property_count: 6
  slug: service-service-role-grant-to
- name: ServiceRole
  property_count: 3
  slug: service-service-role
- name: Service
  property_count: 0
  slug: service-service
- name: ServiceSpecInlineText
  property_count: 1
  slug: service-service-spec-inline-text
- name: ServiceSpec
  property_count: 1
  slug: service-service-spec
- name: ServiceSpecStageFile
  property_count: 2
  slug: service-service-spec-stage-file
- name: Account
  property_count: 38
  slug: snowflake-account
- name: AccountIdentifiers
  property_count: 1
  slug: snowflake-accountidentifiers
- name: AddLiveVersionStreamlitRequest
  property_count: 1
  slug: snowflake-add-live-version-streamlit-request
- name: AddVersionFromGitStreamlitRequest
  property_count: 2
  slug: snowflake-add-version-from-git-streamlit-request
- name: AddVersionStreamlitRequest
  property_count: 2
  slug: snowflake-add-version-streamlit-request
- name: Alert
  property_count: 12
  slug: snowflake-alert
- name: AlertClone
  property_count: 2
  slug: snowflake-alertclone
- name: ApiHook
  property_count: 1
  slug: snowflake-apihook
- name: ApiIntegration
  property_count: 7
  slug: snowflake-apiintegration
- name: ApiKey
  property_count: 0
  slug: snowflake-apikey
- name: Argument
  property_count: 3
  slug: snowflake-argument
- name: ArtifactRepository
  property_count: 9
  slug: snowflake-artifact-repository
- name: AwsCredentials
  property_count: 4
  slug: snowflake-awscredentials
- name: AwsHook
  property_count: 3
  slug: snowflake-awshook
- name: AzureCredentials
  property_count: 1
  slug: snowflake-azurecredentials
- name: AzureHook
  property_count: 4
  slug: snowflake-azurehook
- name: BaseLanguage
  property_count: 4
  slug: snowflake-baselanguage
- name: BindVariable
  property_count: 2
  slug: snowflake-bindvariable
- name: CallArgument
  property_count: 3
  slug: snowflake-callargument
- name: CallArgumentList
  property_count: 1
  slug: snowflake-callargumentlist
- name: CancelStatus
  property_count: 5
  slug: snowflake-cancelstatus
- name: Catalog
  property_count: 1
  slug: snowflake-catalog
- name: CatalogIntegration
  property_count: 8
  slug: snowflake-catalogintegration
- name: Column
  property_count: 0
  slug: snowflake-column
- name: ColumnDefinition
  property_count: 6
  slug: snowflake-columndefinition
- name: ColumnQuery
  property_count: 2
  slug: snowflake-columnquery
- name: ColumnType
  property_count: 2
  slug: snowflake-columntype
- name: CommitStreamlitRequest
  property_count: 1
  slug: snowflake-commit-streamlit-request
- name: CompleteRequest
  property_count: 15
  slug: snowflake-completerequest
- name: ComputePool
  property_count: 22
  slug: snowflake-computepool
- name: Confidence
  property_count: 1
  slug: snowflake-confidence
- name: Constraint
  property_count: 3
  slug: snowflake-constraint
- name: ContainingScope
  property_count: 2
  slug: snowflake-containingscope
- name: ConvertToManagedIcebergTableRequest
  property_count: 2
  slug: snowflake-converttomanagedicebergtablerequest
- name: CortexSearchService
  property_count: 17
  slug: snowflake-cortexsearchservice
- name: Credentials
  property_count: 1
  slug: snowflake-credentials
- name: CronSchedule
  property_count: 2
  slug: snowflake-cronschedule
- name: Snowflake Database
  property_count: 23
  slug: snowflake-database
- name: DatabaseClone
  property_count: 1
  slug: snowflake-databaseclone
- name: DatabaseFromShare
  property_count: 1
  slug: snowflake-databasefromshare
- name: DatabaseRole
  property_count: 8
  slug: snowflake-databaserole
- name: DatabaseRoleClone
  property_count: 1
  slug: snowflake-databaseroleclone
- name: DownstreamLag
  property_count: 0
  slug: snowflake-downstreamlag
- name: DynamicTable
  property_count: 22
  slug: snowflake-dynamictable
- name: DynamicTableClone
  property_count: 4
  slug: snowflake-dynamictableclone
- name: DynamicTableColumn
  property_count: 3
  slug: snowflake-dynamictablecolumn
- name: EmbedRequest
  property_count: 3
  slug: snowflake-embed-request
- name: EmbedResponse
  property_count: 4
  slug: snowflake-embed-response
- name: Encryption
  property_count: 2
  slug: snowflake-encryption
- name: ErrorResponse
  property_count: 4
  slug: snowflake-errorresponse
- name: EventTable
  property_count: 19
  slug: snowflake-eventtable
- name: EventTableColumn
  property_count: 9
  slug: snowflake-eventtablecolumn
- name: ExecutionStats
  property_count: 4
  slug: snowflake-executionstats
- name: ExternalVolume
  property_count: 7
  slug: snowflake-externalvolume
- name: FileTransferMaterial
  property_count: 1
  slug: snowflake-filetransfermaterial
- name: ForeignKey
  property_count: 2
  slug: snowflake-foreignkey
- name: Function
  property_count: 9
  slug: snowflake-function
- name: FunctionArgument
  property_count: 3
  slug: snowflake-functionargument
- name: FunctionArguments
  property_count: 0
  slug: snowflake-functionarguments
- name: FunctionLanguage
  property_count: 2
  slug: snowflake-functionlanguage
- name: Functions
  property_count: 5
  slug: snowflake-functions
- name: GenerateVerifiedQuerySuggestionsRequest
  property_count: 3
  slug: snowflake-generateverifiedquerysuggestionsrequest
- name: GenerateVerifiedQuerySuggestionsResponse
  property_count: 3
  slug: snowflake-generateverifiedquerysuggestionsresponse
- name: GetModelsRequest
  property_count: 1
  slug: snowflake-getmodelsrequest
- name: GetModelsResponse
  property_count: 1
  slug: snowflake-getmodelsresponse
- name: GitHook
  property_count: 3
  slug: snowflake-githook
- name: Glue
  property_count: 4
  slug: snowflake-glue
- name: GoogleCloudHook
  property_count: 3
  slug: snowflake-googlecloudhook
- name: Grant
  property_count: 7
  slug: snowflake-grant
- name: GrantOf
  property_count: 5
  slug: snowflake-grantof
- name: GrantOn
  property_count: 9
  slug: snowflake-granton
- name: GuardrailsConfig
  property_count: 2
  slug: snowflake-guardrailsconfig
- name: IcebergTable
  property_count: 25
  slug: snowflake-icebergtable
- name: IcebergTableAsSelect
  property_count: 6
  slug: snowflake-icebergtableasselect
- name: IcebergTableClone
  property_count: 2
  slug: snowflake-icebergtableclone
- name: IcebergTableColumn
  property_count: 5
  slug: snowflake-icebergtablecolumn
- name: IcebergTableFromAWSGlueCatalog
  property_count: 8
  slug: snowflake-icebergtablefromawsgluecatalog
- name: IcebergTableFromDelta
  property_count: 6
  slug: snowflake-icebergtablefromdelta
- name: IcebergTableFromIcebergFiles
  property_count: 6
  slug: snowflake-icebergtablefromicebergfiles
- name: IcebergTableFromIcebergRest
  property_count: 8
  slug: snowflake-icebergtablefromicebergrest
- name: IcebergTableLike
  property_count: 5
  slug: snowflake-icebergtablelike
- name: Identifier
  property_count: 0
  slug: snowflake-identifier
- name: Image
  property_count: 5
  slug: snowflake-image
- name: ImageRepository
  property_count: 7
  slug: snowflake-imagerepository
- name: JavaFunction
  property_count: 3
  slug: snowflake-javafunction
- name: JavaScriptFunction
  property_count: 0
  slug: snowflake-javascriptfunction
- name: JobService
  property_count: 8
  slug: snowflake-jobservice
- name: ManagedAccount
  property_count: 11
  slug: snowflake-managedaccount
- name: MessageContent
  property_count: 1
  slug: snowflake-messagecontent
- name: MessageContentChartObject
  property_count: 1
  slug: snowflake-messagecontentchartobject
- name: MessageContentDelta
  property_count: 2
  slug: snowflake-messagecontentdelta
- name: MessageContentDeltaSqlObject
  property_count: 2
  slug: snowflake-messagecontentdeltasqlobject
- name: MessageContentDeltaSuggestionsObject
  property_count: 1
  slug: snowflake-messagecontentdeltasuggestionsobject
- name: MessageContentDeltaTextObject
  property_count: 1
  slug: snowflake-messagecontentdeltatextobject
- name: MessageContentResultsObject
  property_count: 1
  slug: snowflake-messagecontentresultsobject
- name: MessageContentSqlObject
  property_count: 2
  slug: snowflake-messagecontentsqlobject
- name: MessageContentSuggestionsObject
  property_count: 1
  slug: snowflake-messagecontentsuggestionsobject
- name: MessageContentTextObject
  property_count: 1
  slug: snowflake-messagecontenttextobject
- name: The message object
  property_count: 2
  slug: snowflake-messageobject
- name: MinutesSchedule
  property_count: 1
  slug: snowflake-minutesschedule
- name: NetworkRule
  property_count: 10
  slug: snowflake-network-rule
- name: NetworkPolicy
  property_count: 9
  slug: snowflake-networkpolicy
- name: NonStreamingCompleteResponse
  property_count: 2
  slug: snowflake-nonstreamingcompleteresponse
- name: Notebook
  property_count: 26
  slug: snowflake-notebook
- name: NotificationEmail
  property_count: 3
  slug: snowflake-notificationemail
- name: NotificationHook
  property_count: 1
  slug: snowflake-notificationhook
- name: NotificationIntegration
  property_count: 5
  slug: snowflake-notificationintegration
- name: NotificationQueueAwsSnsOutbound
  property_count: 4
  slug: snowflake-notificationqueueawssnsoutbound
- name: NotificationQueueAzureEventGridInbound
  property_count: 4
  slug: snowflake-notificationqueueazureeventgridinbound
- name: NotificationQueueAzureEventGridOutbound
  property_count: 4
  slug: snowflake-notificationqueueazureeventgridoutbound
- name: NotificationQueueGcpPubsubInbound
  property_count: 2
  slug: snowflake-notificationqueuegcppubsubinbound
- name: NotificationQueueGcpPubsubOutbound
  property_count: 2
  slug: snowflake-notificationqueuegcppubsuboutbound
- name: NotificationWebhook
  property_count: 4
  slug: snowflake-notificationwebhook
- name: NumericBoost
  property_count: 2
  slug: snowflake-numericboost
- name: OAuth
  property_count: 3
  slug: snowflake-oauth
- name: ObjectStore
  property_count: 0
  slug: snowflake-objectstore
- name: Parameter
  property_count: 6
  slug: snowflake-parameter
- name: PartitionInfo
  property_count: 3
  slug: snowflake-partitioninfo
- name: PasswordPolicy
  property_count: 18
  slug: snowflake-password-policy
- name: Pipe
  property_count: 15
  slug: snowflake-pipe
- name: PointOfTime
  property_count: 2
  slug: snowflake-pointoftime
- name: PointOfTimeOffset
  property_count: 1
  slug: snowflake-pointoftimeoffset
- name: PointOfTimeStatement
  property_count: 1
  slug: snowflake-pointoftimestatement
- name: PointOfTimeStream
  property_count: 1
  slug: snowflake-pointoftimestream
- name: PointOfTimeTimestamp
  property_count: 1
  slug: snowflake-pointoftimetimestamp
- name: Polaris
  property_count: 3
  slug: snowflake-polaris
- name: PresignedUrlRequest
  property_count: 1
  slug: snowflake-presignedurlrequest
- name: PrimaryKey
  property_count: 0
  slug: snowflake-primarykey
- name: Procedure
  property_count: 16
  slug: snowflake-procedure
- name: PythonFunction
  property_count: 2
  slug: snowflake-pythonfunction
- name: QueryFailureStatus
  property_count: 6
  slug: snowflake-queryfailurestatus
- name: QueryRequest
  property_count: 7
  slug: snowflake-queryrequest
- name: QueryResponse
  property_count: 2
  slug: snowflake-queryresponse
- name: QuerySimilarityBoost
  property_count: 3
  slug: snowflake-querysimilarityboost
- name: QueryStatus
  property_count: 6
  slug: snowflake-querystatus
- name: RefreshIcebergTableRequest
  property_count: 1
  slug: snowflake-refreshicebergtablerequest
- name: Reranker
  property_count: 0
  slug: snowflake-reranker
- name: RestAuthentication
  property_count: 1
  slug: snowflake-restauthentication
- name: RestConfig
  property_count: 2
  slug: snowflake-restconfig
- name: ResultSet
  property_count: 9
  slug: snowflake-resultset
- name: ResultSetMetaData
  property_count: 6
  slug: snowflake-resultsetmetadata
- name: ReturnDataType
  property_count: 2
  slug: snowflake-returndatatype
- name: ReturnTable
  property_count: 1
  slug: snowflake-returntable
- name: ReturnType
  property_count: 1
  slug: snowflake-returntype
- name: Role
  property_count: 10
  slug: snowflake-role
- name: ScalaFunction
  property_count: 1
  slug: snowflake-scalafunction
- name: Schedule
  property_count: 1
  slug: snowflake-schedule
- name: SchedulingState
  property_count: 0
  slug: snowflake-schedulingstate
- name: Schema
  property_count: 25
  slug: snowflake-schema
- name: SchemaClone
  property_count: 1
  slug: snowflake-schemaclone
- name: ScoringConfig
  property_count: 3
  slug: snowflake-scoringconfig
- name: Secret
  property_count: 8
  slug: snowflake-secret
- name: Securable
  property_count: 4
  slug: snowflake-securable
- name: the semantic model object
  property_count: 3
  slug: snowflake-semanticmodelobject
- name: SemanticModelSelection
  property_count: 2
  slug: snowflake-semanticmodelselection
- name: SendFeedbackRequest
  property_count: 3
  slug: snowflake-sendfeedbackrequest
- name: SendMessageRequest
  property_count: 10
  slug: snowflake-sendmessagerequest
- name: SendMessageResponse
  property_count: 5
  slug: snowflake-sendmessageresponse
- name: Sequence
  property_count: 10
  slug: snowflake-sequence
- name: Service
  property_count: 21
  slug: snowflake-service
- name: ServiceContainer
  property_count: 13
  slug: snowflake-servicecontainer
- name: ServiceEndpoint
  property_count: 6
  slug: snowflake-serviceendpoint
- name: ServiceFunction
  property_count: 5
  slug: snowflake-servicefunction
- name: ServiceInstance
  property_count: 9
  slug: snowflake-serviceinstance
- name: ServiceRole
  property_count: 3
  slug: snowflake-servicerole
- name: ServiceRoleGrantTo
  property_count: 6
  slug: snowflake-servicerolegrantto
- name: ServiceSpec
  property_count: 1
  slug: snowflake-servicespec
- name: ServiceSpecInlineText
  property_count: 1
  slug: snowflake-servicespecinlinetext
- name: ServiceSpecStageFile
  property_count: 2
  slug: snowflake-servicespecstagefile
- name: SessionParameters
  property_count: 13
  slug: snowflake-sessionparameters
- name: BindVariable
  property_count: 2
  slug: snowflake-sql-rest-bind-variable
- name: CancelStatus
  property_count: 5
  slug: snowflake-sql-rest-cancel-status
- name: ColumnDefinition
  property_count: 6
  slug: snowflake-sql-rest-column-definition
- name: ExecutionStats
  property_count: 4
  slug: snowflake-sql-rest-execution-stats
- name: PartitionInfo
  property_count: 3
  slug: snowflake-sql-rest-partition-info
- name: QueryFailureStatus
  property_count: 6
  slug: snowflake-sql-rest-query-failure-status
- name: QueryStatus
  property_count: 6
  slug: snowflake-sql-rest-query-status
- name: ResultSetMetaData
  property_count: 5
  slug: snowflake-sql-rest-result-set-meta-data
- name: ResultSet
  property_count: 7
  slug: snowflake-sql-rest-result-set
- name: SessionParameters
  property_count: 13
  slug: snowflake-sql-rest-session-parameters
- name: StatementRequest
  property_count: 7
  slug: snowflake-sql-rest-statement-request
- name: SQLFunction
  property_count: 0
  slug: snowflake-sqlfunction
- name: Stage
  property_count: 16
  slug: snowflake-stage
- name: StageFile
  property_count: 4
  slug: snowflake-stagefile
- name: StatementRequest
  property_count: 8
  slug: snowflake-statementrequest
- name: StatusUpdate
  property_count: 3
  slug: snowflake-statusupdate
- name: StorageLocation
  property_count: 2
  slug: snowflake-storagelocation
- name: StorageLocationAzure
  property_count: 2
  slug: snowflake-storagelocationazure
- name: StorageLocationGcs
  property_count: 2
  slug: snowflake-storagelocationgcs
- name: StorageLocationS3
  property_count: 4
  slug: snowflake-storagelocations3
- name: StorageLocationS3Gov
  property_count: 4
  slug: snowflake-storagelocations3gov
- name: Stream
  property_count: 14
  slug: snowflake-stream
- name: StreamClone
  property_count: 2
  slug: snowflake-streamclone
- name: StreamingCompleteResponse
  property_count: 0
  slug: snowflake-streamingcompleteresponse
- name: StreamingCompleteResponseDataEvent
  property_count: 1
  slug: snowflake-streamingcompleteresponsedataevent
- name: StreamingCompleteResponseDelta
  property_count: 0
  slug: snowflake-streamingcompleteresponsedelta
- name: StreamingError
  property_count: 3
  slug: snowflake-streamingerror
- name: StreamlitPushOptions
  property_count: 1
  slug: snowflake-streamlit-push-options
- name: Streamlit
  property_count: 21
  slug: snowflake-streamlit
- name: StreamSource
  property_count: 4
  slug: snowflake-streamsource
- name: StreamSourceExternalTable
  property_count: 2
  slug: snowflake-streamsourceexternaltable
- name: StreamSourceStage
  property_count: 0
  slug: snowflake-streamsourcestage
- name: StreamSourceTable
  property_count: 3
  slug: snowflake-streamsourcetable
- name: StreamSourceView
  property_count: 4
  slug: snowflake-streamsourceview
- name: SuccessAcceptedResponse
  property_count: 3
  slug: snowflake-successacceptedresponse
- name: SuccessResponse
  property_count: 1
  slug: snowflake-successresponse
- name: SuggestionDelta
  property_count: 2
  slug: snowflake-suggestiondelta
- name: Table
  property_count: 25
  slug: snowflake-table
- name: TableAsSelect
  property_count: 3
  slug: snowflake-tableasselect
- name: TableClone
  property_count: 1
  slug: snowflake-tableclone
- name: TableColumn
  property_count: 10
  slug: snowflake-tablecolumn
- name: TableLike
  property_count: 1
  slug: snowflake-tablelike
- name: TableUsingTemplate
  property_count: 1
  slug: snowflake-tableusingtemplate
- name: Tag
  property_count: 10
  slug: snowflake-tag
- name: TargetLag
  property_count: 1
  slug: snowflake-targetlag
- name: Task
  property_count: 29
  slug: snowflake-task
- name: TaskRun
  property_count: 14
  slug: snowflake-taskrun
- name: TaskSchedule
  property_count: 1
  slug: snowflake-taskschedule
- name: TextBoost
  property_count: 2
  slug: snowflake-textboost
- name: TimeDecay
  property_count: 4
  slug: snowflake-timedecay
- name: TokenInfo
  property_count: 2
  slug: snowflake-tokeninfo
- name: UniqueKey
  property_count: 0
  slug: snowflake-uniquekey
- name: User
  property_count: 40
  slug: snowflake-user
- name: UserDefinedFunction
  property_count: 20
  slug: snowflake-userdefinedfunction
- name: UserDefinedLag
  property_count: 1
  slug: snowflake-userdefinedlag
- name: VectorBoost
  property_count: 2
  slug: snowflake-vectorboost
- name: VerifiedQuery
  property_count: 5
  slug: snowflake-verifiedquery
- name: VerifiedQuerySuggestion
  property_count: 3
  slug: snowflake-verifiedquerysuggestion
- name: VersionDetails
  property_count: 5
  slug: snowflake-versiondetails
- name: View
  property_count: 12
  slug: snowflake-view
- name: ViewColumn
  property_count: 3
  slug: snowflake-viewcolumn
- name: Snowflake Warehouse
  property_count: 35
  slug: snowflake-warehouse
- name: The warning object
  property_count: 1
  slug: snowflake-warning
- name: Warnings
  property_count: 1
  slug: snowflake-warnings
- name: WebhookSecret
  property_count: 3
  slug: snowflake-webhooksecret
- name: Weights
  property_count: 3
  slug: snowflake-weights
- name: CancelStatus
  property_count: 5
  slug: sqlapi-cancel-status
- name: QueryFailureStatus
  property_count: 6
  slug: sqlapi-query-failure-status
- name: QueryStatus
  property_count: 6
  slug: sqlapi-query-status
- name: ResultSet
  property_count: 9
  slug: sqlapi-result-set
- name: AwsCredentials
  property_count: 4
  slug: stage-aws-credentials
- name: AzureCredentials
  property_count: 1
  slug: stage-azure-credentials
- name: Credentials
  property_count: 1
  slug: stage-credentials
- name: FileTransferMaterial
  property_count: 1
  slug: stage-file-transfer-material
- name: PresignedUrlRequest
  property_count: 1
  slug: stage-presigned-url-request
- name: StageFile
  property_count: 4
  slug: stage-stage-file
- name: Stage
  property_count: 13
  slug: stage-stage
- name: PointOfTimeOffset
  property_count: 1
  slug: stream-point-of-time-offset
- name: PointOfTime
  property_count: 2
  slug: stream-point-of-time
- name: PointOfTimeStatement
  property_count: 1
  slug: stream-point-of-time-statement
- name: PointOfTimeStream
  property_count: 1
  slug: stream-point-of-time-stream
- name: PointOfTimeTimestamp
  property_count: 1
  slug: stream-point-of-time-timestamp
- name: StreamClone
  property_count: 2
  slug: stream-stream-clone
- name: Stream
  property_count: 13
  slug: stream-stream
- name: StreamSourceExternalTable
  property_count: 1
  slug: stream-stream-source-external-table
- name: StreamSource
  property_count: 4
  slug: stream-stream-source
- name: StreamSourceStage
  property_count: 0
  slug: stream-stream-source-stage
- name: StreamSourceTable
  property_count: 2
  slug: stream-stream-source-table
- name: StreamSourceView
  property_count: 3
  slug: stream-stream-source-view
- name: AddLiveVersionStreamlitRequest
  property_count: 1
  slug: streamlit-add-live-version-streamlit-request
- name: AddLiveVersionStreamlitRequestVersion
  property_count: 2
  slug: streamlit-add-live-version-streamlit-request-version
- name: AddVersionFromGitStreamlitRequest
  property_count: 2
  slug: streamlit-add-version-from-git-streamlit-request
- name: AddVersionStreamlitRequest
  property_count: 2
  slug: streamlit-add-version-streamlit-request
- name: CommitStreamlitRequest
  property_count: 1
  slug: streamlit-commit-streamlit-request
- name: StreamlitPushOptions
  property_count: 1
  slug: streamlit-streamlit-push-options
- name: Streamlit
  property_count: 21
  slug: streamlit-streamlit
- name: StreamlitVersionForGit
  property_count: 2
  slug: streamlit-streamlit-version-for-git
- name: VersionDetailsStreamlit
  property_count: 5
  slug: streamlit-version-details-streamlit
- name: Constraint
  property_count: 3
  slug: table-constraint
- name: ForeignKey
  property_count: 2
  slug: table-foreign-key
- name: PrimaryKey
  property_count: 0
  slug: table-primary-key
- name: TableAsSelect
  property_count: 3
  slug: table-table-as-select
- name: TableClone
  property_count: 0
  slug: table-table-clone
- name: TableColumn
  property_count: 10
  slug: table-table-column
- name: TableLike
  property_count: 1
  slug: table-table-like
- name: Table
  property_count: 25
  slug: table-table
- name: TableUsingTemplate
  property_count: 1
  slug: table-table-using-template
- name: UniqueKey
  property_count: 0
  slug: table-unique-key
- name: Tag
  property_count: 10
  slug: tag-tag
- name: CronSchedule
  property_count: 2
  slug: task-cron-schedule
- name: MinutesSchedule
  property_count: 1
  slug: task-minutes-schedule
- name: TaskRun
  property_count: 14
  slug: task-task-run
- name: TaskSchedule
  property_count: 1
  slug: task-task-schedule
- name: Task
  property_count: 25
  slug: task-task
- name: ContainingScope
  property_count: 2
  slug: user-containing-scope
- name: Argument
  property_count: 3
  slug: user-defined-function-argument
- name: BaseLanguage
  property_count: 3
  slug: user-defined-function-base-language
- name: ColumnType
  property_count: 2
  slug: user-defined-function-column-type
- name: FunctionLanguage
  property_count: 3
  slug: user-defined-function-function-language
- name: JavaFunction
  property_count: 4
  slug: user-defined-function-java-function
- name: JavaScriptFunction
  property_count: 0
  slug: user-defined-function-java-script-function
- name: PythonFunction
  property_count: 3
  slug: user-defined-function-python-function
- name: ReturnDataType
  property_count: 2
  slug: user-defined-function-return-data-type
- name: ReturnTable
  property_count: 1
  slug: user-defined-function-return-table
- name: ReturnType
  property_count: 1
  slug: user-defined-function-return-type
- name: ScalaFunction
  property_count: 2
  slug: user-defined-function-scala-function
- name: SQLFunction
  property_count: 0
  slug: user-defined-function-sql-function
- name: UserDefinedFunction
  property_count: 18
  slug: user-defined-function-user-defined-function
- name: Grant
  property_count: 4
  slug: user-grant
- name: Securable
  property_count: 3
  slug: user-securable
- name: User
  property_count: 40
  slug: user-user
- name: ViewColumn
  property_count: 3
  slug: view-view-column
- name: View
  property_count: 12
  slug: view-view
- name: Warehouse
  property_count: 36
  slug: warehouse-warehouse
json_structures:
- name: Account Account Structure
  property_count: 37
  slug: account-account-structure
- name: Alert Alert Clone Structure
  property_count: 1
  slug: alert-alert-clone-structure
- name: Alert Alert Structure
  property_count: 11
  slug: alert-alert-structure
- name: Alert Cron Schedule Structure
  property_count: 2
  slug: alert-cron-schedule-structure
- name: Alert Minutes Schedule Structure
  property_count: 1
  slug: alert-minutes-schedule-structure
- name: Alert Point Of Time Offset Structure
  property_count: 1
  slug: alert-point-of-time-offset-structure
- name: Alert Point Of Time Statement Structure
  property_count: 1
  slug: alert-point-of-time-statement-structure
- name: Alert Point Of Time Structure
  property_count: 2
  slug: alert-point-of-time-structure
- name: Alert Point Of Time Timestamp Structure
  property_count: 1
  slug: alert-point-of-time-timestamp-structure
- name: Alert Schedule Structure
  property_count: 1
  slug: alert-schedule-structure
- name: Api Integration Api Hook Structure
  property_count: 1
  slug: api-integration-api-hook-structure
- name: Api Integration Api Integration Structure
  property_count: 6
  slug: api-integration-api-integration-structure
- name: Api Integration Api Key Structure
  property_count: 0
  slug: api-integration-api-key-structure
- name: Api Integration Aws Hook Structure
  property_count: 2
  slug: api-integration-aws-hook-structure
- name: Api Integration Azure Hook Structure
  property_count: 3
  slug: api-integration-azure-hook-structure
- name: Api Integration Git Hook Structure
  property_count: 3
  slug: api-integration-git-hook-structure
- name: Api Integration Google Cloud Hook Structure
  property_count: 2
  slug: api-integration-google-cloud-hook-structure
- name: Artifact Repository Artifact Repository Structure
  property_count: 9
  slug: artifact-repository-artifact-repository-structure
- name: Catalog Integration Catalog Integration Structure
  property_count: 7
  slug: catalog-integration-catalog-integration-structure
- name: Catalog Integration Catalog Structure
  property_count: 1
  slug: catalog-integration-catalog-structure
- name: Catalog Integration Glue Structure
  property_count: 4
  slug: catalog-integration-glue-structure
- name: Catalog Integration O Auth Structure
  property_count: 3
  slug: catalog-integration-o-auth-structure
- name: Catalog Integration Object Store Structure
  property_count: 0
  slug: catalog-integration-object-store-structure
- name: Catalog Integration Polaris Structure
  property_count: 1
  slug: catalog-integration-polaris-structure
- name: Catalog Integration Rest Authentication Structure
  property_count: 1
  slug: catalog-integration-rest-authentication-structure
- name: Catalog Integration Rest Config Structure
  property_count: 2
  slug: catalog-integration-rest-config-structure
- name: Common Downstream Lag Structure
  property_count: 0
  slug: common-downstream-lag-structure
- name: Common Error Response Structure
  property_count: 4
  slug: common-error-response-structure
- name: Common Identifier Structure
  property_count: 0
  slug: common-identifier-structure
- name: Common Parameter Structure
  property_count: 6
  slug: common-parameter-structure
- name: Common Point Of Time Offset Structure
  property_count: 1
  slug: common-point-of-time-offset-structure
- name: Common Point Of Time Statement Structure
  property_count: 1
  slug: common-point-of-time-statement-structure
- name: Common Point Of Time Structure
  property_count: 2
  slug: common-point-of-time-structure
- name: Common Point Of Time Timestamp Structure
  property_count: 1
  slug: common-point-of-time-timestamp-structure
- name: Common Success Accepted Response Structure
  property_count: 3
  slug: common-success-accepted-response-structure
- name: Common Success Response Structure
  property_count: 1
  slug: common-success-response-structure
- name: Common Target Lag Structure
  property_count: 1
  slug: common-target-lag-structure
- name: Common User Defined Lag Structure
  property_count: 1
  slug: common-user-defined-lag-structure
- name: Compute Pool Compute Pool Structure
  property_count: 21
  slug: compute-pool-compute-pool-structure
- name: Cortex Analyst Confidence Structure
  property_count: 0
  slug: cortex-analyst-confidence-structure
- name: Cortex Analyst Generate Verified Query Suggestions Request Structure
  property_count: 2
  slug: cortex-analyst-generate-verified-query-suggestions-request-structure
- name: Cortex Analyst Generate Verified Query Suggestions Response Structure
  property_count: 3
  slug: cortex-analyst-generate-verified-query-suggestions-response-structure
- name: Cortex Analyst Message Content Chart Object Structure
  property_count: 0
  slug: cortex-analyst-message-content-chart-object-structure
- name: Cortex Analyst Message Content Delta Sql Object Structure
  property_count: 0
  slug: cortex-analyst-message-content-delta-sql-object-structure
- name: Cortex Analyst Message Content Delta Structure
  property_count: 2
  slug: cortex-analyst-message-content-delta-structure
- name: Cortex Analyst Message Content Delta Suggestions Object Structure
  property_count: 0
  slug: cortex-analyst-message-content-delta-suggestions-object-structure
- name: Cortex Analyst Message Content Delta Text Object Structure
  property_count: 0
  slug: cortex-analyst-message-content-delta-text-object-structure
- name: Cortex Analyst Message Content Results Object Structure
  property_count: 0
  slug: cortex-analyst-message-content-results-object-structure
- name: Cortex Analyst Message Content Sql Object Structure
  property_count: 0
  slug: cortex-analyst-message-content-sql-object-structure
- name: Cortex Analyst Message Content Structure
  property_count: 1
  slug: cortex-analyst-message-content-structure
- name: Cortex Analyst Message Content Suggestions Object Structure
  property_count: 0
  slug: cortex-analyst-message-content-suggestions-object-structure
- name: Cortex Analyst Message Content Text Object Structure
  property_count: 0
  slug: cortex-analyst-message-content-text-object-structure
- name: Cortex Analyst Message Object Structure
  property_count: 2
  slug: cortex-analyst-message-object-structure
- name: Cortex Analyst Semantic Model Object Structure
  property_count: 3
  slug: cortex-analyst-semantic-model-object-structure
- name: Cortex Analyst Semantic Model Selection Structure
  property_count: 1
  slug: cortex-analyst-semantic-model-selection-structure
- name: Cortex Analyst Send Feedback Request Structure
  property_count: 3
  slug: cortex-analyst-send-feedback-request-structure
- name: Cortex Analyst Send Message Request Structure
  property_count: 10
  slug: cortex-analyst-send-message-request-structure
- name: Cortex Analyst Send Message Response Structure
  property_count: 3
  slug: cortex-analyst-send-message-response-structure
- name: Cortex Analyst Status Update Structure
  property_count: 3
  slug: cortex-analyst-status-update-structure
- name: Cortex Analyst Streaming Error Structure
  property_count: 3
  slug: cortex-analyst-streaming-error-structure
- name: Cortex Analyst Suggestion Delta Structure
  property_count: 2
  slug: cortex-analyst-suggestion-delta-structure
- name: Cortex Analyst Token Info Structure
  property_count: 2
  slug: cortex-analyst-token-info-structure
- name: Cortex Analyst Verified Query Structure
  property_count: 5
  slug: cortex-analyst-verified-query-structure
- name: Cortex Analyst Verified Query Suggestion Structure
  property_count: 1
  slug: cortex-analyst-verified-query-suggestion-structure
- name: Cortex Analyst Warning Structure
  property_count: 1
  slug: cortex-analyst-warning-structure
- name: Cortex Analyst Warnings Structure
  property_count: 1
  slug: cortex-analyst-warnings-structure
- name: Cortex Embed Embed Request Structure
  property_count: 3
  slug: cortex-embed-embed-request-structure
- name: Cortex Embed Embed Response Structure
  property_count: 4
  slug: cortex-embed-embed-response-structure
- name: Cortex Inference Complete Request Structure
  property_count: 13
  slug: cortex-inference-complete-request-structure
- name: Cortex Inference Get Models Request Structure
  property_count: 1
  slug: cortex-inference-get-models-request-structure
- name: Cortex Inference Get Models Response Structure
  property_count: 1
  slug: cortex-inference-get-models-response-structure
- name: Cortex Inference Guardrails Config Structure
  property_count: 2
  slug: cortex-inference-guardrails-config-structure
- name: Cortex Inference Non Streaming Complete Response Structure
  property_count: 2
  slug: cortex-inference-non-streaming-complete-response-structure
- name: Cortex Inference Streaming Complete Response Data Event Structure
  property_count: 1
  slug: cortex-inference-streaming-complete-response-data-event-structure
- name: Cortex Inference Streaming Complete Response Delta Structure
  property_count: 0
  slug: cortex-inference-streaming-complete-response-delta-structure
- name: Cortex Inference Streaming Complete Response Structure
  property_count: 0
  slug: cortex-inference-streaming-complete-response-structure
- name: Cortex Search Service Column Query Structure
  property_count: 2
  slug: cortex-search-service-column-query-structure
- name: Cortex Search Service Column Structure
  property_count: 0
  slug: cortex-search-service-column-structure
- name: Cortex Search Service Cortex Search Service Structure
  property_count: 14
  slug: cortex-search-service-cortex-search-service-structure
- name: Cortex Search Service Functions Structure
  property_count: 5
  slug: cortex-search-service-functions-structure
- name: Cortex Search Service Numeric Boost Structure
  property_count: 1
  slug: cortex-search-service-numeric-boost-structure
- name: Cortex Search Service Query Request Structure
  property_count: 6
  slug: cortex-search-service-query-request-structure
- name: Cortex Search Service Query Response Structure
  property_count: 2
  slug: cortex-search-service-query-response-structure
- name: Cortex Search Service Query Similarity Boost Structure
  property_count: 3
  slug: cortex-search-service-query-similarity-boost-structure
- name: Cortex Search Service Reranker Structure
  property_count: 0
  slug: cortex-search-service-reranker-structure
- name: Cortex Search Service Scheduling State Structure
  property_count: 0
  slug: cortex-search-service-scheduling-state-structure
- name: Cortex Search Service Scoring Config Structure
  property_count: 0
  slug: cortex-search-service-scoring-config-structure
- name: Cortex Search Service Text Boost Structure
  property_count: 1
  slug: cortex-search-service-text-boost-structure
- name: Cortex Search Service Time Decay Structure
  property_count: 3
  slug: cortex-search-service-time-decay-structure
- name: Cortex Search Service Vector Boost Structure
  property_count: 1
  slug: cortex-search-service-vector-boost-structure
- name: Cortex Search Service Weights Structure
  property_count: 3
  slug: cortex-search-service-weights-structure
- name: Database Account Identifiers Structure
  property_count: 1
  slug: database-account-identifiers-structure
- name: Database Database Clone Structure
  property_count: 0
  slug: database-database-clone-structure
- name: Database Database From Share Structure
  property_count: 0
  slug: database-database-from-share-structure
- name: Database Database Structure
  property_count: 22
  slug: database-database-structure
- name: Database Role Containing Scope Structure
  property_count: 2
  slug: database-role-containing-scope-structure
- name: Database Role Database Role Clone Structure
  property_count: 1
  slug: database-role-database-role-clone-structure
- name: Database Role Database Role Structure
  property_count: 8
  slug: database-role-database-role-structure
- name: Database Role Grant Structure
  property_count: 5
  slug: database-role-grant-structure
- name: Database Role Securable Structure
  property_count: 4
  slug: database-role-securable-structure
- name: Dynamic Table Dynamic Table Clone Structure
  property_count: 2
  slug: dynamic-table-dynamic-table-clone-structure
- name: Dynamic Table Dynamic Table Column Structure
  property_count: 3
  slug: dynamic-table-dynamic-table-column-structure
- name: Dynamic Table Dynamic Table Structure
  property_count: 21
  slug: dynamic-table-dynamic-table-structure
- name: Event Table Event Table Column Structure
  property_count: 9
  slug: event-table-event-table-column-structure
- name: Event Table Event Table Structure
  property_count: 19
  slug: event-table-event-table-structure
- name: External Volume Encryption Structure
  property_count: 2
  slug: external-volume-encryption-structure
- name: External Volume External Volume Structure
  property_count: 7
  slug: external-volume-external-volume-structure
- name: External Volume Storage Location Azure Structure
  property_count: 2
  slug: external-volume-storage-location-azure-structure
- name: External Volume Storage Location Gcs Structure
  property_count: 1
  slug: external-volume-storage-location-gcs-structure
- name: External Volume Storage Location S3 Gov Structure
  property_count: 3
  slug: external-volume-storage-location-s3-gov-structure
- name: External Volume Storage Location S3 Structure
  property_count: 3
  slug: external-volume-storage-location-s3-structure
- name: External Volume Storage Location Structure
  property_count: 2
  slug: external-volume-storage-location-structure
- name: Function Function Argument Structure
  property_count: 3
  slug: function-function-argument-structure
- name: Function Function Arguments Structure
  property_count: 0
  slug: function-function-arguments-structure
- name: Function Function Structure
  property_count: 9
  slug: function-function-structure
- name: Function Service Function Structure
  property_count: 2
  slug: function-service-function-structure
- name: Grant Grant Structure
  property_count: 9
  slug: grant-grant-structure
- name: Iceberg Table Constraint Structure
  property_count: 3
  slug: iceberg-table-constraint-structure
- name: Iceberg Table Convert To Managed Iceberg Table Request Structure
  property_count: 2
  slug: iceberg-table-convert-to-managed-iceberg-table-request-structure
- name: Iceberg Table Foreign Key Structure
  property_count: 2
  slug: iceberg-table-foreign-key-structure
- name: Iceberg Table Iceberg Table As Select Structure
  property_count: 6
  slug: iceberg-table-iceberg-table-as-select-structure
- name: Iceberg Table Iceberg Table Clone Structure
  property_count: 1
  slug: iceberg-table-iceberg-table-clone-structure
- name: Iceberg Table Iceberg Table Column Structure
  property_count: 5
  slug: iceberg-table-iceberg-table-column-structure
- name: Iceberg Table Iceberg Table From Aws Glue Catalog Structure
  property_count: 8
  slug: iceberg-table-iceberg-table-from-aws-glue-catalog-structure
- name: Iceberg Table Iceberg Table From Delta Structure
  property_count: 6
  slug: iceberg-table-iceberg-table-from-delta-structure
- name: Iceberg Table Iceberg Table From Iceberg Files Structure
  property_count: 6
  slug: iceberg-table-iceberg-table-from-iceberg-files-structure
- name: Iceberg Table Iceberg Table From Iceberg Rest Structure
  property_count: 8
  slug: iceberg-table-iceberg-table-from-iceberg-rest-structure
- name: Iceberg Table Iceberg Table Like Structure
  property_count: 5
  slug: iceberg-table-iceberg-table-like-structure
- name: Iceberg Table Iceberg Table Structure
  property_count: 25
  slug: iceberg-table-iceberg-table-structure
- name: Iceberg Table Primary Key Structure
  property_count: 0
  slug: iceberg-table-primary-key-structure
- name: Iceberg Table Refresh Iceberg Table Request Structure
  property_count: 1
  slug: iceberg-table-refresh-iceberg-table-request-structure
- name: Iceberg Table Unique Key Structure
  property_count: 0
  slug: iceberg-table-unique-key-structure
- name: Image Repository Image Repository Structure
  property_count: 4
  slug: image-repository-image-repository-structure
- name: Image Repository Image Structure
  property_count: 5
  slug: image-repository-image-structure
- name: Managed Account Managed Account Structure
  property_count: 10
  slug: managed-account-managed-account-structure
- name: Network Policy Network Policy Structure
  property_count: 9
  slug: network-policy-network-policy-structure
- name: Network Rule Network Rule Structure
  property_count: 10
  slug: network-rule-network-rule-structure
- name: Notebook Notebook Structure
  property_count: 24
  slug: notebook-notebook-structure
- name: Notebook Version Details Structure
  property_count: 5
  slug: notebook-version-details-structure
- name: Notification Integration Notification Email Structure
  property_count: 3
  slug: notification-integration-notification-email-structure
- name: Notification Integration Notification Hook Structure
  property_count: 1
  slug: notification-integration-notification-hook-structure
- name: Notification Integration Notification Integration Structure
  property_count: 4
  slug: notification-integration-notification-integration-structure
- name: Notification Integration Notification Queue Aws Sns Outbound Structure
  property_count: 4
  slug: notification-integration-notification-queue-aws-sns-outbound-structure
- name: Notification Integration Notification Queue Azure Event Grid Inbound Structure
  property_count: 4
  slug: notification-integration-notification-queue-azure-event-grid-inbound-structure
- name: Notification Integration Notification Queue Azure Event Grid Outbound Structure
  property_count: 4
  slug: notification-integration-notification-queue-azure-event-grid-outbound-structure
- name: Notification Integration Notification Queue Gcp Pubsub Inbound Structure
  property_count: 2
  slug: notification-integration-notification-queue-gcp-pubsub-inbound-structure
- name: Notification Integration Notification Queue Gcp Pubsub Outbound Structure
  property_count: 2
  slug: notification-integration-notification-queue-gcp-pubsub-outbound-structure
- name: Notification Integration Notification Webhook Structure
  property_count: 3
  slug: notification-integration-notification-webhook-structure
- name: Notification Integration Webhook Secret Structure
  property_count: 3
  slug: notification-integration-webhook-secret-structure
- name: Password Policy Password Policy Structure
  property_count: 18
  slug: password-policy-password-policy-structure
- name: Pipe Pipe Structure
  property_count: 15
  slug: pipe-pipe-structure
- name: Procedure Argument Structure
  property_count: 3
  slug: procedure-argument-structure
- name: Procedure Base Language Structure
  property_count: 4
  slug: procedure-base-language-structure
- name: Procedure Call Argument List Structure
  property_count: 1
  slug: procedure-call-argument-list-structure
- name: Procedure Call Argument Structure
  property_count: 3
  slug: procedure-call-argument-structure
- name: Procedure Column Type Structure
  property_count: 2
  slug: procedure-column-type-structure
- name: Procedure Function Language Structure
  property_count: 2
  slug: procedure-function-language-structure
- name: Procedure Java Function Structure
  property_count: 3
  slug: procedure-java-function-structure
- name: Procedure Java Script Function Structure
  property_count: 0
  slug: procedure-java-script-function-structure
- name: Procedure Procedure Structure
  property_count: 14
  slug: procedure-procedure-structure
- name: Procedure Python Function Structure
  property_count: 2
  slug: procedure-python-function-structure
- name: Procedure Return Data Type Structure
  property_count: 2
  slug: procedure-return-data-type-structure
- name: Procedure Return Table Structure
  property_count: 1
  slug: procedure-return-table-structure
- name: Procedure Return Type Structure
  property_count: 1
  slug: procedure-return-type-structure
- name: Procedure Scala Function Structure
  property_count: 1
  slug: procedure-scala-function-structure
- name: Procedure Sql Function Structure
  property_count: 0
  slug: procedure-sql-function-structure
- name: Role Containing Scope Structure
  property_count: 2
  slug: role-containing-scope-structure
- name: Role Grant Of Structure
  property_count: 5
  slug: role-grant-of-structure
- name: Role Grant On Structure
  property_count: 9
  slug: role-grant-on-structure
- name: Role Grant Structure
  property_count: 5
  slug: role-grant-structure
- name: Role Role Structure
  property_count: 10
  slug: role-role-structure
- name: Role Securable Structure
  property_count: 4
  slug: role-securable-structure
- name: Schema Schema Clone Structure
  property_count: 0
  slug: schema-schema-clone-structure
- name: Schema Schema Structure
  property_count: 24
  slug: schema-schema-structure
- name: Secret Secret Structure
  property_count: 8
  slug: secret-secret-structure
- name: Sequence Sequence Structure
  property_count: 10
  slug: sequence-sequence-structure
- name: Service Grant Of Structure
  property_count: 5
  slug: service-grant-of-structure
- name: Service Job Service Structure
  property_count: 5
  slug: service-job-service-structure
- name: Service Service Container Structure
  property_count: 10
  slug: service-service-container-structure
- name: Service Service Endpoint Structure
  property_count: 6
  slug: service-service-endpoint-structure
- name: Service Service Instance Structure
  property_count: 6
  slug: service-service-instance-structure
- name: Service Service Role Grant To Structure
  property_count: 6
  slug: service-service-role-grant-to-structure
- name: Service Service Role Structure
  property_count: 3
  slug: service-service-role-structure
- name: Service Service Spec Inline Text Structure
  property_count: 1
  slug: service-service-spec-inline-text-structure
- name: Service Service Spec Stage File Structure
  property_count: 2
  slug: service-service-spec-stage-file-structure
- name: Service Service Spec Structure
  property_count: 1
  slug: service-service-spec-structure
- name: Service Service Structure
  property_count: 0
  slug: service-service-structure
- name: Snowflake Sql Rest Bind Variable Structure
  property_count: 2
  slug: snowflake-sql-rest-bind-variable-structure
- name: Snowflake Sql Rest Cancel Status Structure
  property_count: 5
  slug: snowflake-sql-rest-cancel-status-structure
- name: Snowflake Sql Rest Column Definition Structure
  property_count: 6
  slug: snowflake-sql-rest-column-definition-structure
- name: Snowflake Sql Rest Execution Stats Structure
  property_count: 4
  slug: snowflake-sql-rest-execution-stats-structure
- name: Snowflake Sql Rest Partition Info Structure
  property_count: 3
  slug: snowflake-sql-rest-partition-info-structure
- name: Snowflake Sql Rest Query Failure Status Structure
  property_count: 6
  slug: snowflake-sql-rest-query-failure-status-structure
- name: Snowflake Sql Rest Query Status Structure
  property_count: 6
  slug: snowflake-sql-rest-query-status-structure
- name: Snowflake Sql Rest Result Set Meta Data Structure
  property_count: 5
  slug: snowflake-sql-rest-result-set-meta-data-structure
- name: Snowflake Sql Rest Result Set Structure
  property_count: 7
  slug: snowflake-sql-rest-result-set-structure
- name: Snowflake Sql Rest Session Parameters Structure
  property_count: 13
  slug: snowflake-sql-rest-session-parameters-structure
- name: Snowflake Sql Rest Statement Request Structure
  property_count: 7
  slug: snowflake-sql-rest-statement-request-structure
- name: Snowflake Structure
  property_count: 0
  slug: snowflake-structure
- name: Sqlapi Cancel Status Structure
  property_count: 5
  slug: sqlapi-cancel-status-structure
- name: Sqlapi Query Failure Status Structure
  property_count: 6
  slug: sqlapi-query-failure-status-structure
- name: Sqlapi Query Status Structure
  property_count: 6
  slug: sqlapi-query-status-structure
- name: Sqlapi Result Set Structure
  property_count: 9
  slug: sqlapi-result-set-structure
- name: Stage Aws Credentials Structure
  property_count: 4
  slug: stage-aws-credentials-structure
- name: Stage Azure Credentials Structure
  property_count: 1
  slug: stage-azure-credentials-structure
- name: Stage Credentials Structure
  property_count: 1
  slug: stage-credentials-structure
- name: Stage File Transfer Material Structure
  property_count: 1
  slug: stage-file-transfer-material-structure
- name: Stage Presigned Url Request Structure
  property_count: 1
  slug: stage-presigned-url-request-structure
- name: Stage Stage File Structure
  property_count: 4
  slug: stage-stage-file-structure
- name: Stage Stage Structure
  property_count: 13
  slug: stage-stage-structure
- name: Stream Point Of Time Offset Structure
  property_count: 1
  slug: stream-point-of-time-offset-structure
- name: Stream Point Of Time Statement Structure
  property_count: 1
  slug: stream-point-of-time-statement-structure
- name: Stream Point Of Time Stream Structure
  property_count: 1
  slug: stream-point-of-time-stream-structure
- name: Stream Point Of Time Structure
  property_count: 2
  slug: stream-point-of-time-structure
- name: Stream Point Of Time Timestamp Structure
  property_count: 1
  slug: stream-point-of-time-timestamp-structure
- name: Stream Stream Clone Structure
  property_count: 2
  slug: stream-stream-clone-structure
- name: Stream Stream Source External Table Structure
  property_count: 1
  slug: stream-stream-source-external-table-structure
- name: Stream Stream Source Stage Structure
  property_count: 0
  slug: stream-stream-source-stage-structure
- name: Stream Stream Source Structure
  property_count: 4
  slug: stream-stream-source-structure
- name: Stream Stream Source Table Structure
  property_count: 2
  slug: stream-stream-source-table-structure
- name: Stream Stream Source View Structure
  property_count: 3
  slug: stream-stream-source-view-structure
- name: Stream Stream Structure
  property_count: 13
  slug: stream-stream-structure
- name: Streamlit Add Live Version Streamlit Request Version Structure
  property_count: 2
  slug: streamlit-add-live-version-streamlit-request-version-structure
- name: Streamlit Add Version From Git Streamlit Request Structure
  property_count: 1
  slug: streamlit-add-version-from-git-streamlit-request-structure
- name: Streamlit Add Version Streamlit Request Structure
  property_count: 2
  slug: streamlit-add-version-streamlit-request-structure
- name: Streamlit Commit Streamlit Request Structure
  property_count: 1
  slug: streamlit-commit-streamlit-request-structure
- name: Streamlit Streamlit Push Options Structure
  property_count: 1
  slug: streamlit-streamlit-push-options-structure
- name: Streamlit Streamlit Structure
  property_count: 19
  slug: streamlit-streamlit-structure
- name: Streamlit Streamlit Version For Git Structure
  property_count: 2
  slug: streamlit-streamlit-version-for-git-structure
- name: Streamlit Version Details Streamlit Structure
  property_count: 5
  slug: streamlit-version-details-streamlit-structure
- name: Table Constraint Structure
  property_count: 3
  slug: table-constraint-structure
- name: Table Foreign Key Structure
  property_count: 2
  slug: table-foreign-key-structure
- name: Table Primary Key Structure
  property_count: 0
  slug: table-primary-key-structure
- name: Table Table As Select Structure
  property_count: 3
  slug: table-table-as-select-structure
- name: Table Table Clone Structure
  property_count: 0
  slug: table-table-clone-structure
- name: Table Table Column Structure
  property_count: 10
  slug: table-table-column-structure
- name: Table Table Like Structure
  property_count: 1
  slug: table-table-like-structure
- name: Table Table Structure
  property_count: 25
  slug: table-table-structure
- name: Table Table Using Template Structure
  property_count: 1
  slug: table-table-using-template-structure
- name: Table Unique Key Structure
  property_count: 0
  slug: table-unique-key-structure
- name: Tag Tag Structure
  property_count: 10
  slug: tag-tag-structure
- name: Task Cron Schedule Structure
  property_count: 2
  slug: task-cron-schedule-structure
- name: Task Minutes Schedule Structure
  property_count: 1
  slug: task-minutes-schedule-structure
- name: Task Task Run Structure
  property_count: 14
  slug: task-task-run-structure
- name: Task Task Schedule Structure
  property_count: 1
  slug: task-task-schedule-structure
- name: Task Task Structure
  property_count: 25
  slug: task-task-structure
- name: User Containing Scope Structure
  property_count: 2
  slug: user-containing-scope-structure
- name: User Defined Function Argument Structure
  property_count: 3
  slug: user-defined-function-argument-structure
- name: User Defined Function Base Language Structure
  property_count: 3
  slug: user-defined-function-base-language-structure
- name: User Defined Function Column Type Structure
  property_count: 2
  slug: user-defined-function-column-type-structure
- name: User Defined Function Function Language Structure
  property_count: 3
  slug: user-defined-function-function-language-structure
- name: User Defined Function Java Function Structure
  property_count: 4
  slug: user-defined-function-java-function-structure
- name: User Defined Function Java Script Function Structure
  property_count: 0
  slug: user-defined-function-java-script-function-structure
- name: User Defined Function Python Function Structure
  property_count: 3
  slug: user-defined-function-python-function-structure
- name: User Defined Function Return Data Type Structure
  property_count: 2
  slug: user-defined-function-return-data-type-structure
- name: User Defined Function Return Table Structure
  property_count: 1
  slug: user-defined-function-return-table-structure
- name: User Defined Function Return Type Structure
  property_count: 1
  slug: user-defined-function-return-type-structure
- name: User Defined Function Scala Function Structure
  property_count: 2
  slug: user-defined-function-scala-function-structure
- name: User Defined Function Sql Function Structure
  property_count: 0
  slug: user-defined-function-sql-function-structure
- name: User Defined Function User Defined Function Structure
  property_count: 18
  slug: user-defined-function-user-defined-function-structure
- name: User Grant Structure
  property_count: 4
  slug: user-grant-structure
- name: User Securable Structure
  property_count: 3
  slug: user-securable-structure
- name: User User Structure
  property_count: 40
  slug: user-user-structure
- name: View View Column Structure
  property_count: 3
  slug: view-view-column-structure
- name: View View Structure
  property_count: 12
  slug: view-view-structure
- name: Warehouse Warehouse Structure
  property_count: 36
  slug: warehouse-warehouse-structure
jsonld:
- class_count: 0
  name: Account Context
  property_count: 0
  slug: account-context
- class_count: 0
  name: Alert Context
  property_count: 0
  slug: alert-context
- class_count: 0
  name: Api Integration Context
  property_count: 0
  slug: api-integration-context
- class_count: 0
  name: Catalog Integration Context
  property_count: 0
  slug: catalog-integration-context
- class_count: 0
  name: Common Context
  property_count: 0
  slug: common-context
- class_count: 0
  name: Compute Pool Context
  property_count: 0
  slug: compute-pool-context
- class_count: 0
  name: Cortex Analyst Context
  property_count: 0
  slug: cortex-analyst-context
- class_count: 0
  name: Cortex Inference Context
  property_count: 0
  slug: cortex-inference-context
- class_count: 0
  name: Cortex Search Service Context
  property_count: 0
  slug: cortex-search-service-context
- class_count: 0
  name: Database Context
  property_count: 0
  slug: database-context
- class_count: 0
  name: Database Role Context
  property_count: 0
  slug: database-role-context
- class_count: 0
  name: Dynamic Table Context
  property_count: 0
  slug: dynamic-table-context
- class_count: 0
  name: Event Table Context
  property_count: 0
  slug: event-table-context
- class_count: 0
  name: External Volume Context
  property_count: 0
  slug: external-volume-context
- class_count: 0
  name: Function Context
  property_count: 0
  slug: function-context
- class_count: 0
  name: Grant Context
  property_count: 0
  slug: grant-context
- class_count: 0
  name: Iceberg Table Context
  property_count: 0
  slug: iceberg-table-context
- class_count: 0
  name: Image Repository Context
  property_count: 0
  slug: image-repository-context
- class_count: 0
  name: Managed Account Context
  property_count: 0
  slug: managed-account-context
- class_count: 0
  name: Network Policy Context
  property_count: 0
  slug: network-policy-context
- class_count: 0
  name: Notebook Context
  property_count: 0
  slug: notebook-context
- class_count: 0
  name: Notification Integration Context
  property_count: 0
  slug: notification-integration-context
- class_count: 0
  name: Pipe Context
  property_count: 0
  slug: pipe-context
- class_count: 0
  name: Procedure Context
  property_count: 0
  slug: procedure-context
- class_count: 0
  name: Role Context
  property_count: 0
  slug: role-context
- class_count: 0
  name: Schema Context
  property_count: 0
  slug: schema-context
- class_count: 0
  name: Service Context
  property_count: 0
  slug: service-context
- class_count: 0
  name: Snowflake Context
  property_count: 4
  slug: snowflake-context
- class_count: 0
  name: Snowflake Sql Rest Context
  property_count: 0
  slug: snowflake-sql-rest-context
- class_count: 0
  name: Sqlapi Context
  property_count: 0
  slug: sqlapi-context
- class_count: 0
  name: Stage Context
  property_count: 0
  slug: stage-context
- class_count: 0
  name: Stream Context
  property_count: 0
  slug: stream-context
- class_count: 0
  name: Table Context
  property_count: 0
  slug: table-context
- class_count: 0
  name: Task Context
  property_count: 0
  slug: task-context
- class_count: 0
  name: User Context
  property_count: 0
  slug: user-context
- class_count: 0
  name: User Defined Function Context
  property_count: 0
  slug: user-defined-function-context
- class_count: 0
  name: View Context
  property_count: 0
  slug: view-context
- class_count: 0
  name: Warehouse Context
  property_count: 0
  slug: warehouse-context
layout: provider
mcp_servers:
- description: Snowflake ships a first-party, account-hosted MCP server. A customer creates one with CREATE MCP SERVER; Snowflake then serves it over HTTPS from the customer's own account host and wraps Snowflake-na
  name: Snowflake-managed MCP server
  slug: snowflake-managed-mcp-server
modified: '2026-09-03'
name: Snowflake
nav: Providers
network: true
overview: 'Snowflake publishes 49 API contracts indexed on the [APIs.io](https://apis.io/) network, including Artifact Repository API, Cortex Embed API, Network Rule API, and 46 more. Tagged areas include Snowflake, Data, Data Warehouse, Data Lakehouse, and Cloud Data Platform.


  The Snowflake catalog on APIs.io includes 1 event-driven AsyncAPI specification, 38 JSON-LD contexts, and 3 Spectral governance rulesets.


  Snowflake''s developer surface includes authentication, sandbox, changelog, CLI, documentation, API reference, getting-started guide, and 75 more developer resources.'
plans:
- name: Snowflake Plans Pricing
  plan_count: 4
  slug: snowflake-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Snowflake Rate Limits
  slug: snowflake-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Snowflake — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: snowflake-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Snowflake API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: snowflake-rules
- authorship: generated
  effective_rule_count: 63
  extends:
  - spectral:oas
  name: Snowflake API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 13
  slug: snowflake-spectral-rules
scopes:
- name: Snowflake Scopes
  scope_count: 5
  slug: snowflake-scopes
  summary_line: 5 scopes · authorizationCode/implicit
score:
  band: exemplar
  composite: 81.1
  coverage:
    artifact_dirs: 42
    catalog_earned: 65.0
    catalog_earned_first_party: 12.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.1
  facets:
    access_clarity: 92.1
    contract_governance: 45.5
    contract_quality: 72.6
    developer_ergonomics: 80.4
    discoverability: 57.5
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 81.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 89.4
      derived: 0
      marker_coverage: 0.0
      total: 47
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/snowflake/snowflake-2026-06-20T194110.png
security:
- kind: authentication
  name: Snowflake Authentication
  slug: snowflake-authentication
  summary_line: http-bearer/oauth2 · 4 schemes
- kind: domain-security
  name: Snowflake Domain Security
  slug: snowflake-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Snowflake Vulnerability Disclosure
  slug: snowflake-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Snowflake Trust Center
  slug: snowflake-trust-center
  summary_line: trust center published
skill_count: 6
skills:
- name: snowflake-ask-cortex-analyst
  slug: snowflake-ask-cortex-analyst
- name: snowflake-manage-warehouse
  slug: snowflake-manage-warehouse
- name: snowflake-provision-objects
  slug: snowflake-provision-objects
- name: snowflake-run-sql
  slug: snowflake-run-sql
- name: snowflake-safe-drop
  slug: snowflake-safe-drop
- name: snowflake-search-unstructured
  slug: snowflake-search-unstructured
slug: snowflake
tags:
- Snowflake
- Data
- Data Warehouse
- Data Lakehouse
- Cloud Data Platform
- Analytics
- Artificial Intelligence
- Data Engineering
- Data Governance
- SQL
- Apache Iceberg
- MCP
- T1
website: https://www.snowflake.com/
---
