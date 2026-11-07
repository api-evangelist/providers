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
  - scopes
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 133
  human_in_the_loop: 10
  name: Snyk Agentic Access
  operation_count: 280
  slug: snyk-agentic-access
  summary_line: 280 operations · 133 acting · 10 human-in-the-loop
api_count: 3
apis:
- description: Manages Snyk Apps, the OAuth2-based extensibility surface that lets third-party applications act on behalf of Snyk users, organizations, and groups.
  name: Snyk REST API - Apps (OAuth)
  slug: rest-apps
- description: The original Snyk REST API. Still in use for project import, monitor, test, and certain reporting endpoints not yet ported to the dated REST API. Subject to end-of-life migration; new integrations sho
  name: Snyk V1 API (Legacy)
  slug: v1
- description: 'Snyk''s first-party Model Context Protocol server, shipped inside the Snyk CLI and run locally over stdio (`npx -y snyk@latest mcp -t stdio`). Twelve security tools - code, dependency, container, IaC, '
  name: Snyk MCP Server (Snyk Studio)
  slug: mcp
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The AiBom API from Snyk — 4 operation(s) for aibom.
  name: Snyk AiBom API
  phrasing_intents:
  - id: getAiBomJob
    intent: Check the status of an AI-BOM job
    question: Has my AI bill of materials finished generating yet?
  - id: createAiBom
    intent: Start generating an AI-BOM
    question: How do I generate an AI bill of materials for my code?
  - id: createAndUploadAiBom
    intent: Create an AI-BOM from a file bundle and store it
    question: Can I upload a file bundle and have Snyk build and save an AI-BOM for a repo?
  - id: getAiBom
    intent: Get a finished AI-BOM
    question: Where do I download the AI-BOM once its job is done?
  phrasing_ops: 4
  slug: snyk-aibom-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Apps API from Snyk — 20 operation(s) for apps.
  name: Snyk Apps API
  phrasing_intents:
  - id: getAppInstallsForGroup
    intent: List Snyk Apps installed for a group
    question: Which Snyk Apps are installed at the group level?
  - id: createGroupAppInstall
    intent: Install a Snyk App for a group
    question: How do I install a client-credentials Snyk App across a whole group?
  - id: deleteGroupAppInstallById
    intent: Revoke a Snyk App install from a group
    question: How do I uninstall a Snyk App from a group so it loses access?
  - id: updateGroupAppInstallSecret
    intent: Manage the client secret of a group app install
    question: How do I rotate the client secret for a non-interactive app installed on my group?
  - id: getAppBots
    intent: List app bots authorized to an org (deprecated)
    question: Which app bots are authorized on my Snyk organization?
  - id: deleteAppBot
    intent: Revoke an app bot's authorization (deprecated)
    question: How do I revoke an app bot from my organization?
  - id: getApps
    intent: List apps created by an org (deprecated endpoint)
    question: Is there an older endpoint that lists the apps my org created?
  - id: createApp
    intent: Create an app for an org (deprecated endpoint)
    question: Can I still create an app with name, redirect URIs and scopes through the old apps endpoint?
  phrasing_ops: 28
  slug: snyk-apps-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Asset API from Snyk — 6 operation(s) for asset.
  name: Snyk Asset API
  phrasing_intents:
  - id: deleteAliasesInGroup
    intent: Bulk remove repository aliases in a group
    question: How do I detach aliased repo URLs from their canonical asset in my group?
  - id: listRepositoryAliasesInGroup
    intent: List repository URL aliases in a group
    question: Which alternate repository URLs are aliased to assets across my group?
  - id: createAliasInGroup
    intent: Add a repository URL alias at group level
    question: How do I tell Snyk that two repo URLs in my group are the same repository?
  - id: listAssets
    intent: Search a group's assets with filters
    question: How can I find repositories, images and other assets in my Snyk group?
  - id: getAsset
    intent: Get an asset by its ID
    question: Where can I see everything Snyk knows about one asset?
  - id: updateAsset
    intent: Update an asset's attributes
    question: How do I change attributes on an asset in my group?
  - id: listRelatedAssets
    intent: List assets related to an asset
    question: What other assets are connected to this repository or image?
  - id: listAssetProjects
    intent: List Snyk projects linked to an asset
    question: Which Snyk projects scan this asset?
  phrasing_ops: 11
  slug: snyk-asset-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Audit Logs API from Snyk — 2 operation(s) for audit logs.
  name: Snyk Audit Logs API
  phrasing_intents:
  - id: listGroupAuditLogs
    intent: Search a group's audit logs
    question: Who changed what across my Snyk group last week?
  - id: listOrgAuditLogs
    intent: Search an organization's audit logs
    question: What happened in my organization's audit trail yesterday?
  phrasing_ops: 2
  slug: snyk-audit-logs-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The BrokerConnections API from Snyk — 7 operation(s) for brokerconnections.
  name: Snyk BrokerConnections API
  phrasing_intents:
  - id: listBrokerConnectionsForOrg
    intent: List Broker connections used by an organization
    question: Which Broker connections are wired into my Snyk organization?
  - id: getBrokerConnectionIntegrations
    intent: List integrations using a Broker connection
    question: Which integrations depend on a particular Broker connection?
  - id: createBrokerConnectionIntegration
    intent: Point an org's integration at a Broker connection
    question: How do I make an organization's integration use a specific Broker connection?
  - id: deleteBrokerConnectionIntegration
    intent: Detach an integration from a Broker connection
    question: How do I stop one org integration from using a Broker connection?
  - id: deleteBrokerConnections
    intent: Delete all Broker connections on a deployment
    question: How do I wipe every Broker connection from a deployment at once?
  - id: listBrokerConnections
    intent: List Broker connections in a deployment
    question: What Broker connections are configured on a given Broker deployment?
  - id: createBrokerConnection
    intent: Create a Broker connection on a deployment
    question: How do I add a new Broker connection to a deployment?
  - id: deleteBrokerConnection
    intent: Delete a single Broker connection
    question: How do I delete just one Broker connection from a deployment?
  phrasing_ops: 12
  slug: snyk-brokerconnections-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The BrokerContexts API from Snyk — 5 operation(s) for brokercontexts.
  name: Snyk BrokerContexts API
  phrasing_intents:
  - id: listConnectionContexts
    intent: List Broker contexts for a connection
    question: Which Broker contexts are attached to a given Broker connection?
  - id: deleteBrokerContext
    intent: Delete a Broker context
    question: Can I remove a Broker context I no longer use?
  - id: getConnectionContext
    intent: Get a Broker context by ID
    question: Can I look up a single Broker context by its ID?
  - id: updateBrokerContext
    intent: Update a Broker context
    question: Can I change the settings of an existing Broker context?
  - id: updateBrokerContextIntegration
    intent: Associate an integration with a Broker context
    question: How do I link an integration to a Broker context?
  - id: deleteBrokerContextIntegration
    intent: Detach an integration from a Broker context
    question: Can I unlink an integration from a Broker context without deleting the context?
  - id: listDeploymentContexts
    intent: List Broker contexts for a deployment
    question: Which contexts belong to a particular Broker deployment?
  - id: createBrokerContext
    intent: Create a Broker context for a deployment
    question: How do I create a new Broker context on a deployment?
  phrasing_ops: 8
  slug: snyk-brokercontexts-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The BrokerDeployments API from Snyk — 3 operation(s) for brokerdeployments.
  name: Snyk BrokerDeployments API
  phrasing_intents:
  - id: listBrokerDeploymentsForTenant
    intent: List all Broker deployments in a tenant
    question: Which Broker deployments exist across my whole tenant?
  - id: listBrokerDeployments
    intent: List Broker deployments for one install
    question: What deployments belong to a specific Broker install?
  - id: createBrokerDeployment
    intent: Create a Broker deployment for an install
    question: How do I create a new Universal Broker deployment?
  - id: deleteBrokerDeployment
    intent: Delete a Broker deployment
    question: How do I tear down a Broker deployment?
  - id: updateBrokerDeployment
    intent: Update a Broker deployment
    question: How do I change the settings of an existing Broker deployment?
  phrasing_ops: 5
  slug: snyk-brokerdeployments-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Catalog Resource API from Snyk — 1 operation(s) for catalog resource.
  name: Snyk Catalog Resource API
  phrasing_intents:
  - id: listLearnCatalog
    intent: List Snyk Learn catalog resources
    question: What security training lessons are in the Snyk Learn catalog?
  phrasing_ops: 1
  slug: snyk-catalog-resource-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Cloud API from Snyk — 6 operation(s) for cloud.
  name: Snyk Cloud API
  phrasing_intents:
  - id: listEnvironments
    intent: List cloud environments for an organization
    question: Which cloud environments has my Snyk org connected?
  - id: createEnvironment
    intent: Connect a new cloud environment and scan it
    question: How do I connect a cloud account to Snyk as a new environment?
  - id: deleteEnvironment
    intent: Delete a cloud environment
    question: How do I disconnect a cloud environment from Snyk?
  - id: updateEnvironment
    intent: Update a cloud environment
    question: How do I edit the settings of a connected cloud environment?
  - id: getPermissions
    intent: Generate the IaC template granting Snyk cloud access
    question: What permissions does Snyk need in my cloud account, and can it give me a template?
  - id: listResources
    intent: List cloud resources Snyk has discovered
    question: What cloud resources has Snyk found in my environments?
  - id: listScan
    intent: List cloud scans for an organization
    question: Which cloud scans have run for my organization?
  - id: createScan
    intent: Trigger a new scan of a cloud environment
    question: How do I rescan a cloud environment on demand?
  phrasing_ops: 9
  slug: snyk-cloud-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Collection API from Snyk — 3 operation(s) for collection.
  name: Snyk Collection API
  phrasing_intents:
  - id: getCollections
    intent: List an organization's project collections
    question: What collections does my org have, with their issue and project counts?
  - id: createCollection
    intent: Create a project collection
    question: How do I group Snyk projects into a new collection?
  - id: deleteCollection
    intent: Delete a collection
    question: How do I delete a collection I no longer need?
  - id: getCollection
    intent: Get a single collection
    question: Where can I see the details of one collection?
  - id: updateCollection
    intent: Rename or edit a collection
    question: How do I rename an existing collection?
  - id: deleteProjectsCollection
    intent: Remove projects from a collection
    question: How do I take projects out of a collection without deleting them?
  - id: getProjectsOfCollection
    intent: List the projects in a collection
    question: Which projects are inside a given collection?
  - id: updateCollectionWithProjects
    intent: Add projects to a collection
    question: How do I add projects to an existing collection?
  phrasing_ops: 8
  slug: snyk-collection-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The ContainerRegistryImportPolicy API from Snyk — 3 operation(s) for containerregistryimportpolicy.
  name: Snyk ContainerRegistryImportPolicy API
  phrasing_intents:
  - id: deleteContainerRegistryImportPolicy
    intent: Delete a container registry import policy
    question: How do I remove the import policy from a registry integration?
  - id: getContainerRegistryImportPolicy
    intent: Get a container registry import policy
    question: What import policy is set on my container registry integration?
  - id: updateContainerRegistryImportPolicy
    intent: Update a container registry import policy
    question: How do I change the rules in an existing registry import policy?
  - id: createContainerRegistryImportPolicy
    intent: Create a container registry import policy
    question: How do I set up an import policy for a container registry integration?
  - id: createContainerRegistryImportPolicyDryRun
    intent: Start a dry run of a registry import policy
    question: Can I test what an import policy would import before applying it?
  - id: getDryRunJob
    intent: Get the status and results of a policy dry run
    question: Has my import policy dry run finished, and what did it find?
  phrasing_ops: 6
  slug: snyk-containerregistryimportpolicy-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Custom Base Images API from Snyk — 2 operation(s) for custom base images.
  name: Snyk Custom Base Images API
  phrasing_intents:
  - id: getCustomBaseImages
    intent: List custom base images
    question: Which custom base images are registered for my org or group?
  - id: createCustomBaseImage
    intent: Mark a container project as a custom base image
    question: How do I register my own base image so Snyk recommends upgrades to it?
  - id: deleteCustomBaseImage
    intent: Delete a custom base image
    question: How do I stop treating an image as a custom base image?
  - id: getCustomBaseImage
    intent: Get a custom base image
    question: Where can I see one custom base image's settings?
  - id: updateCustomBaseImage
    intent: Update a custom base image
    question: How do I exclude a custom base image from recommendations?
  phrasing_ops: 5
  slug: snyk-custom-base-images-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The DeploymentCredentials API from Snyk — 2 operation(s) for deploymentcredentials.
  name: Snyk DeploymentCredentials API
  phrasing_intents:
  - id: listDeploymentCredentials
    intent: List credentials for a Broker deployment
    question: Which credentials are stored on a Broker deployment?
  - id: createDeploymentCredential
    intent: Add a credential to a Broker deployment
    question: How do I add a new credential to a Broker deployment?
  - id: deleteDeploymentCredential
    intent: Delete a Broker deployment credential
    question: Can I remove a credential from a Broker deployment?
  - id: getDeploymentCredential
    intent: Get one Broker deployment credential
    question: Can I look up a single credential on a Broker deployment?
  - id: updateDeploymentCredential
    intent: Update a Broker deployment credential
    question: Can I update an existing Broker deployment credential in place?
  phrasing_ops: 5
  slug: snyk-deploymentcredentials-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Export API from Snyk — 6 operation(s) for export.
  name: Snyk Export API
  phrasing_intents:
  - id: createGroupExport
    intent: Start a data export for a group
    question: Can I export report data for my whole Snyk group?
  - id: getGroupExport
    intent: Get the results of a group export
    question: Where do I download the results of a finished group export?
  - id: getGroupExportJobStatus
    intent: Check a group export job's status
    question: Is my group export finished yet?
  - id: createExport
    intent: Start a data export for an organization
    question: Can I export report data for a single organization?
  - id: getExport
    intent: Get the results of an organization export
    question: Where do I get the output of an org export once it's done?
  - id: getExportJobStatus
    intent: Check an organization export job's status
    question: Has my organization export finished running?
  phrasing_ops: 6
  slug: snyk-export-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Findings API from Snyk — 1 operation(s) for findings.
  name: Snyk Findings API
  phrasing_intents:
  - id: listFindings
    intent: List findings from a test
    question: What vulnerabilities and policy breaches did my Snyk test find?
  phrasing_ops: 1
  slug: snyk-findings-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Group API from Snyk — 1 operation(s) for group.
  name: Snyk Group API
  phrasing_intents:
  - id: getGroup
    intent: Get a group's details
    question: Can I look up the details of a Snyk group by its ID?
  phrasing_ops: 1
  slug: snyk-group-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Groups API from Snyk — 7 operation(s) for groups.
  name: Snyk Groups API
  phrasing_intents:
  - id: listGroups
    intent: List the groups I belong to
    question: Which Snyk groups am I a member of?
  - id: listGroupMemberships
    intent: List memberships in a group
    question: Who are the members of my group and what roles do they have?
  - id: createGroupMembership
    intent: Add a user to a group with a role
    question: How do I add a user to a group with a specific role?
  - id: deleteGroupMembership
    intent: Remove a membership from a group
    question: Can I remove a user's membership from a group?
  - id: updateGroupUserMembership
    intent: Change a user's role in a group membership
    question: Can I change the role on someone's existing group membership?
  - id: listGroupUserOrgMemberships
    intent: List a group user's org memberships
    question: Which organizations in my group does a particular user belong to?
  - id: listGroupSsoConnections
    intent: List a group's SSO connections
    question: Which SSO connections are configured for my group?
  - id: listGroupSsoConnectionUsers
    intent: List users signing in through an SSO connection
    question: Which users log in through a specific SSO connection?
  phrasing_ops: 9
  slug: snyk-groups-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The IacSettings API from Snyk — 2 operation(s) for iacsettings.
  name: Snyk IacSettings API
  phrasing_intents:
  - id: getIacSettingsForGroup
    intent: Get a group's Infrastructure as Code settings
    question: What Infrastructure as Code settings are applied across my Snyk group?
  - id: updateIacSettingsForGroup
    intent: Update a group's Infrastructure as Code settings
    question: Can I change IaC settings for every org in a group at once?
  - id: getIacSettingsForOrg
    intent: Get an org's Infrastructure as Code settings
    question: What Infrastructure as Code settings does one organization use?
  - id: updateIacSettingsForOrg
    intent: Update an org's Infrastructure as Code settings
    question: Can I change the IaC settings for a single organization?
  phrasing_ops: 4
  slug: snyk-iacsettings-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Integrations API from Snyk — 3 operation(s) for integrations.
  name: Snyk Integrations API
  phrasing_intents:
  - id: listIntegrations
    intent: List an organization's integrations
    question: Which integrations are set up in my Snyk organization?
  - id: createIntegration
    intent: Create an integration with credentials
    question: How do I add a new integration with credentials to my org?
  - id: deleteIntegration
    intent: Permanently delete a container registry integration
    question: How do I permanently remove a container registry integration?
  - id: getIntegration
    intent: Get a single integration
    question: Where can I see the details of one integration?
  - id: updateIntegration
    intent: Update an integration's name or credentials
    question: How do I rotate the credentials on an existing integration?
  - id: getIntegrationSettings
    intent: Get an integration's settings
    question: What settings are configured on one of my integrations?
  - id: updateIntegrationSettings
    intent: Update an integration's settings
    question: How do I enable container application scanning on an integration?
  phrasing_ops: 7
  slug: snyk-integrations-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Inventory Assets API from Snyk — 30 operation(s) for inventory assets.
  name: Snyk Inventory Assets API
  phrasing_intents:
  - id: listAssetsGroup
    intent: List or filter inventory assets across a group
    question: Can I see every asset in my Snyk group's inventory in one list?
  - id: updateAssetsBulkGroup
    intent: Bulk update up to 100 assets in a group
    question: Can I relabel many assets in a group's inventory in one request?
  - id: getFilterFieldsGroup
    intent: List fields usable for filtering group assets
    question: Which fields can I use in an RSQL filter on my group's asset inventory?
  - id: getFilterValuesGroup
    intent: Suggest values for a group asset filter field
    question: What distinct values exist for a given asset filter field across my group?
  - id: getGroupFieldsGroup
    intent: List fields for grouping assets in a group
    question: Which fields can I group my Snyk group's assets by?
  - id: getGroupValuesGroup
    intent: Count group assets by each value of a field
    question: How many assets in my group fall under each value of a grouping field?
  - id: createAssetSearchGroup
    intent: Start an async asset search in a group
    question: Can I kick off a background asset search across a whole group?
  - id: getAssetSearchResultsGroup
    intent: Get results of a group asset search
    question: Where do I pick up the results of an asset search I started for my group?
  phrasing_ops: 36
  slug: snyk-inventory-assets-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Invites API from Snyk — 2 operation(s) for invites.
  name: Snyk Invites API
  phrasing_intents:
  - id: listOrgInvitation
    intent: List pending invitations to an organization
    question: Who has been invited to my organization but hasn't accepted yet?
  - id: createOrgInvitation
    intent: Invite a user to an organization
    question: How do I invite a teammate to my Snyk organization by email?
  - id: deleteOrgInvitation
    intent: Cancel a pending organization invitation
    question: Can I revoke an invite I sent before it's accepted?
  phrasing_ops: 3
  slug: snyk-invites-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Issues API from Snyk — 6 operation(s) for issues.
  name: Snyk Issues API
  phrasing_intents:
  - id: listGroupIssues
    intent: List security issues across a group
    question: What open critical vulnerabilities exist across my whole Snyk group?
  - id: getGroupIssueByIssueID
    intent: Get one issue at group level
    question: Where can I see full details of a vulnerability using my group's scope?
  - id: listOrgIssues
    intent: List security issues in an organization
    question: What vulnerabilities does my organization have open right now?
  - id: getOrgIssueByIssueID
    intent: Get one issue in an organization
    question: How do I pull up the details of one vulnerability in my org?
  - id: listIssuesForManyPurls
    intent: Look up vulnerabilities for a batch of packages
    question: Can I check a whole list of package URLs for known vulnerabilities in one request?
  - id: getIssuesPerPurl
    intent: List vulnerabilities for one package version
    question: Is a specific package version known to be vulnerable?
  phrasing_ops: 6
  slug: snyk-issues-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The LanguagesSettings API from Snyk — 2 operation(s) for languagessettings.
  name: Snyk LanguagesSettings API
  phrasing_intents:
  - id: getOrgLanguagesSettings
    intent: Get an org's open source language settings
    question: What open source language settings are configured for my organization?
  - id: updateOrgLanguagesSettings
    intent: Update one language's settings for an org
    question: Can I change the open source settings for a single language in my org?
  phrasing_ops: 2
  slug: snyk-languagessettings-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Learn assignment API from Snyk — 2 operation(s) for learn assignment.
  name: Snyk Learn assignment API
  phrasing_intents:
  - id: deleteOrgAssignments
    intent: Bulk delete Learn assignments (DELETE)
    question: How do I remove several training assignments with a DELETE request?
  - id: listOrgAssignments
    intent: List Snyk Learn assignments in an organization
    question: What security training has been assigned to people in my org?
  - id: updateOrgAssignments
    intent: Change the due date of Learn assignments
    question: How do I extend the deadline on assigned security training?
  - id: createOrgAssignments
    intent: Assign Snyk Learn lessons to users in bulk
    question: How do I assign security lessons to my whole team at once?
  - id: deleteOrgAssignmentsBulk
    intent: Bulk delete Learn assignments via POST
    question: Is there a POST bulk_delete endpoint for clients that can't send a DELETE body?
  phrasing_ops: 5
  slug: snyk-learn-assignment-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Learn progress API from Snyk — 2 operation(s) for learn progress.
  name: Snyk Learn progress API
  phrasing_intents:
  - id: getCatalogProgress
    intent: Get aggregate Snyk Learn progress per lesson
    question: How many people in my org have completed each security lesson?
  - id: getUsersProgress
    intent: Get individual users' Snyk Learn progress
    question: Which developers have finished their assigned security training?
  phrasing_ops: 2
  slug: snyk-learn-progress-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The OpenSourceSettings API from Snyk — 4 operation(s) for opensourcesettings.
  name: Snyk OpenSourceSettings API
  phrasing_intents:
  - id: getOpenSourceSettingsForOrg
    intent: Get an organization's Open Source settings
    question: What Open Source scanning settings apply to my Snyk org?
  - id: deleteOpensourceBrokerSettingForGroup
    intent: Turn off the open source broker for a group
    question: How do I disable the open source broker for my group?
  - id: getOpensourceBrokerSettingForGroup
    intent: Check if the open source broker is on for a group
    question: Is the open source broker enabled across my group?
  - id: enableOpensourceBrokerForGroup
    intent: Enable the open source broker for a group
    question: How do I turn on the open source broker for a whole group?
  - id: deleteOpensourceBrokerSettingForOrg
    intent: Turn off the open source broker for an organization
    question: How do I disable the open source broker in a single organization?
  - id: getOpensourceBrokerSetting
    intent: Check if the open source broker is on for an org
    question: Is the open source broker enabled for this organization?
  - id: enableOpensourceBrokerForOrg
    intent: Enable the open source broker for an organization
    question: How do I turn on the open source broker for just one org?
  - id: getOpensourceBrokerEcosystemSettingsForOrg
    intent: Get an org's broker settings for one ecosystem
    question: What Broker settings does my org have for npm or Maven packages?
  phrasing_ops: 9
  slug: snyk-opensourcesettings-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Orgs API from Snyk — 5 operation(s) for orgs.
  name: Snyk Orgs API
  phrasing_intents:
  - id: listOrgsInGroup
    intent: List the organizations in a group
    question: Which organizations belong to my Snyk group?
  - id: listOrgs
    intent: List organizations I can access
    question: Which organizations do I have access to?
  - id: getOrg
    intent: Get an organization's details
    question: What are the full details of one of my organizations?
  - id: updateOrg
    intent: Update an organization's details
    question: How do I rename an organization?
  - id: listOrgMemberships
    intent: List memberships in an organization
    question: Who belongs to my organization and with what role?
  - id: createOrgMembership
    intent: Add a user to an organization with a role
    question: Can I add an existing user straight into an organization with a role, without an invite?
  - id: deleteOrgMembership
    intent: Remove a user's organization membership
    question: Can I remove someone from my organization?
  - id: updateOrgMembership
    intent: Change a user's role in an organization
    question: Can I change the role on an existing org membership?
  phrasing_ops: 8
  slug: snyk-orgs-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Package API from Snyk — 1 operation(s) for package.
  name: Snyk Package API
  phrasing_intents:
  - id: getPackage
    intent: Get a package's metadata and health
    question: How healthy is an open source package before I add it as a dependency?
  phrasing_ops: 1
  slug: snyk-package-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Package Version API from Snyk — 1 operation(s) for package version.
  name: Snyk Package Version API
  phrasing_intents:
  - id: getPackageVersion
    intent: Get health metadata for a package version
    question: Is a specific version of an npm or PyPI package healthy and secure?
  phrasing_ops: 1
  slug: snyk-package-version-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Policies API from Snyk — 5 operation(s) for policies.
  name: Snyk Policies API
  phrasing_intents:
  - id: listGroupPolicies
    intent: List a group's policies
    question: Which policies are defined at the group level?
  - id: createGroupPolicy
    intent: Create a group-level policy
    question: Can I create a policy that applies across a whole group?
  - id: deleteGroupPolicy
    intent: Delete a group-level policy
    question: Can I remove a policy that was set at the group level?
  - id: updateGroupPolicy
    intent: Update a group-level policy
    question: Can I edit an existing group-level policy?
  - id: getOrgPolicies
    intent: List or search an organization's ignore policies
    question: Which ignore policies does my organization have for Code Consistent Ignores?
  - id: createOrgPolicy
    intent: Create an organization-level policy
    question: Can I create an ignore policy for one organization?
  - id: deleteOrgPolicy
    intent: Delete an organization policy
    question: Can I delete an org-level ignore policy I no longer need?
  - id: getOrgPolicy
    intent: Get one organization policy by ID
    question: Can I look up a single org-level policy by its ID?
  phrasing_ops: 10
  slug: snyk-policies-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Projects API from Snyk — 2 operation(s) for projects.
  name: Snyk Projects API
  phrasing_intents:
  - id: listOrgProjects
    intent: List an organization's Snyk projects
    question: What projects does my Snyk organization monitor?
  - id: deleteOrgProject
    intent: Delete a project
    question: How do I delete a Snyk project I no longer want monitored?
  - id: getOrgProject
    intent: Get a project by ID
    question: Where can I see one project's details and latest issue counts?
  - id: updateOrgProject
    intent: Update a project's settings or attributes
    question: How do I change a project's tags or business criticality?
  phrasing_ops: 4
  slug: snyk-projects-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Pull Request Templates API from Snyk — 1 operation(s) for pull request templates.
  name: Snyk Pull Request Templates API
  phrasing_intents:
  - id: deletePullRequestTemplate
    intent: Delete a group's pull request template
    question: How do I go back to Snyk's default pull request template?
  - id: getPullRequestTemplate
    intent: Get a group's pull request template
    question: What template does Snyk use for fix pull requests in my group?
  - id: createOrUpdatePullRequestTemplate
    intent: Set a group's pull request template
    question: How do I customize the title and description of Snyk fix PRs for every org in my group?
  phrasing_ops: 3
  slug: snyk-pull-request-templates-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The SastSettings API from Snyk — 1 operation(s) for sastsettings.
  name: Snyk SastSettings API
  phrasing_intents:
  - id: getSastSettings
    intent: Get an org's SAST settings
    question: Is Snyk Code static analysis turned on for my organization?
  - id: updateOrgSastSettings
    intent: Enable or disable Snyk Code for an org
    question: Can I switch Snyk Code on for an organization programmatically?
  phrasing_ops: 2
  slug: snyk-sastsettings-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The SBOM API from Snyk — 4 operation(s) for sbom.
  name: Snyk SBOM API
  phrasing_intents:
  - id: getSbom
    intent: Get a project's SBOM document
    question: Can I download a software bill of materials for one of my Snyk projects?
  - id: createSbomTestRun
    intent: Test an SBOM document for vulnerabilities
    question: Can I upload an SBOM and have its components checked for known vulnerabilities?
  - id: getSbomTestStatus
    intent: Check an SBOM test run's status
    question: Has my SBOM test run finished yet?
  - id: getSbomTestResult
    intent: Get the findings of an SBOM test run
    question: What vulnerabilities did my SBOM test find?
  phrasing_ops: 4
  slug: snyk-sbom-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Slack API from Snyk — 2 operation(s) for slack.
  name: Snyk Slack API
  phrasing_intents:
  - id: listChannels
    intent: List Slack channels the Snyk Slack App can access
    question: Which Slack channels can the Snyk Slack App post to for my org?
  - id: getChannelNameById
    intent: Look up a Slack channel's name by ID
    question: What is the name of the Slack channel with a given channel ID?
  phrasing_ops: 2
  slug: snyk-slack-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The SlackSettings API from Snyk — 3 operation(s) for slacksettings.
  name: Snyk SlackSettings API
  phrasing_intents:
  - id: deleteSlackDefaultNotificationSettings
    intent: Remove the Slack App integration
    question: Can I remove the Slack App integration from my organization?
  - id: getSlackDefaultNotificationSettings
    intent: Get default Slack notification settings
    question: What are the default Slack notification settings for my Slack app bot?
  - id: createSlackDefaultNotificationSettings
    intent: Create default Slack notification settings
    question: How do I set up default Slack notifications for my organization?
  - id: getSlackProjectNotificationSettingsCollection
    intent: List per-project Slack notification overrides
    question: Which projects override the default Slack notification settings?
  - id: deleteSlackProjectNotificationSettings
    intent: Remove a project's Slack settings override
    question: Can I make a project fall back to the default Slack settings again?
  - id: updateSlackProjectNotificationSettings
    intent: Update a project's Slack notification override
    question: Can I change an existing project's Slack override settings?
  - id: createSlackProjectNotificationSettings
    intent: Create a Slack settings override for a project
    question: Can one project send Slack notifications to a different channel than the default?
  phrasing_ops: 7
  slug: snyk-slacksettings-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Targets API from Snyk — 2 operation(s) for targets.
  name: Snyk Targets API
  phrasing_intents:
  - id: getOrgsTargets
    intent: List an organization's targets
    question: Which repositories and other targets are imported into my organization?
  - id: deleteOrgsTarget
    intent: Delete a target
    question: Can I delete a target I no longer want monitored?
  - id: getOrgsTarget
    intent: Get one target by ID
    question: Can I look up the details of one target by its ID?
  phrasing_ops: 3
  slug: snyk-targets-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The TenantRole API from Snyk — 2 operation(s) for tenantrole.
  name: Snyk TenantRole API
  phrasing_intents:
  - id: listTenantRoles
    intent: List roles available in a tenant
    question: Which roles are available in my tenant?
  - id: createTenantRole
    intent: Create a custom tenant role
    question: How do I create a custom role for my tenant?
  - id: deleteTenantRole
    intent: Delete a custom tenant role
    question: Can I delete a custom role from my tenant?
  - id: getTenantRole
    intent: Get a tenant role and its permissions
    question: What permissions does a particular tenant role grant?
  - id: updateTenantRole
    intent: Update a custom tenant role
    question: Can I change the permissions on an existing custom tenant role?
  phrasing_ops: 5
  slug: snyk-tenantrole-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Tenants API from Snyk — 4 operation(s) for tenants.
  name: Snyk Tenants API
  phrasing_intents:
  - id: listTenants
    intent: List tenants I belong to
    question: Which Snyk tenants am I a member of?
  - id: getTenant
    intent: Get a tenant's details
    question: What are the full details of my tenant?
  - id: updateTenant
    intent: Update a tenant's details
    question: Can I rename my tenant?
  - id: getTenantMemberships
    intent: List memberships in a tenant
    question: Who are the members of my tenant?
  - id: deleteTenantMembership
    intent: Remove a user's tenant membership
    question: Can I remove a single user from my tenant?
  - id: updateTenantMembership
    intent: Change a user's role in a tenant
    question: Can I give a tenant member a new role?
  phrasing_ops: 6
  slug: snyk-tenants-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Tests API from Snyk — 3 operation(s) for tests.
  name: Snyk Tests API
  phrasing_intents:
  - id: getJob
    intent: Check the progress of a test job
    question: Is the Snyk test I started through the API still running?
  - id: createTest
    intent: Start a new open source or code test
    question: Can I run an open source or code analysis test through the API?
  - id: getTest
    intent: Get a completed test's summary
    question: What was the outcome of a finished Snyk test?
  phrasing_ops: 3
  slug: snyk-tests-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Users API from Snyk — 3 operation(s) for users.
  name: Snyk Users API
  phrasing_intents:
  - id: updateUser
    intent: Remove a user's membership from a group
    question: Can I take a user out of a group by setting their membership to null?
  - id: getUser
    intent: Get a user in an organization by ID
    question: Can I look up a summary of a user in my organization?
  - id: getSelf
    intent: Get my own user details
    question: Which Snyk user is my API token authenticated as?
  phrasing_ops: 3
  slug: snyk-users-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: oauth2
  name: Snyk Oauth2 API
  phrasing_intents:
  - id: getOauth2Authorize
    intent: Start the OAuth authorization code flow
    question: How do I send a user to authorize my app against their Snyk organizations?
  - id: postToken
    intent: Exchange an authorization code for an access token
    question: What do I do with the authorization code once the user is redirected back to my app?
  - id: postRevoke
    intent: Revoke a leaked refresh token
    question: How can I invalidate a refresh token that was accidentally leaked?
  phrasing_ops: 3
  slug: snyk-oauth2-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Access Requests API from Snyk — 1 operation(s) for access requests.
  name: Snyk Access Requests API
  phrasing_intents:
  - id: getAccessRequests
    intent: List my access requests
    question: Which organization access requests have I made in Snyk?
  phrasing_ops: 1
  slug: snyk-access-requests-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Container Image API from Snyk — 3 operation(s) for container image.
  name: Snyk Container Image API
  phrasing_intents:
  - id: listContainerImage
    intent: List container images in an organization
    question: Which container images has Snyk seen in my organization?
  - id: getContainerImage
    intent: Get a container image
    question: Where can I see the details of one container image?
  - id: listImageTargetRefs
    intent: List target references for a container image
    question: Which targets and tags reference a given container image?
  phrasing_ops: 3
  slug: snyk-container-image-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The OpenAPI specification for this service.
  name: Snyk Open API
  phrasing_intents:
  - id: listAPIVersions
    intent: List available API specification versions
    question: Which versions of the Snyk REST API OpenAPI specification are available?
  - id: getAPIVersion
    intent: Get the OpenAPI specification for a version
    question: Can I download the OpenAPI document that was effective at a given version?
  phrasing_ops: 2
  slug: snyk-open-api-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Personal Access Token API from Snyk — 2 operation(s) for personal access token.
  name: Snyk Personal Access Token API
  phrasing_intents:
  - id: listPersonalAccessToken
    intent: List your personal access tokens
    question: Which personal access tokens have I created in Snyk?
  - id: deletePersonalAccessToken
    intent: Delete a personal access token
    question: How do I revoke a personal access token that might have leaked?
  phrasing_ops: 2
  slug: snyk-personal-access-token-api
