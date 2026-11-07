---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
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
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 261
  human_in_the_loop: 5
  name: Tricentis Agentic Access
  operation_count: 507
  slug: tricentis-agentic-access
  summary_line: 507 operations · 261 acting · 5 human-in-the-loop
api_count: 8
apis:
- baseURL: https://dataexport-0.qtestnet.com/uta/api/v1
  baseurl_source: declared
  description: The AccessFiles API from Tricentis — 2 operation(s) for accessfiles.
  name: Tricentis Access Files API
  phrasing_intents:
  - id: getFiles
    intent: List downloadable data files
    question: Which data export files are available for my organization to download?
  - id: getFileByFilepath
    intent: Download a data file
    question: Can I download one parquet part file by its full path?
  phrasing_ops: 2
  slug: tricentis-accessfiles-api
- baseURL: https://pulse-us-east-1.qtestnet.com/api
  baseurl_source: declared
  description: Action API
  name: Tricentis Action API
  phrasing_intents:
  - id: getActions
    intent: List a project's Pulse actions
    question: Which automation actions are defined in my Pulse project?
  - id: postActions
    intent: Create a Pulse action
    question: How do I add a new scripted action to a Pulse project?
  - id: getActionsById
    intent: Get a Pulse action
    question: What code and description does a given Pulse action have?
  - id: putActionsById
    intent: Replace a Pulse action
    question: Can I fully replace an existing action's name and code?
  - id: patchActionsById
    intent: Patch a Pulse action
    question: Can I rename a Pulse action with a PATCH request?
  - id: deleteActionsById
    intent: Delete a Pulse action
    question: How do I remove an action I no longer need from Pulse?
  phrasing_ops: 6
  slug: tricentis-action-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Administration of users API from Tricentis — 1 operation(s) for administration of users.
  name: Tricentis Administration of users API
  phrasing_intents:
  - id: delete_2
    intent: Delete a user by login
    question: Can I delete a user account by login?
  phrasing_ops: 1
  slug: tricentis-administration-of-users-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Attachment API
  name: Tricentis Attachment API
  phrasing_intents:
  - id: search
    intent: Search attachments across a project
    question: How do I find all attachments on defects in a project?
  - id: getAttachmentsOf
    intent: List attachments of one object
    question: What files are attached to this test case or defect?
  - id: getAttachment
    intent: Download an attachment
    question: How do I download a specific attachment?
  - id: upload
    intent: Upload an attachment to an object
    question: How do I attach a screenshot to a defect?
  - id: deleteByBlobHandleId
    intent: Delete an attachment from an object
    question: How do I remove an attachment from a defect?
  phrasing_ops: 5
  slug: tricentis-attachment-api
- baseURL: https://api.ttm4j.tricentis.com
  baseurl_source: declared
  description: The Attachments API from Tricentis — 4 operation(s) for attachments.
  name: Tricentis Attachments API
  phrasing_intents:
  - id: getV1ProjectsByProjectKeyTestRunsByTestRunKeyAttachments
    intent: List attachments on a test run
    question: Which files are attached to a test run?
  - id: postV1ProjectsByProjectKeyTestRunsByTestRunKeyAttachments
    intent: Start an attachment upload to a test run
    question: How do I attach a screenshot to a whole test run?
  - id: getV1ProjectsByProjectKeyTestRunsAttachmentsByAttachmentId
    intent: Get a test run attachment's link
    question: Can I get a download link for one attachment by its id?
  - id: postV1ProjectsByProjectKeyTestRunsByTestRunKeyStepsByStepNumberAttachments
    intent: Start an attachment upload to a run step
    question: Can I attach evidence to one specific step of a test run?
  - id: putV1ProjectsByProjectKeyTestRunsAttachmentsById
    intent: Confirm an attachment finished uploading
    question: How can I check that my attachment actually reached storage?
  phrasing_ops: 5
  slug: tricentis-attachments-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Authentication Systems API
  name: Tricentis Auth Systems API
  phrasing_intents:
  - id: getAll
    intent: List authentication systems
    question: Which authentication systems, like LDAP or SSO, are configured?
  - id: importLDapUsers
    intent: Link users to LDAP accounts
    question: How do I associate existing users with their LDAP accounts?
  - id: getAllLdapUsers
    intent: List unmapped LDAP users
    question: Which LDAP users haven't been mapped to an account yet?
  phrasing_ops: 3
  slug: tricentis-auth-systems-api
- baseURL: https://parameter-1.qtestnet.com
  baseurl_source: declared
  description: Authentication public APIs
  name: Tricentis Authentication API
  phrasing_intents:
  - id: postOauthV1Login
    intent: Sign in with a username and password
    question: How do I get an access token using my qTest username and password?
  - id: postOauthV1TokenLogin
    intent: Sign in with a qTest API token
    question: Can I authenticate with an API token instead of a password?
  - id: getOauthV1Logout
    intent: Log out of qTest
    question: How do I end my current qTest session?
  phrasing_ops: 3
  slug: tricentis-authentication-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Automation Job API
  name: Tricentis Automation Job API
  phrasing_intents:
  - id: searchAutomationAgents
    intent: Search automation agents
    question: Which automation agents are available in my projects?
  - id: createSchedule
    intent: Schedule an automation run on an agent
    question: How do I kick off automated test runs on an agent right away?
  phrasing_ops: 2
  slug: tricentis-automation-job-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The bridgerequirementsetlinks API from Tricentis — 2 operation(s) for bridgerequirementsetlinks.
  name: Tricentis Bridgerequirementsetlinks API
  phrasing_intents:
  - id: getBridgerequirementsetlinks
    intent: List requirement-set link records
    question: Which requirements are linked to which requirement sets in the analytics feed?
  - id: getBridgerequirementsetlinks({id})
    intent: Get one requirement-set link by key
    question: How can I read a single requirement set link record by its key?
  phrasing_ops: 2
  slug: tricentis-bridgerequirementsetlinks-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Build API
  name: Tricentis Build API
  phrasing_intents:
  - id: getBuilds
    intent: List builds under a release
    question: Which builds belong to a given release?
  - id: create
    intent: Create a build under a release
    question: How do I add a new build to a release?
  - id: get
    intent: Get a build
    question: How can I look up one build's details?
  - id: update
    intent: Update a build
    question: Can I rename a build or change its properties?
  - id: delete
    intent: Delete a build
    question: Can I delete a build from a release?
  phrasing_ops: 5
  slug: tricentis-build-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The builds API from Tricentis — 2 operation(s) for builds.
  name: Tricentis Builds API
  phrasing_intents:
  - id: getBuilds
    intent: List builds
    question: Which builds are recorded in the test analytics data?
  - id: getBuilds({id})
    intent: Get a build by key
    question: How do I look up one build by its key?
  phrasing_ops: 2
  slug: tricentis-builds-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Common API
  name: Tricentis Common API
  phrasing_intents:
  - id: updateCustomFieldStatus
    intent: Activate or deactivate custom fields
    question: How do I turn custom fields on or off for test cases?
  - id: editSystemField
    intent: Edit a system field
    question: Can I relabel a built-in system field like Priority?
  phrasing_ops: 2
  slug: tricentis-common-api
- baseURL: https://pulse-us-east-1.qtestnet.com/api
  baseurl_source: declared
  description: Constant API
  name: Tricentis Constant API
  phrasing_intents:
  - id: getConstants
    intent: List a project's Pulse constants
    question: Which constants are defined for my Pulse project?
  - id: postConstants
    intent: Create a Pulse constant
    question: How do I store a reusable value as a Pulse constant?
  - id: getConstantsById
    intent: Get a Pulse constant
    question: What value does a given Pulse constant hold?
  - id: putConstantsById
    intent: Replace a Pulse constant
    question: Can I overwrite a constant's name, value and hidden flag in one PUT?
  - id: patchConstantsById
    intent: Patch a Pulse constant
    question: Can I change only a constant's value with PATCH?
  - id: deleteConstantsById
    intent: Delete a Pulse constant
    question: How do I remove a constant from a Pulse project?
  phrasing_ops: 6
  slug: tricentis-constant-api
- baseURL: https://api.ttm4j.tricentis.com
  baseurl_source: declared
  description: The Cycles API from Tricentis — 3 operation(s) for cycles.
  name: Tricentis Cycles API
  phrasing_intents:
  - id: postV1ProjectsByProjectKeyCycles
    intent: Create test cycles
    question: How do I create a new test cycle for a Jira project?
  - id: putV1ProjectsByProjectKeyCyclesByCycleId
    intent: Update a test cycle
    question: Can I reassign a test cycle to a different person?
  - id: getV1ProjectsByProjectKeyCyclesSearch
    intent: Search test cycles
    question: Which test cycles exist for a given release version?
  phrasing_ops: 3
  slug: tricentis-cycles-api
- baseURL: https://parameter-1.qtestnet.com
  baseurl_source: declared
  description: Dataset public APIs
  name: Tricentis Datasets API
  phrasing_intents:
  - id: postApiV1DataSetsCreate
    intent: Create a dataset
    question: How do I create a new test dataset?
  - id: getApiV1DataSetsById
    intent: Get a dataset
    question: Can I retrieve one dataset by its id?
  - id: deleteApiV1DataSetsById
    intent: Delete a dataset
    question: How do I delete a single dataset?
  - id: putApiV1DataSetsById
    intent: Update a dataset
    question: Can I rename a dataset or change its description?
  - id: postApiV1DataSetsQuery
    intent: Search datasets
    question: Which datasets have a name containing a keyword?
  - id: postApiV1DataSetsBulkDelete
    intent: Delete several datasets
    question: Can I delete many datasets in one call?
  - id: putApiV1DataSetsStatus
    intent: Change the status of several datasets
    question: How do I deactivate a batch of datasets at once?
  - id: postApiV1DataSetsImport
    intent: Import datasets from Excel
    question: Can I import datasets from an Excel workbook?
  phrasing_ops: 11
  slug: tricentis-datasets-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Defect API
  name: Tricentis Defect API
  phrasing_intents:
  - id: submitDefect
    intent: Submit a defect
    question: How do I log a new bug in qTest?
  - id: getLastChanged
    intent: List recently updated defects
    question: Which defects changed since yesterday?
  - id: getDefect
    intent: Get a defect
    question: How do I look up a single defect?
  - id: updateDefect
    intent: Update a defect
    question: How do I change the status or severity of a defect?
  - id: getComments
    intent: List comments on a defect
    question: What comments are on this defect?
  - id: addComment
    intent: Comment on a defect
    question: How do I add a comment to a defect?
  - id: getDefectCommentById
    intent: Get one comment on a defect
    question: How do I fetch a single comment on a defect?
  - id: updateComment
    intent: Edit a comment on a defect
    question: Can I edit a comment on a defect?
  phrasing_ops: 9
  slug: tricentis-defect-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The defects API from Tricentis — 4 operation(s) for defects.
  name: Tricentis Defects API
  phrasing_intents:
  - id: getDefects
    intent: List defects in the analytics feed
    question: Which defects are recorded in the test analytics data?
  - id: getDefects({id})
    intent: Get a defect by key
    question: Where can I read one defect record by its key?
  - id: postV1ProjectsByProjectKeyTestRunsByTestRunKeyDefects
    intent: Create a defect from a test run
    question: How do I raise a new Jira bug from a failed test run?
  - id: postV1ProjectsByProjectKeyTestRunsByTestRunKeyDefectsLink
    intent: Link existing defects to a test run
    question: Can I link a Jira issue that already exists to a test run?
  phrasing_ops: 4
  slug: tricentis-defects-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The defecttestrunlogs API from Tricentis — 2 operation(s) for defecttestrunlogs.
  name: Tricentis Defecttestrunlogs API
  phrasing_intents:
  - id: getDefecttestrunlogs
    intent: List defect to test run log links
    question: Which test run logs are tied to which defects?
  - id: getDefecttestrunlogs('{id}')
    intent: Get a defect run log link by key
    question: How can I read one defect to run log record by its key?
  phrasing_ops: 2
  slug: tricentis-defecttestrunlogs-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Deletion Policies API from Tricentis — 2 operation(s) for deletion policies.
  name: Tricentis Deletion Policies API
  phrasing_intents:
  - id: list
    intent: List deletion policies in a workspace
    question: What automatic deletion policies are set up for my workspace?
  - id: create
    intent: Create a deletion policy
    question: How do I set up a policy that deletes old test results automatically?
  - id: get
    intent: Get a deletion policy
    question: How do I see the details of one deletion policy?
  - id: put
    intent: Replace a deletion policy
    question: Can I overwrite every field of an existing deletion policy?
  - id: delete
    intent: Delete a deletion policy
    question: How do I remove a deletion policy?
  - id: patch
    intent: Partially update a deletion policy
    question: Can I change only the deletion setting of a policy and leave the filter alone?
  phrasing_ops: 6
  slug: tricentis-deletion-policies-api
