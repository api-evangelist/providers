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
  - rate-limits
  - security
  trial: false
  try_now: true
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
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
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
  score: 40.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 936
  human_in_the_loop: 3
  name: Lytics Agentic Access
  operation_count: 1467
  slug: lytics-agentic-access
  summary_line: 1467 operations · 936 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: 'Account related resources of the *Lytics API*. The Account resource describes an account. An account can be a *Master* account, which means that it is a billing account. Master accounts have children '
  name: Lytics Account API
  phrasing_intents:
  - id: RetrieveASingleAccount
    intent: Get one account's details
    question: Can I look up a single Lytics account by its id?
  - id: AccountUpdate
    intent: Rename or update an account
    question: Can I change the name of an existing account?
  - id: AccountCreate
    intent: Create a child account
    question: Can I create a child account under my parent account?
  - id: AccountsList
    intent: List all accounts I can access
    question: Which accounts does my API token have access to?
  - id: postAccount
    intent: Create a child account with full profile
    question: Can I set a timezone, contact email and packages when creating a child account?
  - id: postAccountSetupJobalerts
    intent: Turn job failure email alerts on or off
    question: Can I get an email whenever an import or export job fails?
  - id: getAccountById
    intent: Get an account with its user roles
    question: Can I fetch an account and include the roles users hold on it?
  - id: postAccountById
    intent: Update an account's settings, tags or billing
    question: Can I add tags or change settings on an existing account?
  phrasing_ops: 9
  slug: lytics-account-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Account Settings describe features/settings for a Lytics account.
  name: Lytics Account Settings API
  phrasing_intents:
  - id: RetrieveASingleAccountSetting
    intent: Get the value of one account setting
    question: What is the current value of a specific account setting?
  - id: AccountSettingUpdate
    intent: Change an account setting
    question: Can I change how many days a logon session lasts for my account?
  - id: AccountSettingDelete
    intent: Reset a custom account setting
    question: Can I remove a custom value from an account setting and fall back to the default?
  - id: AccountSettingList
    intent: List all account settings
    question: Which account settings exist and what are they set to?
  phrasing_ops: 4
  slug: lytics-account-settings-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: API for creation or storage of auth tokens. Most of these tokens are created from the Integrations/Imports setup for Lytics integrations. Additionally, api tokens can be created/managed from this endp
  name: Lytics Auth API
  phrasing_intents:
  - id: RetrieveASingleAuth
    intent: Get an integration auth's public details
    question: Can I look up a stored integration credential without exposing its secrets?
  - id: CreateAuth
    intent: Create an integration auth
    question: Can I create an integration auth through the API instead of the Integrations admin page?
  - id: UpdateAuth
    intent: Update an integration auth
    question: Can I edit an existing integration auth record?
  - id: RemoveAnAuth
    intent: Delete an integration auth
    question: What happens to running imports and exports when I delete an auth?
  - id: AuthCreateToken
    intent: Create an API token
    question: How do I generate a new Lytics API token?
  phrasing_ops: 5
  slug: lytics-auth-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Create and manage credentials and access to external systems.
  name: Lytics Auths API
  phrasing_intents:
  - id: getAuth
    intent: List every saved auth in a Lytics account
    question: Which integration credentials are stored in my Lytics account right now?
  - id: postAuthAirshipConnect
    intent: Create an Airship Connect auth
    question: How do I connect Lytics to Airship Connect with a new credential?
  - id: getAuthAirshipConnectById
    intent: Get an Airship Connect auth
    question: Can I look up the details of one Airship Connect auth I already saved?
  - id: putAuthAirshipConnectById
    intent: Update an Airship Connect auth
    question: How do I change the credentials on an existing Airship Connect auth?
  - id: postAuthAirshipMasterSecret
    intent: Create an Airship master secret auth
    question: How do I store an Airship master secret in Lytics?
  - id: getAuthAirshipMasterSecretById
    intent: Get an Airship master secret auth
    question: Where can I view a saved Airship master secret authorization?
  - id: putAuthAirshipMasterSecretById
    intent: Update an Airship master secret auth
    question: How do I rotate the Airship master secret saved in an existing auth?
  - id: postAuthAlgoliaApiKey
    intent: Create an Algolia API key auth
    question: How do I give Lytics my Algolia API key?
  phrasing_ops: 379
  slug: lytics-auths-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Catalog exposes info about the schema of the data in Lytics. * **Entities** are Object Types, the primary one being a *User* although most accounts also have *Content* and *Campaign* as well. Custom o
  name: Lytics Catalog API
  phrasing_intents:
  - id: Streams
    intent: List data streams and their fields
    question: Which data streams do I have and what fields does each contain?
  - id: StreamHide
    intent: Hide or unhide a stream in the UI
    question: Can I hide a temporary stream from the Data Streams screen without deleting its data?
  - id: FieldHide
    intent: Hide or unhide a stream field in the UI
    question: Can I hide a single field of a stream from the web UI?
  - id: SchemaFields
    intent: Get the field schema for a table
    question: What fields are defined on the user table schema?
  - id: FieldInfoForTable
    intent: Get possible values for a table's fields
    question: Which values actually appear in each field of the user table?
  - id: FieldSuggest
    intent: Suggest values for a field (autocomplete)
    question: Can I get autocomplete suggestions for a field's values?
  phrasing_ops: 6
  slug: lytics-catalog-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Create and manage connections to external data sources.
  name: Lytics Connections API
  phrasing_intents:
  - id: getConnection
    intent: List data warehouse connections
    question: Which external data connections are set up on my account?
  - id: postConnection
    intent: Create a connection to an external data source
    question: How do I connect my data warehouse so I can build Cloud Connect models?
  - id: deleteConnectionById
    intent: Delete a connection
    question: How do I remove a data connection I no longer use?
  - id: getConnectionById
    intent: Get one connection's details
    question: Can I look up the settings of a single connection by its id?
  - id: putConnectionById
    intent: Update a connection's label or credentials
    question: Can I swap the auth credentials an existing connection uses?
  - id: postConnectionByIdScan
    intent: Run a sample query on an external source
    question: Can I preview sample rows from my warehouse before building a Cloud Connect model?
  - id: getConnectionByIdSchema
    intent: List the tables on a connection
    question: Which tables can I see through a given connection?
  - id: getConnectionByIdSchemaByTable
    intent: Get the columns of a table on a connection
    question: What columns does a particular table in my warehouse have?
  phrasing_ops: 8
  slug: lytics-connections-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Content APIs for Lytics Content Affinity Engine, allow for adding content into lytics, getting lists of content, and understanding the content and content-topics. **Content Classification** Content cl
  name: Lytics Content API
  phrasing_intents:
  - id: ContentTopics
    intent: List topics in the content graph
    question: Which topics does my content graph contain?
  - id: ContentTopicSummary
    intent: Get a summary of one content topic
    question: Can I see a summary for a single content topic?
  - id: ContentTopicRollupSummary
    intent: Get a summary of a topic rollup by label
    question: Can I get a summary of a topic rollup using its label?
  - id: ContentTopicRollupList
    intent: List topic rollups
    question: Which topic rollups have been set up on my account?
  - id: ContentTopicBlacklistFetch
    intent: Get the blocked topics list
    question: Which content topics are currently blocklisted?
  - id: ContentTopicBlacklistCreate
    intent: Add or remove topics on the blocklist
    question: Can I add a few topics to my blocklist without replacing the rest?
  - id: ContentTopicBlacklistUpdate
    intent: Replace the whole topic blocklist
    question: Can I overwrite my entire topic blocklist with a new set of topics?
  - id: ContentTopicRollupFetch
    intent: Get a topic rollup by id
    question: Can I fetch a single topic rollup by its id?
  phrasing_ops: 30
  slug: lytics-content-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: API for creating and managing Experiences as well as all related and/or dependent models such as but not limited to Groups, Templates, Candidates, etc.
  name: Lytics Experience API
  phrasing_intents:
  - id: ListExperience
    intent: List personalization experiences
    question: Which experiences do I have set up for personalization?
  - id: CreateExperience
    intent: Create a personalization experience
    question: What fields are required to create a new experience, like label and tactic?
  - id: FetchExperience
    intent: Get one experience
    question: Can I fetch one experience along with its templates and parent groups?
  - id: UpdateExperience
    intent: Update an experience or change its state
    question: Can I change only the state of an experience, like pausing it?
  - id: DeleteExperience
    intent: Delete an experience
    question: Is deleting an experience recoverable, or can I hard delete it?
  - id: FetchImport
    intent: List experiences importable from a provider
    question: Which existing campaigns can I import as experiences from a connected provider?
  - id: CreateImport
    intent: Import experiences from a provider
    question: Once I've listed importable experiences, how do I bring them in?
  - id: ListTemplate
    intent: List experience templates
    question: Which experience templates are available to me?
  phrasing_ops: 26
  slug: lytics-experience-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Create and manage flows that orchestrate multi-step audience journeys.
  name: Lytics Flows API
  phrasing_intents:
  - id: getFlow
    intent: List all flows and their versions
    question: Which journey flows exist on my account?
  - id: postFlow
    intent: Create or update a flow by id in the body
    question: How do I create a new customer journey flow with an entry segment?
  - id: getFlowState
    intent: List possible flow state values
    question: What step slugs and personalization keys can flows produce on my account?
  - id: deleteFlowByName
    intent: Delete a flow and all its versions
    question: How do I delete a flow entirely, every version included?
  - id: getFlowByName
    intent: Get a flow by name
    question: Can I fetch a single flow and all its versions by its name?
  - id: postFlowByName
    intent: Create or update a flow addressed by name
    question: Can I save a flow using its name in the URL as the id?
  - id: deleteFlowByNameByVersion
    intent: Delete a single flow version
    question: Can I delete just one version of a flow and keep the others?
  - id: getFlowByNameByVersion
    intent: Get one version of a flow
    question: Can I look at an older version of a flow?
  phrasing_ops: 9
  slug: lytics-flows-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Create and manage data import and export jobs.
  name: Lytics Jobs API
  phrasing_intents:
  - id: getJob
    intent: List the jobs running in my Lytics account
    question: Which data jobs are currently set up in my Lytics account?
  - id: postJobAdrollSync
    intent: Set up an AdRoll sync job
    question: How do I start syncing my audiences to AdRoll?
  - id: getJobAdrollSyncById
    intent: Check the status of an AdRoll sync job
    question: Is my AdRoll sync job still running?
  - id: putJobAdrollSyncById
    intent: Change an existing AdRoll sync job
    question: Can I rename or reconfigure an AdRoll sync after it is created?
  - id: postJobAdwordsCustomerMatch
    intent: Create an AdWords Customer Match job by email
    question: How can I push a Lytics audience into AdWords Customer Match?
  - id: postJobAdwordsCustomerMatchMobile
    intent: Create an AdWords Customer Match job for mobile IDs
    question: Can I match users to AdWords by their mobile device IDs?
  - id: getJobAdwordsCustomerMatchMobileById
    intent: Get an AdWords mobile-ID Customer Match job
    question: Is my mobile device ID match job for AdWords healthy?
  - id: putJobAdwordsCustomerMatchMobileById
    intent: Update an AdWords mobile-ID Customer Match job
    question: Can I edit the config of my AdWords mobile device ID matching job?
  phrasing_ops: 831
  slug: lytics-jobs-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: 'The Metric API provides access to a variety of metrics that are recorded in the Lytics platform. With this API, you can access segment-size metrics, events received per-hour, as well as many workflow '
  name: Lytics Metric API
  phrasing_intents:
  - id: Metric
    intent: Fetch metrics using query parameters
    question: Can I fetch segment size metrics over time with a simple GET?
  - id: Metrics
    intent: Fetch metrics using a request body
    question: Can I request metrics by posting the arguments in a JSON body?
  phrasing_ops: 2
  slug: lytics-metric-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Query time series metrics for segments, streams, experiences, and other Lytics resources.
  name: Lytics Metrics API
  phrasing_intents:
  - id: getMetric
    intent: Query a time-series metric
    question: How has a segment's size changed over the last month?
  - id: postMetric
    intent: Query several metrics in one request
    question: Can I request many metric series at once with a JSON array?
  phrasing_ops: 2
  slug: lytics-metrics-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: The ML Models API from Lytics — 3 operation(s) for ml models.
  name: Lytics ML Models API
  phrasing_intents:
  - id: getMl
    intent: List ML models
    question: Which machine learning models have been built on my account?
  - id: postMl
    intent: Create an ML model
    question: How do I train a model that predicts a target audience from a source audience?
  - id: deleteMlById
    intent: Delete an ML model
    question: How do I permanently remove an ML model?
  - id: getMlById
    intent: Get one ML model
    question: Is a particular ML model active and healthy?
  - id: putMlById
    intent: Activate, hide or relabel an ML model
    question: Can I deactivate an ML model without deleting it?
  - id: getMlByIdSummary
    intent: Get an ML model's performance summary
    question: How accurate is my ML model, according to its summary?
  phrasing_ops: 6
  slug: lytics-ml-models-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: 'Entity API, ie Personalization or Profile API. Retrieve attributes and segments an entity (most likely a user) is a member of. The *Entity* is a *User* most likely, but since Lytics is organized as a '
  name: Lytics Personalization API
  phrasing_intents:
  - id: UserMe
    intent: Get a user profile via the me alias
    question: Is there a shortcut endpoint to fetch a user profile without naming the table?
  - id: Personalization
    intent: Get a profile from any table by identity field
    question: Can I look up a customer profile by email or user id?
  - id: ProfileDeleteRequest
    intent: Request deletion of a user profile
    question: How do I delete a customer's profile for a privacy request?
  - id: WebPersonalization
    intent: Get a profile by cookie id
    question: Can I fetch a visitor's profile using only their browser cookie id?
  - id: ProfileDeletionStatus
    intent: Check a profile deletion request
    question: Has my profile deletion request finished yet?
  phrasing_ops: 5
  slug: lytics-personalization-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Get and delete user profiles.
  name: Lytics Profiles API
  phrasing_intents:
  - id: deleteAttributesByTableByKeyByValue
    intent: Delete a user's profile attributes
    question: Can I clear the stored attributes on a user without deleting the profile?
  - id: getAttributesByTableByKeyByValue
    intent: Get a user's profile attributes
    question: What custom attributes are stored on a particular user's profile?
  - id: patchAttributesByTableByKeyByValue
    intent: Update some of a user's profile attributes
    question: Can I change a couple of attributes on a profile and leave the rest alone?
  - id: putAttributesByTableByKeyByValue
    intent: Replace all of a user's profile attributes
    question: Can I overwrite every attribute on a user's profile at once?
  - id: getIdentityDeletestatusByRequestId
    intent: Check a GDPR profile deletion request
    question: Has my GDPR deletion request for a user finished yet?
  - id: postIdentityLookup
    intent: Look up a user profile with a POST body
    question: Can I look up a profile by sending the identity in a POST body instead of the URL?
  - id: deleteIdentityQueueBulkByTableByField
    intent: Queue bulk GDPR deletion of user profiles
    question: Can I submit many GDPR deletion requests in a single batch?
  - id: deleteIdentityByTableByKeyByValue
    intent: Delete one user profile for GDPR
    question: How do I honor a right-to-be-forgotten request for a single customer?
  phrasing_ops: 9
  slug: lytics-profiles-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Provider is a 3rd party Lytics Integrates with (Mailchimp, Optimizely, Mixpanel, Facebook etc)
  name: Lytics Provider API
  phrasing_intents:
  - id: ProviderList
    intent: List integration providers
    question: Which integration providers are available?
  - id: ProviderFetch
    intent: Get one integration provider
    question: Can I look up a single provider by its slug?
  - id: RemoveAProvider
    intent: Delete an integration provider
    question: Can I remove a provider by its id or slug?
  phrasing_ops: 3
  slug: lytics-provider-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Schema management api to add/edit queries and user-fields. Lytics Query Language ============================= The Lytics Query Language is used to define the transformation of uploaded records, and e
  name: Lytics Query API
  phrasing_intents:
  - id: QueryList
    intent: List data queries
    question: Which LQL queries are defined on my account?
  - id: QueryUpsert
    intent: Create or update a query
    question: Can I create or update an LQL query in one call using its alias?
  - id: QueryFetch
    intent: Get one query by alias or id
    question: Can I fetch a query by its alias instead of its id?
  - id: QueryDelete
    intent: Delete a query
    question: Can I delete a query by alias?
  - id: QueryValidation
    intent: Validate query syntax
    question: Can I check an LQL query's syntax before saving it?
  - id: QueryTestEvaluation
    intent: Test a query against sample data
    question: Can I see how a query would interpret some sample data?
  phrasing_ops: 6
  slug: lytics-query-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Create and manage reports.
  name: Lytics Reports API
  phrasing_intents:
  - id: getReport
    intent: List reports
    question: Which dashboard reports have been built on my account?
  - id: postReport
    intent: Create a report
    question: How do I start a new report to hold charts and components?
  - id: deleteReportById
    intent: Delete a report
    question: How do I delete a whole report I no longer need?
  - id: getReportById
    intent: Get one report
    question: What components make up a particular report?
  - id: putReportById
    intent: Rename or redescribe a report
    question: Can I change the title of a report after creating it?
  - id: postReportByIdComponent
    intent: Add a component to a report
    question: Can I add a new chart component to an existing report?
  - id: deleteReportByIdComponentByComponentid
    intent: Remove a component from a report
    question: Can I take one chart off a report without deleting the report?
  - id: putReportByIdComponentByComponentid
    intent: Update a component on a report
    question: Can I change the config of a chart already on a report?
  phrasing_ops: 8
  slug: lytics-reports-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Manage how data sources populate profile fields.
  name: Lytics Schema API
  phrasing_intents:
  - id: getSchema
    intent: List tables with their schemas
    question: Which data tables does my account have a schema for?
  - id: postSchemaBulk
    intent: Bulk upsert schema objects (POST)
    question: Is there a POST version of the bulk schema upsert?
  - id: putSchemaBulk
    intent: Bulk upsert schema objects (PUT)
    question: Can I create or update many schema fields and mappings in one PUT request?
  - id: postSchemaExpressionEvaluate
    intent: Test a mapping expression on one event
    question: What would a mapping expression produce for a sample event?
  - id: postSchemaLql
    intent: Update the schema from an LQL query
    question: Can I upload an LQL query to add fields and mappings to my schema?
  - id: getSchemaByTable
    intent: Get a table's schema
    question: What fields, mappings and ranks make up the user table schema?
  - id: getSchemaByTableCompare
    intent: Diff two schema versions
    question: What changed between two versions of my schema?
  - id: postSchemaByTableEvaluate
    intent: Evaluate a schema against test events
    question: Will my published schema map test events the way I expect?
  phrasing_ops: 28
  slug: lytics-schema-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Segments are named, logical expressions of users. These segments may logically be built using other segments as well. The segment api provides a list of segments built by both the admin, pre-defined s
  name: Lytics Segment API
  phrasing_intents:
  - id: SegmentList
    intent: List segments
    question: Which audience segments do I have on the user table?
  - id: SegmentCreate
    intent: Create a segment from SegmentQL
    question: How do I create a new audience segment with a SegmentQL filter?
  - id: SegmentFetch
    intent: Get a segment by id or slug
    question: Can I fetch a segment by its slug?
  - id: SegmentUpdate
    intent: Update a segment
    question: Can I change the filter or description of an existing segment?
  - id: SegmentDelete
    intent: Delete a segment
    question: Can I delete a single segment?
  - id: SegmentSize
    intent: Size an unsaved SegmentQL query
    question: How many users would match a SegmentQL filter without saving it?
  - id: SegmentValidate
    intent: Validate a segment query
    question: Can I check that a SegmentQL statement is valid before creating the segment?
  - id: SegmentSizes
    intent: Get sizes of several saved segments
    question: How many users are in each of several saved segments?
  phrasing_ops: 13
  slug: lytics-segment-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Segment Collections are grouped/named lists of segments. Segments that participate in a collection such as **Goals** are related. The Lytics App ui has one predefined collection called **Goals** which
  name: Lytics Segment Collection API
  phrasing_intents:
  - id: SegmentCollectionList
    intent: List segment collections
    question: Which segment collections exist on my account?
  - id: SegmentCollectionCreate
    intent: Create a segment collection
    question: Can I group existing segments into a named collection?
  - id: SegmentCollectionFetch
    intent: Get a segment collection
    question: Can I fetch one segment collection by slug?
  - id: SegmentCollectionUpdate
    intent: Update a segment collection
    question: Can I rename a segment collection or change its segments?
  - id: SegmentCollectionDelete
    intent: Delete a segment collection
    question: Can I delete a segment collection?
  phrasing_ops: 5
  slug: lytics-segmentcollection-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: SegmentML provides a framework for building custom machine learning models directly in Lytics. Lytics SegmentML models are self-training, continuously-updating and real-time. SegmentML models are buil
  name: Lytics Segment ML API
  phrasing_intents:
  - id: SegmentMLModelFetch
    intent: Get a SegmentML model
    question: Can I see the features and accuracy of a lookalike model I built?
  - id: SegmentMLDelete
    intent: Delete a SegmentML model
    question: Can I delete a SegmentML model I no longer need?
  - id: SegmentMLCreate
    intent: Build a SegmentML lookalike model
    question: Can I build a model that predicts which users look like a target segment?
  - id: SegmentMLDependencies
    intent: List what depends on a SegmentML model
    question: What depends on a particular SegmentML model?
  phrasing_ops: 4
  slug: lytics-segmentml-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Create and manage audience segments.
  name: Lytics Segments API
  phrasing_intents:
  - id: getSegment
    intent: List audience segments
    question: Which audience segments exist on my account?
  - id: postSegment
    intent: Create an audience segment
    question: How do I build a new audience from a SegmentQL definition?
  - id: postSegmentExcludeByOperation
    intent: Add or remove a segment on the export exclusion list
    question: Can I exclude everyone in a segment from export jobs?
  - id: deleteSegmentByIds
    intent: Delete several segments at once
    question: Can I delete a batch of segments in one call?
  - id: deleteSegmentById
    intent: Delete a single segment
    question: How do I delete one audience segment?
  - id: getSegmentById
    intent: Get one segment by id or slug
    question: How many users are in a particular segment?
  - id: putSegmentById
    intent: Update a segment's definition
    question: Can I change the rules that define an existing audience?
  phrasing_ops: 7
  slug: lytics-segments-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: 'API for creating stream models. A stream is the same as a [data stream](https://learn.lytics.com/product-docs/data-management/using-data-streams#what-are-data-streams? ) and is consumed for ingestion '
  name: Lytics Stream API
  phrasing_intents:
  - id: RetrieveASingleStream
    intent: Get a stream's settings
    question: Can I look up a stream by its id or slug?
  - id: UpdateAStream
    intent: Update a stream's settings
    question: Can I change a stream's label, description or channel?
  - id: DeleteAStream
    intent: Delete a stream
    question: Can I delete a stream I no longer collect data on?
  - id: RetrieveAListOfStreamsFromAccount
    intent: List stream records for my account
    question: Which stream records are configured on my account?
  - id: CreateAStream
    intent: Create a stream
    question: Can I register a new data stream for a channel like email or SMS?
  phrasing_ops: 5
  slug: lytics-stream-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Get metrics and events for data streams in your Lytics account.
  name: Lytics Streams API
  phrasing_intents:
  - id: getStream
    intent: List data streams
    question: Which event streams are flowing into my account?
  - id: getStreamRule
    intent: List stream rules
    question: What stream routing rules are configured?
  - id: postStreamRule
    intent: Create a stream rule
    question: How do I route events from one stream into another with a rule?
  - id: deleteStreamRuleById
    intent: Delete a stream rule
    question: How do I delete a stream rule I no longer need?
  - id: getStreamRuleById
    intent: Get one stream rule
    question: What expression does a specific stream rule apply?
  - id: postStreamRuleById
    intent: Update a stream rule (POST)
    question: Is there a POST version of updating a stream rule?
  - id: putStreamRuleById
    intent: Update a stream rule (PUT)
    question: Can I replace a stream rule's expression with a PUT?
  - id: getStreamByName
    intent: Get a stream by name
    question: What do I know about the default stream?
  phrasing_ops: 10
  slug: lytics-streams-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: '**BETA API** Subscriptions are queries into real-time events in Lytics, most commonly listening to a list of users entering/leaving segments ie _triggers_. **Common Use Cases** * Upon Entering/Leaving'
  name: Lytics Subscription API
  phrasing_intents:
  - id: SubscriptionList
    intent: List subscriptions
    question: Which webhook subscriptions do I have?
  - id: SubscriptionUpsert
    intent: Create or update a subscription
    question: Can I get a webhook when users enter or leave a segment?
  - id: SubscriptionFetch
    intent: Get a subscription
    question: Can I look at one subscription webhook's settings?
  - id: SubscriptionDelete
    intent: Delete a subscription
    question: Can I stop a webhook subscription?
  phrasing_ops: 4
  slug: lytics-subscription-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Manage Lytics system users and their access to data and resources.
  name: Lytics System API
  phrasing_intents:
  - id: getEvent
    intent: Search system events
    question: What happened on my account in the last day, according to system events?
  - id: getEventById
    intent: Get one system event
    question: Can I open the full details of a single system event?
  phrasing_ops: 2
  slug: lytics-system-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Get internal Lytics system events. These events are generally related to internal changes to state of an account. Common changes are CRUD Operations (Create, Update, Delete) of *Account*, *Admin User*
  name: Lytics System Events API
  phrasing_intents:
  - id: SystemEventsQuery
    intent: Search the account activity log
    question: Which segments were created in the last two weeks?
  - id: SystemEventFetch
    intent: Get one system event
    question: Can I fetch the details of a single system event?
  phrasing_ops: 2
  slug: lytics-system-events-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Create, manage, and test templates.
  name: Lytics Templates API
  phrasing_intents:
  - id: getTemplate
    intent: List templates
    question: Which export templates have been set up on my account?
  - id: postTemplate
    intent: Create a template
    question: How do I create a new template of a given type?
  - id: postTemplateTest
    intent: Test an unsaved template definition
    question: Can I try out a template definition before saving it?
  - id: deleteTemplateById
    intent: Delete a template
    question: How do I delete a template I no longer use?
  - id: getTemplateById
    intent: Get one template
    question: Can I look up a single template by its id?
  - id: postTemplateById
    intent: Update a template's name or type
    question: Can I rename an existing template?
  - id: getTemplateByIdDefinition
    intent: Get a template's definition body
    question: What does the actual body of a saved template contain?
  - id: postTemplateByIdTest
    intent: Test a saved template
    question: Does a saved template render correctly for a sample entity?
  phrasing_ops: 8
  slug: lytics-templates-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Info about Administrative Lytics account users * Lytics users are unique across accounts * They get *invited* to have access to your account
  name: Lytics User API
  phrasing_intents:
  - id: UserFetch
    intent: Get an admin user
    question: Can I look up one admin user on my account?
  - id: UserUpdate
    intent: Update an admin user
    question: Can I change an admin user's details or roles?
  - id: UserCreate
    intent: Invite or create an admin user
    question: How do I invite a teammate to my account?
  - id: UserList
    intent: List admin users and roles
    question: Who has admin access to my account and what roles do they have?
  - id: UserSetPassword
    intent: Set an admin user's password
    question: Can I set a new password for an admin user?
  - id: getUser
    intent: List every user on the account
    question: Which users have access to a given account, not just the admins?
  - id: postUserMePasswordreset
    intent: Change my own password
    question: How do I change the password on my own login?
  - id: deleteUserById
    intent: Remove a user's access to the account
    question: How do I revoke someone's access to my account?
  phrasing_ops: 10
  slug: lytics-user-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: 'Work is an *integration* unit, typically for imports and exports. Most run continually, while some run to completion. You generally would only use it through the Webadmin Integrations. * *Workflow* A '
  name: Lytics Work API
  phrasing_intents:
  - id: WorkList
    intent: List integration jobs
    question: Which integrations are running on my account right now?
  - id: WorkCreate
    intent: Start an integration job
    question: How do I start a new import or export job from a workflow?
  - id: WorkFetch
    intent: Get an integration job
    question: Can I check the details of one integration job?
  - id: WorkDelete
    intent: Delete an integration job
    question: Can I delete an integration job?
  - id: RetrieveWorkStatus
    intent: Check status of integration jobs
    question: Can I check the run status of my jobs to see which are paused, killed or in error-wait?
  - id: WorkCommandPost
    intent: Send a command to an integration job
    question: Can I pause or resume a running integration job?
  - id: WorkBounce
    intent: Bounce all integration jobs
    question: Can I restart every job on the account at once?
  phrasing_ops: 7
  slug: lytics-work-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Workflow is a specification for a work unit
  name: Lytics Workflow API
  phrasing_intents:
  - id: RetrieveWorkflowList
    intent: List available workflow types
    question: Which workflow types can I build an integration job from?
  phrasing_ops: 1
  slug: lytics-workflow-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: Create and manage data models and their record stores.
  name: Lytics Data models API
  phrasing_intents:
  - id: getDataDatamodelSize
    intent: Get record store sizes for several data models
    question: How much storage are several of my data models taking up at once?
  - id: getDataDatamodelByIdSize
    intent: Get one data model's record store size
    question: How big is the record store behind a single data model?
  - id: deleteDatamodel
    intent: Delete several data models at once
    question: Can I delete a batch of data models in one call?
  - id: getDatamodel
    intent: List data models
    question: Which data models are defined on my account?
  - id: postDatamodel
    intent: Create a data model from a SQL query
    question: How do I build a Cloud Connect data model from SQL on my warehouse?
  - id: deleteDatamodelById
    intent: Delete a single data model
    question: How do I remove one data model I no longer need?
  - id: getDatamodelById
    intent: Get one data model
    question: What SQL and sync settings does a specific data model use?
  - id: putDatamodelById
    intent: Update a data model's SQL or sync schedule
    question: Can I change the SQL behind an existing data model?
  phrasing_ops: 10
  slug: lytics-data-models-api
