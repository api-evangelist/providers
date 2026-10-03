---
access_model:
  confidence: medium
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
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: unknown
    idempotency: documented
    mcp_server: templated
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 111
  human_in_the_loop: 13
  name: Kinde Agentic Access
  operation_count: 179
  slug: kinde-agentic-access
  summary_line: 179 operations · 111 acting · 13 human-in-the-loop
api_count: 2
apis:
- description: The Kinde Management MCP server bridges AI agents and a Kinde account. It is TENANT-SCOPED — the endpoint is https://{subdomain}.kinde.com/mcp, one per Kinde business — and is authenticated with an En
  name: Kinde MCP Server
  slug: kinde-mcp-server
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The API Keys API from Kinde — 3 operation(s) for api keys.
  name: Kinde API Keys API
  phrasing_intents:
  - id: getApiKeys
    intent: List API keys
    question: Which API keys exist in my Kinde business right now?
  - id: createApiKey
    intent: Create an API key
    question: How do I issue a new API key that can call one of my registered APIs?
  - id: getApiKey
    intent: Get an API key's details
    question: Where can I see the details of one specific API key?
  - id: deleteApiKey
    intent: Delete an API key
    question: How do I permanently remove an API key I no longer use?
  - id: rotateApiKey
    intent: Rotate an API key
    question: How do I rotate an API key without losing its permissions?
  - id: verifyApiKey
    intent: Verify an API key
    question: Can I check whether an API key presented to my service is valid?
  phrasing_ops: 6
  slug: kinde-api-keys-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Applications API from Kinde — 7 operation(s) for applications.
  name: Kinde Applications API
  phrasing_intents:
  - id: getApplications
    intent: List applications
    question: Which applications and clients exist in my environment?
  - id: createApplication
    intent: Create an application
    question: How do I create a new application for my frontend or backend?
  - id: getApplication
    intent: Get an application
    question: Can I look up one application's settings by its ID?
  - id: updateApplication
    intent: Update an application's settings
    question: Can I rename an application or change its login and homepage URIs?
  - id: deleteApplication
    intent: Delete an application
    question: How do I delete an application I no longer use?
  - id: GetApplicationConnections
    intent: List an application's auth connections
    question: Which sign-in connections are enabled for a given application?
  - id: EnableConnection
    intent: Enable a connection for an application
    question: How do I turn on an auth connection for one application?
  - id: RemoveConnection
    intent: Turn off a connection for an application
    question: How do I disable an auth connection on one application?
  phrasing_ops: 11
  slug: kinde-applications-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Billing Agreements API from Kinde — 1 operation(s) for billing agreements.
  name: Kinde Billing Agreements API
  phrasing_intents:
  - id: getBillingAgreements
    intent: List a billing customer's agreements
    question: Which billing agreements does a customer currently have?
  - id: createBillingAgreement
    intent: Move a customer onto a billing plan
    question: How do I switch a billing customer to a new plan?
  phrasing_ops: 2
  slug: kinde-billing-agreements-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Billing API from Kinde — 2 operation(s) for billing.
  name: Kinde Billing API
  phrasing_intents:
  - id: GetEntitlements
    intent: List the signed-in user's entitlements
    question: What billing entitlements does the current user have access to?
  - id: GetEntitlement
    intent: Get one entitlement by feature key
    question: Can I check whether the signed-in user has a specific feature entitlement?
  phrasing_ops: 2
  slug: kinde-billing-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Billing Entitlements API from Kinde — 1 operation(s) for billing entitlements.
  name: Kinde Billing Entitlements API
  phrasing_intents:
  - id: getBillingEntitlements
    intent: List a billing customer's entitlements
    question: What features is a given billing customer entitled to?
  phrasing_ops: 1
  slug: kinde-billing-entitlements-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Billing Meter Usage API from Kinde — 1 operation(s) for billing meter usage.
  name: Kinde Billing Meter Usage API
  phrasing_intents:
  - id: createMeterUsageRecord
    intent: Record metered usage for a customer
    question: What's the way to report usage for a metered billing feature?
  phrasing_ops: 1
  slug: kinde-billing-meter-usage-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Business API from Kinde — 1 operation(s) for business.
  name: Kinde Business API
  phrasing_intents:
  - id: getBusiness
    intent: Get my business details
    question: What business details are stored on my Kinde account?
  - id: updateBusiness
    intent: Update my business details
    question: How do I change my business name or contact email?
  phrasing_ops: 2
  slug: kinde-business-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Callbacks API from Kinde — 2 operation(s) for callbacks.
  name: Kinde Callbacks API
  phrasing_intents:
  - id: getCallbackURLs
    intent: List an app's redirect callback URLs
    question: Which callback URLs can users be redirected to after signing in to my app?
  - id: addRedirectCallbackURLs
    intent: Add redirect callback URLs
    question: Can I add another sign-in callback URL without removing the existing ones?
  - id: replaceRedirectCallbackURLs
    intent: Replace all redirect callback URLs
    question: Is there a way to overwrite the entire list of sign-in callback URLs for an app?
  - id: deleteCallbackURLs
    intent: Delete redirect callback URLs
    question: How do I remove specific sign-in callback URLs from an application?
  - id: getLogoutURLs
    intent: List an app's logout redirect URLs
    question: Where can users be sent after they log out of my app?
  - id: addLogoutRedirectURLs
    intent: Add logout redirect URLs
    question: Can I add a new post-logout URL while keeping the current ones?
  - id: replaceLogoutRedirectURLs
    intent: Replace all logout redirect URLs
    question: Is there a call that overwrites the whole list of post-logout URLs for an app?
  - id: deleteLogoutURLs
    intent: Delete logout redirect URLs
    question: How do I remove a logout redirect URL from an app?
  phrasing_ops: 8
  slug: kinde-callbacks-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Connected Apps API from Kinde — 3 operation(s) for connected apps.
  name: Kinde Connected Apps API
  phrasing_intents:
  - id: GetConnectedAppAuthUrl
    intent: Get a connected app authorization URL
    question: Where do I send a user to authorize a third-party connected app?
  - id: GetConnectedAppToken
    intent: Get a connected app access token
    question: What gives me an access token to call the third-party provider behind a connected app?
  - id: RevokeConnectedAppToken
    intent: Revoke a connected app session's tokens
    question: How do I disconnect a user's third-party connected app session?
  phrasing_ops: 3
  slug: kinde-connected-apps-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Connections API from Kinde — 2 operation(s) for connections.
  name: Kinde Connections API
  phrasing_intents:
  - id: GetConnections
    intent: List authentication connections
    question: Which authentication connections are set up in my environment?
  - id: CreateConnection
    intent: Create an authentication connection
    question: How do I set up a new enterprise or social sign-in connection?
  - id: GetConnection
    intent: Get an authentication connection
    question: Can I view the configuration of a single connection?
  - id: UpdateConnection
    intent: Partially update a connection
    question: Can I just rename a connection or change its display name?
  - id: ReplaceConnection
    intent: Replace a connection's whole configuration
    question: How do I replace a connection's entire config in one call?
  - id: deleteConnection
    intent: Delete an authentication connection
    question: How do I delete a sign-in connection I no longer need?
  phrasing_ops: 6
  slug: kinde-connections-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Directories API from Kinde — 2 operation(s) for directories.
  name: Kinde Directories API
  phrasing_intents:
  - id: getDirectories
    intent: List SCIM directories
    question: Which SCIM directories are syncing users into my account?
  - id: createDirectory
    intent: Create a SCIM directory
    question: How do I set up SCIM provisioning for an organization?
  - id: getDirectory
    intent: Get a SCIM directory
    question: Can I view the details of one SCIM directory?
  - id: updateDirectory
    intent: Rename a SCIM directory
    question: Can I rename an existing SCIM directory?
  - id: deleteDirectory
    intent: Delete a SCIM directory
    question: What happens to synced data when I delete a SCIM directory?
  phrasing_ops: 5
  slug: kinde-directories-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Environment variables API from Kinde — 2 operation(s) for environment variables.
  name: Kinde Environment variables API
  phrasing_intents:
  - id: getEnvironmentVariables
    intent: List environment variables
    question: Which environment variables are defined in my environment?
  - id: createEnvironmentVariable
    intent: Create an environment variable
    question: How do I store a secret value as an environment variable?
  - id: getEnvironmentVariable
    intent: Get an environment variable
    question: Can I read one environment variable by its ID?
  - id: updateEnvironmentVariable
    intent: Update an environment variable
    question: Can I change the value of an existing environment variable?
  - id: deleteEnvironmentVariable
    intent: Delete an environment variable
    question: How do I delete an environment variable I no longer need?
  phrasing_ops: 5
  slug: kinde-environment-variables-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Environments API from Kinde — 5 operation(s) for environments.
  name: Kinde Environments API
  phrasing_intents:
  - id: getEnvironment
    intent: Get the current environment
    question: Which environment am I currently working in?
  - id: DeleteEnvironementFeatureFlagOverrides
    intent: Clear all environment flag overrides
    question: How do I reset every feature flag override in the environment?
  - id: GetEnvironementFeatureFlags
    intent: List environment feature flags
    question: What feature flag values apply at the environment level?
  - id: DeleteEnvironementFeatureFlagOverride
    intent: Clear one environment flag override
    question: Can I remove the environment override for just one feature flag?
  - id: UpdateEnvironementFeatureFlagOverride
    intent: Override a flag for the environment
    question: How do I change a feature flag's value for the whole environment?
  - id: ReadLogo
    intent: Get the environment's logos
    question: Which logos are configured for my environment?
  - id: AddLogo
    intent: Upload an environment logo
    question: How do I upload a logo for my environment's sign-in pages?
  - id: DeleteLogo
    intent: Delete an environment logo
    question: How do I remove a logo from my environment?
  phrasing_ops: 8
  slug: kinde-environments-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Feature flags API from Kinde — 3 operation(s) for feature flags.
  name: Kinde Feature flags API
  phrasing_intents:
  - id: GetFeatureFlags
    intent: List flags affecting the signed-in user
    question: Which feature flags apply to the currently logged-in user?
  - id: CreateFeatureFlag
    intent: Create a feature flag
    question: How do I create a new feature flag with a default value?
  - id: DeleteFeatureFlag
    intent: Delete a feature flag
    question: Is it possible to delete a feature flag entirely?
  - id: UpdateFeatureFlag
    intent: Replace a feature flag definition
    question: Can I change a feature flag's default value or type after creating it?
  phrasing_ops: 4
  slug: kinde-feature-flags-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Identities API from Kinde — 1 operation(s) for identities.
  name: Kinde Identities API
  phrasing_intents:
  - id: GetIdentity
    intent: Get an identity
    question: Can I look up a single sign-in identity by its ID?
  - id: UpdateIdentity
    intent: Make an identity primary
    question: How do I set an identity as the user's primary one?
  - id: DeleteIdentity
    intent: Delete an identity
    question: How do I remove one sign-in identity from a user?
  phrasing_ops: 3
  slug: kinde-identities-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Industries API from Kinde — 1 operation(s) for industries.
  name: Kinde Industries API
  phrasing_intents:
  - id: getIndustries
    intent: List industries and their keys
    question: What industry keys can I use for my business profile?
  phrasing_ops: 1
  slug: kinde-industries-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The MFA API from Kinde — 1 operation(s) for mfa.
  name: Kinde MFA API
  phrasing_intents:
  - id: ReplaceMFA
    intent: Replace the environment MFA policy
    question: Is there a way to require multi-factor authentication across my environment?
  phrasing_ops: 1
  slug: kinde-mfa-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Organizations API from Kinde — 25 operation(s) for organizations.
  name: Kinde Organizations API
  phrasing_intents:
  - id: getOrganizationInvites
    intent: List an organization's invitations
    question: Which invitations are still pending for an organization?
  - id: createOrganizationInvite
    intent: Invite someone to an organization
    question: What's the way to invite a new person to join an organization with a role?
  - id: getOrganizationInvite
    intent: Get an organization invitation
    question: Can I check the status of one specific invitation?
  - id: deleteOrganizationInvite
    intent: Revoke an organization invitation
    question: How do I cancel an invitation before it's accepted?
  - id: getOrganization
    intent: Get an organization
    question: Can I look up an organization's details by its code?
  - id: createOrganization
    intent: Create an organization
    question: How do I create a new organization for a customer tenant?
  - id: getOrganizations
    intent: List organizations
    question: Which organizations exist in my business?
  - id: updateOrganization
    intent: Update an organization's settings
    question: Can I suspend an organization or enforce MFA for its members?
  phrasing_ops: 40
  slug: kinde-organizations-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Permissions API from Kinde — 3 operation(s) for permissions.
  name: Kinde Permissions API
  phrasing_intents:
  - id: GetUserPermissions
    intent: List the signed-in user's permissions
    question: What permissions does the currently logged-in user have?
  - id: GetPermissions
    intent: List all defined permissions
    question: Which permissions are defined across my business?
  - id: CreatePermission
    intent: Create a permission
    question: How do I define a new permission like create:invoices?
  - id: UpdatePermissions
    intent: Update a permission
    question: Can I rename a permission or change its key?
  - id: DeletePermission
    intent: Delete a permission
    question: How do I delete a permission definition?
  phrasing_ops: 5
  slug: kinde-permissions-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Properties API from Kinde — 3 operation(s) for properties.
  name: Kinde Properties API
  phrasing_intents:
  - id: GetUserProperties
    intent: List the signed-in user's properties
    question: What custom properties are stored for the logged-in user?
  - id: GetProperties
    intent: List property definitions
    question: Which custom properties have I defined?
  - id: CreateProperty
    intent: Create a custom property
    question: How do I define a new custom property for users or organizations?
  - id: UpdateProperty
    intent: Update a property definition
    question: Can I rename a custom property or move it to another category?
  - id: DeleteProperty
    intent: Delete a property definition
    question: How do I delete a custom property definition?
  phrasing_ops: 5
  slug: kinde-properties-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Property Categories API from Kinde — 2 operation(s) for property categories.
  name: Kinde Property Categories API
  phrasing_intents:
  - id: GetCategories
    intent: List property categories
    question: Which property categories exist?
  - id: CreateCategory
    intent: Create a property category
    question: How do I create a category to group custom properties?
  - id: UpdateCategory
    intent: Rename a property category
    question: Can I rename an existing property category?
  phrasing_ops: 3
  slug: kinde-property-categories-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Roles API from Kinde — 7 operation(s) for roles.
  name: Kinde Roles API
  phrasing_intents:
  - id: GetUserRoles
    intent: List the signed-in user's roles
    question: Which roles does the currently logged-in user hold?
  - id: GetRoles
    intent: List all roles
    question: Which roles are defined in my business?
  - id: CreateRole
    intent: Create a role
    question: How do I create a new role like admin or editor?
  - id: GetRole
    intent: Get a role
    question: Can I look up one role by its ID?
  - id: UpdateRoles
    intent: Update a role
    question: Can I rename a role or change its key?
  - id: DeleteRole
    intent: Delete a role
    question: How do I delete a role I no longer use?
  - id: GetRoleScopes
    intent: List a role's API scopes
    question: Which API scopes are attached to a role?
  - id: AddRoleScope
    intent: Add an API scope to a role
    question: How do I grant an API scope to everyone with a role?
  phrasing_ops: 12
  slug: kinde-roles-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Search API from Kinde — 1 operation(s) for search.
  name: Kinde Search API
  phrasing_intents:
  - id: searchUsers
    intent: Search users
    question: Can I search my users by name or email?
  phrasing_ops: 1
  slug: kinde-search-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Self-serve portal API from Kinde — 1 operation(s) for self-serve portal.
  name: Kinde Self-serve portal API
  phrasing_intents:
  - id: GetPortalLink
    intent: Get a self-serve portal link
    question: Where can I send the signed-in user to manage their own account and billing?
  phrasing_ops: 1
  slug: kinde-self-serve-portal-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Subscribers API from Kinde — 2 operation(s) for subscribers.
  name: Kinde Subscribers API
  phrasing_intents:
  - id: GetSubscribers
    intent: List subscribers
    question: Who has subscribed to my mailing list?
  - id: CreateSubscriber
    intent: Add a subscriber
    question: How do I add someone as a subscriber?
  - id: GetSubscriber
    intent: Get a subscriber
    question: Can I look up one subscriber's record?
  phrasing_ops: 3
  slug: kinde-subscribers-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Timezones API from Kinde — 1 operation(s) for timezones.
  name: Kinde Timezones API
  phrasing_intents:
  - id: getTimezones
    intent: List timezones and their keys
    question: What timezone keys can I set on my business?
  phrasing_ops: 1
  slug: kinde-timezones-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Users API from Kinde — 11 operation(s) for users.
  name: Kinde Users API
  phrasing_intents:
  - id: getUsers
    intent: List users
    question: Which users exist in my business?
  - id: refreshUserClaims
    intent: Refresh a user's token claims
    question: How do I make a user's new roles show up in their tokens right away?
  - id: getUserData
    intent: Get a user
    question: Can I look up a single user's record by ID?
  - id: createUser
    intent: Create a user
    question: How do I create a user with an email identity?
  - id: updateUser
    intent: Update a user
    question: Can I suspend a user or force them to reset their password?
  - id: deleteUser
    intent: Delete a user
    question: How do I delete a user account?
  - id: UpdateUserFeatureFlagOverride
    intent: Override a feature flag for a user
    question: How do I turn a feature on for one specific user?
  - id: UpdateUserProperty
    intent: Set one user property
    question: How do I set a single custom property value on a user?
  phrasing_ops: 18
  slug: kinde-users-api
