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
  trial: false
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
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 131
  human_in_the_loop: 3
  name: Jfrog Agentic Access
  operation_count: 257
  slug: jfrog-agentic-access
  summary_line: 257 operations · 131 acting · 3 human-in-the-loop
api_count: 14
apis:
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Token creation and management
  name: JFrog Access Tokens API
  phrasing_intents:
  - id: listTokens
    intent: List access tokens
    question: Which access tokens have been issued on my platform?
  - id: createToken
    intent: Create an access token
    question: How do I generate a scoped access token for a CI job?
  - id: getToken
    intent: Get access token details
    question: What scope and expiry does a particular token have?
  - id: revokeToken
    intent: Revoke an access token
    question: How do I revoke a leaked access token?
  phrasing_ops: 4
  slug: jfrog-access-tokens-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Deploy, retrieve, copy, move, and delete artifacts
  name: JFrog Artifacts & Storage API
  phrasing_intents:
  - id: getStorageInfo
    intent: Get file or folder storage info
    question: What are the checksums and size of a file stored in Artifactory?
  - id: getRepositoryStorageInfo
    intent: Get a repository's storage summary
    question: How much storage is one repository using?
  - id: getStorageSummaryInfo
    intent: Get the instance-wide storage summary
    question: How much binary and file store space is my whole instance using?
  - id: retrieveArtifact
    intent: Download an artifact
    question: How do I download a file from a repository?
  - id: deployArtifact
    intent: Upload (deploy) an artifact
    question: How do I upload a build artifact to a repository path?
  - id: deleteArtifact
    intent: Delete an artifact or folder
    question: Can I delete a whole folder from a repository, not just a single file?
  - id: copyArtifact
    intent: Copy an artifact or folder
    question: Can I do a dry run of copying an artifact to another repository first?
  - id: moveArtifact
    intent: Move an artifact or folder
    question: How do I relocate an artifact to another repository so it leaves the old path?
  phrasing_ops: 8
  slug: jfrog-artifacts-storage-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Curation audit and activity logs
  name: JFrog Audit API
  phrasing_intents:
  - id: getAuditLog
    intent: Get the curation audit log
    question: Which packages did curation block last week?
  phrasing_ops: 1
  slug: jfrog-audit-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Build information and promotion
  name: JFrog Builds API
  phrasing_intents:
  - id: listBuilds
    intent: List all builds
    question: Which builds are stored in Artifactory?
  - id: getBuildRuns
    intent: List runs of a build
    question: What runs exist for a particular build?
  - id: getBuildInfo
    intent: Get build info for a run
    question: How do I get the full build info for a specific build number?
  - id: promoteBuild
    intent: Promote a build to a target repository
    question: How do I promote a build's artifacts to a release repository?
  phrasing_ops: 4
  slug: jfrog-builds-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Remote command execution on devices
  name: JFrog Commands API
  phrasing_intents:
  - id: executeCommand
    intent: Run a remote command on devices
    question: How do I run a shell command on several devices at once?
  - id: getCommandStatus
    intent: Get a remote command's status
    question: Did the remote command I sent to my devices succeed?
  phrasing_ops: 2
  slug: jfrog-commands-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Component details and vulnerability information
  name: JFrog Components API
  phrasing_intents:
  - id: getComponentDetails
    intent: Get vulnerabilities and licenses for components
    question: What known vulnerabilities affect a given open-source component?
  phrasing_ops: 1
  slug: jfrog-components-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Model deployment and serving
  name: JFrog Deployments API
  phrasing_intents:
  - id: listDeployments
    intent: List model deployments
    question: Which ML model deployments are currently serving predictions?
  - id: createDeployment
    intent: Deploy a model version
    question: How do I deploy a trained model version so it can serve predictions?
  - id: getDeployment
    intent: Get a model deployment
    question: What resources and replicas does a model deployment use?
  - id: deleteDeployment
    intent: Remove a model deployment
    question: Can I take a model deployment offline?
  phrasing_ops: 4
  slug: jfrog-deployments-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Logical grouping of devices
  name: JFrog Device Groups API
  phrasing_intents:
  - id: listDeviceGroups
    intent: List device groups in a project
    question: Which device groups exist in a project?
  - id: createDeviceGroup
    intent: Create a device group
    question: How do I group several devices together in a project?
  - id: getDeviceGroup
    intent: Get a device group
    question: How do I see which devices are in a specific group?
  - id: deleteDeviceGroup
    intent: Delete a device group
    question: How do I delete a device group from a project?
  phrasing_ops: 4
  slug: jfrog-device-groups-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Device management and monitoring
  name: JFrog Devices API
  phrasing_intents:
  - id: listDevices
    intent: List devices in a project
    question: Which devices are registered in my project?
  - id: getDevice
    intent: Get a device
    question: How do I see the details of one device?
  - id: removeDevice
    intent: Remove a device from a project
    question: How do I remove a decommissioned device from a project?
  phrasing_ops: 3
  slug: jfrog-devices-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Distribute release bundles to edge nodes
  name: JFrog Distribution API
  phrasing_intents:
  - id: distributeReleaseBundle
    intent: Distribute a signed release bundle (v1)
    question: How do I push a signed release bundle out to edge nodes with the v1 distribution endpoint?
  - id: getDistributionStatus
    intent: Check v1 distribution status
    question: How do I check whether a v1 distribution reached its edge nodes?
  - id: deleteDistributedReleaseBundle
    intent: Delete a release bundle from edge nodes
    question: How do I remove a distributed release bundle from edge nodes?
  - id: postV2ReleaseBundleDistributeByNameByVersion
    intent: Distribute a release bundle (v2)
    question: How do I distribute a v2 release bundle to edge nodes?
  - id: getV2ReleaseBundleDistributeByNameByVersionStatus
    intent: Check v2 release bundle distribution status
    question: How do I check the distribution status of a v2 release bundle?
  phrasing_ops: 5
  slug: jfrog-distribution-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Create and manage evidence attestations
  name: JFrog Evidence API
  phrasing_intents:
  - id: createEvidence
    intent: Attach signed evidence to an artifact or build
    question: How do I attach a signed in-toto attestation to an artifact or build?
  - id: searchEvidence
    intent: Search evidence records
    question: Which evidence records were created by a given user in the last month?
  - id: getEvidence
    intent: Get one evidence record by ID
    question: How do I see the DSSE envelope of one evidence record by its ID?
  - id: deleteEvidence
    intent: Delete an evidence record
    question: How do I remove an evidence record that was attached by mistake?
  - id: getArtifactEvidence
    intent: List evidence attached to an artifact
    question: What attestations are attached to a specific artifact in a repository?
  - id: getBuildEvidence
    intent: List evidence attached to a build
    question: Which attestations were recorded against a particular build run?
  - id: getReleaseBundleEvidence
    intent: List evidence on a release bundle via v1
    question: How do I query the v1 evidence subject endpoint for a release bundle version?
  - id: getPackageEvidence
    intent: List evidence attached to a package
    question: What evidence is attached to a specific package version in a repository?
  phrasing_ops: 10
  slug: jfrog-evidence-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Worker testing and execution
  name: JFrog Execution API
  phrasing_intents:
  - id: testWorker
    intent: Test a worker with a sample payload
    question: How do I try out a worker with test data before enabling it?
  - id: getWorkerLogs
    intent: Get a worker's execution logs
    question: Where can I see the execution logs of a worker?
  phrasing_ops: 2
  slug: jfrog-execution-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: ML experiment tracking
  name: JFrog Experiments API
  phrasing_intents:
  - id: listExperiments
    intent: List ML experiments
    question: Which ML experiments have been run?
  - id: createExperiment
    intent: Create an ML experiment
    question: How do I track a new ML experiment?
  - id: getExperiment
    intent: Get an ML experiment
    question: What parameters were used in a given experiment?
  - id: deleteExperiment
    intent: Delete an ML experiment
    question: Can I delete an experiment I no longer need?
  phrasing_ops: 4
  slug: jfrog-experiments-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: User group management
  name: JFrog Groups API
  phrasing_intents:
  - id: listGroups
    intent: List groups in the Access service
    question: Which user groups are configured in the standalone Access service?
  - id: createGroup
    intent: Create a group in the Access service
    question: How do I create a group for organizing users and permissions in the Access service?
  - id: getGroup
    intent: Get a group and its members from Access
    question: Who are the members of a group in the standalone Access service?
  - id: updateGroup
    intent: Update a group in the Access service
    question: Can I change only a group's description in the Access service without resending everything?
  - id: deleteGroup
    intent: Delete a group in the Access service
    question: What happens to user associations when I delete a group in the Access service?
  - id: getAccessApiV2Groups
    intent: List groups through the Platform route
    question: Which groups exist on my JFrog Platform via the /access route?
  - id: postAccessApiV2Groups
    intent: Create a group through the Platform route
    question: How do I create a platform group using the /access URL?
  - id: getAccessApiV2GroupsByGroupName
    intent: Get a group through the Platform route
    question: What are a group's details when fetched through the platform /access URL?
  phrasing_ops: 10
  slug: jfrog-groups-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Rules for ignoring specific vulnerabilities
  name: JFrog Ignore Rules API
  phrasing_intents:
  - id: listIgnoreRules
    intent: List Xray ignore rules
    question: What ignore rules are configured in Xray?
  - id: createIgnoreRule
    intent: Create an Xray ignore rule
    question: How do I ignore a specific CVE in Xray until a set date?
  - id: getIgnoreRule
    intent: Get an Xray ignore rule
    question: How do I see what one ignore rule covers?
  - id: deleteIgnoreRule
    intent: Delete an Xray ignore rule
    question: How do I stop ignoring a vulnerability in Xray?
  phrasing_ops: 4
  slug: jfrog-ignore-rules-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: External service integrations
  name: JFrog Integrations API
  phrasing_intents:
  - id: listIntegrations
    intent: List integrations
    question: Which external service integrations are set up in Pipelines?
  - id: createIntegration
    intent: Create an integration
    question: How do I connect an external service like a Git provider as an integration?
  - id: getIntegration
    intent: Get an integration
    question: What are the settings of a particular integration?
  - id: updateIntegration
    intent: Update an integration
    question: How do I change the form values or credentials fields of an existing integration?
  - id: deleteIntegration
    intent: Delete an integration
    question: Can I delete an integration I no longer use?
  phrasing_ops: 5
  slug: jfrog-integrations-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: JFrog Platform Deployment management
  name: JFrog JPDs API
  phrasing_intents:
  - id: listJPDs
    intent: List managed platform deployments
    question: Which JFrog Platform Deployments does Mission Control manage?
  - id: addJPD
    intent: Add a platform deployment to Mission Control
    question: How do I register a new JFrog Platform Deployment with Mission Control?
  - id: getJPD
    intent: Get a platform deployment
    question: How do I see the details of one managed JPD?
  - id: updateJPD
    intent: Update a platform deployment
    question: How do I change the URL of a JPD that Mission Control manages?
  - id: removeJPD
    intent: Remove a platform deployment
    question: How do I stop Mission Control from managing a JPD?
  phrasing_ops: 5
  slug: jfrog-jpds-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Custom label management for packages
  name: JFrog Labels API
  phrasing_intents:
  - id: listLabels
    intent: List Catalog labels
    question: What custom labels have been defined in the Catalog?
  - id: createLabel
    intent: Create a Catalog label
    question: How do I create a new label for organizing packages?
  - id: getLabel
    intent: Get a Catalog label
    question: How do I see the description and color of one label?
  - id: updateLabel
    intent: Update a Catalog label
    question: How do I rename an existing label?
  - id: deleteLabel
    intent: Delete a Catalog label
    question: Does deleting a label detach it from every package?
  - id: applyLabelToPackages
    intent: Apply a label to packages
    question: How do I tag several packages with the same label at once?
  - id: removeLabelFromPackages
    intent: Remove a label from packages
    question: How do I take a label off some packages without deleting the label?
  phrasing_ops: 7
  slug: jfrog-labels-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: License management across instances
  name: JFrog Licenses API
  phrasing_intents:
  - id: listLicenseBuckets
    intent: List license buckets
    question: Which license buckets are attached?
  - id: addLicenseBucket
    intent: Add a license bucket
    question: How do I attach a new license bucket?
  - id: deleteLicenseBucket
    intent: Remove a license bucket
    question: Can I remove a license bucket I attached earlier?
  phrasing_ops: 3
  slug: jfrog-licenses-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Model version management
  name: JFrog Model Versions API
  phrasing_intents:
  - id: listModelVersions
    intent: List a model's versions
    question: Which versions exist for a given model?
  - id: createModelVersion
    intent: Create a model version
    question: How do I add a new version to a registered model?
  - id: getModelVersion
    intent: Get a model version
    question: What metrics and status does one model version have?
  - id: deleteModelVersion
    intent: Delete a model version
    question: Can I delete just one version of a model and keep the rest?
  phrasing_ops: 4
  slug: jfrog-model-versions-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: ML model registry and management
  name: JFrog Models API
  phrasing_intents:
  - id: listModels
    intent: List registered ML models
    question: Which ML models are registered in the model registry?
  - id: createModel
    intent: Register an ML model
    question: How do I register a new machine learning model in the registry?
  - id: getModel
    intent: Get an ML model
    question: What metadata is stored for a registered model?
  - id: updateModel
    intent: Update an ML model's metadata
    question: Can I change a registered model's tags or description?
  - id: deleteModel
    intent: Delete a model and all its versions
    question: What happens to a model's versions when I delete the model?
  phrasing_ops: 5
  slug: jfrog-models-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Build node pool management
  name: JFrog Node Pools API
  phrasing_intents:
  - id: listNodePools
    intent: List build node pools
    question: Which build node pools are configured for Pipelines?
  - id: createNodePool
    intent: Create a build node pool
    question: How do I create an on-demand pool of build nodes?
  - id: getNodePool
    intent: Get a build node pool
    question: How many nodes does a specific pool have?
  - id: deleteNodePool
    intent: Delete a build node pool
    question: How do I remove a node pool I no longer use?
  phrasing_ops: 4
  slug: jfrog-node-pools-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Package metadata search and retrieval
  name: JFrog Packages API
  phrasing_intents:
  - id: searchPackages
    intent: Search the package catalog
    question: Which packages in the catalog have known vulnerabilities?
  - id: getPackage
    intent: Get package details
    question: What licenses and vulnerabilities does a specific package have?
  - id: getPackageVersions
    intent: List a package's versions
    question: Which versions of a package are known, with vulnerability counts?
  - id: getVersionVulnerabilities
    intent: List CVEs affecting a package version
    question: Which CVEs affect a specific version of a package, including transitive ones?
  phrasing_ops: 4
  slug: jfrog-packages-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Permission target management
  name: JFrog Permissions API
  phrasing_intents:
  - id: listPermissions
    intent: List permission targets (/api/v2)
    question: Which permission targets are configured across the platform via /api/v2/permissions?
  - id: createPermission
    intent: Create a permission target (/api/v2)
    question: How do I create a permission target covering repositories, builds and release bundles?
  - id: getPermission
    intent: Get a permission target (/api/v2)
    question: What is the full configuration of a permission target under /api/v2?
  - id: updatePermission
    intent: Replace a permission target (/api/v2)
    question: Does the /api/v2 permission update replace the whole configuration?
  - id: deletePermission
    intent: Delete a permission target (/api/v2)
    question: What happens to access rules when I delete a target via /api/v2/permissions?
  - id: getAccessApiV2Permissions
    intent: List permissions in the Access service
    question: Which permission configurations does the Access service hold?
  - id: postAccessApiV2Permissions
    intent: Create a permission in the Access service
    question: How do I create a permission configuration through the Access service path?
  - id: getAccessApiV2PermissionsByPermissionName
    intent: Get a permission from the Access service
    question: How do I read one permission's details from the Access service?
  phrasing_ops: 10
  slug: jfrog-permissions-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Manage pipeline source configurations
  name: JFrog Pipeline Sources API
  phrasing_intents:
  - id: listPipelineSources
    intent: List pipeline sources
    question: Which repositories are registered as pipeline sources?
  - id: createPipelineSource
    intent: Add a pipeline source repository
    question: How do I point Pipelines at a Git repository with my pipeline definitions?
  - id: getPipelineSource
    intent: Get a pipeline source
    question: Which branch is a specific pipeline source tracking?
  - id: deletePipelineSource
    intent: Delete a pipeline source
    question: How do I remove a pipeline source?
  phrasing_ops: 4
  slug: jfrog-pipeline-sources-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Pipeline definitions and management
  name: JFrog Pipelines API
  phrasing_intents:
  - id: listPipelines
    intent: List pipelines
    question: Which pipelines are defined in my Pipelines setup?
  - id: getPipeline
    intent: Get a pipeline
    question: What are the details of a particular pipeline definition?
  phrasing_ops: 2
  slug: jfrog-pipelines-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Curation policy management
  name: JFrog Policies API
  phrasing_intents:
  - id: listPolicies
    intent: List curation policies
    question: Which curation policies are blocking or allowing packages right now?
  - id: createPolicy
    intent: Create a curation policy
    question: How do I block certain packages from entering my repositories with JFrog Curation?
  - id: getPolicy
    intent: Get a curation policy
    question: What conditions and actions does a given curation policy use?
  - id: updatePolicy
    intent: Update a curation policy
    question: Can I disable a curation policy without deleting it?
  - id: deletePolicy
    intent: Delete a curation policy
    question: Can I delete a curation policy I no longer need?
  - id: getV2Policies
    intent: List security and license policies
    question: Which security and license compliance policies are defined for scanning?
  - id: postV2Policies
    intent: Create a security or license policy
    question: How do I create a policy that flags vulnerable components or banned licenses?
  - id: getV2PoliciesByPolicyName
    intent: Get a security or license policy
    question: What rules are in a given security or license policy?
  phrasing_ops: 10
  slug: jfrog-policies-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Project administration
  name: JFrog Projects API
  phrasing_intents:
  - id: listProjects
    intent: List projects in the Access service
    question: Which projects exist when I call the standalone Access service directly?
  - id: createProject
    intent: Create a project in the Access service
    question: How do I create a JFrog project with its own isolated resource scope via the Access service?
  - id: getProject
    intent: Get a project from the Access service
    question: What settings does a given project key have in the standalone Access service?
  - id: updateProject
    intent: Update a project in the Access service
    question: How can I change a project's display name or storage quota through the Access service?
  - id: deleteProject
    intent: Delete a project from the Access service
    question: What happens to a project's resources when I permanently delete it in the Access service?
  - id: addUserToProject
    intent: Add a user to a project in the Access service
    question: How do I give a user a role in a project using the standalone Access service?
  - id: removeUserFromProject
    intent: Remove a user from a project in Access
    question: How do I revoke all of a member's project roles using the standalone Access service?
  - id: addGroupToProject
    intent: Add a group to a project
    question: How do I give a whole group of users roles in a project?
  phrasing_ops: 20
  slug: jfrog-projects-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Promote release bundles through environments
  name: JFrog Promotion API
  phrasing_intents:
  - id: getPromotionStatus
    intent: Get a release bundle's promotion history
    question: Which environments has a release bundle version been promoted to?
  - id: promoteReleaseBundle
    intent: Promote a release bundle to an environment
    question: How do I promote a release bundle version to production?
  phrasing_ops: 2
  slug: jfrog-promotion-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Set, update, and delete artifact properties
  name: JFrog Properties API
  phrasing_intents:
  - id: getItemProperties
    intent: Get properties on an artifact or folder
    question: What properties are set on a given artifact?
  - id: setItemProperties
    intent: Set properties on an artifact or folder
    question: How do I tag an artifact with custom properties?
  - id: deleteItemProperties
    intent: Remove properties from an artifact or folder
    question: How do I delete a property from an artifact?
  phrasing_ops: 3
  slug: jfrog-properties-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Create and manage release bundles (v1)
  name: JFrog Release Bundles V1 API
  phrasing_intents:
  - id: listReleaseBundles
    intent: List release bundles
    question: Which release bundles have been created for distribution?
  - id: createReleaseBundle
    intent: Create a release bundle
    question: How do I package a set of artifacts into a release bundle for distribution?
  - id: getReleaseBundle
    intent: Get a release bundle version
    question: What artifacts and release notes are in a given release bundle version?
  - id: updateReleaseBundle
    intent: Update a release bundle
    question: Can I change a release bundle's release notes before signing it?
  - id: deleteReleaseBundle
    intent: Delete a release bundle version
    question: Can I delete a release bundle version I created by mistake?
  - id: signReleaseBundle
    intent: Sign a release bundle
    question: How do I make a release bundle immutable so it can be distributed?
  phrasing_ops: 6
  slug: jfrog-release-bundles-v1-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Create and manage release bundles v2
  name: JFrog Release Bundles V2 API
  phrasing_intents:
  - id: createReleaseBundle
    intent: Create a v2 release bundle
    question: How do I create a v2 release bundle from builds or artifacts?
  - id: listReleaseBundles
    intent: List v2 release bundle records
    question: Which v2 release bundles exist?
  - id: getReleaseBundle
    intent: Get a v2 release bundle version
    question: What is in a specific v2 release bundle version?
  - id: deleteReleaseBundle
    intent: Delete a v2 release bundle version
    question: Can I delete a v2 release bundle version?
  phrasing_ops: 4
  slug: jfrog-release-bundles-v2-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Push and pull replication configuration
  name: JFrog Replication API
  phrasing_intents:
  - id: listReplications
    intent: List replication configurations
    question: Which repositories have replication set up?
  - id: getReplication
    intent: Get a repository's replication config
    question: How is replication configured for a specific repository?
  - id: createOrReplaceReplication
    intent: Create or replace repository replication
    question: How do I set up scheduled replication of a repository to another URL?
  - id: deleteReplication
    intent: Delete a repository's replication
    question: How do I stop replicating a repository?
  phrasing_ops: 4
  slug: jfrog-replication-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Vulnerability and compliance reports
  name: JFrog Reports API
  phrasing_intents:
  - id: generateVulnerabilityReport
    intent: Generate a vulnerability report
    question: How do I generate a vulnerability report for certain repositories or builds?
  - id: getReportStatus
    intent: Get a report's status
    question: Is my vulnerability report finished generating?
  - id: deleteReport
    intent: Delete a generated report
    question: Can I delete a report I generated earlier?
  phrasing_ops: 3
  slug: jfrog-reports-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Create, read, update, and delete repositories
  name: JFrog Repositories API
  phrasing_intents:
  - id: listRepositories
    intent: List repositories
    question: Which repositories exist in my Artifactory instance?
  - id: getRepository
    intent: Get a repository's configuration
    question: How do I see the full configuration of one repository?
  - id: createRepository
    intent: Create a repository
    question: How do I create a new local Maven repository?
  - id: updateRepository
    intent: Update a repository's configuration
    question: How do I black out an existing repository?
  - id: deleteRepository
    intent: Delete a repository
    question: How do I delete a repository I no longer use?
  phrasing_ops: 5
  slug: jfrog-repositories-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Pipeline run execution and monitoring
  name: JFrog Runs API
  phrasing_intents:
  - id: listRuns
    intent: List pipeline runs
    question: Which pipeline runs have failed recently?
  - id: getRun
    intent: Get a pipeline run
    question: What is the status of a particular pipeline run?
  - id: cancelRun
    intent: Cancel a pipeline run
    question: How do I stop a pipeline run that is in progress?
  - id: triggerPipeline
    intent: Trigger a pipeline run
    question: How do I start a new run of a pipeline on demand?
  phrasing_ops: 4
  slug: jfrog-runs-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: On-demand scanning operations
  name: JFrog Scanning API
  phrasing_intents:
  - id: scanBuild
    intent: Scan a build on demand
    question: How do I trigger a security scan of a CI build?
  - id: scanArtifact
    intent: Scan an artifact by component ID
    question: How do I scan a single artifact for vulnerabilities?
  phrasing_ops: 2
  slug: jfrog-scanning-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Remote execution scripts
  name: JFrog Scripts API
  phrasing_intents:
  - id: listScripts
    intent: List execution scripts
    question: Which execution scripts are available to run on my JPDs?
  - id: createScript
    intent: Create an execution script
    question: How do I add a new script that can run on my platform deployments?
  - id: executeScript
    intent: Run a script on platform deployments
    question: How do I run a script across several JPDs at once?
  phrasing_ops: 3
  slug: jfrog-scripts-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Search for artifacts using various criteria
  name: JFrog Searches API
  phrasing_intents:
  - id: executeAqlSearch
    intent: Run an AQL query
    question: How do I query Artifactory with AQL for complex artifact searches?
  - id: searchByGAVC
    intent: Search artifacts by Maven coordinates
    question: How do I find a Maven artifact by its group ID and artifact ID?
  - id: searchByProperties
    intent: Search artifacts by property values
    question: Which artifacts carry a particular property value?
  - id: searchByChecksum
    intent: Find artifacts by checksum
    question: Where else is a file with this SHA-256 stored?
  - id: getLatestVersion
    intent: Get the latest version of an artifact
    question: What is the newest version of a given Maven group and artifact?
  phrasing_ops: 5
  slug: jfrog-searches-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Users, groups, permissions, and access tokens
  name: JFrog Security API
  phrasing_intents:
  - id: listUsers
    intent: List all Artifactory users
    question: Who are all the users set up in my Artifactory instance?
  - id: getUser
    intent: Get an Artifactory user's details
    question: What groups and admin rights does a given Artifactory user have?
  - id: createOrReplaceUser
    intent: Create or replace an Artifactory user
    question: How do I add a new user to Artifactory with a password and email?
  - id: deleteUser
    intent: Delete an Artifactory user
    question: How do I remove a user account from Artifactory security?
  - id: listGroups
    intent: List all Artifactory groups
    question: Which user groups exist in my Artifactory instance?
  - id: getGroup
    intent: Get an Artifactory group's details
    question: What realm and auto-join settings does an Artifactory group have?
  - id: createOrReplaceGroup
    intent: Create or replace an Artifactory group
    question: How do I create a group that new users join automatically?
  - id: deleteGroup
    intent: Delete an Artifactory group
    question: How do I get rid of a security group I no longer use?
  phrasing_ops: 13
  slug: jfrog-security-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Pipeline step execution details
  name: JFrog Steps API
  phrasing_intents:
  - id: getStep
    intent: Get a pipeline step's details
    question: How do I see the status of one pipeline step execution?
  - id: getStepLogs
    intent: Get a pipeline step's console logs
    question: Where can I read the console output of a failed step?
  phrasing_ops: 2
  slug: jfrog-steps-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Artifact and build vulnerability summaries
  name: JFrog Summary API
  phrasing_intents:
  - id: getArtifactSummary
    intent: Get an artifact security and license summary
    question: What security issues and licenses affect these artifacts?
  - id: getBuildSummary
    intent: Get a build's security summary
    question: What security issues were found in a specific build?
  phrasing_ops: 2
  slug: jfrog-summary-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Access service system information
  name: JFrog System API
  phrasing_intents:
  - id: systemPing
    intent: Ping the Access service
    question: Is the Access service up and responding?
  - id: getSystemVersion
    intent: Get the Access service version
    question: Which version and revision of the Access service am I running?
  - id: getV1SystemPing
    intent: Ping a service's /v1 health endpoint
    question: Is the service behind the /v1/system/ping endpoint responding?
  - id: getV1SystemVersion
    intent: Get the Mission Control version
    question: What version of Mission Control is installed?
  - id: getSystemInfo
    intent: Get Pipelines system info
    question: Which version of JFrog Pipelines is running?
  - id: routerPing
    intent: Ping the platform router
    question: Is the platform router reachable?
  - id: getSystemHealth
    intent: Get health of all platform services
    question: Are all of the platform's services healthy right now?
  phrasing_ops: 7
  slug: jfrog-system-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: System health, configuration, and version information
  name: JFrog System & Configuration API
  phrasing_intents:
  - id: systemPing
    intent: Check that Artifactory is reachable
    question: Is my Artifactory instance up and responding?
  - id: getSystemVersion
    intent: Get the Artifactory version
    question: Which Artifactory version and build am I running?
  - id: getSystemConfiguration
    intent: Get the system configuration descriptor
    question: How do I export Artifactory's full system configuration as XML?
  - id: updateSystemConfiguration
    intent: Patch the system configuration with YAML
    question: How do I apply a partial configuration change to Artifactory using YAML?
  - id: getSystemLicenses
    intent: Get installed license details
    question: What license is installed on my Artifactory instance?
  phrasing_ops: 5
  slug: jfrog-system-configuration-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Access token creation, management, and revocation
  name: JFrog Tokens API
  phrasing_intents:
  - id: listTokens
    intent: List access tokens
    question: Which access tokens exist on the platform?
  - id: createToken
    intent: Create a scoped access token
    question: How do I create a project-scoped access token?
  - id: getToken
    intent: Get access token details
    question: How do I see when an access token expires?
  - id: revokeToken
    intent: Revoke an access token
    question: How do I immediately invalidate a leaked access token?
  phrasing_ops: 4
  slug: jfrog-tokens-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: OTA software update deployments
  name: JFrog Updates API
  phrasing_intents:
  - id: listUpdates
    intent: List OTA update deployments
    question: Which over-the-air updates are rolling out in a device project?
  - id: createUpdate
    intent: Create an OTA software update
    question: How do I push a software update over the air to my devices?
  - id: getUpdate
    intent: Get an OTA update's status
    question: How far along is a particular OTA update?
  - id: cancelUpdate
    intent: Cancel an OTA update
    question: Can I cancel an OTA update that is still pending or in progress?
  phrasing_ops: 4
  slug: jfrog-updates-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Platform user management
  name: JFrog Users API
  phrasing_intents:
  - id: listUsers
    intent: List platform users with status filter
    question: Which platform users are currently disabled?
  - id: createUser
    intent: Create a user via /api/v2/users
    question: How do I create a user and block their UI access at the same time?
  - id: getUser
    intent: Get a user via /api/v2/users
    question: How do I fetch a user's record from the /api/v2/users endpoint?
  - id: updateUser
    intent: Update or disable a user via /api/v2
    question: How do I disable a user account without deleting it?
  - id: deleteUser
    intent: Permanently delete a user via /api/v2
    question: Is deleting a user through /api/v2/users permanent?
  - id: getAccessApiV2Users
    intent: List users via the Access service
    question: How do I list all users through the /access/api/v2 endpoint?
  - id: postAccessApiV2Users
    intent: Create a user via the Access service
    question: How do I create a user through the /access/api/v2 path?
  - id: getAccessApiV2UsersByUsername
    intent: Get a user via the Access service
    question: How do I look up a user through the /access/api/v2 path?
  phrasing_ops: 10
  slug: jfrog-users-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Verify evidence and retrieve verification status
  name: JFrog Verification API
  phrasing_intents:
  - id: verifyEvidence
    intent: Verify an evidence record's signature
    question: How do I check that an evidence attestation's signature is valid?
  phrasing_ops: 1
  slug: jfrog-verification-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Policy violations management
  name: JFrog Violations API
  phrasing_intents:
  - id: getViolations
    intent: Get policy violations
    question: Which security and license violations have my watches found?
  phrasing_ops: 1
  slug: jfrog-violations-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Watch policies for monitoring artifacts
  name: JFrog Watches API
  phrasing_intents:
  - id: listWatches
    intent: List watches
    question: Which watches are monitoring my artifacts for policy violations?
  - id: createWatch
    intent: Create a watch
    question: How do I start monitoring repositories or builds against my security policies?
  - id: getWatch
    intent: Get a watch
    question: What resources and policies does a given watch cover?
  - id: updateWatch
    intent: Update a watch
    question: How do I add more repositories to an existing watch?
  - id: deleteWatch
    intent: Delete a watch
    question: Can I stop monitoring by removing a watch?
  phrasing_ops: 5
  slug: jfrog-watches-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Webhook configuration
  name: JFrog Webhooks API
  phrasing_intents:
  - id: listWebhooks
    intent: List webhooks
    question: What webhooks are configured on my platform?
  - id: createWebhook
    intent: Create a webhook subscription
    question: How do I get notified at my URL when an artifact is deployed?
  - id: getWebhook
    intent: Get a webhook
    question: How do I see which events a specific webhook listens for?
  - id: updateWebhook
    intent: Update a webhook
    question: How do I change the target URL of an existing webhook?
  - id: deleteWebhook
    intent: Delete a webhook
    question: How do I stop a webhook from firing permanently?
  phrasing_ops: 5
  slug: jfrog-webhooks-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: Worker lifecycle management
  name: JFrog Workers API
  phrasing_intents:
  - id: listWorkers
    intent: List workers
    question: Which serverless workers are registered on my platform?
  - id: createWorker
    intent: Create a serverless worker
    question: How do I deploy a TypeScript worker that runs on a platform event?
  - id: getWorker
    intent: Get a worker
    question: How do I view a worker's code and configuration?
  - id: updateWorker
    intent: Update a worker's code or config
    question: How do I push new code to an existing worker?
  - id: deleteWorker
    intent: Delete a worker
    question: How do I remove a worker I no longer need?
  - id: enableWorker
    intent: Enable a worker
    question: How do I turn a disabled worker back on?
  - id: disableWorker
    intent: Disable a worker
    question: How do I pause a worker without deleting it?
  phrasing_ops: 7
  slug: jfrog-workers-api