- baseURL: https://api.lytics.io/v2
  baseurl_source: declared
  description: APIs for collecting or uploading data.
  name: Lytics Data Upload API
  phrasing_intents:
  - id: BulkCSVUpload
    intent: Bulk upload a CSV file to a stream
    question: Can I bulk load a gzipped CSV file into a data stream?
  - id: BulkJSONUpload
    intent: Bulk upload JSON records to a stream
    question: Can I bulk upload a file of JSON records to a stream?
  - id: DataJSONUpload
    intent: Send JSON events to a stream
    question: Can I post individual JSON events to a stream using an access token?
  phrasing_ops: 3
  slug: lytics-data-upload-api
artifact_total: 76
asyncapis:
- description: ''
  name: Lytics Webhooks
  slug: lytics-webhooks
collections:
- collection_type: open
  name: V1 Lytics API
  slug: open-lytics-api-v1
- collection_type: open
  name: Lytics API
  slug: open-lytics-api-v2
common:
- group: other
  href: https://artifacts.apis.io/lytics/capabilities/lytics-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/lytics-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/lytics/overlays/lytics-api-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lytics-api-v2-overlay.yaml
- group: other
  href: https://artifacts.apis.io/lytics/overlays/lytics-api-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/lytics-api-v1-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/lytics/agentic-access/lytics-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/lytics-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/lytics/security/lytics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lytics-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/lytics/authentication/lytics-authentication.yml
  title: ''
  type: Authentication
  url: authentication/lytics-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.lytics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lytics.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/lytics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lytics
