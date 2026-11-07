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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: verified
    mcp_server: verified
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
  score: 46.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 271
  human_in_the_loop: 15
  name: Clerk Com Agentic Access
  operation_count: 428
  slug: clerk-com-agentic-access
  summary_line: 428 operations · 271 acting · 15 human-in-the-loop
api_count: 8
apis:
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The Account Portal API from Clerk — 1 operation(s) for account portal.
  name: Clerk Account Portal API
  phrasing_intents:
  - id: getAccountPortal
    intent: Get the account portal settings
    question: How does my frontend get the hosted account portal configuration?
  phrasing_ops: 1
  slug: clerk-com-account-portal-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with the sessions of the current user.
  name: Clerk Active Sessions API
  phrasing_intents:
  - id: getSessions
    intent: List my active sessions with activity
    question: Which devices am I currently signed in on, with their recent activity?
  - id: revokeSession
    intent: Sign out one of my sessions
    question: How do I sign myself out of a device I no longer use?
  - id: getUsersSessions
    intent: List all my sessions
    question: How do I get every session of the current user, not just active ones?
  phrasing_ops: 3
  slug: clerk-com-active-sessions-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Allow your users to sign in on behalf of other users.
  name: Clerk Actor Tokens API
  phrasing_intents:
  - id: CreateActorToken
    intent: Create an actor token to impersonate a user
    question: How do I let a support agent impersonate a user?
  - id: RevokeActorToken
    intent: Revoke a pending actor token
    question: How do I cancel an impersonation token before it's used?
  phrasing_ops: 2
  slug: clerk-com-actor-tokens-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Tasks that allow creating user sessions for agent-based interactions.
  name: Clerk Agent Tasks API
  phrasing_intents:
  - id: CreateAgentTask
    intent: Create an agent task acting for a user
    question: How do I let an AI agent act on behalf of a user with a session link?
  - id: RevokeAgentTask
    intent: Revoke a pending agent task
    question: How do I cancel an agent task before the agent uses its link?
  phrasing_ops: 2
  slug: clerk-com-agent-tasks-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Allow-lists and Block-lists allow you to control who can sign up or sign in to your application, by restricting access based on the user's email address or phone number.
  name: Clerk Allow-list / Block-list API
  phrasing_intents:
  - id: ListAllowlistIdentifiers
    intent: List allow-listed identifiers
    question: Which email addresses or domains are allowed to sign up to my app?
  - id: CreateAllowlistIdentifier
    intent: Allow an identifier to sign up
    question: How do I let a specific email or domain sign up to a restricted app?
  - id: DeleteAllowlistIdentifier
    intent: Remove an identifier from the allow-list
    question: How do I take someone off the sign-up allow-list?
  - id: ListBlocklistIdentifiers
    intent: List blocked identifiers
    question: Which emails or domains are blocked from accessing my app?
  - id: CreateBlocklistIdentifier
    intent: Block an identifier from access
    question: How do I block a disposable email domain from my app?
  - id: DeleteBlocklistIdentifier
    intent: Remove an identifier from the block-list
    question: How do I unblock an email or domain I blocked earlier?
  phrasing_ops: 6
  slug: clerk-com-allow-list-block-list-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Endpoints for managing API Keys
  name: Clerk API Keys API
  phrasing_intents:
  - id: createApiKey
    intent: Create an API key
    question: How do I issue an API key to one of my users?
  - id: getApiKeys
    intent: List API keys for a subject
    question: Which API keys have been issued to a given user or organization?
  - id: getApiKey
    intent: Retrieve an API key by ID
    question: How do I look up the metadata of an API key by its ID?
  - id: updateApiKey
    intent: Update an API key's scopes or expiry
    question: How do I change the scopes on an existing API key?
  - id: deleteApiKey
    intent: Delete an API key
    question: How do I permanently delete an API key record?
  - id: getApiKeySecret
    intent: Reveal an API key's secret
    question: How do I retrieve the secret value of an API key?
  - id: revokeApiKey
    intent: Revoke an API key
    question: How do I revoke a leaked API key so it stops working?
  - id: verifyApiKey
    intent: Verify an API key secret
    question: How do I check whether an API key presented to my service is valid?
  phrasing_ops: 8
  slug: clerk-com-api-keys-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: 'An object representing a transfer request for an application between workspaces. The high-level flow for application transfer: 1. The initial workspace can create an application transfer. A single-use'
  name: Clerk Application Transfers API
  phrasing_intents:
  - id: PlatformListApplicationTransfers
    intent: List application transfers my workspace created
    question: Which application ownership transfers has my workspace started?
  - id: PlatformCreateApplicationTransfer
    intent: Start transferring an application to another workspace
    question: How do I hand an application over to another workspace?
  - id: PlatformGetApplicationTransfer
    intent: Get an application transfer
    question: Has the other workspace accepted my application transfer yet?
  - id: PlatformCancelApplicationTransfer
    intent: Cancel a pending application transfer
    question: How do I cancel an application transfer I started by mistake?
  phrasing_ops: 4
  slug: clerk-com-application-transfers-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: An object representing a Clerk application. Each `application` can have multiple `instances`, typically one for development and one for production, each with distinct user pools.
  name: Clerk Applications API
  phrasing_intents:
  - id: PlatformListApplications
    intent: List my Clerk applications
    question: Which applications exist in my Clerk workspace?
  - id: PlatformCreateApplication
    intent: Create a new application
    question: How do I spin up a new Clerk application programmatically?
  - id: PlatformGetApplication
    intent: Get an application's details
    question: What instances and settings does one of my applications have?
  - id: PlatformUpdateApplication
    intent: Rename an application
    question: How do I rename an existing application?
  - id: PlatformDeleteApplication
    intent: Delete an application
    question: How do I permanently delete an application from my workspace?
  - id: PlatformUploadApplicationLogo
    intent: Upload an application's logo
    question: How do I set the logo shown on my application's sign-in screens?
  - id: PlatformDeleteApplicationLogo
    intent: Remove an application's logo
    question: How do I remove the logo from an application?
  - id: PlatformUploadApplicationFavicon
    intent: Upload an application's favicon
    question: How do I set the favicon for my application?
  phrasing_ops: 11
  slug: clerk-com-applications-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with the two factor authentication backup codes of the current user.
  name: Clerk Backup Codes API
  phrasing_intents:
  - id: createBackupCodes
    intent: Generate my two-factor backup codes
    question: How does a signed-in user generate two-factor backup codes?
  phrasing_ops: 1
  slug: clerk-com-backup-codes-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Modify instance settings that are currently in beta.
  name: Clerk Beta Features API
  phrasing_intents:
  - id: UpdateInstanceAuthConfig
    intent: Update instance restrictions and test mode
    question: How do I restrict sign-ups on my instance to the allowlist?
  - id: UpdateProductionInstanceDomain
    intent: Change the production domain (beta endpoint)
    question: How do I move my production instance to a new domain using the beta_features domain endpoint?
  - id: ChangeProductionInstanceDomain
    intent: Change the production domain (instance endpoint)
    question: How do I change my production instance's domain with the instance change_domain endpoint?
  phrasing_ops: 3
  slug: clerk-com-beta-features-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Billing-related endpoints for managing statements and payment attempts.
  name: Clerk Billing API
  phrasing_intents:
  - id: GetUserBillingSubscription
    intent: Retrieve a user's billing subscription
    question: What plans is a given user subscribed to and what is their payment status?
  - id: GetUserBillingCreditBalance
    intent: Check a user's credit balance
    question: How much billing credit does a user have left?
  - id: AdjustUserBillingCreditBalance
    intent: Add or remove credit for a user
    question: How do I give a user account credit toward future charges?
  - id: GetOrganizationBillingSubscription
    intent: Retrieve an organization's billing subscription
    question: Which plans is an organization subscribed to, as seen from the backend?
  - id: GetOrganizationBillingCreditBalance
    intent: Check an organization's credit balance
    question: How much billing credit does an organization have available?
  - id: AdjustOrganizationBillingCreditBalance
    intent: Add or remove credit for an organization
    question: How do I grant an organization credit to offset its next bill?
  - id: GetCommercePlanList
    intent: List all billing plans for the instance
    question: What billing plans, free and paid, are configured on my instance?
  - id: GetBillingPriceList
    intent: List billing prices
    question: Which prices, including custom ones, exist for my billing plans?
  phrasing_ops: 16
  slug: clerk-com-billing-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with the checkout flow.
  name: Clerk Checkouts API
  phrasing_intents:
  - id: CreateUserBillingCheckout
    intent: Start a checkout for my own plan
    question: How do I start checking out a paid plan for myself?
  - id: GetUserBillingCheckout
    intent: Get my checkout
    question: What is the status and total of the checkout I started?
  - id: ConfirmUserBillingCheckout
    intent: Confirm and pay for my checkout
    question: How do I complete my own checkout and pay for the plan?
  - id: CreateOrganizationBillingCheckout
    intent: Start a checkout for an organization
    question: How do I start a plan purchase on behalf of my organization?
  - id: GetOrganizationBillingCheckout
    intent: Get an organization's checkout
    question: What is the status of the checkout my organization started?
  - id: ConfirmOrganizationBillingCheckout
    intent: Confirm an organization's checkout
    question: How do I finish paying for my organization's plan checkout?
  phrasing_ops: 6
  slug: clerk-com-checkouts-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The Clear Site Data API from Clerk — 1 operation(s) for clear site data.
  name: Clerk Clear Site Data API
  phrasing_intents:
  - id: clearSiteData
    intent: Clear the site's cookies, storage and cache
    question: How do I wipe cookies and local storage for my site's auth domain?
  phrasing_ops: 1
  slug: clerk-com-clear-site-data-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with the Client Object.
  name: Clerk Client API
  phrasing_intents:
  - id: getClient
    intent: Get the current browser client
    question: Which client and sessions does the current browser have?
  - id: putClient
    intent: Create a new client via PUT
    question: Can I create a fresh client with a PUT request?
  - id: postClient
    intent: Create a new client via POST
    question: How do I create a new client and have it set in the response cookies?
  - id: deleteClientSessions
    intent: Sign out all sessions on this client
    question: How do I sign out of every session in the current browser at once?
  - id: syncClient
    intent: Start syncing a satellite domain's client
    question: How does a satellite domain start syncing the session from the primary domain?
  - id: linkClient
    intent: Finish linking clients across domains
    question: How is the satellite and primary domain sync completed?
  - id: handshakeClient
    intent: Refresh a session token through a handshake
    question: How does my server get a fresh session token when it can't tell if the user is signed in?
  - id: createAgentTask
    intent: Create a session from an agent task ticket
    question: How does an AI agent get signed in without going through the sign-in page?
  phrasing_ops: 8
  slug: clerk-com-client-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The Client object tracks sessions, as well as the state of any sign in and sign up attempts, for a given device.
  name: Clerk Clients API
  phrasing_intents:
  - id: GetClientList
    intent: List all clients (deprecated)
    question: How do I list every client device record in my instance?
  - id: VerifyClient
    intent: Verify a client token
    question: How do I verify the client contained in a token on my backend?
  - id: GetClient
    intent: Get a client's details
    question: How do I look up one client and its sessions by ID?
  phrasing_ops: 3
  slug: clerk-com-clients-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Operations for managing instance configuration. The config API provides a unified interface for reading and updating instance settings, including authentication methods, SSO connections, and other ins
  name: Clerk Config API
  phrasing_intents:
  - id: PlatformGetConfig
    intent: Get an instance's configuration
    question: How do I read the current settings of my production instance?
  - id: PlatformPatchConfig
    intent: Partially update an instance's configuration
    question: How do I change just a few settings on an instance without resending everything?
  - id: PlatformPutConfig
    intent: Replace an instance's full configuration
    question: How do I overwrite an instance's entire configuration in one request?
  - id: PlatformGetConfigSchema
    intent: Get the instance config JSON Schema
    question: Where can I get the JSON Schema that describes instance configuration?
  phrasing_ops: 4
  slug: clerk-com-config-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The Dev Browser API from Clerk — 2 operation(s) for dev browser.
  name: Clerk Dev Browser API
  phrasing_intents:
  - id: postDevBrowserInitSetCookie
    intent: Set the dev browser first-party cookie
    question: How does a development instance set its first-party dev browser cookie?
  - id: getDevBrowserInit
    intent: Initialize a dev browser for a development instance
    question: How do I initialize a dev browser for a staging or development instance?
  - id: createDevBrowser
    intent: Create a Dev Browser token
    question: How do I authenticate requests against a development instance?
  phrasing_ops: 3
  slug: clerk-com-dev-browser-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Domains represent each instance's URLs and DNS setup.
  name: Clerk Domains API
  phrasing_intents:
  - id: ListDomains
    intent: List my instance's primary and satellite domains
    question: Which domains is my Clerk instance currently running on, including satellites?
  - id: AddDomain
    intent: Add a satellite domain to an instance
    question: How do I add a satellite domain to a multi-domain instance?
  - id: DeleteDomain
    intent: Delete a satellite domain from the instance
    question: How do I remove a satellite domain I no longer use from my instance?
  - id: UpdateDomain
    intent: Update an instance domain or its proxy URL
    question: How do I set a proxy URL on my production instance's domain?
  - id: CreateOrganizationDomain
    intent: Add a domain to an organization
    question: How do I add a company email domain to an organization as the signed-in user?
  - id: ListOrganizationDomains
    intent: List an organization's domains
    question: Which email domains are attached to this organization?
  - id: GetOrganizationDomain
    intent: Get one organization domain's details
    question: What are the verification and enrollment details of one organization domain?
  - id: deleteOrganizationDomain
    intent: Remove a domain from an organization
    question: How do I remove an email domain from my organization?
  phrasing_ops: 20
  slug: clerk-com-domains-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: A user can be associated with one or more email addresses, which allows them to be contacted via email.
  name: Clerk Email Addresses API
  phrasing_intents:
  - id: CreateEmailAddress
    intent: Add an email address to a user (backend)
    question: How do I attach an extra email address to a user from my backend?
  - id: GetEmailAddress
    intent: Retrieve an email address by ID (backend)
    question: What are the details and verification state of an email address ID from the backend?
  - id: DeleteEmailAddress
    intent: Delete any user's email address (backend)
    question: How does my backend remove an email address from a user's account?
  - id: UpdateEmailAddress
    intent: Mark an email address verified or primary
    question: How do I mark a user's email address as verified from the backend?
  - id: getEmailAddresses
    intent: List the signed-in user's email addresses
    question: Which email addresses are on my own account?
  - id: createEmailAddresses
    intent: Add an email address to my own account
    question: How do I add another email address to my own account?
  - id: verifyEmailAddress
    intent: Submit the code to verify my email address
    question: I got a verification code by email, how do I confirm my new address?
  - id: sendVerificationEmail
    intent: Send a verification code or link to my email
    question: How do I get a verification code sent to an email address I just added?
  phrasing_ops: 10
  slug: clerk-com-email-addresses-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Email & SMS templates allow you to customize the theming and wording of emails & SMS messages that are sent by your instance.
  name: Clerk Email & SMS Templates API
  phrasing_intents:
  - id: GetTemplateList
    intent: List email or SMS templates
    question: Which email templates can I customize for my instance?
  - id: GetTemplate
    intent: Retrieve one email or SMS template
    question: What does the current verification code email template say?
  - id: UpsertTemplate
    intent: Edit an email or SMS template
    question: How do I customize the subject and body of an email template?
  - id: RevertTemplate
    intent: Revert a template to its default
    question: How do I undo my customizations and restore a template's default?
  - id: PreviewTemplate
    intent: Preview changes to a template
    question: Can I see how a template will render before saving my edits?
  - id: ToggleTemplateDelivery
    intent: Turn Clerk delivery on or off for a template
    question: How do I send a template's emails myself instead of having Clerk deliver them?
  phrasing_ops: 6
  slug: clerk-com-email-sms-templates-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: An Enterprise Connection holds configuration data required for facilitating an enterprise SSO flow between your Clerk instance and an identity provider.
  name: Clerk Enterprise Connections API
  phrasing_intents:
  - id: ListEnterpriseConnections
    intent: List enterprise SSO connections
    question: Which enterprise SSO connections are set up on my instance?
  - id: CreateEnterpriseConnection
    intent: Create an enterprise SSO connection
    question: How do I set up SAML or OIDC single sign-on for a customer's email domains?
  - id: GetEnterpriseConnection
    intent: Retrieve an enterprise connection
    question: What SAML or OIDC settings does a specific enterprise connection have?
  - id: UpdateEnterpriseConnection
    intent: Update or activate an enterprise connection
    question: How do I turn on an enterprise connection once its SSO is configured?
  - id: DeleteEnterpriseConnection
    intent: Delete an enterprise connection
    question: How do I remove an enterprise SSO connection I no longer need?
  phrasing_ops: 5
  slug: clerk-com-enterprise-connections-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to get and update the current Environment
  name: Clerk Environment API
  phrasing_intents:
  - id: getEnvironment
    intent: Get the instance environment settings
    question: Which sign-in features and settings are enabled for this instance's frontend?
  - id: updateEnvironment
    intent: Update the environment from the request origin
    question: How do I refresh the environment record using the calling origin?
  phrasing_ops: 2
  slug: clerk-com-environment-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with the external accounts of the current user.
  name: Clerk External Accounts API
  phrasing_intents:
  - id: postOAuthAccounts
    intent: Connect a social login account to my profile
    question: How do I link a social login account to my existing profile?
  - id: reauthorizeExternalAccount
    intent: Reauthorize a connected external account
    question: How do I re-consent a connected account to grant new scopes?
  - id: deleteExternalAccount
    intent: Unlink an external account from my profile
    question: How do I disconnect a social login from my account?
  - id: revokeExternalAccountTokens
    intent: Revoke OAuth tokens of a linked account
    question: How do I revoke the access and refresh tokens stored for a linked account but keep the link?
  phrasing_ops: 4
  slug: clerk-com-external-accounts-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to get the health status of the API.
  name: Clerk Health API
  phrasing_intents:
  - id: getHealth
    intent: Check Frontend API health
    question: Is the Frontend API up and healthy right now?
  phrasing_ops: 1
  slug: clerk-com-health-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Modify the settings of your instance.
  name: Clerk Instance Settings API
  phrasing_intents:
  - id: GetInstance
    intent: Fetch the current instance
    question: What are the current settings of my Clerk instance?
  - id: UpdateInstance
    intent: Update general instance settings
    question: How do I change the support email shown for my instance?
  - id: UpdateInstanceRestrictions
    intent: Update sign-up allowlist and blocklist restrictions
    question: How do I restrict sign-ups to an allowlist of identifiers?
  - id: GetInstanceProtect
    intent: Get the instance's protect settings
    question: Are protect rules currently enabled on my instance?
  - id: UpdateInstanceProtect
    intent: Update the instance's protect settings
    question: How do I turn protect rules on for my instance?
  - id: GetInstanceCommunication
    intent: Get SMS communication settings
    question: Which countries are blocked from receiving SMS for my instance?
  - id: UpdateInstanceCommunication
    intent: Replace the SMS country blocklist
    question: How do I stop sending SMS codes to certain countries?
  - id: GetInstanceOAuthApplicationSettings
    intent: Get OAuth application settings
    question: Is dynamic OAuth client registration turned on for my instance?
  phrasing_ops: 11
  slug: clerk-com-instance-settings-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Invitations allow you to invite someone to sign up to your application, via email.
  name: Clerk Invitations API
  phrasing_intents:
  - id: CreateInvitation
    intent: Invite someone to sign up
    question: How do I invite a new user to sign up to my application by email?
  - id: ListInvitations
    intent: List application invitations
    question: How do I see every invitation I've sent to join my application?
  - id: CreateBulkInvitations
    intent: Invite many people to sign up at once
    question: How do I send sign-up invitations to a whole list of email addresses at once?
  - id: RevokeInvitation
    intent: Revoke an application invitation
    question: How do I cancel an application invitation I sent by mistake?
  - id: createOrganizationInvitations
    intent: Invite someone to an organization
    question: How does an organization admin invite a colleague to join their organization?
  - id: getOrganizationInvitations
    intent: List an organization's invitations
    question: How do I see all invitations sent to join a particular organization?
  - id: bulkCreateOrganizationInvitations
    intent: Invite many people to an organization
    question: How do I invite a whole team to an organization in one request?
  - id: getAllPendingOrganizationInvitations
    intent: List pending organization invitations (legacy)
    question: Which invitations to an organization have not been accepted yet, using the older pending endpoint?
  phrasing_ops: 9
  slug: clerk-com-invitations-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Retrieve the JSON Web Key Set which can be used to verify the token signatures of the instance.
  name: Clerk JWKS API
  phrasing_intents:
  - id: GetJWKS
    intent: Get the instance's JSON Web Key Set
    question: Where do I get the public keys to verify session tokens?
  phrasing_ops: 1
  slug: clerk-com-jwks-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: JWT Templates allow you to generate custom authentication tokens tied to authenticated sessions, enabling you to integrate with third-party services.
  name: Clerk JWT Templates API
  phrasing_intents:
  - id: ListJWTTemplates
    intent: List JWT templates
    question: What JWT templates are set up in my instance?
  - id: CreateJWTTemplate
    intent: Create a JWT template
    question: How do I create a JWT template with custom claims for a third-party service?
  - id: GetJWTTemplate
    intent: Retrieve a JWT template
    question: How do I view the claims configured on one JWT template?
  - id: UpdateJWTTemplate
    intent: Update a JWT template
    question: How do I change the claims on an existing JWT template?
  - id: DeleteJWTTemplate
    intent: Delete a JWT template
    question: How do I delete a JWT template I no longer use?
  - id: PlatformListJWTTemplates
    intent: List an application instance's JWT templates
    question: How do I list JWT templates for one of my applications using the Platform API?
  - id: PlatformCreateJWTTemplate
    intent: Create a JWT template in an application instance
    question: How do I add a JWT template to another application's instance through the Platform API?
  - id: PlatformGetJWTTemplate
    intent: Get a JWT template in an application instance
    question: How do I read one JWT template from a specific application instance via the Platform API?
  phrasing_ops: 10
  slug: clerk-com-jwt-templates-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Machine to Machine Tokens are used to manage authentication between Machines.
  name: Clerk M2M Tokens API
  phrasing_intents:
  - id: createM2MToken
    intent: Create a machine-to-machine token
    question: How does a machine get a token to call another machine's API?
  - id: getM2MTokens
    intent: List M2M tokens for a machine
    question: Which machine-to-machine tokens have been issued for a machine?
  - id: revokeM2MToken
    intent: Revoke an M2M token
    question: How do I revoke a machine token that leaked?
  - id: verifyM2MToken
    intent: Verify an M2M token
    question: How do I check that an incoming machine token is valid?
  phrasing_ops: 4
  slug: clerk-com-m2m-tokens-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: A Machine represents a machine/server/service which can be used in machine-to-machine authentication.
  name: Clerk Machines API
  phrasing_intents:
  - id: ListMachines
    intent: List machines in an instance
    question: Which machines have been set up for machine-to-machine auth in my instance?
  - id: CreateMachine
    intent: Create a machine identity
    question: How do I register a new service as a machine for M2M tokens?
  - id: GetMachine
    intent: Retrieve a machine
    question: How do I see the details of one machine?
  - id: UpdateMachine
    intent: Rename or reconfigure a machine
    question: How do I rename an existing machine?
  - id: DeleteMachine
    intent: Delete a machine
    question: How do I remove a machine that is no longer used?
  - id: GetMachineSecretKey
    intent: Get a machine's secret key
    question: Where do I find the secret key for a machine so my service can authenticate?
  - id: RotateMachineSecretKey
    intent: Rotate a machine's secret key
    question: How do I rotate a machine secret without breaking services immediately?
  - id: CreateMachineScope
    intent: Allow one machine to access another
    question: How do I let one machine call another machine?
  phrasing_ops: 9
  slug: clerk-com-machines-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with the members of an organization. The current user must be an administrator to access them.
  name: Clerk Members API
  phrasing_intents:
  - id: CreateOrganizationMembership
    intent: Add a user to an organization
    question: How do I add an existing user straight into my organization without an invite?
  - id: ListOrganizationMemberships
    intent: List an organization's members
    question: Who are the members of my organization?
  - id: UpdateOrganizationMembership
    intent: Change a member's organization role
    question: How do I promote an organization member to admin?
  - id: removeOrganizationMember
    intent: Remove a member from an organization
    question: How do I kick a user out of my organization?
  phrasing_ops: 4
  slug: clerk-com-members-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with the members of an organization. The current user must be an administrator to access them.
  name: Clerk Membership Requests API
  phrasing_intents:
  - id: listOrganizationMembershipRequests
    intent: List requests to join an organization
    question: Who has asked to join my organization?
  - id: acceptOrganizationMembershipRequest
    intent: Approve a request to join an organization
    question: How do I approve someone who asked to join my organization?
  - id: rejectOrganizationMembershipRequest
    intent: Reject a request to join an organization
    question: How do I turn down a request to join my organization?
  phrasing_ops: 3
  slug: clerk-com-membership-requests-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Various endpoints that do not belong in any particular category.
  name: Clerk Miscellaneous API
  phrasing_intents:
  - id: GetPublicInterstitial
    intent: Get the interstitial page markup
    question: What is the interstitial page SDKs load when auth state is unknown?
  phrasing_ops: 1
  slug: clerk-com-miscellaneous-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Endpoints for managing OAuth Access Tokens, which are credentials to access protected resources on behalf of a user.
  name: Clerk OAuth Access Tokens API
  phrasing_intents:
  - id: verifyOAuthAccessToken
    intent: Verify an OAuth access token
    question: How do I check that an access token issued to one of my OAuth applications is valid?
  phrasing_ops: 1
  slug: clerk-com-oauth-access-tokens-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: OAuth applications contain data for clients using Clerk as an OAuth2 identity provider.
  name: Clerk OAuth Applications API
  phrasing_intents:
  - id: ListOAuthApplications
    intent: List OAuth applications
    question: What OAuth applications are registered in my instance?
  - id: CreateOAuthApplication
    intent: Register an OAuth application
    question: How do I register an OAuth client so another app can sign in with my users?
  - id: GetOAuthApplication
    intent: Retrieve an OAuth application
    question: How do I look up the settings of one OAuth application by its ID?
  - id: UpdateOAuthApplication
    intent: Update an OAuth application
    question: How do I add a redirect URI to an existing OAuth application?
  - id: DeleteOAuthApplication
    intent: Delete an OAuth application
    question: How do I permanently delete an OAuth application?
  - id: UploadOAuthApplicationLogo
    intent: Upload an OAuth application's logo
    question: How do I add a logo that shows on an OAuth application's consent screen?
  - id: RotateOAuthApplicationSecret
    intent: Rotate an OAuth application's client secret
    question: How do I rotate the client secret of an OAuth application after a leak?
  phrasing_ops: 7
  slug: clerk-com-oauth-applications-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to receive callbacks from successful OAuth attempts.
  name: Clerk OAuth2 Callbacks API
  phrasing_intents:
  - id: getOauthCallback
    intent: Handle an OAuth provider redirect
    question: Which URL do OAuth providers redirect back to after a successful sign-in?
  - id: postOauthCallback
    intent: Handle an OAuth provider POST callback
    question: How are OAuth providers that POST back instead of redirecting handled?
  phrasing_ops: 2
  slug: clerk-com-oauth2-callbacks-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Requests for the OAuth2 authorization flow.
  name: Clerk OAuth2 Identity Provider API
  phrasing_intents:
  - id: requestOAuthAuthorize
    intent: Start an OAuth2 authorization via GET redirect
    question: How do I send a user to the authorization endpoint to get an OAuth code using a GET link?
  - id: requestOAuthAuthorizePOST
    intent: Start an OAuth2 authorization via form POST
    question: Can I post the authorization request as a form body instead of query parameters?
  - id: registerOAuthClient
    intent: Dynamically register an OAuth client
    question: How can an app register itself as an OAuth client without manual setup?
  - id: getOAuthToken
    intent: Exchange a code or refresh token for tokens
    question: How do I trade an authorization code for access and ID tokens?
  - id: getOAuthUserInfo
    intent: Get user info with an access token via GET
    question: How do I fetch the signed-in user's profile claims with an OAuth access token using GET?
  - id: getOAuthUserInfoPOST
    intent: Get user info with an access token via POST
    question: Can I request OIDC userinfo with a POST instead of a GET?
  - id: getOAuthTokenInfo
    intent: Introspect an access or refresh token
    question: How do I check whether an OAuth token is still active and what scopes it has?
  - id: revokeOAuthToken
    intent: Revoke an OAuth2 token
    question: How do I invalidate an OAuth access or refresh token that was issued to my app?
  phrasing_ops: 10
  slug: clerk-com-oauth2-identity-provider-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with an organization and its properties. The current user must be an administrator to access them.
  name: Clerk Organization API
  phrasing_intents:
  - id: createOrganization
    intent: Create an organization as the signed-in user
    question: How can a signed-in user create their own organization from the frontend?
  - id: getOrganization
    intent: Get an organization I belong to
    question: How does the frontend load the details of an organization the user is a member of?
  - id: updateOrganization
    intent: Rename an organization I administer
    question: How does an organization admin rename their organization from the frontend?
  - id: deleteOrganization
    intent: Delete an organization I administer
    question: How can an organization admin delete their organization from the app?
  - id: updateOrganizationLogo
    intent: Change my organization's logo
    question: How does an admin upload a new logo for their organization from the app?
  - id: deleteOrganizationLogo
    intent: Remove my organization's logo
    question: How does an admin remove their organization's logo in the app?
  phrasing_ops: 6
  slug: clerk-com-organization-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to get suggested defaults when creating a new organization.
  name: Clerk Organization Creation Defaults API
  phrasing_intents:
  - id: getOrganizationCreationDefaults
    intent: Get suggested defaults for a new organization
    question: What organization name would be suggested for me when I create one?
  phrasing_ops: 1
  slug: clerk-com-organization-creation-defaults-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Manage organization domains.
  name: Clerk Organization Domains API
  phrasing_intents:
  - id: CreateOrganizationDomain
    intent: Add a domain to an organization
    question: How do I attach a company email domain to an organization so staff can join?
  - id: ListOrganizationDomains
    intent: List one organization's domains
    question: Which email domains are attached to a particular organization?
  - id: UpdateOrganizationDomain
    intent: Change an organization domain's settings
    question: How do I switch an organization domain to automatic invitations?
  - id: DeleteOrganizationDomain
    intent: Remove a domain from an organization
    question: How do I detach an email domain from an organization?
  - id: ListAllOrganizationDomains
    intent: List domains across all organizations
    question: How do I see every organization domain across my whole instance?
  phrasing_ops: 5
  slug: clerk-com-organization-domains-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Invite users to an organization.
  name: Clerk Organization Invitations API
  phrasing_intents:
  - id: ListInstanceOrganizationInvitations
    intent: List organization invitations across the instance
    question: Which organization invitations exist across all organizations in my instance?
  - id: CreateOrganizationInvitation
    intent: Invite someone to an organization
    question: How do I invite a new member to an organization by email?
  - id: ListOrganizationInvitations
    intent: List one organization's invitations
    question: Who has been invited to this organization, and have they accepted?
  - id: CreateOrganizationInvitationBulk
    intent: Invite several people to an organization at once
    question: How do I send organization invitations to several emails in one request?
  - id: ListPendingOrganizationInvitations
    intent: List an organization's pending invitations
    question: Which invitations to this organization haven't been accepted yet?
  - id: GetOrganizationInvitation
    intent: Retrieve an organization invitation
    question: What role and status does a specific organization invitation have?
  - id: RevokeOrganizationInvitation
    intent: Revoke a pending organization invitation
    question: How do I cancel an organization invitation that hasn't been accepted?
  phrasing_ops: 7
  slug: clerk-com-organization-invitations-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Manage member roles in an organization.
  name: Clerk Organization Memberships API
  phrasing_intents:
  - id: CreateOrganizationMembership
    intent: Add a user to an organization
    question: How do I add an existing user to an organization with a role?
  - id: ListOrganizationMemberships
    intent: List members of an organization
    question: Who are the members of a given organization?
  - id: UpdateOrganizationMembership
    intent: Change a member's organization role
    question: How do I promote an organization member to admin?
  - id: DeleteOrganizationMembership
    intent: Remove a member from an organization
    question: How do I kick a user out of an organization?
  - id: UpdateOrganizationMembershipMetadata
    intent: Merge metadata on an organization membership
    question: How do I store custom data on a user's membership in an organization?
  - id: InstanceGetOrganizationMemberships
    intent: List all organization memberships in the instance
    question: How do I see every organization membership across my whole instance?
  phrasing_ops: 6
  slug: clerk-com-organization-memberships-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Manage organization permissions that define what members can do within an organization.
  name: Clerk Organization Permissions API
  phrasing_intents:
  - id: ListOrganizationPermissions
    intent: List organization permissions
    question: Which custom organization permissions are defined in my instance?
  - id: CreateOrganizationPermission
    intent: Create an organization permission
    question: How do I define a new permission like org:invoices:read for organization roles?
  - id: GetOrganizationPermission
    intent: Retrieve an organization permission
    question: How do I see the details of one organization permission?
  - id: UpdateOrganizationPermission
    intent: Update an organization permission
    question: How do I rename an organization permission or change its key?
  - id: DeleteOrganizationPermission
    intent: Delete an organization permission
    question: How do I delete a custom organization permission I no longer need?
  phrasing_ops: 5
  slug: clerk-com-organization-permissions-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Manage custom roles in an organization.
  name: Clerk Organization Roles API
  phrasing_intents:
  - id: ListOrganizationRoles
    intent: List organization roles
    question: What custom organization roles exist in my instance?
  - id: CreateOrganizationRole
    intent: Create an organization role
    question: How do I define a custom role like billing manager for organizations?
  - id: GetOrganizationRole
    intent: Retrieve an organization role
    question: How do I see the permissions attached to one organization role?
  - id: UpdateOrganizationRole
    intent: Update an organization role
    question: How do I rename an organization role or change its description?
  - id: DeleteOrganizationRole
    intent: Delete an organization role
    question: How do I delete a custom organization role?
  - id: AssignPermissionToOrganizationRole
    intent: Add a permission to an organization role
    question: How do I grant one extra permission to an existing organization role?
  - id: RemovePermissionFromOrganizationRole
    intent: Remove a permission from an organization role
    question: How do I take a single permission away from an organization role?
  phrasing_ops: 7
  slug: clerk-com-organization-roles-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Organizations are used to group members under a common entity and provide shared access to resources.
  name: Clerk Organizations API
  phrasing_intents:
  - id: ListOrganizations
    intent: List organizations in the instance
    question: How do I list every organization in my instance, newest first?
  - id: CreateOrganization
    intent: Create an organization
    question: How do I create an organization for a customer from my backend?
  - id: GetOrganization
    intent: Retrieve an organization by ID or slug
    question: How do I fetch one organization by its ID or slug?
  - id: UpdateOrganization
    intent: Update an organization
    question: How do I rename an organization or change its slug from the backend?
  - id: DeleteOrganization
    intent: Delete an organization
    question: How do I permanently delete an organization and its memberships?
  - id: MergeOrganizationMetadata
    intent: Merge metadata into an organization
    question: How do I add a key to an organization's metadata without replacing the rest?
  - id: UploadOrganizationLogo
    intent: Upload an organization's logo
    question: How do I upload a logo image for an organization from the backend?
  - id: DeleteOrganizationLogo
    intent: Delete an organization's logo
    question: How do I remove an organization's logo from the backend?
  phrasing_ops: 11
  slug: clerk-com-organizations-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with the current user's organization memberships, invitations and suggestions.
  name: Clerk Organizations Memberships API
  phrasing_intents:
  - id: getOrganizationMemberships
    intent: List my organization memberships
    question: Which organizations do I belong to?
  - id: deleteOrganizationMemberships
    intent: Leave an organization
    question: How do I leave an organization I'm a member of?
  - id: getUsersOrganizationInvitations
    intent: List invitations I've received
    question: Which organizations have invited me to join?
  - id: acceptOrganizationInvitation
    intent: Accept an organization invitation I received
    question: How do I accept an invitation to join an organization?
  - id: getOrganizationSuggestions
    intent: List organizations suggested for me
    question: Which organizations are suggested to me based on my email domain?
  - id: acceptOrganizationSuggestion
    intent: Accept an organization suggestion
    question: How do I act on a suggestion to join my company's organization?
  phrasing_ops: 6
  slug: clerk-com-organizations-memberships-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with the passkeys of the logged in user.
  name: Clerk Passkeys API
  phrasing_intents:
  - id: postPasskey
    intent: Register a new passkey for my account
    question: How do I add a passkey to my account?
  - id: readPasskey
    intent: Get one of my passkeys
    question: What details are stored about one of my passkeys?
  - id: patchPasskey
    intent: Rename a passkey
    question: How do I give one of my passkeys a friendlier name?
  - id: deletePasskey
    intent: Delete a passkey
    question: How do I remove a passkey from a lost device?
  - id: attemptPasskeyVerification
    intent: Verify a newly created passkey
    question: How do I finish setting up a passkey with the browser's credential response?
  phrasing_ops: 5
  slug: clerk-com-passkeys-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with payment attempts for users and organizations.
  name: Clerk Payment Attempts API
  phrasing_intents:
  - id: GetUserPaymentAttempts
    intent: List my payment attempts
    question: Which charges have been attempted on my account?
  - id: GetUserPaymentAttempt
    intent: Get one of my payment attempts
    question: Why did a particular payment on my account fail?
  phrasing_ops: 2
  slug: clerk-com-payment-attempts-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with payment methods belonging to users and organizations.
  name: Clerk Payment Methods API
  phrasing_intents:
  - id: GetUserPaymentMethods
    intent: List my saved payment methods
    question: Which cards do I have saved for billing on my account?
  - id: CreateUserPaymentMethod
    intent: Save a payment method to my account
    question: How do I add a card to my personal billing account?
  - id: InitializeUserPaymentMethod
    intent: Start setting up a personal payment method
    question: How do I begin the card setup flow for my own account?
  - id: DeleteUserPaymentMethod
    intent: Delete one of my payment methods
    question: How do I remove a saved card from my own account?
  - id: SetUserDefaultPaymentMethod
    intent: Set my default payment method
    question: How do I choose which of my cards is charged by default?
  - id: GetOrganizationPaymentMethods
    intent: List an organization's payment methods
    question: Which payment methods does our organization have on file?
  - id: CreateOrganizationPaymentMethod
    intent: Save a payment method for an organization
    question: How do I add a card to my organization's billing?
  - id: InitializeOrganizationPaymentMethod
    intent: Start setting up an organization payment method
    question: How do I start the card setup flow for an organization?
  phrasing_ops: 10
  slug: clerk-com-payment-methods-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: A user can be associated with one or more phone numbers, which allows them to be contacted via SMS.
  name: Clerk Phone Numbers API
  phrasing_intents:
  - id: CreatePhoneNumber
    intent: Add a phone number to a user from the backend
    question: How do I attach a phone number to a user from my server?
  - id: GetPhoneNumber
    intent: Retrieve a phone number from the backend
    question: How do I look up a phone number record by ID on the server?
  - id: DeletePhoneNumber
    intent: Delete a user's phone number from the backend
    question: How do I remove a phone number from any user using my secret key?
  - id: UpdatePhoneNumber
    intent: Update a phone number from the backend
    question: How do I mark a user's phone number as verified or primary from my server?
  - id: getPhoneNumbers
    intent: List the signed-in user's phone numbers
    question: What phone numbers are on my own account?
  - id: postPhoneNumbers
    intent: Add a phone number to my account
    question: How do I add a new phone number to my own profile?
  - id: verifyPhoneNumber
    intent: Verify my phone number with the SMS code
    question: How do I confirm my phone number with the code I got by text?
  - id: sendVerificationSMS
    intent: Text a verification code to my phone
    question: How do I get an SMS verification code sent to a phone number I just added?
  phrasing_ops: 11
  slug: clerk-com-phone-numbers-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with plans that users and organizations can purchase.
  name: Clerk Plans API
  phrasing_intents:
  - id: GetBillingPlanList
    intent: List public billing plans
    question: Which plans can users subscribe to on my pricing page?
  - id: GetBillingPlan
    intent: Get a public billing plan by ID or slug
    question: How do I load one plan's details for a pricing page using its slug?
  phrasing_ops: 2
  slug: clerk-com-plans-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Check if a user is using a proxy.
  name: Clerk Proxy Checks API
  phrasing_intents:
  - id: VerifyDomainProxy
    intent: Check that a domain's proxy is working
    question: How do I confirm my proxy URL can reach the Frontend API before enabling it?
  phrasing_ops: 1
  slug: clerk-com-proxy-checks-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The Proxy Health API from Clerk — 1 operation(s) for proxy health.
  name: Clerk Proxy Health API
  phrasing_intents:
  - id: getProxyHealth
    intent: Check a domain's proxy configuration
    question: How do I test whether my Frontend API proxy is set up correctly for a domain?
  phrasing_ops: 1
  slug: clerk-com-proxy-health-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The Redirect API from Clerk — 1 operation(s) for redirect.
  name: Clerk Redirect API
  phrasing_intents:
  - id: redirectToUrl
    intent: Redirect to a validated URL
    question: How do I safely redirect a user after an auth flow?
  phrasing_ops: 1
  slug: clerk-com-redirect-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Redirect URLs are whitelisted URLs that facilitate secure authentication flows in native applications (e.g. React Native, Expo). In these contexts, Clerk ensures that security-critical nonces are pass
  name: Clerk Redirect URLs API
  phrasing_intents:
  - id: ListRedirectURLs
    intent: List allowed redirect URLs for the instance
    question: Which redirect URLs are whitelisted for my instance?
  - id: CreateRedirectURL
    intent: Allow a new redirect URL on the instance
    question: How do I add a redirect URL to my instance's whitelist, e.g. for a mobile app?
  - id: GetRedirectURL
    intent: Retrieve an instance redirect URL
    question: How do I look up a whitelisted redirect URL by its ID with the backend API?
  - id: DeleteRedirectURL
    intent: Remove a redirect URL from the instance
    question: How do I remove a redirect URL from my instance's whitelist?
  - id: PlatformListRedirectURLs
    intent: List redirect URLs for an application instance
    question: How do I list redirect URLs for one of my applications' production environment via the Platform API?
  - id: PlatformCreateRedirectURL
    intent: Add a redirect URL to an application instance
    question: How do I add a redirect URL to a specific application's development instance via the Platform API?
  - id: PlatformGetRedirectURL
    intent: Get a redirect URL on an application instance
    question: How do I read one redirect URL from an application's instance through the Platform API?
  - id: PlatformDeleteRedirectURL
    intent: Delete a redirect URL from an application instance
    question: How do I delete a redirect URL from one application's production instance with the Platform API?
  phrasing_ops: 8
  slug: clerk-com-redirect-urls-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Role sets define collections of roles that can be assigned to organization members. Each organization uses one role set to determine the available roles for its members. Role sets support default role
  name: Clerk Role Sets API
  phrasing_intents:
  - id: ListRoleSets
    intent: List role sets
    question: Which role sets exist in my instance?
  - id: CreateRoleSet
    intent: Create a role set
    question: How do I group organization roles into a new role set?
  - id: GetRoleSet
    intent: Retrieve a role set
    question: How do I see which roles are in a role set?
  - id: UpdateRoleSet
    intent: Update a role set's settings
    question: How do I rename a role set or change its description?
  - id: ReplaceRoleSet
    intent: Replace a role set and migrate organizations
    question: How do I retire a role set and move its organizations to another one?
  - id: AddRolesToRoleSet
    intent: Add roles to a role set
    question: How do I add more roles to an existing role set?
  - id: ReplaceRoleInRoleSet
    intent: Swap one role for another in a role set
    question: How do I remove a role from a role set and move its members to a different role?
  phrasing_ops: 7
  slug: clerk-com-role-sets-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The Roles API from Clerk — 1 operation(s) for roles.
  name: Clerk Roles API
  phrasing_intents:
  - id: ListOrganizationRoles
    intent: List the roles available in an organization
    question: Which roles can members be assigned in my organization?
  phrasing_ops: 1
  slug: clerk-com-roles-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used in authentication flows using SAML.
  name: Clerk SAML API
  phrasing_intents:
  - id: samlMetadata
    intent: Get service provider SAML metadata
    question: Where do I get the SAML service provider metadata XML to give my IdP?
  - id: acs
    intent: Receive a SAML response from the IdP
    question: Which endpoint processes the SAML responses my identity provider posts back?
  phrasing_ops: 2
  slug: clerk-com-saml-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: A SAML Connection holds configuration data required for facilitating a SAML SSO flow between your Clerk Instance (SP) and a particular SAML IdP.
  name: Clerk SAML Connections API
  phrasing_intents:
  - id: ListSAMLConnections
    intent: List SAML connections
    question: What SAML SSO connections are configured in my instance?
  - id: CreateSAMLConnection
    intent: Create a SAML SSO connection
    question: How do I set up SAML single sign-on for a customer's identity provider?
  - id: GetSAMLConnection
    intent: Retrieve a SAML connection
    question: How do I view the IdP settings of one SAML connection?
  - id: UpdateSAMLConnection
    intent: Update a SAML connection
    question: How do I rotate the IdP certificate on an existing SAML connection?
  - id: DeleteSAMLConnection
    intent: Delete a SAML connection
    question: How do I remove a SAML SSO connection for a customer who left?
  phrasing_ops: 5
  slug: clerk-com-saml-connections-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The Session object is an abstraction over an HTTP session. It models the period of information exchange between a user and the server. Sessions are created when a user successfully goes through the si
  name: Clerk Sessions API
  phrasing_intents:
  - id: GetSessionList
    intent: List sessions for a user or client
    question: Which sessions does a given user currently have in Clerk?
  - id: createSession
    intent: Create a test session for a user
    question: How do I create an active session for a user in a test instance?
  - id: GetSession
    intent: Retrieve a session by ID from the backend
    question: How do I look up the details of a session from my backend using its ID?
  - id: RefreshSession
    intent: Refresh a session with an expired token
    question: How do I get a new session token when the old one has expired, using the refresh token?
  - id: RevokeSession
    intent: Revoke a user's session
    question: How do I force a user to sign in again by revoking their session from the backend?
  - id: CreateSessionToken
    intent: Mint a session JWT from the backend
    question: How do I generate a session JWT for a session from my server?
  - id: CreateSessionTokenFromTemplate
    intent: Mint a backend session JWT from a template
    question: How do I create a JWT for a session using one of my instance's JWT templates on the server?
  - id: removeClientSessionsAndRetainCookie
    intent: Remove all sessions from the current client
    question: How do I clear every session on the current browser client but keep the __client cookie?
  phrasing_ops: 19
  slug: clerk-com-sessions-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: 'Sign-in tokens are JWTs that can be used to sign in to an application without specifying any credentials. A sign-in token can be used at most once and they can be consumed from the Frontend API using '
  name: Clerk Sign-in Tokens API
  phrasing_intents:
  - id: CreateSignInToken
    intent: Create a sign-in token for a user
    question: How do I generate a magic sign-in link for a user from my backend?
  - id: RevokeSignInToken
    intent: Revoke a sign-in token
    question: How do I invalidate a sign-in token before it's used?
  phrasing_ops: 2
  slug: clerk-com-sign-in-tokens-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to sign in a user in the current client.
  name: Clerk Sign Ins API
  phrasing_intents:
  - id: createSignIn
    intent: Start a sign-in on the current client
    question: How do I start signing a user in with their email or username?
  - id: getSignIn
    intent: Retrieve a sign-in attempt
    question: What status is my in-progress sign-in attempt in?
  - id: resetPassword
    intent: Reset the password during sign-in
    question: How does a user set a new password while signing in after a reset code?
  - id: prepareSignInFactorOne
    intent: Send the first-factor code or link for a sign-in
    question: How do I send a one-time code to the user's email or phone during sign-in?
  - id: attemptSignInFactorOne
    intent: Submit the first-factor code or password
    question: How do I complete the first sign-in step with the code the user received?
  - id: prepareSignInFactorTwo
    intent: Send the second-factor code for a sign-in
    question: How do I send an MFA code by SMS once a sign-in needs a second factor?
  - id: attemptSignInFactorTwo
    intent: Submit the second-factor code
    question: How do I finish two-factor sign-in with the user's TOTP or SMS code?
  - id: acceptTicket
    intent: Accept a ticket link such as an invitation
    question: What happens when a user clicks a ticket link from an invitation email?
  phrasing_ops: 9
  slug: clerk-com-sign-ins-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with billing statements for users and organizations.
  name: Clerk Statements API
  phrasing_intents:
  - id: GetUserStatements
    intent: List my billing statements
    question: Where can I see my own past billing statements?
  - id: GetUserStatement
    intent: Get one of my billing statements
    question: How do I open a specific statement from my own billing history?
  - id: GetOrganizationStatements
    intent: List an organization's billing statements
    question: Where can I see my organization's billing statements as a member?
  - id: GetOrganizationStatement
    intent: Get one organization billing statement
    question: How do I view a single statement for my organization?
  phrasing_ops: 4
  slug: clerk-com-statements-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with subscription items belonging to users and organizations.
  name: Clerk Subscription Items API
  phrasing_intents:
  - id: GetUserBillingSubscriptionItems
    intent: List my subscription items
    question: Which plans am I currently subscribed to?
  - id: DeleteUserBillingSubscriptionItem
    intent: Cancel one of my subscription items
    question: How do I cancel my personal subscription to a plan?
  - id: GetOrganizationBillingSubscriptionItems
    intent: List an organization's subscription items
    question: Which plans is our organization subscribed to?
  - id: DeleteOrganizationBillingSubscriptionItem
    intent: Cancel an organization's subscription item
    question: How do I cancel a plan my organization is subscribed to?
  phrasing_ops: 4
  slug: clerk-com-subscription-items-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with subscriptions belonging to users and organizations.
  name: Clerk Subscriptions API
  phrasing_intents:
  - id: GetUserMainBillingSubscription
    intent: Get my main billing subscription
    question: What plan am I currently subscribed to?
  - id: GetOrganizationBillingSubscription
    intent: Get my organization's subscription as a member
    question: What plan is my organization on, seen from the frontend?
  phrasing_ops: 2
  slug: clerk-com-subscriptions-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Tokens meant for use by end-to-end test suites in requests to the Frontend API, so as to bypass bot detection measures.
  name: Clerk Testing Tokens API
  slug: clerk-com-testing-tokens-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with One Time Password authenticators of the current user.
  name: Clerk TOTP API
  phrasing_intents:
  - id: postTOTP
    intent: Set up an authenticator app secret
    question: How do I enable an authenticator app for two-step verification on my account?
  - id: deleteTOTP
    intent: Remove my authenticator app
    question: How do I turn off authenticator-app two-factor on my account?
  - id: verifyTOTP
    intent: Confirm authenticator app setup with a code
    question: How do I finish setting up my authenticator app with the six-digit code?
  phrasing_ops: 3
  slug: clerk-com-totp-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with the properties of the current user.
  name: Clerk User API
  phrasing_intents:
  - id: getUser
    intent: Get the signed-in user's profile
    question: How does my frontend get the attributes of the currently signed-in user?
  - id: patchUser
    intent: Update the signed-in user's profile
    question: How does a signed-in user change their own first and last name?
  - id: deleteUser
    intent: Delete the signed-in user's account
    question: How can a signed-in user delete their own account from the frontend?
  - id: patchUserMetadata
    intent: Merge the signed-in user's unsafe metadata
    question: How does the frontend add to the current user's unsafe metadata without wiping it?
  - id: createServiceToken
    intent: Mint a JWT for the signed-in user
    question: How do I get a JWT for the current user to call another service?
  - id: updateProfileImage
    intent: Change the signed-in user's avatar
    question: How does a signed-in user upload their own profile picture?
  - id: deleteProfileImage
    intent: Remove the signed-in user's avatar
    question: How does a user remove their own profile picture?
  - id: changePassword
    intent: Change the signed-in user's password
    question: How does a signed-in user change their own password?
  phrasing_ops: 9
  slug: clerk-com-user-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The user object represents a user that has successfully signed up to your application.
  name: Clerk Users API
  phrasing_intents:
  - id: GetUserList
    intent: List and filter users
    question: How do I list every user in my Clerk instance, newest first?
  - id: CreateUser
    intent: Create a new user
    question: How do I create a user account from my backend without a sign-up flow?
  - id: GetUsersCount
    intent: Count users matching filters
    question: How many users are signed up in my application?
  - id: GetUser
    intent: Retrieve a user's details
    question: How do I look up the full profile of one user by their ID?
  - id: UpdateUser
    intent: Update a user's attributes
    question: How do I change a user's name or username from the backend?
  - id: DeleteUser
    intent: Delete a user
    question: How do I permanently remove a user account through the backend API?
  - id: BanUser
    intent: Ban a single user
    question: How do I ban one abusive user so they can never sign in again?
  - id: UnbanUser
    intent: Unban a single user
    question: How do I lift the ban on one user I banned by mistake?
  phrasing_ops: 35
  slug: clerk-com-users-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with the waitlist.
  name: Clerk Waitlist API
  phrasing_intents:
  - id: joinWaitlist
    intent: Join the waitlist
    question: How do I add someone's email to the waitlist?
  phrasing_ops: 1
  slug: clerk-com-waitlist-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Manage waitlist entries.
  name: Clerk Waitlist Entries API
  phrasing_intents:
  - id: ListWaitlistEntries
    intent: List waitlist entries
    question: Who is on the waitlist for my app?
  - id: CreateWaitlistEntry
    intent: Add an email to the waitlist
    question: How do I add someone to my app's waitlist from the backend?
  - id: CreateBulkWaitlistEntries
    intent: Add many emails to the waitlist
    question: How do I import a list of signups onto the waitlist in one call?
  - id: DeleteWaitlistEntry
    intent: Delete a pending waitlist entry
    question: How do I remove someone from the waitlist who is still pending?
  - id: InviteWaitlistEntry
    intent: Invite someone off the waitlist
    question: How do I let a waitlisted person in by sending them an invite?
  - id: RejectWaitlistEntry
    intent: Reject a waitlist entry
    question: How do I turn down someone on the waitlist?
  phrasing_ops: 6
  slug: clerk-com-waitlist-entries-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Used to interact with the web3 wallets of the logged in user.
  name: Clerk Web3 Wallets API
  phrasing_intents:
  - id: getWeb3Wallets
    intent: List my web3 wallets
    question: Which crypto wallets are linked to my account?
  - id: postWeb3Wallets
    intent: Add a web3 wallet to my account
    question: How do I link an Ethereum wallet address to my account?
  - id: readWeb3Wallet
    intent: Get one of my web3 wallets
    question: Is a wallet I linked verified yet?
  - id: deleteWeb3Wallet
    intent: Remove a web3 wallet from my account
    question: How do I unlink a crypto wallet from my profile?
  - id: prepareWeb3WalletVerification
    intent: Start verifying a web3 wallet
    question: How do I get a message to sign so I can prove I own a wallet?
  - id: attemptWeb3WalletVerification
    intent: Verify a web3 wallet with a signature
    question: How do I submit my wallet signature to finish verification?
  phrasing_ops: 6
  slug: clerk-com-web3-wallets-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: You can configure webhooks to be notified about various events that happen on your instance.
  name: Clerk Webhooks API
  phrasing_intents:
  - id: CreateSvixApp
    intent: Enable webhooks via a Svix app
    question: How do I turn on webhooks for my instance by creating a Svix app?
  - id: DeleteSvixApp
    intent: Remove the instance's Svix app
    question: How do I disconnect the Svix webhook app from my instance?
  - id: GenerateSvixAuthURL
    intent: Get a Svix dashboard link
    question: How do I open the Svix dashboard to manage my webhook endpoints?
  phrasing_ops: 3
  slug: clerk-com-webhooks-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Well-known endpoints like JWKS, deep linking, and openid-configuration.
  name: Clerk Well Known API
  phrasing_intents:
  - id: getAndroidAssetLinks
    intent: Get Android asset links for deep linking
    question: Where is the assetlinks.json my Android app needs for verified app links?
  - id: getJWKS
    intent: Get the instance's JSON Web Key Set
    question: Where do I get the public keys to verify session JWTs?
  - id: getAppleAppSiteAssociation
    intent: Get the Apple App Site Association file
    question: Where is the apple-app-site-association file for iOS universal links?
  - id: getOpenIDConfiguration
    intent: Get the OpenID Connect discovery document
    question: Where is the OpenID configuration discovery document for my instance?
  - id: getOAuth2AuthorizationServerMetadata
    intent: Get OAuth 2.0 authorization server metadata
    question: Does the instance publish RFC 8414 authorization server metadata?
  phrasing_ops: 5
  slug: clerk-com-well-known-api
