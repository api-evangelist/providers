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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.2
  scored_at: '2026-11-06'
api_count: 8
apis:
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Account API from Strivacity — 23 operation(s) for account.
  name: Strivacity Account API
  phrasing_intents:
  - id: listAccounts
    intent: List accounts in an identity store
    question: Which accounts in my identity store have never logged in?
  - id: createAccount
    intent: Create a customer account
    question: How do I create a new user account in a Strivacity identity store?
  - id: deleteAccountById
    intent: Delete an account
    question: How do I permanently delete a user account?
  - id: getAccountById
    intent: Get an account's details
    question: What details are stored on a single customer account?
  - id: addAuthenticator
    intent: Add an email or phone authenticator
    question: How do I add a phone number as an MFA authenticator for a user?
  - id: deleteAuthenticator
    intent: Remove an authenticator from an account
    question: How do I remove an MFA authenticator from a user's account?
  - id: disableAccount
    intent: Disable an account
    question: How do I disable a user so they can no longer sign in?
  - id: enableAccount
    intent: Re-enable a disabled account
    question: How do I re-enable an account that was disabled?
  phrasing_ops: 27
  slug: strivacity-account-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Account Attribute API from Strivacity — 2 operation(s) for account attribute.
  name: Strivacity Account Attribute API
  phrasing_intents:
  - id: getAllAccountAttributes
    intent: List account attributes
    question: What account attributes are defined in an identity store?
  - id: createAccountAttribute
    intent: Create an account attribute
    question: How do I add a custom profile field to customer accounts?
  - id: reorderAccountAttributes
    intent: Reorder account attributes
    question: How do I change the display order of account attributes?
  - id: getAccountAttribute_1
    intent: Get an account attribute
    question: Can I view the definition of one account attribute?
  - id: updateAccountAttribute_1
    intent: Update an account attribute
    question: Which parts of an account attribute can't be changed after creation?
  phrasing_ops: 5
  slug: strivacity-account-attribute-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Account Child Attribute API from Strivacity — 2 operation(s) for account child attribute.
  name: Strivacity Account Child Attribute API
  phrasing_intents:
  - id: getAllAccountAttributes_1
    intent: List child attributes of a complex attribute
    question: Which sub-fields belong to a complex account attribute like address?
  - id: createAccountAttribute_1
    intent: Add a child attribute to a complex attribute
    question: How do I add a new sub-field such as postal code to a complex attribute?
  - id: reorderAccountAttributes_1
    intent: Reorder child attributes of a complex attribute
    question: How do I change the display order of fields inside a complex attribute?
  - id: getAccountAttribute
    intent: Get a child attribute
    question: How do I view the definition of one child attribute?
  - id: updateAccountAttribute
    intent: Update a child attribute
    question: Can I change the type or name of an existing child attribute?
  phrasing_ops: 5
  slug: strivacity-account-child-attribute-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Account Event API from Strivacity — 5 operation(s) for account event.
  name: Strivacity Account Event API
  phrasing_intents:
  - id: getAccountEvents
    intent: List customer account events
    question: What login and registration events happened for a customer account?
  - id: getAccountEventById
    intent: Get a customer account event
    question: What exactly happened in a single account event?
  - id: getDescriptor
    intent: List account event type descriptors
    question: What event types can appear in the account event log?
  - id: getNotificationEvents
    intent: List customer notification events
    question: Was a notification email or SMS actually delivered to a customer?
  - id: getNotificationEventById
    intent: Get a customer notification event
    question: What happened with one specific notification that was sent?
  phrasing_ops: 5
  slug: strivacity-account-event-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Account Event TTL API from Strivacity — 1 operation(s) for account event ttl.
  name: Strivacity Account Event TTL API
  phrasing_intents:
  - id: getAvailableAccountEventTTLs
    intent: List account event retention options
    question: How long can account events be kept in an identity store?
  phrasing_ops: 1
  slug: strivacity-account-event-ttl-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Account Identity API from Strivacity — 3 operation(s) for account identity.
  name: Strivacity Account Identity API
  phrasing_intents:
  - id: getIdentities
    intent: List identities linked to an account
    question: Which social or external logins are linked to a user's account?
  - id: forceSyncConnectorIdentity
    intent: Force sync a connector identity
    question: How do I force a user's connector identity to resync from the source system?
  - id: deleteExternalIdentity
    intent: Unlink an external identity from an account
    question: How do I unlink a social login from a user's account?
  phrasing_ops: 3
  slug: strivacity-account-identity-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Account Invitation API from Strivacity — 3 operation(s) for account invitation.
  name: Strivacity Account Invitation API
  phrasing_intents:
  - id: getAccountInvitations
    intent: List account invitations
    question: Which customer invitations are still pending in an identity store?
  - id: createInvitation
    intent: Invite someone to create an account
    question: How do I invite someone by email to register a customer account?
  - id: deleteAccountInvitation
    intent: Revoke an account invitation
    question: How do I cancel a customer invitation that was sent by mistake?
  - id: getAccountInvitation
    intent: Get an account invitation
    question: Has a specific customer invitation been accepted yet?
  - id: resendInvitation
    intent: Resend an account invitation
    question: Can I resend an account invitation that the customer never received?
  phrasing_ops: 5
  slug: strivacity-account-invitation-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Account Lifecycle Rule API from Strivacity — 2 operation(s) for account lifecycle rule.
  name: Strivacity Account Lifecycle Rule API
  phrasing_intents:
  - id: listLifecycleRules
    intent: List account lifecycle rules
    question: Which automatic account lifecycle rules run on an identity store?
  - id: createLifecycleRule
    intent: Create an account lifecycle rule
    question: How do I automatically act on accounts that match a filter?
  - id: deleteLifecycleRule
    intent: Delete an account lifecycle rule
    question: How do I remove an account lifecycle rule I no longer want?
  - id: getLifecycleRule
    intent: Get an account lifecycle rule
    question: What filter and actions does a particular lifecycle rule use?
  - id: updateLifecycleRule
    intent: Update an account lifecycle rule
    question: How do I change the filter on an existing lifecycle rule?
  phrasing_ops: 5
  slug: strivacity-account-lifecycle-rule-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Active Telephony Provider Configuration API from Strivacity — 2 operation(s) for active telephony provider configuration.
  name: Strivacity Active Telephony Provider Configuration API
  phrasing_intents:
  - id: readActiveTelephonyProviders
    intent: List the active telephony providers per channel
    question: Which telephony provider is currently active for SMS and voice?
  - id: deactivate
    intent: Deactivate the telephony provider for a channel
    question: How do I turn off the active telephony provider for a channel?
  - id: readActiveTelephonyProvider
    intent: Get the active telephony provider for a channel
    question: Which provider is sending messages on a particular channel?
  - id: activate
    intent: Activate a telephony provider for a channel
    question: How do I switch which telephony provider sends my SMS passcodes?
  phrasing_ops: 4
  slug: strivacity-active-telephony-provider-configuration-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Adaptive Access Policy (Adaptive MFA) API from Strivacity — 5 operation(s) for adaptive access policy (adaptive mfa).
  name: Strivacity Adaptive Access Policy (Adaptive MFA) API
  phrasing_intents:
  - id: getInternalAdaptiveMFA
    intent: Get the admin adaptive access policy
    question: What MFA rules apply to admin console logins?
  - id: updateInternalAdaptiveMFA
    intent: Update the admin adaptive access policy
    question: How do I require MFA for administrators signing in?
  - id: getAdminMFAPolicyLocation
    intent: Search locations for the admin access policy
    question: Which locations match a prefix when building admin MFA location rules?
  - id: getMFAPolicies
    intent: List adaptive access policies
    question: What adaptive access policies exist for my customer applications?
  - id: createAdaptiveMFA
    intent: Create an adaptive access policy
    question: How do I set up a new risk-based MFA policy for customers?
  - id: getMFAPolicyLocation
    intent: Search locations for adaptive access policies
    question: Which locations can I use in a customer adaptive access policy rule?
  - id: deleteAdaptiveMFAById
    intent: Delete an adaptive access policy
    question: Can I delete an adaptive access policy that is still assigned to an application?
  - id: getAdaptiveMFA
    intent: Get an adaptive access policy
    question: Can I see the rules and MFA settings of one adaptive access policy?
  phrasing_ops: 9
  slug: strivacity-adaptive-access-policy-adaptive-mfa-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Admin Account API from Strivacity — 18 operation(s) for admin account.
  name: Strivacity Admin Account API
  phrasing_intents:
  - id: listAccounts
    intent: List admin accounts
    question: Which Strivacity admin accounts have never logged in?
  - id: createAccount
    intent: Create an admin account
    question: How do I add a new administrator to the admin portal?
  - id: deleteAccountById
    intent: Delete an admin account
    question: How do I permanently remove an administrator's account?
  - id: getAccountById
    intent: Get an admin account
    question: How can I look up the details of one specific admin account?
  - id: addAuthenticator
    intent: Add an email or phone authenticator to an admin
    question: How do I register a phone number as an MFA authenticator for an admin?
  - id: deleteAuthenticator
    intent: Remove an authenticator from an admin account
    question: How do I remove an admin's old phone authenticator?
  - id: disableAccount
    intent: Disable an admin account
    question: How do I suspend an administrator without deleting them?
  - id: getPersonalData
    intent: Download an admin account's data
    question: How do I export everything stored about an admin account?
  phrasing_ops: 21
  slug: strivacity-admin-account-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Admin Account Attribute API from Strivacity — 1 operation(s) for admin account attribute.
  name: Strivacity Admin Account Attribute API
  phrasing_intents:
  - id: getAllAccountAttributes
    intent: List admin account attributes
    question: Which attributes are defined on admin accounts?
  phrasing_ops: 1
  slug: strivacity-admin-account-attribute-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Admin Account Event API from Strivacity — 5 operation(s) for admin account event.
  name: Strivacity Admin Account Event API
  phrasing_intents:
  - id: getAccountEvents
    intent: List admin account events
    question: What did my administrators do in the admin console recently?
  - id: getAccountEventById
    intent: Get an admin account event
    question: What happened in a particular admin account event?
  - id: getDescriptor
    intent: List admin event type descriptors
    question: What event types can appear in the admin event log?
  - id: getNotificationEvents
    intent: List admin notification events
    question: Did my admins receive their notification emails?
  - id: getNotificationEventById
    intent: Get an admin notification event
    question: What was the outcome of one notification sent to an admin?
  phrasing_ops: 5
  slug: strivacity-admin-account-event-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Admin Account Invitation API from Strivacity — 3 operation(s) for admin account invitation.
  name: Strivacity Admin Account Invitation API
  phrasing_intents:
  - id: getAccountInvitations
    intent: List admin account invitations
    question: Which administrator invitations are still waiting to be accepted?
  - id: createInvitation
    intent: Invite a new administrator
    question: How do I invite a new administrator to the admin console?
  - id: deleteAccountInvitation
    intent: Revoke an admin account invitation
    question: How do I withdraw an invitation sent to a would-be administrator?
  - id: getAccountInvitation
    intent: Get an admin account invitation
    question: Has a particular admin invitation been accepted?
  - id: resendInvitation
    intent: Resend an admin account invitation
    question: Can I send an admin invitation email again?
  phrasing_ops: 5
  slug: strivacity-admin-account-invitation-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Admin API Security Policy API from Strivacity — 3 operation(s) for admin api security policy.
  name: Strivacity Admin API Security Policy API
  phrasing_intents:
  - id: getAdminApiAccessPolicy
    intent: Get the admin API security policy
    question: What security policy governs access to the admin API?
  - id: createApplicationAssignment
    intent: Grant a client access to the admin API
    question: How do I give a machine client scoped access to the admin API?
  - id: deleteAdminApplicationAssignmentFromApiAccessPolicy
    intent: Revoke a client's admin API access
    question: How do I cut off a client's access to the admin API?
  - id: getAdminApiAccessPolicyByClientId
    intent: Get a client's admin API assignment
    question: Which admin API scopes does a particular client have?
  - id: updateApplicationAssignment
    intent: Change a client's admin API scopes
    question: How do I add or remove admin API scopes for an existing client?
  phrasing_ops: 5
  slug: strivacity-admin-api-security-policy-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Admin Claim API from Strivacity — 2 operation(s) for admin claim.
  name: Strivacity Admin Claim API
  phrasing_intents:
  - id: getAvailableNativeClaims
    intent: List unassigned admin native claims
    question: Which native claims are still free to map to an admin attribute?
  - id: getNativeClaimMappings
    intent: List admin native claim mappings
    question: How are native claims mapped to admin account attributes?
  phrasing_ops: 2
  slug: strivacity-admin-claim-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Admin External Login Mapping API from Strivacity — 3 operation(s) for admin external login mapping.
  name: Strivacity Admin External Login Mapping API
  phrasing_intents:
  - id: getNotAssignedNativeClaims
    intent: List unmapped native claims for an admin provider
    question: Which native claims are still free to map from an admin external login provider?
  - id: getEnterpriseLoginMappings
    intent: List claim mappings for an admin login provider
    question: How are claims from an admin external login provider mapped to native claims?
  - id: createEnterpriseLoginMapping
    intent: Create a claim mapping for an admin login provider
    question: How do I map a claim from an admin identity provider to a native claim?
  - id: delete
    intent: Delete a claim mapping for an admin login provider
    question: How do I remove a claim mapping from an admin external login provider?
  - id: getEnterpriseLoginMapping
    intent: Get a claim mapping for an admin login provider
    question: What source path does one admin login provider claim mapping read from?
  - id: updateGenericOIDCMapping
    intent: Update a claim mapping for an admin login provider
    question: Can I disable one claim mapping on an admin login provider?
  phrasing_ops: 6
  slug: strivacity-admin-external-login-mapping-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Admin External Login Provider API from Strivacity — 2 operation(s) for admin external login provider.
  name: Strivacity Admin External Login Provider API
  phrasing_intents:
  - id: getExternalLoginProviders
    intent: List admin external login providers
    question: Which external identity providers can admins sign in with?
  - id: createExternalLoginProvider
    intent: Add an admin external login provider
    question: How do I let administrators sign in through our corporate IdP?
  - id: deleteExternalLoginProvider
    intent: Delete an admin external login provider
    question: How do I stop admins from logging in via an external IdP?
  - id: getExternalLoginProvider
    intent: Get an admin external login provider
    question: How is a specific admin sign-in provider configured?
  - id: updateExternalLoginProvider
    intent: Update an admin external login provider
    question: How do I change settings of the IdP my admins log in with?
  phrasing_ops: 5
  slug: strivacity-admin-external-login-provider-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Admin Notification Preference Descriptor API from Strivacity — 1 operation(s) for admin notification preference descriptor.
  name: Strivacity Admin Notification Preference Descriptor API
  phrasing_intents:
  - id: getNotificationPreferencesDescriptor
    intent: List admin notification preference descriptors
    question: What notification preferences can administrators choose from?
  phrasing_ops: 1
  slug: strivacity-admin-notification-preference-descriptor-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Admin Principal API from Strivacity — 1 operation(s) for admin principal.
  name: Strivacity Admin Principal API
  phrasing_intents:
  - id: adminPrincipal
    intent: Get the signed-in admin's information
    question: Which admin account is my API token acting as?
  - id: updateAdminPrincipal
    intent: Save my admin console UI settings
    question: How do I save my personal admin console UI preferences?
  phrasing_ops: 2
  slug: strivacity-admin-principal-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Admin Role API from Strivacity — 3 operation(s) for admin role.
  name: Strivacity Admin Role API
  phrasing_intents:
  - id: list
    intent: List admin roles
    question: Which admin roles are defined for the admin portal?
  - id: create
    intent: Create an admin role
    question: How do I make a custom admin role with limited permissions?
  - id: getAllScopes
    intent: List scopes available to admin roles
    question: What permission scopes can be granted to an admin role?
  - id: delete_2
    intent: Delete an admin role
    question: How do I remove a custom admin role?
  - id: get_1
    intent: Get an admin role
    question: How do I see which scopes a particular admin role grants?
  - id: update_1
    intent: Update an admin role
    question: How do I add a scope to an existing admin role?
  phrasing_ops: 6
  slug: strivacity-admin-role-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Admin Role Assignee API from Strivacity — 2 operation(s) for admin role assignee.
  name: Strivacity Admin Role Assignee API
  phrasing_intents:
  - id: listRoleAssignees
    intent: List admin accounts holding a role
    question: Which administrators have been given a particular role?
  - id: assignRole
    intent: Assign an admin account to a role
    question: How do I add an administrator to a specific role?
  - id: removeRole
    intent: Remove an admin account from a role
    question: How do I take a role away from an administrator?
  phrasing_ops: 3
  slug: strivacity-admin-role-assignee-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The API Security Policy API from Strivacity — 4 operation(s) for api security policy.
  name: Strivacity API Security Policy API
  phrasing_intents:
  - id: listApiAccessPolicies
    intent: List API security policies
    question: Which API security policies are configured in my instance?
  - id: createApiAccessPolicy
    intent: Create an API security policy
    question: How do I protect my API with a new security policy and audience?
  - id: deleteApiAccessPolicy
    intent: Delete an API security policy
    question: How do I remove an API security policy I no longer use?
  - id: getApiAccessPolicy
    intent: Get an API security policy
    question: What audience and settings does a given API security policy use?
  - id: updateApiAccessPolicy
    intent: Update an API security policy
    question: How do I change the audience or name of an API security policy?
  - id: createApplicationAssignment
    intent: Assign a client to an API security policy
    question: How do I let a client call an API protected by a security policy?
  - id: deleteApplicationAssignmentFromApiAccessPolicy
    intent: Unassign a client from an API security policy
    question: How do I revoke a client's access to an API security policy?
  - id: getApiAccessPolicyAssignmentByClientId
    intent: Get a client's API security policy assignment
    question: Which scopes does a client have on an API security policy?
  phrasing_ops: 9
  slug: strivacity-api-security-policy-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The API Security Policy Scope API from Strivacity — 2 operation(s) for api security policy scope.
  name: Strivacity API Security Policy Scope API
  phrasing_intents:
  - id: createScope
    intent: Add a scope to an API security policy
    question: How do I define a new scope for an API I'm protecting?
  - id: deleteScope
    intent: Delete an API security policy scope
    question: How do I remove a scope from an API security policy?
  - id: getScope
    intent: Get an API security policy scope
    question: What is a particular scope on my API security policy?
  - id: updateScope
    intent: Rename an API security policy scope
    question: How do I rename a scope on an API security policy?
  phrasing_ops: 4
  slug: strivacity-api-security-policy-scope-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Application API from Strivacity — 2 operation(s) for application.
  name: Strivacity Application API
  phrasing_intents:
  - id: getAllApplicationConfigs
    intent: List applications
    question: What applications are configured in my Strivacity instance?
  - id: createApplicationConfig
    intent: Create an application
    question: How do I register a new application with its identity store and login providers?
  - id: deleteApplicationConfig
    intent: Delete an application
    question: How do I delete an application I no longer need?
  - id: getApplicationConfig
    intent: Get an application
    question: Can I view the full configuration of one application?
  - id: updateApplicationConfig
    intent: Update an application
    question: Can I change an application's type after it's created?
  phrasing_ops: 5
  slug: strivacity-application-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Application Client API from Strivacity — 6 operation(s) for application client.
  name: Strivacity Application Client API
  phrasing_intents:
  - id: getAllClients
    intent: List an application's clients
    question: What OAuth or SAML clients are configured under an application?
  - id: createClient
    intent: Create an application client
    question: How do I add a new client to an existing application?
  - id: deleteApplicationClient
    intent: Delete an application client
    question: How do I remove a client from an application?
  - id: getClient
    intent: Get an application client
    question: Can I view the configuration of one specific application client?
  - id: updateClient
    intent: Update an application client
    question: Can I change the name or login URL of a self-service portal client?
  - id: getTokenExchangeClaimMappingLogs
    intent: List token exchange claim mapping logs
    question: Can I see logs from a client's token exchange claim mapping function?
  - id: getTokenExchangeEventHookLogById
    intent: Get a token exchange claim mapping log
    question: How do I open a single token exchange claim mapping log entry?
  - id: getSaml2MetadataDescriptor
    intent: Get SAML2 metadata for a client
    question: Where can I download the SAML2 metadata for an application client?
  phrasing_ops: 9
  slug: strivacity-application-client-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Application Variant API from Strivacity — 3 operation(s) for application variant.
  name: Strivacity Application Variant API
  phrasing_intents:
  - id: applicationVariants
    intent: List variants across all applications
    question: What A/B testing variants exist across all my applications?
  - id: listVariants
    intent: List an application's A/B testing variants
    question: Which A/B testing variants does one application have?
  - id: createVariant
    intent: Create an A/B testing variant
    question: Can I A/B test different policies or consents for part of an application's users?
  - id: reorderVariants
    intent: Reorder an application's variants
    question: How do I change the priority order of an application's variants?
  - id: deleteVariant
    intent: Delete an A/B testing variant
    question: How do I remove an A/B test variant from an application?
  - id: getVariant
    intent: Get an A/B testing variant
    question: What overrides does a particular application variant apply?
  - id: updateVariant
    intent: Update an A/B testing variant
    question: Can I disable an A/B test variant without deleting it?
  phrasing_ops: 7
  slug: strivacity-application-variant-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Audit entry API from Strivacity — 2 operation(s) for audit entry.
  name: Strivacity Audit entry API
  phrasing_intents:
  - id: list_6
    intent: List audit log entries
    question: Who changed configuration in my instance and when?
  - id: get_6
    intent: Get an audit log entry
    question: What exactly changed in one audit log entry?
  phrasing_ops: 2
  slug: strivacity-audit-entry-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Authenticating to the API API from Strivacity — 1 operation(s) for authenticating to the api.
  name: Strivacity Authenticating to the API
  phrasing_intents:
  - id: tokenpost
    intent: Get an access token for the API
    question: How do I authenticate to the Strivacity admin API?
  phrasing_ops: 1
  slug: strivacity-authenticating-to-the-api-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Authenticator management API from Strivacity — 2 operation(s) for authenticator management.
  name: Strivacity Authenticator management API
  phrasing_intents:
  - id: addAuthenticatorRequest
    intent: Enroll an authenticator on my account
    question: How can a signed-in user add a new authenticator to their own account?
  - id: removeAuthenticatorRequest
    intent: Remove an authenticator from my account
    question: How does a user remove an authenticator from their account?
  - id: updateAuthenticator
    intent: Update an authenticator's methods
    question: Can I change which methods an existing authenticator uses, like SMS or voice?
  phrasing_ops: 3
  slug: strivacity-authenticator-management-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Available Role Scope API from Strivacity — 1 operation(s) for available role scope.
  name: Strivacity Available Role Scope API
  phrasing_intents:
  - id: getScopes
    intent: List scopes available to roles
    question: Which scopes can I grant when defining a role?
  phrasing_ops: 1
  slug: strivacity-available-role-scope-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Branding Policy API from Strivacity — 3 operation(s) for branding policy.
  name: Strivacity Branding Policy API
  phrasing_intents:
  - id: getInternalBrand
    intent: Get the admin portal branding
    question: What logo and colors does the admin console currently use?
  - id: updateInternalBrand
    intent: Update the admin portal branding
    question: How do I put my company logo on the admin console?
  - id: getBrands
    intent: List customer branding policies
    question: Which branding policies exist for my customer login pages?
  - id: createBrand
    intent: Create a customer branding policy
    question: How do I brand the customer login pages for a new product?
  - id: deleteBrandById
    intent: Delete a customer branding policy
    question: How do I remove a branding policy I no longer need?
  - id: getBrand
    intent: Get a customer branding policy
    question: How do I view the full settings of one branding policy?
  - id: updateBrand
    intent: Update a customer branding policy
    question: How do I change the privacy policy link on an existing login brand?
  phrasing_ops: 7
  slug: strivacity-branding-policy-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Bridge Policy API from Strivacity — 2 operation(s) for bridge policy.
  name: Strivacity Bridge Policy API
  phrasing_intents:
  - id: list_1
    intent: List bridge policies for an application client
    question: Which bridge policies proxy traffic for an application client?
  - id: create_2
    intent: Create a bridge policy to an upstream service
    question: How do I route an application client's API calls to my upstream URLs?
  - id: delete
    intent: Delete a bridge policy
    question: How do I remove a bridge policy from an application client?
  - id: get
    intent: Get a bridge policy
    question: Which upstream URLs does a specific bridge policy forward to?
  - id: update
    intent: Update a bridge policy
    question: How do I change the upstream URLs of an existing bridge policy?
  phrasing_ops: 5
  slug: strivacity-bridge-policy-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Bridge Policy Resource API from Strivacity — 2 operation(s) for bridge policy resource.
  name: Strivacity Bridge Policy Resource API
  phrasing_intents:
  - id: list
    intent: List bridge policy resources
    question: Which path patterns are protected by a bridge policy on my client?
  - id: create
    intent: Add a resource to a bridge policy
    question: How do I protect a new path pattern behind a bridge policy?
  - id: reOrder
    intent: Reorder bridge policy resources
    question: How do I change the evaluation order of bridge policy resources?
  - id: delete_1
    intent: Delete a bridge policy resource
    question: How do I stop protecting a path in a bridge policy?
  - id: get_1
    intent: Get a bridge policy resource
    question: What methods and authentication does one bridge resource require?
  - id: update_1
    intent: Update a bridge policy resource
    question: How do I change the path pattern of a bridge resource?
  phrasing_ops: 6
  slug: strivacity-bridge-policy-resource-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Bulk Operation API from Strivacity — 3 operation(s) for bulk operation.
  name: Strivacity Bulk Operation API
  phrasing_intents:
  - id: isRunning
    intent: Check whether a bulk operation is running
    question: Is there a bulk operation in progress right now?
  - id: createJob
    intent: Start a bulk operation job
    question: How do I run a bulk import or update across many accounts?
  - id: getJobStatus
    intent: Get a bulk job's status
    question: How far along is my bulk operation job?
  - id: errors
    intent: List errors from a bulk job
    question: Which records failed in my bulk operation?
  phrasing_ops: 4
  slug: strivacity-bulk-operation-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Claim API from Strivacity — 2 operation(s) for claim.
  name: Strivacity Claim API
  phrasing_intents:
  - id: getClaims
    intent: List claims in a dialect
    question: Which claims are defined in a token dialect?
  - id: createClaim
    intent: Add a claim to a dialect
    question: How do I add a custom claim to tokens through a dialect?
  - id: deleteClaimById
    intent: Delete a dialect claim
    question: How do I remove a claim from a dialect?
  - id: getClaim
    intent: Get a dialect claim
    question: What native claim does a dialect claim map to?
  - id: updateClaim
    intent: Update a dialect claim
    question: How do I rename a claim or change its native claim mapping?
  phrasing_ops: 5
  slug: strivacity-claim-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Consent API from Strivacity — 5 operation(s) for consent.
  name: Strivacity Consent API
  phrasing_intents:
  - id: getAllConsents
    intent: List configured consents
    question: Which consents have we configured for customers to accept?
  - id: createConsent
    intent: Create a consent
    question: How do I add a new terms or marketing consent?
  - id: getConsentById
    intent: Get a consent definition
    question: What text and version does a consent definition have?
  - id: updateConsent
    intent: Update a consent definition
    question: How do I publish a new version of a consent's wording?
  - id: getConsents
    intent: List my own consents
    question: Which consents have I accepted on my account?
  - id: optInConsent
    intent: Accept a consent as the signed-in user
    question: How does a customer opt in to a consent themselves?
  - id: optOutConsent
    intent: Revoke a consent as the signed-in user
    question: How does a customer withdraw a consent they gave earlier?
  phrasing_ops: 7
  slug: strivacity-consent-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Custom Adaptive MFA API from Strivacity — 2 operation(s) for custom adaptive mfa.
  name: Strivacity Custom Adaptive MFA API
  phrasing_intents:
  - id: list_2
    intent: List custom MFAs
    question: What custom MFA methods have been built for my instance?
  - id: create_2
    intent: Create a custom MFA
    question: How do I add my own MFA method with custom code?
  - id: deleteAdaptiveMFAById
    intent: Delete a custom MFA
    question: Why can't I delete a custom MFA that a policy still uses?
  - id: getCustomMfa
    intent: Get a custom MFA
    question: Can I see the code and methods of one custom MFA?
  - id: updateCustomMFA
    intent: Update a custom MFA
    question: How do I change the code of an existing custom MFA?
  phrasing_ops: 5
  slug: strivacity-custom-adaptive-mfa-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Dialect API from Strivacity — 2 operation(s) for dialect.
  name: Strivacity Dialect API
  phrasing_intents:
  - id: getDialects
    intent: List claim dialects
    question: Which claim dialects are defined in my tenant?
  - id: createDialect
    intent: Create a claim dialect
    question: How do I define a new claim dialect with its own URI?
  - id: deleteDialectById
    intent: Delete a claim dialect
    question: How do I remove a claim dialect I no longer use?
  - id: getDialect
    intent: Get a claim dialect
    question: How do I view one claim dialect's URI and description?
  - id: updateDialect
    intent: Update a claim dialect
    question: How do I change the URI of an existing claim dialect?
  phrasing_ops: 5
  slug: strivacity-dialect-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Email Provider Configuration API from Strivacity — 3 operation(s) for email provider configuration.
  name: Strivacity Email Provider Configuration API
  phrasing_intents:
  - id: getActiveProviderId
    intent: Get the active email service provider
    question: Which email service provider is currently sending our emails?
  - id: setActiveProviderId
    intent: Set the active email service provider
    question: How do I switch the instance to a different email service provider?
  - id: readEmailProviders
    intent: List email service providers
    question: What email service providers are configured on my instance?
  - id: createEmailProviders
    intent: Create an email service provider
    question: How do I configure a new email service provider for sending notifications?
  - id: deleteEmailProvider
    intent: Delete an email service provider
    question: Can I delete an email service provider I no longer use?
  - id: readEmailProvider
    intent: Get an email service provider
    question: Can I view the settings of one configured email provider?
  - id: updateEmailProvider
    intent: Update an email service provider
    question: How do I change the credentials of an existing email provider?
  phrasing_ops: 7
  slug: strivacity-email-provider-configuration-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Enterprise Login Claim Mapping API from Strivacity — 3 operation(s) for enterprise login claim mapping.
  name: Strivacity Enterprise Login Claim Mapping API
  phrasing_intents:
  - id: getNotAssignedNativeClaims_1
    intent: List unmapped native claims for an enterprise provider
    question: Which native claims haven't been mapped yet for an enterprise login provider?
  - id: getEnterpriseLoginMappings
    intent: List claim mappings for an enterprise provider
    question: How are claims from an enterprise identity provider mapped into customer accounts?
  - id: createEnterpriseLoginMapping
    intent: Create a claim mapping for an enterprise provider
    question: How do I map an attribute from an enterprise SSO provider to a native claim?
  - id: delete_4
    intent: Delete a claim mapping for an enterprise provider
    question: How do I delete a claim mapping from an enterprise SSO provider?
  - id: getEnterpriseLoginMapping
    intent: Get a claim mapping for an enterprise provider
    question: What does one enterprise login provider claim mapping look like?
  - id: updateGenericOIDCMapping
    intent: Update a claim mapping for an enterprise provider
    question: Can I turn off a single enterprise login claim mapping?
  phrasing_ops: 6
  slug: strivacity-enterprise-login-claim-mapping-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Enterprise Login Provider API from Strivacity — 2 operation(s) for enterprise login provider.
  name: Strivacity Enterprise Login Provider API
  phrasing_intents:
  - id: getEnterpriseLoginProviders
    intent: List enterprise login providers
    question: Which enterprise SSO providers are configured for customers?
  - id: createEnterpriseLoginProvider
    intent: Add an enterprise login provider
    question: How do I connect a business customer's SAML or OIDC IdP?
  - id: deleteEnterpriseLoginProvider
    intent: Delete an enterprise login provider
    question: How do I remove an enterprise SSO connection?
  - id: getEnterpriseLoginProvider
    intent: Get an enterprise login provider
    question: How is a specific enterprise SSO connection configured?
  - id: updateEnterpriseLoginProvider
    intent: Update an enterprise login provider
    question: How do I update certificates or settings on an enterprise SSO connection?
  phrasing_ops: 5
  slug: strivacity-enterprise-login-provider-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Event Streaming API from Strivacity — 3 operation(s) for event streaming.
  name: Strivacity Event Streaming API
  phrasing_intents:
  - id: list_4
    intent: List event streaming configurations
    question: Where are my tenant's events currently being streamed to?
  - id: create_6
    intent: Set up a new event streaming destination
    question: How do I start streaming identity events to my SIEM?
  - id: delete_7
    intent: Delete an event streaming configuration
    question: How do I stop streaming events to a destination for good?
  - id: getById
    intent: Get an event streaming configuration
    question: How do I see the settings of one event streaming configuration?
  - id: update_5
    intent: Update an event streaming configuration
    question: How do I change where an existing event stream delivers events?
  - id: sendTestEvent
    intent: Send a test event through an event stream
    question: How can I check that my event streaming destination actually receives events?
  phrasing_ops: 6
  slug: strivacity-event-streaming-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Group API from Strivacity — 2 operation(s) for group.
  name: Strivacity Group API
  phrasing_intents:
  - id: getGroups
    intent: List groups in an identity store
    question: Which groups exist in an identity store?
  - id: createGroup
    intent: Create a group
    question: How do I create a new group of accounts in an identity store?
  - id: deleteGroup
    intent: Delete a group
    question: Why can't I delete a group that still has members?
  - id: getGroup
    intent: Get a group
    question: How do I look up a single group's details?
  - id: updateGroup
    intent: Update a group
    question: How do I rename an existing group?
  phrasing_ops: 5
  slug: strivacity-group-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Group API Security Policy Assignment API from Strivacity — 2 operation(s) for group api security policy assignment.
  name: Strivacity Group API Security Policy Assignment API
  phrasing_intents:
  - id: listGroupApiAccessPolicyAssignments
    intent: List a group's API security policy assignments
    question: Which API security policies is a group assigned to?
  - id: createGroupApiAccessPolicyAssignment
    intent: Assign an API security policy to a group
    question: How do I give a group access to an API with specific scopes?
  - id: deleteGroupApiAccessPolicyAssignment
    intent: Remove an API security policy from a group
    question: How do I take API access away from a group?
  - id: getGroupApiAccessPolicyAssignment
    intent: Get a group's API security policy assignment
    question: What scopes does a group have under one specific API security policy?
  - id: updateGroupApiAccessPolicyAssignment
    intent: Update a group's assigned API scopes
    question: How do I change the scopes a group has on an API it's already assigned to?
  phrasing_ops: 5
  slug: strivacity-group-api-security-policy-assignment-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Group Member API from Strivacity — 2 operation(s) for group member.
  name: Strivacity Group Member API
  phrasing_intents:
  - id: listGroupMembers
    intent: List members of a group
    question: Who are the members of a particular group?
  - id: addGroup
    intent: Add an account to a group
    question: How do I add a user to a group?
  - id: removeGroup
    intent: Remove an account from a group
    question: How do I take a user out of a group?
  phrasing_ops: 3
  slug: strivacity-group-member-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Identity Store API from Strivacity — 4 operation(s) for identity store.
  name: Strivacity Identity Store API
  phrasing_intents:
  - id: getIdentityStores
    intent: List identity stores
    question: Which identity stores are configured in my tenant?
  - id: createIdentityStore
    intent: Create an identity store
    question: How do I set up a new store to hold customer accounts?
  - id: deleteIdentityStoreByName
    intent: Delete an identity store
    question: Why do I get a conflict when deleting an identity store?
  - id: getIdentityStore
    intent: Get an identity store
    question: How do I see the password policy and hooks of one identity store?
  - id: updateIdentityStore
    intent: Update an identity store
    question: How do I change the password policy on an existing identity store?
  - id: getAvailableNativeClaims
    intent: List native claims available to an identity store
    question: Which native claims can I map attributes to in an identity store?
  - id: getNativeClaimMappings
    intent: List an identity store's native claim mappings
    question: How are attributes currently mapped to native claims in an identity store?
  phrasing_ops: 7
  slug: strivacity-identity-store-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Identity Verification API from Strivacity — 3 operation(s) for identity verification.
  name: Strivacity Identity Verification API
  phrasing_intents:
  - id: getAccountProofing
    intent: List an account's identity verifications
    question: Which identity verifications has a customer account gone through?
  - id: addAccountProofing
    intent: Create an identity verification
    question: How do I start an identity verification for a customer account?
  - id: deleteAccountProofingFailures
    intent: Clear attempts on an identity verification
    question: Can I clear failed attempts so a customer can retry identity verification?
  - id: invalidateAccountProofing
    intent: Invalidate an identity verification
    question: How do I mark a completed identity verification as no longer valid?
  phrasing_ops: 4
  slug: strivacity-identity-verification-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Identity Verification Policy API from Strivacity — 2 operation(s) for identity verification policy.
  name: Strivacity Identity Verification Policy API
  phrasing_intents:
  - id: getAllIdentityProofings
    intent: List identity verification policies
    question: Which identity verification policies have we set up?
  - id: createIdentityProofing
    intent: Create an identity verification policy
    question: How do I set up identity proofing for new customers?
  - id: deleteIdentityProofingById
    intent: Delete an identity verification policy
    question: How do I remove an identity verification policy?
  - id: getIdentityProofingById
    intent: Get an identity verification policy
    question: How is a particular identity verification policy configured?
  - id: updateIdentityProofing
    intent: Update an identity verification policy
    question: How do I change the failure message of an identity verification policy?
  phrasing_ops: 5
  slug: strivacity-identity-verification-policy-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Identity Verification Step API from Strivacity — 2 operation(s) for identity verification step.
  name: Strivacity Identity Verification Step API
  phrasing_intents:
  - id: findAll
    intent: List steps in an identity verification policy
    question: What steps does my identity verification policy run?
  - id: create_1
    intent: Add an identity verification step
    question: How do I add a new step to an identity verification policy?
  - id: reorder
    intent: Reorder identity verification steps
    question: How do I change the order in which verification steps run?
  - id: deleteById
    intent: Delete an identity verification step
    question: How do I remove a step from my identity verification flow?
  - id: findById
    intent: Get an identity verification step
    question: How is a specific verification step configured?
  - id: update_7
    intent: Update an identity verification step
    question: How do I change the settings of a verification step?
  phrasing_ops: 6
  slug: strivacity-identity-verification-step-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: These endpoints are subject to change
  name: Strivacity Inbound Connection [beta] API
  phrasing_intents:
  - id: listInboundConnections
    intent: List an identity store's inbound connections
    question: What inbound connections feed accounts into an identity store?
  - id: createInboundConnection
    intent: Create an inbound connection
    question: How do I set up an inbound connection to sync users into an identity store?
  - id: deleteInboundConnection
    intent: Delete an inbound connection
    question: How do I remove an inbound connection from an identity store?
  - id: getInboundConnection
    intent: Get an inbound connection
    question: Can I look at the configuration of a single inbound connection?
  - id: updateInboundConnection
    intent: Update an inbound connection
    question: Can I pause an inbound connection by disabling it?
  - id: inboundConnectionFullSync
    intent: Force a sync of an inbound connection
    question: Can I force a full sync on an inbound connection right now?
  phrasing_ops: 6
  slug: strivacity-inbound-connection-beta-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Instance Config API from Strivacity — 2 operation(s) for instance config.
  name: Strivacity Instance Config API
  phrasing_intents:
  - id: getInstanceConfig
    intent: Get the instance configuration
    question: What company name and IP allow list are set on my instance?
  - id: updateInstanceConfig
    intent: Update the instance configuration
    question: How do I restrict admin access to an IP allow list?
  - id: getInstanceAddress
    intent: Get the instance addresses
    question: What addresses does my instance use?
  phrasing_ops: 3
  slug: strivacity-instance-config-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Lifecycle Event Hook API from Strivacity — 4 operation(s) for lifecycle event hook.
  name: Strivacity Lifecycle Event Hook API
  phrasing_intents:
  - id: getAllEventHookFunctions
    intent: List lifecycle event hooks
    question: Which lifecycle event hooks are configured in my instance?
  - id: createEventHookFunction
    intent: Create a lifecycle event hook
    question: How do I run custom code when a user registers or logs in?
  - id: deleteEventHookFunction
    intent: Delete a lifecycle event hook
    question: How do I remove an event hook I no longer need?
  - id: getEventHookFunctionById
    intent: Get a lifecycle event hook
    question: What code and settings does a specific event hook have?
  - id: updateEventHookFunction
    intent: Update a lifecycle event hook
    question: How do I change the code of an existing event hook?
  - id: deployEventHookFunction
    intent: Deploy a lifecycle event hook
    question: How do I make my latest event hook code go live?
  - id: getEventHookFunctionStatusById
    intent: Check a lifecycle event hook's status
    question: Has my event hook finished deploying?
  phrasing_ops: 7
  slug: strivacity-lifecycle-event-hook-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Lifecycle Event Hook Descriptor API from Strivacity — 1 operation(s) for lifecycle event hook descriptor.
  name: Strivacity Lifecycle Event Hook Descriptor API
  phrasing_intents:
  - id: getAllEventHooks
    intent: List lifecycle event hook descriptors
    question: What lifecycle event hook types can I attach code to?
  phrasing_ops: 1
  slug: strivacity-lifecycle-event-hook-descriptor-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Lifecycle Event Hook Log API from Strivacity — 2 operation(s) for lifecycle event hook log.
  name: Strivacity Lifecycle Event Hook Log API
  phrasing_intents:
  - id: getEventHookLogs
    intent: List event hook logs
    question: Why did a lifecycle event hook fail for a user, and where are its logs?
  - id: getEventHookLogById
    intent: Get an event hook log
    question: Can I open the full details of one event hook log entry?
  phrasing_ops: 2
  slug: strivacity-lifecycle-event-hook-log-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Lifecycle Event Hook Tryout API from Strivacity — 3 operation(s) for lifecycle event hook tryout.
  name: Strivacity Lifecycle Event Hook Tryout API
  phrasing_intents:
  - id: createFunctionResource
    intent: Create a tryout event hook function
    question: Can I test lifecycle event hook code before deploying it?
  - id: deleteFunctionResource
    intent: Delete a tryout event hook function
    question: How do I clean up a tryout event hook resource when testing is done?
  - id: callFunctionResource
    intent: Run a tryout event hook function
    question: Can I run a tryout event hook function against a sample request?
  phrasing_ops: 3
  slug: strivacity-lifecycle-event-hook-tryout-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Native Claim API from Strivacity — 2 operation(s) for native claim.
  name: Strivacity Native Claim API
  phrasing_intents:
  - id: getAllNativeClaims
    intent: List native claims
    question: What native claims are defined in my instance?
  - id: createNativeClaim
    intent: Create a native claim
    question: How do I define a new native claim for tokens?
  - id: deleteNativeClaim
    intent: Delete a native claim
    question: Why can't I delete a native claim that an account attribute uses?
  - id: getNativeClaim
    intent: Get a native claim
    question: Can I view the details of one native claim?
  - id: updateNativeClaim
    intent: Update a native claim
    question: How do I change the display name of a native claim?
  phrasing_ops: 5
  slug: strivacity-native-claim-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Native Journey API API from Strivacity — 23 operation(s) for native journey api.
  name: Strivacity Native Journey API
  phrasing_intents:
  - id: additionalActions
    intent: Perform an additional action in a login journey
    question: Can a customer in a native login journey trigger forgot-password or forgot-username from the form?
  - id: customerInput
    intent: Submit customer input collected in a journey
    question: How do I post the attributes a customer filled in on the customer input step of a journey?
  - id: externalLoginProvider
    intent: Choose an external login provider in a journey
    question: Can a native journey hand the user off to an external login provider they picked?
  - id: forgottenPasswordEmail
    intent: Send a forgotten password email
    question: Can my custom login screen send a password reset email through the native flow?
  - id: forgottenPasswordPhone
    intent: Start password recovery via phone
    question: Is it possible to recover a password with phone verification instead of email?
  - id: forgottenUsername
    intent: Send a forgotten username reminder
    question: What does a user need to provide to get a forgotten username reminder?
  - id: genericAction
    intent: Submit a generic action in a journey
    question: Can I post a custom action button from a native journey screen?
  - id: genericResult
    intent: Continue a journey from a result screen
    question: How do I move a native flow past a generic result screen?
  phrasing_ops: 23
  slug: strivacity-native-journey-api-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Notification Policy API from Strivacity — 3 operation(s) for notification policy.
  name: Strivacity Notification Policy API
  phrasing_intents:
  - id: getAdminNotificationPolicy
    intent: Get the admin notification policy
    question: What sender address do admin notification emails come from?
  - id: updateAdminNotificationPolicy
    intent: Update the admin notification policy
    question: How do I change the sender of admin notification emails?
  - id: getNotificationPolicies
    intent: List notification policies
    question: Which customer notification policies are defined?
  - id: createNotificationPolicy
    intent: Create a notification policy
    question: How do I create a notification policy with its own sender address?
  - id: deleteNotificationPolicy
    intent: Delete a notification policy
    question: Why can't I delete a notification policy that applications use?
  - id: getNotificationPolicy
    intent: Get a notification policy
    question: What sender does a specific customer notification policy use?
  - id: updateNotificationPolicy
    intent: Update a notification policy
    question: Can I change the sender on an existing customer notification policy?
  phrasing_ops: 7
  slug: strivacity-notification-policy-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Notification Preference Descriptor API from Strivacity — 1 operation(s) for notification preference descriptor.
  name: Strivacity Notification Preference Descriptor API
  phrasing_intents:
  - id: getNotificationPreferencesDescriptor
    intent: List notification preference descriptors
    question: Which notification types can be configured for accounts?
  phrasing_ops: 1
  slug: strivacity-notification-preference-descriptor-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Notification Template API from Strivacity — 8 operation(s) for notification template.
  name: Strivacity Notification Template API
  phrasing_intents:
  - id: updateAdminNotificationTemplateEmail
    intent: Update an admin email notification template
    question: How do I edit the email admins receive for a notification?
  - id: updateAdminNotificationTemplateSMS
    intent: Update an admin SMS notification template
    question: How do I change the text message sent to admins?
  - id: getAdminNotificationTemplateParameters
    intent: List admin notification templates by type
    question: What admin notification templates exist for email?
  - id: getAdminNotificationTemplate
    intent: Get an admin notification template
    question: What does a specific admin notification template currently say?
  - id: updateNotificationTemplateEmail
    intent: Update a customer email template in a policy
    question: How do I customize the email customers receive from a notification policy?
  - id: updateNotificationTemplateSMS
    intent: Update a customer SMS template in a policy
    question: How do I change the SMS text customers get from a notification policy?
  - id: getNotificationTemplateParameters
    intent: List a notification policy's templates by type
    question: Which SMS templates does my notification policy contain?
  - id: getNotificationTemplate
    intent: Get a template from a notification policy
    question: What is the current wording of a customer-facing notification template?
  phrasing_ops: 8
  slug: strivacity-notification-template-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The NPM Dependency API from Strivacity — 2 operation(s) for npm dependency.
  name: Strivacity NPM Dependency API
  phrasing_intents:
  - id: getPackage
    intent: List versions of an NPM package for a hook
    question: Which versions of an NPM package can my event hook depend on?
  - id: getSuggestions
    intent: Search NPM packages for a lifecycle hook
    question: Can I search for NPM packages to add to an event hook by keyword?
  phrasing_ops: 2
  slug: strivacity-npm-dependency-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Organization API from Strivacity — 2 operation(s) for organization.
  name: Strivacity Organization API
  phrasing_intents:
  - id: getOrganizations
    intent: List organizations in an identity store
    question: Which B2B organizations exist in an identity store?
  - id: createOrganization
    intent: Create an organization
    question: How do I onboard a new business customer as an organization?
  - id: deleteOrganization
    intent: Delete an organization
    question: Why can't I delete an organization that still has accounts?
  - id: getOrganization
    intent: Get an organization
    question: How do I view the configuration and routes of one organization?
  - id: updateOrganization
    intent: Update an organization
    question: How do I change the routes of an existing organization?
  phrasing_ops: 5
  slug: strivacity-organization-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Organization Policy API from Strivacity — 2 operation(s) for organization policy.
  name: Strivacity Organization Policy API
  phrasing_intents:
  - id: getOrganizationPolicies
    intent: List an application's organization policies
    question: Which organizations have custom policies on my application?
  - id: createOrganizationPolicy
    intent: Create an organization policy for an app
    question: How do I give one organization its own login providers on an app?
  - id: deleteOrganizationPolicy
    intent: Delete an organization policy from an app
    question: How do I remove an organization's override from an application?
  - id: getOrganizationPolicy
    intent: Get an organization policy for an app
    question: What policies apply to one organization on my application?
  - id: updateOrganizationPolicy
    intent: Update an organization policy for an app
    question: How do I change the login providers an organization uses on an app?
  phrasing_ops: 5
  slug: strivacity-organization-policy-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Outbound Provision API from Strivacity — 6 operation(s) for outbound provision.
  name: Strivacity Outbound Provision API
  phrasing_intents:
  - id: listOutboundProvisions
    intent: List an identity store's outbound provisions
    question: Which outbound provisioning targets are set up for an identity store?
  - id: createOutboundProvision
    intent: Create an outbound provision
    question: How do I push account changes from an identity store to another system?
  - id: deleteOutboundProvision
    intent: Delete an outbound provision
    question: How do I remove a provisioning target from an identity store?
  - id: getOutboundProvision
    intent: Get an outbound provision
    question: How can I view the code and filter of one outbound provision?
  - id: updateOutboundProvision
    intent: Update an outbound provision
    question: How do I change the code or filter of an existing outbound provision?
  - id: getProvisionFunctionLogs
    intent: List an outbound provision's function logs
    question: Why did provisioning fail for a particular account?
  - id: getProvisionFunctionLog
    intent: Get one provision function log entry
    question: How do I open the full detail of a single provisioning log line?
  - id: getProvisionStatus
    intent: Check an outbound provision's run status
    question: Is my outbound provisioning function currently running or idle?
  phrasing_ops: 9
  slug: strivacity-outbound-provision-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Password Quality Policy API from Strivacity — 2 operation(s) for password quality policy.
  name: Strivacity Password Quality Policy API
  phrasing_intents:
  - id: getAllPasswordPolicies
    intent: List password quality policies
    question: What password quality policies are set up?
  - id: createPasswordPolicy
    intent: Create a password quality policy
    question: How do I enforce password complexity rules for customers?
  - id: deletePasswordPolicy
    intent: Delete a password quality policy
    question: Why can't I delete a password policy that an identity store uses?
  - id: getPasswordPolicy
    intent: Get a password quality policy
    question: What rules does a specific password policy enforce?
  - id: updatePasswordPolicy
    intent: Update a password quality policy
    question: How do I tighten the rules on an existing password policy?
  phrasing_ops: 5
  slug: strivacity-password-quality-policy-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Personal Data API from Strivacity — 2 operation(s) for personal data.
  name: Strivacity Personal Data API
  phrasing_intents:
  - id: getPersonalData
    intent: Download a customer's personal data as admin
    question: How can an admin export all data held about a customer for a GDPR request?
  - id: getMyaccountApiV1MePersonalData
    intent: Download my own personal data
    question: How do I, as a signed-in customer, download the data stored about me?
  phrasing_ops: 2
  slug: strivacity-personal-data-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Plugin Library API from Strivacity — 7 operation(s) for plugin library.
  name: Strivacity Plugin Library API
  phrasing_intents:
  - id: getCategories
    intent: List plugin library categories
    question: What categories are plugins grouped into in the plugin library?
  - id: getSnippets
    intent: List code snippets for an event hook type
    question: Are there ready-made code snippets for a given lifecycle hook type?
  - id: getSnippetCode
    intent: Get the code of an event hook snippet
    question: How do I get the actual source code of a hook snippet?
  - id: getEventHooks
    intent: Browse lifecycle event hook integrations
    question: Which prebuilt integrations exist for lifecycle event hooks?
  - id: getEventHookIntegration
    intent: Get a lifecycle event hook integration
    question: How do I see the details of one event hook integration?
  - id: getJourneys
    intent: Browse journey integrations
    question: Which prebuilt integrations can I use in login journeys?
  - id: getJourneyIntegration
    intent: Get a journey integration
    question: How do I view the details of one journey plugin?
  phrasing_ops: 7
  slug: strivacity-plugin-library-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Policy Tag API from Strivacity — 2 operation(s) for policy tag.
  name: Strivacity Policy Tag API
  phrasing_intents:
  - id: getAllTags
    intent: List policy tags
    question: Which policy tags are available to label my policies?
  - id: createTag
    intent: Create a policy tag
    question: How do I create a colored tag to group related policies?
  - id: deleteTag
    intent: Delete a policy tag
    question: Why can't I delete a policy tag that is still assigned?
  - id: getPolicyTag
    intent: Get a policy tag
    question: How do I look up the color and description of one policy tag?
  - id: updateTag
    intent: Update a policy tag
    question: How do I change the color of an existing policy tag?
  phrasing_ops: 5
  slug: strivacity-policy-tag-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Restricted Password API from Strivacity — 4 operation(s) for restricted password.
  name: Strivacity Restricted Password API
  phrasing_intents:
  - id: list_2
    intent: List banned-password lists in a password policy
    question: Which restricted password word lists are on my password policy?
  - id: create_3
    intent: Upload a banned-password word list
    question: How do I upload a list of words users can't use in passwords?
  - id: getTotalSize
    intent: Check banned-password storage used
    question: How much space do my restricted password lists take in MB?
  - id: delete_2
    intent: Delete a banned-password word list
    question: How do I remove a restricted password list from my policy?
  - id: get_2
    intent: Get a banned-password word list
    question: What is in one restricted password list?
  - id: update_2
    intent: Rename or describe a banned-password list
    question: How do I rename a restricted password word list?
  - id: export_1
    intent: Export a banned-password word list
    question: How do I download a restricted password list I uploaded?
  phrasing_ops: 7
  slug: strivacity-restricted-password-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Role API from Strivacity — 2 operation(s) for role.
  name: Strivacity Role API
  phrasing_intents:
  - id: list_5
    intent: List roles in an identity store
    question: Which roles are defined in my identity store?
  - id: create_7
    intent: Create a role
    question: How do I define a new role with specific scopes?
  - id: delete_8
    intent: Delete a role
    question: How do I remove a role I no longer use?
  - id: get_5
    intent: Get a role
    question: What scopes does a given role grant?
  - id: update_6
    intent: Update a role
    question: How do I change the scopes a role grants?
  phrasing_ops: 5
  slug: strivacity-role-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Self Management API from Strivacity — 9 operation(s) for self management.
  name: Strivacity Self Management API
  phrasing_intents:
  - id: getAvailableAttributes
    intent: List profile attributes I can manage
    question: Which profile attributes am I allowed to edit on my own account?
  - id: updateIdentifierRequest
    intent: Change my email or phone identifier
    question: How do I change the email address I sign in with?
  - id: getMyIdentities
    intent: List my linked identities
    question: Which social or external logins are linked to my account?
  - id: deleteExternalIdentity
    intent: Unlink an external login from my account
    question: How do I disconnect a social login from my account?
  - id: getPrincipal
    intent: Get my account information
    question: How do I fetch the details of the account I'm signed in as?
  - id: getNotificationPreferences
    intent: Get my notification preferences
    question: Which security emails am I currently set to receive?
  - id: updateNotificationPreferences
    intent: Update my notification preferences
    question: How do I turn off emails when my account attributes change?
  - id: getNotificationPreferencesDescriptor
    intent: Describe the available notification options
    question: What notification types and channels can a customer choose from?
  phrasing_ops: 11
  slug: strivacity-self-management-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Self Service Policy API from Strivacity — 2 operation(s) for self service policy.
  name: Strivacity Self Service Policy API
  phrasing_intents:
  - id: getSelfServicePolicies
    intent: List self-service policies
    question: Which self-service policies control what customers can change on their own?
  - id: createSelfServicePolicy
    intent: Create a self-service policy
    question: How do I define what users can manage themselves in their account portal?
  - id: deleteSelfServicePolicyById
    intent: Delete a self-service policy
    question: Why can't I delete a self-service policy that an application uses?
  - id: getSelfServicePolicy
    intent: Get a self-service policy
    question: What options are enabled in a particular self-service policy?
  - id: updateSelfServicePolicy
    intent: Update a self-service policy
    question: How do I change what customers can edit under an existing self-service policy?
  phrasing_ops: 5
  slug: strivacity-self-service-policy-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Simplelogin API from Strivacity — 2 operation(s) for simplelogin.
  name: Strivacity Simplelogin API
  phrasing_intents:
  - id: authenticate-with-identifier-and-password
    intent: Authenticate with identifier and password
    question: How do I sign a user in with identifier and password in a simple login flow?
  - id: token-1
    intent: Request tokens with identifier and password
    question: Can I get an access token and ID token directly with a username and password?
  phrasing_ops: 2
  slug: strivacity-simplelogin-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Social Login Claim Mapping API from Strivacity — 3 operation(s) for social login claim mapping.
  name: Strivacity Social Login Claim Mapping API
  phrasing_intents:
  - id: getNotAssignedNativeClaims
    intent: List native claims not yet mapped for a social login
    question: Which native claims are still free to map for a social login provider?
  - id: getSocialMappings
    intent: List a social login provider's claim mappings
    question: How are fields from a social login mapped into my native claims?
  - id: createSocialMapping
    intent: Map a social login field to a native claim
    question: How do I copy the email from a social login profile into a native claim?
  - id: delete_3
    intent: Delete a social login claim mapping
    question: How do I remove a claim mapping from a social login provider?
  - id: getSocialMapping
    intent: Get one social login claim mapping
    question: How do I view a single claim mapping on a social provider?
  - id: updateSocialMapping
    intent: Update a social login claim mapping
    question: How do I change the source path of an existing social claim mapping?
  phrasing_ops: 6
  slug: strivacity-social-login-claim-mapping-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Social Login Provider API from Strivacity — 2 operation(s) for social login provider.
  name: Strivacity Social Login Provider API
  phrasing_intents:
  - id: getLoginProviders
    intent: List social login providers
    question: Which social sign-in options are configured for my customers?
  - id: createLoginProvider
    intent: Add a social login provider
    question: How do I let customers sign in with a social account?
  - id: deleteLoginProvider
    intent: Delete a social login provider
    question: Why can't I delete a social login that is assigned to an application?
  - id: getLoginProvider
    intent: Get a social login provider
    question: How do I view the configuration of one social login provider?
  - id: updateLoginProvider
    intent: Update a social login provider
    question: How do I change the settings of a social login that already exists?
  phrasing_ops: 5
  slug: strivacity-social-login-provider-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Statistics API from Strivacity — 5 operation(s) for statistics.
  name: Strivacity Statistics API
  phrasing_intents:
  - id: queryActiveAccountsStatistics
    intent: Get active account statistics
    question: How many active accounts did we have each month?
  - id: connectorJobStatistics
    intent: Get connector job statistics
    question: How are my inbound connector jobs performing?
  - id: queryConnectorUptimeStatistics
    intent: Get connector uptime statistics
    question: What was the uptime of my identity store connectors?
  - id: queryConsentAcceptanceStatistics
    intent: Get consent acceptance statistics
    question: What share of users accept our consents?
  - id: queryNamedStatistics
    intent: Query a named statistic
    question: Which statistics can I query by name, such as flow runs or screen time?
  phrasing_ops: 5
  slug: strivacity-statistics-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Tag Based Permission API from Strivacity — 2 operation(s) for tag based permission.
  name: Strivacity Tag Based Permission API
  phrasing_intents:
  - id: list_1
    intent: List an admin role's tag based permissions
    question: Which policy tags can an admin role manage?
  - id: create_1
    intent: Create tag based permissions for an admin role
    question: How do I let an admin role manage only policies with certain tags?
  - id: delete_1
    intent: Delete a tag based permission entry
    question: How do I remove a tag based permission from an admin role?
  - id: get
    intent: Get a tag based permission entry
    question: Can I view one tag based permission entry on an admin role?
  - id: update
    intent: Update a tag based permission entry
    question: How do I change the tags or scopes of an admin role's tag permission?
  phrasing_ops: 5
  slug: strivacity-tag-based-permission-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Telephony Provider Configuration API from Strivacity — 2 operation(s) for telephony provider configuration.
  name: Strivacity Telephony Provider Configuration API
  phrasing_intents:
  - id: readTelephonyProviders
    intent: List telephony service providers
    question: Which SMS and voice telephony providers are configured on my instance?
  - id: createTelephonyProviders
    intent: Add a telephony service provider
    question: How do I connect a new SMS gateway for sending one-time passcodes?
  - id: deleteTelephonyProvider
    intent: Delete a telephony service provider
    question: How do I remove a telephony provider configuration I no longer use?
  - id: readTelephonyProvider
    intent: Get a telephony service provider
    question: How do I view the settings of one telephony provider configuration?
  - id: updateTelephonyProvider
    intent: Update a telephony service provider
    question: How do I change the settings of a telephony provider that already exists?
  phrasing_ops: 5
  slug: strivacity-telephony-provider-configuration-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Translation API from Strivacity — 4 operation(s) for translation.
  name: Strivacity Translation API
  phrasing_intents:
  - id: list_7
    intent: List admin console translations
    question: Which languages have translations in my instance?
  - id: reset
    intent: Reset a language translation to default
    question: How do I undo a translation I imported?
  - id: export
    intent: Export a language translation
    question: How do I download the translation file for a language?
  - id: importTranslation
    intent: Import a language translation
    question: How do I upload my own translated strings for a language?
  - id: disableLanguage
    intent: Disable a language
    question: How do I stop offering a language to users?
  - id: enableLanguage
    intent: Enable a language
    question: How do I make a new language available to users?
  phrasing_ops: 6
  slug: strivacity-translation-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Variables API from Strivacity — 2 operation(s) for variables.
  name: Strivacity Variables API
  phrasing_intents:
  - id: getAll
    intent: List instance variables
    question: Which variables are defined in my instance?
  - id: create_5
    intent: Create an instance variable
    question: How do I store a reusable value or secret for my hooks?
  - id: delete_6
    intent: Delete an instance variable
    question: How do I remove a variable I no longer need?
  - id: get_4
    intent: Get an instance variable
    question: What value does a particular variable hold?
  - id: update_4
    intent: Update an instance variable
    question: How do I change the value of a variable?
  phrasing_ops: 5
  slug: strivacity-variables-api