- baseURL: https://pulse-us-east-1.qtestnet.com/api
  baseurl_source: declared
  description: Execution API
  name: Tricentis Execution API
  phrasing_intents:
  - id: getExecutions
    intent: List Pulse rule executions
    question: Which Pulse action executions ran in a time window?
  - id: getExecutionsById
    intent: Get a Pulse execution
    question: What was the outcome of one Pulse action execution?
  phrasing_ops: 2
  slug: tricentis-execution-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The executionsummaries API from Tricentis — 2 operation(s) for executionsummaries.
  name: Tricentis Executionsummaries API
  phrasing_intents:
  - id: getExecutionsummaries
    intent: List execution summaries
    question: What do the execution summary records show across my tests?
  - id: getExecutionsummaries({id})
    intent: Get an execution summary by key
    question: How do I read one execution summary record?
  phrasing_ops: 2
  slug: tricentis-executionsummaries-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Field API
  name: Tricentis Field API
  phrasing_intents:
  - id: getAllSiteFields
    intent: List site-level fields of an object type
    question: What site-wide fields exist for test cases across all projects?
  - id: createCustomSiteField
    intent: Create a site-level custom field
    question: How do I add a custom field that applies at the site level for every project?
  - id: getCustomSiteField
    intent: Get a site-level custom field
    question: How can I look up one site-level custom field's settings?
  - id: updateCustomSiteField
    intent: Update a site-level custom field
    question: Can I rename or deactivate a site-wide custom field?
  - id: deleteCustomSiteField
    intent: Delete a site-level custom field
    question: Can I delete a custom field defined at the site level?
  - id: getSiteFieldAllowedValues
    intent: List allowed values of a site field
    question: Which options can be picked in a site-level combo box field?
  - id: createSiteFieldAllowedValues
    intent: Add allowed values to a site field
    question: How many new options can I add to a site-level dropdown field at once?
  - id: updateSiteFieldAllowedValues
    intent: Update an allowed value of a site field
    question: Can I change the label or color of one option in a site-level field?
  phrasing_ops: 18
  slug: tricentis-field-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The folderhierarchies API from Tricentis — 2 operation(s) for folderhierarchies.
  name: Tricentis Folderhierarchies API
  phrasing_intents:
  - id: getFolderhierarchies
    intent: List folder hierarchies
    question: How are test folders nested across my projects?
  - id: getFolderhierarchies({projectid})
    intent: Get a project's folder hierarchy
    question: What does the folder tree of one project look like?
  phrasing_ops: 2
  slug: tricentis-folderhierarchies-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The folders API from Tricentis — 4 operation(s) for folders.
  name: Tricentis Folders API
  phrasing_intents:
  - id: getFolders
    intent: List folders in the analytics feed
    question: Which folders appear in the test analytics data?
  - id: getFolders({id})
    intent: Get an analytics folder by key
    question: How do I read one folder record from the analytics feed?
  - id: getV1ProjectsByProjectKeyFolders
    intent: List test case folders in a Jira project
    question: Which test case folders exist in my Jira project?
  - id: postV1ProjectsByProjectKeyFolders
    intent: Create test case folders
    question: How do I create new test case folders in a Jira project?
  - id: putV1ProjectsByProjectKeyFoldersByFolderId
    intent: Rename or move a test case folder
    question: Can I move a test folder under a different parent?
  phrasing_ops: 5
  slug: tricentis-folders-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: User Group API
  name: Tricentis Groups API
  phrasing_intents:
  - id: getAllUserGroups
    intent: List user groups
    question: Which user groups exist on the instance?
  - id: createCustomUserGroup
    intent: Create a custom user group
    question: How do I create a custom user group with specific permissions?
  phrasing_ops: 2
  slug: tricentis-groups-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Information API from Tricentis — 2 operation(s) for information.
  name: Tricentis Information API
  phrasing_intents:
  - id: GetInformation
    intent: Get NeoLoad Web version and resource info
    question: What version of NeoLoad Web am I connected to?
  - id: GetUsage
    intent: Get usage data
    question: How much have we used NeoLoad Web this month?
  phrasing_ops: 2
  slug: tricentis-information-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Infrastructure Providers API from Tricentis — 1 operation(s) for infrastructure providers.
  name: Tricentis Infrastructure Providers API
  phrasing_intents:
  - id: list_1
    intent: List infrastructure providers
    question: Which infrastructure providers are configured on my account?
  phrasing_ops: 1
  slug: tricentis-infrastructure-providers-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Integration Settings
  name: Tricentis Integration Settings API
  phrasing_intents:
  - id: getConnections
    intent: List a project's Jira connections
    question: Which Jira connections are set up for my qTest project?
  - id: addNewConnection
    intent: Connect a project to a Jira server
    question: How do I connect a qTest project to our Jira instance?
  - id: getAuthorizeURL
    intent: Get the OAuth authorize URL for Jira Server
    question: Where do I get the OAuth authorization link to connect Jira Server or Data Center?
  - id: updateIntegrationConnectionStatus
    intent: Activate or deactivate a Jira connection
    question: Can I temporarily turn off a Jira connection without deleting it?
  - id: deleteConnection
    intent: Delete a Jira connection
    question: Can I permanently remove a Jira connection from a project?
  - id: configurePopulatingJiraUnlinkedDefects
    intent: Toggle storing unlinked Jira defects
    question: Can qTest pull in Jira defects that aren't linked to any test run?
  - id: getDefectMappings
    intent: List defect mappings of a Jira connection
    question: Which Jira issue types are mapped to qTest defects on this connection?
  - id: addNewDefectMapping
    intent: Add a defect mapping to a Jira connection
    question: How can I map a new Jira issue type to qTest defects?
  phrasing_ops: 21
  slug: tricentis-integration-settings-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The latestrunlogs API from Tricentis — 2 operation(s) for latestrunlogs.
  name: Tricentis Latestrunlogs API
  phrasing_intents:
  - id: getLatestrunlogs
    intent: List latest test run logs
    question: What is the most recent run log for each test run?
  - id: getLatestrunlogs({testrunlogid})
    intent: Get a latest run log by key
    question: How can I read one latest run log by its run log id?
  phrasing_ops: 2
  slug: tricentis-latestrunlogs-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The latesttestrunstatuses API from Tricentis — 2 operation(s) for latesttestrunstatuses.
  name: Tricentis Latesttestrunstatuses API
  phrasing_intents:
  - id: getLatesttestrunstatuses
    intent: List latest test run statuses
    question: What is the current status of each of my test runs?
  - id: getLatesttestrunstatuses({id})
    intent: Get a latest test run status by key
    question: How do I read the latest status record of one test run?
  phrasing_ops: 2
  slug: tricentis-latesttestrunstatuses-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Login API
  name: Tricentis Login API
  phrasing_intents:
  - id: tokenStatus
    intent: Check an access token's status
    question: Is my API access token still valid?
  - id: postAccessToken
    intent: Log in and get an access token
    question: How do I authenticate to qTest Manager and get an access token?
  phrasing_ops: 2
  slug: tricentis-login-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Module API
  name: Tricentis Module API
  phrasing_intents:
  - id: getSubModulesOf
    intent: List or search modules
    question: What modules are in my project's test design tree?
  - id: createModule
    intent: Create a module
    question: How do I create a folder-like module to organize test cases?
  - id: getModule
    intent: Get a module
    question: How do I fetch one module's details?
  - id: updateModule
    intent: Update or move a module
    question: How do I rename a module?
  - id: deleteModule
    intent: Delete a module
    question: How do I delete a module?
  phrasing_ops: 5
  slug: tricentis-module-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Object Link API
  name: Tricentis Object Link API
  phrasing_intents:
  - id: find
    intent: Get objects linked to given objects
    question: Which requirements are linked to these test cases?
  - id: linkArtifacts
    intent: Link objects by ID
    question: How do I link test cases to a requirement by their IDs?
  - id: unlinkArtifacts
    intent: Unlink objects by ID
    question: Can I remove the link between a requirement and its test cases using IDs?
  - id: linkArtifactsByPid
    intent: Link defects to a test step or log by PID
    question: Can I attach existing defects or Jira defect IDs to a failed test log?
  - id: unlinkArtifactsByPid
    intent: Unlink defects from a test step or log by PID
    question: How do I remove a defect link from a test log using the defect PID?
  phrasing_ops: 5
  slug: tricentis-object-link-api