- baseURL: https://myserver.jfrog.io/artifactory/api
  baseurl_source: declared
  description: GraphQL query interface for package and CVE data
  name: JFrog Graph QL API
  phrasing_intents:
  - id: executeGraphQLQuery
    intent: Query the catalog with GraphQL
    question: How do I query the JFrog Catalog for packages and CVEs using GraphQL?
  phrasing_ops: 1
  slug: jfrog-graph-ql-api
arazzos:
- description: Create a group then a user in that group via the Access service.
  name: JFrog Access Create User With Group
  slug: jfrog-access-create-user-with-group-workflow
- description: Create a project, add a user to it, and confirm the project.
  name: JFrog Access Provision Project
  slug: jfrog-access-provision-project-workflow
- description: Create signed evidence for a build then verify its signature.
  name: JFrog Attach Build Evidence
  slug: jfrog-attach-build-evidence-workflow
- description: Run an AQL search for stale artifacts and delete the first match.
  name: JFrog Cleanup Stale Artifacts
  slug: jfrog-cleanup-stale-artifacts-workflow
- description: Confirm a repository exists then configure push replication for it.
  name: JFrog Configure Repository Replication
  slug: jfrog-configure-repository-replication-workflow
- description: Create a curation policy then review its audit log.
  name: JFrog Curation Policy Setup
  slug: jfrog-curation-policy-setup-workflow
