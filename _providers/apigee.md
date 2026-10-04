---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.5
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 101
  human_in_the_loop: 1
  name: Apigee Agentic Access
  operation_count: 179
  slug: apigee-agentic-access
  summary_line: 179 operations · 101 acting · 1 human-in-the-loop
api_count: 5
apis:
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Query analytics data and manage data stores
  name: Apigee Analytics API
  phrasing_intents:
  - id: getEnvironmentStats
    intent: Get traffic and latency stats for an environment
    question: How much traffic and how many errors did my API proxies see last week?
  - id: listDatastores
    intent: List analytics export data stores
    question: Where can my analytics data be exported to?
  - id: createDatastore
    intent: Create an analytics export data store
    question: How do I set up a destination for exporting Apigee analytics data?
  phrasing_ops: 3
  slug: apigee-analytics-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Track API deployment records
  name: Apigee API Deployments API
  phrasing_intents:
  - id: listApiDeployments
    intent: List deployment records for a registry API
    question: Where is a given API deployed according to the Apigee Registry?
  - id: createApiDeployment
    intent: Record a deployment for a registry API
    question: How do I record an endpoint URI where a registry API is deployed?
  - id: getApiDeployment
    intent: Get a registry API deployment record
    question: Which spec revision and endpoint does a registry deployment record point to?
  - id: updateApiDeployment
    intent: Update a registry API deployment record
    question: Can I change the endpoint URI on an existing registry deployment?
  - id: deleteApiDeployment
    intent: Delete a registry API deployment record
    question: How do I delete a deployment record from a registry API?
  - id: rollbackApiDeployment
    intent: Roll a registry deployment back to a revision
    question: How do I revert a registry deployment record to an earlier revision?
  phrasing_ops: 6
  slug: apigee-api-deployments-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: View and manage discovered API observations
  name: Apigee API Observations API
  phrasing_intents:
  - id: listApiObservations
    intent: List shadow APIs found by an observation job
    question: What shadow APIs has my observation job discovered?
  - id: getApiObservation
    intent: Get a discovered API observation
    question: What hostname and server IPs does a discovered shadow API have?
  - id: batchEditApiObservationTags
    intent: Tag several discovered APIs at once
    question: Can I tag many discovered APIs in one call?
  phrasing_ops: 3
  slug: apigee-api-observations-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: View discovered API operations
  name: Apigee API Operations API
  phrasing_intents:
  - id: listApiOperations
    intent: List endpoints found in a discovered API
    question: Which HTTP methods and paths were detected on a discovered API?
  - id: getApiOperation
    intent: Get a discovered API operation
    question: What traffic statistics exist for one discovered endpoint?
  phrasing_ops: 2
  slug: apigee-api-operations-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Bundle APIs into products for consumption
  name: Apigee API Products API
  phrasing_intents:
  - id: listApiProducts
    intent: List API products in an organization
    question: What API products are defined in my Apigee organization?
  - id: createApiProduct
    intent: Create an API product
    question: How do I bundle API proxies into a product that developers can subscribe to?
  - id: getApiProduct
    intent: Get an API product's configuration
    question: Which proxies, environments and quota does an API product include?
  - id: updateApiProduct
    intent: Update an API product
    question: Do I need to send the whole API product object to change one setting?
  - id: deleteApiProduct
    intent: Delete an API product
    question: What happens to apps using an API product when I delete it?
  phrasing_ops: 5
  slug: apigee-api-products-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Create, deploy, and manage API proxy definitions
  name: Apigee API Proxies API
  phrasing_intents:
  - id: listApiProxies
    intent: List API proxies in an organization
    question: What API proxies exist in my Apigee organization?
  - id: createApiProxy
    intent: Create an API proxy
    question: How do I create a new API proxy from a bundle?
  - id: getApiProxy
    intent: Get an API proxy and its revisions
    question: Which revisions exist for one of my API proxies?
  - id: deleteApiProxy
    intent: Delete an API proxy
    question: Must a proxy be undeployed everywhere before I can delete it?
  - id: patchApiProxy
    intent: Update an API proxy's labels and metadata
    question: Can I change the labels on an API proxy without uploading a new bundle?
  phrasing_ops: 5
  slug: apigee-api-proxies-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage revisions of API proxies
  name: Apigee API Proxy Revisions API
  phrasing_intents:
  - id: listApiProxyRevisions
    intent: List revisions of an API proxy
    question: What revision numbers exist for an API proxy?
  - id: getApiProxyRevision
    intent: Get one API proxy revision
    question: What configuration does a specific proxy revision contain?
  - id: deleteApiProxyRevision
    intent: Delete an API proxy revision
    question: Can I delete a proxy revision that is still deployed?
  phrasing_ops: 3
  slug: apigee-api-proxy-revisions-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage API specification documents
  name: Apigee API Specs API
  phrasing_intents:
  - id: listApiSpecs
    intent: List specs for a registry API version
    question: What spec files are attached to a version of an API in Apigee Registry?
  - id: createApiSpec
    intent: Add a spec to a registry API version
    question: How do I add an OpenAPI file to an API version in the registry?
  - id: getApiSpec
    intent: Get a registry spec's metadata
    question: What metadata does the registry hold for one spec, like its hash and revision?
  - id: updateApiSpec
    intent: Update a registry spec
    question: Will changing a registry spec's contents create a new revision?
  - id: deleteApiSpec
    intent: Delete a registry spec and its revisions
    question: Does deleting a registry spec remove all of its revisions too?
  - id: getApiSpecContents
    intent: Download a registry spec's raw contents
    question: How do I fetch the actual spec file content stored in the registry?
  - id: rollbackApiSpec
    intent: Roll a registry spec back to a revision
    question: How do I revert a registry spec to an earlier revision?
  phrasing_ops: 7
  slug: apigee-api-specs-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage API version records
  name: Apigee API Versions API
  phrasing_intents:
  - id: listApiVersions
    intent: List versions of a registry API
    question: What versions of an API are recorded in the Apigee Registry?
  - id: createApiVersion
    intent: Create a registry API version
    question: How do I add a new version to an API in the registry?
  - id: getApiVersion
    intent: Get a registry API version
    question: What details does the registry hold about one API version?
  - id: updateApiVersion
    intent: Update a registry API version
    question: How do I change the state of a registry API version?
  - id: deleteApiVersion
    intent: Delete a registry API version
    question: Does deleting a registry API version remove its specs too?
  phrasing_ops: 5
  slug: apigee-api-versions-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage developer groups and their applications
  name: Apigee App Groups API
  phrasing_intents:
  - id: listAppGroups
    intent: List app groups in an organization
    question: What app groups exist in my Apigee organization?
  - id: createAppGroup
    intent: Create an app group
    question: How do I group developers and their apps together in Apigee?
  - id: getAppGroup
    intent: Get an app group
    question: What are the details and status of one app group?
  - id: updateAppGroup
    intent: Update an app group
    question: Do I have to send the full app group object to update it?
  - id: deleteAppGroup
    intent: Delete an app group
    question: How do I remove an app group from my organization?
  phrasing_ops: 5
  slug: apigee-app-groups-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage metadata artifacts
  name: Apigee Artifacts API
  phrasing_intents:
  - id: listArtifacts
    intent: List registry artifacts in a location
    question: What artifacts are stored at the project level in Apigee Registry?
  - id: createArtifact
    intent: Create a registry artifact
    question: How do I store a new artifact in the registry at the project level?
  - id: getArtifact
    intent: Get a registry artifact's metadata
    question: What size and hash does a registry artifact have?
  - id: replaceArtifact
    intent: Replace a registry artifact's contents
    question: How do I overwrite the contents of an existing registry artifact?
  - id: deleteArtifact
    intent: Delete a registry artifact
    question: How do I remove an artifact from the registry?
  - id: getArtifactContents
    intent: Get a registry artifact's raw contents
    question: How do I download the raw data stored in a registry artifact?
  phrasing_ops: 6
  slug: apigee-artifacts-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage custom attributes
  name: Apigee Attributes API
  phrasing_intents:
  - id: listAttributes
    intent: List custom attributes in API Hub
    question: What custom attributes are defined in my API Hub?
  - id: createAttribute
    intent: Define a custom attribute in API Hub
    question: How do I add a custom metadata field to API Hub?
  phrasing_ops: 2
  slug: apigee-attributes-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage authentication configurations
  name: Apigee Auth Configs API
  phrasing_intents:
  - id: listAuthConfigs
    intent: List integration auth configs
    question: Which credentials have my integrations been set up to use?
  - id: createAuthConfig
    intent: Create an integration auth config
    question: How do I store an OAuth token or API key for an integration to use?
  - id: getAuthConfig
    intent: Get an integration auth config
    question: What credential type and state does one auth config have?
  - id: updateAuthConfig
    intent: Update an integration auth config
    question: How do I rotate the credentials in an existing auth config?
  - id: deleteAuthConfig
    intent: Delete an integration auth config
    question: Can I delete an auth config that an active integration version still uses?
  phrasing_ops: 5
  slug: apigee-auth-configs-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage SSL/TLS certificates
  name: Apigee Certificates API
  phrasing_intents:
  - id: listCertificates
    intent: List integration TLS certificates
    question: Which TLS certificates are available to my integrations?
  - id: createCertificate
    intent: Upload a certificate for integrations
    question: How do I add an SSL certificate for an integration that needs mutual TLS?
  - id: getCertificate
    intent: Get an integration certificate
    question: When does one of my integration certificates expire?
  - id: updateCertificate
    intent: Update an integration certificate
    question: How do I replace the certificate data on an existing integration certificate?
  - id: deleteCertificate
    intent: Delete an integration certificate
    question: Can I delete a certificate that an active integration version still references?
  phrasing_ops: 5
  slug: apigee-certificates-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Track API dependencies
  name: Apigee Dependencies API
  phrasing_intents:
  - id: listDependencies
    intent: List API dependencies in API Hub
    question: Which APIs depend on each other according to API Hub?
  - id: createDependency
    intent: Record a dependency between APIs
    question: How do I record that one API consumes another in API Hub?
  - id: getDependency
    intent: Get an API dependency
    question: What consumer and supplier does a recorded dependency link?
  - id: updateDependency
    intent: Update an API dependency
    question: Can I change the description of an existing API Hub dependency?
  - id: deleteDependency
    intent: Delete an API dependency
    question: How do I remove a dependency link between two APIs in API Hub?
  phrasing_ops: 5
  slug: apigee-dependencies-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage API deployments
  name: Apigee Deployments API
  phrasing_intents:
  - id: listDeployments
    intent: List API Hub deployment records
    question: Which API deployments are recorded in my API Hub for a region?
  - id: createDeployment
    intent: Record a new deployment in API Hub
    question: How do I track in API Hub where an API version is deployed?
  - id: getDeployment
    intent: Get an API Hub deployment record
    question: What details are stored for one deployment record in API Hub?
  - id: updateDeployment
    intent: Update an API Hub deployment record
    question: Can I change the endpoints listed on an existing API Hub deployment record?
  - id: deleteDeployment
    intent: Delete an API Hub deployment record
    question: How do I remove a stale deployment record from API Hub?
  - id: deployApiProxyRevision
    intent: Deploy an API proxy revision to an environment
    question: How do I deploy an API proxy revision so it starts accepting client requests?
  - id: undeployApiProxyRevision
    intent: Undeploy an API proxy revision
    question: How do I stop an API proxy revision from serving traffic in an environment?
  - id: listOrganizationDeployments
    intent: List proxy deployments across an organization
    question: Which API proxy revisions are deployed in which environments across my Apigee org?
  phrasing_ops: 8
  slug: apigee-deployments-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage API keys and credentials for developer apps
  name: Apigee Developer App Keys API
  phrasing_intents:
  - id: listDeveloperAppKeys
    intent: List a developer app's API keys
    question: What consumer keys and secrets does a developer app have?
  - id: createDeveloperAppKey
    intent: Add a custom consumer key to an app
    question: How do I migrate an existing consumer key and secret into Apigee?
  - id: getDeveloperAppKey
    intent: Get a developer app key
    question: Which API products is a particular consumer key approved for?
  - id: updateDeveloperAppKey
    intent: Add API products to an app key
    question: How do I give an existing app key access to another API product?
  - id: deleteDeveloperAppKey
    intent: Delete a developer app key
    question: Can a consumer key still call APIs after I delete it?
  phrasing_ops: 5
  slug: apigee-developer-app-keys-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage applications registered by developers
  name: Apigee Developer Apps API
  phrasing_intents:
  - id: listDeveloperApps
    intent: List a developer's apps
    question: What apps has a particular developer registered?
  - id: createDeveloperApp
    intent: Register an app for a developer
    question: How do I create an app for a developer so they get an API key?
  - id: getDeveloperApp
    intent: Get a developer app
    question: Which API keys and products are tied to a developer's app?
  - id: updateDeveloperApp
    intent: Update a developer app's attributes
    question: Does updating a developer app replace all of its attributes?
  - id: deleteDeveloperApp
    intent: Delete a developer app
    question: What happens to the app's API keys when I delete a developer app?
  phrasing_ops: 5
  slug: apigee-developer-apps-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage developer accounts and credentials
  name: Apigee Developers API
  phrasing_intents:
  - id: listDevelopers
    intent: List developers in an organization
    question: Which developers are registered in my Apigee organization?
  - id: createDeveloper
    intent: Register a developer
    question: How do I register a new API consumer in my organization?
  - id: getDeveloper
    intent: Get a developer's profile
    question: Can I look up a developer by email address?
  - id: updateDeveloper
    intent: Update a developer's profile
    question: Do I need to send the whole developer profile to change one field?
  - id: deleteDeveloper
    intent: Delete a developer
    question: What happens to a developer's apps and keys when I delete them?
  phrasing_ops: 5
  slug: apigee-developers-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage runtime execution environments
  name: Apigee Environments API
  phrasing_intents:
  - id: listEnvironments
    intent: List environments in an organization
    question: What environments exist in my Apigee organization?
  - id: createEnvironment
    intent: Create an environment
    question: How do I add a new runtime environment like test or prod?
  - id: getEnvironment
    intent: Get an environment's profile
    question: What properties and deployment type does an environment have?
  - id: updateEnvironment
    intent: Update an environment
    question: Must I send the full environment object to change its properties?
  - id: deleteEnvironment
    intent: Delete an environment
    question: Do I have to undeploy all proxies before deleting an environment?
  phrasing_ops: 5
  slug: apigee-environments-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: View integration execution results
  name: Apigee Executions API
  phrasing_intents:
  - id: listExecutions
    intent: List runs of an integration
    question: Which runs of my integration failed recently?
  - id: getExecution
    intent: Get an integration run's details
    question: What inputs and outputs did a specific integration run have?
  phrasing_ops: 2
  slug: apigee-executions-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage external API references
  name: Apigee External APIs API
  phrasing_intents:
  - id: listExternalApis
    intent: List external API references in API Hub
    question: Which third-party APIs are referenced in my API Hub?
  - id: createExternalApi
    intent: Add an external API reference to API Hub
    question: How do I record an API we consume but do not own in API Hub?
  phrasing_ops: 2
  slug: apigee-external-apis-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage Apigee runtime instances
  name: Apigee Instances API
  phrasing_intents:
  - id: listInstances
    intent: List Apigee runtime instances
    question: Which runtime instances does my Apigee organization have?
  - id: createInstance
    intent: Provision an Apigee runtime instance
    question: How do I provision runtime infrastructure for my Apigee organization?
  - id: getInstance
    intent: Get an Apigee runtime instance
    question: What host and port is my Apigee runtime instance listening on?
  - id: deleteInstance
    intent: Deprovision an Apigee runtime instance
    question: How do I tear down an Apigee runtime instance and its infrastructure?
  - id: postProjectsByProjectIdLocationsByLocationIdInstances
    intent: Provision an Apigee Registry instance
    question: How do I set up a Registry instance in a Google Cloud project?
  - id: getProjectsByProjectIdLocationsByLocationIdInstancesByInstanceId
    intent: Get an Apigee Registry instance
    question: What state is my Apigee Registry instance in?
  - id: deleteProjectsByProjectIdLocationsByLocationIdInstancesByInstanceId
    intent: Delete an Apigee Registry instance
    question: How do I remove the Registry instance from a project?
  phrasing_ops: 7
  slug: apigee-instances-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage integration versions and publishing
  name: Apigee Integration Versions API
  phrasing_intents:
  - id: listIntegrationVersions
    intent: List the versions of an integration
    question: What versions exist for one of my Apigee integrations?
  - id: createIntegrationVersion
    intent: Create a new integration version
    question: How do I save a new version of an integration with its triggers and tasks?
  - id: getIntegrationVersion
    intent: Get one integration version's configuration
    question: Where can I see the full trigger, task and parameter setup of a single integration version?
  - id: updateIntegrationVersion
    intent: Edit a draft integration version
    question: Is it possible to edit an integration version after it has been published?
  - id: deleteIntegrationVersion
    intent: Delete an integration version
    question: Can I delete an integration version that is currently published?
  - id: publishIntegrationVersion
    intent: Publish an integration version
    question: How do I make a draft integration version the active one that runs new executions?
  - id: unpublishIntegrationVersion
    intent: Unpublish an integration version
    question: How do I stop a published integration version from receiving executions?
  - id: downloadIntegrationVersion
    intent: Download an integration version bundle
    question: Can I export an integration version as a JSON file?
  phrasing_ops: 9
  slug: apigee-integration-versions-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage and execute integrations
  name: Apigee Integrations API
  phrasing_intents:
  - id: listIntegrations
    intent: List integrations for a product
    question: What integrations exist in my Apigee project and region?
  - id: deleteIntegration
    intent: Delete an integration
    question: Can I delete an integration that still has an active version?
  - id: executeIntegration
    intent: Run an integration and wait for the result
    question: How do I run an integration synchronously and get its output?
  - id: scheduleIntegration
    intent: Schedule an integration run for later
    question: Can I schedule an integration to run at a specific time?
  phrasing_ops: 4
  slug: apigee-integrations-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage key-value storage maps
  name: Apigee Key Value Maps API
  phrasing_intents:
  - id: listKeyValueMaps
    intent: List key value maps in an environment
    question: Which key value maps exist in an environment?
  - id: createKeyValueMap
    intent: Create a key value map
    question: How do I create a store of values policies can read at runtime?
  - id: deleteKeyValueMap
    intent: Delete a key value map
    question: How do I remove a key value map from an environment?
  phrasing_ops: 3
  slug: apigee-key-value-maps-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage project locations and search resources
  name: Apigee Locations API
  phrasing_intents:
  - id: searchResources
    intent: Search API Hub resources
    question: Can I full-text search across APIs, versions, specs and deployments in API Hub?
  phrasing_ops: 1
  slug: apigee-locations-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage API observation jobs for shadow API discovery
  name: Apigee Observation Jobs API
  phrasing_intents:
  - id: listObservationJobs
    intent: List shadow API observation jobs
    question: Which observation jobs are scanning traffic for shadow APIs in my project?
  - id: createObservationJob
    intent: Create a shadow API observation job
    question: How do I start discovering undocumented APIs from network traffic?
  - id: getObservationJob
    intent: Get an observation job's details
    question: What state is my shadow API observation job in?
  - id: deleteObservationJob
    intent: Delete an observation job
    question: Do I need to disable an observation job before deleting it?
  - id: enableObservationJob
    intent: Enable an observation job
    question: How do I resume shadow API discovery on a disabled job?
  - id: disableObservationJob
    intent: Disable an observation job
    question: How do I pause traffic analysis on an active observation job?
  phrasing_ops: 6
  slug: apigee-observation-jobs-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage sources for API observation
  name: Apigee Observation Sources API
  phrasing_intents:
  - id: listObservationSources
    intent: List traffic observation sources
    question: Which network infrastructure am I monitoring for API traffic?
  - id: createObservationSource
    intent: Create a traffic observation source
    question: How do I tell Apigee which load balancer traffic to watch for shadow APIs?
  - id: getObservationSource
    intent: Get an observation source
    question: What infrastructure does a specific observation source monitor?
  - id: deleteObservationSource
    intent: Delete an observation source
    question: Can I delete an observation source that an active job still uses?
  phrasing_ops: 4
  slug: apigee-observation-sources-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage long-running operations
  name: Apigee Operations API
  phrasing_intents:
  - id: listOperations
    intent: List long-running operations
    question: What long-running operations are in progress in my project?
  - id: getOperation
    intent: Check a long-running operation's status
    question: Has my long-running operation finished yet?
  - id: cancelOperation
    intent: Cancel a long-running operation
    question: Can I stop a long-running operation that is still running?
  phrasing_ops: 3
  slug: apigee-operations-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage Apigee organizations and their configuration
  name: Apigee Organizations API
  phrasing_intents:
  - id: listOrganizations
    intent: List my Apigee organizations
    question: Which Apigee organizations can I access?
  - id: createOrganization
    intent: Create an Apigee organization
    question: How do I set up a new Apigee organization for a Google Cloud project?
  - id: getOrganization
    intent: Get an organization's properties
    question: What subscription type and runtime does my organization use?
  - id: updateOrganization
    intent: Update an organization's properties
    question: Can I change the display name or description of my Apigee org?
  - id: deleteOrganization
    intent: Delete an Apigee organization
    question: What gets removed when I delete an Apigee organization?
  phrasing_ops: 5
  slug: apigee-organizations-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: The Projects API from Apigee — 2 operation(s) for projects.
  name: Apigee Projects API
  phrasing_intents:
  - id: listApis
    intent: List APIs in API Hub
    question: What APIs are cataloged in API Hub for my project?
  - id: createApi
    intent: Register an API in API Hub
    question: How do I add a new API to the API Hub catalog?
  - id: getApi
    intent: Get an API from API Hub
    question: Who owns a particular API in API Hub?
  - id: updateApi
    intent: Update an API in API Hub
    question: Can I change only the owner of an API in API Hub?
  - id: deleteApi
    intent: Delete an API from API Hub
    question: Does deleting an API from API Hub also delete its versions and specs?
  phrasing_ops: 5
  slug: apigee-projects-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage runtime project attachments
  name: Apigee Runtime Project Attachments API
  phrasing_intents:
  - id: listRuntimeProjectAttachments
    intent: List runtime projects attached to API Hub
    question: Which Google Cloud projects are attached to my API Hub for discovery?
  - id: createRuntimeProjectAttachment
    intent: Attach a runtime project to API Hub
    question: How do I link another Google Cloud project to API Hub for API discovery?
  phrasing_ops: 2
  slug: apigee-runtime-project-attachments-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage Salesforce channels
  name: Apigee SFDC Channels API
  phrasing_intents:
  - id: listSfdcChannels
    intent: List Salesforce channels on an instance
    question: Which Salesforce channels are set up on an SFDC instance?
  - id: createSfdcChannel
    intent: Create a Salesforce channel
    question: How do I subscribe an integration to a Salesforce event topic?
  phrasing_ops: 2
  slug: apigee-sfdc-channels-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage Salesforce instances
  name: Apigee SFDC Instances API
  phrasing_intents:
  - id: listSfdcInstances
    intent: List Salesforce instances for integrations
    question: Which Salesforce orgs are connected to my integrations?
  - id: createSfdcInstance
    intent: Connect a Salesforce instance
    question: How do I connect a Salesforce org to my integrations?
  - id: getSfdcInstance
    intent: Get a Salesforce instance configuration
    question: Which Salesforce org ID does an SFDC instance point to?
  - id: updateSfdcInstance
    intent: Update a Salesforce instance configuration
    question: Can I switch a Salesforce instance to a different auth config?
  - id: deleteSfdcInstance
    intent: Delete a Salesforce instance configuration
    question: How do I disconnect a Salesforce org from integrations?
  phrasing_ops: 5
  slug: apigee-sfdc-instances-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage reusable shared flow logic
  name: Apigee Shared Flows API
  phrasing_intents:
  - id: listSharedFlows
    intent: List shared flows in an organization
    question: What reusable shared flows exist in my organization?
  - id: createSharedFlow
    intent: Import a shared flow bundle
    question: How do I upload a ZIP bundle as a new shared flow?
  - id: getSharedFlow
    intent: Get a shared flow and its revisions
    question: Which revisions exist for a shared flow?
  - id: deleteSharedFlow
    intent: Delete a shared flow
    question: Must a shared flow be undeployed before it can be deleted?
  phrasing_ops: 4
  slug: apigee-shared-flows-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage API specifications
  name: Apigee Specs API
  phrasing_intents:
  - id: listApiSpecs
    intent: List specs for an API Hub version
    question: What OpenAPI or Protocol Buffer specs are attached to an API version in API Hub?
  - id: createApiSpec
    intent: Add a spec to an API Hub version
    question: How do I attach an OpenAPI document to an API version in API Hub?
  - id: getApiSpec
    intent: Get an API Hub spec's metadata
    question: What spec type and parsing mode does an API Hub spec use?
  - id: updateApiSpec
    intent: Update an API Hub spec
    question: How do I replace the contents of a spec already in API Hub?
  - id: deleteApiSpec
    intent: Delete a spec from API Hub
    question: Is there a way to drop an outdated spec from an API version in API Hub?
  - id: getApiSpecContents
    intent: Get the raw contents of an API Hub spec
    question: How do I download the actual OpenAPI or proto file behind an API Hub spec?
  - id: lintApiSpec
    intent: Lint an API Hub spec
    question: Can API Hub check my spec against style and correctness rules?
  phrasing_ops: 7
  slug: apigee-specs-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage integration execution suspensions
  name: Apigee Suspensions API
  phrasing_intents:
  - id: listSuspensions
    intent: List suspensions on an integration execution
    question: Which steps of an integration run are paused waiting for approval?
  - id: liftSuspension
    intent: Lift a suspension and resume the execution
    question: How do I let a paused integration run continue?
  - id: resolveSuspension
    intent: Resolve a suspension with a final decision
    question: How do I record an approval decision on a suspended task?
  phrasing_ops: 3
  slug: apigee-suspensions-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Configure backend target server endpoints
  name: Apigee Target Servers API
  phrasing_intents:
  - id: listTargetServers
    intent: List target servers in an environment
    question: Which backend target servers are defined in an environment?
  - id: createTargetServer
    intent: Create a target server
    question: How do I define a backend host and port that proxies can reference by name?
  - id: getTargetServer
    intent: Get a target server
    question: What host and port is a target server configured with?
  - id: updateTargetServer
    intent: Update a target server
    question: How do I point an existing target server at a new backend host?
  - id: deleteTargetServer
    intent: Delete a target server
    question: How do I remove a backend target server from an environment?
  phrasing_ops: 5
  slug: apigee-target-servers-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: Manage API versions
  name: Apigee Versions API
  phrasing_intents:
  - id: listApiVersions
    intent: List versions of an API in API Hub
    question: What releases of an API are recorded in API Hub?
  - id: createApiVersion
    intent: Create an API version in API Hub
    question: How do I add a new release of an API to API Hub?
  - id: getApiVersion
    intent: Get an API version from API Hub
    question: What lifecycle state and compliance status does an API Hub version have?
  - id: updateApiVersion
    intent: Update an API version in API Hub
    question: Can I change the lifecycle stage of an API Hub version?
  - id: deleteApiVersion
    intent: Delete an API version from API Hub
    question: Does deleting an API Hub version also remove its specs and operations?
  phrasing_ops: 5
  slug: apigee-versions-api