- description: 'Browser-facing API consumed by Clerk''s frontend SDKs and ClerkJS for sign-up, sign-in, session refresh, and user profile mutations. Endpoint is instance-specific (subdomain on clerk.accounts.dev or a '
  name: Clerk Frontend API
  slug: frontend-api
- description: Webhook events delivered via Svix for user, session, organization, email, SMS, and role lifecycle changes. Customers configure endpoints in the dashboard and verify signatures with the Svix libraries.
  name: Clerk Webhooks (Svix)
  slug: webhooks
- description: Official ClerkJS browser library and monorepo of framework adapters (Next.js, React, Expo, React Router, Astro, Chrome Extension, TanStack). Powers Clerk's prebuilt UI components and headless hooks.
  name: Clerk JavaScript SDK
  slug: javascript
- description: Next.js integration covering App Router and Pages Router, middleware, route handlers, server components, and server actions. Distributed from the @clerk/nextjs package inside the JavaScript monorepo.
  name: Clerk Next.js SDK
  slug: sdk-nextjs
- description: React components, hooks, and providers from the @clerk/clerk-react package for plain React SPAs.
  name: Clerk React SDK
  slug: sdk-react
- description: Expo / React Native bindings for Clerk supporting OAuth via deep links, secure session storage, and biometrics.
  name: Clerk Expo SDK
  slug: sdk-expo