- description: Deploy an artifact to a repository and confirm its storage metadata.
  name: JFrog Deploy and Verify Artifact
  slug: jfrog-deploy-and-verify-artifact-workflow
- description: Create a release bundle, sign it, distribute it, and poll for status.
  name: JFrog Distribution Release Bundle
  slug: jfrog-distribution-release-bundle-workflow
- description: Create a permission target granting a group access to a repository.
  name: JFrog Grant Repository Permission
  slug: jfrog-grant-repository-permission-workflow
- description: Register an ML model then publish a version of it.
  name: JFrog ML Register Model Version
  slug: jfrog-ml-register-model-version-workflow
- description: Trigger a pipeline run, find the new run, and poll until it finishes.
  name: JFrog Pipelines Trigger and Monitor
  slug: jfrog-pipelines-trigger-and-monitor-workflow
- description: Create a platform webhook subscription and confirm it.
  name: JFrog Platform Register Webhook
  slug: jfrog-platform-register-webhook-workflow
- description: Issue a fresh platform token then revoke a superseded one.
  name: JFrog Platform Rotate Access Token
  slug: jfrog-platform-rotate-access-token-workflow
- description: Find an artifact by its checksum and copy it to a release repository.
  name: JFrog Promote Artifact by Checksum
  slug: jfrog-promote-artifact-by-checksum-workflow