- baseURL: https://parameter-1.qtestnet.com
  baseurl_source: declared
  description: Parameter public APIs
  name: Tricentis Parameters API
  phrasing_intents:
  - id: postApiV1ParametersCreate
    intent: Create a test parameter
    question: How do I create a new test parameter for my projects?
  - id: postApiV1ParametersQuery
    intent: Search parameters
    question: Which parameters are not used by any test case?
  - id: postApiV1ParametersBulkQuery
    intent: Look up parameters by exact identifiers
    question: Can I fetch several parameters at once by a list of identifiers?
  - id: getApiV1ParametersById
    intent: Get a parameter
    question: Can I retrieve a single parameter by its id?
  - id: deleteApiV1ParametersById
    intent: Delete or archive a parameter
    question: Does deleting a parameter archive it unless I force it?
  - id: putApiV1ParametersById
    intent: Update a parameter
    question: How do I rename a parameter or change its status?
  - id: postApiV1ParametersBulkDelete
    intent: Delete several parameters
    question: Can I delete many parameters in one request?
  - id: postApiV1ParametersBulkArchive
    intent: Archive several parameters
    question: Can I archive a group of parameters at once?
  phrasing_ops: 16
  slug: tricentis-parameters-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Project API
  name: Tricentis Project API
  phrasing_intents:
  - id: getProjects
    intent: List projects I can access
    question: Which qTest projects do I have access to?
  - id: createProject
    intent: Create a project
    question: How do I create a new test project?
  - id: searchProjects
    intent: Search projects by UUID
    question: Can I find a project by its UUID?
  - id: getProject
    intent: Get a project
    question: How can I look up one project's details?
  - id: updateProject
    intent: Update a project
    question: Can I rename a project or change its dates?
  - id: getCurrentProfile
    intent: Get my permissions in a project
    question: What am I allowed to do in this project?
  - id: getUsers
    intent: List users in a project
    question: Who are the members of a project?
  - id: getProjects
    intent: List qTest Pulse projects
    question: What projects exist in qTest Pulse?
  phrasing_ops: 9
  slug: tricentis-project-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The projects API from Tricentis — 3 operation(s) for projects.
  name: Tricentis Projects API
  phrasing_intents:
  - id: getProjects
    intent: List projects in the analytics feed
    question: Which projects appear in the test analytics data?
  - id: getProjects({id})
    intent: Get an analytics project by key
    question: How do I read one project record from the analytics feed?
  - id: getV1Projects
    intent: List Jira projects
    question: Which Jira projects can I manage tests in?
  phrasing_ops: 3
  slug: tricentis-projects-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Release API
  name: Tricentis Release API
  phrasing_intents:
  - id: getAllReleases
    intent: List releases in a project
    question: What releases are set up in my qTest project?
  - id: createRelease
    intent: Create a release
    question: How do I create a new release to plan testing against?
  - id: getReleaseById
    intent: Get a release
    question: How do I look up one release?
  - id: updateReleaseById
    intent: Update a release
    question: How do I change a release's dates or description?
  - id: deleteReleaseById
    intent: Delete a release
    question: How do I delete a release?
  phrasing_ops: 5
  slug: tricentis-release-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The releases API from Tricentis — 2 operation(s) for releases.
  name: Tricentis Releases API
  phrasing_intents:
  - id: getReleases
    intent: List releases
    question: Which releases are recorded in the test analytics data?
  - id: getReleases({id})
    intent: Get a release by key
    question: How do I read one release record by its key?
  phrasing_ops: 2
  slug: tricentis-releases-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Requirement API
  name: Tricentis Requirement API
  phrasing_intents:
  - id: getRequirements
    intent: List requirements in a project or module
    question: What requirements are in my qTest project?
  - id: createRequirement
    intent: Create a requirement
    question: How do I add a new requirement to a project?
  - id: getPublicTraceabilityMatrixReport
    intent: Get the requirement traceability matrix
    question: Which test cases cover each of my requirements?
  - id: getAllRequirementComments
    intent: List comments on a requirement
    question: What comments have been left on this requirement?
  - id: addRequirementComment
    intent: Comment on a requirement
    question: How do I add a comment to a requirement?
  - id: getRequirementCommentById
    intent: Get one comment on a requirement
    question: How do I fetch a single requirement comment?
  - id: updateRequirementCommentById
    intent: Edit a comment on a requirement
    question: Can I edit a comment I left on a requirement?
  - id: deleteRequirementCommentById
    intent: Delete a comment from a requirement
    question: How do I remove a comment from a requirement?
  phrasing_ops: 13
  slug: tricentis-requirement-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The requirementreleases API from Tricentis — 2 operation(s) for requirementreleases.
  name: Tricentis Requirementreleases API
  phrasing_intents:
  - id: getRequirementreleases
    intent: List requirement release links
    question: Which requirements are planned for which releases?
  - id: getRequirementreleases({projectid})
    intent: Get a project's requirement releases
    question: How do I see requirement release links for one project?
  phrasing_ops: 2
  slug: tricentis-requirementreleases-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The requirements API from Tricentis — 5 operation(s) for requirements.
  name: Tricentis Requirements API
  phrasing_intents:
  - id: getRequirements
    intent: List requirements in the analytics feed
    question: Which requirements are in the test analytics data?
  - id: getRequirements({id})
    intent: Get an analytics requirement by key
    question: Is there a way to read one requirement record from the analytics feed?
  - id: postV1ProjectsByProjectKeyTestCasesRequirements
    intent: Create Jira requirements
    question: How do I create requirement issues in a Jira project?
  - id: postV1ProjectsByProjectKeyTestCasesByKeyRequirements
    intent: Create requirements for a test case
    question: Can I create a new requirement and link it to a test case in one step?
  - id: postV1ProjectsByProjectKeyTestCasesByKeyRequirementLink
    intent: Link existing requirements to a test case
    question: Can I link a requirement issue that already exists to a test case?
  phrasing_ops: 5
  slug: tricentis-requirements-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The requirementsets API from Tricentis — 2 operation(s) for requirementsets.
  name: Tricentis Requirementsets API
  phrasing_intents:
  - id: getRequirementsets
    intent: List requirement sets
    question: Which requirement sets exist in the analytics data?
  - id: getRequirementsets({id})
    intent: Get a requirement set by key
    question: How do I read one requirement set by its key?
  phrasing_ops: 2
  slug: tricentis-requirementsets-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The requirementtestcases API from Tricentis — 2 operation(s) for requirementtestcases.
  name: Tricentis Requirementtestcases API
  phrasing_intents:
  - id: getRequirementtestcases
    intent: List requirement to test case links
    question: Which test cases cover which requirements?
  - id: getRequirementtestcases('{id}')
    intent: Get a requirement test case link by key
    question: How do I read one requirement to test case link by its key?
  phrasing_ops: 2
  slug: tricentis-requirementtestcases-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Resources|Reservations API from Tricentis — 2 operation(s) for resources|reservations.
  name: Tricentis Resources|Reservations API
  phrasing_intents:
  - id: GetReservations
    intent: List resource reservations
    question: What reservations are booked in a given time window?
  - id: GetReservationsMode
    intent: Check whether reservation mode is on
    question: Is reservation mode currently switched on for the account?
  - id: switchReservationMode
    intent: Turn reservation mode on or off
    question: Can I switch reservation mode off for the account?
  phrasing_ops: 3
  slug: tricentis-resources-reservations-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Resources|Zones API from Tricentis — 1 operation(s) for resources|zones.
  name: Tricentis Resources|Zones API
  phrasing_intents:
  - id: GetZones
    intent: List load generation zones
    question: What zones are available to run my controllers and load generators?
  phrasing_ops: 1
  slug: tricentis-resources-zones-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Results API from Tricentis — 5 operation(s) for results.
  name: Tricentis Results API
  phrasing_intents:
  - id: GetTestResultList
    intent: List test results in a workspace
    question: What load test results do I have in my NeoLoad Web workspace?
  - id: GetTestResult
    intent: Get a test result summary
    question: How do I see the name, dates and owner of a test result?
  - id: DeleteTestResult
    intent: Delete a test result
    question: How do I delete a test result and its statistics?
  - id: UpdateTestResult
    intent: Update a test result
    question: Can I rename a test result or change its description?
  - id: GetTestResultLogs
    intent: Get logs of a test result
    question: Where can I see the logs from a load test run?
  - id: GetTestResultStatistics
    intent: Get main statistics of a test result
    question: What were the headline statistics of my load test?
  - id: GetTestRawResult
    intent: Download all raw data of a test result
    question: Can I export all the raw data of a test result as JSON or CSV?
  phrasing_ops: 7
  slug: tricentis-results-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Results|Elements API from Tricentis — 8 operation(s) for results|elements.
  name: Tricentis Results|Elements API
  phrasing_intents:
  - id: GetTestResultElements
    intent: List elements of a test result by category
    question: Which transactions or requests were measured in a load test result?
  - id: GetTestResultAllElementsValues
    intent: Get values for every element of a test result
    question: Can I get aggregated values for all elements of a test result in one call?
  - id: GetTestResultElementDefinition
    intent: Get one test result element definition
    question: How do I see the definition of a single element in a test result?
  - id: GetTestResultElementsValues
    intent: Get values of one test result element
    question: What were the aggregated values for one transaction in a test result?
  - id: GetTestResultElementsPoints
    intent: Get time-series points for a result element
    question: How do I chart a transaction's response time over the duration of a test?
  - id: GetTestResultElementsPercentiles
    intent: Get response-time percentiles for a transaction
    question: What was the 95th percentile response time for a transaction?
  - id: GetTestRawResultElement
    intent: Download raw data for one transaction
    question: Can I export the raw samples for a single transaction as CSV?
  - id: GetTestResultElementsSla
    intent: Get SLA status of one result element
    question: Did a specific transaction meet its SLA during the test?
  phrasing_ops: 8
  slug: tricentis-results-elements-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Results|Events API from Tricentis — 2 operation(s) for results|events.
  name: Tricentis Results|Events API
  phrasing_intents:
  - id: GetTestResultEvents
    intent: List events of a test result
    question: What errors and events happened during a load test?
  - id: PostTestResultCustomEvent
    intent: Add a custom event to a test result
    question: Can I mark something that happened outside NeoLoad, like a deployment, on a test result?
  - id: PatchTestResultCustomEvent
    intent: Edit a custom event on a test result
    question: Can I change the end time of a custom event I already added?
  phrasing_ops: 3
  slug: tricentis-results-events-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Results|Monitors API from Tricentis — 4 operation(s) for results|monitors.
  name: Tricentis Results|Monitors API
  phrasing_intents:
  - id: GetTestResultMonitors
    intent: List monitor counters of a test result
    question: Which monitors and counters were collected for a test result?
  - id: PostTestResultMonitors
    intent: Push custom monitor data to a running test
    question: Can I send my own external metrics into a test while it is running?
  - id: GetTestResultMonitorDefinition
    intent: Get a monitor counter definition
    question: What does a specific monitor counter measure and in what unit?
  - id: GetTestResultMonitorsValues
    intent: Get summary values of a monitor counter
    question: What were the values of a given monitor counter during a test?
  - id: GetTestResultMonitorsPoints
    intent: Get time-series points of a monitor counter
    question: Can I get the time series of a counter averaged over intervals?
  phrasing_ops: 5
  slug: tricentis-results-monitors-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Results|Reporting API from Tricentis — 3 operation(s) for results|reporting.
  name: Tricentis Results|Reporting API
  phrasing_intents:
  - id: GetTestResultGraph
    intent: Render a graph for one test result
    question: Can I get a chart image of response times and monitors for a test result?
  - id: GetTestReportResult
    intent: Get a PDF report of a test result
    question: Can I download a PDF report of a test result?
  - id: GetTestResultMultiGraph
    intent: Render a graph comparing test results
    question: How can I compare several test results on one chart?
  phrasing_ops: 3
  slug: tricentis-results-reporting-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Results|SLAs API from Tricentis — 3 operation(s) for results|slas.
  name: Tricentis Results|SL As API
  phrasing_intents:
  - id: GetTestResultSLAGlobalIndicators
    intent: Get overall SLA indicators of a test result
    question: Did my load test pass its global SLAs?
  - id: GetTestResultSLAPerTest
    intent: Get per-test SLA results
    question: Which elements failed their per-test SLAs across the whole run?
  - id: GetTestResultSLAPerInterval
    intent: Get per-interval SLA results
    question: When during the test did SLAs start failing?
  phrasing_ops: 3
  slug: tricentis-results-slas-api