- baseURL: https://api.snyk.io/rest
  baseurl_source: declared
  description: The Service Accounts API from Snyk — 6 operation(s) for service accounts.
  name: Snyk Service Accounts API
  phrasing_intents:
  - id: getManyGroupServiceAccount
    intent: List a group's service accounts
    question: Which service accounts exist at the group level in Snyk?
  - id: createGroupServiceAccount
    intent: Create a group-level service account
    question: How do I create a service account that can call the Snyk API for a whole group?
  - id: deleteOneGroupServiceAccount
    intent: Permanently delete a group service account
    question: Can I permanently remove a service account from my group?
  - id: getOneGroupServiceAccount
    intent: Get a group service account by ID
    question: Can I look up the details of one group-level service account?
  - id: updateGroupServiceAccount
    intent: Rename a group service account
    question: Can I rename a service account that belongs to my group?
  - id: updateServiceAccountSecret
    intent: Manage a group service account's client secret
    question: Can I manage the client secret of a group service account through the API?
  - id: getManyOrgServiceAccounts
    intent: List an organization's service accounts
    question: Which service accounts have been created in my organization?
  - id: createOrgServiceAccount
    intent: Create an organization service account
    question: Can I create a service account for just one Snyk organization?
  phrasing_ops: 12
  slug: snyk-service-accounts-api