- description: Adapter for React Router v7 (Remix successor) covering loaders, actions, and server-rendered authentication.
  name: Clerk React Router SDK
  slug: sdk-react-router
- description: Adapter for the Astro framework with components and middleware.
  name: Clerk Astro SDK
  slug: sdk-astro
- description: Adapter for TanStack Start (React full-stack framework) with route-level authentication helpers.
  name: Clerk TanStack Start SDK
  slug: sdk-tanstack-start
- description: Backend SDK for Node.js (@clerk/backend / @clerk/express / @clerk/fastify) that wraps the Backend API and verifies session JWTs.
  name: Clerk Node.js SDK
  slug: sdk-node
- description: Official Go SDK for the Clerk Backend API.
  name: Clerk Go SDK
  slug: sdk-go
- description: Official Python SDK for the Clerk Backend API.
  name: Clerk Python SDK
  slug: sdk-python
- description: Official Ruby SDK for the Clerk Backend API, with a Rails integration.
  name: Clerk Ruby SDK
  slug: sdk-ruby
- description: Official Java SDK for the Clerk Backend API.
  name: Clerk Java SDK
  slug: sdk-java
- description: Official PHP SDK for the Clerk Backend API.
  name: Clerk PHP SDK
  slug: sdk-php
- description: Official C# / .NET SDK for the Clerk Backend API.
  name: Clerk C# / .NET SDK
  slug: sdk-csharp