- baseURL: https://{subdomain}.kinde.com/api/v1
  baseurl_source: declared
  description: The Webhooks API from Kinde — 4 operation(s) for webhooks.
  name: Kinde Webhooks API
  phrasing_intents:
  - id: GetEvent
    intent: Get a webhook event
    question: Can I fetch the payload of a specific event that fired?
  - id: GetEventTypes
    intent: List webhook event types
    question: Which event types can a webhook subscribe to?
  - id: DeleteWebHook
    intent: Delete a webhook
    question: How do I delete a webhook I no longer need?
  - id: UpdateWebHook
    intent: Update a webhook
    question: Can I change which events an existing webhook listens for?
  - id: GetWebHooks
    intent: List webhooks
    question: Which webhooks are configured?
  - id: CreateWebHook
    intent: Create a webhook
    question: How do I get notified at my endpoint when a user signs up?
  phrasing_ops: 6
  slug: kinde-webhooks-api
- baseURL: https://{subdomain}.kinde.com/mcp
  baseurl_source: declared
  description: The APIs API from Kinde — 6 operation(s) for apis.
  name: Kinde APIs API
  phrasing_intents:
  - id: getAPIs
    intent: List registered APIs
    question: Which APIs have I registered in Kinde?
  - id: addAPIs
    intent: Register a new API
    question: How do I register my backend API so it can receive access tokens?
  - id: getAPI
    intent: Get a registered API
    question: Can I view the configuration of one registered API?
  - id: deleteAPI
    intent: Delete a registered API
    question: How do I remove an API I registered but no longer need?
  - id: getAPIScopes
    intent: List an API's scopes
    question: Which scopes are defined on one of my APIs?
  - id: addAPIScope
    intent: Create a scope on an API
    question: How do I define a new scope like read:orders on my API?
  - id: getAPIScope
    intent: Get one API scope
    question: Can I look up a single scope on an API by its ID?
  - id: updateAPIScope
    intent: Update an API scope's description
    question: Can I change the description of an existing API scope?
  phrasing_ops: 12
  slug: kinde-apis-api
