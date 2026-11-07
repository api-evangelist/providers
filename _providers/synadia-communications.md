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
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The account API from Synadia Communications — 27 operation(s) for account.
  name: Synadia Communications Account API
  phrasing_intents:
  - id: deleteAccount
    intent: Delete a NATS account
    question: Can I permanently delete a NATS account from a system in Synadia Control Plane?
  - id: getAccount
    intent: Look up a NATS account
    question: How do I fetch the details of one Synadia account by its ID?
  - id: updateAccount
    intent: Update a NATS account's settings
    question: How do I rename an account or change its auth type?
  - id: listAccountSkGroup
    intent: List an account's signing key groups
    question: Which signing key groups exist on a NATS account?
  - id: createAccountSkGroup
    intent: Create an account signing key group
    question: How do I add a new signing key group to an account so users get scoped permissions?
  - id: listAlertRules
    intent: List an account's alert rules
    question: What alert rules are configured on my NATS account?
  - id: createAlertRule
    intent: Create an account alert rule
    question: How do I get alerted when a stream or consumer metric crosses a threshold?
  - id: deleteAlertRule
    intent: Delete an account alert rule
    question: Can I remove an alert rule I no longer need from an account?
  phrasing_ops: 45
  slug: synadia-communications-account-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The admin API from Synadia Communications — 1 operation(s) for admin.
  name: Synadia Communications Admin API
  phrasing_intents:
  - id: checkAppAdmin
    intent: Check whether an admin user exists
    question: Has an App Admin user been created on this install yet?
  - id: createAppAdmin
    intent: Create the initial admin user
    question: How do I create the first admin user on a clean install programmatically?
  phrasing_ops: 2
  slug: synadia-communications-admin-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The agent-token API from Synadia Communications — 1 operation(s) for agent-token.
  name: Synadia Communications Agent Token API
  phrasing_intents:
  - id: deleteAgentToken
    intent: Delete an agent token
    question: How do I revoke a token issued to an agent?
  phrasing_ops: 1
  slug: synadia-communications-agent-token-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The alert API from Synadia Communications — 2 operation(s) for alert.
  name: Synadia Communications Alert API
  phrasing_intents:
  - id: getAlert
    intent: Look up an alert
    question: How do I see the details of one fired alert?
  - id: acknowledgeAlert
    intent: Acknowledge an alert
    question: How do I acknowledge an alert so the team knows it's being handled?
  phrasing_ops: 2
  slug: synadia-communications-alert-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The app-service-account API from Synadia Communications — 2 operation(s) for app-service-account.
  name: Synadia Communications App Service Account API
  phrasing_intents:
  - id: deleteAppServiceAccount
    intent: Delete an app service account
    question: Can I delete a service account that automation no longer uses?
  - id: getAppServiceAccount
    intent: Look up an app service account
    question: How do I see the role and resources of one service account?
  - id: updateAppServiceAccount
    intent: Update an app service account
    question: How do I change a service account's role?
  - id: listAppServiceAccountTokens
    intent: List a service account's access tokens
    question: Which access tokens have been issued for a service account?
  - id: createAppServiceAccountToken
    intent: Issue an access token for a service account
    question: How do I mint an API token for a service account?
  phrasing_ops: 5
  slug: synadia-communications-app-service-account-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The app-service-account-tokens API from Synadia Communications — 1 operation(s) for app-service-account-tokens.
  name: Synadia Communications App Service Account Tokens API
  phrasing_intents:
  - id: deleteAppServiceAccountToken
    intent: Revoke a service account token
    question: How do I revoke a service account token that leaked?
  - id: getAppServiceAccountToken
    intent: Look up a service account token
    question: How do I check when a service account token expires?
  - id: updateAppServiceAccountToken
    intent: Update a service account token
    question: Can I extend the expiry on a service account token?
  phrasing_ops: 3
  slug: synadia-communications-app-service-account-tokens-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The app-user API from Synadia Communications — 3 operation(s) for app-user.
  name: Synadia Communications App User API
  phrasing_intents:
  - id: deleteAppUser
    intent: Delete an app user
    question: Can I delete a user from the platform entirely?
  - id: getAppUser
    intent: Get an app user
    question: Can I look up a platform user's profile by ID?
  - id: updateAppUser
    intent: Update an app user or reset their password
    question: Can I force a password reset for a user?
  - id: listAppUserRoles
    intent: List an app user's roles
    question: What roles does a given user hold across teams and systems?
  - id: assignTeamAppUser
    intent: Add an existing user to a team with a role
    question: Can I add an existing user directly to a team without an invitation?
  phrasing_ops: 5
  slug: synadia-communications-app-user-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The auth-callout API from Synadia Communications — 5 operation(s) for auth-callout.
  name: Synadia Communications Auth Callout API
  phrasing_intents:
  - id: deleteAuthCallout
    intent: Remove an auth callout config
    question: Can I turn off auth callout and restore the control account's JWT?
  - id: getAuthCallout
    intent: Get an auth callout config
    question: Which control account does an auth callout config use?
  - id: listAuthCalloutTargetAccounts
    intent: List auth callout target accounts
    question: Which accounts can auth callout place users into?
  - id: addAuthCalloutTargetAccount
    intent: Add a target account to auth callout
    question: How do I let auth callout issue users into another account?
  - id: deleteAuthCalloutTargetAccount
    intent: Remove a target account from auth callout
    question: Can I stop auth callout from issuing users into a particular account?
  - id: listAuthCalloutUsers
    intent: List auth callout service users
    question: Which control-account users are allowed to serve auth callout requests?
  - id: addAuthCalloutUser
    intent: Add a user that serves auth callout
    question: How do I authorize my auth service's NATS user to handle callout requests?
  - id: deleteAuthCalloutUser
    intent: Remove an auth callout user
    question: Can I revoke a control account user's access to auth callout?
  phrasing_ops: 8
  slug: synadia-communications-auth-callout-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The authz API from Synadia Communications — 3 operation(s) for authz.
  name: Synadia Communications Authz API
  phrasing_intents:
  - id: check
    intent: Check my authorization for a resource
    question: Which policies apply to my session for a given service or resource?
  - id: listPolicies
    intent: List authorization policies
    question: What app policies are configured?
  - id: listRoles
    intent: List available roles
    question: Which roles can I assign to users and service accounts?
  phrasing_ops: 3
  slug: synadia-communications-authz-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The component-versions API from Synadia Communications — 1 operation(s) for component-versions.
  name: Synadia Communications Component Versions API
  phrasing_intents:
  - id: getAvailableComponentVersions
    intent: List available component versions
    question: Which platform component versions are available?
  - id: getAvailableComponentVersionsByType
    intent: Find component versions by type and release
    question: Which component versions match a given major and minor release?
  phrasing_ops: 2
  slug: synadia-communications-component-versions-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The Extended KV Entry Operations API from Synadia Communications — 1 operation(s) for extended kv entry operations.
  name: Synadia Communications Extended KV Entry Operations API
  phrasing_intents:
  - id: KvGetEntry
    intent: Read a value from a KV store
    question: How do I read the value stored under a key in a KV bucket?
  - id: KvCreateEntry
    intent: Create a new KV key only if absent
    question: Is there a way to add a key to a KV bucket only when it doesn't already exist?
  - id: KvPutEntry
    intent: Put a value into a KV store
    question: How do I set or overwrite the value of a key in a KV bucket?
  - id: KvDeleteEntry
    intent: Delete a key from a KV store
    question: How do I delete a key from a KV bucket?
  phrasing_ops: 4
  slug: synadia-communications-extended-kv-entry-operations-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The issuance API from Synadia Communications — 1 operation(s) for issuance.
  name: Synadia Communications Issuance API
  phrasing_intents:
  - id: getNatsUserIssuance
    intent: Get the download history of a user issuance
    question: Who downloaded or imported a NATS user's credentials, and when?
  phrasing_ops: 1
  slug: synadia-communications-issuance-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The KV API API from Synadia Communications — 1 operation(s) for kv api.
  name: Synadia Communications KV API
  phrasing_intents:
  - id: SimpleKvGet
    intent: Read a value from a KV bucket
    question: How do I read the value stored under a key?
  - id: SimpleKvCreateEntry
    intent: Create a new key only if absent
    question: Can I add a key so the call fails if it already exists?
  - id: SimpleKvPutEntry
    intent: Put a value in a KV bucket
    question: Can I write a key whether or not it already exists?
  - id: SimpleKvDeleteEntry
    intent: Delete a key from a KV bucket
    question: Can I delete a key and also purge its history?
  phrasing_ops: 4
  slug: synadia-communications-kv-api-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The kv-bucket API from Synadia Communications — 5 operation(s) for kv-bucket.
  name: Synadia Communications Kv Bucket API
  phrasing_intents:
  - id: deleteKvBucket
    intent: Delete a KV bucket
    question: Can I delete a key-value bucket entirely?
  - id: getKvBucket
    intent: Get a KV bucket's info
    question: What's the configuration and size of my key-value bucket?
  - id: updateKvBucket
    intent: Update a KV bucket's configuration
    question: Can I change a KV bucket's history, TTL or size limits after creating it?
  - id: listKvConsumers
    intent: List consumers on a KV bucket
    question: Which consumers are reading from my KV bucket?
  - id: createKvPullConsumer
    intent: Create a pull consumer on a KV bucket
    question: Can I create a pull consumer that fetches changes from a KV bucket in batches?
  - id: createKvPushConsumer
    intent: Create a push consumer on a KV bucket
    question: Can KV bucket updates be pushed to a delivery subject automatically?
  - id: purgeKvBucket
    intent: Purge all entries from a KV bucket
    question: Can I wipe every key from a KV bucket but keep the bucket?
  phrasing_ops: 7
  slug: synadia-communications-kv-bucket-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The KV Management API API from Synadia Communications — 5 operation(s) for kv management api.
  name: Synadia Communications KV Management API
  phrasing_intents:
  - id: ListKvStores
    intent: List all key-value stores
    question: What key-value stores exist on the NATS server?
  - id: KvStoreInfo
    intent: Get metadata for a key-value store
    question: How do I see a KV store's history depth, TTL and size?
  - id: AddKvStore
    intent: Add a key-value store
    question: How do I create a KV store over the HTTP gateway?
  - id: KvStoreDestroy
    intent: Delete a key-value store entirely
    question: How do I delete a KV store along with all its keys?
  - id: KvStorePurge
    intent: Purge deleted keys from a KV store
    question: How do I clean up the tombstones of deleted keys in a KV store?
  - id: KvStoreKeys
    intent: List keys in a KV store
    question: What keys are in a given key-value store?
  - id: KvStoreWatch
    intent: Watch a KV store for changes
    question: How do I get notified as keys change in a key-value store?
  phrasing_ops: 7
  slug: synadia-communications-kv-management-api-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The license API from Synadia Communications — 1 operation(s) for license.
  name: Synadia Communications License API
  phrasing_intents:
  - id: deleteLicense
    intent: Remove the stored license
    question: Can I remove the license stored on this installation?
  - id: getLicenseStatus
    intent: Check license status and entitlements
    question: Is my Synadia Control Plane license valid, and what does it entitle me to?
  - id: updateLicense
    intent: Install a new license key
    question: How do I apply a new license key to the Control Plane?
  phrasing_ops: 3
  slug: synadia-communications-license-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The mirror API from Synadia Communications — 5 operation(s) for mirror.
  name: Synadia Communications Mirror API
  phrasing_intents:
  - id: deleteMirror
    intent: Delete a mirror stream
    question: Can I delete a mirror without affecting its source stream?
  - id: getMirror
    intent: Get a mirror stream
    question: What source stream is my mirror copying from?
  - id: updateMirror
    intent: Update a mirror stream's configuration
    question: Can I change a mirror's retention limits like max age or max bytes?
  - id: listMirrorConsumers
    intent: List consumers on a mirror
    question: Which consumers are reading from my mirror stream?
  - id: createMirrorPullConsumer
    intent: Create a pull consumer on a mirror
    question: Can I fetch messages from a mirror stream with a pull consumer?
  - id: createMirrorPushConsumer
    intent: Create a push consumer on a mirror
    question: Can a mirror stream push its messages to a delivery subject?
  - id: purgeMirror
    intent: Purge all messages from a mirror
    question: Can I empty a mirror stream's stored messages?
  phrasing_ops: 7
  slug: synadia-communications-mirror-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The NATS Core Messaging (Experimental) API from Synadia Communications — 1 operation(s) for nats core messaging (experimental).
  name: Synadia Communications NATS Core Messaging (Experimental) API
  phrasing_intents:
  - id: request
    intent: Send a request and wait for a reply
    question: Can I do request-reply against a NATS service over HTTP?
  - id: publish
    intent: Publish a message to a subject
    question: How do I publish a message to a NATS subject over HTTP?
  - id: subscribe
    intent: Subscribe to a subject and receive messages
    question: Can I receive messages published to a subject over HTTP?
  phrasing_ops: 3
  slug: synadia-communications-nats-core-messaging-experimental-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The nats-user API from Synadia Communications — 10 operation(s) for nats-user.
  name: Synadia Communications Nats User API
  phrasing_intents:
  - id: deleteNatsUser
    intent: Delete a NATS user
    question: Can I delete a NATS user from its account?
  - id: getNatsUser
    intent: Look up a NATS user
    question: How do I fetch the details of one NATS user by ID?
  - id: updateNatsUser
    intent: Update a NATS user
    question: How do I rename an existing NATS user?
  - id: listNatsUserTeamAppUsers
    intent: List app users with access to a NATS user
    question: Which teammates have been granted access to a specific NATS user?
  - id: unAssignNatsUserTeamAppUser
    intent: Remove a team member from a NATS user
    question: How do I revoke a teammate's access to a particular NATS user?
  - id: assignNatsUserTeamAppUser
    intent: Grant a team member a role on a NATS user
    question: How do I give a teammate access to one NATS user with a role?
  - id: downloadNatsUserBearerJwt
    intent: Get a bearer JWT for a NATS user
    question: How can I get a bearer token for a NATS user to connect with?
  - id: listNatsUserConnections
    intent: List a NATS user's live connections
    question: Which clients are currently connected as a given NATS user?
  phrasing_ops: 13
  slug: synadia-communications-nats-user-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The object-bucket API from Synadia Communications — 5 operation(s) for object-bucket.
  name: Synadia Communications Object Bucket API
  phrasing_intents:
  - id: deleteObjectBucket
    intent: Delete an object bucket
    question: Can I delete an object store bucket I no longer need?
  - id: getObjectBucket
    intent: Get an object bucket's info
    question: How do I see the configuration and state of one object store bucket?
  - id: updateObjectBucket
    intent: Update or seal an object bucket
    question: How do I change an existing object bucket's configuration?
  - id: listObjConsumers
    intent: List consumers on an object bucket
    question: Which consumers are reading from an object store bucket?
  - id: createObjPullConsumer
    intent: Create a pull consumer on an object bucket
    question: How do I add a pull consumer to an object store bucket?
  - id: createObjPushConsumer
    intent: Create a push consumer on an object bucket
    question: How do I push an object bucket's messages to a deliver subject?
  - id: purgeObjBucket
    intent: Purge all objects from an object bucket
    question: How do I empty an object bucket while keeping the bucket itself?
  phrasing_ops: 7
  slug: synadia-communications-object-bucket-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The ObjectStore API API from Synadia Communications — 1 operation(s) for objectstore api.
  name: Synadia Communications ObjectStore API
  phrasing_intents:
  - id: SimpleObjGet
    intent: Download an object from a bucket
    question: How do I fetch a stored object by bucket and name?
  - id: SimpleObjPutEntry
    intent: Upload or replace an object
    question: How do I upload a file into an object store bucket?
  - id: SimpleObjDeleteEntry
    intent: Delete an object from a bucket
    question: How do I delete a stored object from an object bucket?
  phrasing_ops: 3
  slug: synadia-communications-objectstore-api-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The ObjectStore Entry Operations API from Synadia Communications — 1 operation(s) for objectstore entry operations.
  name: Synadia Communications ObjectStore Entry Operations API
  phrasing_intents:
  - id: ObjGetEntry
    intent: Download an object from an object store
    question: How do I download a file stored in an object store?
  - id: ObjCreateEntry
    intent: Upload or replace an object
    question: Can I upload a file into an object store?
  - id: ObjDeleteEntry
    intent: Delete an object from an object store
    question: Can I delete a single file from an object store?
  phrasing_ops: 3
  slug: synadia-communications-objectstore-entry-operations-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The ObjectStore Management API API from Synadia Communications — 4 operation(s) for objectstore management api.
  name: Synadia Communications ObjectStore Management API
  phrasing_intents:
  - id: ObjmList
    intent: List all object stores
    question: What object store buckets do I have?
  - id: ObjmStoreInfo
    intent: Get an object store's metadata
    question: How big is an object store and what are its settings?
  - id: ObjmStoreAdd
    intent: Create an object store
    question: How do I create a new object store bucket?
  - id: ObjmStoreDestroy
    intent: Delete an object store and all its objects
    question: Can I delete an entire object store including every object in it?
  - id: ObjStoreKeys
    intent: List the objects in an object store
    question: What objects are stored in my object store?
  - id: ObjStoreWatch
    intent: Watch an object store for changes
    question: Can I get notified as objects change in an object store?
  phrasing_ops: 6
  slug: synadia-communications-objectstore-management-api-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The oidc-provider API from Synadia Communications — 3 operation(s) for oidc-provider.
  name: Synadia Communications Oidc Provider API
  phrasing_intents:
  - id: listOidcProviders
    intent: List configured OIDC sign-in providers
    question: Which OIDC identity providers are set up for single sign-on?
  - id: createOidcProvider
    intent: Add an OIDC sign-in provider
    question: How do I set up single sign-on with an OIDC identity provider?
  - id: deleteOidcProvider
    intent: Remove an OIDC provider
    question: Can I remove an OIDC provider so it's no longer used for login?
  - id: getOidcProvider
    intent: Look up one OIDC provider
    question: How can I view the settings of a specific OIDC provider?
  - id: updateOidcProvider
    intent: Change an OIDC provider's settings
    question: How do I rotate the client secret on an existing OIDC provider?
  - id: listOidcDefaultProvider
    intent: List default OIDC provider templates
    question: What default settings are offered for common OIDC identity providers?
  phrasing_ops: 6
  slug: synadia-communications-oidc-provider-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The personal-access-token API from Synadia Communications — 1 operation(s) for personal-access-token.
  name: Synadia Communications Personal Access Token API
  phrasing_intents:
  - id: deletePersonalAccessToken
    intent: Revoke a personal access token
    question: How do I revoke a personal access token I no longer use?
  - id: getPersonalAccessToken
    intent: Look up a personal access token
    question: How can I see when one of my personal access tokens expires?
  - id: updatePersonalAccessToken
    intent: Update a personal access token
    question: Can I extend the expiry of a personal access token?
  phrasing_ops: 3
  slug: synadia-communications-personal-access-token-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The platform-components API from Synadia Communications — 1 operation(s) for platform-components.
  name: Synadia Communications Platform Components API
  phrasing_intents:
  - id: platformComponentConnect
    intent: Connect a platform component
    question: How does a platform component register its connection with the Control Plane?
  phrasing_ops: 1
  slug: synadia-communications-platform-components-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The pull-consumer API from Synadia Communications — 1 operation(s) for pull-consumer.
  name: Synadia Communications Pull Consumer API
  phrasing_intents:
  - id: deletePullConsumer
    intent: Delete a pull consumer
    question: Can I delete a pull consumer I no longer need?
  - id: getPullConsumerInfo
    intent: Get a pull consumer's info
    question: How many messages are pending for my pull consumer?
  - id: updatePullConsumer
    intent: Update a pull consumer's settings
    question: Can I change a pull consumer's ack wait or max deliveries?
  phrasing_ops: 3
  slug: synadia-communications-pull-consumer-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The push-consumer API from Synadia Communications — 1 operation(s) for push-consumer.
  name: Synadia Communications Push Consumer API
  phrasing_intents:
  - id: deletePushConsumer
    intent: Delete a push consumer
    question: Can I delete a push consumer that is no longer delivering anywhere?
  - id: getPushConsumerInfo
    intent: Get a push consumer's info
    question: How do I check a push consumer's delivery subject and pending messages?
  - id: updatePushConsumer
    intent: Update a push consumer
    question: How do I change where a push consumer delivers messages?
  phrasing_ops: 3
  slug: synadia-communications-push-consumer-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The session API from Synadia Communications — 9 operation(s) for session.
  name: Synadia Communications Session API
  phrasing_intents:
  - id: listAlerts
    intent: List alerts
    question: What alerts have fired across my Synadia Control Plane?
  - id: listAppUsers
    intent: List application users
    question: Who are all the users of the Control Plane application?
  - id: createAppUser
    intent: Invite a user to the application
    question: How do I invite a new person to the Control Plane with a role?
  - id: listInvitations
    intent: List my pending team invitations
    question: Which team invitations are waiting for me to answer?
  - id: decideInvitation
    intent: Accept or decline a team invitation
    question: How do I accept an invitation to join a team?
  - id: listAppUserAccessTokens
    intent: List my personal access tokens
    question: Which personal access tokens have I created?
  - id: createAppUserAccessToken
    intent: Create a personal access token
    question: How do I create a personal access token to call the Control Plane API?
  - id: listAppServiceAccounts
    intent: List app service accounts
    question: Which service accounts exist for automation against the application?
  phrasing_ops: 13
  slug: synadia-communications-session-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The sig-key API from Synadia Communications — 1 operation(s) for sig-key.
  name: Synadia Communications Sig Key API
  phrasing_intents:
  - id: deleteAccountSk
    intent: Delete an account signing key
    question: Can I delete an old account signing key?
  - id: getAccountSk
    intent: Get an account signing key
    question: Can I view one account signing key by ID?
  - id: updateAccountSk
    intent: Disable a signing key or set its seed
    question: Can I disable one signing key without deleting it?
  phrasing_ops: 3
  slug: synadia-communications-sig-key-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The sig-key-group API from Synadia Communications — 5 operation(s) for sig-key-group.
  name: Synadia Communications Sig Key Group API
  phrasing_intents:
  - id: deleteAccountSkGroup
    intent: Delete a signing key group
    question: Can I delete an account signing key group?
  - id: getAccountSkGroup
    intent: Get an account signing key group
    question: What scope and status does a signing key group have?
  - id: updateAccountSkGroup
    intent: Update or disable a signing key group
    question: Can I disable a signing key group temporarily?
  - id: listAccountSkGroupKeys
    intent: List signing keys in a group
    question: Which signing keys belong to a signing key group?
  - id: copyAccountSkGroup
    intent: Copy a signing key group with its users
    question: Can I clone a signing key group, including its users with fresh NKeys?
  - id: listAccountSKGroupUsers
    intent: List NATS users in a signing key group
    question: Which NATS users were issued under a signing key group?
  - id: rotateAccountSk
    intent: Rotate a group's active signing key
    question: How do I rotate the active signing key for a group?
  phrasing_ops: 7
  slug: synadia-communications-sig-key-group-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The stream API from Synadia Communications — 5 operation(s) for stream.
  name: Synadia Communications Stream API
  phrasing_intents:
  - id: deleteStream
    intent: Delete a JetStream stream
    question: Can I delete a stream and its stored messages?
  - id: getStreamInfo
    intent: Get a JetStream stream's info
    question: How do I check a stream's configuration and message count?
  - id: updateStream
    intent: Update a JetStream stream's config
    question: How do I change the subjects an existing stream captures?
  - id: listConsumers
    intent: List consumers on a stream
    question: Which consumers are attached to a JetStream stream?
  - id: createPullConsumer
    intent: Create a pull consumer on a stream
    question: How do I create a pull consumer so workers fetch messages from a stream?
  - id: createPushConsumer
    intent: Create a push consumer on a stream
    question: How do I have a stream push messages to a deliver subject?
  - id: purgeStream
    intent: Purge all messages from a stream
    question: How do I clear every message out of a stream but keep the stream?
  phrasing_ops: 7
  slug: synadia-communications-stream-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The stream-export API from Synadia Communications — 3 operation(s) for stream-export.
  name: Synadia Communications Stream Export API
  phrasing_intents:
  - id: deleteStreamExport
    intent: Delete a stream export
    question: Can I stop exporting a stream to other accounts?
  - id: getStreamExport
    intent: Look up a stream export
    question: How do I see the details of one stream export?
  - id: listStreamShares
    intent: List accounts a stream export is shared with
    question: Which accounts can import a stream I've exported?
  - id: createStreamShares
    intent: Share a stream export with another account
    question: How do I let another account import my exported stream?
  - id: deleteStreamShare
    intent: Revoke a stream share from an account
    question: How do I revoke one account's access to my exported stream?
  phrasing_ops: 5
  slug: synadia-communications-stream-export-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The stream-import API from Synadia Communications — 1 operation(s) for stream-import.
  name: Synadia Communications Stream Import API
  phrasing_intents:
  - id: deleteStreamImport
    intent: Delete a stream import
    question: Can I stop importing a stream from another account?
  - id: getStreamImport
    intent: Look up a stream import
    question: How do I view the details of one stream import?
  phrasing_ops: 2
  slug: synadia-communications-stream-import-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The subject-export API from Synadia Communications — 3 operation(s) for subject-export.
  name: Synadia Communications Subject Export API
  phrasing_intents:
  - id: deleteSubjectExport
    intent: Delete a subject export
    question: Can I stop exporting a subject to other accounts?
  - id: getSubjectExport
    intent: Get a subject export
    question: What subject does a given export expose to other accounts?
  - id: updateSubjectExport
    intent: Update a subject export's settings
    question: Can I turn on service latency metrics for an exported subject?
  - id: listSubjectShares
    intent: List accounts a subject export is shared with
    question: Which accounts have been granted access to my exported subject?
  - id: createSubjectShares
    intent: Share a subject export with an account
    question: How do I share an exported subject with another account?
  - id: deleteSubjectShare
    intent: Revoke an account's share of a subject export
    question: Can I revoke one account's access to my exported subject?
  phrasing_ops: 6
  slug: synadia-communications-subject-export-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The subject-import API from Synadia Communications — 1 operation(s) for subject-import.
  name: Synadia Communications Subject Import API
  phrasing_intents:
  - id: deleteSubjectImport
    intent: Delete a subject import
    question: Can I remove a subject import from my account?
  - id: getSubjectImport
    intent: Look up a subject import
    question: How do I view the settings of one subject import?
  - id: updateSubjectImport
    intent: Update a subject import
    question: How do I change the JWT settings of an existing subject import?
  phrasing_ops: 3
  slug: synadia-communications-subject-import-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The system API from Synadia Communications — 35 operation(s) for system.
  name: Synadia Communications System API
  phrasing_intents:
  - id: deleteSystem
    intent: Delete a system
    question: What happens to the accounts when I delete a whole system?
  - id: getSystem
    intent: Get a NATS system's details
    question: What connection settings and JetStream domain does my NATS system have?
  - id: updateSystem
    intent: Update a system's settings
    question: Can I change a system's server URL and test the connection before saving?
  - id: listAccounts
    intent: List accounts in a system
    question: Which NATS accounts exist in my system?
  - id: createAccount
    intent: Create an account in a system
    question: How do I add a new NATS account to my system?
  - id: listAccountsOverviewMetrics
    intent: Get overview metrics for a system's accounts
    question: What are the usage metrics across all accounts in my system?
  - id: listAgentTokens
    intent: List dataplane agent tokens
    question: Which agent tokens have been issued for my system's dataplane agent?
  - id: rotateAgentToken
    intent: Rotate the dataplane agent token
    question: How do I rotate the token my dataplane agent uses to connect?
  phrasing_ops: 44
  slug: synadia-communications-system-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The team API from Synadia Communications — 10 operation(s) for team.
  name: Synadia Communications Team API
  phrasing_intents:
  - id: deleteTeam
    intent: Delete a team
    question: Can I permanently delete a team?
  - id: getTeam
    intent: Get a team
    question: Can I look up a team's details by its ID?
  - id: updateTeam
    intent: Rename a team
    question: Can I change a team's name?
  - id: listTeamAppUsers
    intent: List a team's app users
    question: Who are the members of my team?
  - id: unAssignTeamAppUser
    intent: Remove a user from a team
    question: Can I remove someone from my team?
  - id: updateTeamAppUser
    intent: Change a user's role on a team
    question: Can I promote a team member to a different role?
  - id: inviteAppUser
    intent: Invite a user to a team
    question: How do I invite a colleague to join my team?
  - id: leaveTeam
    intent: Leave a team
    question: Can I remove myself from a team?
  phrasing_ops: 15
  slug: synadia-communications-team-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The team-service-account API from Synadia Communications — 2 operation(s) for team-service-account.
  name: Synadia Communications Team Service Account API
  phrasing_intents:
  - id: deleteTeamServiceAccount
    intent: Delete a team service account
    question: Can I delete a service account I no longer use?
  - id: getTeamServiceAccount
    intent: Get a team service account
    question: What role and resources does a service account have?
  - id: updateTeamServiceAccount
    intent: Update a team service account
    question: Can I change a service account's role or the resources it can reach?
  - id: listTeamServiceAccountTokens
    intent: List a service account's access tokens
    question: Which access tokens exist for a service account?
  - id: createTeamServiceAccountToken
    intent: Create an access token for a service account
    question: How do I generate an API token for a service account?
  phrasing_ops: 5
  slug: synadia-communications-team-service-account-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The team-service-account-tokens API from Synadia Communications — 1 operation(s) for team-service-account-tokens.
  name: Synadia Communications Team Service Account Tokens API
  phrasing_intents:
  - id: deleteTeamServiceAccountToken
    intent: Revoke a service account token
    question: Can I revoke a leaked service account token?
  - id: getTeamServiceAccountToken
    intent: Get a service account token
    question: When does a service account token expire?
  - id: updateTeamServiceAccountToken
    intent: Rename or extend a service account token
    question: Can I change when a service account token expires?
  phrasing_ops: 3
  slug: synadia-communications-team-service-account-tokens-api