- description: Public repository of OpenAPI specifications for Clerk's APIs, used as the source for generated SDKs and documentation.
  name: Clerk OpenAPI Specifications
  slug: openapi-specs
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The Admin Portal Link Tokens API from Clerk — 2 operation(s) for admin portal link tokens.
  name: Clerk Admin Portal Link Tokens API
  slug: clerk-com-admin-portal-link-tokens-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The Directories API from Clerk — 5 operation(s) for directories.
  name: Clerk Directories API
  slug: clerk-com-directories-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The SCIM Directories API from Clerk — 5 operation(s) for scim directories.
  name: Clerk SCIM Directories API
  slug: clerk-com-scim-directories-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: The SSO bypass allowlist names users who may sign in with an email code when their enterprise identity provider is unreachable.
  name: Clerk SSO Bypass API
  slug: clerk-com-sso-bypass-api
- baseURL: https://api.clerk.com/v1
  baseurl_source: declared
  description: Sign-up objects track the progress of a sign-up attempt and store any field collected from user input.
  name: Clerk Signups API
  phrasing_intents:
  - id: GetSignUp
    intent: Retrieve a sign-up from the backend
    question: Can my server look up a sign-up attempt by its ID?
  - id: UpdateSignUp
    intent: Set a sign-up's external ID or custom action
    question: How do I attach my own external ID to a sign-up from my backend?
  - id: createSignUps
    intent: Start a sign-up on the current client
    question: How do I register a new user with email and password?
  - id: getSignUps
    intent: Get the current client's sign-up
    question: Which fields are still missing on my in-progress sign-up?
  - id: updateSignUps
    intent: Add details to an in-progress sign-up
    question: How do I add a phone number or username to a sign-up already started?
  - id: prepareSignUpsVerification
    intent: Send a verification code for a sign-up
    question: How do I send the new user a code to verify their email during sign-up?
  - id: attemptSignUpsVerification
    intent: Submit a sign-up verification code
    question: How do I complete sign-up with the code the user received?
  phrasing_ops: 7
  slug: clerk-com-signups-api