- baseURL: https://{subdomain}.kinde.com/mcp
  baseurl_source: declared
  description: The OAuth API from Kinde — 3 operation(s) for oauth.
  name: Kinde O Auth API
  phrasing_intents:
  - id: getUserProfileV2
    intent: Get the signed-in user's profile
    question: How do I get the logged-in user's name, email and picture?
  - id: tokenIntrospection
    intent: Introspect a token
    question: Can I check whether an access token is still active?
  - id: tokenRevocation
    intent: Revoke an access or refresh token
    question: How do I invalidate a refresh token so it can't be used again?
  phrasing_ops: 3
  slug: kinde-oauth-api
arazzos:
- description: Find an existing user by email and grant them a role within an organization.
  name: Kinde Assign Organization User Role
  slug: kinde-assign-org-user-role-workflow
- description: Stand up a new organization and seed it with existing users and roles.
  name: Kinde Create Organization with Users
  slug: kinde-create-organization-with-users-workflow
- description: Create a permission, create a role, and attach the permission to the role.
  name: Kinde Create Role with Permission
  slug: kinde-create-role-with-permission-workflow
- description: Read the signed-in user's profile, roles, and entitlements, then mint a self-serve portal link.
  name: Kinde End User Self-Serve Portal
  slug: kinde-end-user-self-serve-portal-workflow