- baseURL: https://pulse-us-east-1.qtestnet.com/api
  baseurl_source: declared
  description: Rule API
  name: Tricentis Rule API
  phrasing_intents:
  - id: getRules
    intent: List a project's Pulse rules
    question: Which automation rules are set up in my Pulse project?
  - id: postRules
    intent: Create a Pulse rule
    question: How do I create a rule that runs actions when a trigger fires?
  - id: getRulesById
    intent: Get a Pulse rule
    question: Which trigger and actions does a given rule use?
  - id: putRulesById
    intent: Replace a Pulse rule
    question: Can I fully replace a rule's trigger and actions with PUT?
  - id: patchRulesById
    intent: Patch a Pulse rule
    question: Can I just switch a rule off with PATCH?
  - id: deleteRulesById
    intent: Delete a Pulse rule
    question: How do I remove an automation rule from Pulse?
  phrasing_ops: 6
  slug: tricentis-rule-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Search API
  name: Tricentis Search API
  phrasing_intents:
  - id: searchCommentWithQuery
    intent: Search comments in a project
    question: Can I find comments left by a particular author on test cases?
  - id: queryHistories
    intent: Query change history of objects
    question: Who changed this requirement and what did they change?
  - id: searchArtifact
    intent: Query requirements, test cases, runs or defects
    question: Can I run the same data query I use in the web app through the API?
  phrasing_ops: 3
  slug: tricentis-search-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Site Templates API
  name: Tricentis Site Templates API
  phrasing_intents:
  - id: getAllSiteTemplates
    intent: List site templates
    question: What site templates are available on our qTest site?
  - id: addProjects
    intent: Apply a site template to existing projects
    question: How do I apply a site template to projects that already exist?
  - id: removeProjectTemplates
    intent: Remove projects from a site template
    question: How do I detach projects from a site template?
  phrasing_ops: 3
  slug: tricentis-site-templates-api
- baseURL: https://api.ttm4j.tricentis.com
  baseurl_source: declared
  description: The Status API from Tricentis — 1 operation(s) for status.
  name: Tricentis Status API
  phrasing_intents:
  - id: headV1ApiKeyIsAlive
    intent: Check whether my API key is valid
    question: Is my test management API key still valid?
  phrasing_ops: 1
  slug: tricentis-status-api
- baseURL: https://parameter-1.qtestnet.com
  baseurl_source: declared
  description: Tasks public APIs
  name: Tricentis Tasks API
  phrasing_intents:
  - id: getApiV1TasksById
    intent: Check an import or export task
    question: How do I check the progress of an import or export task?
  - id: getApiV1TasksByIdResult
    intent: Get a finished task's result
    question: Where do I read the outcome of a completed import task?
  phrasing_ops: 2
  slug: tricentis-tasks-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Test Case API
  name: Tricentis Test Case API
  phrasing_intents:
  - id: getTestCases
    intent: List test cases in a project or module
    question: What test cases are in my qTest project?
  - id: createTestCase
    intent: Create a test case
    question: How do I add a new test case to a qTest project?
  - id: updateMultipleTestCases
    intent: Bulk update several test cases at once
    question: Can I update many test cases in one request instead of one at a time?
  - id: getTestCaseComments
    intent: List comments on a test case
    question: What comments have people left on this test case?
  - id: addTestCaseComment
    intent: Comment on a test case
    question: How do I leave a comment on a test case?
  - id: getTestCaseCommentById
    intent: Get one comment on a test case
    question: How do I read a single comment on a test case by its ID?
  - id: updateTestCaseComment
    intent: Edit a comment on a test case
    question: Can I edit a comment I already left on a test case?
  - id: deleteTestCaseComment
    intent: Delete a comment from a test case
    question: How do I remove a comment from a test case?
  phrasing_ops: 23
  slug: tricentis-test-case-api
- baseURL: https://api.ttm4j.tricentis.com
  baseurl_source: declared
  description: The Test Cases API from Tricentis — 7 operation(s) for test cases.
  name: Tricentis Test Cases API
  phrasing_intents:
  - id: getV1ProjectsByProjectKeyTestCases
    intent: Read test cases (deprecated paging)
    question: Is there an older offset-paged way to read a project's test cases?
  - id: postV1ProjectsByProjectKeyTestCases
    intent: Create test cases
    question: How do I create new test cases in a Jira project?
  - id: getV1ProjectsByProjectKeyTestCasesBulk
    intent: Read test cases in bulk
    question: Which test cases are in a particular folder of my project?
  - id: postV1TestCasesSearch
    intent: Search test cases with JQL (deprecated)
    question: Is there a legacy offset-paged JQL search for test cases?
  - id: postV1TestCasesSearchJql
    intent: Search test cases with JQL
    question: How do I find test cases with a JQL query?
  - id: getV1ProjectsByProjectKeyJobsByJobId
    intent: Check a test case import job
    question: Has my asynchronous test case import finished?
  - id: putV1ProjectsByProjectKeyTestCasesByKey
    intent: Update a test case
    question: How do I change a test case's summary or fields?
  - id: deleteV1ProjectsByProjectKeyTestCasesByKey
    intent: Delete a test case
    question: How do I delete a test case?
  phrasing_ops: 11
  slug: tricentis-test-cases-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Test Cycle API
  name: Tricentis Test Cycle API
  phrasing_intents:
  - id: getTestCycles
    intent: List test cycles
    question: What test cycles are in my project?
  - id: createCycle
    intent: Create a test cycle
    question: How do I create a test cycle?
  - id: getTestCycle
    intent: Get a test cycle
    question: How do I fetch one test cycle?
  - id: updateCycle
    intent: Update or move a test cycle
    question: How do I rename a test cycle?
  - id: deleteCycle
    intent: Delete a test cycle
    question: How do I delete a test cycle?
  phrasing_ops: 5
  slug: tricentis-test-cycle-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Test Log API
  name: Tricentis Test Log API
  phrasing_intents:
  - id: submitAutomationTestLogs
    intent: Submit automation results for many test runs
    question: How can I push a batch of automated test results to qTest in one call?
  - id: track
    intent: Check a batch test log submission job
    question: Did my batch upload of automation results finish processing?
  - id: submitAutomationTestLogsWithTreeStructure
    intent: Submit automation results and build the test tree
    question: Can I upload automation results and have qTest create the modules, cycles and suites for them?
  - id: submitAutomationLog
    intent: Submit one automation test log
    question: How do I record the result of a single automated test run?
  - id: modifyAutomationLog
    intent: Modify an automation test log
    question: Can I correct an automation result that was already submitted?
  - id: getTestLogsList
    intent: List all test logs of a test run
    question: Where can I see the full execution history of a test run?
  - id: submitTestLog
    intent: Submit a manual test log
    question: How do I record a manual tester's pass or fail result?
  - id: getLastRunLog
    intent: Get the latest result of a test run
    question: What was the most recent result of this test run?
  phrasing_ops: 10
  slug: tricentis-test-log-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Test Run API
  name: Tricentis Test Run API
  phrasing_intents:
  - id: getOf
    intent: List test runs in a project or container
    question: What test runs are in my project?
  - id: createTestRun
    intent: Create a test run for a test case
    question: How do I schedule a single test case for execution as a test run?
  - id: addTestRunWithParametersDataset
    intent: Create test runs from a parameter dataset
    question: Can I generate test runs from rows in a parameter dataset?
  - id: addTestRunWithParameters
    intent: Create test runs with hand-picked parameter values
    question: How do I create several test runs where I choose each run's parameter values myself?
  - id: addTestRunWithParametersRandomize
    intent: Create test runs with random parameter combinations
    question: Can qTest randomly combine parameter values into multiple test runs?
  - id: getStatusValuable
    intent: List test run execution statuses
    question: What execution statuses can a test run have in my project?
  - id: getSubhierachy
    intent: Get the test execution tree under a container
    question: How do I see the full tree of cycles and suites under a release?
  - id: getTestRunComments
    intent: List comments on a test run
    question: What comments are on this test run?
  phrasing_ops: 15
  slug: tricentis-test-run-api
- baseURL: https://api.ttm4j.tricentis.com
  baseurl_source: declared
  description: The Test Runs API from Tricentis — 4 operation(s) for test runs.
  name: Tricentis Test Runs API
  phrasing_intents:
  - id: postV1ProjectsByProjectKeyImportExecutionJunit
    intent: Import test results from JUnit XML
    question: How do I import JUnit results as test runs?
  - id: postV1ProjectsByProjectKeyTestRunsSearch
    intent: Search test runs
    question: Which test runs belong to a given cycle or version?
  - id: postV1ProjectsByProjectKeyTestRuns
    intent: Create test runs
    question: How do I record new test runs for a release version?
  - id: putV1ProjectsByProjectKeyTestRunsByTestRunKey
    intent: Update a test run
    question: How do I set a test run's status to failed?
  - id: deleteV1ProjectsByProjectKeyTestRunsByTestRunKey
    intent: Delete a test run
    question: What removes a test run entirely?
  - id: getTestruns
    intent: List test runs in the analytics feed
    question: Which test runs are in the test analytics data?
  - id: getTestruns({id})
    intent: Get an analytics test run by key
    question: Where do I read one test run record from the analytics feed?
  phrasing_ops: 7
  slug: tricentis-test-runs-api