- description: Resolve a build run and promote it to a target repository.
  name: JFrog Promote Build
  slug: jfrog-promote-build-workflow
- description: Create a local Artifactory repository and confirm its configuration.
  name: JFrog Provision Local Repository
  slug: jfrog-provision-local-repository-workflow
- description: Create a v2 release bundle from a build and promote it to an environment.
  name: JFrog Release Bundle v2 Promote
  slug: jfrog-release-bundle-v2-promote-workflow
- description: Deploy an artifact then immediately scan it with Xray for issues.
  name: JFrog Secure Publish Artifact
  slug: jfrog-secure-publish-artifact-workflow
- description: Create a worker, run a test payload, then enable it on success.
  name: JFrog Worker Deploy and Test
  slug: jfrog-worker-deploy-and-test-workflow
- description: Look up component details then confirm via the catalog version data.
  name: JFrog Xray Component License Check
  slug: jfrog-xray-component-license-check-workflow
- description: Create a security policy then a watch that assigns it to a repository.
  name: JFrog Xray Policy and Watch
  slug: jfrog-xray-policy-and-watch-workflow
- description: Trigger an Xray scan for an artifact then pull its security summary.
  name: JFrog Xray Scan Artifact
  slug: jfrog-xray-scan-artifact-workflow
- description: Trigger an Xray CI build scan then read the build security summary.
  name: JFrog Xray Scan Build
  slug: jfrog-xray-scan-build-workflow
