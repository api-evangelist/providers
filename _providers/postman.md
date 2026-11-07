---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 55.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 155
  human_in_the_loop: 1
  name: Postman Agentic Access
  operation_count: 286
  slug: postman-agentic-access
  summary_line: 286 operations · 155 acting · 1 human-in-the-loop
api_count: 21
apis:
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: Postman is the single platform for collaborative API development used by 35+ million developers. It covers the entire API lifecycle - design, build, test, document, mock, monitor, and govern - and now
  name: Postman
  slug: postman
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Collections API lets you programmatically create, read, update, and delete Postman Collections including requests, folders, scripts, and environments. Powers CI/CD integration, sync, and collectio
  name: Postman Collections API
  phrasing_intents:
  - id: asyncMergePullCollectionFork
    intent: Merge or pull fork changes asynchronously
    question: How do I merge a forked Postman collection into its parent in the background and track it as a task?
  - id: asyncMergePullCollectionTaskStatus
    intent: Check a collection merge or pull task
    question: Did my async collection merge or pull task finish, or is it still running?
  - id: getCollections
    intent: List my collections
    question: What collections do I have access to, including ones I'm subscribed to?
  - id: createCollection
    intent: Create a collection
    question: How do I create a new collection in a specific workspace through the API?
  - id: getCollectionsForkedByUser
    intent: List the collections I have forked
    question: Which collections have I forked?
  - id: createCollectionFork
    intent: Fork a collection into a workspace
    question: How do I fork an existing collection into another workspace?
  - id: mergeCollectionFork
    intent: Merge a fork using the deprecated endpoint
    question: Is there an older synchronous endpoint for merging a forked collection back into its parent?
  - id: getCollection
    intent: Get a collection
    question: How do I fetch the full contents of one collection by its ID?
  phrasing_ops: 34
  slug: collections-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: Manage personal, team, partner, public, and private workspaces. Control visibility, membership, roles, and the elements (collections, environments, mocks, monitors, APIs) attached to each workspace.
  name: Postman Workspaces API
  phrasing_intents:
  - id: managePartnerWorkspaceInvites
    intent: Invite or remove Partner Workspace partners
    question: How do I invite external partners by email to a Partner Workspace?
  - id: getWorkspaces
    intent: List workspaces
    question: Which workspaces do I have access to?
  - id: createWorkspace
    intent: Create a workspace
    question: How do I create a new team workspace?
  - id: getAllWorkspaceRoles
    intent: List the available workspace roles
    question: What roles can be assigned in a workspace on my plan?
  - id: getWorkspace
    intent: Get a workspace
    question: How do I look up one workspace's details and visibility?
  - id: updateWorkspace
    intent: Rename a workspace or change its visibility
    question: Can I rename a workspace or make it public?
  - id: deleteWorkspace
    intent: Delete a workspace
    question: How do I delete a workspace I no longer use?
  - id: getWorkspaceActivityFeed
    intent: View a workspace's activity feed
    question: What has changed recently in this workspace and who did it?
  phrasing_ops: 19
  slug: workspaces-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Environments API enables programmatic management of Postman environments and global variables, including secret variables stored in the Postman Vault, so you can scope work to dev/staging/prod env
  name: Postman Environments API
  phrasing_intents:
  - id: getEnvironments
    intent: List environments
    question: Which environments do I have?
  - id: createEnvironment
    intent: Create an environment
    question: How do I create a new environment with variables in a workspace?
  - id: getEnvironment
    intent: Get an environment
    question: How do I see the variables stored in one environment?
  - id: putEnvironment
    intent: Replace all of an environment's data
    question: Can I overwrite an environment completely with new variables?
  - id: deleteEnvironment
    intent: Delete an environment
    question: How do I delete an environment?
  - id: patchEnvironment
    intent: Update specific environment variables
    question: Can I add or change just one variable in an environment without replacing it?
  - id: getEnvironmentForks
    intent: List an environment's forks
    question: Who has forked this environment?
  - id: forkEnvironment
    intent: Fork an environment
    question: How do I fork an environment into a workspace?
  phrasing_ops: 10
  slug: environments-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: 'The Monitors API runs Postman Collections on a recurring schedule to validate API health, performance, and contract conformance. Surfaces metrics, test results, and notification webhooks for incident '
  name: Postman Monitors API
  phrasing_intents:
  - id: getMonitors
    intent: List monitors
    question: Which scheduled monitors are set up in my workspace?
  - id: createMonitor
    intent: Create a monitor for a collection
    question: How do I schedule a collection to run on a recurring monitor?
  - id: getMonitor
    intent: Get a monitor
    question: What schedule and last run result does one of my monitors have?
  - id: updateMonitor
    intent: Change a monitor's configuration
    question: How do I change how often a monitor runs?
  - id: deleteMonitor
    intent: Delete a monitor
    question: How do I stop and remove a monitor I no longer need?
  - id: runMonitor
    intent: Run a monitor now
    question: Can I trigger a monitor run on demand instead of waiting for its schedule?
  - id: getRunnerInstances
    intent: List instances of a private monitor runner
    question: Which instances of my self-hosted runner are polling for monitor runs?
  - id: getRunnerMetrics
    intent: Get a runner's queue and polling metrics
    question: When did my monitor runner last poll, and how deep is its run queue?
  phrasing_ops: 8
  slug: monitors-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Webhooks API creates webhooks that trigger collection runs with custom payloads, integrating Postman with external systems (GitHub, Slack, custom triggers) for event-driven automation.
  name: Postman Webhooks API
  phrasing_intents:
  - id: createWebhook
    intent: Create a webhook that triggers a collection
    question: Can I run a collection whenever an external system calls a URL?
  phrasing_ops: 1
  slug: webhooks-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Tags API manages tags applied to APIs, collections, and workspaces for organization, governance reporting, and discoverability across the Private and Public API Networks.
  name: Postman Tags API
  phrasing_intents:
  - id: getApiTags
    intent: Get an API's tags
    question: What tags are on this API?
  - id: updateApiTags
    intent: Replace an API's tags
    question: Does updating an API's tags replace the existing ones?
  - id: getCollectionTags
    intent: Get a collection's tags
    question: Which tags are on this collection?
  - id: updateCollectionTags
    intent: Replace a collection's tags
    question: How do I tag a collection?
  - id: getTaggedEntities
    intent: Find elements carrying a tag
    question: Which workspaces, APIs and collections share a given tag?
  - id: getWorkspaceTags
    intent: Get a workspace's tags
    question: What tags are applied to this workspace?
  - id: updateWorkspaceTags
    intent: Replace a workspace's tags
    question: How do I tag a workspace?
  - id: getEntityTags
    intent: Get tags for any entity by type
    question: Is there one generic endpoint to read tags for an API, collection or workspace by type?
  phrasing_ops: 9
  slug: tags-api
- description: The Postman MCP Server exposes Postman Collections, environments, and workspaces over Anthropic's Model Context Protocol so AI agents (Claude, Cursor, custom LLM clients) can reason over and execute A
  name: Postman MCP Server
  slug: mcp-server