- baseURL: https://cloud.synadia.com/api
  baseurl_source: declared
  description: The workloads API from Synadia Communications — 2 operation(s) for workloads.
  name: Synadia Communications Workloads API
  phrasing_intents:
  - id: getWorkloadLimits
    intent: Get workload limits for an account
    question: What workload limits apply to my account?
  - id: listWorkloadTags
    intent: List workload tags for an account
    question: Which tags are used on workloads in my account?
  phrasing_ops: 2
  slug: synadia-communications-workloads-api
artifact_total: 56
asyncapis:
- description: ''
  name: Synadia Communications Event Surface
  slug: synadia-communications-event-surface
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.synadia.com/rss.xml
- group: other
  href: https://artifacts.apis.io/synadia-communications/capabilities/synadia-communications-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/synadia-communications-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/synadia-communications/overlays/synadia-communications-control-plane-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/synadia-communications-control-plane-overlay.yaml
- group: other
  href: https://artifacts.apis.io/synadia-communications/overlays/synadia-communications-http-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/synadia-communications-http-gateway-overlay.yaml
- group: commercial
  title: ''
  type: License
  url: https://github.com/synadia-io/control-plane-sdk-go/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.synadia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.synadia.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.synadia.com/
- group: docs
  title: ''
  type: APIReference
  url: https://cloud.synadia.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.synadia.com/cloud/walkthrough
