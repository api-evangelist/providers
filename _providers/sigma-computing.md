---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 58.3
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Sigma's first-party remote Model Context Protocol server. AI assistants such as Claude, ChatGPT, Codex, Cursor and Snowflake Cortex Code connect over HTTP with OAuth and can then search a Sigma organi
  name: Sigma MCP Server
  slug: sigma-mcp-server
- description: Secure embedding of Sigma workbooks, pages and individual elements into a host application. Embed URLs are signed with JSON Web Tokens carrying the viewing user's identity, team and user attributes so
  name: Sigma Embed API
  slug: sigma-embed-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Auth API from Sigma Computing — 1 operation(s) for auth.
  name: Sigma Computing Auth API
  phrasing_intents:
  - id: postToken
    intent: Get an API access token
    question: How do I get a bearer token to call the Sigma API?
  phrasing_ops: 1
  slug: sigma-computing-auth-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Connections API from Sigma Computing — 13 operation(s) for connections.
  name: Sigma Computing Connections API
  phrasing_intents:
  - id: lookupConnection
    intent: Look up a warehouse object by its path
    question: How do I find the connection path ID for a schema or table by its name path?
  - id: listConnections
    intent: List my warehouse connections
    question: Which data warehouse connections does my Sigma organization have?
  - id: createConnection
    intent: Connect a cloud data warehouse
    question: How do I connect Sigma to my cloud data warehouse through the API?
  - id: updateConnectionDeprecated
    intent: Rename a connection (deprecated PATCH)
    question: Is there an older deprecated endpoint to rename a connection or toggle OAuth?
  - id: getConnection
    intent: Get a connection's metadata
    question: What are the settings of one of my warehouse connections?
  - id: deleteConnection
    intent: Delete a warehouse connection
    question: How do I remove a data warehouse connection from Sigma?
  - id: updateConnection
    intent: Update or restore a connection
    question: How do I change a connection's settings while keeping the details I want?
  - id: postConnectionDbtArtifacts
    intent: Upload dbt run artifacts for a connection
    question: How do I push dbt Core metadata into Sigma for a connection?
  phrasing_ops: 22
  slug: sigma-computing-connections-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Credentials API from Sigma Computing — 2 operation(s) for credentials.
  name: Sigma Computing Credentials API
  phrasing_intents:
  - id: createCredentials
    intent: Create API client credentials for a user
    question: How do I generate a client ID and secret for a Sigma user?
  - id: deleteCredentials
    intent: Revoke API client credentials
    question: How do I revoke a leaked API client ID?
  phrasing_ops: 2
  slug: sigma-computing-credentials-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Datasets API from Sigma Computing — 7 operation(s) for datasets.
  name: Sigma Computing Datasets API
  phrasing_intents:
  - id: listDatasets
    intent: List datasets (deprecated)
    question: Which legacy datasets do I still have access to?
  - id: getDataset
    intent: Get a dataset (deprecated)
    question: How do I look up one legacy dataset by ID?
  - id: listDatasetGrants
    intent: List permissions on a dataset
    question: Who has been granted access to a dataset?
  - id: createDatasetGrant
    intent: Grant access to a dataset
    question: How do I give a team access to a legacy dataset?
  - id: deleteDatasetGrant
    intent: Revoke a dataset permission
    question: How do I remove someone's access to a dataset?
  - id: materializeDataset
    intent: Start a dataset materialization run
    question: How do I trigger a materialization for a dataset right now?
  - id: listDatasetMaterializations
    intent: List a dataset's materialization jobs
    question: When did a dataset last materialize?
  - id: migrateDatasetToDataModel
    intent: Migrate a dataset to a data model
    question: How do I convert a deprecated dataset into a data model?
  phrasing_ops: 9
  slug: sigma-computing-datasets-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The deploymentPolicies API from Sigma Computing — 7 operation(s) for deploymentpolicies.
  name: Sigma Computing Deployment Policies API
  phrasing_intents:
  - id: createDeployment
    intent: Create a deployment policy
    question: How do I define which documents get deployed to tenant organizations?
  - id: listDeployments
    intent: List deployment policies
    question: What deployment policies are set up in my Sigma organization?
  - id: getDeployment
    intent: Get a deployment policy
    question: How do I see the settings of one deployment policy?
  - id: updateDeployment
    intent: Update a deployment policy
    question: Can I rename a deployment policy or change its name in tenants?
  - id: archiveDeployment
    intent: Archive a deployment policy
    question: How do I retire a deployment policy I no longer use?
  - id: listInodesForDeployment
    intent: List documents in a deployment policy
    question: Which workbooks and data models are included in a deployment policy?
  - id: addInodesToDeployment
    intent: Add documents to a deployment policy
    question: How do I include more workbooks in a deployment policy?
  - id: removeInodesFromDeployment
    intent: Remove a document from a deployment policy
    question: How do I stop deploying a particular workbook to tenants?
  phrasing_ops: 12
  slug: sigma-computing-deploymentpolicies-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Favorites API from Sigma Computing — 3 operation(s) for favorites.
  name: Sigma Computing Favorites API
  phrasing_intents:
  - id: addFavorite
    intent: Favorite a document for a user
    question: How do I add a workbook or folder to someone's favorites?
  - id: listFavorites
    intent: List a user's favorite documents
    question: What documents has a user marked as favorites?
  - id: removeFavorite
    intent: Unfavorite a document for a user
    question: How do I remove a document from a user's favorites?
  phrasing_ops: 3
  slug: sigma-computing-favorites-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Files API from Sigma Computing — 2 operation(s) for files.
  name: Sigma Computing Files API
  phrasing_intents:
  - id: filesList
    intent: List documents and folders
    question: What workbooks and folders can I see under a given folder?
  - id: filesCreate
    intent: Create an empty folder, workbook or report
    question: How do I create a new folder in Sigma through the API?
  - id: filesGet
    intent: Get details of a document or folder
    question: How do I look up a workbook, report or folder by its file ID?
  - id: filesUpdate
    intent: Rename, move or restore a document
    question: How do I move a workbook into a different folder?
  - id: filesDelete
    intent: Delete a document or folder
    question: How do I delete a folder or workbook by its file ID?
  phrasing_ops: 5
  slug: sigma-computing-files-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Grants API from Sigma Computing — 2 operation(s) for grants.
  name: Sigma Computing Grants API
  phrasing_intents:
  - id: listGrants
    intent: List permission grants for a document, user or team
    question: Who has access to a particular document or folder?
  - id: createGrant
    intent: Grant access to a document, folder or workspace
    question: How do I give a user edit access to a folder or workspace?
  - id: getGrant
    intent: Get a grant by ID
    question: What permission and grantee does a specific grant have?
  - id: deleteGrant
    intent: Delete a grant by ID
    question: How do I revoke a document or folder permission by its grant ID?
  phrasing_ops: 4
  slug: sigma-computing-grants-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Members API from Sigma Computing — 9 operation(s) for members.
  name: Sigma Computing Members API
  phrasing_intents:
  - id: listMembers
    intent: List users in the organization (v2)
    question: How do I find a Sigma user by email address with the original v2 members list?
  - id: createMember
    intent: Invite a new user
    question: How do I add a new user to Sigma and send them an invitation?
  - id: getMember
    intent: Get a user by member ID
    question: How do I look up one user's profile by their member ID?
  - id: updateMember
    intent: Update a user's profile or account type
    question: How do I change a user's account type or email?
  - id: deleteMember
    intent: Deactivate a user
    question: Can a Sigma user be fully deleted, or only deactivated?
  - id: listAccessibleInodes
    intent: List documents a user can access
    question: Which workbooks and folders can a specific user open?
  - id: listFavoriteInodes
    intent: List a user's favorite documents
    question: What documents has a user marked as favorites?
  - id: listRecentInodes
    intent: List a user's recent documents
    question: What has a user opened recently?
  phrasing_ops: 12
  slug: sigma-computing-members-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Organizations API from Sigma Computing — 4 operation(s) for organizations.
  name: Sigma Computing Organizations API
  phrasing_intents:
  - id: updateOrganizationSettings
    intent: Change the organization's timezone
    question: How do I set the default timezone for my Sigma organization?
  - id: getBulkCopySetting
    intent: Check if members can bulk copy table data
    question: Are members allowed to bulk copy data out of tables?
  - id: updateBulkCopySetting
    intent: Turn bulk copy on or off
    question: How do I stop members from bulk copying table data?
  - id: getLicenseUpgradeRequestsSetting
    intent: Check if users can request license upgrades
    question: Can members of my organization request a license upgrade?
  - id: updateLicenseUpgradeRequestsSetting
    intent: Allow or block license upgrade requests
    question: How do I stop members from requesting license upgrades?
  - id: getPublicEmbedsSetting
    intent: Check if public embeds are allowed
    question: Does my organization allow workbooks to be embedded publicly?
  - id: updatePublicEmbedsSetting
    intent: Allow or block public workbook embeds
    question: How do I disable public embedding of workbooks?
  phrasing_ops: 7
  slug: sigma-computing-organizations-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The plugins API from Sigma Computing — 2 operation(s) for plugins.
  name: Sigma Computing Plugins API
  phrasing_intents:
  - id: listCustomPlugins
    intent: List custom plugins
    question: Which custom plugins are registered in my organization?
  - id: createCustomPlugin
    intent: Register a custom plugin
    question: How do I register a new custom plugin for workbooks?
  - id: getCustomPlugin
    intent: Get a custom plugin's metadata
    question: What are the name and URLs of a specific custom plugin?
  - id: updateCustomPlugin
    intent: Update a custom plugin's name or dev URL
    question: How do I rename a custom plugin or change its dev URL?
  - id: deleteCustomPlugin
    intent: Delete a custom plugin
    question: How do I permanently delete a custom plugin?
  phrasing_ops: 5
  slug: sigma-computing-plugins-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Query API from Sigma Computing — 1 operation(s) for query.
  name: Sigma Computing Query API
  phrasing_intents:
  - id: downloadQuery
    intent: Download an exported file
    question: How do I download the file after exporting a workbook or report?
  phrasing_ops: 1
  slug: sigma-computing-query-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Reports API from Sigma Computing — 26 operation(s) for reports.
  name: Sigma Computing Reports API
  phrasing_intents:
  - id: listReports
    intent: List the reports I can access
    question: Which Sigma reports can I see, including ones in My Documents?
  - id: createReport
    intent: Create an empty report in a folder
    question: How do I create a new blank report for stakeholders?
  - id: getReport
    intent: Get a report's details and metadata
    question: What is the URL and folder path of a specific report?
  - id: listReportColumns
    intent: List columns across every element of a report
    question: Which columns are used across all the data elements in a report?
  - id: listReportControls
    intent: List the control elements in a report
    question: What filters and input controls does a report offer its viewers?
  - id: copyReport
    intent: Duplicate a report into a folder
    question: How do I make a copy of an existing report?
  - id: listReportElements
    intent: List all elements in a report
    question: What charts, tables and controls make up a report?
  - id: listReportElementColumns
    intent: List columns of one report element
    question: What columns and formulas does a single chart or table in a report use?
  phrasing_ops: 29
  slug: sigma-computing-reports-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The SAML API from Sigma Computing — 5 operation(s) for saml.
  name: Sigma Computing SAML API
  phrasing_intents:
  - id: listSamlServiceProviders
    intent: List SAML service providers
    question: Which SAML service providers are configured in my organization?
  - id: listSamlServiceProviderCertificates
    intent: List certificates for a SAML service provider
    question: What certificates does a SAML service provider have?
  - id: createSamlServiceProviderCertificate
    intent: Create a SAML service provider certificate
    question: How do I generate a new certificate for SAML signing or encryption?
  - id: getSamlServiceProviderCertificate
    intent: Get a SAML certificate for my IdP
    question: How do I get the certificate to upload to my identity provider?
  - id: removeSamlServiceProviderCertificate
    intent: Remove a SAML certificate
    question: How do I delete an old SAML service provider certificate?
  - id: activateSamlServiceProviderCertificate
    intent: Activate a SAML certificate
    question: How do I switch SSO over to a newly created SAML certificate?
  - id: deactivateSamlServiceProviderCertificate
    intent: Deactivate a SAML certificate
    question: How do I stop using a SAML certificate without deleting it?
  phrasing_ops: 7
  slug: sigma-computing-saml-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The shortcuts API from Sigma Computing — 1 operation(s) for shortcuts.
  name: Sigma Computing Shortcuts API
  phrasing_intents:
  - id: shortcutsCreate
    intent: Create a shortcut to a document
    question: How do I surface a workbook in another folder without copying it?
  phrasing_ops: 1
  slug: sigma-computing-shortcuts-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The sourceSwapPolicies API from Sigma Computing — 2 operation(s) for sourceswappolicies.
  name: Sigma Computing Source Swap Policies API
  phrasing_intents:
  - id: createSourceSwapPolicy
    intent: Create a source swap policy
    question: How do I define a policy that swaps connections based on a user attribute?
  - id: listSourceSwapPolicies
    intent: List source swap policies
    question: What source swap policies are defined in my organization?
  - id: updateSourceSwapPolicy
    intent: Update a source swap policy
    question: How do I change the swaps in an existing source swap policy?
  - id: deleteSourceSwapPolicy
    intent: Delete a source swap policy
    question: How do I remove a source swap policy I no longer need?
  - id: getSourceSwapPolicy
    intent: Get a source swap policy
    question: How do I view one source swap policy's settings?
  phrasing_ops: 5
  slug: sigma-computing-sourceswappolicies-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Tags API from Sigma Computing — 3 operation(s) for tags.
  name: Sigma Computing Tags API
  phrasing_intents:
  - id: createVersionTag
    intent: Create a version tag
    question: How do I create a version tag like Production or Staging?
  - id: listVersionTag
    intent: List version tags
    question: What version tags exist in my Sigma organization?
  - id: deleteVersionTag
    intent: Delete a version tag
    question: How do I delete a version tag I no longer use?
  - id: updateVersionTag
    intent: Change a version tag's description
    question: How do I edit the description of a version tag?
  - id: listWorkbooksForTag
    intent: List workbooks carrying a version tag
    question: Which workbooks have a particular version tag applied?
  phrasing_ops: 5
  slug: sigma-computing-tags-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Teams API from Sigma Computing — 6 operation(s) for teams.
  name: Sigma Computing Teams API
  phrasing_intents:
  - id: listTeams
    intent: List teams (v2)
    question: Which teams exist in my Sigma organization?
  - id: createTeam
    intent: Create a team
    question: How do I create a new team and add members to it?
  - id: getTeam
    intent: Get a team and its member IDs
    question: What are the details of a specific team?
  - id: updateTeam
    intent: Rename a team or change its visibility
    question: How do I rename a team or change its description?
  - id: deleteTeam
    intent: Delete a team
    question: How do I delete a team I no longer need?
  - id: assignUserAttributesToTeam
    intent: Assign user attributes to a team
    question: How do I give a team several user attribute values at once?
  - id: getTeamMembers
    intent: List the members of a team
    question: Who is on a particular team?
  - id: updateTeamMembers
    intent: Add or remove team members
    question: How do I add people to or remove people from a team?
  phrasing_ops: 10
  slug: sigma-computing-teams-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Templates API from Sigma Computing — 4 operation(s) for templates.
  name: Sigma Computing Templates API
  phrasing_intents:
  - id: listTemplates
    intent: List workbook templates
    question: Which workbook templates are available to me?
  - id: getTemplate
    intent: Get a template
    question: How do I look up one template by its ID?
  - id: sourceSwapTemplate
    intent: Swap a template's data sources
    question: How do I point a workbook template at a different connection?
  - id: saveWorkbookFromTemplate
    intent: Create a workbook from a template
    question: How do I make a new workbook from a template?
  phrasing_ops: 4
  slug: sigma-computing-templates-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Tenants API from Sigma Computing — 6 operation(s) for tenants.
  name: Sigma Computing Tenants API
  phrasing_intents:
  - id: createTenant
    intent: Create a tenant organization
    question: How do I spin up a new tenant organization for a customer?
  - id: listTenants
    intent: List tenant organizations
    question: Which tenant organizations exist under my Sigma parent org?
  - id: patchTenant
    intent: Rename a tenant or change its slug
    question: How do I rename a tenant organization?
  - id: deleteTenant
    intent: Delete a tenant organization
    question: How do I remove a tenant organization for an offboarded customer?
  - id: getTenant
    intent: Get a tenant organization's details
    question: What are the name and slug of a specific tenant organization?
  - id: listTenantDeploymentCapabilities
    intent: List tenants a tenant can deploy to
    question: Which tenant organizations can a given tenant deploy content to?
  - id: addTenantDeploymentCapabilities
    intent: Allow a tenant to deploy to other tenants
    question: How do I let one tenant deploy workbooks to other tenants?
  - id: removeTenantDeploymentCapabilities
    intent: Revoke a tenant's deployment rights
    question: How do I stop a tenant from deploying to certain other tenants?
  phrasing_ops: 9
  slug: sigma-computing-tenants-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Translations API from Sigma Computing — 3 operation(s) for translations.
  name: Sigma Computing Translations API
  phrasing_intents:
  - id: listOrgLocales
    intent: List organization translation files
    question: Which locales have translation files defined for my organization?
  - id: createOrgTranslation
    intent: Create an organization translation file
    question: How do I add a translation file for a new language?
  - id: getOrgTranslations
    intent: Get a locale's base translation file
    question: What translations are defined for a locale, without custom variants?
  - id: updateOrgTranslation
    intent: Update a locale's base translation file
    question: How do I change the base translations for a language?
  - id: deleteOrgTranslation
    intent: Delete a locale's base translation file
    question: How do I delete the translation file for a language?
  - id: getOrgTranslationsWithVariant
    intent: Get a locale's custom variant translations
    question: How do I get a locale's translations including a custom variant?
  - id: updateOrgTranslationWithVariant
    intent: Update a custom translation variant
    question: How do I edit the key-value pairs of a custom translation variant?
  - id: deleteOrgTranslationWithVariant
    intent: Delete a custom translation variant
    question: How do I remove a custom translation variant for a locale?
  phrasing_ops: 8
  slug: sigma-computing-translations-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Webhooks API from Sigma Computing — 2 operation(s) for webhooks.
  name: Sigma Computing Webhooks API
  phrasing_intents:
  - id: webhooks
    intent: Trigger a workbook action via webhook
    question: How do I send data into a Sigma workbook action sequence from outside?
  - id: getWebhookSchema
    intent: Get the expected webhook message schema
    question: What fields does a workbook webhook expect before I send data?
  phrasing_ops: 2
  slug: sigma-computing-webhooks-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Whoami API from Sigma Computing — 1 operation(s) for whoami.
  name: Sigma Computing Whoami API
  phrasing_intents:
  - id: whoAmI
    intent: Get the current authenticated user
    question: Which Sigma user am I authenticated as?
  phrasing_ops: 1
  slug: sigma-computing-whoami-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Workbooks API from Sigma Computing — 44 operation(s) for workbooks.
  name: Sigma Computing Workbooks API
  phrasing_intents:
  - id: listWorkbooks
    intent: List workbooks I can access
    question: Which Sigma workbooks do I have access to?
  - id: createWorkbook
    intent: Create an empty workbook
    question: How do I create a blank workbook through the API?
  - id: getWorkbook
    intent: Get a workbook's details
    question: How do I look up a single workbook's name, URL and path?
  - id: getWorkbookBookmarks
    intent: List bookmarks in a workbook
    question: Which bookmarks exist on a workbook, including ones shared with me?
  - id: postWorkbookBookmarks
    intent: Add a bookmark to a workbook
    question: How do I save an exploration as a bookmark on a workbook?
  - id: getWorkbookBookmark
    intent: Get one bookmark on a workbook
    question: How do I fetch the details of a single bookmark on a regular workbook?
  - id: updateWorkbookBookmark
    intent: Update a workbook bookmark
    question: How do I point an existing workbook bookmark at a new exploration?
  - id: deleteWorkbookBookmarks
    intent: Delete a bookmark from a workbook
    question: How do I remove a bookmark I no longer need from an untagged workbook?
  phrasing_ops: 60
  slug: sigma-computing-workbooks-api