- description: Postman Flows is a visual workflow builder that chains API calls, transformations, and conditional logic. Flows are executable, debuggable, and cloneable documentation that powers AI agent orchestrati
  name: Postman Flows
  slug: flows-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: Operations for creating and managing mock servers.
  name: Postman Mocks API
  slug: postman-mocks-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The analytics API from Postman — 2 operation(s) for analytics.
  name: Postman Analytics API
  phrasing_intents:
  - id: getAnalyticsData
    intent: Get workspace and API usage analytics
    question: How much traffic and success are my public and partner workspaces getting?
  - id: getAnalyticsMetadata
    intent: List available analytics resources and metrics
    question: What analytics resources and metrics can I query?
  phrasing_ops: 2
  slug: postman-analytics-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The apiCatalog API from Postman — 11 operation(s) for apicatalog.
  name: Postman API Catalog API
  phrasing_intents:
  - id: getApiCatalogDiscoveryServices
    intent: List discovered services
    question: Which services has API Catalog discovered in my infrastructure that aren't catalogued yet?
  - id: postApiCatalogDiscoveryServices
    intent: Add discovered services to API Catalog
    question: How do I promote discovered services into the API Catalog?
  - id: getApiCatalogDiscoveryService
    intent: Get a discovered service's details
    question: What endpoints and OpenAPI spec were detected for a discovered service?
  - id: getApiCatalogServices
    intent: List catalogued services in an environment
    question: Which services are catalogued in my production system environment?
  - id: getApiCatalogService
    intent: Get a catalogued service's health and ownership
    question: What is the health, traffic and compliance status of one service in the catalog?
  - id: getApiCatalogServiceEndpoints
    intent: List a service's observed endpoints and metrics
    question: Which endpoints of a service are actually receiving traffic, and how are they performing?
  - id: getApiCatalogServiceMonitorRuns
    intent: List a service's scheduled monitor runs
    question: How have the scheduled monitors for a catalogued service been doing lately?
  - id: getApiCatalogServiceSpecificationLints
    intent: List a service's spec lint results
    question: How many governance issues did the latest spec lint find on a service?
  phrasing_ops: 16
  slug: postman-apicatalog-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The billing API from Postman — 2 operation(s) for billing.
  name: Postman Billing API
  phrasing_intents:
  - id: getAccounts
    intent: Get my team's billing account
    question: What billing account details does my team have?
  - id: getAccountInvoices
    intent: List a billing account's invoices
    question: Which invoices are on my billing account?
  phrasing_ops: 2
  slug: postman-billing-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The comments API from Postman — 1 operation(s) for comments.
  name: Postman Comments API
  phrasing_intents:
  - id: resolveCommentThread
    intent: Resolve a comment thread
    question: Can I mark a comment thread and its replies as resolved?
  phrasing_ops: 1
  slug: postman-comments-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The components API from Postman — 5 operation(s) for components.
  name: Postman Components API
  phrasing_intents:
  - id: getAllComponents
    intent: List components in the team library
    question: What reusable components are in my team's component library?
  - id: createComponent
    intent: Create a reusable component
    question: How do I add a reusable schema component to the team library?
  - id: getComponent
    intent: Get a component
    question: What is the status and latest published version of a component?
  - id: updateComponent
    intent: Rename, archive or reactivate a component
    question: How do I archive a component that is no longer used?
  - id: getComponentDraft
    intent: Get a component's unpublished draft
    question: What unpublished edits are sitting in a component's working draft?
  - id: updateComponentDraft
    intent: Edit a component's draft
    question: How do I change a component's content before publishing a new version?
  - id: getComponentVersions
    intent: List a component's published versions
    question: Which versions of a component have been published?
  - id: createComponentVersion
    intent: Publish a component version from its draft
    question: How do I publish the current draft of a component as a new version?
  phrasing_ops: 9
  slug: postman-components-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The groups API from Postman — 2 operation(s) for groups.
  name: Postman Groups API
  phrasing_intents:
  - id: getGroups
    intent: List the team's user groups
    question: What user groups exist on my Postman team?
  - id: getGroup
    intent: Get a user group
    question: Who belongs to a particular user group?
  phrasing_ops: 2
  slug: postman-groups-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The import API from Postman — 1 operation(s) for import.
  name: Postman Import API
  phrasing_intents:
  - id: openApiDefinition
    intent: Import an OpenAPI definition as a collection
    question: Can I turn an OpenAPI file into a Postman Collection through the API?
  phrasing_ops: 1
  slug: postman-import-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The postbot API from Postman — 1 operation(s) for postbot.
  name: Postman Postbot API
  phrasing_intents:
  - id: generateTool
    intent: Generate agent tool code from a public request
    question: Can I generate AI agent tool code from a public collection request?
  phrasing_ops: 1
  slug: postman-postbot-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The scim API from Postman — 6 operation(s) for scim.
  name: Postman SCIM API
  phrasing_intents:
  - id: getScimGroupResources
    intent: List SCIM groups
    question: Which user groups has my identity provider provisioned in Postman over SCIM?
  - id: createScimGroup
    intent: Provision a group via SCIM
    question: How do I provision a new user group and its members through SCIM?
  - id: getScimGroupResource
    intent: Get a SCIM group
    question: Who is in a particular SCIM-provisioned group?
  - id: deleteScimGroup
    intent: Delete a SCIM group
    question: What happens to member accounts when I delete a SCIM group?
  - id: updateGroup
    intent: Rename a SCIM group or change its members
    question: How do I add or remove members from a SCIM group?
  - id: getScimResourceTypes
    intent: List supported SCIM resource types
    question: Which SCIM resource types does Postman support?
  - id: getScimServiceProviderConfig
    intent: Get the SCIM service provider config
    question: Which SCIM operations like PATCH, filtering or bulk are supported?
  - id: getScimUserResources
    intent: List SCIM users
    question: Which team members are provisioned through SCIM?
  phrasing_ops: 12
  slug: postman-scim-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The search API from Postman — 1 operation(s) for search.
  name: Postman Search API
  phrasing_intents:
  - id: postmanResources
    intent: Search workspaces, collections and requests
    question: Where can I find a collection or request across all of Postman by keyword?
  phrasing_ops: 1
  slug: postman-search-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The specs API from Postman — 14 operation(s) for specs.
  name: Postman Specs API
  phrasing_intents:
  - id: getMigrationStatus
    intent: Check an API Builder to Spec Hub migration
    question: Has my API Builder definition finished migrating to Spec Hub?
  - id: migrateApiToSpecHub
    intent: Migrate an API Builder API to Spec Hub
    question: How do I move a legacy API Builder definition over to Spec Hub?
  - id: getGeneratedCollectionSpecs
    intent: Get the spec generated from a collection
    question: Where do I find the OpenAPI spec that was generated from my collection?
  - id: generateSpecFromCollection
    intent: Generate an OpenAPI spec from a collection
    question: How do I turn an existing Postman collection into an OpenAPI 3.1 specification?
  - id: syncCollectionWithSpec
    intent: Update a generated collection from its spec
    question: How do I push spec changes into the collection that was generated from it?
  - id: getAsyncSpecTaskStatus
    intent: Check a spec or collection generation task
    question: Is the spec generation or sync task I kicked off still running?
  - id: getAllSpecs
    intent: List the specs in a workspace
    question: Which API specifications live in my workspace's Spec Hub?
  - id: createSpec
    intent: Create a spec in Spec Hub
    question: How do I create a new OpenAPI or AsyncAPI specification in Spec Hub?
  phrasing_ops: 24
  slug: postman-specs-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The teams API from Postman — 6 operation(s) for teams.
  name: Postman Teams API
  phrasing_intents:
  - id: getTeams
    intent: List teams in my organization
    question: What teams exist in my Postman organization?
  - id: createTeam
    intent: Create a team
    question: How do I create a new team in my organization?
  - id: getTeam
    intent: Get a team
    question: How do I look up details about one team?
  - id: getTeamAccessRequests
    intent: List a team's pending access requests
    question: Who is waiting for access to my team?
  - id: createAccessRequest
    intent: Request access to a team
    question: How do I request to join a team or get a higher role?
  - id: approveDenyAccessRequest
    intent: Approve or deny a team access request
    question: How do I approve someone's request to join my team?
  - id: manageTeamMemberRoles
    intent: Add or remove member roles in bulk
    question: Can I add and remove roles for many team members in one call?
  - id: removeTeamMembers
    intent: Remove members from a team
    question: How do I remove users from my team?
  phrasing_ops: 10
  slug: postman-teams-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The users API from Postman — 3 operation(s) for users.
  name: Postman Users API
  phrasing_intents:
  - id: getAuthenticatedUser
    intent: Get the user behind my API key
    question: Which Postman user and team does my API key belong to?
  - id: getTeamUsers
    intent: List users on my team
    question: Who is on my team?
  - id: getTeamUser
    intent: Get a team user
    question: How do I look up one teammate's details?
  phrasing_ops: 3
  slug: postman-users-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: Operations for managing API schemas and specifications.
  name: Postman API Schemas API
  phrasing_intents:
  - id: getApiSchemas
    intent: List an API's schemas
    question: Which schemas are defined for one of my APIs?
  - id: createApiSchema
    intent: Create a schema for an API
    question: How do I add a GraphQL or OpenAPI schema to an API?
  - id: getApiSchema
    intent: Get an API schema with its content
    question: How do I read the content of one schema on an API?
  - id: getApiSchemaFiles
    intent: List files in a multi-file API schema
    question: What files make up a multi-file API schema?
  phrasing_ops: 4
  slug: postman-api-schemas-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: Operations for running collections and retrieving results.
  name: Postman Collection Runs API
  phrasing_intents:
  - id: getCollectionRuns
    intent: List a collection's run history
    question: How have past runs of my collection gone?
  - id: getCollectionRun
    intent: Get results of one collection run
    question: Which requests and test assertions failed in a particular collection run?
  phrasing_ops: 2
  slug: postman-collection-runs-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: Operations for managing elements (APIs, collections, workspaces) in the network.
  name: Postman Network Elements API
  phrasing_intents:
  - id: addNetworkElement
    intent: Publish an element to the private API network
    question: How do I publish an API or collection to our private API network?
  - id: updateNetworkElement
    intent: Update an element's private network listing
    question: Can I change the summary of an element listed in the private network?
  - id: removeNetworkElement
    intent: Remove an element from the private API network
    question: Does removing an element from the private network delete the underlying collection or API?
  phrasing_ops: 3
  slug: postman-network-elements-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: Operations for managing folders in the private API network.
  name: Postman Network Folders API
  phrasing_intents:
  - id: getNetworkFolders
    intent: List folders in the private API network
    question: How is our private API network organized into folders?
  - id: createNetworkFolder
    intent: Create a private network folder
    question: How do I add a folder to organize APIs in our private API network?
  - id: updateNetworkFolder
    intent: Rename or move a private network folder
    question: How do I rename a folder in the private API network?
  - id: deleteNetworkFolder
    intent: Delete a private network folder
    question: Is there a way to remove an empty folder from our private API network?
  phrasing_ops: 4
  slug: postman-network-folders-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: Operations for managing requests to add elements to the network.
  name: Postman Network Requests API
  phrasing_intents:
  - id: getNetworkRequests
    intent: List requests to add elements to the network
    question: Which requests to publish elements to our private network are waiting?
  - id: approveNetworkRequest
    intent: Approve a private network request
    question: How do I approve a request to add something to our private network?
  - id: denyNetworkRequest
    intent: Deny a private network request
    question: How do I reject a request to publish an element to the private network?
  phrasing_ops: 3
  slug: postman-network-requests-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: Operations for managing detected secrets and leaked credentials.
  name: Postman Secret Scanner API
  phrasing_intents:
  - id: getDetectedSecrets
    intent: List secrets detected in team resources
    question: Have any API keys or tokens leaked into our collections or environments?
  - id: getDetectedSecret
    intent: Get a detected secret's details
    question: What type of secret was found and what is its resolution history?
  - id: resolveDetectedSecret
    intent: Resolve a detected secret
    question: How do I mark a leaked key as revoked after I've rotated it?
  - id: getSecretLocations
    intent: List where a detected secret appears
    question: In which collections and environments does a leaked secret appear?
  - id: getSecretTypes
    intent: List secret types the scanner detects
    question: What kinds of credentials can the secret scanner detect?
  - id: detectedSecretsQueries
    intent: Search secrets found by the Secret Scanner
    question: Which leaked secrets has the Secret Scanner found across our workspaces?
  - id: updateDetectedSecretResolutions
    intent: Mark a detected secret as resolved
    question: How do I mark a detected secret as revoked or a false positive?
  - id: getDetectedSecretsLocations
    intent: Find where a detected secret appears
    question: Where exactly was this secret found in the workspace?
  phrasing_ops: 9
  slug: postman-secret-scanner-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: Operations for managing mock server responses and examples.
  name: Postman Server Responses API
  phrasing_intents:
  - id: getMockServerResponses
    intent: List a mock server's custom responses
    question: Which custom server responses override the defaults on my mock server?
  - id: createServerResponse
    intent: Add a custom response to a mock server
    question: How do I make my mock server return a 500 error to test failure handling?
  - id: updateServerResponse
    intent: Change a mock server's custom response
    question: How do I change the status code of an existing mock server response?
  - id: deleteServerResponse
    intent: Remove a custom response from a mock server
    question: Can I delete a custom server response so the mock falls back to collection examples?
  phrasing_ops: 4
  slug: postman-server-responses-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The sdKs API from Postman — 6 operation(s) for sdks.
  name: Postman SDKs API
  phrasing_intents:
  - id: getSdks
    intent: List SDKs in a workspace
    question: Which SDKs have been generated in my workspace?
  - id: createSdk
    intent: Generate an SDK from a collection or spec
    question: How do I generate a TypeScript client library from my collection?
  - id: getSdk
    intent: Get an SDK and its build status
    question: Has my SDK generation job finished building?
  - id: deleteSdk
    intent: Delete an SDK and its archive
    question: How do I delete a generated SDK and its stored zip?
  - id: getSdkDownloadUrl
    intent: Get a download link for a generated SDK
    question: Where can I download the zip of my generated SDK?
  - id: getSdkGitConnections
    intent: List SDK Git repository connections
    question: Which Git repositories are my SDKs publishing into?
  - id: createSdkGitConnection
    intent: Connect an SDK to a Git repository
    question: How do I have SDK updates pushed to my own Git repository automatically?
  - id: getSdkGitConnection
    intent: Get an SDK Git connection
    question: Which SDK version is currently on the target branch of a Git connection?
  phrasing_ops: 10
  slug: postman-sdks-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Apis API from Postman — 16 operation(s) for apis.
  name: Postman APIs API
  phrasing_intents:
  - id: getApis
    intent: List the APIs in a workspace
    question: Which APIs exist in my Postman workspace?
  - id: createApi
    intent: Create a new API in a workspace
    question: How do I create a new API in the API Builder programmatically?
  - id: getApi
    intent: Get details of one API
    question: What versions, schemas and collections does one of my API Builder APIs have?
  - id: updateApi
    intent: Rename or redescribe an API
    question: How can I rename an existing API in the API Builder?
  - id: deleteApi
    intent: Delete an API
    question: What's the way to permanently remove an API from the API Builder?
  - id: addApiCollection
    intent: Attach a collection to an API
    question: How do I attach a collection to one of my API Builder APIs?
  - id: getApiCollection
    intent: Get a collection attached to an API
    question: How do I read a collection that is attached to an API?
  - id: getApiCollectionComments
    intent: List comments on an API's collection
    question: What have reviewers commented on the collection attached to my API?
  phrasing_ops: 28
  slug: postman-apis-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The API Security API from Postman — 1 operation(s) for api security.
  name: Postman API Security API
  phrasing_intents:
  - id: schemaSecurityValidation
    intent: Check an API definition against security rules
    question: Does my OpenAPI definition violate any of our configured security and governance rules?
  phrasing_ops: 1
  slug: postman-api-security-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Audit Logs API from Postman — 2 operation(s) for audit logs.
  name: Postman Audit Logs API
  phrasing_intents:
  - id: getAuditLogs
    intent: List team audit events
    question: Who changed team settings or removed a user recently?
  - id: getAuditLogEventActions
    intent: List audit log event action types
    question: What kinds of actions are recorded in audit logs?
  phrasing_ops: 2
  slug: postman-audit-logs-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Collection Access Keys API from Postman — 2 operation(s) for collection access keys.
  name: Postman Collection Access Keys API
  phrasing_intents:
  - id: getCollectionAccessKeys
    intent: List my collection access keys
    question: Which collection access keys have I created?
  - id: deleteCollectionAccessKey
    intent: Revoke a collection access key
    question: How do I revoke a collection access key I shared?
  phrasing_ops: 2
  slug: postman-collection-access-keys-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Collection Folders API from Postman — 2 operation(s) for collection folders.
  name: Postman Collection Folders API
  phrasing_intents:
  - id: getFolderComments
    intent: List comments on a folder
    question: What comments have been left on this folder?
  - id: createFolderComment
    intent: Comment on a folder
    question: How do I comment on a folder in a collection?
  - id: updateFolderComment
    intent: Edit a comment on a folder
    question: Can I edit a comment I left on a folder?
  - id: deleteFolderComment
    intent: Delete a comment on a folder
    question: How do I delete a comment from a folder?
  phrasing_ops: 4
  slug: postman-collection-folders-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Collection Items API from Postman — 6 operation(s) for collection items.
  name: Postman Collection Items API
  phrasing_intents:
  - id: createCollectionFolder
    intent: Create a folder in a collection
    question: What's the way to add a new folder to a collection?
  - id: createCollectionRequest
    intent: Add a request to a collection
    question: How do I add a new request to a collection or one of its folders?
  - id: createCollectionResponse
    intent: Save an example response on a request
    question: Can I save an example response for a request in a collection?
  - id: getCollectionFolder
    intent: Get a folder in a collection
    question: Is there a way to look up one folder inside a collection by ID?
  - id: updateCollectionFolder
    intent: Rename or redescribe a folder
    question: Can I rename a folder in a collection?
  - id: deleteCollectionFolder
    intent: Delete a folder from a collection
    question: What's the call to delete a folder from a collection?
  - id: getCollectionRequest
    intent: Get a request in a collection
    question: Where can I read one saved request's details from a collection?
  - id: updateCollectionRequest
    intent: Update a request in a collection
    question: Can I change a saved request's URL or method?
  phrasing_ops: 12
  slug: postman-collection-items-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Collection Requests API from Postman — 2 operation(s) for collection requests.
  name: Postman Collection Requests API
  phrasing_intents:
  - id: getRequestComments
    intent: List comments on a request
    question: What have teammates said about a specific request in a collection?
  - id: createRequestComment
    intent: Comment on a request
    question: How do I leave a comment on a request inside a collection?
  - id: updateRequestComment
    intent: Edit a comment on a request
    question: How do I edit a comment I left on a request?
  - id: deleteRequestComment
    intent: Delete a comment on a request
    question: How do I remove a comment from a request?
  phrasing_ops: 4
  slug: postman-collection-requests-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Collection Responses API from Postman — 2 operation(s) for collection responses.
  name: Postman Collection Responses API
  phrasing_intents:
  - id: getResponseComments
    intent: List comments on a saved response
    question: What comments have been left on this example response?
  - id: createResponseComment
    intent: Comment on a saved response
    question: How do I comment on an example response?
  - id: updateResponseComment
    intent: Edit a comment on a saved response
    question: Can I edit my comment on an example response?
  - id: deleteResponseComment
    intent: Delete a comment on a saved response
    question: How do I delete a comment on an example response?
  phrasing_ops: 4
  slug: postman-collection-responses-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The OAuth 2.0 API from Postman — 2 operation(s) for oauth 2.0.
  name: Postman OAuth 2.0 API
  phrasing_intents:
  - id: generateOauthToken
    intent: Get an OAuth access token for a client app
    question: How does a backend service or bot get an OAuth token without a user?
  - id: revokeOauthToken
    intent: Revoke an OAuth access token
    question: Can a revoked OAuth token be restored?
  phrasing_ops: 2
  slug: postman-oauth-2-0-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Private API Network API from Postman — 4 operation(s) for private api network.
  name: Postman Private API Network API
  phrasing_intents:
  - id: listPrivateNetworkWorkspaces
    intent: List workspaces in the Private API Network
    question: Which workspaces has my team published to the Private API Network?
  - id: addWorkspaceToPrivateNetwork
    intent: Publish a workspace to the Private API Network
    question: How do I add a workspace to our team's Private API Network?
  - id: updatePanElementOrFolder
    intent: Update a private network workspace (deprecated)
    question: Is there a deprecated endpoint for updating a workspace entry in the Private API Network?
  - id: removeWorkspaceFromPrivateNetwork
    intent: Remove a workspace from the Private API Network
    question: Does removing a workspace from the Private API Network delete it?
  - id: listPrivateNetworkAddRequests
    intent: List requests to add workspaces to the network
    question: Who has asked to add workspaces to our Private API Network?
  - id: respondPrivateNetworkAddRequest
    intent: Approve or deny a request to add a workspace
    question: Who can approve a request to add a workspace to the Private API Network?
  phrasing_ops: 6
  slug: postman-private-api-network-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Pull Requests API from Postman — 2 operation(s) for pull requests.
  name: Postman Pull Requests API
  phrasing_intents:
  - id: getPullRequest
    intent: Get a pull request
    question: Who reviewed a pull request and has it been merged yet?
  - id: updatePullRequest
    intent: Edit an open pull request
    question: How do I change the title or reviewers of an open pull request?
  - id: reviewPullRequest
    intent: Approve, decline or merge a pull request
    question: How do I approve a pull request on a forked collection?
  phrasing_ops: 3
  slug: postman-pull-requests-api