- group: operate
  title: ''
  type: Support
  url: https://www.synadia.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.synadia.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/synadia-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.synadia.com/cloud/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.synadia.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.synadia.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.synadia.com/legal/privacy
- group: agent
  href: https://artifacts.apis.io/synadia-communications/llms/synadia-communications-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/synadia-communications-llms.txt
- group: agent
  href: https://artifacts.apis.io/synadia-communications/well-known/synadia-communications-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/synadia-communications-well-known.yml
- group: build
  href: https://artifacts.apis.io/synadia-communications/packages/synadia-communications-packages.yml
  title: ''
  type: Packages
  url: packages/synadia-communications-packages.yml
- group: build
  href: https://artifacts.apis.io/synadia-communications/packages/synadia-communications-packages.yml
  title: ''
  type: SDKs
  url: packages/synadia-communications-packages.yml
- group: build
  href: https://artifacts.apis.io/synadia-communications/cli/synadia-communications-cli.yml
  title: ''
  type: CLI
  url: cli/synadia-communications-cli.yml
- group: agent
  href: https://artifacts.apis.io/synadia-communications/mcp/synadia-communications-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/synadia-communications-mcp.yml
- group: agent
  href: https://artifacts.apis.io/synadia-communications/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/synadia-communications/conventions/synadia-communications-conventions.yml
  title: ''
  type: Conventions
  url: conventions/synadia-communications-conventions.yml