- baseURL: https://api.sigmacomputing.com
  baseurl_source: declared
  description: The Workspaces API from Sigma Computing — 5 operation(s) for workspaces.
  name: Sigma Computing Workspaces API
  phrasing_intents:
  - id: listWorkspaces
    intent: List workspaces (v2)
    question: What workspaces exist in my organization, using the original v2 list?
  - id: createWorkspace
    intent: Create a workspace
    question: How do I create a new workspace for a project?
  - id: getWorkspace
    intent: Get a workspace
    question: How do I view the details of a single workspace?
  - id: updateWorkspace
    intent: Rename a workspace
    question: How do I rename a workspace?
  - id: deleteWorkspace
    intent: Delete a workspace permanently
    question: Can a deleted workspace be recovered?
  - id: createWorkspaceGrant
    intent: Grant workspace access to users or teams
    question: How do I give a team access to a workspace?
  - id: listWorkspaceGrants
    intent: List permissions on a workspace
    question: Who has access to a workspace and at what level?
  - id: deleteWorkspaceGrant
    intent: Revoke a workspace permission
    question: How do I remove a team's access to a workspace?
  phrasing_ops: 9
  slug: sigma-computing-workspaces-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The allowedIps API from Sigma Computing — 1 operation(s) for allowedips.
  name: Sigma Computing Allowed Ips API
  phrasing_intents:
  - id: v3alpha_listIpAllowlistEntries
    intent: List IP allowlist entries
    question: Which IP addresses and CIDR ranges are on my organization's allowlist?
  phrasing_ops: 1
  slug: sigma-computing-allowedips-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The allowedIps\:batchCreate API from Sigma Computing — 1 operation(s) for allowedips\:batchcreate.
  name: Sigma Computing Allowed Ips\:batch Create API
  phrasing_intents:
  - id: v3alpha_createIpAllowlistEntries
    intent: Add IP addresses to the allowlist
    question: How do I add office IP ranges to our Sigma IP allowlist?
  phrasing_ops: 1
  slug: sigma-computing-allowedips-batchcreate-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The allowedIps\:batchDelete API from Sigma Computing — 1 operation(s) for allowedips\:batchdelete.
  name: Sigma Computing Allowed Ips\:batch Delete API
  phrasing_intents:
  - id: v3alpha_deleteIpAllowlistEntries
    intent: Remove entries from the IP allowlist
    question: How do I remove IP addresses from my organization's allowlist?
  phrasing_ops: 1
  slug: sigma-computing-allowedips-batchdelete-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The api-connectors API from Sigma Computing — 2 operation(s) for api-connectors.
  name: Sigma Computing API Connectors API
  phrasing_intents:
  - id: listApiConnectors
    intent: List API connectors
    question: Which API connectors can I see in Sigma?
  - id: createApiConnector
    intent: Create an API connector
    question: How do I set up Sigma to call an external HTTP endpoint from a workbook action?
  - id: getApiConnector
    intent: Get an API connector's configuration
    question: What request parameters and config does an API connector use?
  - id: updateApiConnector
    intent: Update an API connector
    question: Can I change the credential an existing API connector uses?
  - id: deleteApiConnector
    intent: Archive an API connector
    question: How do I stop an API connector from being used in new workbook actions?
  phrasing_ops: 5
  slug: sigma-computing-api-connectors-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The api-credentials API from Sigma Computing — 2 operation(s) for api-credentials.
  name: Sigma Computing API Credentials API
  phrasing_intents:
  - id: listApiCredentials
    intent: List stored API credentials
    question: Which API credentials are stored for my API connectors?
  - id: createApiCredential
    intent: Store a credential for API connectors
    question: How do I save a secret for use with the Call API action?
  - id: getApiCredential
    intent: Get an API credential's non-secret details
    question: What hosts and description does a stored API credential have?
  - id: updateApiCredential
    intent: Update or rotate an API credential
    question: How do I rotate the secret in a stored API credential?
  - id: deleteApiCredential
    intent: Archive an API credential
    question: How do I retire an API credential so new connectors cannot use it?
  phrasing_ops: 5
  slug: sigma-computing-api-credentials-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The shared_templates API from Sigma Computing — 3 operation(s) for shared_templates.
  name: Sigma Computing Shared Templates API
  phrasing_intents:
  - id: deleteExternalShare
    intent: Remove a template shared with my organization
    question: How do I get rid of a workbook template another organization shared with us?
  - id: acceptTemplateShare
    intent: Accept a pending template share
    question: How do I accept a workbook template shared with my organization?
  - id: listTemplatesSharedWithYou
    intent: List templates shared with my organization
    question: Which workbook templates have been shared with us?
  phrasing_ops: 3
  slug: sigma-computing-shared-templates-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The user-attributes API from Sigma Computing — 8 operation(s) for user-attributes.
  name: Sigma Computing User Attributes API
  phrasing_intents:
  - id: listUserAttributes
    intent: List user attributes
    question: What user attributes are defined in my Sigma organization?
  - id: createUserAttribute
    intent: Create a user attribute
    question: How do I define a new user attribute for row-level security?
  - id: deleteUserAttribute
    intent: Delete a user attribute permanently
    question: Who is allowed to delete a user attribute entirely?
  - id: getUserAttribute
    intent: Get a user attribute
    question: How do I look up the details of one user attribute?
  - id: getUserAttributeTeamAssignments
    intent: List teams assigned a user attribute
    question: Which teams have a value set for a given user attribute?
  - id: updateUserAttributeForTeams
    intent: Bulk-remove a user attribute from teams
    question: Can I clear a user attribute from many teams in one request?
  - id: setUserAttributeForTeams
    intent: Assign a user attribute value to teams
    question: How do I set a user attribute value for several teams at once?
  - id: deleteUserAttributeForTeam
    intent: Remove a user attribute from one team
    question: How do I unset a user attribute for a single team?
  phrasing_ops: 16
  slug: sigma-computing-user-attributes-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The Account Types API from Sigma Computing — 3 operation(s) for account types.
  name: Sigma Computing Account Types API
  phrasing_intents:
  - id: listAccountTypes
    intent: List account types
    question: What account types exist in my Sigma organization?
  - id: createAccountType
    intent: Create a custom account type
    question: How do I create a custom account type with specific permissions?
  - id: deleteAccountType
    intent: Delete a custom account type
    question: Can default Sigma account types be deleted?
  - id: listAccountTypePermissions
    intent: List an account type's permissions
    question: Which feature permissions does an account type grant?
  phrasing_ops: 4
  slug: sigma-computing-account-types-api