- group: company
  title: ''
  type: Blog
  url: https://www.lytics.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lytics.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://lytics.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://x.com/lyticsio
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.lytics.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://support.lytics.com/hc/en-us
- group: commercial
  href: https://artifacts.apis.io/lytics/plans/lytics-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lytics-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/lytics/rate-limits/lytics-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/lytics-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/lytics/finops/lytics-finops.yml
  title: ''
  type: FinOps
  url: finops/lytics-finops.yml
- group: docs
  title: ''
  type: OpenAPI Source
  url: https://dash.readme.com/api/v1/api-registry/1y876emrv8pb2i
- group: build
  href: https://artifacts.apis.io/lytics/packages/lytics-packages.yml
  title: ''
  type: Packages
  url: packages/lytics-packages.yml
- group: build
  href: https://artifacts.apis.io/lytics/packages/lytics-packages.yml
  title: ''
  type: SDKs
  url: packages/lytics-packages.yml
- group: agent
  href: https://artifacts.apis.io/lytics/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/lytics/mcp/lytics-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/lytics-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/lytics/llms/lytics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lytics-llms.txt
- group: design
  href: https://artifacts.apis.io/lytics/conventions/lytics-conventions.yml
  title: ''
  type: Conventions
  url: conventions/lytics-conventions.yml