- baseURL: https://api.ttm4j.tricentis.com
  baseurl_source: declared
  description: The Test Runs Fields API from Tricentis — 2 operation(s) for test runs fields.
  name: Tricentis Test Runs Fields API
  phrasing_intents:
  - id: postV1TestRunsSchemeBySchemeNameAllowedValues
    intent: Add an allowed environment or build value
    question: How do I add a new environment option for test runs?
  - id: deleteV1TestRunsSchemeBySchemeNameAllowedValuesByAllowedValueName
    intent: Remove an allowed environment or build value
    question: Can I remove an environment that is no longer used from test runs?
  phrasing_ops: 2
  slug: tricentis-test-runs-fields-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Test Suite API
  name: Tricentis Test Suite API
  phrasing_intents:
  - id: getListTestSuite
    intent: List test suites under a container
    question: Which test suites sit under a given test cycle or release?
  - id: createTestSuite
    intent: Create a test suite
    question: How do I create a test suite inside a test cycle?
  - id: getTestSuite
    intent: Get a test suite
    question: How can I look up one test suite's details?
  - id: updateTestSuite
    intent: Update or move a test suite
    question: Can I move a test suite to another test cycle?
  - id: deleteTestSuiteById
    intent: Delete a test suite
    question: Can I delete a test suite I no longer need?
  phrasing_ops: 5
  slug: tricentis-test-suite-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The testrunlogs API from Tricentis — 2 operation(s) for testrunlogs.
  name: Tricentis Testrunlogs API
  phrasing_intents:
  - id: getTestrunlogs
    intent: List test run logs
    question: What run logs exist for my test runs?
  - id: getTestrunlogs({id})
    intent: Get a test run log by key
    question: How do I read one test run log by its key?
  phrasing_ops: 2
  slug: tricentis-testrunlogs-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Tests API from Tricentis — 2 operation(s) for tests.
  name: Tricentis Tests API
  phrasing_intents:
  - id: GetTestList
    intent: List tests in a workspace
    question: What load tests are defined in my workspace?
  - id: PostCreateTest
    intent: Create a load test
    question: How do I create a new NeoLoad test?
  - id: GetTest
    intent: Get a load test
    question: How do I see the settings of one test?
  - id: PatchTest
    intent: Partially update a test
    question: Can I change just the scenario of a test without touching other settings?
  - id: PutTest
    intent: Replace all settings of a test
    question: Can I overwrite every field of a test in one go?
  - id: DeleteTest
    intent: Delete a load test
    question: How do I delete a test?
  phrasing_ops: 6
  slug: tricentis-tests-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Tests|Projects API from Tricentis — 1 operation(s) for tests|projects.
  name: Tricentis Tests|Projects API
  phrasing_intents:
  - id: PostUploadProject
    intent: Upload a project to a test
    question: How do I upload a NeoLoad project zip to a test?
  - id: ReadProjectMetadata
    intent: Get the project metadata of a test
    question: Which NeoLoad project is attached to this test?
  phrasing_ops: 2
  slug: tricentis-tests-projects-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Tests|Runtime API from Tricentis — 2 operation(s) for tests|runtime.
  name: Tricentis Tests|Runtime API
  phrasing_intents:
  - id: GetTestsRun
    intent: Start a test
    question: How do I launch a test from the API?
  - id: StopTestResult
    intent: Stop a running test
    question: Can I stop a test that is still running?
  phrasing_ops: 2
  slug: tricentis-tests-runtime-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Tests|Test Analysis API from Tricentis — 1 operation(s) for tests|test analysis.
  name: Tricentis Tests|Test Analysis API
  phrasing_intents:
  - id: get_1
    intent: Get a test analysis configuration
    question: How is test analysis configured for my test?
  - id: put_1
    intent: Update a test analysis configuration
    question: Can I make a test fail when it misses its analysis objective?
  phrasing_ops: 2
  slug: tricentis-tests-test-analysis-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Tosca Integration API
  name: Tricentis Tosca API
  phrasing_intents:
  - id: notifyTestEventImport
    intent: Import Tosca TestEvents into a project
    question: Can I bring Tosca TestEvent objects into qTest?
  phrasing_ops: 1
  slug: tricentis-tosca-api