- baseURL: https://{tenant}.strivacity.com/admin/api/v1
  baseurl_source: declared
  description: The Web Analytics API from Strivacity — 2 operation(s) for web analytics.
  name: Strivacity Web Analytics API
  phrasing_intents:
  - id: list_3
    intent: List web analytics integrations
    question: Which web analytics integrations are connected to my instance?
  - id: create_4
    intent: Create a web analytics integration
    question: How do I connect a web analytics tool to track login pages?
  - id: delete_5
    intent: Delete a web analytics integration
    question: How do I disconnect a web analytics integration completely?
  - id: get_3
    intent: Get a web analytics integration
    question: Can I view the settings of one web analytics integration?
  - id: update_3
    intent: Update a web analytics integration
    question: How do I rotate the API key of a web analytics integration?
  phrasing_ops: 5
  slug: strivacity-web-analytics-api
artifact_total: 99
asyncapis:
- description: ''
  name: Strivacity Events
  slug: strivacity-events
common:
- group: other
  href: https://artifacts.apis.io/strivacity/capabilities/strivacity-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/strivacity-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/strivacity/overlays/strivacity-admin-portal-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/strivacity-admin-portal-overlay.yaml
- group: other
  href: https://artifacts.apis.io/strivacity/overlays/strivacity-admin-management-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/strivacity-admin-management-overlay.yaml