- baseURL: https://api.sigmacomputing.com/mcp
  baseurl_source: declared
  description: The Data models API from Sigma Computing — 19 operation(s) for data models.
  name: Sigma Computing Data models API
  phrasing_intents:
  - id: listDataModels
    intent: List the data models in my organization
    question: Which data models exist in Sigma so I can spot duplicates or gaps?
  - id: getDataModel
    intent: Get details of one data model
    question: What are the name, owner and location of a specific data model?
  - id: materializeDataModelElement
    intent: Run a materialization for a data model element now
    question: How do I trigger a materialization of a data model element on demand?
  - id: getDataModelColumns
    intent: List columns across a data model
    question: What columns exist across all elements of a data model?
  - id: listDataModelElements
    intent: List elements in a data model
    question: Which tables and controls make up a data model?
  - id: listDataModelElementColumnSecurityRules
    intent: List column-level security rules on an element
    question: Which column-level security rules protect a data model table?
  - id: createDataModelElementColumnSecurityRules
    intent: Add column-level security rules to an element
    question: How do I hide sensitive columns in a data model from certain users?
  - id: updateDataModelElementColumnSecurityRule
    intent: Replace a column-level security rule
    question: How do I change which columns an existing CLS rule covers?
  phrasing_ops: 24
  slug: sigma-computing-data-models-api