- baseURL: https://pulse-us-east-1.qtestnet.com/api
  baseurl_source: declared
  description: Trigger API
  name: Tricentis Trigger API
  phrasing_intents:
  - id: getTriggers
    intent: List a project's Pulse triggers
    question: Which triggers are defined in my Pulse project?
  - id: postTriggers
    intent: Create a Pulse trigger
    question: How do I create a trigger that Pulse rules can fire on?
  - id: getTriggersById
    intent: Get a Pulse trigger
    question: Can I look up one Pulse trigger by id?
  - id: putTriggersById
    intent: Replace a Pulse trigger
    question: Can I fully replace a trigger's name and project with PUT?
  - id: patchTriggersById
    intent: Patch a Pulse trigger
    question: Can I rename a trigger with a PATCH request?
  - id: deleteTriggersById
    intent: Delete a Pulse trigger
    question: How do I remove a trigger from Pulse?
  phrasing_ops: 6
  slug: tricentis-trigger-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: User API
  name: Tricentis User API
  phrasing_intents:
  - id: reevaluateToken
    intent: Get my own user information
    question: Who am I logged in as in qTest?
  - id: findUsersByProjectsName
    intent: Find users by project name
    question: Which users are assigned to a project with a given name?
  - id: createUser
    intent: Invite a new user
    question: How can I invite someone new to our test management instance?
  - id: assignUsersToProject
    intent: Assign several users to a project
    question: How do I add a list of users to a project at once?
  - id: removeAssociationUsersAndProjects
    intent: Remove users from projects
    question: Can I take several users off a project in one request?
  - id: findByUserNameOrEmail
    intent: Search users by username
    question: Is there a user with this username already?
  - id: getUserById
    intent: Get a user by ID
    question: How can I retrieve one user's details by ID?
  - id: updateUser
    intent: Update a user's information
    question: Can I change a user's recovery email or reset their password?
  phrasing_ops: 13
  slug: tricentis-user-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: User Profile API
  name: Tricentis User Profile API
  phrasing_intents:
  - id: getCurrent
    intent: Get my admin profile
    question: What admin permissions do I have in qTest?
  - id: getUserProfiles
    intent: List available user and admin profiles
    question: Which permission profiles exist on our qTest instance?
  - id: batchAssignUserProfileInClient
    intent: Assign users to a profile site-wide
    question: How do I give a group of users the same site-level profile?
  - id: getProfilesOfCurrentUser
    intent: List my profiles across projects
    question: What role do I have in each project?
  - id: batchAssignUserProfileInProject
    intent: Assign users to a profile in one project
    question: How do I change the profile of several users inside a single project?
  phrasing_ops: 5
  slug: tricentis-user-profile-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The users API from Tricentis — 2 operation(s) for users.
  name: Tricentis Users API
  phrasing_intents:
  - id: getUsers
    intent: List users in the analytics feed
    question: Which users appear in the test analytics data?
  - id: getUsers({id})
    intent: Get an analytics user by key
    question: How do I read one user record from the analytics feed?
  phrasing_ops: 2
  slug: tricentis-users-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Application Information V2 APIs
  name: Tricentis V2 Application Information API
  phrasing_intents:
  - id: getSessionsBySessionIdAppInfos
    intent: List a session's application info
    question: Which applications were captured during an exploratory session?
  - id: postSessionsBySessionIdAppInfos
    intent: Add application info to a session
    question: How do I record a new application against an exploratory session?
  - id: putSessionsBySessionIdAppInfos
    intent: Replace a session's application info list
    question: Can I update the whole list of applications on a session at once?
  - id: deleteSessionsBySessionIdAppInfosByAppInfoId
    intent: Delete an application info entry
    question: How do I remove an application captured by mistake from a session?
  - id: getSessionsBySessionIdAppInfosByAppInfoId
    intent: Get one application info entry
    question: Can I read a single application entry captured in a session?
  - id: putSessionsBySessionIdAppInfosByAppInfoId
    intent: Update one application info entry
    question: Can I correct the name or version of one captured application?
  phrasing_ops: 6
  slug: tricentis-v2-application-information-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Coverage V2 APIs
  name: Tricentis V2 Coverage API
  phrasing_intents:
  - id: getSessionsBySessionIdCoverages
    intent: List a session's coverages
    question: Which requirements or test objects does an exploratory session cover?
  - id: putSessionsBySessionIdCoverages
    intent: Replace all coverages of a session
    question: Can I reset the full coverage list of a session in one call?
  - id: postSessionsBySessionIdCoverages
    intent: Add a coverage to a session
    question: How do I link a session to a requirement it covers?
  - id: getSessionsBySessionIdCoveragesByCoverageId
    intent: Get one session coverage
    question: Can I read a single coverage link of a session?
  - id: putSessionsBySessionIdCoveragesByCoverageId
    intent: Update one session coverage
    question: Can I change the title or order of one coverage on a session?
  - id: deleteSessionsBySessionIdCoveragesByCoverageId
    intent: Remove a coverage from a session
    question: How do I unlink a requirement a session no longer covers?
  phrasing_ops: 6
  slug: tricentis-v2-coverage-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Project V2 APIs
  name: Tricentis V2 Project API
  phrasing_intents:
  - id: getPermissions
    intent: Get my permissions across projects
    question: What am I allowed to do in each of these projects?
  - id: getProjectsByProjectIdReset
    intent: Reset sample project data
    question: How do I restore the sample project to its original data?
  phrasing_ops: 2
  slug: tricentis-v2-project-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Project settings V2 APIs
  name: Tricentis V2 Project Settings API
  phrasing_intents:
  - id: getProjectSettingsByProjectId
    intent: Get a project's session settings
    question: What note types and time types does a project use for sessions?
  - id: putProjectSettingsByProjectId
    intent: Update a project's session settings
    question: How do I change the note types available in a project?
  - id: getProjectSettings
    intent: Get settings for several projects
    question: Can I fetch session settings for multiple projects in one call?
  phrasing_ops: 3
  slug: tricentis-v2-project-settings-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Resource V2 APIs
  name: Tricentis V2 Resource API
  phrasing_intents:
  - id: getSessionsBySessionIdResources
    intent: List a session's resources
    question: Which files are attached to an exploratory session?
  - id: getSessionsBySessionIdResourcesByResourceId
    intent: Get a session resource's details
    question: Can I read the metadata of one resource in a session?
  - id: deleteSessionsBySessionIdResourcesByResourceId
    intent: Delete a session resource
    question: How do I remove a file attached to a session?
  - id: getSessionsBySessionIdResourcesByResourceIdDownload
    intent: Download a session resource
    question: How do I download a file that was attached to a session?
  - id: postSessionsBySessionIdResourcesUpload
    intent: Upload a resource to a session
    question: How do I attach a file to an exploratory session?
  phrasing_ops: 5
  slug: tricentis-v2-resource-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Screen V2 APIs
  name: Tricentis V2 Screen API
  phrasing_intents:
  - id: getSessionsBySessionIdScreens
    intent: List a session's screens
    question: Which screens were captured during an exploratory session?
  - id: postSessionsBySessionIdScreens
    intent: Add a screen to a session
    question: How do I add a new captured screen to a session?
  - id: putSessionsBySessionIdScreens
    intent: Update several screens at once
    question: Can I update many captured screens of a session in one request?
  - id: getSessionsBySessionIdScreensByScreenId
    intent: Get a session screen
    question: Can I read the details of one captured screen?
  - id: putSessionsBySessionIdScreensByScreenId
    intent: Update a session screen
    question: How do I rename or annotate one captured screen?
  - id: deleteSessionsBySessionIdScreensByScreenId
    intent: Delete a session screen
    question: How do I remove a captured screen from a session?
  - id: getSessionsBySessionIdScreensByScreenIdImages
    intent: Get a screen's image
    question: Can I download the full-size image of a captured screen?
  - id: postSessionsBySessionIdScreensByScreenIdImages
    intent: Upload a screen's image
    question: How do I upload the screenshot for a captured screen?
  phrasing_ops: 11
  slug: tricentis-v2-screen-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Plugin V2 APIs
  name: Tricentis V2 Script Generator Plugin API
  phrasing_intents:
  - id: getPlugins
    intent: List script generator plugins
    question: Which script generator plugins are installed?
  - id: postPlugins
    intent: Add a script generator plugin
    question: How do I install a new script generator plugin?
  - id: deletePluginsByPluginid
    intent: Delete a script generator plugin
    question: How do I uninstall a script generator plugin?
  - id: getPluginsByPluginidFile
    intent: Download a script generator plugin
    question: Can I download the file of an installed plugin?
  phrasing_ops: 4
  slug: tricentis-v2-script-generator-plugin-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Session V2 APIs
  name: Tricentis V2 Session API
  phrasing_intents:
  - id: postSessions
    intent: Create an exploratory testing session
    question: How do I start a new exploratory testing session in a project?
  - id: getSessionsBySessionId
    intent: Get an exploratory session
    question: Can I read a session together with its timeline and app info?
  - id: putSessionsBySessionId
    intent: Update an exploratory session
    question: How do I change a session's title or summary?
  - id: deleteSessionsBySessionId
    intent: Delete an exploratory session
    question: How do I delete one exploratory session?
  - id: getSessionsBySessionIdStatus
    intent: Get an exploratory session's status
    question: What state is an exploratory session in right now?
  - id: putSessionsBySessionIdStatus
    intent: Change an exploratory session's status
    question: How do I mark an exploratory session as complete?
  - id: getCoveragesSessions
    intent: Find sessions linked to a qTest Manager object
    question: Which exploratory sessions cover a given requirement or test case?
  - id: getSessionsBySessionIdHistory
    intent: Get an exploratory session's history
    question: Who changed an exploratory session and when?
  phrasing_ops: 8
  slug: tricentis-v2-session-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: System Information V2 APIs
  name: Tricentis V2 System Information API
  phrasing_intents:
  - id: postSessionsBySessionIdSysInfos
    intent: Record system information for a session
    question: How do I record the OS and hardware a session ran on?
  - id: getSessionsBySessionIdSysInfosBySysInfoId
    intent: Get a session's system information
    question: What machine and OS was a session captured on?
  - id: putSessionsBySessionIdSysInfosBySysInfoId
    intent: Update a session's system information
    question: Can I correct the OS or computer name stored on a session?
  - id: deleteSessionsBySessionIdSysInfosBySysInfoId
    intent: Delete a session's system information
    question: Is it possible to remove the system details from a session?
  phrasing_ops: 4
  slug: tricentis-v2-system-information-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: view settings V2 APIs
  name: Tricentis V2 View Setting API
  phrasing_intents:
  - id: getViewSettings
    intent: Get the sessions list view settings
    question: Which columns are shown in the sessions list for a qTest Manager object?
  - id: putViewSettings
    intent: Update the sessions list view settings
    question: How do I change the columns of the sessions list?
  phrasing_ops: 2
  slug: tricentis-v2-view-setting-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Application Information V3 APIs
  name: Tricentis V3 Application Information API
  phrasing_intents:
  - id: getApiSessionsBySessionIdAppInfos
    intent: List a session's application info
    question: Which applications were captured during an exploratory session?
  - id: postApiSessionsBySessionIdAppInfos
    intent: Add application info to a session
    question: How do I record a new application against an exploratory session?
  - id: putApiSessionsBySessionIdAppInfos
    intent: Replace a session's application info list
    question: Can I update the whole list of applications on a session at once?
  - id: deleteApiSessionsBySessionIdAppInfosByAppInfoId
    intent: Delete an application info entry
    question: How do I remove an application captured by mistake from a session?
  - id: getApiSessionsBySessionIdAppInfosByAppInfoId
    intent: Get one application info entry
    question: Can I read a single application entry captured in a session?
  - id: putApiSessionsBySessionIdAppInfosByAppInfoId
    intent: Update one application info entry
    question: Can I correct the name or version of one captured application?
  phrasing_ops: 6
  slug: tricentis-v3-application-information-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Config V3 APIs
  name: Tricentis V3 Config API
  phrasing_intents:
  - id: getApiConfig
    intent: Get the current app configuration
    question: What configuration is the exploratory testing app running with?
  - id: getApiUserSettings
    intent: Get my user settings
    question: What are my personal session settings?
  - id: putApiUserSettings
    intent: Update my user settings
    question: How do I change my personal session preferences?
  phrasing_ops: 3
  slug: tricentis-v3-config-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Coverage V3 APIs
  name: Tricentis V3 Coverage API
  phrasing_intents:
  - id: getApiSessionsBySessionIdCoverages
    intent: List a session's coverages
    question: Which requirements or test objects does an exploratory session cover?
  - id: putApiSessionsBySessionIdCoverages
    intent: Replace all coverages of a session
    question: Can I reset the full coverage list of a session in one call?
  - id: postApiSessionsBySessionIdCoverages
    intent: Add a coverage to a session
    question: How do I link a session to a requirement it covers?
  - id: getApiSessionsBySessionIdCoveragesByCoverageId
    intent: Get one session coverage
    question: Can I read a single coverage link of a session?
  - id: putApiSessionsBySessionIdCoveragesByCoverageId
    intent: Update one session coverage
    question: Can I change the title or order of one coverage on a session?
  - id: deleteApiSessionsBySessionIdCoveragesByCoverageId
    intent: Remove a coverage from a session
    question: How do I unlink a requirement a session no longer covers?
  phrasing_ops: 6
  slug: tricentis-v3-coverage-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Export V3 APIs
  name: Tricentis V3 Export API
  phrasing_intents:
  - id: postApiExportImage
    intent: Export session screens as images
    question: Can I export the screens of a session as image files?
  - id: postApiExportDoc
    intent: Export session screens to Word
    question: Can I export a session's screens to a Word document?
  - id: postApiExportPdf
    intent: Export session screens to PDF
    question: Can I export a session's screens as a PDF?
  - id: postApiExportTestcase
    intent: Export a session as a test case
    question: Can I turn an exploratory session into a test case?
  - id: getSessionExportByExportId
    intent: Download an exported file
    question: Where do I download the result of a session export?
  phrasing_ops: 5
  slug: tricentis-v3-export-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Project settings V3 APIs
  name: Tricentis V3 Project Settings API
  phrasing_intents:
  - id: getApiProjectSettingsByProjectId
    intent: Get a project's session settings
    question: What note types and time types does a project use for sessions?
  - id: putApiProjectSettingsByProjectId
    intent: Update a project's session settings
    question: How do I change the note types available in a project?
  phrasing_ops: 2
  slug: tricentis-v3-project-settings-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Query V3 APIs
  name: Tricentis V3 Query API
  phrasing_intents:
  - id: getApiQuerySessionsTree
    intent: List saved session queries
    question: Which saved session queries exist in my project?
  - id: getApiQuerySessionsByQueryid
    intent: Run a saved session query
    question: How do I run a saved query to list matching sessions?
  - id: getApiQuerySessionsByQueryidStatistic
    intent: Get statistics for a session query
    question: How many sessions does a saved query match?
  phrasing_ops: 3
  slug: tricentis-v3-query-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Resource V3 APIs
  name: Tricentis V3 Resource API
  phrasing_intents:
  - id: getApiSessionsBySessionIdResources
    intent: List a session's resources
    question: Which files are attached to an exploratory session?
  - id: getApiSessionsBySessionIdResourcesByResourceId
    intent: Get a session resource's details
    question: Can I read the metadata of one resource in a session?
  - id: deleteApiSessionsBySessionIdResourcesByResourceId
    intent: Delete a session resource
    question: How do I remove a file attached to a session?
  - id: getApiSessionsBySessionIdResourcesByResourceIdDownload
    intent: Download a session resource
    question: How do I download a file that was attached to a session?
  - id: postApiSessionsBySessionIdResourcesUpload
    intent: Upload a resource to a session
    question: How do I attach a file to an exploratory session?
  phrasing_ops: 5
  slug: tricentis-v3-resource-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Screen V3 APIs
  name: Tricentis V3 Screen API
  phrasing_intents:
  - id: getApiSessionsBySessionIdScreens
    intent: List a session's screens
    question: Which screens were captured during an exploratory session?
  - id: postApiSessionsBySessionIdScreens
    intent: Add a screen to a session
    question: How do I add a new captured screen to a session?
  - id: putApiSessionsBySessionIdScreens
    intent: Update several screens at once
    question: Can I update many captured screens of a session in one request?
  - id: getApiSessionsBySessionIdScreensByScreenId
    intent: Get a session screen
    question: Can I read the details of one captured screen?
  - id: putApiSessionsBySessionIdScreensByScreenId
    intent: Update a session screen
    question: How do I rename or annotate one captured screen?
  - id: deleteApiSessionsBySessionIdScreensByScreenId
    intent: Delete a session screen
    question: How do I remove a captured screen from a session?
  - id: getApiSessionsBySessionIdScreensByScreenIdImages
    intent: Get a screen's image
    question: Can I download the full-size image of a captured screen?
  - id: postApiSessionsBySessionIdScreensByScreenIdImages
    intent: Upload a screen's image
    question: How do I upload the screenshot for a captured screen?
  phrasing_ops: 11
  slug: tricentis-v3-screen-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Search V3 APIs
  name: Tricentis V3 Search API
  phrasing_intents:
  - id: getApiField
    intent: Get a session field for search
    question: Which values can I search sessions by for a given field?
  - id: getApiSearchList
    intent: Search sessions by field
    question: How do I search sessions in a project by a field?
  phrasing_ops: 2
  slug: tricentis-v3-search-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Session V3 APIs
  name: Tricentis V3 Session API
  phrasing_intents:
  - id: postApiSessions
    intent: Create an exploratory testing session
    question: How do I start a new exploratory testing session in a project?
  - id: putApiSessionsBatch
    intent: Update several sessions at once
    question: Can I update many exploratory sessions in a single request?
  - id: deleteApiSessionsBatch
    intent: Delete several sessions at once
    question: Can I delete a batch of exploratory sessions together?
  - id: getApiSessionsBySessionId
    intent: Get an exploratory session
    question: Can I read a session together with its timeline and app info?
  - id: putApiSessionsBySessionId
    intent: Update an exploratory session
    question: How do I change a session's title or summary?
  - id: deleteApiSessionsBySessionId
    intent: Delete an exploratory session
    question: How do I delete one exploratory session?
  - id: getApiSessionsBySessionIdStatus
    intent: Get an exploratory session's status
    question: What state is an exploratory session in right now?
  - id: putApiSessionsBySessionIdStatus
    intent: Change an exploratory session's status
    question: How do I mark an exploratory session as complete?
  phrasing_ops: 8
  slug: tricentis-v3-session-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: System Information V3 APIs
  name: Tricentis V3 System Information API
  phrasing_intents:
  - id: postApiSessionsBySessionIdSysInfos
    intent: Record system information for a session
    question: How do I record the OS and hardware a session ran on?
  - id: getApiSessionsBySessionIdSysInfosBySysInfoId
    intent: Get a session's system information
    question: What machine and OS was a session captured on?
  - id: putApiSessionsBySessionIdSysInfosBySysInfoId
    intent: Update a session's system information
    question: Can I correct the OS or computer name stored on a session?
  - id: deleteApiSessionsBySessionIdSysInfosBySysInfoId
    intent: Delete a session's system information
    question: Is it possible to remove the system details from a session?
  phrasing_ops: 4
  slug: tricentis-v3-system-information-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Upload V3 APIs
  name: Tricentis V3 Upload API
  phrasing_intents:
  - id: getApiUpload
    intent: Get an uploaded resource by key
    question: Can I fetch an uploaded resource by its key?
  - id: deleteApiUpload
    intent: Delete an uploaded resource
    question: How do I delete a resource I uploaded?
  - id: postApiUpload
    intent: Upload a resource
    question: How do I upload a standalone resource file?
  - id: postUploadObjects
    intent: Upload a media file
    question: How do I upload a file as a media object?
  - id: getMedia
    intent: Get a media file by key
    question: Can I fetch an uploaded media object by key?
  - id: deleteMedia
    intent: Delete a media file
    question: How do I delete a media object?
  phrasing_ops: 6
  slug: tricentis-v3-upload-api