- group: other
  href: https://artifacts.apis.io/strivacity/overlays/strivacity-myaccount-portal-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/strivacity-myaccount-portal-overlay.yaml
- group: other
  href: https://artifacts.apis.io/strivacity/overlays/strivacity-native-journey-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/strivacity-native-journey-overlay.yaml
- group: other
  href: https://artifacts.apis.io/strivacity/overlays/strivacity-simple-authentication-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/strivacity-simple-authentication-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.strivacity.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.strivacity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.strivacity.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.strivacity.com/reference/getting-started-with-the-admin-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.strivacity.com/reference/getting-started-1
- group: operate
  title: ''
  type: Support
  url: https://support.strivacity.com/
- group: company
  title: ''
  type: Blog
  url: https://www.strivacity.com/learn-support/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/strivacity
- group: commercial
  title: ''
  type: Pricing
  url: https://www.strivacity.com/products/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.strivacity.com/free-trial
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.strivacity.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.strivacity.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.strivacity.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.strivacity.com/docs/release-support-matrix
- group: auth
  title: ''
  type: Security
  url: https://www.strivacity.com/report-a-security-issue
- group: auth
  title: ''
  type: Compliance
  url: https://security.strivacity.com
- group: auth
  href: https://artifacts.apis.io/strivacity/security/strivacity-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/strivacity-trust-center.yml