- group: design
  href: https://artifacts.apis.io/synadia-communications/errors/synadia-communications-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/synadia-communications-problem-types.yml
- group: design
  href: https://artifacts.apis.io/synadia-communications/data-model/synadia-communications-data-model.yml
  title: ''
  type: DataModel
  url: data-model/synadia-communications-data-model.yml
- group: design
  href: https://artifacts.apis.io/synadia-communications/conformance/synadia-communications-conformance.yml
  title: ''
  type: Conformance
  url: conformance/synadia-communications-conformance.yml
- group: auth
  href: https://artifacts.apis.io/synadia-communications/conformance/synadia-communications-conformance.yml
  title: ''
  type: Compliance
  url: conformance/synadia-communications-conformance.yml
- group: auth
  href: https://artifacts.apis.io/synadia-communications/security/synadia-communications-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/synadia-communications-trust-center.yml
- group: design
  href: https://artifacts.apis.io/synadia-communications/lifecycle/synadia-communications-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/synadia-communications-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/synadia-communications/authentication/synadia-communications-authentication.yml
  title: ''
  type: Authentication
  url: authentication/synadia-communications-authentication.yml
- group: auth
  href: https://artifacts.apis.io/synadia-communications/security/synadia-communications-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/synadia-communications-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/synadia-communications/security/synadia-communications-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/synadia-communications-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/synadia-communications/security/synadia-communications-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/synadia-communications-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/synadia-communications/plans/synadia-communications-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/synadia-communications-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/synadia-communications/rate-limits/synadia-communications-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/synadia-communications-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/synadia-communications/changelog/synadia-communications-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/synadia-communications-changelog.yml