artifact_total: 50
asyncapis:
- description: ''
  name: Sigma Computing Webhooks
  slug: sigma-computing-webhooks
common:
- group: other
  href: https://artifacts.apis.io/sigma-computing/capabilities/sigma-computing-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/sigma-computing-capability-edges.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/sigmacomputing/embed-sdk/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.sigmacomputing.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.sigmacomputing.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.sigmacomputing.com/docs/get-started-with-sigmas-api
- group: docs
  title: ''
  type: APIReference
  url: https://help.sigmacomputing.com/reference/get-started-sigma-api
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sigmacomputing.com/reference/get-started-sigma-api
- group: operate
  title: ''
  type: Support
  url: https://help.sigmacomputing.com/docs/sigma-support
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.sigmacomputing.com/
- group: company
  title: ''
  type: Blog
  url: https://www.sigmacomputing.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sigmacomputing
- group: start
  title: ''
  type: SignUp
  url: https://www.sigmacomputing.com/go/free-trial
- group: start
  title: ''
  type: Login
  url: https://app.sigmacomputing.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sigmacomputing.com/company/contact-us
- group: commercial
  href: https://artifacts.apis.io/sigma-computing/plans/sigma-computing-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sigma-computing-plans-pricing.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sigmacomputing.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sigmacomputing.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sigmacomputing.com