- description: Validate roles, create an organization invitation, and poll until it is sent.
  name: Kinde Invite User to Organization
  slug: kinde-invite-user-to-organization-workflow
- description: Create a user with an email identity and import their existing hashed password.
  name: Kinde Migrate User with Password
  slug: kinde-migrate-user-with-password-workflow
- description: Create a user, add them to an organization, and grant a role in one pass.
  name: Kinde Provision User into Organization
  slug: kinde-provision-user-workflow
- description: Create an application, set its callback URLs, create a social connection, and enable it.
  name: Kinde Register Application with Connection
  slug: kinde-register-application-with-connection-workflow
- description: Create an org-overridable feature flag and set its value for one organization.
  name: Kinde Roll Out Feature Flag to Organization
  slug: kinde-rollout-feature-flag-workflow
artifact_total: 103
collections:
- collection_type: postman
  name: Kinde Account API
  slug: postman-kinde-frontend-api
- collection_type: postman
  name: Kinde Management API
  slug: postman-kinde-management-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Kinde Account API Keys API
  slug: open-kinde-api-keys-api
- collection_type: open
  name: Kinde Account API Keys APIs API
  slug: open-kinde-apis-api
- collection_type: open
  name: Kinde Account API Keys Applications API
  slug: open-kinde-applications-api