- description: Apigee is Google Cloud's API management platform enabling organizations to design, secure, publish, analyze, and scale their APIs with advanced analytics, developer portal, and monetization features.
  name: Google Apigee
  slug: google-apigee
- description: The Apigee Connect API enables Apigee hybrid to connect the Apigee management plane to the customer-managed runtime plane without requiring the runtime plane to have an inbound firewall rule. It allow
  name: Google Apigee Connect API
  slug: google-apigee-connect-api
- description: Apigee API Hub is a centralized repository and governance platform for discovering, managing, and analyzing APIs across an organization. It enables teams to register APIs, manage API versions and spec
  name: Google Apigee API Hub
  slug: google-apigee-api-hub
- description: The Apigee Analytics API provides access to API usage metrics, traffic data, error rates, latency statistics, and custom reports generated by the Apigee analytics engine. It allows developers and oper
  name: Google Apigee Analytics API
  slug: google-apigee-analytics-api
- baseURL: https://apigee.googleapis.com
  baseurl_source: declared
  description: The Organizations API from Google Apigee — 9 operation(s) for organizations.
  name: Google Apigee Organizations API
  phrasing_intents:
  - id: listOrganizations
    intent: List my Apigee organizations
    question: Which Apigee organizations can I access?
  - id: createOrganization
    intent: Create an Apigee organization
    question: How do I set up a new Apigee organization for a Google Cloud project?
  - id: getOrganization
    intent: Get an organization's properties
    question: What subscription type and runtime does my organization use?
  - id: updateOrganization
    intent: Update an organization's properties
    question: Can I change the display name or description of my Apigee org?
  - id: deleteOrganization
    intent: Delete an Apigee organization
    question: What gets removed when I delete an Apigee organization?
  phrasing_ops: 5
  slug: google-apigee-organizations-api