artifact_total: 270
asyncapis:
- description: ''
  name: Snyk Webhooks
  slug: snyk-webhooks
collections:
- collection_type: open
  name: Snyk AccessRequests API
  slug: open-snyk-accessrequests-api
- collection_type: open
  name: Snyk AccessRequests AiBom API
  slug: open-snyk-aibom-api
- collection_type: open
  name: Snyk AccessRequests Apps API
  slug: open-snyk-apps-api
- collection_type: open
  name: Snyk AccessRequests Asset API
  slug: open-snyk-asset-api
- collection_type: open
  name: Snyk AccessRequests Audit Logs API
  slug: open-snyk-audit-logs-api
- collection_type: open
  name: Snyk AccessRequests BrokerConnections API
  slug: open-snyk-brokerconnections-api
- collection_type: open
  name: Snyk AccessRequests BrokerContexts API
  slug: open-snyk-brokercontexts-api
- collection_type: open
  name: Snyk AccessRequests BrokerDeployments API
  slug: open-snyk-brokerdeployments-api
- collection_type: open
  name: Snyk AccessRequests Catalog Resource API
  slug: open-snyk-catalog-resource-api
- collection_type: open
  name: Snyk AccessRequests Cloud API
  slug: open-snyk-cloud-api
- collection_type: open
  name: Snyk AccessRequests Collection API
  slug: open-snyk-collection-api