artifact_total: 318
collections:
- collection_type: postman
  name: Clerk Backend Account Portal API
  slug: postman-clerk-com-account-portal-api
- collection_type: postman
  name: Clerk Backend Account Portal Active Sessions API
  slug: postman-clerk-com-active-sessions-api
- collection_type: postman
  name: Clerk Backend Account Portal Actor Tokens API
  slug: postman-clerk-com-actor-tokens-api
- collection_type: postman
  name: Clerk Backend Account Portal Agent Tasks API
  slug: postman-clerk-com-agent-tasks-api
- collection_type: postman
  name: Clerk Backend Account Portal Allow-list / Block-list API
  slug: postman-clerk-com-allow-list-block-list-api
- collection_type: postman
  name: Clerk Backend Account Portal API Keys API
  slug: postman-clerk-com-api-keys-api
- collection_type: postman
  name: Clerk Backend Account Portal Application Transfers API
  slug: postman-clerk-com-application-transfers-api
- collection_type: postman
  name: Clerk Backend Account Portal Applications API
  slug: postman-clerk-com-applications-api
- collection_type: postman
  name: Clerk Backend Account Portal Backup Codes API
  slug: postman-clerk-com-backup-codes-api
- collection_type: postman
  name: Clerk Backend Account Portal Beta Features API
  slug: postman-clerk-com-beta-features-api