- group: operate
  href: https://artifacts.apis.io/strivacity/changelog/strivacity-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/strivacity-changelog.yml
- group: agent
  href: https://artifacts.apis.io/strivacity/llms/strivacity-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/strivacity-llms.txt
- group: agent
  href: https://artifacts.apis.io/strivacity/well-known/strivacity-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/strivacity-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.strivacity.com/.well-known/api-catalog
- group: build
  href: https://artifacts.apis.io/strivacity/packages/strivacity-packages.yml
  title: ''
  type: Packages
  url: packages/strivacity-packages.yml
- group: build
  href: https://artifacts.apis.io/strivacity/packages/strivacity-packages.yml
  title: ''
  type: SDKs
  url: packages/strivacity-packages.yml
- group: auth
  href: https://artifacts.apis.io/strivacity/authentication/strivacity-authentication.yml
  title: ''
  type: Authentication
  url: authentication/strivacity-authentication.yml
- group: auth
  href: https://artifacts.apis.io/strivacity/scopes/strivacity-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/strivacity-scopes.yml
- group: design
  href: https://artifacts.apis.io/strivacity/conventions/strivacity-conventions.yml
  title: ''
  type: Conventions
  url: conventions/strivacity-conventions.yml
- group: design
  href: https://artifacts.apis.io/strivacity/errors/strivacity-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/strivacity-problem-types.yml