- collection_type: open
  name: Snyk AccessRequests ContainerImage API
  slug: open-snyk-containerimage-api
- collection_type: open
  name: Snyk AccessRequests ContainerRegistryImportPolicy API
  slug: open-snyk-containerregistryimportpolicy-api
- collection_type: open
  name: Snyk AccessRequests Custom Base Images API
  slug: open-snyk-custom-base-images-api
- collection_type: open
  name: Snyk AccessRequests DeploymentCredentials API
  slug: open-snyk-deploymentcredentials-api
- collection_type: open
  name: Snyk AccessRequests Export API
  slug: open-snyk-export-api
- collection_type: open
  name: Snyk AccessRequests Findings API
  slug: open-snyk-findings-api
- collection_type: open
  name: Snyk AccessRequests Group API
  slug: open-snyk-group-api
- collection_type: open
  name: Snyk AccessRequests Groups API
  slug: open-snyk-groups-api
- collection_type: open
  name: Snyk AccessRequests IacSettings API
  slug: open-snyk-iacsettings-api
- collection_type: open
  name: Snyk AccessRequests Integrations API
  slug: open-snyk-integrations-api
- collection_type: open
  name: Snyk AccessRequests Inventory Assets API
  slug: open-snyk-inventory-assets-api
- collection_type: open
  name: Snyk AccessRequests Invites API
  slug: open-snyk-invites-api