- description: Query Xray violations and create an ignore rule when any are found.
  name: JFrog Xray Triage Violation
  slug: jfrog-xray-triage-violation-workflow
- description: Generate a vulnerability report and poll until it completes.
  name: JFrog Xray Vulnerability Report
  slug: jfrog-xray-vulnerability-report-workflow
artifact_total: 362
collections:
- collection_type: postman
  name: JFrog Access REST API
  slug: postman-jfrog-access
- collection_type: postman
  name: JFrog Artifactory REST API
  slug: postman-jfrog-artifactory
- collection_type: postman
  name: JFrog Catalog REST API
  slug: postman-jfrog-catalog
- collection_type: postman
  name: JFrog Connect REST API
  slug: postman-jfrog-connect
- collection_type: postman
  name: JFrog Curation REST API
  slug: postman-jfrog-curation
- collection_type: postman
  name: JFrog Distribution REST API
  slug: postman-jfrog-distribution
- collection_type: postman
  name: JFrog Evidence REST API
  slug: postman-jfrog-evidence
- collection_type: postman
  name: JFrog Mission Control REST API
  slug: postman-jfrog-mission-control
- collection_type: postman
  name: JFrog ML REST API
  slug: postman-jfrog-ml
- collection_type: postman
  name: JFrog Pipelines REST API
  slug: postman-jfrog-pipelines
- collection_type: postman
  name: JFrog Platform REST API
  slug: postman-jfrog-platform
- collection_type: postman
  name: JFrog Release Lifecycle Management REST API
  slug: postman-jfrog-release-lifecycle
- collection_type: postman
  name: JFrog Workers REST API
  slug: postman-jfrog-workers
- collection_type: postman
  name: JFrog Xray REST API
  slug: postman-jfrog-xray
- collection_type: open
  name: JFrog Access REST Access Tokens API
  slug: open-jfrog-access-tokens-api
- collection_type: open
  name: JFrog Access REST API
  slug: open-jfrog-access
- collection_type: open
  name: JFrog Artifactory REST API
  slug: open-jfrog-artifactory
- collection_type: open
  name: JFrog Access REST Access Tokens Artifacts & Storage API
  slug: open-jfrog-artifacts-storage-api
- collection_type: open
  name: JFrog Access REST Access Tokens Audit API
  slug: open-jfrog-audit-api
- collection_type: open
  name: JFrog Access REST Access Tokens Builds API
  slug: open-jfrog-builds-api
- collection_type: open
  name: JFrog Catalog REST API
  slug: open-jfrog-catalog
- collection_type: open
  name: JFrog Access REST Access Tokens Commands API
  slug: open-jfrog-commands-api
- collection_type: open
  name: JFrog Access REST Access Tokens Components API
  slug: open-jfrog-components-api
- collection_type: open
  name: JFrog Connect REST API
  slug: open-jfrog-connect
- collection_type: open
  name: JFrog Curation REST API
  slug: open-jfrog-curation
- collection_type: open
  name: JFrog Access REST Access Tokens Deployments API
  slug: open-jfrog-deployments-api
- collection_type: open
  name: JFrog Access REST Access Tokens Device Groups API
  slug: open-jfrog-device-groups-api
- collection_type: open
  name: JFrog Access REST Access Tokens Devices API
  slug: open-jfrog-devices-api
- collection_type: open
  name: JFrog Access REST Access Tokens Distribution API
  slug: open-jfrog-distribution-api
- collection_type: open
  name: JFrog Distribution REST API
  slug: open-jfrog-distribution
- collection_type: open
  name: JFrog Access REST Access Tokens Evidence API
  slug: open-jfrog-evidence-api
- collection_type: open
  name: JFrog Evidence REST API
  slug: open-jfrog-evidence
- collection_type: open
  name: JFrog Access REST Access Tokens Execution API
  slug: open-jfrog-execution-api
- collection_type: open
  name: JFrog Access REST Access Tokens Experiments API
  slug: open-jfrog-experiments-api
- collection_type: open
  name: JFrog Access REST Access Tokens GraphQL API
  slug: open-jfrog-graphql-api
- collection_type: open
  name: JFrog Access REST Access Tokens Groups API
  slug: open-jfrog-groups-api
- collection_type: open
  name: JFrog Access REST Access Tokens Ignore Rules API
  slug: open-jfrog-ignore-rules-api
- collection_type: open
  name: JFrog Access REST Access Tokens Integrations API
  slug: open-jfrog-integrations-api
- collection_type: open
  name: JFrog Access REST Access Tokens JPDs API
  slug: open-jfrog-jpds-api
- collection_type: open
  name: JFrog Access REST Access Tokens Labels API
  slug: open-jfrog-labels-api
- collection_type: open
  name: JFrog Access REST Access Tokens Licenses API
  slug: open-jfrog-licenses-api
- collection_type: open
  name: JFrog Mission Control REST API
  slug: open-jfrog-mission-control
- collection_type: open
  name: JFrog ML REST API
  slug: open-jfrog-ml
- collection_type: open
  name: JFrog Access REST Access Tokens Model Versions API
  slug: open-jfrog-model-versions-api
- collection_type: open
  name: JFrog Access REST Access Tokens Models API
  slug: open-jfrog-models-api
- collection_type: open
  name: JFrog Access REST Access Tokens Node Pools API
  slug: open-jfrog-node-pools-api
- collection_type: open
  name: JFrog Access REST Access Tokens Packages API
  slug: open-jfrog-packages-api
- collection_type: open
  name: JFrog Access REST Access Tokens Permissions API
  slug: open-jfrog-permissions-api
- collection_type: open
  name: JFrog Access REST Access Tokens Pipeline Sources API
  slug: open-jfrog-pipeline-sources-api
- collection_type: open
  name: JFrog Access REST Access Tokens Pipelines API
  slug: open-jfrog-pipelines-api
- collection_type: open
  name: JFrog Pipelines REST API
  slug: open-jfrog-pipelines
- collection_type: open
  name: JFrog Platform REST API
  slug: open-jfrog-platform
- collection_type: open
  name: JFrog Access REST Access Tokens Policies API
  slug: open-jfrog-policies-api
- collection_type: open
  name: JFrog Access REST Access Tokens Projects API
  slug: open-jfrog-projects-api
- collection_type: open
  name: JFrog Access REST Access Tokens Promotion API
  slug: open-jfrog-promotion-api
- collection_type: open
  name: JFrog Access REST Access Tokens Properties API
  slug: open-jfrog-properties-api
- collection_type: open
  name: JFrog Access REST Access Tokens Release Bundles V1 API
  slug: open-jfrog-release-bundles-v1-api
- collection_type: open
  name: JFrog Access REST Access Tokens Release Bundles V2 API
  slug: open-jfrog-release-bundles-v2-api
- collection_type: open
  name: JFrog Release Lifecycle Management REST API
  slug: open-jfrog-release-lifecycle
- collection_type: open
  name: JFrog Access REST Access Tokens Replication API
  slug: open-jfrog-replication-api
- collection_type: open
  name: JFrog Access REST Access Tokens Reports API
  slug: open-jfrog-reports-api
- collection_type: open
  name: JFrog Access REST Access Tokens Repositories API
  slug: open-jfrog-repositories-api
- collection_type: open
  name: JFrog Access REST Access Tokens Runs API
  slug: open-jfrog-runs-api
- collection_type: open
  name: JFrog Access REST Access Tokens Scanning API
  slug: open-jfrog-scanning-api
- collection_type: open
  name: JFrog Access REST Access Tokens Scripts API
  slug: open-jfrog-scripts-api
- collection_type: open
  name: JFrog Access REST Access Tokens Searches API
  slug: open-jfrog-searches-api
- collection_type: open
  name: JFrog Access REST Access Tokens Security API
  slug: open-jfrog-security-api
- collection_type: open
  name: JFrog Access REST Access Tokens Steps API
  slug: open-jfrog-steps-api
- collection_type: open
  name: JFrog Access REST Access Tokens Summary API
  slug: open-jfrog-summary-api
- collection_type: open
  name: JFrog Access REST Access Tokens System API
  slug: open-jfrog-system-api
- collection_type: open
  name: JFrog Access REST Access Tokens System & Configuration API
  slug: open-jfrog-system-configuration-api
- collection_type: open
  name: JFrog Access REST Access Tokens API
  slug: open-jfrog-tokens-api
- collection_type: open
  name: JFrog Access REST Access Tokens Updates API
  slug: open-jfrog-updates-api
- collection_type: open
  name: JFrog Access REST Access Tokens Users API
  slug: open-jfrog-users-api