arazzos:
- description: Create an analytics datastore for export, then query environment statistics for a dimension.
  name: Apigee Set Up Analytics Export and Read Stats
  slug: apigee-analytics-datastore-setup-workflow
- description: Create an app group, add a developer, register an app, and read the app back.
  name: Apigee Onboard an App Group
  slug: apigee-app-group-onboarding-workflow
- description: Register an API in API Hub, add a version and spec, trigger a lint, then read the lint outcome.
  name: Apigee API Hub Catalog and Lint
  slug: apigee-catalog-api-hub-workflow
- description: Undeploy a proxy revision from an environment, delete that revision, then delete the proxy.
  name: Apigee Decommission an API Proxy
  slug: apigee-decommission-proxy-workflow
- description: Run a full-text search across API Hub, then read a matching API and list its versions.
  name: Apigee API Hub Discover and Search
  slug: apigee-discover-and-search-hub-workflow
- description: List deployments, undeploy a proxy revision from the environment, then delete the environment.
  name: Apigee Tear Down an Environment
  slug: apigee-environment-teardown-workflow
- description: Create a new API product, confirm the target app and its key, then bind the product to the key.
  name: Apigee Grant an App Access to a New Product
  slug: apigee-grant-app-product-access-workflow
- description: Create an auth config, list auth configs to confirm it, then author an integration version.
  name: Apigee Integration Auth Setup
  slug: apigee-integration-auth-setup-workflow