- collection_type: open
  name: Snyk AccessRequests Issues API
  slug: open-snyk-issues-api
- collection_type: open
  name: Snyk AccessRequests LanguagesSettings API
  slug: open-snyk-languagessettings-api
- collection_type: open
  name: Snyk AccessRequests Learn assignment API
  slug: open-snyk-learn-assignment-api
- collection_type: open
  name: Snyk AccessRequests Learn progress API
  slug: open-snyk-learn-progress-api
- collection_type: open
  name: Snyk AccessRequests OpenAPI API
  slug: open-snyk-openapi-api
- collection_type: open
  name: Snyk AccessRequests OpenSourceSettings API
  slug: open-snyk-opensourcesettings-api
- collection_type: open
  name: Snyk AccessRequests Orgs API
  slug: open-snyk-orgs-api
- collection_type: open
  name: Snyk AccessRequests Package API
  slug: open-snyk-package-api
- collection_type: open
  name: Snyk AccessRequests Package Version API
  slug: open-snyk-package-version-api
- collection_type: open
  name: Snyk AccessRequests PersonalAccessToken API
  slug: open-snyk-personalaccesstoken-api
- collection_type: open
  name: Snyk AccessRequests Policies API
  slug: open-snyk-policies-api
- collection_type: open
  name: Snyk AccessRequests Projects API
  slug: open-snyk-projects-api