- group: design
  href: https://artifacts.apis.io/lytics/errors/lytics-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/lytics-error-codes.yml
- group: design
  href: https://artifacts.apis.io/lytics/lifecycle/lytics-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/lytics-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/lytics/conformance/lytics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lytics-conformance.yml
- group: design
  href: https://artifacts.apis.io/lytics/data-model/lytics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lytics-data-model.yml
- group: build
  href: https://artifacts.apis.io/lytics/cli/lytics-cli.yml
  title: ''
  type: CLI
  url: cli/lytics-cli.yml
- group: design
  href: https://artifacts.apis.io/lytics/components/lytics-components.yml
  title: ''
  type: Components
  url: components/lytics-components.yml
- group: design
  href: https://artifacts.apis.io/lytics/asyncapi/lytics-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/lytics-webhooks.yml
- group: auth
  href: https://artifacts.apis.io/lytics/security/lytics-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lytics-trust-center.yml
- group: design
  href: https://artifacts.apis.io/lytics/vocabulary/lytics-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lytics-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/lytics/rules/lytics-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/lytics-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/lytics/json-ld/lytics-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lytics-context.jsonld
- group: docs
  href: https://artifacts.apis.io/lytics/json-schema/lytics-user-profile-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/lytics-user-profile-schema.json