- group: operate
  href: https://artifacts.apis.io/sigma-computing/lifecycle/sigma-computing-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/sigma-computing-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sigma-computing/lifecycle/sigma-computing-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sigma-computing-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://help.sigmacomputing.com/changelog
- group: operate
  href: https://artifacts.apis.io/sigma-computing/changelog/sigma-computing-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/sigma-computing-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sigmacomputing.com/product/vdp
- group: auth
  href: https://artifacts.apis.io/sigma-computing/security/sigma-computing-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sigma-computing-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sigma-computing/security/sigma-computing-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/sigma-computing-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sigma-computing/security/sigma-computing-trust-center.yml
  title: ''
  type: Compliance
  url: security/sigma-computing-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/sigma-computing/security/sigma-computing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sigma-computing-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/sigma-computing/authentication/sigma-computing-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sigma-computing-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sigma-computing/scopes/sigma-computing-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sigma-computing-scopes.yml
- group: design
  href: https://artifacts.apis.io/sigma-computing/conventions/sigma-computing-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sigma-computing-conventions.yml
- group: design
  href: https://artifacts.apis.io/sigma-computing/conventions/sigma-computing-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/sigma-computing-conventions.yml
- group: build
  href: https://artifacts.apis.io/sigma-computing/packages/sigma-computing-packages.yml
  title: ''
  type: Packages
  url: packages/sigma-computing-packages.yml