- collection_type: open
  name: Snyk AccessRequests Pull Request Templates API
  slug: open-snyk-pull-request-templates-api
- collection_type: open
  name: Snyk API
  slug: open-snyk-rest
- collection_type: open
  name: Snyk AccessRequests SastSettings API
  slug: open-snyk-sastsettings-api
- collection_type: open
  name: Snyk AccessRequests SBOM API
  slug: open-snyk-sbom-api
- collection_type: open
  name: Snyk AccessRequests ServiceAccounts API
  slug: open-snyk-serviceaccounts-api
- collection_type: open
  name: Snyk AccessRequests Slack API
  slug: open-snyk-slack-api
- collection_type: open
  name: Snyk AccessRequests SlackSettings API
  slug: open-snyk-slacksettings-api
- collection_type: open
  name: Snyk AccessRequests Targets API
  slug: open-snyk-targets-api
- collection_type: open
  name: Snyk AccessRequests TenantRole API
  slug: open-snyk-tenantrole-api
- collection_type: open
  name: Snyk AccessRequests Tenants API
  slug: open-snyk-tenants-api
- collection_type: open
  name: Snyk AccessRequests Tests API
  slug: open-snyk-tests-api
- collection_type: open
  name: Snyk AccessRequests Users API
  slug: open-snyk-users-api
common:
- group: design
  href: https://artifacts.apis.io/snyk/rules/snyk-rules.yml
  title: ''
  type: Spectral
  url: rules/snyk-rules.yml
- group: design
  href: https://artifacts.apis.io/snyk/json-ld/snyk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/snyk-context.jsonld
- group: design
  href: https://artifacts.apis.io/snyk/vocabulary/snyk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/snyk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/snyk/llms/snyk-site-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snyk-site-llms.txt
- group: agent
  href: https://artifacts.apis.io/snyk/llms/snyk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/snyk-llms.txt
- group: other
  href: https://artifacts.apis.io/snyk/hosts/snyk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/snyk-hosts.yml
- group: other
  href: https://artifacts.apis.io/snyk/vendors/snyk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/snyk-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://snyk.io/news/
- group: other
  title: ''
  type: Leadership
  url: https://snyk.io/about/leadership/
- group: other
  href: https://artifacts.apis.io/snyk/overlays/snyk-accessrequests-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snyk-accessrequests-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snyk/overlays/snyk-containerimage-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snyk-containerimage-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snyk/overlays/snyk-openapi-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snyk-openapi-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snyk/overlays/snyk-personalaccesstoken-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snyk-personalaccesstoken-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snyk/overlays/snyk-serviceaccounts-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snyk-serviceaccounts-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snyk/overlays/snyk-oauth2-app-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snyk-oauth2-app-overlay.yaml
- group: other
  href: https://artifacts.apis.io/snyk/overlays/snyk-oauth2-token-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/snyk-oauth2-token-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/snyk/studio-mcp/blob/main/LICENSE
- group: other
  href: https://artifacts.apis.io/snyk/capabilities/snyk-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/snyk-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/snyk/agentic-access/snyk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/snyk-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/snyk/security/snyk-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/snyk-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/snyk/security/snyk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/snyk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/snyk/security/snyk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/snyk-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/snyk/authentication/snyk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/snyk-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/snyk
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/snyk
- group: company
  title: ''
  type: Website
  url: https://snyk.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.snyk.io/developer-tools/snyk-api
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.snyk.io/
- group: commercial
  href: https://artifacts.apis.io/snyk/plans/snyk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/snyk-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/snyk/rate-limits/snyk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/snyk-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/snyk/finops/snyk-finops.yml
  title: ''
  type: FinOps
  url: finops/snyk-finops.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.snyk.io/llms.txt
- group: company
  title: ''
  type: BlogRSS
  url: https://snyk.io/blog/feed/
- group: build
  href: https://artifacts.apis.io/snyk/packages/snyk-packages.yml
  title: ''
  type: Packages
  url: packages/snyk-packages.yml
- group: build
  href: https://artifacts.apis.io/snyk/packages/snyk-packages.yml
  title: ''
  type: SDKs
  url: packages/snyk-packages.yml
- group: build
  href: https://artifacts.apis.io/snyk/cli/snyk-cli.yml
  title: ''
  type: CLI
  url: cli/snyk-cli.yml
- group: agent
  href: https://artifacts.apis.io/snyk/mcp/snyk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/snyk-mcp.yml
- group: build
  href: https://artifacts.apis.io/snyk/mcp/snyk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/snyk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/snyk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/snyk/well-known/snyk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/snyk-well-known.yml
- group: auth
  href: https://artifacts.apis.io/snyk/well-known/snyk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/snyk-security.txt
- group: auth
  href: https://artifacts.apis.io/snyk/security/snyk-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/snyk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/snyk/security/snyk-trust-center.yml
  title: ''
  type: Compliance
  url: security/snyk-trust-center.yml
- group: design
  href: https://artifacts.apis.io/snyk/conformance/snyk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/snyk-conformance.yml
- group: design
  href: https://artifacts.apis.io/snyk/conventions/snyk-conventions.yml
  title: ''
  type: Conventions
  url: conventions/snyk-conventions.yml
- group: design
  href: https://artifacts.apis.io/snyk/errors/snyk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/snyk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/snyk/lifecycle/snyk-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/snyk-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/snyk/lifecycle/snyk-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/snyk-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.snyk.io/
- group: operate
  href: https://artifacts.apis.io/snyk/changelog/snyk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/snyk-changelog.yml
- group: auth
  href: https://artifacts.apis.io/snyk/scopes/snyk-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/snyk-scopes.yml
- group: design
  href: https://artifacts.apis.io/snyk/data-model/snyk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/snyk-data-model.yml
- group: design
  href: https://artifacts.apis.io/snyk/asyncapi/snyk-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/snyk-webhooks.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.snyk.io/developer-tools/snyk-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.snyk.io/getting-started-guides/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.snyk.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://snyk.io/plans/
- group: start
  title: ''
  type: SignUp
  url: https://app.snyk.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://snyk.io/policies/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://snyk.io/policies/privacy/
- group: company
  title: ''
  type: Blog
  url: https://snyk.io/blog/
created: '2026-05-08'
description: Snyk is a developer-first security platform covering code, open-source dependencies, container images, and infrastructure-as-code. The Snyk REST API and V1 API expose groups, organizations, projects, issues, targets, integrations, audit logs, SBOMs, container images, custom base images, webhooks, and exports for application-security teams.
finops:
- has_sources: true
  method: derived
  name: Snyk Finops
  primary_unit: subscription
  service_category: ''
  slug: snyk-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/snyk.png
json_schemas:
- name: AccessRequest
  property_count: 3
  slug: snyk-access-request
- name: AppBot
  property_count: 5
  slug: snyk-app-bot
- name: AppInstallData
  property_count: 5
  slug: snyk-app-install-data
- name: AppInstallDataWithSecret
  property_count: 5
  slug: snyk-app-install-data-with-secret
- name: AppInstallWithClient
  property_count: 5
  slug: snyk-app-install-with-client
- name: AppPostRequest
  property_count: 1
  slug: snyk-app-post-request
- name: AssetListResponse
  property_count: 3
  slug: snyk-asset-list-response
- name: AssetProjectResponseData
  property_count: 3
  slug: snyk-asset-project-response-data
- name: AssetResponseData
  property_count: 5
  slug: snyk-asset-response-data
- name: AuditLogSearch
  property_count: 2
  slug: snyk-audit-log-search
- name: AuthCode
  property_count: 5
  slug: snyk-auth-code
- name: BrokerSettings
  property_count: 1
  slug: snyk-broker-settings
- name: BulkMigrationCreateResponse
  property_count: 3
  slug: snyk-bulk-migration-create-response
- name: BulkPackageUrlsRequestBody
  property_count: 1
  slug: snyk-bulk-package-urls-request-body
- name: CatalogProgressResponse
  property_count: 4
  slug: snyk-catalog-progress-response