- group: docs
  href: https://artifacts.apis.io/lytics/json-schema/lytics-collect-event-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/lytics-collect-event-schema.json
- group: docs
  href: https://artifacts.apis.io/lytics/json-schema/lytics-segment-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/lytics-segment-schema.json
- group: build
  href: https://artifacts.apis.io/lytics/examples/lytics-user-profile-example.json
  title: ''
  type: Examples
  url: examples/lytics-user-profile-example.json
- group: build
  href: https://artifacts.apis.io/lytics/examples/lytics-collect-event-example.json
  title: ''
  type: Examples
  url: examples/lytics-collect-event-example.json
- group: build
  href: https://artifacts.apis.io/lytics/examples/lytics-segment-scan-request-example.json
  title: ''
  type: Examples
  url: examples/lytics-segment-scan-request-example.json
- group: build
  href: https://artifacts.apis.io/lytics/examples/lytics-segment-scan-response-example.json
  title: ''
  type: Examples
  url: examples/lytics-segment-scan-response-example.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lytics.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lytics.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lytics.com/reference/getting-started
- group: start
  title: ''
  type: Quickstart
  url: https://docs.lytics.com/docs/developer-quickstart
- group: start
  title: ''
  type: SignUp
  url: https://app.lytics.com/register
- group: start
  title: ''
  type: Login
  url: https://app.lytics.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lytics.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lytics.com/privacy-policy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/lytics-cdp/lytics-s-public-workspace
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lytics
- group: operate
  title: ''
  type: Community
  url: https://docs.lytics.com/discuss