- collection_type: postman
  name: Clerk Backend Account Portal Billing API
  slug: postman-clerk-com-billing-api
- collection_type: postman
  name: Clerk Backend Account Portal Checkouts API
  slug: postman-clerk-com-checkouts-api
- collection_type: postman
  name: Clerk Backend Account Portal Clear Site Data API
  slug: postman-clerk-com-clear-site-data-api
- collection_type: postman
  name: Clerk Backend Account Portal Client API
  slug: postman-clerk-com-client-api
- collection_type: postman
  name: Clerk Backend Account Portal Clients API
  slug: postman-clerk-com-clients-api
- collection_type: postman
  name: Clerk Backend Account Portal Config API
  slug: postman-clerk-com-config-api
- collection_type: postman
  name: Clerk Backend Account Portal Dev Browser API
  slug: postman-clerk-com-dev-browser-api
- collection_type: postman
  name: Clerk Backend Account Portal DevBrowser API
  slug: postman-clerk-com-devbrowser-api
- collection_type: postman
  name: Clerk Backend Account Portal Domains API
  slug: postman-clerk-com-domains-api
- collection_type: postman
  name: Clerk Backend Account Portal Email Addresses API
  slug: postman-clerk-com-email-addresses-api
- collection_type: postman
  name: Clerk Backend Account Portal Email & SMS Templates API
  slug: postman-clerk-com-email-sms-templates-api
- collection_type: postman
  name: Clerk Backend Account Portal Enterprise Connections API
  slug: postman-clerk-com-enterprise-connections-api
- collection_type: postman
  name: Clerk Backend Account Portal Environment API
  slug: postman-clerk-com-environment-api
- collection_type: postman
  name: Clerk Backend Account Portal External Accounts API
  slug: postman-clerk-com-external-accounts-api
- collection_type: postman
  name: Clerk Backend Account Portal Health API
  slug: postman-clerk-com-health-api
- collection_type: postman
  name: Clerk Backend Account Portal Instance Settings API
  slug: postman-clerk-com-instance-settings-api
- collection_type: postman
  name: Clerk Backend Account Portal Invitations API
  slug: postman-clerk-com-invitations-api
- collection_type: postman
  name: Clerk Backend Account Portal JWKS API
  slug: postman-clerk-com-jwks-api
- collection_type: postman
  name: Clerk Backend Account Portal JWT Templates API
  slug: postman-clerk-com-jwt-templates-api
- collection_type: postman
  name: Clerk Backend Account Portal M2M Tokens API
  slug: postman-clerk-com-m2m-tokens-api
- collection_type: postman
  name: Clerk Backend Account Portal Machines API
  slug: postman-clerk-com-machines-api
- collection_type: postman
  name: Clerk Backend Account Portal Members API
  slug: postman-clerk-com-members-api
- collection_type: postman
  name: Clerk Backend Account Portal Membership Requests API
  slug: postman-clerk-com-membership-requests-api
- collection_type: postman
  name: Clerk Backend Account Portal Miscellaneous API
  slug: postman-clerk-com-miscellaneous-api
- collection_type: postman
  name: Clerk Backend Account Portal OAuth Access Tokens API
  slug: postman-clerk-com-oauth-access-tokens-api
- collection_type: postman
  name: Clerk Backend Account Portal OAuth Applications API
  slug: postman-clerk-com-oauth-applications-api
- collection_type: postman
  name: Clerk Backend Account Portal OAuth2 Callbacks API
  slug: postman-clerk-com-oauth2-callbacks-api
- collection_type: postman
  name: Clerk Backend Account Portal OAuth2 Identity Provider API
  slug: postman-clerk-com-oauth2-identity-provider-api
- collection_type: postman
  name: Clerk Backend Account Portal Organization API
  slug: postman-clerk-com-organization-api
- collection_type: postman
  name: Clerk Backend Account Portal Organization Creation Defaults API
  slug: postman-clerk-com-organization-creation-defaults-api
- collection_type: postman
  name: Clerk Backend Account Portal Organization Domains API
  slug: postman-clerk-com-organization-domains-api
- collection_type: postman
  name: Clerk Backend Account Portal Organization Invitations API
  slug: postman-clerk-com-organization-invitations-api
- collection_type: postman
  name: Clerk Backend Account Portal Organization Memberships API
  slug: postman-clerk-com-organization-memberships-api
- collection_type: postman
  name: Clerk Backend Account Portal Organization Permissions API
  slug: postman-clerk-com-organization-permissions-api
- collection_type: postman
  name: Clerk Backend Account Portal Organization Roles API
  slug: postman-clerk-com-organization-roles-api
- collection_type: postman
  name: Clerk Backend Account Portal Organizations API
  slug: postman-clerk-com-organizations-api
- collection_type: postman
  name: Clerk Backend Account Portal Organizations Memberships API
  slug: postman-clerk-com-organizations-memberships-api
- collection_type: postman
  name: Clerk Backend Account Portal Passkeys API
  slug: postman-clerk-com-passkeys-api
- collection_type: postman
  name: Clerk Backend Account Portal Payment Attempts API
  slug: postman-clerk-com-payment-attempts-api
- collection_type: postman
  name: Clerk Backend Account Portal Payment Methods API
  slug: postman-clerk-com-payment-methods-api
- collection_type: postman
  name: Clerk Backend Account Portal Phone Numbers API
  slug: postman-clerk-com-phone-numbers-api
- collection_type: postman
  name: Clerk Backend Account Portal Plans API
  slug: postman-clerk-com-plans-api
- collection_type: postman
  name: Clerk Backend Account Portal Proxy Checks API
  slug: postman-clerk-com-proxy-checks-api
- collection_type: postman
  name: Clerk Backend Account Portal Proxy Health API
  slug: postman-clerk-com-proxy-health-api
- collection_type: postman
  name: Clerk Backend Account Portal Redirect API
  slug: postman-clerk-com-redirect-api
- collection_type: postman
  name: Clerk Backend Account Portal Redirect URLs API
  slug: postman-clerk-com-redirect-urls-api
- collection_type: postman
  name: Clerk Backend Account Portal Role Sets API
  slug: postman-clerk-com-role-sets-api
- collection_type: postman
  name: Clerk Backend Account Portal Roles API
  slug: postman-clerk-com-roles-api
- collection_type: postman
  name: Clerk Backend Account Portal SAML API
  slug: postman-clerk-com-saml-api
- collection_type: postman
  name: Clerk Backend Account Portal SAML Connections API
  slug: postman-clerk-com-saml-connections-api
- collection_type: postman
  name: Clerk Backend Account Portal Sessions API
  slug: postman-clerk-com-sessions-api
- collection_type: postman
  name: Clerk Backend Account Portal Sign-in Tokens API
  slug: postman-clerk-com-sign-in-tokens-api