- name: ClientCredentials
  property_count: 0
  slug: snyk-client-credentials
- name: CollectionRelationships
  property_count: 2
  slug: snyk-collection-relationships
- name: CollectionResponse
  property_count: 5
  slug: snyk-collection-response
- name: ContainerRegistryImportPolicyAttributes
  property_count: 1
  slug: snyk-container-registry-import-policy-attributes
- name: CreateAiBomRequestBody
  property_count: 1
  slug: snyk-create-ai-bom-request-body
- name: CreateAiBomResponseBody
  property_count: 3
  slug: snyk-create-ai-bom-response-body
- name: CreateAndUploadAiBomRequestBody
  property_count: 1
  slug: snyk-create-and-upload-ai-bom-request-body
- name: CreateAssignmentsPayload
  property_count: 10
  slug: snyk-create-assignments-payload
- name: CreateBrokerConnectionRequest
  property_count: 1
  slug: snyk-create-broker-connection-request
- name: CreateBrokerContextRequest
  property_count: 1
  slug: snyk-create-broker-context-request
- name: CreateBrokerDeploymentRequest
  property_count: 1
  slug: snyk-create-broker-deployment-request
- name: CreateDeploymentCredentialRequest
  property_count: 1
  slug: snyk-create-deployment-credential-request
- name: CreateGroupMembershipRequestBody
  property_count: 1
  slug: snyk-create-group-membership-request-body
- name: CreateOrgMembershipRequestBody20240825
  property_count: 1
  slug: snyk-create-org-membership-request-body20240825
- name: CreateSearchRequestBody
  property_count: 1
  slug: snyk-create-search-request-body
- name: CreateTenantRoleRequestAttributes
  property_count: 3
  slug: snyk-create-tenant-role-request-attributes
- name: CustomBaseImageCollectionResponse
  property_count: 3
  slug: snyk-custom-base-image-collection-response
- name: CustomBaseImagePatchRequest
  property_count: 1
  slug: snyk-custom-base-image-patch-request
- name: CustomBaseImagePostRequest
  property_count: 1
  slug: snyk-custom-base-image-post-request
- name: CustomBaseImageResponse
  property_count: 3
  slug: snyk-custom-base-image-response
- name: DeleteAssignmentsRequest
  property_count: 1
  slug: snyk-delete-assignments-request
- name: DeleteOrgAssignmentsBulkRequest
  property_count: 1
  slug: snyk-delete-org-assignments-bulk-request
- name: DeleteProjectsFromCollectionRequest
  property_count: 1
  slug: snyk-delete-projects-from-collection-request
- name: DryRunJobCreationResponseAttributes
  property_count: 1
  slug: snyk-dry-run-job-creation-response-attributes
- name: DryRunJobResponseAttributes
  property_count: 6
  slug: snyk-dry-run-job-response-attributes
- name: EducationResourceExtended
  property_count: 3
  slug: snyk-education-resource-extended
- name: EnvironmentAttributes
  property_count: 8
  slug: snyk-environment-attributes
- name: FilterFieldsResponse
  property_count: 2
  slug: snyk-filter-fields-response
- name: FindingData
  property_count: 5
  slug: snyk-finding-data
- name: GetAiBomResponseBody
  property_count: 3
  slug: snyk-get-ai-bom-response-body
- name: GetAiBomResponseJobBody
  property_count: 3
  slug: snyk-get-ai-bom-response-job-body
- name: GetBrokerConnectionIntegrationsResponse
  property_count: 3
  slug: snyk-get-broker-connection-integrations-response
- name: GetBrokerContextResponse
  property_count: 3
  slug: snyk-get-broker-context-response
- name: GetBrokerDeploymentResponse
  property_count: 3
  slug: snyk-get-broker-deployment-response
- name: GetDeploymentCredentialResponse
  property_count: 3
  slug: snyk-get-deployment-credential-response
- name: GetProjectSettingsCollection
  property_count: 3
  slug: snyk-get-project-settings-collection
- name: GroupFieldsResponse
  property_count: 2
  slug: snyk-group-fields-response
- name: GroupIacSettingsRequest
  property_count: 2
  slug: snyk-group-iac-settings-request
- name: GroupIacSettingsResponse
  property_count: 3
  slug: snyk-group-iac-settings-response
- name: GroupMembershipOrgMembership
  property_count: 5
  slug: snyk-group-membership-org-membership
- name: GroupMembershipResponseData
  property_count: 0
  slug: snyk-group-membership-response-data
- name: GroupMembership
  property_count: 4
  slug: snyk-group-membership
- name: GroupPolicyResponse
  property_count: 3
  slug: snyk-group-policy-response
- name: GroupResponse
  property_count: 3
  slug: snyk-group-response
- name: GroupValuesResponse
  property_count: 2
  slug: snyk-group-values-response
- name: Image
  property_count: 4
  slug: snyk-image
- name: ImageTargetRef
  property_count: 3
  slug: snyk-image-target-ref
- name: IntegrationId
  property_count: 0
  slug: snyk-integration-id
- name: IntegrationPatchRequestData
  property_count: 1
  slug: snyk-integration-patch-request-data
- name: IntegrationRequestData
  property_count: 1
  slug: snyk-integration-request-data
- name: Integration
  property_count: 4
  slug: snyk-integration
- name: IntegrationSettingsPatchRequestData
  property_count: 1
  slug: snyk-integration-settings-patch-request-data
- name: IntegrationSettings
  property_count: 3
  slug: snyk-integration-settings
- name: io.snyk.api.common.JsonApi
  property_count: 1
  slug: snyk-io-snyk-api-common-json-api
- name: io.snyk.api.common.LinkProperty
  property_count: 0
  slug: snyk-io-snyk-api-common-link-property
- name: io.snyk.api.common.Meta
  property_count: 0
  slug: snyk-io-snyk-api-common-meta
- name: IssuesResponse
  property_count: 4
  slug: snyk-issues-response
- name: IssuesWithPurlsResponse
  property_count: 4
  slug: snyk-issues-with-purls-response
- name: JsonApi
  property_count: 1
  slug: snyk-json-api
- name: LanguagesSettingsResponse
  property_count: 3
  slug: snyk-languages-settings-response
- name: LanguagesSettingsUpdateRequest
  property_count: 3
  slug: snyk-languages-settings-update-request
- name: LatestIssueCounts
  property_count: 5
  slug: snyk-latest-issue-counts
- name: LessonAssignmentDecoratedResource
  property_count: 3
  slug: snyk-lesson-assignment-decorated-resource
- name: Links
  property_count: 6
  slug: snyk-links
- name: ListBrokerConnectionsResponse
  property_count: 3
  slug: snyk-list-broker-connections-response
- name: ListBrokerConnectionsSummaryResponse
  property_count: 3
  slug: snyk-list-broker-connections-summary-response
- name: ListBrokerContextsResponse
  property_count: 3
  slug: snyk-list-broker-contexts-response
- name: ListBrokerDeploymentsResponse
  property_count: 3
  slug: snyk-list-broker-deployments-response
- name: ListDeploymentCredentialsResponse
  property_count: 3
  slug: snyk-list-deployment-credentials-response
- name: ListRepositoryAliasesResponse
  property_count: 3
  slug: snyk-list-repository-aliases-response
- name: MembershipPatchRequestBody
  property_count: 4
  slug: snyk-membership-patch-request-body
- name: OrgAttributes
  property_count: 7
  slug: snyk-org-attributes
- name: OrgIacSettingsRequest
  property_count: 2
  slug: snyk-org-iac-settings-request
- name: OrgIacSettingsResponse
  property_count: 3
  slug: snyk-org-iac-settings-response
- name: OrgInvitationPostData
  property_count: 2
  slug: snyk-org-invitation-post-data
- name: OrgInvitation
  property_count: 4
  slug: snyk-org-invitation
- name: OrgInvitation20240621
  property_count: 4
  slug: snyk-org-invitation20240621
- name: OrgMembership
  property_count: 4
  slug: snyk-org-membership
- name: Org20230529
  property_count: 4
  slug: snyk-org20230529
- name: PackageAttributes
  property_count: 10
  slug: snyk-package-attributes
- name: PackageVersionAttributes
  property_count: 13
  slug: snyk-package-version-attributes