- description: Execute an integration, list its recent executions, then read the execution detail.
  name: Apigee Integration Execution Monitor
  slug: apigee-integration-execution-monitor-workflow
- description: Create an integration version, publish it, then execute it synchronously and read the result.
  name: Apigee Publish and Execute an Integration
  slug: apigee-integration-publish-and-execute-workflow
- description: Create an API product, register a developer, create their app, and read the issued API keys.
  name: Apigee Onboard a Developer App
  slug: apigee-onboard-developer-app-workflow
- description: List a proxy's revisions, deploy the newest one with override, then undeploy the prior revision.
  name: Apigee Promote a New Proxy Revision
  slug: apigee-promote-proxy-revision-workflow
- description: Create an environment, poll until it is active, then add a target server and a key value map.
  name: Apigee Provision an Environment
  slug: apigee-provision-environment-workflow
- description: Create an Apigee runtime instance, poll until it is active, then create an environment on it.
  name: Apigee Provision a Runtime Instance
  slug: apigee-provision-runtime-instance-workflow
- description: Import an API proxy bundle, find its newest revision, deploy it, and confirm the deployment.
  name: Apigee Import and Deploy an API Proxy
  slug: apigee-proxy-import-and-deploy-workflow
- description: Import a proxy, deploy its revision, then bundle it into an API product ready for consumption.
  name: Apigee Publish an API Proxy as a Product
  slug: apigee-publish-api-product-workflow