- baseURL: https://api.getpostman.com
  baseurl_source: declared
  description: The Service Accounts API from Postman — 1 operation(s) for service accounts.
  name: Postman Service Accounts API
  phrasing_intents:
  - id: generateServiceAccountToken
    intent: Exchange a service account key for a token
    question: Can a service account get a short-lived access token from its API key?
  phrasing_ops: 1
  slug: postman-service-accounts-api
arazzos:
- description: Build a workspace, collection, and environment, then monitor and run the collection.
  name: Postman Stand Up an API Testing Pipeline
  slug: postman-api-testing-pipeline-workflow
- description: Create a workspace, then seed it with a collection and an environment.
  name: Postman Bootstrap a Workspace
  slug: postman-bootstrap-workspace-workflow
- description: Create, read, update, and delete a Postman collection end to end.
  name: Postman Collection Lifecycle
  slug: postman-collection-crud-workflow
- description: Create a scheduled monitor for a collection, then trigger and read a run.
  name: Postman Create and Run a Monitor
  slug: postman-create-and-run-monitor-workflow
- description: Create an API in a workspace, add a version, and attach an OpenAPI schema.
  name: Postman Create an API with a Schema
  slug: postman-create-api-with-schema-workflow
- description: Create a collection, stand up a mock server from it, and read the mock back.
  name: Postman Create a Mock Server from a Collection
  slug: postman-create-mock-from-collection-workflow