- group: build
  href: https://artifacts.apis.io/sigma-computing/packages/sigma-computing-packages.yml
  title: ''
  type: SDKs
  url: packages/sigma-computing-packages.yml
- group: build
  href: https://artifacts.apis.io/sigma-computing/cli/sigma-computing-cli.yml
  title: ''
  type: CLI
  url: cli/sigma-computing-cli.yml
- group: design
  href: https://artifacts.apis.io/sigma-computing/components/sigma-computing-components.yml
  title: ''
  type: Components
  url: components/sigma-computing-components.yml
- group: agent
  href: https://artifacts.apis.io/sigma-computing/mcp/sigma-computing-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sigma-computing-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sigma-computing/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/sigma-computing/well-known/sigma-computing-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sigma-computing-well-known.yml
- group: other
  href: https://artifacts.apis.io/sigma-computing/well-known/sigma-computing-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/sigma-computing-api-catalog.json
- group: agent
  href: https://artifacts.apis.io/sigma-computing/llms/sigma-computing-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sigma-computing-llms.txt
- group: design
  href: https://artifacts.apis.io/sigma-computing/conformance/sigma-computing-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sigma-computing-conformance.yml
- group: design
  href: https://artifacts.apis.io/sigma-computing/errors/sigma-computing-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sigma-computing-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/sigma-computing/rate-limits/sigma-computing-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sigma-computing-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/sigma-computing/asyncapi/sigma-computing-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/sigma-computing-webhooks.yml