- collection_type: open
  name: JFrog Access REST Access Tokens Verification API
  slug: open-jfrog-verification-api
- collection_type: open
  name: JFrog Access REST Access Tokens Violations API
  slug: open-jfrog-violations-api
- collection_type: open
  name: JFrog Access REST Access Tokens Watches API
  slug: open-jfrog-watches-api
- collection_type: open
  name: JFrog Access REST Access Tokens Webhooks API
  slug: open-jfrog-webhooks-api
- collection_type: open
  name: JFrog Access REST Access Tokens Workers API
  slug: open-jfrog-workers-api
- collection_type: open
  name: JFrog Workers REST API
  slug: open-jfrog-workers
- collection_type: open
  name: JFrog Xray REST API
  slug: open-jfrog-xray
common:
- group: design
  href: https://artifacts.apis.io/jfrog/rules/jfrog-rules.yml
  title: ''
  type: Spectral
  url: rules/jfrog-rules.yml
- group: design
  href: https://artifacts.apis.io/jfrog/rules/jfrog-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/jfrog-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/jfrog/json-ld/jfrog-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jfrog-context.jsonld
- group: design
  href: https://artifacts.apis.io/jfrog/vocabulary/jfrog-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jfrog-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/jfrog/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/jfrog/data-model/jfrog-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jfrog-data-model.yml
- group: operate
  href: https://artifacts.apis.io/jfrog/changelog/jfrog-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/jfrog-changelog.yml
- group: auth
  href: https://artifacts.apis.io/jfrog/security/jfrog-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/jfrog-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/jfrog/errors/jfrog-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jfrog-problem-types.yml
- group: design
  href: https://artifacts.apis.io/jfrog/conformance/jfrog-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jfrog-conformance.yml
- group: other
  href: https://artifacts.apis.io/jfrog/overlays/jfrog-access-tokens-api-phrasing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/jfrog-access-tokens-api-phrasing-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/jfrog/llms/jfrog-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jfrog-llms.txt
- group: auth
  href: https://artifacts.apis.io/jfrog/well-known/jfrog-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jfrog-status-security.txt
- group: auth
  href: https://artifacts.apis.io/jfrog/well-known/jfrog-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/jfrog-security.txt
- group: agent
  href: https://artifacts.apis.io/jfrog/well-known/jfrog-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jfrog-well-known.yml
- group: other
  href: https://artifacts.apis.io/jfrog/hosts/jfrog-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jfrog-hosts.yml
- group: build
  href: https://artifacts.apis.io/jfrog/integrations/jfrog-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/jfrog-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/jfrog/vendors/jfrog-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jfrog-vendors.yml
- group: build
  href: https://artifacts.apis.io/jfrog/packages/jfrog-packages.yml
  title: ''
  type: Packages
  url: packages/jfrog-packages.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://jfrog.com/trust/
- group: company
  title: ''
  type: Newsroom
  url: https://jfrog.com/about/press/
- group: other
  title: ''
  type: Leadership
  url: https://jfrog.com/about/management/
- group: commercial
  href: https://artifacts.apis.io/jfrog/finops/jfrog-finops.yml
  title: ''
  type: FinOps
  url: finops/jfrog-finops.yml
- group: operate
  href: https://artifacts.apis.io/jfrog/rate-limits/jfrog-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jfrog-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jfrog/plans/jfrog-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jfrog-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/jfrog/capabilities/jfrog-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/jfrog-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/jfrog/agentic-access/jfrog-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jfrog-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/jfrog/security/jfrog-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jfrog-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jfrog/security/jfrog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jfrog-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/jfrog/authentication/jfrog-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jfrog-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/jfrog/overview
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-access-create-user-with-group-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-access-create-user-with-group-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-access-provision-project-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-access-provision-project-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-attach-build-evidence-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-attach-build-evidence-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-cleanup-stale-artifacts-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-cleanup-stale-artifacts-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-configure-repository-replication-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-configure-repository-replication-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-curation-policy-setup-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-curation-policy-setup-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-deploy-and-verify-artifact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-deploy-and-verify-artifact-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-distribution-release-bundle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-distribution-release-bundle-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-grant-repository-permission-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-grant-repository-permission-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-ml-register-model-version-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-ml-register-model-version-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-pipelines-trigger-and-monitor-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-pipelines-trigger-and-monitor-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-platform-register-webhook-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-platform-register-webhook-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-platform-rotate-access-token-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-platform-rotate-access-token-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-promote-artifact-by-checksum-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-promote-artifact-by-checksum-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-promote-build-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-promote-build-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-provision-local-repository-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-provision-local-repository-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-release-bundle-v2-promote-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-release-bundle-v2-promote-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-secure-publish-artifact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-secure-publish-artifact-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-worker-deploy-and-test-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-worker-deploy-and-test-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-xray-component-license-check-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-xray-component-license-check-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-xray-policy-and-watch-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-xray-policy-and-watch-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-xray-scan-artifact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-xray-scan-artifact-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-xray-scan-build-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-xray-scan-build-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-xray-triage-violation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-xray-triage-violation-workflow.yml
- group: design
  href: https://artifacts.apis.io/jfrog/arazzo/jfrog-xray-vulnerability-report-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/jfrog-xray-vulnerability-report-workflow.yml
- group: docs
  title: ''
  type: Documentation
  url: https://jfrog.com/help/r/jfrog-rest-apis/jfrog-rest-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://jfrog.com/artifactory/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/access-tokens
- group: company
  title: ''
  type: Blog
  url: https://jfrog.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.jfrog.io/
- group: operate
  title: ''
  type: Support
  url: https://jfrog.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jfrog.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jfrog
- group: operate
  title: ''
  type: Community
  url: https://jfrog.com/community/
- group: company
  title: ''
  type: Website
  url: https://jfrog.com/
- group: start
  title: ''
  type: Login
  url: https://my.jfrog.com/login/
- group: start
  title: ''
  type: Signup
  url: https://jfrog.com/start-free/
- group: commercial
  title: ''
  type: Pricing
  url: https://jfrog.com/pricing/
- group: build
  title: ''
  type: CLI
  url: https://jfrog.com/getcli/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jfrog/jfrog-client-go
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/jfrog/artifactory-client-java
- group: build
  title: ''
  type: JavaScript SDK
  url: https://github.com/jfrog/jfrog-client-js
- group: learn
  title: ''
  type: Academy
  url: https://academy.jfrog.com/
- group: design
  title: ''
  type: Webhooks
  url: https://jfrog.com/help/r/jfrog-platform-administration-documentation/webhooks
- group: other
  title: ''
  type: Terraform Provider
  url: https://registry.terraform.io/providers/jfrog/platform/latest/docs
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/jfrog
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/api-evangelist/jfrog/documentation/zgmorin/jfrog-rest-api
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/jfrog-ltd
- group: design
  href: https://artifacts.apis.io/jfrog/json-ld/jfrog-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/jfrog-context.jsonld
- group: docs
  href: https://artifacts.apis.io/jfrog/json-schema/jfrog-artifact-schema.json
  title: ''
  type: JSON Schema - Artifact
  url: json-schema/jfrog-artifact-schema.json
- group: docs
  href: https://artifacts.apis.io/jfrog/json-schema/jfrog-repository-schema.json
  title: ''
  type: JSON Schema - Repository
  url: json-schema/jfrog-repository-schema.json
- group: docs
  href: https://artifacts.apis.io/jfrog/json-schema/jfrog-build-info-schema.json
  title: ''
  type: JSON Schema - Build Info
  url: json-schema/jfrog-build-info-schema.json
- group: docs
  href: https://artifacts.apis.io/jfrog/json-schema/jfrog-release-bundle-schema.json
  title: ''
  type: JSON Schema - Release Bundle
  url: json-schema/jfrog-release-bundle-schema.json
- group: docs
  href: https://artifacts.apis.io/jfrog/json-schema/jfrog-security-vulnerability-schema.json
  title: ''
  type: JSON Schema - Security Vulnerability
  url: json-schema/jfrog-security-vulnerability-schema.json
- group: docs
  href: https://artifacts.apis.io/jfrog/json-schema/jfrog-user-schema.json
  title: ''
  type: JSON Schema - User
  url: json-schema/jfrog-user-schema.json
- group: docs
  href: https://artifacts.apis.io/jfrog/json-schema/jfrog-permission-schema.json
  title: ''
  type: JSON Schema - Permission
  url: json-schema/jfrog-permission-schema.json
- group: docs
  href: https://artifacts.apis.io/jfrog/json-schema/jfrog-pipeline-schema.json
  title: ''
  type: JSON Schema - Pipeline
  url: json-schema/jfrog-pipeline-schema.json
- group: docs
  href: https://artifacts.apis.io/jfrog/json-schema/jfrog-worker-schema.json
  title: ''
  type: JSON Schema - Worker
  url: json-schema/jfrog-worker-schema.json
- group: docs
  href: https://artifacts.apis.io/jfrog/json-schema/jfrog-curation-policy-schema.json
  title: ''
  type: JSON Schema - Curation Policy
  url: json-schema/jfrog-curation-policy-schema.json