- collection_type: open
  name: Kinde Account API Keys Billing Agreements API
  slug: open-kinde-billing-agreements-api
- collection_type: open
  name: Kinde Account API Keys Billing API
  slug: open-kinde-billing-api
- collection_type: open
  name: Kinde Account API Keys Billing Entitlements API
  slug: open-kinde-billing-entitlements-api
- collection_type: open
  name: Kinde Account API Keys Billing Meter Usage API
  slug: open-kinde-billing-meter-usage-api
- collection_type: open
  name: Kinde Account API Keys Business API
  slug: open-kinde-business-api
- collection_type: open
  name: Kinde Account API Keys Callbacks API
  slug: open-kinde-callbacks-api
- collection_type: open
  name: Kinde Account API Keys Connected Apps API
  slug: open-kinde-connected-apps-api
- collection_type: open
  name: Kinde Account API Keys Connections API
  slug: open-kinde-connections-api
- collection_type: open
  name: Kinde Account API Keys Directories API
  slug: open-kinde-directories-api
- collection_type: open
  name: Kinde Account API Keys Environment variables API
  slug: open-kinde-environment-variables-api
- collection_type: open
  name: Kinde Account API Keys Environments API
  slug: open-kinde-environments-api
- collection_type: open
  name: Kinde Account API Keys Feature flags API
  slug: open-kinde-feature-flags-api