- description: Record a deployment in API Hub, declare a dependency between two APIs, then read it back.
  name: Apigee API Hub Deployment and Dependency
  slug: apigee-register-deployment-dependency-workflow
- description: Register an external API reference, define a custom attribute, then list external APIs.
  name: Apigee API Hub Register External API
  slug: apigee-register-external-api-workflow
- description: Register an API in the Registry, add a version and a spec, then record a deployment.
  name: Apigee Registry Catalog an API Version
  slug: apigee-registry-catalog-version-workflow
- description: Read a spec's current revision, push a new revision via update, then roll back to the original.
  name: Apigee Registry Spec Revision Rollback
  slug: apigee-registry-spec-rollback-workflow
- description: Issue a fresh consumer key for an app, grant it product access, then revoke the old key.
  name: Apigee Rotate a Developer App Key
  slug: apigee-rotate-app-key-workflow
- description: Create an observation source, wait for it, start an observation job, wait again, then enable it.
  name: Apigee Shadow API Discovery
  slug: apigee-shadow-api-discovery-workflow
- description: Import a shared flow bundle, read it back for its revisions, and list shared flow deployments.
  name: Apigee Catalog a Shared Flow
  slug: apigee-shared-flow-catalog-workflow
- description: Create a backend target server, read it back, then update its host and port.
  name: Apigee Roll Out a Target Server Change
  slug: apigee-target-server-rollout-workflow
- description: Read an API product, then update its quota limits while preserving its existing bindings.
  name: Apigee Update an API Product Quota
  slug: apigee-update-product-quota-workflow
artifact_total: 260
collections:
- collection_type: postman
  name: Apigee API Hub API
  slug: postman-apigee-api-hub
- collection_type: postman
  name: Apigee API Management
  slug: postman-apigee-api-management
- collection_type: postman
  name: Apigee API Management API
  slug: postman-apigee-apim
- collection_type: postman
  name: Apigee Integrations API
  slug: postman-apigee-integrations
- collection_type: postman
  name: Apigee Registry API
  slug: postman-apigee-registry
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apigee API Hub Analytics API
  slug: open-apigee-analytics-api
- collection_type: open
  name: Apigee API Hub Analytics API Deployments API
  slug: open-apigee-api-deployments-api
- collection_type: open
  name: Apigee API Hub API
  slug: open-apigee-api-hub
- collection_type: open
  name: Apigee API Management
  slug: open-apigee-api-management
- collection_type: open
  name: Apigee API Hub Analytics API Observations API
  slug: open-apigee-api-observations-api
- collection_type: open
  name: Apigee API Hub Analytics API Operations API
  slug: open-apigee-api-operations-api
- collection_type: open
  name: Apigee API Hub Analytics API Products API
  slug: open-apigee-api-products-api
- collection_type: open
  name: Apigee API Hub Analytics API Proxies API
  slug: open-apigee-api-proxies-api
- collection_type: open
  name: Apigee API Hub Analytics API Proxy Revisions API
  slug: open-apigee-api-proxy-revisions-api
- collection_type: open
  name: Apigee API Hub Analytics API Specs API
  slug: open-apigee-api-specs-api
- collection_type: open
  name: Apigee API Hub Analytics API Versions API
  slug: open-apigee-api-versions-api
- collection_type: open
  name: Apigee API Management API
  slug: open-apigee-apim
- collection_type: open
  name: Apigee API Hub Analytics App Groups API
  slug: open-apigee-app-groups-api
- collection_type: open
  name: Apigee API Hub Analytics Artifacts API
  slug: open-apigee-artifacts-api
- collection_type: open
  name: Apigee API Hub Analytics Attributes API
  slug: open-apigee-attributes-api
- collection_type: open
  name: Apigee API Hub Analytics Auth Configs API
  slug: open-apigee-auth-configs-api
- collection_type: open
  name: Apigee API Hub Analytics Certificates API
  slug: open-apigee-certificates-api
- collection_type: open
  name: Apigee API Hub Analytics Dependencies API
  slug: open-apigee-dependencies-api
- collection_type: open
  name: Apigee API Hub Analytics Deployments API
  slug: open-apigee-deployments-api
- collection_type: open
  name: Apigee API Hub Analytics Developer App Keys API
  slug: open-apigee-developer-app-keys-api
- collection_type: open
  name: Apigee API Hub Analytics Developer Apps API
  slug: open-apigee-developer-apps-api