- group: start
  href: https://artifacts.apis.io/sigma-computing/sandbox/sigma-computing-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/sigma-computing-sandbox.yml
- group: design
  href: https://artifacts.apis.io/sigma-computing/data-model/sigma-computing-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sigma-computing-data-model.yml
- group: other
  href: https://artifacts.apis.io/sigma-computing/overlays/sigma-computing-rest-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sigma-computing-rest-api-overlay.yaml
created: '2026-08-27'
description: Sigma Computing is a warehouse-first analytics and business-application platform. Instead of extracting data into its own store, Sigma queries the customer's cloud data warehouse live — Snowflake, Databricks, BigQuery, Redshift, Amazon Athena, PostgreSQL and ClickHouse — and puts a spreadsheet-style interface, governed data models, input tables with write-back, pixel-perfect paginated reports, embedded white-label analytics and AI agents on top of it. The developer surface is a 274-operation REST API (OpenAPI 3.1) covering workbooks, data models, reports, connections, members, teams, workspaces, permissions, user attributes, tenants, templates and API connectors; a first-party Rust CLI generated from that same OpenAPI; a remote OAuth-protected MCP server that lets AI assistants search, describe and query governed data in natural language; JavaScript embed and plugin SDKs; and three Apache-2.0 agent skills Sigma publishes for Claude Code, Cursor, Codex and Snowflake Cortex Code.
finops:
- has_sources: true
  method: derived
  name: Sigma Computing Finops
  primary_unit: ''
  service_category: ''
  slug: sigma-computing-finops
  template: true