- group: design
  href: https://artifacts.apis.io/strivacity/lifecycle/strivacity-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/strivacity-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/strivacity/data-model/strivacity-data-model.yml
  title: ''
  type: DataModel
  url: data-model/strivacity-data-model.yml
- group: design
  href: https://artifacts.apis.io/strivacity/conformance/strivacity-conformance.yml
  title: ''
  type: Conformance
  url: conformance/strivacity-conformance.yml
- group: auth
  href: https://artifacts.apis.io/strivacity/security/strivacity-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/strivacity-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/strivacity/security/strivacity-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/strivacity-vulnerability-disclosure.yml
- group: start
  href: https://artifacts.apis.io/strivacity/sandbox/strivacity-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/strivacity-sandbox.yml
- group: design
  href: https://artifacts.apis.io/strivacity/components/strivacity-components.yml
  title: ''
  type: Components
  url: components/strivacity-components.yml
- group: design
  href: https://artifacts.apis.io/strivacity/asyncapi/strivacity-events.yml
  title: ''
  type: Webhooks
  url: asyncapi/strivacity-events.yml
- group: agent
  href: https://artifacts.apis.io/strivacity/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/strivacity/rate-limits/strivacity-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/strivacity-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/strivacity/plans/strivacity-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/strivacity-plans-pricing.yml