- collection_type: open
  name: Apigee API Hub Analytics Developers API
  slug: open-apigee-developers-api
- collection_type: open
  name: Apigee API Hub Analytics Environments API
  slug: open-apigee-environments-api
- collection_type: open
  name: Apigee API Hub Analytics Executions API
  slug: open-apigee-executions-api
- collection_type: open
  name: Apigee API Hub Analytics External APIs API
  slug: open-apigee-external-apis-api
- collection_type: open
  name: Apigee API Hub Analytics Instances API
  slug: open-apigee-instances-api
- collection_type: open
  name: Apigee API Hub Analytics Integration Versions API
  slug: open-apigee-integration-versions-api
- collection_type: open
  name: Apigee API Hub Analytics Integrations API
  slug: open-apigee-integrations-api
- collection_type: open
  name: Apigee Integrations API
  slug: open-apigee-integrations
- collection_type: open
  name: Apigee API Hub Analytics Key Value Maps API
  slug: open-apigee-key-value-maps-api
- collection_type: open
  name: Apigee API Hub Analytics Locations API
  slug: open-apigee-locations-api
- collection_type: open
  name: Apigee API Hub Analytics Observation Jobs API
  slug: open-apigee-observation-jobs-api
- collection_type: open
  name: Apigee API Hub Analytics Observation Sources API
  slug: open-apigee-observation-sources-api
- collection_type: open
  name: Apigee API Hub Analytics Operations API
  slug: open-apigee-operations-api
- collection_type: open
  name: Apigee API Hub Analytics Organizations API
  slug: open-apigee-organizations-api
- collection_type: open
  name: Apigee API Hub Analytics Projects API
  slug: open-apigee-projects-api
- collection_type: open
  name: Apigee Registry API
  slug: open-apigee-registry
- collection_type: open
  name: Apigee API Hub Analytics Runtime Project Attachments API
  slug: open-apigee-runtime-project-attachments-api
- collection_type: open
  name: Apigee API Hub Analytics SFDC Channels API
  slug: open-apigee-sfdc-channels-api
- collection_type: open
  name: Apigee API Hub Analytics SFDC Instances API
  slug: open-apigee-sfdc-instances-api
- collection_type: open
  name: Apigee API Hub Analytics Shared Flows API
  slug: open-apigee-shared-flows-api
- collection_type: open
  name: Apigee API Hub Analytics Specs API
  slug: open-apigee-specs-api
- collection_type: open
  name: Apigee API Hub Analytics Suspensions API
  slug: open-apigee-suspensions-api
- collection_type: open
  name: Apigee API Hub Analytics Target Servers API
  slug: open-apigee-target-servers-api
- collection_type: open
  name: Apigee API Hub Analytics Versions API
  slug: open-apigee-versions-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/vendor-facets/apigee-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/apigee-vendor-facets.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/rate-limits/apigee-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apigee-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/plans/apigee-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apigee-plans-pricing.yml
- group: start
  title: ''
  type: Console
  url: https://console.cloud.google.com/apigee
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/apigee
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@googlecloudtech
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/capabilities/apigee-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/apigee-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apigee/apigeecli/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apigee/apigeecli/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apigee/apigeecli/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apigee/apigeecli/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: TrustCenter
  url: https://cloud.google.com/trust-center
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/sdk
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/agentic-access/apigee-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apigee-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/security/apigee-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/apigee-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/security/apigee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apigee-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/authentication/apigee-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apigee-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/scopes/apigee-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/apigee-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apigee/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-analytics-datastore-setup-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-analytics-datastore-setup-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-app-group-onboarding-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-app-group-onboarding-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-catalog-api-hub-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-catalog-api-hub-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-decommission-proxy-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-decommission-proxy-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-discover-and-search-hub-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-discover-and-search-hub-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-environment-teardown-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-environment-teardown-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-grant-app-product-access-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-grant-app-product-access-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-integration-auth-setup-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-integration-auth-setup-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-integration-execution-monitor-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-integration-execution-monitor-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-integration-publish-and-execute-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-integration-publish-and-execute-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-onboard-developer-app-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-onboard-developer-app-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-promote-proxy-revision-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-promote-proxy-revision-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-provision-environment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-provision-environment-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-provision-runtime-instance-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-provision-runtime-instance-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-proxy-import-and-deploy-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-proxy-import-and-deploy-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-publish-api-product-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-publish-api-product-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-register-deployment-dependency-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-register-deployment-dependency-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-register-external-api-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-register-external-api-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-registry-catalog-version-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-registry-catalog-version-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-registry-spec-rollback-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-registry-spec-rollback-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-rotate-app-key-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-rotate-app-key-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-shadow-api-discovery-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-shadow-api-discovery-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-shared-flow-catalog-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-shared-flow-catalog-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-target-server-rollout-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-target-server-rollout-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/arazzo/apigee-update-product-quota-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/apigee-update-product-quota-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apigee-legacy
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/apigee
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/apigee/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/apigee/docs/api-platform/get-started/overview
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-home
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/api-management
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/apigee/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cloud.google.com/terms/cloud-privacy-notice
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apigee
- group: operate
  title: ''
  type: Community
  url: https://www.googlecloudcommunity.com/gc/Apigee/bd-p/cloud-apigee
- group: company
  title: ''
  type: Website
  url: https://cloud.google.com/apigee
- group: start
  title: ''
  type: Login
  url: https://console.cloud.google.com/
- group: start
  title: ''
  type: Signup
  url: https://cloud.google.com/apigee
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/apigee/pricing
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://cloud.google.com/apigee/docs/release-notes
- group: operate
  title: ''
  type: ChangeLog
  url: https://cloud.google.com/apigee/docs/release/release-notes
- group: build
  title: ''
  type: SDKs
  url: https://cloud.google.com/apigee/docs/apihub/libraries
- group: learn
  title: ''
  type: Tutorials
  url: https://cloud.google.com/apigee/docs/api-platform/get-started/tutorials
- group: learn
  title: ''
  type: Learning Resources
  url: https://cloud.google.com/apigee/docs/api-platform/get-started/learning-path
- group: learn
  title: ''
  type: Coursera
  url: https://www.coursera.org/specializations/apigee-api-gcp
- group: auth
  title: ''
  type: Security
  url: https://cloud.google.com/architecture/best-practices-securing-applications-and-apis-using-apigee
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.google.com/apigee/docs/api-platform/publish/intro-portals
- group: other
  title: ''
  type: API Products
  url: https://cloud.google.com/apigee/docs/api-platform/publish/what-api-product
- group: other
  title: ''
  type: Analytics
  url: https://cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview
- group: other
  title: ''
  type: Monetization
  url: https://cloud.google.com/apigee/docs/api-platform/monetization/overview
- group: other
  title: ''
  type: Hybrid
  url: https://cloud.google.com/apigee/docs/hybrid/v1.9/what-is-hybrid
- group: other
  title: ''
  type: Envoy Adapter
  url: https://cloud.google.com/apigee/docs/api-platform/envoy-adapter/v2.0.x/operation
- group: auth
  title: ''
  type: Advanced API Security
  url: https://cloud.google.com/apigee/docs/api-security
- group: other
  title: ''
  type: ModelContextProtocol
  url: https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview
- group: agent
  title: ''
  type: AgenticAI
  url: https://cloud.google.com/blog/products/api-management/turn-your-api-sprawl-into-an-agent-ready-catalog