- group: start
  href: https://artifacts.apis.io/synadia-communications/sandbox/synadia-communications-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/synadia-communications-sandbox.yml
created: '2026-08-29'
description: 'Synadia Communications, Inc. is the creator and primary maintainer of NATS.io, the CNCF connectivity and messaging system, and sells the commercial platform built on it. Its products are Synadia Cloud (fully managed, globally distributed NATS with a REST control-plane API and an HTTP Gateway that exposes NATS key-value, object store, publish, request and subscribe over plain HTTP), Synadia Platform / Control Plane (self-hosted management, security and observability for NATS deployments on Kubernetes or Docker), Synadia Connect (managed connectors bridging NATS to external data systems), Synadia Insights (NATS monitoring and 143 automated audit checks), and Synadia Protect (a policy-enforcing security gateway for NATS traffic). The company positions NATS as the connectivity fabric for agentic AI, edge and distributed systems, and publishes an unusually complete machine-readable surface for agents: an llms.txt site index, Markdown twins of every page, an RFC 9727 API catalog,
  and a registry of provider-authored Agent Skills.'
finops:
- has_sources: true
  method: derived
  name: Synadia Communications Finops
  primary_unit: one nats system
  service_category: ''
  slug: synadia-communications-finops
  template: false
image: https://www.synadia.com/images/og-image-default.webp
layout: provider
modified: '2026-10-06'
name: Synadia Communications
nav: Providers
network: true
overview: 'Synadia Communications publishes 41 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Admin API, Agent Token API, and 38 more. Tagged areas include Company, Messaging, Event Streaming, NATS, and Distributed Systems.


  The Synadia Communications catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Synadia Communications'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Synadia Communications Plans Pricing
  plan_count: 5
  slug: synadia-communications-plans-pricing