- description: Create, read, update, and delete a Postman environment with variables.
  name: Postman Environment Lifecycle
  slug: postman-environment-crud-workflow
- description: Fork a collection into a workspace, then merge the fork back into the source.
  name: Postman Fork and Merge a Collection
  slug: postman-fork-and-merge-collection-workflow
- description: Read an API, list its schemas, fetch one schema, and read its files.
  name: Postman Inspect an API Schema
  slug: postman-inspect-api-schema-workflow
- description: Read a collection's requests, folders, and saved example responses.
  name: Postman Inspect Collection Contents
  slug: postman-inspect-collection-contents-workflow
- description: Read a mock server, review its custom responses, and pull its call logs.
  name: Postman Audit Mock Server Call Logs
  slug: postman-mock-call-logs-workflow
- description: Create, update the schedule, run, and delete a Postman monitor.
  name: Postman Monitor Lifecycle
  slug: postman-monitor-lifecycle-workflow
- description: Create a collection, organize a network folder, and publish the collection into it.
  name: Postman Publish a Collection to the Private API Network
  slug: postman-publish-collection-to-network-workflow
- description: Publish an existing mock server, add a custom server response, and verify it.
  name: Postman Publish a Mock and Add a Custom Response
  slug: postman-publish-mock-and-add-response-workflow
- description: Find unresolved secrets, inspect one, locate it, and mark it revoked.
  name: Postman Remediate a Detected Secret
  slug: postman-remediate-detected-secret-workflow
- description: List a collection's run history and pull the latest run's full details.
  name: Postman Review the Latest Collection Run
  slug: postman-review-collection-run-workflow
- description: Create a collection, apply governance tags to it, and read the tags back.
  name: Postman Tag a Collection for Governance
  slug: postman-tag-collection-workflow
- description: List pending network requests, then approve the oldest one and confirm the catalog.
  name: Postman Triage a Private API Network Request
  slug: postman-triage-network-request-workflow
- description: Create a collection, then create a webhook that runs it on incoming POSTs.
  name: Postman Webhook Triggers a Collection
  slug: postman-webhook-triggers-collection-workflow
- description: Create, read, update, and delete a Postman workspace.
  name: Postman Workspace Lifecycle
  slug: postman-workspace-crud-workflow
- description: Create a workspace, then set and verify its global variables.
  name: Postman Manage Workspace Global Variables
  slug: postman-workspace-global-variables-workflow