- group: docs
  title: ''
  type: SpecificationBoost
  url: https://cloud.google.com/apigee/docs/apihub/spec-boost
- group: build
  title: ''
  type: CLI
  url: https://github.com/apigee/apigeecli
- group: other
  title: ''
  type: AnalystReport
  url: https://cloud.google.com/blog/products/api-management/apigee-named-leader-in-gartner-magic-quadrant-for-api-management
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apigee/api-platform-samples
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apigee/apigeecli
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apigee/apigeelint
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apigee/devrel
- group: agent
  title: ''
  type: LlmsText
  url: https://apigee.com/llms.txt
created: '2024-01-01'
description: Apigee is Google Cloud's native API management platform for building, managing, and securing APIs across any use case, environment, or scale. It provides API proxies, security, rate limiting, quotas, analytics, monetization, and developer portal capabilities.
examples:
- key_count: 5
  name: Apigee Api Product Example
  slug: apigee-api-product-example
- key_count: 3
  name: Apigee Api Proxy Example
  slug: apigee-api-proxy-example
- key_count: 4
  name: Apigee Deployment Example
  slug: apigee-deployment-example
- key_count: 4
  name: Apigee Developer App Example
  slug: apigee-developer-app-example
- key_count: 4
  name: Apigee Developer Example
  slug: apigee-developer-example
- key_count: 3
  name: Apigee Environment Example
  slug: apigee-environment-example
- key_count: 3
  name: Apigee Integration Example
  slug: apigee-integration-example
- key_count: 4
  name: Apigee Organization Example
  slug: apigee-organization-example
finops:
- name: Apigee Finops
  service_category: API Management / Gateways
  slug: apigee-finops
image: https://www.apigee.com/about/sites/default/files/apigee-logo.png
json_schemas:
- name: AllowedValue
  property_count: 4
  slug: apigee-allowedvalue
- name: Apigee API Product
  property_count: 14
  slug: apigee-api-product
- name: Apigee API Proxy
  property_count: 7
  slug: apigee-api-proxy
- name: Api
  property_count: 15
  slug: apigee-api
- name: ApiDeployment
  property_count: 15
  slug: apigee-apideployment
- name: ApiObservation
  property_count: 12
  slug: apigee-apiobservation
- name: ApiOperation
  property_count: 5
  slug: apigee-apioperation
- name: ApiProduct
  property_count: 14
  slug: apigee-apiproduct
- name: ApiProxy
  property_count: 7
  slug: apigee-apiproxy
- name: ApiProxyRevision
  property_count: 13
  slug: apigee-apiproxyrevision
- name: ApiSpec
  property_count: 12
  slug: apigee-apispec
- name: ApiVersion
  property_count: 14
  slug: apigee-apiversion
- name: AppGroup
  property_count: 9
  slug: apigee-appgroup
- name: Artifact
  property_count: 7
  slug: apigee-artifact
- name: Attribute
  property_count: 11
  slug: apigee-attribute
- name: AttributeValues
  property_count: 4
  slug: apigee-attributevalues
- name: AuthConfig
  property_count: 11
  slug: apigee-authconfig
- name: BatchEditTagsRequest
  property_count: 1
  slug: apigee-batchedittagsrequest
- name: BatchEditTagsResponse
  property_count: 1
  slug: apigee-batchedittagsresponse
- name: Certificate
  property_count: 7
  slug: apigee-certificate
- name: Datastore
  property_count: 7
  slug: apigee-datastore
- name: Dependency
  property_count: 8
  slug: apigee-dependency
- name: DependencyEntityReference
  property_count: 3
  slug: apigee-dependencyentityreference
- name: Apigee Deployment
  property_count: 7
  slug: apigee-deployment
- name: Apigee Developer App
  property_count: 11
  slug: apigee-developer-app
- name: Apigee Developer
  property_count: 13
  slug: apigee-developer
- name: DeveloperApp
  property_count: 11
  slug: apigee-developerapp
- name: DeveloperAppKey
  property_count: 8
  slug: apigee-developerappkey
- name: Documentation
  property_count: 1
  slug: apigee-documentation
- name: DownloadIntegrationVersionResponse
  property_count: 1
  slug: apigee-downloadintegrationversionresponse
- name: EntityMetadata
  property_count: 3
  slug: apigee-entitymetadata
- name: EnumAttributeValue
  property_count: 2
  slug: apigee-enumattributevalue
- name: Apigee Environment
  property_count: 12
  slug: apigee-environment
- name: Error
  property_count: 1
  slug: apigee-error
- name: EventParameter
  property_count: 2
  slug: apigee-eventparameter
- name: ExecuteIntegrationRequest
  property_count: 5
  slug: apigee-executeintegrationrequest
- name: ExecuteIntegrationResponse
  property_count: 3
  slug: apigee-executeintegrationresponse
- name: Execution
  property_count: 9
  slug: apigee-execution
- name: ExternalApi
  property_count: 9
  slug: apigee-externalapi
- name: HttpBody
  property_count: 3
  slug: apigee-httpbody
- name: Instance
  property_count: 12
  slug: apigee-instance
- name: Apigee Integration Version
  property_count: 12
  slug: apigee-integration
- name: IntegrationParameter
  property_count: 6
  slug: apigee-integrationparameter
- name: IntegrationVersion
  property_count: 12
  slug: apigee-integrationversion
- name: KeyValueMap
  property_count: 2
  slug: apigee-keyvaluemap
- name: LiftSuspensionRequest
  property_count: 1
  slug: apigee-liftsuspensionrequest
- name: LiftSuspensionResponse
  property_count: 1
  slug: apigee-liftsuspensionresponse
- name: LintResponse
  property_count: 4
  slug: apigee-lintresponse
- name: ListApiDeploymentsResponse
  property_count: 2
  slug: apigee-listapideploymentsresponse
- name: ListApiObservationsResponse
  property_count: 2
  slug: apigee-listapiobservationsresponse
- name: ListApiOperationsResponse
  property_count: 2
  slug: apigee-listapioperationsresponse
- name: ListApiProductsResponse
  property_count: 1
  slug: apigee-listapiproductsresponse
- name: ListApiProxiesResponse
  property_count: 1
  slug: apigee-listapiproxiesresponse
- name: ListApiSpecsResponse
  property_count: 3
  slug: apigee-listapispecsresponse
- name: ListApisResponse
  property_count: 3
  slug: apigee-listapisresponse
- name: ListApiVersionsResponse
  property_count: 3
  slug: apigee-listapiversionsresponse
- name: ListAppGroupsResponse
  property_count: 3
  slug: apigee-listappgroupsresponse
- name: ListArtifactsResponse
  property_count: 2
  slug: apigee-listartifactsresponse
- name: ListAttributesResponse
  property_count: 3
  slug: apigee-listattributesresponse
- name: ListAuthConfigsResponse
  property_count: 2
  slug: apigee-listauthconfigsresponse
- name: ListCertificatesResponse
  property_count: 2
  slug: apigee-listcertificatesresponse
- name: ListDatastoresResponse
  property_count: 1
  slug: apigee-listdatastoresresponse
- name: ListDependenciesResponse
  property_count: 3
  slug: apigee-listdependenciesresponse
- name: ListDeploymentsResponse
  property_count: 3
  slug: apigee-listdeploymentsresponse