- group: auth
  title: ''
  type: Compliance
  url: https://docs.lytics.com/docs/compliance
created: '2026-06-13'
description: Lytics is a customer data platform (CDP) that provides two concurrent REST APIs for managing unified user profiles, behavioral audiences, content affinity scoring, campaign flows, and real-time personalization. The v2 API (886 paths / 1,331 operations) covers accounts, authorizations, connections, schema and identity configuration, data models, streams, jobs and ML models; the v1 API still owns data collection, personalization, entity lookup and content classification. Lytics ingests data from 100+ sources, builds predictive audiences, and activates them across advertising networks, email providers, data warehouses and on-site personalization. Lytics joined Contentstack in January 2025.
examples:
- key_count: 7
  name: Lytics Collect Event Example
  slug: lytics-collect-event-example
- key_count: 1
  name: Lytics Segment Scan Request Example
  slug: lytics-segment-scan-request-example
- key_count: 5
  name: Lytics Segment Scan Response Example
  slug: lytics-segment-scan-response-example
- key_count: 11
  name: Lytics User Profile Example
  slug: lytics-user-profile-example
finops:
- has_sources: true
  method: derived
  name: Lytics Finops
  primary_unit: ''
  service_category: ''
  slug: lytics-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lytics.png
json_schemas:
- name: Lytics Collect Event
  property_count: 7
  slug: lytics-collect-event