artifact_total: 394
asyncapis:
- description: Postman Webhooks enable you to receive incoming HTTP POST requests that trigger collection runs. When an external system sends a POST request to a Postman webhook URL, the webhook triggers a collectio
  name: Postman Webhooks
  slug: postman-webhooks-asyncapi
collections:
- collection_type: postman
  name: Postman APIs API
  slug: postman-postman-apis-api
- collection_type: postman
  name: Postman Audit Logs API
  slug: postman-postman-audit-logs-api
- collection_type: postman
  name: Postman Collection Runs API
  slug: postman-postman-collection-runs-api
- collection_type: postman
  name: Postman Collections API
  slug: postman-postman-collections-api
- collection_type: postman
  name: Postman Environments API
  slug: postman-postman-environments-api
- collection_type: postman
  name: Postman Mock Servers API
  slug: postman-postman-mock-servers-api
- collection_type: postman
  name: Postman Monitors API
  slug: postman-postman-monitors-api
- collection_type: postman
  name: Postman Private API Network API
  slug: postman-postman-private-api-network-api
- collection_type: postman
  name: Postman Secret Scanner API
  slug: postman-postman-secret-scanner-api
- collection_type: postman
  name: Postman Tags API
  slug: postman-postman-tags-api
- collection_type: postman
  name: Postman Webhooks API
  slug: postman-postman-webhooks-api
- collection_type: postman
  name: Postman Workspaces API
  slug: postman-postman-workspaces-api
- collection_type: open
  name: Postman Analytics API
  slug: open-postman-analytics-api
- collection_type: open
  name: Postman API
  slug: open-postman-api-api
- collection_type: open
  name: Postman API Catalog API
  slug: open-postman-apicatalog-api
- collection_type: open
  name: Postman APIs API
  slug: open-postman-apis-api
- collection_type: open
  name: Postman API Security API
  slug: open-postman-apisecurity-api
- collection_type: open
  name: Postman Audit Logs API
  slug: open-postman-audit-logs-api
- collection_type: open
  name: Postman Audit Logs API
  slug: open-postman-auditlogs-api
- collection_type: open
  name: Postman Billing API
  slug: open-postman-billing-api
- collection_type: open
  name: Postman Collection Runs API
  slug: open-postman-collection-runs-api
- collection_type: open
  name: Postman Collection Access Keys API
  slug: open-postman-collectionaccesskeys-api
- collection_type: open
  name: Postman Collection Folders API
  slug: open-postman-collectionfolders-api
- collection_type: open
  name: Postman Collection Items API
  slug: open-postman-collectionitems-api
- collection_type: open
  name: Postman Collection Requests API
  slug: open-postman-collectionrequests-api
- collection_type: open
  name: Postman Collection Responses API
  slug: open-postman-collectionresponses-api
- collection_type: open
  name: Postman Collections API
  slug: open-postman-collections-api
- collection_type: open
  name: Postman Comments API
  slug: open-postman-comments-api
- collection_type: open
  name: Postman Components API
  slug: open-postman-components-api
- collection_type: open
  name: Postman Environments API
  slug: open-postman-environments-api
- collection_type: open
  name: Postman Groups API
  slug: open-postman-groups-api
- collection_type: open
  name: Postman Import API
  slug: open-postman-import-api
- collection_type: open
  name: Postman Mock Servers API
  slug: open-postman-mock-servers-api
- collection_type: open
  name: Postman Mocks API
  slug: open-postman-mocks-api
- collection_type: open
  name: Postman Monitors API
  slug: open-postman-monitors-api
- collection_type: open
  name: Postman O Auth20 API
  slug: open-postman-oauth20-api
- collection_type: open
  name: Postman Postbot API
  slug: open-postman-postbot-api
- collection_type: open
  name: Postman Private API Network API
  slug: open-postman-private-api-network-api
- collection_type: open
  name: Postman Private API Network API
  slug: open-postman-privateapinetwork-api
- collection_type: open
  name: Postman Pull Requests API
  slug: open-postman-pullrequests-api
- collection_type: open
  name: Postman SCIM API
  slug: open-postman-scim-api
- collection_type: open
  name: Postman Sd Ks API
  slug: open-postman-sdks-api
- collection_type: open
  name: Postman Search API
  slug: open-postman-search-api
- collection_type: open
  name: Postman Secret Scanner API
  slug: open-postman-secret-scanner-api
- collection_type: open
  name: Postman Secret Scanner API
  slug: open-postman-secretscanner-api
- collection_type: open
  name: Postman Service Accounts API
  slug: open-postman-serviceaccounts-api
- collection_type: open
  name: Postman Specs API
  slug: open-postman-specs-api
- collection_type: open
  name: Postman Tags API
  slug: open-postman-tags-api
- collection_type: open
  name: Postman Teams API
  slug: open-postman-teams-api
- collection_type: open
  name: Postman Users API
  slug: open-postman-users-api
- collection_type: open
  name: Postman Webhooks API
  slug: open-postman-webhooks-api
- collection_type: open
  name: Postman Workspaces API
  slug: open-postman-workspaces-api
common:
- group: commercial
  href: https://artifacts.apis.io/postman/plans/postman-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/postman-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/postman/finops/postman-finops.yml
  title: ''
  type: FinOps
  url: finops/postman-finops.yml
- group: operate
  href: https://artifacts.apis.io/postman/rate-limits/postman-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/postman-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/postman/rules/postman-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/postman-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/postman/rules/postman-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/postman-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/postman/json-ld/postman-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/postman-context.jsonld
- group: agent
  href: https://artifacts.apis.io/postman/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/postman/asyncapi/postman-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/postman-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/postman/data-model/postman-data-model.yml
  title: ''
  type: DataModel
  url: data-model/postman-data-model.yml
- group: design
  href: https://artifacts.apis.io/postman/errors/postman-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/postman-problem-types.yml
- group: design
  href: https://artifacts.apis.io/postman/conformance/postman-conformance.yml
  title: ''
  type: Conformance
  url: conformance/postman-conformance.yml
- group: agent
  href: https://artifacts.apis.io/postman/llms/postman-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/postman-llms.txt
- group: agent
  href: https://artifacts.apis.io/postman/well-known/postman-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/postman-well-known.yml
- group: other
  href: https://artifacts.apis.io/postman/hosts/postman-hosts.yml
  title: ''
  type: Hosts
  url: hosts/postman-hosts.yml
- group: other
  href: https://artifacts.apis.io/postman/vendors/postman-vendors.yml
  title: ''
  type: Vendors
  url: vendors/postman-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: http://api.eu.postman.com`
- group: other
  href: https://artifacts.apis.io/postman/vendor-facets/postman-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/postman-vendor-facets.yml
- group: other
  href: https://artifacts.apis.io/postman/capabilities/postman-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/postman-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/postman/agentic-access/postman-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/postman-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/postman/security/postman-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/postman-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/postman/security/postman-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/postman-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/postman/security/postman-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postman-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/postman/authentication/postman-authentication.yml
  title: ''
  type: Authentication
  url: authentication/postman-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/postman/overview
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-api-testing-pipeline-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-api-testing-pipeline-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-bootstrap-workspace-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-bootstrap-workspace-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-collection-crud-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-collection-crud-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-create-and-run-monitor-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-create-and-run-monitor-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-create-api-with-schema-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-create-api-with-schema-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-create-mock-from-collection-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-create-mock-from-collection-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-environment-crud-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-environment-crud-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-fork-and-merge-collection-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-fork-and-merge-collection-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-inspect-api-schema-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-inspect-api-schema-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-inspect-collection-contents-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-inspect-collection-contents-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-mock-call-logs-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-mock-call-logs-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-monitor-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-monitor-lifecycle-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-publish-collection-to-network-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-publish-collection-to-network-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-publish-mock-and-add-response-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-publish-mock-and-add-response-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-remediate-detected-secret-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-remediate-detected-secret-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-review-collection-run-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-review-collection-run-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-tag-collection-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-tag-collection-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-triage-network-request-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-triage-network-request-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-webhook-triggers-collection-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-webhook-triggers-collection-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-workspace-crud-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-workspace-crud-workflow.yml
- group: design
  href: https://artifacts.apis.io/postman/arazzo/postman-workspace-global-variables-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/postman-workspace-global-variables-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.postman.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.postman.com/pricing/