created: '2026-08-29'
description: 'Strivacity is a customer identity and access management (CIAM) vendor that runs a single-tenant, dedicated-cloud identity platform for consumer, partner, B2B and — since its Agentic AI release — AI-agent identities. The product covers registration and self-service, adaptive multi-factor authentication, passkeys and FIDO2, social and enterprise federation, consent management, identity verification, fraud detection, delegated administration and identity orchestration, and it exposes all of it through published REST APIs: an Admin API for configuring and operating an instance, an Admin Management API for the admin plane itself, a MyAccount API for end-customer self-service, a Journey Flow (Native Journey) API for rendering login and registration natively, and a Simple Authentication API. Strivacity also acts as the OAuth 2.1 authorization server in front of a customer''s own MCP servers and APIs, issuing audience-restricted, consent-gated tokens to AI agents.'
finops:
- has_sources: true
  method: derived
  name: Strivacity Finops
  primary_unit: monthly active users (maus)
  service_category: ''
  slug: strivacity-finops
  template: false
image: https://cdn.prod.website-files.com/64259842d8e30c2ec61617ab/642b123a6f2bf0db754b0ab3_webclip.png
layout: provider
modified: '2026-08-29'
name: Strivacity
nav: Providers
network: true
overview: 'Strivacity publishes 82 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Account Attribute API, Account Child Attribute API, and 79 more. Tagged areas include Identity, customer-identity-and-access-management, CIAM, Authentication, and Authorization.


  The Strivacity catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Strivacity''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Strivacity Plans Pricing
  plan_count: 1
  slug: strivacity-plans-pricing