- name: PaginatedLinks
  property_count: 5
  slug: snyk-paginated-links
- name: PatTenantId
  property_count: 0
  slug: snyk-pat-tenant-id
- name: PatchProjectRequest
  property_count: 1
  slug: snyk-patch-project-request
- name: PersonalAccessTokenCreatedAt
  property_count: 0
  slug: snyk-personal-access-token-created-at
- name: PersonalAccessTokenExpiresAt
  property_count: 0
  slug: snyk-personal-access-token-expires-at
- name: PersonalAccessTokenLabel
  property_count: 0
  slug: snyk-personal-access-token-label
- name: PolicyResponse
  property_count: 3
  slug: snyk-policy-response
- name: PolymorphicAssetData
  property_count: 5
  slug: snyk-polymorphic-asset-data
- name: Principal20240422
  property_count: 3
  slug: snyk-principal20240422
- name: ProjectAttributes
  property_count: 15
  slug: snyk-project-attributes
- name: ProjectRelationships
  property_count: 4
  slug: snyk-project-relationships
- name: ProjectSettingsData
  property_count: 3
  slug: snyk-project-settings-data
- name: ProjectSettingsPatchRequest
  property_count: 1
  slug: snyk-project-settings-patch-request
- name: PublicTarget
  property_count: 4
  slug: snyk-public-target
- name: PullRequestTemplateAttributes
  property_count: 3
  slug: snyk-pull-request-template-attributes
- name: PullRequsetTemplateId
  property_count: 0
  slug: snyk-pull-requset-template-id
- name: RefreshToken
  property_count: 3
  slug: snyk-refresh-token
- name: RemoveRepositoryAliasRequestData
  property_count: 3
  slug: snyk-remove-repository-alias-request-data
- name: ResourceAttributes
  property_count: 20
  slug: snyk-resource-attributes
- name: ResourceReference
  property_count: 2
  slug: snyk-resource-reference
- name: ResourceRelationships
  property_count: 0
  slug: snyk-resource-relationships
- name: SastEnablement
  property_count: 3
  slug: snyk-sast-enablement
- name: SbomResponse
  property_count: 2
  slug: snyk-sbom-response
- name: SbomTestCreateAttributes
  property_count: 2
  slug: snyk-sbom-test-create-attributes
- name: ScanAttributes
  property_count: 12
  slug: snyk-scan-attributes
- name: ScanRelationships
  property_count: 0
  slug: snyk-scan-relationships
- name: SelfLink
  property_count: 1
  slug: snyk-self-link
- name: ServiceAccount
  property_count: 4
  slug: snyk-service-account
- name: SettingsRequest
  property_count: 1
  slug: snyk-settings-request
- name: SlackChannel
  property_count: 3
  slug: snyk-slack-channel
- name: SlackDefaultSettingsData
  property_count: 3
  slug: snyk-slack-default-settings-data
- name: TenantAttributes
  property_count: 4
  slug: snyk-tenant-attributes
- name: TenantResponseData
  property_count: 4
  slug: snyk-tenant-response-data
- name: TenantRoleResponseData
  property_count: 5
  slug: snyk-tenant-role-response-data
- name: TenantRolesExternalMeta
  property_count: 1
  slug: snyk-tenant-roles-external-meta
- name: TestData
  property_count: 4
  slug: snyk-test-data
- name: TestRequestBody
  property_count: 1
  slug: snyk-test-request-body
- name: Types
  property_count: 0
  slug: snyk-types
- name: UpdateAssetRequestData
  property_count: 3
  slug: snyk-update-asset-request-data
- name: UpdateBrokerConnectionIntegrationWithContextResponse
  property_count: 3
  slug: snyk-update-broker-connection-integration-with-context-response
- name: UpdateBrokerConnectionIntegrationWithContext
  property_count: 1
  slug: snyk-update-broker-connection-integration-with-context
- name: UpdateBrokerConnectionRequest
  property_count: 1
  slug: snyk-update-broker-connection-request
- name: UpdateBrokerContextRequest
  property_count: 1
  slug: snyk-update-broker-context-request
- name: UpdateBrokerDeploymentRequest
  property_count: 1
  slug: snyk-update-broker-deployment-request
- name: UpdateCollectionRequest
  property_count: 1
  slug: snyk-update-collection-request
- name: UpdateCollectionWithProjectsRequest
  property_count: 1
  slug: snyk-update-collection-with-projects-request
- name: UpdateDeploymentCredentialRequest
  property_count: 1
  slug: snyk-update-deployment-credential-request
- name: UpdateGroupPolicyPayload
  property_count: 1
  slug: snyk-update-group-policy-payload
- name: UpdateOrgMembershipRequestBody20240825
  property_count: 4
  slug: snyk-update-org-membership-request-body20240825
- name: UpdatePolicyPayload
  property_count: 1
  slug: snyk-update-policy-payload
- name: UpdateTenantMembershipRequestData
  property_count: 4
  slug: snyk-update-tenant-membership-request-data
- name: UpdateTenantRoleRequestAttributes
  property_count: 3
  slug: snyk-update-tenant-role-request-attributes
- name: UserPatchRequestBody
  property_count: 3
  slug: snyk-user-patch-request-body
- name: User
  property_count: 3
  slug: snyk-user
- name: UsersProgressResponse
  property_count: 3
  slug: snyk-users-progress-response
jsonld:
- class_count: 120
  name: Snyk Context
  property_count: 120
  slug: snyk-context
layout: provider
mcp_servers:
- description: 'Snyk ships a first-party MCP server as part of Snyk Studio, its agentic-development security layer. It is deliberately LOCAL ONLY: the server runs on the developer''s own machine through the Snyk CLI s'
  name: Snyk MCP Server
  slug: snyk-mcp-server
modified: '2026-08-27'
name: Snyk
nav: Providers
network: true
overview: 'Snyk publishes 50 API contracts indexed on the [APIs.io](https://apis.io/) network, including AiBom API, Apps API, Asset API, and 47 more. Tagged areas include Security, DevSecOps, Vulnerability Management, Application Security, and Software Composition Analysis.


  The Snyk catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Snyk''s developer surface includes authentication, documentation, API reference, CLI, changelog, getting-started guide, support, and 54 more developer resources.'
plans:
- name: Snyk Plans Pricing
  plan_count: 3
  slug: snyk-plans-pricing
- name: Snyk Price Estimates
  plan_count: 0
  slug: snyk-price-estimates
random_paper: 21
rate_limits:
- limit_count: 3
  name: Snyk Rate Limits
  slug: snyk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Snyk API Rules
  rule_count: 14
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 5
  slug: snyk-rules
scopes:
- name: Snyk Scopes
  scope_count: 26
  slug: snyk-scopes
  summary_line: 26 scopes · authorization_code/refresh_token/client_credentials
score:
  band: exemplar
  composite: 80.5
  coverage:
    artifact_dirs: 36
    catalog_earned: 87.8
    catalog_earned_first_party: 24.0
    catalog_gap: 27.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.2
  facets:
    access_clarity: 100.0
    contract_governance: 22.0
    contract_quality: 74.3
    developer_ergonomics: 71.4
    discoverability: 70.0
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 80.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 47
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
    score: 22.2
screenshot: https://apis.io/screenshots/snyk/snyk-2026-06-20T194114.png
security:
- kind: authentication
  name: Snyk Authentication
  slug: snyk-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Snyk Domain Security
  slug: snyk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Snyk Vulnerability Disclosure
  slug: snyk-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Snyk Trust Center
  slug: snyk-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
skill_count: 8
skills:
- name: ai-inventory
  slug: snyk-ai-inventory
- name: container-security
  slug: snyk-container-security
- name: drift-detector
  slug: snyk-drift-detector
- name: snyk-fix
  slug: snyk-fix
- name: iac-security
  slug: snyk-iac-security
- name: sbom-analyzer
  slug: snyk-sbom-analyzer
- name: secure-at-inception
  slug: snyk-secure-at-inception
- name: secure-dependency-health-check
  slug: snyk-secure-dependency-health-check
slug: snyk
tags:
- Security
- DevSecOps
- Vulnerability Management
- Application Security
- Software Composition Analysis
- SAST
- Container Security
- IaC
website: https://snyk.io/
---