- collection_type: open
  name: Kinde Account API
  slug: open-kinde-frontend-api
- collection_type: open
  name: Kinde Account API Keys Identities API
  slug: open-kinde-identities-api
- collection_type: open
  name: Kinde Account API Keys Industries API
  slug: open-kinde-industries-api
- collection_type: open
  name: Kinde Management API
  slug: open-kinde-management-api
- collection_type: open
  name: Kinde Account API Keys MFA API
  slug: open-kinde-mfa-api
- collection_type: open
  name: Kinde Account API Keys OAuth API
  slug: open-kinde-oauth-api
- collection_type: open
  name: Kinde Account API Keys Organizations API
  slug: open-kinde-organizations-api
- collection_type: open
  name: Kinde Account API Keys Permissions API
  slug: open-kinde-permissions-api
- collection_type: open
  name: Kinde Account API Keys Properties API
  slug: open-kinde-properties-api
- collection_type: open
  name: Kinde Account API Keys Property Categories API
  slug: open-kinde-property-categories-api
- collection_type: open
  name: Kinde Account API Keys Roles API
  slug: open-kinde-roles-api
- collection_type: open
  name: Kinde Account API Keys Search API
  slug: open-kinde-search-api
- collection_type: open
  name: Kinde Account API Keys Self-serve portal API
  slug: open-kinde-self-serve-portal-api
- collection_type: open
  name: Kinde Account API Keys Subscribers API
  slug: open-kinde-subscribers-api
- collection_type: open
  name: Kinde Account API Keys Timezones API
  slug: open-kinde-timezones-api
- collection_type: open
  name: Kinde Account API Keys Users API
  slug: open-kinde-users-api
- collection_type: open
  name: Kinde Account API Keys Webhooks API
  slug: open-kinde-webhooks-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.kinde.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/agentic-access/kinde-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kinde-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/security/kinde-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/kinde-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/security/kinde-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kinde-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/security/kinde-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kinde-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/authentication/kinde-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kinde-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/kinde/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-assign-org-user-role-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-assign-org-user-role-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-create-organization-with-users-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-create-organization-with-users-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-create-role-with-permission-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-create-role-with-permission-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-end-user-self-serve-portal-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-end-user-self-serve-portal-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-invite-user-to-organization-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-invite-user-to-organization-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-migrate-user-with-password-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-migrate-user-with-password-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-provision-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-provision-user-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-register-application-with-connection-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-register-application-with-connection-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/arazzo/kinde-rollout-feature-flag-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kinde-rollout-feature-flag-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://docs.kinde.com