- group: docs
  href: https://artifacts.apis.io/jfrog/json-schema/jfrog-evidence-schema.json
  title: ''
  type: JSON Schema - Evidence
  url: json-schema/jfrog-evidence-schema.json
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/jfrog/mcp-jfrog
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/jfrog/jfrog-skills
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.connect.jfrog.io/llms.txt
created: '2024'
description: JFrog provides universal DevOps solutions for software supply chain automation and security, offering a unified platform for managing binaries, securing the software supply chain, and automating DevOps workflows.
finops:
- has_sources: true
  method: derived
  name: Jfrog Finops
  primary_unit: subscription
  service_category: ''
  slug: jfrog-finops
  template: false
image: https://jfrog.com/brand/jfrog-logo.png
json_schemas:
- name: AccessToken
  property_count: 5
  slug: jfrog-access-token
- name: AccessToken
  property_count: 5
  slug: jfrog-accesstoken
- name: AqlSearchResult
  property_count: 2
  slug: jfrog-aql-search-result
- name: AqlSearchResult
  property_count: 2
  slug: jfrog-aqlsearchresult
- name: JFrog Artifact
  property_count: 16
  slug: jfrog-artifact
- name: ArtifactSummary
  property_count: 1
  slug: jfrog-artifact-summary
- name: ArtifactSummary
  property_count: 1
  slug: jfrog-artifactsummary
- name: AuditEntry
  property_count: 9
  slug: jfrog-audit-entry
- name: AuditEntry
  property_count: 9
  slug: jfrog-auditentry
- name: JFrog Build Info
  property_count: 16
  slug: jfrog-build-info
- name: BuildPromotion
  property_count: 11
  slug: jfrog-build-promotion
- name: BuildRuns
  property_count: 2
  slug: jfrog-build-runs
- name: BuildSummary
  property_count: 2
  slug: jfrog-build-summary
- name: BuildInfo
  property_count: 1
  slug: jfrog-buildinfo
- name: BuildPromotion
  property_count: 11
  slug: jfrog-buildpromotion
- name: BuildRuns
  property_count: 2
  slug: jfrog-buildruns
- name: BuildsList
  property_count: 1
  slug: jfrog-builds-list
- name: BuildsList
  property_count: 1
  slug: jfrog-buildslist
- name: BuildSummary
  property_count: 2
  slug: jfrog-buildsummary
- name: CatalogVulnerability
  property_count: 9
  slug: jfrog-catalog-vulnerability
- name: CatalogVulnerability
  property_count: 9
  slug: jfrog-catalogvulnerability
- name: Checksums
  property_count: 3
  slug: jfrog-checksums
- name: CommandRequest
  property_count: 4
  slug: jfrog-command-request
- name: CommandRequest
  property_count: 4
  slug: jfrog-commandrequest
- name: ComponentDetail
  property_count: 6
  slug: jfrog-component-detail
- name: ComponentDetail
  property_count: 6
  slug: jfrog-componentdetail
- name: CreateEvidenceRequest
  property_count: 6
  slug: jfrog-create-evidence-request
- name: CreateTokenRequest
  property_count: 7
  slug: jfrog-create-token-request
- name: CreateUserRequest_2
  property_count: 6
  slug: jfrog-create-user-request-2
- name: CreateUserRequest
  property_count: 7
  slug: jfrog-create-user-request
- name: CreateEvidenceRequest
  property_count: 6
  slug: jfrog-createevidencerequest
- name: CreateTokenRequest
  property_count: 8
  slug: jfrog-createtokenrequest
- name: CreateUserRequest
  property_count: 7
  slug: jfrog-createuserrequest
- name: CurationPolicyRequest
  property_count: 8
  slug: jfrog-curation-policy-request
- name: JFrog Curation Policy
  property_count: 10
  slug: jfrog-curation-policy
- name: CurationPolicy
  property_count: 10
  slug: jfrog-curationpolicy
- name: CurationPolicyRequest
  property_count: 8
  slug: jfrog-curationpolicyrequest
- name: DeployResponse
  property_count: 10
  slug: jfrog-deploy-response
- name: DeploymentRequest
  property_count: 5
  slug: jfrog-deployment-request
- name: Deployment
  property_count: 9
  slug: jfrog-deployment
- name: DeploymentRequest
  property_count: 5
  slug: jfrog-deploymentrequest
- name: DeployResponse
  property_count: 10
  slug: jfrog-deployresponse
- name: DeviceGroupRequest
  property_count: 3
  slug: jfrog-device-group-request
- name: DeviceGroup
  property_count: 5
  slug: jfrog-device-group
- name: Device
  property_count: 13
  slug: jfrog-device
- name: DeviceGroup
  property_count: 5
  slug: jfrog-devicegroup
- name: DeviceGroupRequest
  property_count: 3
  slug: jfrog-devicegrouprequest
- name: DistributeRequest
  property_count: 2
  slug: jfrog-distribute-request
- name: DistributeRequest
  property_count: 2
  slug: jfrog-distributerequest
- name: DistributionRequest
  property_count: 3
  slug: jfrog-distribution-request
- name: DistributionRequest
  property_count: 3
  slug: jfrog-distributionrequest
- name: Evidence_2
  property_count: 9
  slug: jfrog-evidence-2
- name: EvidenceRequest
  property_count: 6
  slug: jfrog-evidence-request
- name: JFrog Evidence
  property_count: 11
  slug: jfrog-evidence
- name: EvidenceSearchRequest
  property_count: 7
  slug: jfrog-evidence-search-request
- name: EvidenceRequest
  property_count: 6
  slug: jfrog-evidencerequest
- name: EvidenceSearchRequest
  property_count: 7
  slug: jfrog-evidencesearchrequest
- name: ExperimentRequest
  property_count: 4
  slug: jfrog-experiment-request
- name: Experiment
  property_count: 10
  slug: jfrog-experiment
- name: ExperimentRequest
  property_count: 4
  slug: jfrog-experimentrequest
- name: FileInfo
  property_count: 13
  slug: jfrog-file-info
- name: FileInfo
  property_count: 13
  slug: jfrog-fileinfo
- name: FolderInfo
  property_count: 9
  slug: jfrog-folder-info
- name: FolderInfo
  property_count: 9
  slug: jfrog-folderinfo
- name: GraphQLRequest
  property_count: 3
  slug: jfrog-graph-qlrequest
- name: GraphQLResponse
  property_count: 2
  slug: jfrog-graph-qlresponse
- name: GraphQLRequest
  property_count: 3
  slug: jfrog-graphqlrequest
- name: GraphQLResponse
  property_count: 2
  slug: jfrog-graphqlresponse
- name: Group
  property_count: 7
  slug: jfrog-group
- name: GroupSummary
  property_count: 2
  slug: jfrog-group-summary
- name: GroupSummary
  property_count: 2
  slug: jfrog-groupsummary
- name: IgnoreRule
  property_count: 10
  slug: jfrog-ignore-rule
- name: IgnoreRule
  property_count: 10
  slug: jfrog-ignorerule
- name: IntegrationRequest
  property_count: 5
  slug: jfrog-integration-request
- name: Integration
  property_count: 7
  slug: jfrog-integration
- name: IntegrationRequest
  property_count: 5
  slug: jfrog-integrationrequest
- name: Issue
  property_count: 9
  slug: jfrog-issue
- name: ItemProperties
  property_count: 2
  slug: jfrog-item-properties
- name: ItemProperties
  property_count: 2
  slug: jfrog-itemproperties
- name: JPD
  property_count: 7
  slug: jfrog-jpd
- name: JPDRequest
  property_count: 4
  slug: jfrog-jpdrequest
- name: LabelRequest
  property_count: 3
  slug: jfrog-label-request
- name: Label
  property_count: 6
  slug: jfrog-label
- name: LabelRequest
  property_count: 3
  slug: jfrog-labelrequest
- name: LicenseBucket
  property_count: 6
  slug: jfrog-license-bucket
- name: LicenseInfo
  property_count: 3
  slug: jfrog-license-info
- name: LicenseBucket
  property_count: 6
  slug: jfrog-licensebucket
- name: LicenseInfo
  property_count: 3
  slug: jfrog-licenseinfo
- name: ModelRequest
  property_count: 5
  slug: jfrog-model-request
- name: Model
  property_count: 11
  slug: jfrog-model
- name: ModelVersionRequest
  property_count: 6
  slug: jfrog-model-version-request
- name: ModelVersion
  property_count: 10
  slug: jfrog-model-version
- name: ModelRequest
  property_count: 5
  slug: jfrog-modelrequest
- name: ModelVersion
  property_count: 10
  slug: jfrog-modelversion
- name: ModelVersionRequest
  property_count: 6
  slug: jfrog-modelversionrequest
- name: MoveOrCopyResponse
  property_count: 1
  slug: jfrog-move-or-copy-response
- name: MoveOrCopyResponse
  property_count: 1
  slug: jfrog-moveorcopyresponse
- name: NodePoolRequest
  property_count: 6
  slug: jfrog-node-pool-request
- name: NodePool
  property_count: 9
  slug: jfrog-node-pool
- name: NodePool
  property_count: 9
  slug: jfrog-nodepool
- name: NodePoolRequest
  property_count: 6
  slug: jfrog-nodepoolrequest
- name: PackageDetail
  property_count: 10
  slug: jfrog-package-detail
- name: PackageSearchRequest
  property_count: 7
  slug: jfrog-package-search-request