- name: Synadia Communications Price Estimates
  plan_count: 0
  slug: synadia-communications-price-estimates
random_paper: 23
rate_limits:
- limit_count: 0
  name: Synadia Communications Rate Limits
  slug: synadia-communications-rate-limits
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: Synadia Communications API Rules
  rule_count: 59
  severity_counts:
    error: 34
    hint: 0
    info: 7
    warn: 18
  slug: synadia-communications-rules
score:
  band: exemplar
  composite: 72.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 62.1
    developer_ergonomics: 85.7
    discoverability: 73.2
    operational_transparency: 28.9
  previous_composite: 70.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 41
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/synadia-communications/synadia-communications-2026-09-02T161447.png
security:
- kind: authentication
  name: Synadia Communications Authentication
  slug: synadia-communications-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Synadia Communications Domain Security
  slug: synadia-communications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Synadia Communications Vulnerability Disclosure
  slug: synadia-communications-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Synadia Communications Trust Center
  slug: synadia-communications-trust-center
  summary_line: SOC 2
skill_count: 5
skills:
- name: nats-server-quickstart
  slug: synadia-communications-nats-server-quickstart
- name: synadia-cloud-onboarding
  slug: synadia-communications-synadia-cloud-onboarding
- name: synadia-deploy-for-kubernetes
  slug: synadia-communications-synadia-deploy-for-kubernetes
- name: synadia-insights-setup
  slug: synadia-communications-synadia-insights-setup
- name: synadia-platform-deployment
  slug: synadia-communications-synadia-platform-deployment
slug: synadia-communications
tags:
- Company
- Messaging
- Event Streaming
- NATS
- Distributed Systems
- Edge Computing
- Publish Subscribe
- Key-Value Store
- Object Storage
- Infrastructure
- AI Agents
- Open Source
website: https://www.synadia.com/
---