- name: Lytics Segment
  property_count: 10
  slug: lytics-segment
- name: Lytics User Profile
  property_count: 11
  slug: lytics-user-profile
jsonld:
- class_count: 8
  name: Lytics Context
  property_count: 32
  slug: lytics-context
layout: provider
modified: '2026-08-13'
name: Lytics
nav: Providers
network: true
overview: 'Lytics publishes 34 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Account Settings API, Auth API, and 31 more. Tagged areas include Customer Data Platform, CDP, Personalization, Segmentation, and User Profiles.


  The Lytics catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Lytics'' developer surface includes authentication, documentation, engineering blog, pricing, changelog, support, CLI, and 49 more developer resources.'
plans:
- name: Lytics Plans Pricing
  plan_count: 3
  slug: lytics-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Lytics Rate Limits
  slug: lytics-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Lytics — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: lytics-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 68.7
  coverage:
    artifact_dirs: 35
    catalog_earned: 67.8
    catalog_earned_first_party: 12.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.9
  facets:
    access_clarity: 81.6
    contract_governance: 28.0
    contract_quality: 65.4
    developer_ergonomics: 77.4
    discoverability: 73.2
    operational_transparency: 42.1
  previous_composite: 65.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 34
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/lytics/lytics-2026-06-20T184816.png
security:
- kind: authentication
  name: Lytics Authentication
  slug: lytics-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Lytics Domain Security
  slug: lytics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Lytics Trust Center
  slug: lytics-trust-center
  summary_line: trust center published