- baseURL: https://session-js.qtestnet.com
  baseurl_source: declared
  description: Query V4 APIs
  name: Tricentis V4 Query API
  phrasing_intents:
  - id: postApiV4Query
    intent: Create a saved session query
    question: How do I save a new query for finding sessions?
  - id: putApiV4QueryByQueryid
    intent: Update a saved session query
    question: Can I rename a saved query or change its clauses?
  - id: deleteApiV4QueryByQueryid
    intent: Delete a saved session query
    question: Is there a way to delete a saved query?
  - id: putApiV4QueryShare
    intent: Share saved queries
    question: How do I share my saved queries with others?
  phrasing_ops: 4
  slug: tricentis-v4-query-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: Webhook
  name: Tricentis Webhook API
  phrasing_intents:
  - id: getAllWebhooks
    intent: List registered webhooks
    question: Which webhooks are currently registered?
  - id: createWebhook
    intent: Register a webhook
    question: How do I get notified at my own URL when test events happen in qTest?
  - id: getAllEventNames
    intent: List webhook event names
    question: What events can a webhook subscribe to?
  - id: getWebhookById
    intent: Get a webhook
    question: How can I check the URL and events of one webhook?
  - id: updateWebhook
    intent: Update a webhook
    question: Can I change the target URL of an existing webhook?
  - id: deleteWebhookById
    intent: Delete a webhook
    question: Can I unregister a webhook so it stops sending events?
  phrasing_ops: 6
  slug: tricentis-webhook-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Workspaces API from Tricentis — 5 operation(s) for workspaces.
  name: Tricentis Workspaces API
  phrasing_intents:
  - id: GetWorkspaceList
    intent: List accessible workspaces
    question: Which workspaces can I access?
  - id: create_1
    intent: Create a workspace
    question: How do I set up a new workspace for a team?
  - id: find
    intent: Get a workspace
    question: How can I look up a single workspace's settings?
  - id: patch_1
    intent: Update a workspace
    question: Can I rename a workspace or change its description?
  - id: addMembersToWorkspace
    intent: Add members to a workspace
    question: How can I give more people access to a workspace?
  - id: removeMembersFromWorkspace
    intent: Remove members from a workspace
    question: How do I take someone out of a workspace?
  - id: delete_1
    intent: Delete a workspace
    question: What gets lost when I delete a workspace?
  phrasing_ops: 7
  slug: tricentis-workspaces-api
- baseURL: https://apitryout.qtestnet.com/
  baseurl_source: declared
  description: The Test Suites API from Tricentis — 2 operation(s) for test suites.
  name: Tricentis Test Suites API
  phrasing_intents:
  - id: getTestsuites
    intent: List test suites
    question: Which test suites are in the test analytics data?
  - id: getTestsuites({id})
    intent: Get a test suite by key
    question: How do I read one test suite by its key?
  phrasing_ops: 2
  slug: tricentis-test-suites-api
artifact_total: 237
asyncapis:
- description: ''
  name: Tricentis Qtest Webhooks
  slug: tricentis-qtest-webhooks
collections:
- collection_type: open
  name: qTest Data Export Access Files API
  slug: open-tricentis-accessfiles-api
- collection_type: open
  name: qTest Pulse Action API
  slug: open-tricentis-action-api
- collection_type: open
  name: NeoLoad Administration of users API
  slug: open-tricentis-administration-of-users-api
- collection_type: open
  name: qTest Manager API Version 3.0 Attachment API
  slug: open-tricentis-attachment-api
- collection_type: open
  name: TTM for Jira Attachments API
  slug: open-tricentis-attachments-api
- collection_type: open
  name: qTest Manager API Version 3.0 Auth Systems API
  slug: open-tricentis-auth-systems-api
- collection_type: open
  name: qTest Parameters Authentication API
  slug: open-tricentis-authentication-api
- collection_type: open
  name: qTest Manager API Version 3.0 Automation Job API
  slug: open-tricentis-automation-job-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Bridgerequirementsetlinks API
  slug: open-tricentis-bridgerequirementsetlinks-api
- collection_type: open
  name: qTest Manager API Version 3.0 Build API
  slug: open-tricentis-build-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Builds API
  slug: open-tricentis-builds-api
- collection_type: open
  name: qTest Manager API Version 3.0 Common API
  slug: open-tricentis-common-api
- collection_type: open
  name: qTest Pulse Constant API
  slug: open-tricentis-constant-api
- collection_type: open
  name: TTM for Jira Cycles API
  slug: open-tricentis-cycles-api
- collection_type: open
  name: qTest Parameters Datasets API
  slug: open-tricentis-datasets-api
- collection_type: open
  name: qTest Manager API Version 3.0 Defect API
  slug: open-tricentis-defect-api
- collection_type: open
  name: Tricentis Defects API
  slug: open-tricentis-defects-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Defecttestrunlogs API
  slug: open-tricentis-defecttestrunlogs-api
- collection_type: open
  name: NeoLoad Deletion Policies API
  slug: open-tricentis-deletion-policies-api
- collection_type: open
  name: qTest Pulse Execution API
  slug: open-tricentis-execution-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Executionsummaries API
  slug: open-tricentis-executionsummaries-api
- collection_type: open
  name: qTest Manager API Version 3.0 Field API
  slug: open-tricentis-field-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Folderhierarchies API
  slug: open-tricentis-folderhierarchies-api
- collection_type: open
  name: Tricentis Folders API
  slug: open-tricentis-folders-api
- collection_type: open
  name: qTest Manager API Version 3.0 Groups API
  slug: open-tricentis-groups-api
- collection_type: open
  name: NeoLoad Information API
  slug: open-tricentis-information-api
- collection_type: open
  name: NeoLoad Infrastructure Providers API
  slug: open-tricentis-infrastructure-providers-api
- collection_type: open
  name: qTest Manager API Version 3.0 Integration Settings API
  slug: open-tricentis-integration-settings-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Latestrunlogs API
  slug: open-tricentis-latestrunlogs-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Latesttestrunstatuses API
  slug: open-tricentis-latesttestrunstatuses-api
- collection_type: open
  name: qTest Manager API Version 3.0 Login API
  slug: open-tricentis-login-api
- collection_type: open
  name: qTest Manager API Version 3.0 Module API
  slug: open-tricentis-module-api
- collection_type: open
  name: qTest Manager API Version 3.0 Object Link API
  slug: open-tricentis-object-link-api
- collection_type: open
  name: qTest Parameters API
  slug: open-tricentis-parameters-api
- collection_type: open
  name: Tricentis Project API
  slug: open-tricentis-project-api
- collection_type: open
  name: Tricentis Projects API
  slug: open-tricentis-projects-api
- collection_type: open
  name: qTest Manager API Version 3.0 Release API
  slug: open-tricentis-release-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Releases API
  slug: open-tricentis-releases-api
- collection_type: open
  name: qTest Manager API Version 3.0 Requirement API
  slug: open-tricentis-requirement-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Requirementreleases API
  slug: open-tricentis-requirementreleases-api
- collection_type: open
  name: Tricentis Requirements API
  slug: open-tricentis-requirements-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Requirementsets API
  slug: open-tricentis-requirementsets-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Requirementtestcases API
  slug: open-tricentis-requirementtestcases-api
- collection_type: open
  name: NeoLoad Resources|Reservations API
  slug: open-tricentis-resources-reservations-api
- collection_type: open
  name: NeoLoad Resources|Zones API
  slug: open-tricentis-resources-zones-api
- collection_type: open
  name: NeoLoad Results API
  slug: open-tricentis-results-api
- collection_type: open
  name: NeoLoad Results|Elements API
  slug: open-tricentis-results-elements-api
- collection_type: open
  name: NeoLoad Results|Events API
  slug: open-tricentis-results-events-api
- collection_type: open
  name: NeoLoad Results|Monitors API
  slug: open-tricentis-results-monitors-api
- collection_type: open
  name: NeoLoad Results|Reporting API
  slug: open-tricentis-results-reporting-api
- collection_type: open
  name: NeoLoad Results|SL As API
  slug: open-tricentis-results-slas-api
- collection_type: open
  name: qTest Pulse Rule API
  slug: open-tricentis-rule-api
- collection_type: open
  name: qTest Manager API Version 3.0 Search API
  slug: open-tricentis-search-api
- collection_type: open
  name: qTest Manager API Version 3.0 Site Templates API
  slug: open-tricentis-site-templates-api
- collection_type: open
  name: TTM for Jira Status API
  slug: open-tricentis-status-api
- collection_type: open
  name: qTest Parameters Tasks API
  slug: open-tricentis-tasks-api
- collection_type: open
  name: qTest Manager API Version 3.0 Test Case API
  slug: open-tricentis-test-case-api
- collection_type: open
  name: TTM for Jira Test Cases API
  slug: open-tricentis-test-cases-api
- collection_type: open
  name: qTest Manager API Version 3.0 Test Cycle API
  slug: open-tricentis-test-cycle-api
- collection_type: open
  name: qTest Manager API Version 3.0 Test Log API
  slug: open-tricentis-test-log-api
- collection_type: open
  name: qTest Manager API Version 3.0 Test Run API
  slug: open-tricentis-test-run-api
- collection_type: open
  name: TTM for Jira Test Runs API
  slug: open-tricentis-test-runs-api
- collection_type: open
  name: TTM for Jira Test Runs Fields API
  slug: open-tricentis-test-runs-fields-api
- collection_type: open
  name: qTest Manager API Version 3.0 Test Suite API
  slug: open-tricentis-test-suite-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Testcases API
  slug: open-tricentis-testcases-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Testrunlogs API
  slug: open-tricentis-testrunlogs-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Testruns API
  slug: open-tricentis-testruns-api
- collection_type: open
  name: NeoLoad Tests API
  slug: open-tricentis-tests-api
- collection_type: open
  name: NeoLoad Tests|Projects API
  slug: open-tricentis-tests-projects-api
- collection_type: open
  name: NeoLoad Tests|Runtime API
  slug: open-tricentis-tests-runtime-api
- collection_type: open
  name: NeoLoad Tests|Test Analysis API
  slug: open-tricentis-tests-test-analysis-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Testsuites API
  slug: open-tricentis-testsuites-api
- collection_type: open
  name: qTest Manager API Version 3.0 Tosca API
  slug: open-tricentis-tosca-api
- collection_type: open
  name: qTest Pulse Trigger API
  slug: open-tricentis-trigger-api
- collection_type: open
  name: Tricentis User API
  slug: open-tricentis-user-api
- collection_type: open
  name: qTest Manager API Version 3.0 User Profile API
  slug: open-tricentis-user-profile-api
- collection_type: open
  name: Tricentis Analytics (Tech Review) Users API
  slug: open-tricentis-users-api
- collection_type: open
  name: qTest Explorer | Sessions V2 Application Information API
  slug: open-tricentis-v2-application-information-api
- collection_type: open
  name: qTest Explorer | Sessions V2 Coverage API
  slug: open-tricentis-v2-coverage-api
- collection_type: open
  name: qTest Explorer | Sessions V2 Project API
  slug: open-tricentis-v2-project-api
- collection_type: open
  name: qTest Explorer | Sessions V2 Project Settings API
  slug: open-tricentis-v2-project-settings-api
- collection_type: open
  name: qTest Explorer | Sessions V2 Resource API
  slug: open-tricentis-v2-resource-api