- name: Strivacity Price Estimates
  plan_count: 0
  slug: strivacity-price-estimates
random_paper: 2
rate_limits:
- limit_count: 9
  name: Strivacity Rate Limits
  slug: strivacity-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Strivacity API Rules
  rule_count: 59
  severity_counts:
    error: 31
    hint: 0
    info: 5
    warn: 23
  slug: strivacity-rules
scopes:
- name: Strivacity Scopes
  scope_count: 106
  slug: strivacity-scopes
  summary_line: 106 scopes · client_credentials
score:
  band: exemplar
  composite: 74.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 67.5
    catalog_earned_first_party: 20.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.5
  facets:
    access_clarity: 89.5
    contract_governance: 31.8
    contract_quality: 60.2
    developer_ergonomics: 63.7
    discoverability: 89.3
    operational_transparency: 92.1
  previous_composite: 71.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 4.9
      total: 82
    mcp: derived
    skills: derived
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
    score: 0.0
screenshot: https://apis.io/screenshots/strivacity/strivacity-2026-09-02T161018.png
security:
- kind: authentication
  name: Strivacity Authentication
  slug: strivacity-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Strivacity Domain Security
  slug: strivacity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Strivacity Vulnerability Disclosure
  slug: strivacity-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Strivacity Trust Center
  slug: strivacity-trust-center
  summary_line: SOC 2 Type II, SOC 3, PCI DSS, GDPR, CCPA, FIPS 140-2, VPAT, FIDO Certification
skill_count: 6
skills:
- name: strivacity-account-events-and-streaming
  slug: strivacity-account-events-and-streaming
- name: strivacity-admin-api-access-token
  slug: strivacity-admin-api-access-token
- name: strivacity-consent-and-personal-data
  slug: strivacity-consent-and-personal-data
- name: strivacity-customer-self-service
  slug: strivacity-customer-self-service
- name: strivacity-lifecycle-event-hook
  slug: strivacity-lifecycle-event-hook
- name: strivacity-provision-customer-account
  slug: strivacity-provision-customer-account
slug: strivacity
tags:
- Identity
- customer-identity-and-access-management
- CIAM
- Authentication
- Authorization
- OAuth
- OpenID Connect
- Consent Management
- Multi-Factor Authentication
- Identity Verification
- Fraud Prevention
- Agentic Identity
- Security
website: https://www.strivacity.com/
---