- group: other
  title: ''
  type: Knowledgebase
  url: https://www.postman.com/learn/
- group: docs
  title: ''
  type: Documentation
  url: https://learning.postman.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://learning.postman.com/docs/developer/postman-api/intro-api/
- group: auth
  title: ''
  type: Authentication
  url: https://learning.postman.com/docs/developer/postman-api/authentication/
- group: operate
  title: ''
  type: RateLimits
  url: https://learning.postman.com/docs/developer/postman-api/postman-api-rate-limits/
- group: company
  title: ''
  type: Blog
  url: https://blog.postman.com/
- group: other
  title: ''
  type: Templates
  url: https://www.postman.com/templates/
- group: operate
  title: ''
  type: Support
  url: https://support.postman.com/hc/en-us
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.postman.com/release-notes/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.postman.com/
- group: other
  title: ''
  type: Events
  url: https://www.postman.com/events/
- group: build
  title: ''
  type: CLI
  url: https://learning.postman.com/docs/postman-cli/postman-cli-installation/
- group: build
  title: ''
  type: CLI
  url: https://github.com/postmanlabs/newman
- group: company
  title: ''
  type: Partners
  url: https://www.postman.com/partner-program/
- group: other
  title: ''
  type: Customers
  url: https://www.postman.com/case-studies/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.postman.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.postman.com/legal/privacy-policy/
- group: other
  title: ''
  type: Trademark
  url: https://www.postman.com/legal/trademark-policy/
- group: auth
  title: ''
  type: Trust
  url: https://www.postman.com/trust/
- group: auth
  title: ''
  type: Security
  url: https://security.postman.com/
- group: auth
  title: ''
  type: Compliance
  url: https://www.postman.com/trust/compliance/
- group: build
  title: ''
  type: VSCodeExtension
  url: https://marketplace.visualstudio.com/items?itemName=Postman.postman-for-vscode
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Postman
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/postman-platform
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/getpostman
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/getpostman/
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/bKjz3CXbB6
- group: operate
  title: ''
  type: Forums
  url: https://community.postman.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/postman
- group: other
  title: ''
  type: Downloads
  url: https://www.postman.com/downloads/
- group: other
  title: ''
  type: APINetwork
  url: https://www.postman.com/explore
- group: agent
  title: ''
  type: MCPNetwork
  url: https://www.postman.com/explore/mcp
- group: learn
  title: ''
  type: Academy
  url: https://academy.postman.com/
- group: other
  title: ''
  type: StudentProgram
  url: https://www.postman.com/student-program/
- group: company
  title: ''
  type: About
  url: https://www.postman.com/company/about-postman/
- group: company
  title: ''
  type: Careers
  url: https://www.postman.com/company/careers/
- group: operate
  title: ''
  type: ContactSales
  url: https://www.postman.com/company/contact-sales/
- group: company
  title: ''
  type: Press
  url: https://www.postman.com/company/press-media/
- group: build
  title: ''
  type: SDKs
  url: https://learning.postman.com/docs/developer/collection-sdk/
- group: docs
  title: ''
  type: SchemaCatalog
  url: https://schema.postman.com/
- group: other
  title: ''
  type: AIAgentBuilder
  url: https://www.postman.com/product/ai-agent-builder/
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/postmanlabs/postman-mcp-server
- group: other
  title: ''
  type: Flows
  url: https://www.postman.com/product/flows/
- group: other
  title: ''
  type: Governance
  url: https://www.postman.com/api-platform/api-governance/
- group: agent
  title: ''
  type: LlmsText
  url: https://www.postman.com/llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: https://learning.postman.com/api-docs/openapi.json
- group: other
  title: ''
  type: Workspaces
  url: https://www.postman.com/product/workspaces/
- group: other
  title: ''
  type: APICatalog
  url: https://www.postman.com/product/api-catalog/
- group: start
  title: ''
  type: Signup
  url: https://identity.getpostman.com/signup
- group: start
  title: ''
  type: Login
  url: https://identity.getpostman.com/login
- group: start
  title: ''
  type: Console
  url: https://go.postman.co/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postmanlabs
- group: company
  title: ''
  type: Newsletter
  url: https://www.postman.com/newsletter/
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/postmanlabs/postman-skills-2
created: '2025-01-08T00:00:00.000Z'
description: Postman is the world's leading API platform, used by 35+ million developers to design, build, test, document, mock, monitor, and govern APIs across the entire API lifecycle. The platform spans Collections, Workspaces, the API Client, Spec Hub, Mock Servers, Monitors, the Postman CLI, Newman, Flows, AI Agent Builder, the Postman MCP Server and MCP Generator, API Governance, the Private API Network, Live Collections, Insights, and a public Postman API Network with millions of public workspaces.
examples:
- key_count: 2
  name: Postman Audit Logs Example
  slug: postman-audit-logs-example
- key_count: 2
  name: Postman Create Api Spec Example
  slug: postman-create-api-spec-example
- key_count: 2
  name: Postman Create Mock Server Example
  slug: postman-create-mock-server-example
- key_count: 2
  name: Postman Get All Collections Example
  slug: postman-get-all-collections-example
- key_count: 2
  name: Postman Run Monitor Example
  slug: postman-run-monitor-example
features:
- name: API Client (HTTP, GraphQL, gRPC, WebSocket, MQTT, Socket.io)
- name: Collections
- name: Workspaces (Personal, Team, Partner, Private, Public)
- name: Environments and Variables
- name: Postman Vault (Encrypted Secret Storage)
- name: Mock Servers
- name: Monitors and Scheduled Collection Runs
- name: Documentation and Custom Domains
- name: Collection Runner
- name: Newman CLI
- name: Postman CLI
- name: Spec Hub (OpenAPI, AsyncAPI, GraphQL, gRPC, RAML, WSDL)
- name: Live Collections
- name: SDK Generator
- name: Postman Flows (Visual Workflow Builder)
- name: Postman AI Agent Builder
- name: Postman MCP Server
- name: Postman MCP Generator
- name: Postman Insights (Production API Observability)
- name: API Governance (Rules, Reports, Linting)
- name: Custom Governance Rules
- name: Secret Scanner
- name: Security Warnings
- name: Audit Logs
- name: Private API Network
- name: Public API Network
- name: API Catalog
- name: Role-Based Access Control (Basic and Advanced)
- name: Element-Level Roles
- name: Single Sign-On (SAML, SSO)
- name: SCIM 2.0 User Provisioning
- name: Postman Interceptor
- name: Postman Proxy
- name: VS Code Extension
- name: Postbot AI Assistant
- name: Partner Workspaces
- name: Reporting and Analytics
- name: Data-Driven Testing
- name: Test Data Storage
- name: Webhooks and Integrations
- name: Multi-Region Monitors
- name: Private Cloud Runners
- name: 90-Day Collection Recovery
finops:
- has_sources: true
  method: derived
  name: Postman Finops
  primary_unit: month billed annually
  service_category: ''
  slug: postman-finops
  template: false
image: https://www.postman.com/assets/logos/postman-logo-horizontal-orange.svg
integrations:
- name: 1Password Vault
- name: Aikido Security
- name: Amazon API Gateway
- name: Apigee
- name: APIMatic
- name: APIsec
- name: AppMap
- name: AWS API Gateway
- name: AWS Secrets Manager
- name: Azure API Management
- name: Azure DevOps
- name: Azure Key Vault
- name: BigPanda
- name: Bitbucket
- name: Bitbucket Pipelines
- name: CircleCI
- name: Coralogix
- name: Datadog
- name: Dropbox
- name: GitHub
- name: GitHub Actions
- name: GitLab
- name: GitLab CI/CD
- name: HashiCorp Vault
- name: Helios
- name: ilert
- name: Jenkins
- name: Jira
- name: Keen
- name: liblab
- name: Microsoft Power Automate
- name: Microsoft Teams
- name: New Relic
- name: OpenAPI
- name: Opsgenie
- name: PagerDuty
- name: Pynt
- name: ReadMe
- name: Slack
- name: Snyk
- name: Speedscale
- name: Splunk
- name: Splunk On-Call
- name: Stainless
- name: StatusPage
- name: Travis CI
- name: VS Code
- name: Workato
json_schemas:
- name: ApiSchema
  property_count: 9
  slug: postman-api-schema