- group: start
  title: ''
  type: Login
  url: https://app.kinde.com/admin
- group: start
  title: ''
  type: Signup
  url: https://app.kinde.com/register
- group: commercial
  title: ''
  type: Pricing
  url: https://kinde.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://kinde.com/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.kinde.com
- group: operate
  title: ''
  type: StatusPageRSS
  url: https://status.kinde.com/history.rss
- group: operate
  title: ''
  type: StatusPageAtom
  url: https://status.kinde.com/history.atom
- group: operate
  title: ''
  type: ChangeLog
  url: https://updates.kinde.com
- group: operate
  title: ''
  type: RoadMap
  url: https://updates.kinde.com/board
- group: build
  title: ''
  type: GitHub
  url: https://github.com/kinde-oss
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.kinde.com/trust-center/agreements/terms-of-service/
- group: auth
  title: ''
  type: TrustCenter
  url: https://docs.kinde.com/trust-center/
- group: operate
  title: ''
  type: Support
  url: mailto:support@kinde.com
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/plans/kinde-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kinde-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/rate-limits/kinde-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kinde-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/finops/kinde-finops.yml
  title: ''
  type: FinOps
  url: finops/kinde-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/vocabulary/kinde-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/kinde-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/json-ld/kinde-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/kinde-context.jsonld
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-typescript-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-auth-nextjs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-auth-react
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-auth-pkce-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-nodejs-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-node-express
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-node-express-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-remix-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-auth-remix-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-sveltekit-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/nuxt-kinde
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-tsr
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-java-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-dotnet-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-php-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-ruby-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-elixir-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-auth-wordpress
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-flutter-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-sdk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-sdk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/expo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/kinde-react-native-sdk-0-7x
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kinde-oss/management-api-js
- group: build
  title: ''
  type: CLI
  url: https://github.com/kinde-oss/kinde-cli
- group: build
  title: ''
  type: CLI
  url: https://github.com/kinde-oss/homebrew-kinde-cli
- group: build
  title: ''
  type: CLI
  url: https://github.com/kinde-oss/scoop-kinde-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/jwt-validator
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/jwt-decoder
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/js-utils
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/webhook
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/kinde-translations
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/infrastructure
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/workflows-runtime
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/terraform-provider-kinde
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/kinde-convex-sync
- group: build
  title: ''
  type: Tools
  url: https://github.com/kinde-oss/kinde-convex-billing
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/kinde-oss/documentation
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.kinde.com/llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/packages/kinde-packages.yml
  title: ''
  type: Packages
  url: packages/kinde-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/packages/kinde-packages.yml
  title: ''
  type: SDKs
  url: packages/kinde-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/well-known/kinde-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kinde-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/well-known/kinde-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kinde-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/security/kinde-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/kinde-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/conformance/kinde-conformance.yml
  title: ''
  type: Compliance
  url: conformance/kinde-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/conformance/kinde-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kinde-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/conventions/kinde-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kinde-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/conventions/kinde-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/kinde-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/errors/kinde-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kinde-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/lifecycle/kinde-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kinde-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/lifecycle/kinde-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/kinde-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/scopes/kinde-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/kinde-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/data-model/kinde-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kinde-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/sandbox/kinde-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/kinde-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/changelog/kinde-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kinde-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/cli/kinde-cli.yml
  title: ''
  type: CLI
  url: cli/kinde-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/components/kinde-components.yml
  title: ''
  type: Components
  url: components/kinde-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/webhooks/kinde-webhooks.yml
  title: ''
  type: Webhooks
  url: webhooks/kinde-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/llms/kinde-www-llms.txt
  title: ''
  type: LlmsText
  url: llms/kinde-www-llms.txt
- group: operate
  title: ''
  type: HelpCenter
  url: https://kinde.com/support/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kinde.com/kinde-apis/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.kinde.com/trust-center/privacy-and-compliance/privacy-policy/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.kinde.com/trust-center/privacy-and-compliance/compliance/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/overlays/kinde-management-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kinde-management-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/overlays/kinde-account-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kinde-account-api-overlay.yaml