- name: ListDeveloperAppKeysResponse
  property_count: 1
  slug: apigee-listdeveloperappkeysresponse
- name: ListDeveloperAppsResponse
  property_count: 1
  slug: apigee-listdeveloperappsresponse
- name: ListDevelopersResponse
  property_count: 1
  slug: apigee-listdevelopersresponse
- name: ListExecutionsResponse
  property_count: 3
  slug: apigee-listexecutionsresponse
- name: ListExternalApisResponse
  property_count: 3
  slug: apigee-listexternalapisresponse
- name: ListInstancesResponse
  property_count: 2
  slug: apigee-listinstancesresponse
- name: ListIntegrationsResponse
  property_count: 2
  slug: apigee-listintegrationsresponse
- name: ListIntegrationVersionsResponse
  property_count: 3
  slug: apigee-listintegrationversionsresponse
- name: ListObservationJobsResponse
  property_count: 3
  slug: apigee-listobservationjobsresponse
- name: ListObservationSourcesResponse
  property_count: 3
  slug: apigee-listobservationsourcesresponse
- name: ListOperationsResponse
  property_count: 2
  slug: apigee-listoperationsresponse
- name: ListOrganizationsResponse
  property_count: 1
  slug: apigee-listorganizationsresponse
- name: ListRuntimeProjectAttachmentsResponse
  property_count: 3
  slug: apigee-listruntimeprojectattachmentsresponse
- name: ListSfdcChannelsResponse
  property_count: 2
  slug: apigee-listsfdcchannelsresponse
- name: ListSfdcInstancesResponse
  property_count: 2
  slug: apigee-listsfdcinstancesresponse
- name: ListSharedFlowsResponse
  property_count: 1
  slug: apigee-listsharedflowsresponse
- name: ListSuspensionsResponse
  property_count: 2
  slug: apigee-listsuspensionsresponse
- name: NodeConfig
  property_count: 3
  slug: apigee-nodeconfig
- name: ObservationJob
  property_count: 5
  slug: apigee-observationjob
- name: ObservationSource
  property_count: 5
  slug: apigee-observationsource
- name: Operation
  property_count: 5
  slug: apigee-operation
- name: OperationConfig
  property_count: 4
  slug: apigee-operationconfig
- name: OperationGroup
  property_count: 2
  slug: apigee-operationgroup
- name: Apigee Organization
  property_count: 14
  slug: apigee-organization
- name: Owner
  property_count: 2
  slug: apigee-owner
- name: PodStatus
  property_count: 9
  slug: apigee-podstatus
- name: Properties
  property_count: 1
  slug: apigee-properties
- name: ResolveSuspensionRequest
  property_count: 1
  slug: apigee-resolvesuspensionrequest
- name: ResolveSuspensionResponse
  property_count: 0
  slug: apigee-resolvesuspensionresponse
- name: RuntimeProjectAttachment
  property_count: 3
  slug: apigee-runtimeprojectattachment
- name: ScheduleIntegrationRequest
  property_count: 5
  slug: apigee-scheduleintegrationrequest
- name: ScheduleIntegrationResponse
  property_count: 1
  slug: apigee-scheduleintegrationresponse
- name: SearchResourcesResponse
  property_count: 2
  slug: apigee-searchresourcesresponse
- name: SfdcChannel
  property_count: 9
  slug: apigee-sfdcchannel
- name: SfdcInstance
  property_count: 9
  slug: apigee-sfdcinstance
- name: SharedFlow
  property_count: 4
  slug: apigee-sharedflow
- name: SharedFlowRevision
  property_count: 9
  slug: apigee-sharedflowrevision
- name: Stats
  property_count: 2
  slug: apigee-stats
- name: Status
  property_count: 3
  slug: apigee-status
- name: TargetServer
  property_count: 7
  slug: apigee-targetserver
- name: TaskConfig
  property_count: 7
  slug: apigee-taskconfig
- name: TlsInfo
  property_count: 8
  slug: apigee-tlsinfo
- name: TriggerConfig
  property_count: 8
  slug: apigee-triggerconfig
- name: UploadIntegrationVersionRequest
  property_count: 2
  slug: apigee-uploadintegrationversionrequest
- name: UploadIntegrationVersionResponse
  property_count: 1
  slug: apigee-uploadintegrationversionresponse
- name: ValueType
  property_count: 6
  slug: apigee-valuetype
json_structures:
- name: Apigee Api Product Structure
  property_count: 14
  slug: apigee-api-product-structure
- name: Apigee Api Proxy Structure
  property_count: 7
  slug: apigee-api-proxy-structure
- name: Apigee Deployment Structure
  property_count: 7
  slug: apigee-deployment-structure
- name: Apigee Developer App Structure
  property_count: 11
  slug: apigee-developer-app-structure
- name: Apigee Developer Structure
  property_count: 13
  slug: apigee-developer-structure
- name: Apigee Environment Structure
  property_count: 12
  slug: apigee-environment-structure
- name: Apigee Integration Structure
  property_count: 12
  slug: apigee-integration-structure
- name: Apigee Organization Structure
  property_count: 14
  slug: apigee-organization-structure
- name: Apigee Structure
  property_count: 0
  slug: apigee-structure
jsonld:
- class_count: 0
  name: Apigee Context
  property_count: 14
  slug: apigee-context
layout: provider
modified: '2026-05-22'
name: Apigee
nav: Providers
network: true
overview: 'Apigee publishes 45 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, API Deployments API, API Observations API, and 42 more. Tagged areas include Apigee, Advanced API Security, AI Agents, Analytics, and API Gateway.


  The Apigee catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apigee''s developer surface includes developer console, Stack Overflow tag, YouTube channel, authentication, developer portal, documentation, getting-started guide, and 77 more developer resources.'
plans:
- name: Apigee Plans Pricing
  plan_count: 11
  slug: apigee-plans-pricing
- name: Apigee Price Estimates
  plan_count: 0
  slug: apigee-price-estimates
random_paper: 3
rate_limits:
- limit_count: 0
  name: Apigee Rate Limits
  slug: apigee-rate-limits
rules:
- effective_rule_count: 7
  extends: []
  name: Apigee API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 5
  slug: apigee-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Apigee API Rules
  rule_count: 23
  severity_counts:
    error: 5
    hint: 0
    info: 3
    warn: 15
  slug: apigee-spectral-rules
scopes:
- name: Apigee Scopes
  scope_count: 1
  slug: apigee-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 68.2
  coverage:
    artifact_dirs: 25
    catalog_earned: 76.5
    catalog_earned_first_party: 12.0
    catalog_gap: 38.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 78.9
    contract_governance: 13.6
    contract_quality: 67.2
    developer_ergonomics: 82.1
    discoverability: 85.7
    operational_transparency: 44.7
  previous_composite: 67.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 41.8
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/apigee/refs/heads/main/screenshots/apigee-2026-06-20T172238.png
security:
- kind: authentication
  name: Apigee Authentication
  slug: apigee-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Apigee Domain Security
  slug: apigee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apigee Vulnerability Disclosure
  slug: apigee-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apigee
tags:
- Apigee
- Advanced API Security
- AI Agents
- Analytics
- API Gateway
- API Governance
- API Hub
- API Management
- Developer Portal
- Enterprise
- Generative AI
- Hybrid
- Integration
- Microservices
- MCP
- Monetization
website: https://cloud.google.com/apigee
---