- name: approveDenyAccessRequestResponse
  property_count: 1
  slug: postman-approve-deny-access-request-response
- name: asyncCollectionForkMerge
  property_count: 3
  slug: postman-async-collection-fork-merge
- name: CollectionRun
  property_count: 11
  slug: postman-collection-run
- name: CollectionRunSummary
  property_count: 9
  slug: postman-collection-run-summary
- name: Postman Collection
  property_count: 6
  slug: postman-collection
- name: commentCreate
  property_count: 3
  slug: postman-comment-create
- name: commentCreatedUpdated
  property_count: 1
  slug: postman-comment-created-updated
- name: commentResponse
  property_count: 1
  slug: postman-comment-response
- name: commentUpdate
  property_count: 2
  slug: postman-comment-update
- name: componentVersionData
  property_count: 6
  slug: postman-component-version-data
- name: createAccessRequest
  property_count: 4
  slug: postman-create-access-request
- name: createApiCatalogSystemEnvironment
  property_count: 5
  slug: postman-create-api-catalog-system-environment
- name: createApiResponse
  property_count: 8
  slug: postman-create-api-response
- name: createApiSchemaResponse
  property_count: 7
  slug: postman-create-api-schema-response
- name: createCollectionRequestResponse
  property_count: 4
  slug: postman-create-collection-request-response
- name: createCollectionRequest
  property_count: 13
  slug: postman-create-collection-request
- name: createCollectionResponse
  property_count: 17
  slug: postman-create-collection-response
- name: createComponent
  property_count: 4
  slug: postman-create-component
- name: createComponentVersion
  property_count: 2
  slug: postman-create-component-version
- name: createMonitor
  property_count: 1
  slug: postman-create-monitor
- name: createScimUser
  property_count: 7
  slug: postman-create-scim-user
- name: createSdkGitConnection
  property_count: 5
  slug: postman-create-sdk-git-connection
- name: createSdk
  property_count: 15
  slug: postman-create-sdk
- name: createSpecResponse
  property_count: 7
  slug: postman-create-spec-response
- name: createTeam
  property_count: 2
  slug: postman-create-team
- name: createUpdateApiSchemaFileResponse
  property_count: 8
  slug: postman-create-update-api-schema-file-response
- name: createUpdateMonitorResponse
  property_count: 1
  slug: postman-create-update-monitor-response
- name: createUpdateSpecFileResponse
  property_count: 7
  slug: postman-create-update-spec-file-response
- name: createWebhookResponse
  property_count: 1
  slug: postman-create-webhook-response
- name: createWebhook
  property_count: 1
  slug: postman-create-webhook
- name: createWorkspaceUpdate
  property_count: 4
  slug: postman-create-workspace-update
- name: deleteMockServerResponse
  property_count: 9
  slug: postman-delete-mock-server-response
- name: deletePanElement
  property_count: 1
  slug: postman-delete-pan-element
- name: DetectedSecretDetail
  property_count: 11
  slug: postman-detected-secret-detail
- name: DetectedSecret
  property_count: 8
  slug: postman-detected-secret
- name: detectedSecretsQueriesRequest
  property_count: 6
  slug: postman-detected-secrets-queries-request
- name: Postman Environment
  property_count: 10
  slug: postman-environment
- name: Environments_patchEnvironment_Request
  property_count: 0
  slug: postman-environments-patch-environment-request
- name: forkEnvironmentResponse
  property_count: 1
  slug: postman-fork-environment-response
- name: generateOauthTokenResponse
  property_count: 3
  slug: postman-generate-oauth-token-response
- name: generateOauthToken
  property_count: 3
  slug: postman-generate-oauth-token
- name: generateServiceAccountTokenResponse
  property_count: 1
  slug: postman-generate-service-account-token-response
- name: generateToolResponse
  property_count: 1
  slug: postman-generate-tool-response
- name: generateTool
  property_count: 3
  slug: postman-generate-tool
- name: getAccountInvoices
  property_count: 1
  slug: postman-get-account-invoices
- name: getAllPanAddElementRequests
  property_count: 2
  slug: postman-get-all-pan-add-element-requests
- name: getAnalyticsData
  property_count: 1
  slug: postman-get-analytics-data
- name: getAnalyticsMetadata
  property_count: 1
  slug: postman-get-analytics-metadata
- name: getApiCatalogDiscoveryService
  property_count: 20
  slug: postman-get-api-catalog-discovery-service
- name: getApiCatalogServiceEndpoints
  property_count: 2
  slug: postman-get-api-catalog-service-endpoints
- name: getApiCatalogServiceMonitorRuns
  property_count: 2
  slug: postman-get-api-catalog-service-monitor-runs
- name: getApiCatalogServiceSpecificationLints
  property_count: 2
  slug: postman-get-api-catalog-service-specification-lints
- name: getApiCollection
  property_count: 4
  slug: postman-get-api-collection
- name: getApiSchemaFileContents
  property_count: 8
  slug: postman-get-api-schema-file-contents
- name: getAuditLogEventActions
  property_count: 0
  slug: postman-get-audit-log-event-actions
- name: getAuditLogs
  property_count: 1
  slug: postman-get-audit-logs
- name: getAuthenticatedUser
  property_count: 2
  slug: postman-get-authenticated-user
- name: getCollectionAccessKeys
  property_count: 2
  slug: postman-get-collection-access-keys
- name: getComponentVersions
  property_count: 2
  slug: postman-get-component-versions
- name: getEnvironmentForks
  property_count: 2
  slug: postman-get-environment-forks
- name: getGroup
  property_count: 10
  slug: postman-get-group
- name: getGroups
  property_count: 1
  slug: postman-get-groups
- name: getMockCallLogs
  property_count: 2
  slug: postman-get-mock-call-logs
- name: getMocks
  property_count: 1
  slug: postman-get-mocks
- name: getMonitors
  property_count: 2
  slug: postman-get-monitors
- name: getPanElements
  property_count: 3
  slug: postman-get-pan-elements
- name: getRunnerInstances
  property_count: 2
  slug: postman-get-runner-instances
- name: getRunnerMetrics
  property_count: 3
  slug: postman-get-runner-metrics
- name: getScimServiceProviderConfig
  property_count: 10
  slug: postman-get-scim-service-provider-config
- name: getSpecFile
  property_count: 9
  slug: postman-get-spec-file
- name: getTaggedEntities
  property_count: 2
  slug: postman-get-tagged-entities
- name: getTeamAccessRequests
  property_count: 2
  slug: postman-get-team-access-requests
- name: getTeamUsers
  property_count: 1
  slug: postman-get-team-users
- name: getWorkspaces
  property_count: 2
  slug: postman-get-workspaces
- name: Import_openApiDefinition_Request
  property_count: 0
  slug: postman-import-open-api-definition-request
- name: importOpenApiDefinition
  property_count: 1
  slug: postman-import-open-api-definition
- name: invoicesAccountInfo
  property_count: 6
  slug: postman-invoices-account-info
- name: manageTeamMemberRoles
  property_count: 2
  slug: postman-manage-team-member-roles
- name: mergeCollectionFork
  property_count: 3
  slug: postman-merge-collection-fork
- name: mergeEnvironmentForkResponse
  property_count: 1
  slug: postman-merge-environment-fork-response
- name: mergeEnvironmentFork
  property_count: 2
  slug: postman-merge-environment-fork
- name: mockCreateUpdateResponse
  property_count: 1
  slug: postman-mock-create-update-response
- name: mockServerResponse
  property_count: 11
  slug: postman-mock-server-response
- name: NetworkElement
  property_count: 10
  slug: postman-network-element
- name: NetworkFolder
  property_count: 7
  slug: postman-network-folder
- name: NetworkRequest
  property_count: 11
  slug: postman-network-request
- name: panElementCreated
  property_count: 13
  slug: postman-pan-element-created
- name: Private API Network_respondPrivateNetworkAddRequest_Response_200
  property_count: 0
  slug: postman-private-api-network-respond-private-network-add-request-response-200
- name: publishDocumentationResponse
  property_count: 10
  slug: postman-publish-documentation-response
- name: publishDocumentation
  property_count: 4
  slug: postman-publish-documentation