image: https://cdn.sanity.io/images/9i48iita/production/2fcbd9fc0f6c54c2bc25877917e563fe805ad864-1200x630.png
layout: provider
mcp_servers:
- description: Sigma ships a first-party remote MCP server that lets an AI assistant search the organization for workbooks, data models and warehouse tables, describe their columns and semantics, and run governed qu
  name: Sigma MCP Server
  slug: sigma-mcp-server
modified: '2026-08-27'
name: Sigma Computing
nav: Providers
network: true
overview: 'Sigma Computing publishes 36 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Connections API, Credentials API, and 33 more. Tagged areas include Business Intelligence, Analytics, Embedded Analytics, Data Modeling, and Data Warehouse.


  The Sigma Computing catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Sigma Computing''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 40 more developer resources.'
plans:
- name: Sigma Computing Plans Pricing
  plan_count: 0
  slug: sigma-computing-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 6
  name: Sigma Computing Rate Limits
  slug: sigma-computing-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Sigma Computing API Rules
  rule_count: 60
  severity_counts:
    error: 44
    hint: 0
    info: 2
    warn: 14
  slug: sigma-computing-rules
scopes:
- name: Sigma Computing Scopes
  scope_count: 0
  slug: sigma-computing-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 75.1
  coverage:
    artifact_dirs: 31
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 60.5
    contract_governance: 31.8
    contract_quality: 64.3
    developer_ergonomics: 85.7
    discoverability: 80.0
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 74.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 82.4
      total: 34
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
screenshot: https://apis.io/screenshots/sigma-computing/sigma-computing-2026-09-02T155428.png
security:
- kind: authentication
  name: Sigma Computing Authentication
  slug: sigma-computing-authentication
  summary_line: oauth2/http · 3 schemes
- kind: domain-security
  name: Sigma Computing Domain Security
  slug: sigma-computing-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Sigma Computing Vulnerability Disclosure
  slug: sigma-computing-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Sigma Computing Trust Center
  slug: sigma-computing-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO/IEC 27001, ISO/IEC 27017:2015, ISO/IEC 27018:2019, ISO/IEC 27701, HIPAA, GDPR, CCPA, EU-US Data Privacy Framework
skill_count: 3
skills:
- name: sigma-api
  slug: sigma-computing-sigma-api
- name: sigma-cli
  slug: sigma-computing-sigma-cli
- name: sigma-data-models
  slug: sigma-computing-sigma-data-models
slug: sigma-computing
tags:
- Business Intelligence
- Analytics
- Embedded Analytics
- Data Modeling
- Data Warehouse
- Reporting
- Spreadsheets
- MCP
- AI Agents
- Snowflake
- Databricks
- Data Governance
website: https://www.sigmacomputing.com/
---