- collection_type: open
  name: qTest Explorer | Sessions V2 Screen API
  slug: open-tricentis-v2-screen-api
- collection_type: open
  name: qTest Explorer | Sessions V2 Script Generator Plugin API
  slug: open-tricentis-v2-script-generator-plugin-api
- collection_type: open
  name: qTest Explorer | Sessions V2 Session API
  slug: open-tricentis-v2-session-api
- collection_type: open
  name: qTest Explorer | Sessions V2 System Information API
  slug: open-tricentis-v2-system-information-api
- collection_type: open
  name: qTest Explorer | Sessions V2 View Setting API
  slug: open-tricentis-v2-view-setting-api
- collection_type: open
  name: qTest Explorer | Sessions V3 Application Information API
  slug: open-tricentis-v3-application-information-api
- collection_type: open
  name: qTest Explorer | Sessions V3 Config API
  slug: open-tricentis-v3-config-api
- collection_type: open
  name: qTest Explorer | Sessions V3 Coverage API
  slug: open-tricentis-v3-coverage-api
- collection_type: open
  name: qTest Explorer | Sessions V3 Export API
  slug: open-tricentis-v3-export-api
- collection_type: open
  name: qTest Explorer | Sessions V3 Project Settings API
  slug: open-tricentis-v3-project-settings-api
- collection_type: open
  name: qTest Explorer | Sessions V3 Query API
  slug: open-tricentis-v3-query-api
- collection_type: open
  name: qTest Explorer | Sessions V3 Resource API
  slug: open-tricentis-v3-resource-api
- collection_type: open
  name: qTest Explorer | Sessions V3 Screen API
  slug: open-tricentis-v3-screen-api
- collection_type: open
  name: qTest Explorer | Sessions V3 Search API
  slug: open-tricentis-v3-search-api
- collection_type: open
  name: qTest Explorer | Sessions V3 Session API
  slug: open-tricentis-v3-session-api
- collection_type: open
  name: qTest Explorer | Sessions V3 System Information API
  slug: open-tricentis-v3-system-information-api
- collection_type: open
  name: qTest Explorer | Sessions V3 Upload API
  slug: open-tricentis-v3-upload-api
- collection_type: open
  name: qTest Explorer | Sessions V4 Query API
  slug: open-tricentis-v4-query-api
- collection_type: open
  name: qTest Manager API Version 3.0 Webhook API
  slug: open-tricentis-webhook-api
- collection_type: open
  name: NeoLoad Workspaces API
  slug: open-tricentis-workspaces-api
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.tricentis.com/feed.xml
- group: commercial
  href: https://artifacts.apis.io/tricentis/plans/tricentis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tricentis-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/tricentis/capabilities/tricentis-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tricentis-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/tricentis/agentic-access/tricentis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tricentis-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/tricentis/security/tricentis-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tricentis-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/tricentis/security/tricentis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tricentis-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tricentis/security/tricentis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tricentis-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/tricentis/authentication/tricentis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tricentis-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.tricentis.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tricentis.com/all/home.htm
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.tricentis.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.qasymphony.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tricentis.com/qtest-saas/content/apis/overview/how_to_use_interactive_api_documentation.htm
- group: company
  title: ''
  type: Blog
  url: https://www.tricentis.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.tricentis.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://shiftsync.tricentis.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Tricentis
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tricentis.com/products/unified-test-management-qtest/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.tricentis.com/software-testing-tool-trial-demo/qtest-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tricentis.com/legal-information/general-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tricentis.com/legal-information/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tricentis.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.tricentis.com/trust/security
- group: auth
  title: ''
  type: Security
  url: https://www.tricentis.com/trust/vulnerability-disclosure-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.tricentis.com/qtest-saas/content/release_notes_and_announcements/release_notes_landing_page.htm
- group: agent
  href: https://artifacts.apis.io/tricentis/llms/tricentis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tricentis-llms.txt
- group: build
  href: https://artifacts.apis.io/tricentis/packages/tricentis-packages.yml
  title: ''
  type: Packages
  url: packages/tricentis-packages.yml
- group: build
  href: https://artifacts.apis.io/tricentis/packages/tricentis-packages.yml
  title: ''
  type: SDKs
  url: packages/tricentis-packages.yml
- group: agent
  href: https://artifacts.apis.io/tricentis/well-known/tricentis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tricentis-well-known.yml
- group: agent
  href: https://artifacts.apis.io/tricentis/mcp/tricentis-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tricentis-mcp.yml
- group: build
  href: https://artifacts.apis.io/tricentis/mcp/tricentis-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tricentis-tool-crosswalk.yml
- group: design
  href: https://artifacts.apis.io/tricentis/conformance/tricentis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tricentis-conformance.yml
- group: design
  href: https://artifacts.apis.io/tricentis/errors/tricentis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tricentis-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tricentis/lifecycle/tricentis-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tricentis-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.tricentis.com/qtest-saas/content/release_notes_and_announcements/end_of_support_announcements.htm
- group: auth
  href: https://artifacts.apis.io/tricentis/scopes/tricentis-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tricentis-scopes.yml
- group: design
  href: https://artifacts.apis.io/tricentis/conventions/tricentis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tricentis-conventions.yml
- group: operate
  href: https://artifacts.apis.io/tricentis/conventions/tricentis-conventions.yml
  title: ''
  type: RateLimits
  url: conventions/tricentis-conventions.yml
- group: operate
  href: https://artifacts.apis.io/tricentis/changelog/tricentis-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tricentis-changelog.yml
- group: build
  href: https://artifacts.apis.io/tricentis/cli/tricentis-cli.yml
  title: ''
  type: CLI
  url: cli/tricentis-cli.yml
- group: start
  href: https://artifacts.apis.io/tricentis/sandbox/tricentis-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tricentis-sandbox.yml
- group: design
  href: https://artifacts.apis.io/tricentis/data-model/tricentis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tricentis-data-model.yml
- group: design
  href: https://artifacts.apis.io/tricentis/asyncapi/tricentis-qtest-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tricentis-qtest-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/tricentis/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/tricentis/overlays/tricentis-qtest-manager-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tricentis-qtest-manager-overlay.yaml
created: '2026-08-02'
description: Tricentis is an enterprise continuous testing and quality engineering company, founded in Austria in 2007 and headquartered in Vienna with US operations in Austin, Texas. Its platform spans model-based UI and API test automation (Tosca, Tosca Cloud), AI-driven test management (qTest), performance testing (NeoLoad), Jira-native test management (Tricentis Test Management for Jira), SAP change impact analysis (LiveCompare), data and ETL validation (Data Integrity), regulated-industry validation (Vera), and quality analytics. Tricentis exposes machine-readable REST contracts for qTest Manager, Parameters, Pulse, Scenario, Sessions, Data Export and Analytics, for NeoLoad Web, and for Tricentis Test Management for Jira, and it was among the first enterprise quality-engineering vendors to ship remote Model Context Protocol (MCP) servers plus an open-source, Apache-2.0 catalog of agent skills for driving Tosca and qTest from AI coding assistants.
finops:
- has_sources: true
  method: derived
  name: Tricentis Finops
  primary_unit: ''
  service_category: ''
  slug: tricentis-finops
  template: true
image: https://be.tricentis.com/media-assets/2022/08/Tricentis-Logo-1-1120x446-1.png
layout: provider
mcp_servers:
- description: 'Tricentis ships remote, product-scoped MCP servers across its quality-engineering platform — Tosca Cloud, Tosca Commander (in-process), qTest and Tricentis Test Management for Jira. Every endpoint is '
  name: Tricentis MCP Server
  slug: tricentis-mcp-yml
modified: '2026-10-06'
name: Tricentis
nav: Providers
network: true
overview: 'Tricentis publishes 100 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Files API, Action API, Administration of users API, and 97 more. Tagged areas include Company, Testing, Test Automation, Quality Engineering, and Test Management.


  The Tricentis catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Tricentis'' developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, support, pricing, and 38 more developer resources.'
plans:
- name: Tricentis Plans Pricing
  plan_count: 0
  slug: tricentis-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Tricentis API Rules
  rule_count: 56
  severity_counts:
    error: 28
    hint: 0
    info: 12
    warn: 16
  slug: tricentis-rules
scopes:
- name: Tricentis Scopes
  scope_count: 1
  slug: tricentis-scopes
  summary_line: 1 scope
score:
  band: exemplar
  composite: 70.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 57.7
    developer_ergonomics: 85.7
    discoverability: 80.0
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - austria
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - dach
    - europe
  previous_composite: 70.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 68.3
      derived: 0
      marker_coverage: 23.8
      total: 101
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/tricentis/tricentis-2026-08-17T082438.png
security:
- kind: authentication
  name: Tricentis Authentication
  slug: tricentis-authentication
  summary_line: apiKey/http · 6 schemes
- kind: domain-security
  name: Tricentis Domain Security
  slug: tricentis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tricentis Vulnerability Disclosure
  slug: tricentis-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Tricentis Trust Center
  slug: tricentis-trust-center
  summary_line: SOC 2 Type 2, ISO/IEC 27001:2022, ISO/IEC 27701:2019, ISO 9001, GDPR
skill_count: 30
skills:
- name: cli-api-commander
  slug: tricentis-cli-api-commander
- name: commander-mcp
  slug: tricentis-commander-mcp
- name: qtest-register-webhook
  slug: tricentis-qtest-register-webhook
- name: qtest-submit-automation-results
  slug: tricentis-qtest-submit-automation-results
- name: tosca-agents
  slug: tricentis-tosca-agents
- name: tosca-analyzing-execution-history
  slug: tricentis-tosca-analyzing-execution-history
- name: tosca-analyzing-execution-results
  slug: tricentis-tosca-analyzing-execution-results
- name: tosca-authoring-automated-testcase
  slug: tricentis-tosca-authoring-automated-testcase
- name: tosca-authoring-manual-testcase
  slug: tricentis-tosca-authoring-manual-testcase
- name: tosca-cloud-basics
  slug: tricentis-tosca-cloud-basics
- name: tosca-cloud-connect
  slug: tricentis-tosca-cloud-connect
- name: tosca-cloud-mcp
  slug: tricentis-tosca-cloud-mcp
- name: tosca-cloud
  slug: tricentis-tosca-cloud
- name: tosca-create-playlist
  slug: tricentis-tosca-create-playlist
- name: tosca-create-workspace
  slug: tricentis-tosca-create-workspace
- name: tosca-datasets
  slug: tricentis-tosca-datasets
- name: tosca-delete-playlist
  slug: tricentis-tosca-delete-playlist
- name: tosca-delete-workspace
  slug: tricentis-tosca-delete-workspace
- name: tosca-execution
  slug: tricentis-tosca-execution
- name: tosca-explaining-testcase
  slug: tricentis-tosca-explaining-testcase
- name: tosca-export-dataset
  slug: tricentis-tosca-export-dataset
- name: tosca-find
  slug: tricentis-tosca-find
- name: tosca-import-dataset
  slug: tricentis-tosca-import-dataset
- name: tosca-login
  slug: tricentis-tosca-login
slug: tricentis
tags:
- Company
- Testing
- Test Automation
- Quality Engineering
- Test Management
- Performance Testing
- Continuous Testing
- DevOps
- SAP
- Data Integrity
- Agentic Testing
website: https://www.tricentis.com/
---