skill_count: 23
skills:
- name: account-sync
  slug: lytics-account-sync
- name: audience-advisor
  slug: lytics-audience-advisor
- name: audience-builder
  slug: lytics-audience-builder
- name: audience-snapshot
  slug: lytics-audience-snapshot
- name: campaign-flow-builder
  slug: lytics-campaign-flow-builder
- name: connection-manager
  slug: lytics-connection-manager
- name: data-health-monitor
  slug: lytics-data-health-monitor
- name: entity-lookup
  slug: lytics-entity-lookup
- name: export-debugger
  slug: lytics-export-debugger
- name: filterql-builder
  slug: lytics-filterql-builder
- name: flow-manager
  slug: lytics-flow-manager
- name: integration-advisor
  slug: lytics-integration-advisor
- name: integration-setup
  slug: lytics-integration-setup
- name: job-manager
  slug: lytics-job-manager
- name: lytics-agent
  slug: lytics-lytics-agent
- name: profile-explorer
  slug: lytics-profile-explorer
- name: profile-investigator
  slug: lytics-profile-investigator
- name: schema-discovery
  slug: lytics-schema-discovery
- name: schema-manager
  slug: lytics-schema-manager
- name: schema-optimizer
  slug: lytics-schema-optimizer
- name: segment-manager
  slug: lytics-segment-manager
- name: stream-inspector
  slug: lytics-stream-inspector
- name: webhook-template-builder
  slug: lytics-webhook-template-builder
slug: lytics
tags:
- Customer Data Platform
- CDP
- Personalization
- Segmentation
- User Profiles
- Behavioral Analytics
- Content Affinity
- Real-Time Data
- Marketing Automation
- Audience Activation
website: https://www.lytics.com/
---