- name: PackageSearchResponse
  property_count: 2
  slug: jfrog-package-search-response
- name: PackageVersion
  property_count: 7
  slug: jfrog-package-version
- name: PackageDetail
  property_count: 10
  slug: jfrog-packagedetail
- name: PackageSearchRequest
  property_count: 7
  slug: jfrog-packagesearchrequest
- name: PackageSearchResponse
  property_count: 2
  slug: jfrog-packagesearchresponse
- name: PackageSummary
  property_count: 7
  slug: jfrog-packagesummary
- name: PackageVersion
  property_count: 7
  slug: jfrog-packageversion
- name: Permission_2
  property_count: 2
  slug: jfrog-permission-2
- name: JFrog Permission Target
  property_count: 2
  slug: jfrog-permission
- name: PermissionTarget
  property_count: 3
  slug: jfrog-permission-target
- name: PermissionTarget
  property_count: 3
  slug: jfrog-permissiontarget
- name: PermissionTargetSummary
  property_count: 2
  slug: jfrog-permissiontargetsummary
- name: JFrog Pipeline
  property_count: 9
  slug: jfrog-pipeline
- name: PipelineSourceRequest
  property_count: 6
  slug: jfrog-pipeline-source-request
- name: PipelineSource
  property_count: 9
  slug: jfrog-pipeline-source
- name: PipelineSource
  property_count: 9
  slug: jfrog-pipelinesource
- name: PipelineSourceRequest
  property_count: 6
  slug: jfrog-pipelinesourcerequest
- name: PlatformGroup
  property_count: 7
  slug: jfrog-platform-group
- name: PlatformUser
  property_count: 8
  slug: jfrog-platform-user
- name: PlatformGroup
  property_count: 7
  slug: jfrog-platformgroup
- name: PlatformUser
  property_count: 8
  slug: jfrog-platformuser
- name: Policy
  property_count: 4
  slug: jfrog-policy
- name: Project_3
  property_count: 8
  slug: jfrog-project-3
- name: Project
  property_count: 8
  slug: jfrog-project
- name: ProjectRequest
  property_count: 5
  slug: jfrog-projectrequest
- name: PromotionRequest
  property_count: 5
  slug: jfrog-promotion-request
- name: PromotionStatus
  property_count: 4
  slug: jfrog-promotion-status
- name: PromotionRequest
  property_count: 5
  slug: jfrog-promotionrequest
- name: PromotionStatus
  property_count: 4
  slug: jfrog-promotionstatus
- name: ReleaseBundleRequest
  property_count: 7
  slug: jfrog-release-bundle-request
- name: JFrog Release Bundle
  property_count: 13
  slug: jfrog-release-bundle
- name: ReleaseBundleV2Request
  property_count: 5
  slug: jfrog-release-bundle-v2-request
- name: ReleaseBundleV2
  property_count: 9
  slug: jfrog-release-bundle-v2
- name: ReleaseBundleV2Summary
  property_count: 6
  slug: jfrog-release-bundle-v2-summary
- name: ReleaseBundle
  property_count: 8
  slug: jfrog-releasebundle
- name: ReleaseBundleRequest
  property_count: 7
  slug: jfrog-releasebundlerequest
- name: ReleaseBundleV2
  property_count: 9
  slug: jfrog-releasebundlev2
- name: ReleaseBundleV2Request
  property_count: 5
  slug: jfrog-releasebundlev2request
- name: ReleaseBundleV2Summary
  property_count: 6
  slug: jfrog-releasebundlev2summary
- name: ReplicationConfig
  property_count: 12
  slug: jfrog-replication-config
- name: ReplicationConfig
  property_count: 12
  slug: jfrog-replicationconfig
- name: RepositoryConfiguration
  property_count: 15
  slug: jfrog-repository-configuration
- name: RepositoryListItem
  property_count: 5
  slug: jfrog-repository-list-item
- name: JFrog Repository
  property_count: 20
  slug: jfrog-repository
- name: RepositoryConfiguration
  property_count: 15
  slug: jfrog-repositoryconfiguration
- name: RepositoryListItem
  property_count: 5
  slug: jfrog-repositorylistitem
- name: Run
  property_count: 10
  slug: jfrog-run
- name: ScriptRequest
  property_count: 3
  slug: jfrog-script-request
- name: Script
  property_count: 5
  slug: jfrog-script
- name: ScriptRequest
  property_count: 3
  slug: jfrog-scriptrequest
- name: SearchResult
  property_count: 1
  slug: jfrog-search-result
- name: SearchResult
  property_count: 1
  slug: jfrog-searchresult
- name: JFrog Security Vulnerability
  property_count: 16
  slug: jfrog-security-vulnerability
- name: Step
  property_count: 9
  slug: jfrog-step
- name: StorageSummary
  property_count: 3
  slug: jfrog-storage-summary
- name: StorageSummary
  property_count: 3
  slug: jfrog-storagesummary
- name: SystemHealth
  property_count: 2
  slug: jfrog-system-health
- name: SystemVersion
  property_count: 4
  slug: jfrog-system-version
- name: SystemHealth
  property_count: 2
  slug: jfrog-systemhealth
- name: SystemVersion
  property_count: 4
  slug: jfrog-systemversion
- name: TokenInfo
  property_count: 8
  slug: jfrog-token-info
- name: TokenResponse
  property_count: 7
  slug: jfrog-token-response
- name: TokenInfo
  property_count: 9
  slug: jfrog-tokeninfo
- name: TokenResponse
  property_count: 7
  slug: jfrog-tokenresponse
- name: UpdateRequest
  property_count: 12
  slug: jfrog-update-request
- name: Update
  property_count: 10
  slug: jfrog-update
- name: UpdateUserRequest_2
  property_count: 5
  slug: jfrog-update-user-request-2
- name: UpdateUserRequest
  property_count: 7
  slug: jfrog-update-user-request
- name: UpdateRequest
  property_count: 12
  slug: jfrog-updaterequest
- name: UpdateUserRequest
  property_count: 7
  slug: jfrog-updateuserrequest
- name: JFrog Platform User
  property_count: 11
  slug: jfrog-user
- name: UserSummary
  property_count: 4
  slug: jfrog-user-summary
- name: UserSummary
  property_count: 4
  slug: jfrog-usersummary
- name: VerificationResult
  property_count: 6
  slug: jfrog-verification-result
- name: VerificationResult
  property_count: 6
  slug: jfrog-verificationresult
- name: ViolationsResponse
  property_count: 2
  slug: jfrog-violations-response
- name: ViolationsResponse
  property_count: 2
  slug: jfrog-violationsresponse
- name: Vulnerability
  property_count: 9
  slug: jfrog-vulnerability
- name: Watch
  property_count: 3
  slug: jfrog-watch
- name: WebhookRequest
  property_count: 7
  slug: jfrog-webhook-request
- name: Webhook
  property_count: 7
  slug: jfrog-webhook
- name: WebhookRequest
  property_count: 7
  slug: jfrog-webhookrequest
- name: WorkerRequest
  property_count: 7
  slug: jfrog-worker-request
- name: JFrog Worker
  property_count: 9
  slug: jfrog-worker
- name: WorkerRequest
  property_count: 7
  slug: jfrog-workerrequest
json_structures:
- name: Jfrog Structure
  property_count: 0
  slug: jfrog-structure
jsonld:
- class_count: 9
  name: Jfrog Context
  property_count: 13
  slug: jfrog-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: JFrog
nav: Providers
network: true
overview: 'JFrog publishes 53 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Tokens API, Artifacts & Storage API, Audit API, and 50 more. Tagged areas include Artifactory, CI/CD, Container Registry, Developer Tools, and DevOps.


  The JFrog catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  JFrog''s developer surface includes changelog, authentication, documentation, getting-started guide, engineering blog, support, signup flow, and 87 more developer resources.'
plans:
- name: Jfrog Plans Pricing
  plan_count: 3
  slug: jfrog-plans-pricing
- name: Jfrog Price Estimates
  plan_count: 0
  slug: jfrog-price-estimates
random_paper: 8
rate_limits:
- limit_count: 3
  name: Jfrog Rate Limits
  slug: jfrog-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: JFrog — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: jfrog-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: JFrog API Rules
  rule_count: 69
  severity_counts:
    error: 52
    hint: 0
    info: 2
    warn: 15
  slug: jfrog-rules
score:
  band: exemplar
  composite: 74.4
  coverage:
    artifact_dirs: 36
    catalog_earned: 96.0
    catalog_earned_first_party: 24.0
    catalog_gap: 19.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.9
  facets:
    access_clarity: 75.0
    contract_governance: 31.8
    contract_quality: 65.7
    developer_ergonomics: 78.0
    discoverability: 89.3
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 70.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 53
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/jfrog/jfrog-2026-06-20T183730.png
security:
- kind: authentication
  name: Jfrog Authentication
  slug: jfrog-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Jfrog Domain Security
  slug: jfrog-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jfrog Vulnerability Disclosure
  slug: jfrog-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: jfrog-package-safety-and-download
  slug: jfrog-package-safety-and-download
- name: jfrog
  slug: jfrog
slug: jfrog
tags:
- Artifactory
- CI/CD
- Container Registry
- Developer Tools
- DevOps
- MLOps
- Package Management
- Security
- Software Supply Chain
website: https://jfrog.com/
---