created: '2026-05-22'
description: Kinde is a developer-first authentication and customer identity platform that bundles authentication (passwords, passwordless, social, enterprise SSO), authorization (roles, permissions, scopes), B2B organizations, billing, and feature flags into a single integrated product. Founded in Australia, Kinde positions itself as "the fully integrated developer platform — secure and monetize your product from day one" and is used by over 70,000 developers. The platform exposes a Management API for tenant administration and an Account API for end-user self-service flows, both backed by published OpenAPI specs and a large open-source SDK ecosystem on GitHub (TypeScript, React, Next.js, Python, Go, Java, .NET, PHP, Ruby, Elixir, Flutter, iOS, Android, Expo, React Native, SvelteKit, Nuxt, Remix, TanStack Start) plus a Go-based CLI, a Terraform provider, and a Model Context Protocol (MCP) server for AI agents.
examples:
- key_count: 2
  name: Kinde Create Application Example
  slug: kinde-create-application-example
- key_count: 2
  name: Kinde Create Feature Flag Example
  slug: kinde-create-feature-flag-example
- key_count: 2
  name: Kinde Create Organization Example
  slug: kinde-create-organization-example
- key_count: 2
  name: Kinde Create Role Example
  slug: kinde-create-role-example
- key_count: 2
  name: Kinde Create User Example
  slug: kinde-create-user-example
- key_count: 2
  name: Kinde Create Webhook Example
  slug: kinde-create-webhook-example
finops:
- name: Kinde Finops
  service_category: Identity
  slug: kinde-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kinde.png
json_schemas:
- name: Application
  property_count: 10
  slug: kinde-application
- name: FeatureFlag
  property_count: 6
  slug: kinde-feature-flag
- name: Organization
  property_count: 11
  slug: kinde-organization
- name: Permission
  property_count: 4
  slug: kinde-permission
- name: Role
  property_count: 5
  slug: kinde-role
- name: User
  property_count: 15
  slug: kinde-user
- name: Webhook
  property_count: 8
  slug: kinde-webhook
json_structures:
- name: Kinde Organization Structure
  property_count: 0
  slug: kinde-organization-structure
- name: Kinde User Structure
  property_count: 0
  slug: kinde-user-structure
jsonld:
- class_count: 36
  name: Kinde Context
  property_count: 9
  slug: kinde-context
layout: provider
mcp_servers:
- description: 'Kinde ships TWO distinct MCP surfaces and they must not be conflated. (1) The Kinde Management MCP Server: a Kinde-authored remote MCP server exposing a read-and-create subset of the Kinde Management '
  name: Kinde MCP Server
  slug: kinde-mcp-server
modified: '2026-09-12'
name: Kinde
nav: Providers
network: true
overview: 'Kinde publishes 31 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Applications API, Billing Agreements API, and 28 more. Tagged areas include Authentication, Authorization, Customer Identity, Identity Management, and OpenID Connect.


  The Kinde catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Kinde''s developer surface includes authentication, developer portal, signup flow, pricing, engineering blog, changelog, GitHub presence, and 96 more developer resources.'
plans:
- name: Kinde Plans Pricing
  plan_count: 5
  slug: kinde-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Kinde Rate Limits
  slug: kinde-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Kinde API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: kinde-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Kinde API Rules
  rule_count: 12
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 8
  slug: kinde-rules
scopes:
- name: Kinde Scopes
  scope_count: 0
  slug: kinde-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 88.0
  coverage:
    artifact_dirs: 37
    catalog_earned: 88.8
    catalog_earned_first_party: 12.0
    catalog_gap: 26.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 90.3
    contract_governance: 45.5
    contract_quality: 68.2
    developer_ergonomics: 91.1
    discoverability: 68.3
    operational_transparency: 92.1
  previous_composite: 87.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 90.0
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 66.7
screenshot: https://raw.githubusercontent.com/api-evangelist/kinde/refs/heads/main/screenshots/kinde-2026-06-20T184038.png
security:
- kind: authentication
  name: Kinde Authentication
  slug: kinde-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kinde Domain Security
  slug: kinde-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kinde Vulnerability Disclosure
  slug: kinde-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Kinde Trust Center
  slug: kinde-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: kinde
tags:
- Authentication
- Authorization
- Customer Identity
- Identity Management
- OpenID Connect
- SSO
- Multi-Factor Authentication
- Role-Based Access Control
- Feature Flags
- Billing
- B2B
- Software-as-a-Service
- Developer Platform
website: https://www.kinde.com/
---