- name: publishUnpublishMockResponse
  property_count: 1
  slug: postman-publish-unpublish-mock-response
- name: pullEnvironmentResponse
  property_count: 1
  slug: postman-pull-environment-response
- name: pullRequestCreated
  property_count: 9
  slug: postman-pull-request-created
- name: pullRequestGet
  property_count: 14
  slug: postman-pull-request-get
- name: pullRequestReviewReponse
  property_count: 4
  slug: postman-pull-request-review-reponse
- name: pullRequestReview
  property_count: 2
  slug: postman-pull-request-review
- name: pullRequestUpdate
  property_count: 3
  slug: postman-pull-request-update
- name: pullRequestUpdated
  property_count: 10
  slug: postman-pull-request-updated
- name: respondPanElementAddRequestBody
  property_count: 2
  slug: postman-respond-pan-element-add-request-body
- name: runMonitor
  property_count: 1
  slug: postman-run-monitor
- name: schemaSecurityValidationRequest
  property_count: 1
  slug: postman-schema-security-validation-request
- name: schemaSecurityValidationResponse
  property_count: 1
  slug: postman-schema-security-validation-response
- name: sdkDownload
  property_count: 4
  slug: postman-sdk-download
- name: sdkGitConnectionPullRequestList
  property_count: 2
  slug: postman-sdk-git-connection-pull-request-list
- name: sdkGitConnection
  property_count: 11
  slug: postman-sdk-git-connection
- name: sdk
  property_count: 10
  slug: postman-sdk
- name: searchPostmanResourcesResponse
  property_count: 2
  slug: postman-search-postman-resources-response
- name: searchPostmanResources
  property_count: 4
  slug: postman-search-postman-resources
- name: SecretLocation
  property_count: 8
  slug: postman-secret-location
- name: ServerResponseInput
  property_count: 5
  slug: postman-server-response-input
- name: ServerResponse
  property_count: 8
  slug: postman-server-response
- name: specData
  property_count: 8
  slug: postman-spec-data
- name: tagGetPut
  property_count: 1
  slug: postman-tag-get-put
- name: Tag
  property_count: 2
  slug: postman-tag
- name: tagUpdateTags
  property_count: 1
  slug: postman-tag-update-tags
- name: teamUser
  property_count: 6
  slug: postman-team-user
- name: Teams_getTeams_Response_200
  property_count: 2
  slug: postman-teams-get-teams-response-200
- name: transferCollectionItems
  property_count: 4
  slug: postman-transfer-collection-items
- name: transferWorkspaceElement
  property_count: 3
  slug: postman-transfer-workspace-element
- name: updateApiCatalogSystemEnvironment
  property_count: 4
  slug: postman-update-api-catalog-system-environment
- name: updateApiResponse
  property_count: 8
  slug: postman-update-api-response
- name: updateCollectionFolderResponse
  property_count: 4
  slug: postman-update-collection-folder-response
- name: updateCollectionRequest
  property_count: 13
  slug: postman-update-collection-request
- name: updateCollectionResponse
  property_count: 17
  slug: postman-update-collection-response
- name: updateComponentDraft
  property_count: 2
  slug: postman-update-component-draft
- name: updateComponentResponse
  property_count: 3
  slug: postman-update-component-response
- name: updateSecretResolutionsRequest
  property_count: 2
  slug: postman-update-secret-resolutions-request
- name: updateSecretResolutions
  property_count: 4
  slug: postman-update-secret-resolutions
- name: updateSpecFile
  property_count: 3
  slug: postman-update-spec-file
- name: updateSpecPropertiesResponse
  property_count: 7
  slug: postman-update-spec-properties-response
- name: updateWorkspaceUpdate
  property_count: 5
  slug: postman-update-workspace-update
- name: Postman Workspace
  property_count: 14
  slug: postman-workspace
- name: workspaceUpdateData
  property_count: 11
  slug: postman-workspace-update-data
- name: workspaceUpdatePostPatchResponseData
  property_count: 11
  slug: postman-workspace-update-post-patch-response-data
json_structures:
- name: Postman Collection Structure
  property_count: 6
  slug: postman-collection-structure
- name: Postman Monitor Structure
  property_count: 1
  slug: postman-monitor-structure
- name: Postman Workspace Structure
  property_count: 1
  slug: postman-workspace-structure
jsonld:
- class_count: 120
  name: Postman Context
  property_count: 155
  slug: postman-context
layout: provider
mcp_servers:
- description: ''
  name: Postman MCP Server
  slug: postman-mcp-server
- description: Remote MCP server at mcp.postman.com over HTTP.
  name: Postman MCP Server
  slug: postman
modified: '2026-09-16'
name: Postman
nav: Providers
network: true
overview: 'Postman publishes 43 API contracts indexed on the [APIs.io](https://apis.io/) network, including Postman, Collections API, Workspaces API, and 40 more. Tagged areas include Environment, Flow, Specification, Workspace, and Postman.


  The Postman catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Postman''s developer surface includes authentication, pricing, documentation, getting-started guide, engineering blog, support, changelog, and 94 more developer resources.'
plans:
- name: Postman Plans Pricing
  plan_count: 8
  slug: postman-plans-pricing
- name: Postman Price Estimates
  plan_count: 0
  slug: postman-price-estimates
random_paper: 2
rate_limits:
- limit_count: 6
  name: Postman Rate Limits
  slug: postman-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Postman — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: postman-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Postman — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: postman-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 83
  extends:
  - spectral:oas
  - spectral:asyncapi
  name: Postman API Rules
  rule_count: 15
  severity_counts:
    error: 7
    hint: 0
    info: 0
    warn: 8
  slug: postman-rules
score:
  band: exemplar
  composite: 83.5
  coverage:
    artifact_dirs: 36
    catalog_earned: 82.0
    catalog_earned_first_party: 12.0
    catalog_gap: 33.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 77.3
    developer_ergonomics: 68.5
    discoverability: 83.3
    operational_transparency: 63.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 84.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 82.5
      total: 40
    mcp: first-party
    skills: derived
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
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/postman/postman-2026-06-20T192015.png
security:
- kind: authentication
  name: Postman Authentication
  slug: postman-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Postman Domain Security
  slug: postman-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Postman Vulnerability Disclosure
  slug: postman-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Postman Trust Center
  slug: postman-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, HIPAA, GDPR, CSA STAR
skill_count: 5
skills:
- name: postman-collection-create-and-publish
  slug: postman-collection-create-and-publish
- name: postman-collection-items-create
  slug: postman-collection-items-create
- name: postman-create-api-add-collection
  slug: postman-create-api-add-collection
- name: postman-create-workspace
  slug: postman-create-workspace
- name: postman-manage-request-comments
  slug: postman-manage-request-comments
slug: postman
solutions:
- name: API-First Development
- name: Enterprise API Platform
- name: API Testing at Scale
- name: API Governance and Compliance
- name: Developer Experience
- name: AI Agents and MCP
- name: Partner Integrations
- name: Microservices and Distributed Systems
- name: API Productization
tags:
- Environment
- Flow
- Specification
- Workspace
- Postman
- AI Agent Builder
- AI Agents
- API Catalog
- API Client
- API Design
- API Development
- API Documentation
- API Governance
- API Lifecycle
- API Monitoring
- API Network
- API Platform
- API Testing
- Audit Logs
- Automation
- CI/CD
- Collaboration
- Collection
- Compliance
- Discovery
- GraphQL
- gRPC
- HTTP
- Insights
- MCP
- MCP Generator
- Mock Servers
- Mocking
- Monitors
- Newman
- OpenAPI
- Platform
- Private API Network
- Public API Network
- Secret Scanning
- Spec Hub
- SSO
- Testing
- Vault
- WebSocket
- Workflows
use_cases:
- name: API-First Development
- name: API Testing and Quality
- name: API Documentation
- name: API Mocking and Simulation
- name: API Monitoring and Observability
- name: API Governance and Compliance
- name: API Discovery and Catalog
- name: Developer Portals
- name: Developer Onboarding
- name: Partner API Programs
- name: CI/CD and Test Automation
- name: AI Agent Development
- name: MCP Server Publishing
- name: API Workflow Orchestration
website: https://www.postman.com/
---