- collection_type: postman
  name: Clerk Backend Account Portal Sign Ins API
  slug: postman-clerk-com-sign-ins-api
- collection_type: postman
  name: Clerk Backend Account Portal Sign Ups API
  slug: postman-clerk-com-sign-ups-api
- collection_type: postman
  name: Clerk Backend Account Portal Statements API
  slug: postman-clerk-com-statements-api
- collection_type: postman
  name: Clerk Backend Account Portal Subscription Items API
  slug: postman-clerk-com-subscription-items-api
- collection_type: postman
  name: Clerk Backend Account Portal Subscriptions API
  slug: postman-clerk-com-subscriptions-api
- collection_type: postman
  name: Clerk Backend Account Portal Testing Tokens API
  slug: postman-clerk-com-testing-tokens-api
- collection_type: postman
  name: Clerk Backend Account Portal TOTP API
  slug: postman-clerk-com-totp-api
- collection_type: postman
  name: Clerk Backend Account Portal User API
  slug: postman-clerk-com-user-api
- collection_type: postman
  name: Clerk Backend Account Portal Users API
  slug: postman-clerk-com-users-api
- collection_type: postman
  name: Clerk Backend Account Portal Waitlist API
  slug: postman-clerk-com-waitlist-api
- collection_type: postman
  name: Clerk Backend Account Portal Waitlist Entries API
  slug: postman-clerk-com-waitlist-entries-api
- collection_type: postman
  name: Clerk Backend Account Portal Web3 Wallets API
  slug: postman-clerk-com-web3-wallets-api
- collection_type: postman
  name: Clerk Backend Account Portal Webhooks API
  slug: postman-clerk-com-webhooks-api
- collection_type: postman
  name: Clerk Backend Account Portal Well Known API
  slug: postman-clerk-com-well-known-api
- collection_type: open
  name: Clerk Backend API
  slug: open-clerk-backend-api
- collection_type: open
  name: Clerk Backend Account Portal API
  slug: open-clerk-com-account-portal-api
- collection_type: open
  name: Clerk Backend Account Portal Active Sessions API
  slug: open-clerk-com-active-sessions-api
- collection_type: open
  name: Clerk Backend Account Portal Actor Tokens API
  slug: open-clerk-com-actor-tokens-api
- collection_type: open
  name: Clerk Backend Account Portal Agent Tasks API
  slug: open-clerk-com-agent-tasks-api
- collection_type: open
  name: Clerk Backend Account Portal Allow-list / Block-list API
  slug: open-clerk-com-allow-list-block-list-api
- collection_type: open
  name: Clerk Backend Account Portal API Keys API
  slug: open-clerk-com-api-keys-api
- collection_type: open
  name: Clerk Backend Account Portal Application Transfers API
  slug: open-clerk-com-application-transfers-api
- collection_type: open
  name: Clerk Backend Account Portal Applications API
  slug: open-clerk-com-applications-api
- collection_type: open
  name: Clerk Backend Account Portal Backup Codes API
  slug: open-clerk-com-backup-codes-api
- collection_type: open
  name: Clerk Backend Account Portal Beta Features API
  slug: open-clerk-com-beta-features-api
- collection_type: open
  name: Clerk Backend Account Portal Billing API
  slug: open-clerk-com-billing-api
- collection_type: open
  name: Clerk Backend Account Portal Checkouts API
  slug: open-clerk-com-checkouts-api
- collection_type: open
  name: Clerk Backend Account Portal Clear Site Data API
  slug: open-clerk-com-clear-site-data-api
- collection_type: open
  name: Clerk Backend Account Portal Client API
  slug: open-clerk-com-client-api
- collection_type: open
  name: Clerk Backend Account Portal Clients API
  slug: open-clerk-com-clients-api
- collection_type: open
  name: Clerk Backend Account Portal Config API
  slug: open-clerk-com-config-api
- collection_type: open
  name: Clerk Backend Account Portal Dev Browser API
  slug: open-clerk-com-dev-browser-api
- collection_type: open
  name: Clerk Backend Account Portal DevBrowser API
  slug: open-clerk-com-devbrowser-api
- collection_type: open
  name: Clerk Backend Account Portal Domains API
  slug: open-clerk-com-domains-api
- collection_type: open
  name: Clerk Backend Account Portal Email Addresses API
  slug: open-clerk-com-email-addresses-api
- collection_type: open
  name: Clerk Backend Account Portal Email & SMS Templates API
  slug: open-clerk-com-email-sms-templates-api
- collection_type: open
  name: Clerk Backend Account Portal Enterprise Connections API
  slug: open-clerk-com-enterprise-connections-api
- collection_type: open
  name: Clerk Backend Account Portal Environment API
  slug: open-clerk-com-environment-api
- collection_type: open
  name: Clerk Backend Account Portal External Accounts API
  slug: open-clerk-com-external-accounts-api
- collection_type: open
  name: Clerk Backend Account Portal Health API
  slug: open-clerk-com-health-api
- collection_type: open
  name: Clerk Backend Account Portal Instance Settings API
  slug: open-clerk-com-instance-settings-api
- collection_type: open
  name: Clerk Backend Account Portal Invitations API
  slug: open-clerk-com-invitations-api
- collection_type: open
  name: Clerk Backend Account Portal JWKS API
  slug: open-clerk-com-jwks-api
- collection_type: open
  name: Clerk Backend Account Portal JWT Templates API
  slug: open-clerk-com-jwt-templates-api
- collection_type: open
  name: Clerk Backend Account Portal M2M Tokens API
  slug: open-clerk-com-m2m-tokens-api
- collection_type: open
  name: Clerk Backend Account Portal Machines API
  slug: open-clerk-com-machines-api
- collection_type: open
  name: Clerk Backend Account Portal Members API
  slug: open-clerk-com-members-api
- collection_type: open
  name: Clerk Backend Account Portal Membership Requests API
  slug: open-clerk-com-membership-requests-api
- collection_type: open
  name: Clerk Backend Account Portal Miscellaneous API
  slug: open-clerk-com-miscellaneous-api
- collection_type: open
  name: Clerk Backend Account Portal OAuth Access Tokens API
  slug: open-clerk-com-oauth-access-tokens-api
- collection_type: open
  name: Clerk Backend Account Portal OAuth Applications API
  slug: open-clerk-com-oauth-applications-api
- collection_type: open
  name: Clerk Backend Account Portal OAuth2 Callbacks API
  slug: open-clerk-com-oauth2-callbacks-api
- collection_type: open
  name: Clerk Backend Account Portal OAuth2 Identity Provider API
  slug: open-clerk-com-oauth2-identity-provider-api
- collection_type: open
  name: Clerk Backend Account Portal Organization API
  slug: open-clerk-com-organization-api
- collection_type: open
  name: Clerk Backend Account Portal Organization Creation Defaults API
  slug: open-clerk-com-organization-creation-defaults-api
- collection_type: open
  name: Clerk Backend Account Portal Organization Domains API
  slug: open-clerk-com-organization-domains-api
- collection_type: open
  name: Clerk Backend Account Portal Organization Invitations API
  slug: open-clerk-com-organization-invitations-api
- collection_type: open
  name: Clerk Backend Account Portal Organization Memberships API
  slug: open-clerk-com-organization-memberships-api
- collection_type: open
  name: Clerk Backend Account Portal Organization Permissions API
  slug: open-clerk-com-organization-permissions-api
- collection_type: open
  name: Clerk Backend Account Portal Organization Roles API
  slug: open-clerk-com-organization-roles-api
- collection_type: open
  name: Clerk Backend Account Portal Organizations API
  slug: open-clerk-com-organizations-api
- collection_type: open
  name: Clerk Backend Account Portal Organizations Memberships API
  slug: open-clerk-com-organizations-memberships-api
- collection_type: open
  name: Clerk Backend Account Portal Passkeys API
  slug: open-clerk-com-passkeys-api
- collection_type: open
  name: Clerk Backend Account Portal Payment Attempts API
  slug: open-clerk-com-payment-attempts-api
- collection_type: open
  name: Clerk Backend Account Portal Payment Methods API
  slug: open-clerk-com-payment-methods-api
- collection_type: open
  name: Clerk Backend Account Portal Phone Numbers API
  slug: open-clerk-com-phone-numbers-api
- collection_type: open
  name: Clerk Backend Account Portal Plans API
  slug: open-clerk-com-plans-api
- collection_type: open
  name: Clerk Backend Account Portal Proxy Checks API
  slug: open-clerk-com-proxy-checks-api
- collection_type: open
  name: Clerk Backend Account Portal Proxy Health API
  slug: open-clerk-com-proxy-health-api
- collection_type: open
  name: Clerk Backend Account Portal Redirect API
  slug: open-clerk-com-redirect-api
- collection_type: open
  name: Clerk Backend Account Portal Redirect URLs API
  slug: open-clerk-com-redirect-urls-api
- collection_type: open
  name: Clerk Backend Account Portal Role Sets API
  slug: open-clerk-com-role-sets-api
- collection_type: open
  name: Clerk Backend Account Portal Roles API
  slug: open-clerk-com-roles-api
- collection_type: open
  name: Clerk Backend Account Portal SAML API
  slug: open-clerk-com-saml-api
- collection_type: open
  name: Clerk Backend Account Portal SAML Connections API
  slug: open-clerk-com-saml-connections-api
- collection_type: open
  name: Clerk Backend Account Portal Sessions API
  slug: open-clerk-com-sessions-api
- collection_type: open
  name: Clerk Backend Account Portal Sign-in Tokens API
  slug: open-clerk-com-sign-in-tokens-api
- collection_type: open
  name: Clerk Backend Account Portal Sign Ins API
  slug: open-clerk-com-sign-ins-api
- collection_type: open
  name: Clerk Backend Account Portal Sign Ups API
  slug: open-clerk-com-sign-ups-api
- collection_type: open
  name: Clerk Backend Account Portal Statements API
  slug: open-clerk-com-statements-api
- collection_type: open
  name: Clerk Backend Account Portal Subscription Items API
  slug: open-clerk-com-subscription-items-api
- collection_type: open
  name: Clerk Backend Account Portal Subscriptions API
  slug: open-clerk-com-subscriptions-api
- collection_type: open
  name: Clerk Backend Account Portal Testing Tokens API
  slug: open-clerk-com-testing-tokens-api
- collection_type: open
  name: Clerk Backend Account Portal TOTP API
  slug: open-clerk-com-totp-api
- collection_type: open
  name: Clerk Backend Account Portal User API
  slug: open-clerk-com-user-api
- collection_type: open
  name: Clerk Backend Account Portal Users API
  slug: open-clerk-com-users-api
- collection_type: open
  name: Clerk Backend Account Portal Waitlist API
  slug: open-clerk-com-waitlist-api
- collection_type: open
  name: Clerk Backend Account Portal Waitlist Entries API
  slug: open-clerk-com-waitlist-entries-api
- collection_type: open
  name: Clerk Backend Account Portal Web3 Wallets API
  slug: open-clerk-com-web3-wallets-api
- collection_type: open
  name: Clerk Backend Account Portal Webhooks API
  slug: open-clerk-com-webhooks-api
- collection_type: open
  name: Clerk Backend Account Portal Well Known API
  slug: open-clerk-com-well-known-api
- collection_type: open
  name: Clerk Frontend API
  slug: open-clerk-frontend-api
- collection_type: open
  name: Clerk Platform API
  slug: open-clerk-platform-api
- collection_type: open
  name: Clerk Webhook Events
  slug: open-clerk-webhooks
common:
- group: other
  href: https://artifacts.apis.io/clerk-com/vendor-facets/clerk-com-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/clerk-com-vendor-facets.yml
- group: other
  href: https://artifacts.apis.io/clerk-com/capabilities/clerk-com-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/clerk-com-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/clerk/overview
- group: agent
  href: https://artifacts.apis.io/clerk-com/agentic-access/clerk-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clerk-com-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/clerk-com/security/clerk-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clerk-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clerk-com/security/clerk-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clerk-com-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/clerk-com/authentication/clerk-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clerk-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://clerk.com
- group: docs
  title: ''
  type: Documentation
  url: https://clerk.com/docs
- group: start
  title: ''
  type: Signup
  url: https://dashboard.clerk.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://dashboard.clerk.com/sign-in
- group: commercial
  title: ''
  type: Pricing
  url: https://clerk.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clerk.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clerk.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://clerk.com/security
- group: company
  title: ''
  type: Blog
  url: https://clerk.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://clerk.com/changelog
- group: operate
  title: ''
  type: ChangelogRSS
  url: https://clerk.com/changelog/atom.xml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clerk.com
- group: operate
  title: ''
  type: Support
  url: https://clerk.com/support
- group: build
  title: ''
  type: GitHub
  url: https://github.com/clerk
- group: docs
  title: ''
  type: OpenAPIRepository
  url: https://github.com/clerk/openapi-specs
- group: other
  title: ''
  type: X
  url: https://x.com/ClerkDev
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/javascript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-csharp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-ios
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-android
- group: build
  title: ''
  type: SDKs
  url: https://github.com/clerk/clerk-sdk-flutter
- group: build
  title: ''
  type: CLI
  url: https://github.com/clerk/cli
- group: build
  title: ''
  type: CLI
  url: https://github.com/clerk/protect-cli
- group: build
  title: ''
  type: Tools
  url: https://github.com/clerk/agent-toolkit-example
- group: build
  title: ''
  type: Tools
  url: https://github.com/clerk/agentpass
- group: build
  title: ''
  type: Tools
  url: https://github.com/clerk/mcp-tools
- group: build
  title: ''
  type: Tools
  url: https://github.com/clerk/migration-tool
- group: commercial
  href: https://artifacts.apis.io/clerk-com/plans/clerk-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clerk-com-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/clerk-com/rate-limits/clerk-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clerk-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/clerk-com/finops/clerk-com-finops.yml
  title: ''
  type: FinOps
  url: finops/clerk-com-finops.yml
- group: design
  href: https://artifacts.apis.io/clerk-com/vocabulary/clerk-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clerk-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clerk-com/json-ld/clerk-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clerk-com-context.jsonld
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-user-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-user-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-user-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-user-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-session-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-session-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-session-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-session-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-organization-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-organization-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-organization-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-organization-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-organizationmembership-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-organizationmembership-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-organizationmembership-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-organizationmembership-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-organizationinvitation-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-organizationinvitation-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-organizationinvitation-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-organizationinvitation-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-invitation-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-invitation-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-invitation-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-invitation-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-emailaddress-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-emailaddress-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-emailaddress-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-emailaddress-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-phonenumber-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-phonenumber-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-phonenumber-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-phonenumber-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-client-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-client-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-client-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-client-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-oauthapplication-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-oauthapplication-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-oauthapplication-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-oauthapplication-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-samlconnection-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-samlconnection-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-samlconnection-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-samlconnection-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-jwttemplate-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-jwttemplate-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-jwttemplate-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-jwttemplate-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-signintoken-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-signintoken-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-signintoken-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-signintoken-structure.json
- group: docs
  href: https://artifacts.apis.io/clerk-com/json-schema/clerk-actortoken-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/clerk-actortoken-schema.json
- group: design
  href: https://artifacts.apis.io/clerk-com/json-structure/clerk-actortoken-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/clerk-actortoken-structure.json
- group: agent
  title: ''
  type: LlmsText
  url: https://clerk.com/llms.txt
created: '2026-05-22'
description: Clerk is a complete user management and authentication infrastructure platform offering embeddable UI components, flexible APIs, and admin dashboards. It provides full-stack authentication including multi-factor authentication, social sign-on, passkeys, organizations for B2B SaaS, billing, session management, and machine-to-machine authentication, with SDKs spanning Next.js, React, Expo, iOS, Android, Go, Python, Ruby, Java, PHP, and C#.
examples:
- key_count: 9
  name: Clerk Actortoken Example
  slug: clerk-actortoken-example
- key_count: 7
  name: Clerk Backend Api Getapikeys 200
  slug: clerk-backend-api-getapikeys-200
- key_count: 7
  name: Clerk Backend Api Getm2Mtokens 200
  slug: clerk-backend-api-getm2mtokens-200
- key_count: 7
  name: Clerk Backend Api Verifyoauthaccesstoken 200
  slug: clerk-backend-api-verifyoauthaccesstoken-200
- key_count: 10
  name: Clerk Client Example
  slug: clerk-client-example
- key_count: 9
  name: Clerk Emailaddress Example
  slug: clerk-emailaddress-example
- key_count: 7
  name: Clerk Frontend Api Getapikeys 200
  slug: clerk-frontend-api-getapikeys-200
- key_count: 7
  name: Clerk Frontend Api Gethealth 200
  slug: clerk-frontend-api-gethealth-200
- key_count: 7
  name: Clerk Frontend Api Getorganizationcreationdefaults 200
  slug: clerk-frontend-api-getorganizationcreationdefaults-200
- key_count: 10
  name: Clerk Invitation Example
  slug: clerk-invitation-example
- key_count: 10
  name: Clerk Jwttemplate Example
  slug: clerk-jwttemplate-example
- key_count: 21
  name: Clerk Oauthapplication Example
  slug: clerk-oauthapplication-example
- key_count: 18
  name: Clerk Organization Example
  slug: clerk-organization-example
- key_count: 15
  name: Clerk Organizationinvitation Example
  slug: clerk-organizationinvitation-example
- key_count: 11
  name: Clerk Organizationmembership Example
  slug: clerk-organizationmembership-example
- key_count: 11
  name: Clerk Phonenumber Example
  slug: clerk-phonenumber-example
- key_count: 7
  name: Clerk Platform Api Platformgetconfig 200
  slug: clerk-platform-api-platformgetconfig-200
- key_count: 7
  name: Clerk Platform Api Platformlistapplicationdomains 200
  slug: clerk-platform-api-platformlistapplicationdomains-200
- key_count: 7
  name: Clerk Platform Api Platformlistapplications 200
  slug: clerk-platform-api-platformlistapplications-200
- key_count: 7
  name: Clerk Platform Api Platformlistapplicationtransfers 200
  slug: clerk-platform-api-platformlistapplicationtransfers-200
- key_count: 7
  name: Clerk Platform Api Platformlistinstanceusers 200
  slug: clerk-platform-api-platformlistinstanceusers-200
- key_count: 7
  name: Clerk Platform Api Platformlistjwttemplates 200
  slug: clerk-platform-api-platformlistjwttemplates-200
- key_count: 7
  name: Clerk Platform Api Platformlistredirecturls 200
  slug: clerk-platform-api-platformlistredirecturls-200
- key_count: 14
  name: Clerk Session Example
  slug: clerk-session-example
- key_count: 8
  name: Clerk Signintoken Example
  slug: clerk-signintoken-example
- key_count: 46
  name: Clerk User Example
  slug: clerk-user-example
finops:
- has_sources: true
  method: derived
  name: Clerk Com Finops
  primary_unit: subscription
  service_category: ''
  slug: clerk-com-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clerk-com.png
json_schemas:
- name: Clerk ActorToken
  property_count: 9
  slug: clerk-actortoken
- name: Clerk Client
  property_count: 10
  slug: clerk-client
- name: Clerk EmailAddress
  property_count: 9
  slug: clerk-emailaddress
- name: Clerk Invitation
  property_count: 10
  slug: clerk-invitation
- name: Clerk JWTTemplate
  property_count: 10
  slug: clerk-jwttemplate
- name: Clerk OAuthApplication
  property_count: 21
  slug: clerk-oauthapplication
- name: Clerk Organization
  property_count: 18
  slug: clerk-organization
- name: Clerk OrganizationInvitation
  property_count: 15
  slug: clerk-organizationinvitation
- name: Clerk OrganizationMembership
  property_count: 11
  slug: clerk-organizationmembership
- name: Clerk PhoneNumber
  property_count: 11
  slug: clerk-phonenumber
- name: Clerk SAMLConnection
  property_count: 27
  slug: clerk-samlconnection
- name: Clerk Session
  property_count: 14
  slug: clerk-session
- name: Clerk SignInToken
  property_count: 8
  slug: clerk-signintoken
- name: Clerk User
  property_count: 46
  slug: clerk-user
json_structures:
- name: Clerk Actortoken Structure
  property_count: 0
  slug: clerk-actortoken-structure
- name: Clerk Client Structure
  property_count: 0
  slug: clerk-client-structure
- name: Clerk Emailaddress Structure
  property_count: 0
  slug: clerk-emailaddress-structure
- name: Clerk Invitation Structure
  property_count: 0
  slug: clerk-invitation-structure
- name: Clerk Jwttemplate Structure
  property_count: 0
  slug: clerk-jwttemplate-structure
- name: Clerk Oauthapplication Structure
  property_count: 0
  slug: clerk-oauthapplication-structure
- name: Clerk Organization Structure
  property_count: 0
  slug: clerk-organization-structure
- name: Clerk Organizationinvitation Structure
  property_count: 0
  slug: clerk-organizationinvitation-structure
- name: Clerk Organizationmembership Structure
  property_count: 0
  slug: clerk-organizationmembership-structure
- name: Clerk Phonenumber Structure
  property_count: 0
  slug: clerk-phonenumber-structure
- name: Clerk Samlconnection Structure
  property_count: 0
  slug: clerk-samlconnection-structure
- name: Clerk Session Structure
  property_count: 0
  slug: clerk-session-structure
- name: Clerk Signintoken Structure
  property_count: 0
  slug: clerk-signintoken-structure
- name: Clerk User Structure
  property_count: 0
  slug: clerk-user-structure
jsonld:
- class_count: 66
  name: Clerk Com Context
  property_count: 6
  slug: clerk-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.clerk.com over HTTP; 2 tools listed.
  name: Clerk MCP Server
  slug: clerk-com
modified: '2026-09-16'
name: Clerk
nav: Providers
network: true
overview: 'Clerk publishes 96 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Portal API, Active Sessions API, Actor Tokens API, and 93 more. Tagged areas include Authentication, Authorization, B2B SaaS, CIAM, and Identity and Access Management.


  The Clerk catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Clerk''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, changelog, support, and 66 more developer resources.'
plans:
- name: Clerk Com Plans Pricing
  plan_count: 3
  slug: clerk-com-plans-pricing
- name: Clerk Com Price Estimates
  plan_count: 0
  slug: clerk-com-price-estimates
random_paper: 5
rate_limits:
- limit_count: 14
  name: Clerk Com Rate Limits
  slug: clerk-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Clerk — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: clerk-com-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Clerk — clerk rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 4
    warn: 3
  slug: clerk-rules
score:
  band: exemplar
  composite: 72.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 84.0
    catalog_earned_first_party: 24.0
    catalog_gap: 31.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 27.3
    contract_quality: 70.3
    developer_ergonomics: 72.6
    discoverability: 80.0
    operational_transparency: 68.4
  previous_composite: 72.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 154
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/clerk-com/clerk-com-2026-06-20T174512.png
security:
- kind: authentication
  name: Clerk Com Authentication
  slug: clerk-com-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Clerk Com Domain Security
  slug: clerk-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Clerk Com Vulnerability Disclosure
  slug: clerk-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: clerk-com
tags:
- Authentication
- Authorization
- B2B SaaS
- CIAM
- Identity and Access Management
- MFA
- OAuth
- OpenID Connect
- Organization
- Passkeys
- SAML
- Security
- Sessions
- SSO
- User Management
- Identity Federation
website: https://clerk.com
---
