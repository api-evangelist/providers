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
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 636
  human_in_the_loop: 1
  name: Authentik Agentic Access
  operation_count: 1193
  slug: authentik-agentic-access
  summary_line: 1193 operations · 636 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Users, groups, applications, tokens, brands, application entitlements and authenticated sessions — the identity records and the objects users see.
  name: Authentik Core API
  phrasing_intents:
  - id: core_application_entitlements_list
    intent: List application entitlements
    question: Which entitlements are defined for my applications in authentik?
  - id: core_application_entitlements_create
    intent: Create an application entitlement
    question: How do I define a new entitlement that users of an application can be granted?
  - id: core_application_entitlements_retrieve
    intent: Get an application entitlement
    question: What attributes does a specific entitlement carry?
  - id: core_application_entitlements_update
    intent: Replace an application entitlement
    question: Can I fully overwrite an existing entitlement's name and application?
  - id: core_application_entitlements_partial_update
    intent: Edit fields on an entitlement
    question: Can I rename an entitlement without resending its application?
  - id: core_application_entitlements_destroy
    intent: Delete an application entitlement
    question: Can I remove an entitlement that is no longer needed?
  - id: core_application_entitlements_used_by_list
    intent: See what uses an entitlement
    question: Which objects depend on a given entitlement before I delete it?
  - id: core_application_entitlements_requestable_list
    intent: List entitlements I can request
    question: Which entitlements am I allowed to request access to?
  phrasing_ops: 78
  slug: authentik-core-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Certificate-key pairs used to sign SAML assertions and OIDC ID tokens, and to validate webhook receivers.
  name: Authentik Crypto API
  phrasing_intents:
  - id: crypto_certificatekeypairs_list
    intent: List certificate-key pairs
    question: Which certificates and key pairs are stored in my authentik instance?
  - id: crypto_certificatekeypairs_create
    intent: Import a certificate-key pair
    question: How do I upload an existing PEM certificate so authentik can use it?
  - id: crypto_certificatekeypairs_retrieve
    intent: Get a certificate-key pair
    question: What are the details of one certificate-key pair, like its fingerprint and expiry?
  - id: crypto_certificatekeypairs_update
    intent: Replace a certificate-key pair
    question: How do I swap in a renewed certificate on an existing keypair?
  - id: crypto_certificatekeypairs_partial_update
    intent: Edit fields on a certificate-key pair
    question: Can I just rename a certificate-key pair without re-uploading it?
  - id: crypto_certificatekeypairs_destroy
    intent: Delete a certificate-key pair
    question: How do I remove a certificate I no longer need from authentik?
  - id: crypto_certificatekeypairs_used_by_list
    intent: See what uses a certificate-key pair
    question: Which providers or sources depend on this certificate before I rotate it?
  - id: crypto_certificatekeypairs_view_certificate_retrieve
    intent: View or download a certificate
    question: How do I get the PEM text of a certificate stored in authentik?
  phrasing_ops: 10
  slug: authentik-crypto-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Audit events, notification rules and notification transports — including the webhook and Slack transports that push authentik events to external receivers.
  name: Authentik Events API
  phrasing_intents:
  - id: events_events_list
    intent: Browse the audit event log
    question: Which login and admin events did a specific user trigger?
  - id: events_events_create
    intent: Record a custom audit event
    question: Can I write my own entry into the authentik event log?
  - id: events_events_retrieve
    intent: Get one audit event
    question: What exactly is recorded in a single event, including its context?
  - id: events_events_update
    intent: Replace an audit event
    question: Can I overwrite an existing event record with a new action and app?
  - id: events_events_partial_update
    intent: Edit fields on an audit event
    question: Can I change just the expiry date of a logged event?
  - id: events_events_destroy
    intent: Delete an audit event
    question: Can I remove a single entry from the event log?
  - id: events_events_actions_list
    intent: List all event action types
    question: What kinds of actions can appear in the authentik event log?
  - id: events_events_export_create
    intent: Export audit events to a file
    question: How do I download the event log as a file?
  phrasing_ops: 33
  slug: authentik-events-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Flow instances, flow bindings and the flow executor that drives authentication, enrollment, recovery and unenrollment.
  name: Authentik Flows API
  phrasing_intents:
  - id: flows_bindings_list
    intent: List flow stage bindings
    question: Which stages are bound to my authentik flows, and in what order?
  - id: flows_bindings_create
    intent: Add a stage to a flow
    question: How do I add a stage to a login flow at a specific position?
  - id: flows_bindings_retrieve
    intent: Get a flow stage binding
    question: What order and policy settings does a specific stage binding have?
  - id: flows_bindings_update
    intent: Replace a flow stage binding
    question: Can I overwrite every field of a stage binding in one call?
  - id: flows_bindings_partial_update
    intent: Change part of a flow stage binding
    question: Can I just move a stage to a different position in its flow?
  - id: flows_bindings_destroy
    intent: Remove a stage from a flow
    question: How do I take a stage out of a flow?
  - id: flows_bindings_used_by_list
    intent: See what uses a flow stage binding
    question: What objects reference a particular stage binding?
  - id: flows_executor_get
    intent: Get the next challenge in a running flow
    question: How does a custom login UI fetch the current challenge of an authentik flow?
  phrasing_ops: 22
  slug: authentik-flows-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Policies and policy bindings — expression, event matcher, GeoIP, password, password expiry, reputation and unique-password types.
  name: Authentik Policies API
  phrasing_intents:
  - id: policies_all_list
    intent: List policies of every type
    question: Which policies of any type exist in my authentik instance?
  - id: policies_all_retrieve
    intent: Get any policy by UUID
    question: What is a policy when I only know its UUID and not its type?
  - id: policies_all_destroy
    intent: Delete a policy of any type
    question: Can I delete a policy by UUID without knowing which type it is?
  - id: policies_all_test_create
    intent: Test a policy against a user
    question: How do I check whether a policy would pass or fail for a particular user?
  - id: policies_all_used_by_list
    intent: See what uses a policy of any type
    question: Which flows, stages or apps reference a policy I only know by UUID?
  - id: policies_all_cache_clear_create
    intent: Clear the policy cache
    question: How do I flush cached policy results so changes take effect immediately?
  - id: policies_all_cache_info_retrieve
    intent: Show policy cache statistics
    question: How many policy results are currently cached?
  - id: policies_all_types_list
    intent: List creatable policy types
    question: What kinds of policies can I create in authentik?
  phrasing_ops: 76
  slug: authentik-policies-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: 'Protocol providers: OAuth2/OIDC, SAML, SCIM, LDAP, RADIUS, Proxy, RAC, WS-Fed, Google Workspace, Microsoft Entra and the Shared Signals Framework backchannel.'
  name: Authentik Providers API
  phrasing_intents:
  - id: providers_all_list
    intent: List all providers of every type
    question: Which providers of any type are configured in my authentik instance?
  - id: providers_all_retrieve
    intent: Get any provider by ID
    question: What type of provider is a given provider ID, whatever its protocol?
  - id: providers_all_destroy
    intent: Delete a provider of any type
    question: Can I delete a provider without knowing which protocol type it is?
  - id: providers_all_used_by_list
    intent: See what depends on a provider
    question: What objects reference a provider before I delete it, whatever its type?
  - id: providers_all_types_list
    intent: List creatable provider types
    question: What kinds of providers can I create in authentik?
  - id: providers_google_workspace_list
    intent: List Google Workspace providers
    question: Which Google Workspace sync providers have I set up?
  - id: providers_google_workspace_create
    intent: Create a Google Workspace provider
    question: How do I sync authentik users and groups into Google Workspace?
  - id: providers_google_workspace_retrieve
    intent: Get a Google Workspace provider
    question: What settings does a specific Google Workspace provider use for user deletion?
  phrasing_ops: 131
  slug: authentik-providers-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Role-based access control — roles, global and object-level permissions, and initial permission sets.
  name: Authentik RBAC API
  phrasing_intents:
  - id: rbac_initial_permissions_list
    intent: List initial permission sets
    question: Which initial permission sets are configured for newly created objects?
  - id: rbac_initial_permissions_create
    intent: Create an initial permission set
    question: How do I grant a role permissions automatically on objects a user creates?
  - id: rbac_initial_permissions_retrieve
    intent: Get one initial permission set
    question: What role and permissions does a specific initial permissions entry grant?
  - id: rbac_initial_permissions_update
    intent: Replace an initial permission set
    question: How do I fully overwrite an existing initial permissions entry?
  - id: rbac_initial_permissions_partial_update
    intent: Patch fields of an initial permission set
    question: Can I change only the permissions list on an initial permission set?
  - id: rbac_initial_permissions_destroy
    intent: Delete an initial permission set
    question: How do I stop auto-granting permissions on new objects by removing an initial permission set?
  - id: rbac_initial_permissions_used_by_list
    intent: See what uses an initial permission set
    question: Which objects reference a given initial permissions entry?
  - id: rbac_permissions_list
    intent: List available permissions
    question: Which permissions exist in authentik that I can grant to roles?
  phrasing_ops: 22
  slug: authentik-rbac-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: The self-describing OpenAPI schema endpoint every authentik instance serves.
  name: Authentik Schema API
  phrasing_intents:
  - id: schema_retrieve
    intent: Download the OpenAPI schema for the API
    question: Where can I download the OpenAPI 3 definition for my authentik instance's API?
  phrasing_ops: 1
  slug: authentik-schema-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: External identity sources — LDAP, OAuth, SAML, SCIM, Kerberos, Plex and Telegram — plus their user and group connections.
  name: Authentik Sources API
  phrasing_intents:
  - id: sources_all_list
    intent: List all federation and sync sources
    question: Which login and directory sources are set up in authentik across every type?
  - id: sources_all_retrieve
    intent: Get any source by its slug
    question: What type of source is behind a given slug, whatever protocol it uses?
  - id: sources_all_destroy
    intent: Delete a source of any type
    question: Can built-in sources be deleted, or only ones I created?
  - id: sources_all_used_by_list
    intent: See what depends on a source
    question: Which objects still reference a source before I delete it?
  - id: sources_all_types_list
    intent: List source types that can be created
    question: What kinds of sources can I create in authentik?
  - id: sources_all_user_settings_list
    intent: List sources the current user can configure
    question: Which sources can I, as a signed-in user, connect or configure on my own account?
  - id: sources_group_connections_all_list
    intent: List group-source connections of every type
    question: Which authentik groups are linked to groups in external sources, across all source types?
  - id: sources_group_connections_all_retrieve
    intent: Get a group-source connection of any type
    question: What external identifier is a particular group connection mapped to, whatever its source type?
  phrasing_ops: 173
  slug: authentik-sources-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: 'Flow stages: identification, password, consent, prompt, email, captcha, mTLS, redirect, user write/login/logout/delete, account lockdown and every authenticator setup and validation stage.'
  name: Authentik Stages API
  phrasing_intents:
  - id: stages_account_lockdown_list
    intent: List account lockdown stages
    question: Which account lockdown stages are configured in my authentik instance?
  - id: stages_account_lockdown_create
    intent: Create an account lockdown stage
    question: How do I add a stage that locks down a compromised account?
  - id: stages_account_lockdown_retrieve
    intent: Get an account lockdown stage
    question: What does a specific account lockdown stage do to the user when it runs?
  - id: stages_account_lockdown_update
    intent: Replace an account lockdown stage's settings
    question: Can I overwrite every setting on an existing account lockdown stage in one request?
  - id: stages_account_lockdown_partial_update
    intent: Change one setting on an account lockdown stage
    question: Can I turn on token revocation for an existing lockdown stage without touching its other settings?
  - id: stages_account_lockdown_destroy
    intent: Delete an account lockdown stage
    question: How can I remove an account lockdown stage I no longer need?
  - id: stages_account_lockdown_used_by_list
    intent: See what uses an account lockdown stage
    question: Which flows depend on a given account lockdown stage?
  - id: stages_all_list
    intent: List every stage of any type
    question: What stages exist across all types in my authentik install?
  phrasing_ops: 210
  slug: authentik-stages-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Instance administration — installed apps, models, version, system information, workers and the file storage backend.
  name: Authentik Admin API
  phrasing_intents:
  - id: admin_apps_list
    intent: List the installed apps
    question: Which Django apps are installed in my authentik server?
  - id: admin_file_list
    intent: List files in the storage backend
    question: What files have been uploaded to authentik's storage backend?
  - id: admin_file_create
    intent: Upload a file to storage
    question: How do I upload a logo or background image into authentik's file storage?
  - id: admin_file_destroy
    intent: Delete a file from storage
    question: Can I remove an uploaded file from authentik's storage backend?
  - id: admin_file_used_by_list
    intent: See what uses a stored file
    question: Which objects still reference an uploaded file before I delete it?
  - id: admin_models_list
    intent: List the installed models
    question: Which data models are installed in my authentik instance?
  - id: admin_settings_retrieve
    intent: Get the system settings
    question: What are the current global settings on my authentik instance?
  - id: admin_settings_update
    intent: Replace the system settings
    question: Can I overwrite the full set of global settings, feature flags included, in one call?
  phrasing_ops: 14
  slug: authentik-admin-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Agent accounts — service accounts that act on behalf of a parent user when calling the authentik API, with expiring tokens and audited delegation.
  name: Authentik Agents API
  phrasing_intents:
  - id: agents_agents_list
    intent: List agent identities
    question: Which delegate agent identities have been provisioned in authentik?
  - id: agents_agents_create
    intent: Provision an agent identity for a user
    question: How do I create a delegate identity that acts for a user, like an AI agent?
  - id: agents_agents_retrieve
    intent: Get an agent identity
    question: What are the details of one agent identity, including its parent user?
  - id: agents_agents_update
    intent: Replace an agent identity's profile
    question: How do I overwrite an agent's username, display name and email all at once?
  - id: agents_agents_partial_update
    intent: Change settings on an agent identity
    question: Can I deactivate an agent without deleting it?
  - id: agents_agents_destroy
    intent: Delete an agent identity
    question: How do I permanently remove a delegate agent identity?
  phrasing_ops: 6
  slug: authentik-agents-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Authenticator device management for TOTP, static, WebAuthn, SMS, email, Duo and endpoint devices, from both the admin and end-user perspectives.
  name: Authentik Authenticators API
  phrasing_intents:
  - id: authenticators_admin_all_list
    intent: List every MFA device a user has (admin)
    question: As an admin, how can I see all of a given user's MFA devices across every type?
  - id: authenticators_admin_duo_list
    intent: List all users' Duo devices (admin)
    question: Which Duo devices are enrolled across all users in authentik?
  - id: authenticators_admin_duo_create
    intent: Create a Duo device record (admin)
    question: Can an admin register a Duo device record directly through the API?
  - id: authenticators_admin_duo_retrieve
    intent: Get any user's Duo device (admin)
    question: As an admin, how do I inspect a specific user's Duo device?
  - id: authenticators_admin_duo_update
    intent: Replace any user's Duo device (admin)
    question: As an admin, how do I fully overwrite another user's Duo device record?
  - id: authenticators_admin_duo_partial_update
    intent: Rename any user's Duo device (admin)
    question: As an admin, can I rename a user's Duo device without resending the whole record?
  - id: authenticators_admin_duo_destroy
    intent: Remove any user's Duo device (admin)
    question: How can an admin remove a user's lost Duo device?
  - id: authenticators_admin_email_list
    intent: List all users' email authenticators (admin)
    question: Which email-based MFA devices exist across all users?
  phrasing_ops: 83
  slug: authentik-authenticators-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Endpoint device management — the authentik Agent connectors, device enrollment tokens, device bindings, device access groups, Fleet and Google Chrome device-trust connectors, and platform SSO registra
  name: Authentik Endpoints API
  phrasing_intents:
  - id: endpoints_agents_connectors_list
    intent: List authentik Agent connectors
    question: Which authentik Agent connectors are set up for my devices?
  - id: endpoints_agents_connectors_create
    intent: Create an authentik Agent connector
    question: How do I set up a new connector for the authentik Agent on endpoints?
  - id: endpoints_agents_connectors_retrieve
    intent: Get an authentik Agent connector
    question: What settings does a particular Agent connector have?
  - id: endpoints_agents_connectors_update
    intent: Replace an Agent connector's settings
    question: Can I overwrite the full configuration of an Agent connector in one call?
  - id: endpoints_agents_connectors_partial_update
    intent: Change some settings on an Agent connector
    question: Can I just disable an Agent connector without touching its other settings?
  - id: endpoints_agents_connectors_destroy
    intent: Delete an authentik Agent connector
    question: How do I remove an Agent connector I no longer use?
  - id: endpoints_agents_connectors_mdm_config_create
    intent: Generate MDM config to deploy the Agent
    question: How do I get a configuration profile to push the authentik Agent through my MDM?
  - id: endpoints_agents_connectors_used_by_list
    intent: See what uses an Agent connector
    question: What objects depend on this Agent connector?
  phrasing_ops: 70
  slug: authentik-endpoints-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Enterprise licensing — license installation, summary and forecast for a licensed authentik deployment.
  name: Authentik Enterprise API
  phrasing_intents:
  - id: enterprise_license_list
    intent: List enterprise licenses
    question: Which enterprise licenses are installed on my authentik instance?
  - id: enterprise_license_create
    intent: Install an enterprise license key
    question: How do I add a new enterprise license key to authentik?
  - id: enterprise_license_retrieve
    intent: Get one enterprise license
    question: What are the details of one specific installed license?
  - id: enterprise_license_update
    intent: Replace the key of an installed license
    question: How do I swap the key on an existing license record with a renewed one?
  - id: enterprise_license_partial_update
    intent: Patch an installed license's key
    question: Can I patch just the key field on an installed license?
  - id: enterprise_license_destroy
    intent: Remove an enterprise license
    question: How do I uninstall an enterprise license I no longer use?
  - id: enterprise_license_used_by_list
    intent: See what depends on a license
    question: What objects reference a given enterprise license?
  - id: enterprise_license_forecast_retrieve
    intent: Forecast license user needs for a year
    question: How many users will I need to license a year from now?
  phrasing_ops: 10
  slug: authentik-enterprise-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Identity lifecycle operations, including scheduled user offboarding with session and token revocation and a cancellable pending state.
  name: Authentik Lifecycle API
  phrasing_intents:
  - id: lifecycle_iterations_create
    intent: Start an access review iteration
    question: How do I kick off a new access review cycle for an object type?
  - id: lifecycle_iterations_list_latest
    intent: Get the latest review iteration for an object
    question: What is the most recent access review for a specific group or application?
  - id: lifecycle_iterations_list_open
    intent: List open access review iterations
    question: Which access reviews are still open and waiting on reviewers?
  - id: lifecycle_reviews_create
    intent: Submit a review for an iteration
    question: How do I sign off on an access review I was assigned?
  - id: lifecycle_rules_list
    intent: List lifecycle review rules
    question: What recurring access review rules are configured?
  - id: lifecycle_rules_create
    intent: Create a lifecycle review rule
    question: How do I schedule periodic access reviews for groups or applications?
  - id: lifecycle_rules_retrieve
    intent: Get a lifecycle review rule
    question: How often does a given access review rule run and who reviews it?
  - id: lifecycle_rules_update
    intent: Replace a lifecycle review rule
    question: How do I redefine an entire access review rule in one request?
  phrasing_ops: 14
  slug: authentik-lifecycle-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Blueprints — the YAML templates that declare authentik configuration as code, and the blueprint instances that apply them.
  name: Authentik Managed API
  phrasing_intents:
  - id: managed_blueprints_list
    intent: List blueprint instances
    question: Which blueprint instances are configured in authentik?
  - id: managed_blueprints_create
    intent: Create a blueprint instance
    question: How do I register a blueprint so authentik applies it?
  - id: managed_blueprints_retrieve
    intent: Get a blueprint instance
    question: What path and context does a particular blueprint instance use?
  - id: managed_blueprints_update
    intent: Replace a blueprint instance
    question: Can I overwrite all settings of a blueprint instance at once?
  - id: managed_blueprints_partial_update
    intent: Change part of a blueprint instance
    question: Can I just disable a blueprint instance without deleting it?
  - id: managed_blueprints_destroy
    intent: Delete a blueprint instance
    question: How do I remove a blueprint instance?
  - id: managed_blueprints_apply_create
    intent: Apply a blueprint instance now
    question: How do I run a blueprint immediately instead of waiting for the schedule?
  - id: managed_blueprints_used_by_list
    intent: See what uses a blueprint instance
    question: What objects reference a given blueprint instance?
  phrasing_ops: 10
  slug: authentik-managed-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Outpost instances and service connections (Docker, Kubernetes) — the deployable components that run the proxy, LDAP and RADIUS providers.
  name: Authentik Outposts API
  phrasing_intents:
  - id: outposts_instances_list
    intent: List outposts
    question: Which outposts are deployed in my authentik instance?
  - id: outposts_instances_create
    intent: Create an outpost
    question: How do I deploy a new proxy or LDAP outpost in authentik?
  - id: outposts_instances_retrieve
    intent: Get an outpost's details
    question: What providers and config does one specific outpost have?
  - id: outposts_instances_update
    intent: Replace an outpost's settings
    question: Can I overwrite an outpost's whole definition, including name, type, providers and config, in one call?
  - id: outposts_instances_partial_update
    intent: Change some outpost settings
    question: Can I just rename an outpost without resending its config?
  - id: outposts_instances_destroy
    intent: Delete an outpost
    question: How do I remove an outpost I no longer run?
  - id: outposts_instances_health_list
    intent: Check an outpost's current health
    question: Is my outpost connected and healthy right now?
  - id: outposts_instances_used_by_list
    intent: See what uses an outpost
    question: Which objects depend on a given outpost?
  phrasing_ops: 34
  slug: authentik-outposts-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Property mappings — the expressions that shape claims, attributes and payloads for every provider and source type, plus notification webhook bodies.
  name: Authentik Property Mappings API
  phrasing_intents:
  - id: propertymappings_all_list
    intent: List property mappings of every type
    question: What property mappings exist across all types in my authentik instance?
  - id: propertymappings_all_retrieve
    intent: Get any property mapping by ID
    question: How do I look up a property mapping when I only have its UUID and not its type?
  - id: propertymappings_all_destroy
    intent: Delete any property mapping by ID
    question: Can I delete a property mapping through the generic endpoint without knowing its type?
  - id: propertymappings_all_test_create
    intent: Test a property mapping against a user
    question: How do I preview what a property mapping expression returns for a given user?
  - id: propertymappings_all_used_by_list
    intent: See what uses any property mapping
    question: Which providers or sources reference a mapping, looked up by its UUID alone?
  - id: propertymappings_all_types_list
    intent: List creatable property mapping types
    question: What kinds of property mappings can I create in authentik?
  - id: propertymappings_notification_list
    intent: List notification webhook mappings
    question: Which webhook mappings shape the payload of my notification transports?
  - id: propertymappings_notification_create
    intent: Create a notification webhook mapping
    question: How do I customize the JSON body a notification webhook sends?
  phrasing_ops: 111
  slug: authentik-propertymappings-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Remote Access Control — browser-based RDP, SSH and VNC endpoints and their single-use connection tokens.
  name: Authentik RAC API
  phrasing_intents:
  - id: rac_connection_tokens_list
    intent: List remote access connection tokens
    question: Which remote access connection tokens are active?
  - id: rac_connection_tokens_retrieve
    intent: Get a remote access connection token
    question: Which endpoint and provider does a connection token point to?
  - id: rac_connection_tokens_update
    intent: Replace a remote access connection token
    question: Can I overwrite both the provider and endpoint on a connection token?
  - id: rac_connection_tokens_partial_update
    intent: Change part of a connection token
    question: Can I just point a connection token at a different endpoint?
  - id: rac_connection_tokens_destroy
    intent: Revoke a remote access connection token
    question: How do I kill a remote access connection token?
  - id: rac_connection_tokens_used_by_list
    intent: See what uses a connection token
    question: What references a particular RAC connection token?
  - id: rac_endpoints_list
    intent: List accessible remote access endpoints
    question: Which remote desktop or SSH endpoints can I connect to?
  - id: rac_endpoints_create
    intent: Create a remote access endpoint
    question: How do I add an RDP, SSH or VNC host for remote access?
  phrasing_ops: 13
  slug: authentik-rac-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Reporting surface for exportable user and event data.
  name: Authentik Reports API
  phrasing_intents:
  - id: reports_exports_list
    intent: List data exports
    question: Which report exports have been generated in authentik?
  - id: reports_exports_retrieve
    intent: Get one data export
    question: What are the details of a single report export I already generated?
  - id: reports_exports_destroy
    intent: Delete a data export
    question: How do I remove an old report export I no longer need?
  phrasing_ops: 3
  slug: authentik-reports-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Privileged access management — access request rules, rule bindings, grant requests, reviewer workflows and grant revocation.
  name: Authentik Requests API
  phrasing_intents:
  - id: requests_grant_requests_list
    intent: List access grant requests
    question: Which access grant requests have been filed, and what status are they in?
  - id: requests_grant_requests_create
    intent: Request access to resources
    question: How do I ask for temporary access to something I don't have yet?
  - id: requests_grant_requests_retrieve
    intent: Get one grant request
    question: What is the current status of a particular access request?
  - id: requests_grant_requests_destroy
    intent: Delete a grant request
    question: Can I withdraw and delete an access request I filed by mistake?
  - id: requests_grant_requests_fulfill_partial_update
    intent: Approve or deny a grant request
    question: How do I approve a pending access request as a reviewer?
  - id: requests_grant_requests_revoke_destroy
    intent: Revoke an active access grant
    question: How can I end someone's temporary access before it expires?
  - id: requests_grant_requests_agent_create
    intent: Delegate owner access to an agent
    question: Can an AI agent ask its owner for time-boxed access without running a browser flow?
  - id: requests_grant_requests_pending_review_list
    intent: List grant requests awaiting my review
    question: Which access requests am I eligible to approve right now?
  phrasing_ops: 29
  slug: authentik-requests-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Root configuration endpoint describing the running instance to its own frontend.
  name: Authentik Root API
  phrasing_intents:
  - id: root_config_retrieve
    intent: Get the public instance configuration
    question: What public configuration does my authentik instance expose to clients?
  phrasing_ops: 1
  slug: authentik-root-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: OpenID Shared Signals Framework streams — the SSF stream surface a receiving application manages on authentik as transmitter of Security Event Tokens.
  name: Authentik SSF API
  phrasing_intents:
  - id: ssf_streams_list
    intent: List Shared Signals Framework streams
    question: Which SSF event streams are currently registered in authentik?
  - id: ssf_streams_retrieve
    intent: Get one SSF stream
    question: What delivery method and endpoint does a specific SSF stream use?
  - id: ssf_streams_destroy
    intent: Delete an SSF stream
    question: Can I remove a shared signals stream a receiver no longer uses?
  phrasing_ops: 3
  slug: authentik-ssf-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Background task schedules and runs executed by the authentik worker.
  name: Authentik Tasks API
  phrasing_intents:
  - id: tasks_schedules_list
    intent: List scheduled background jobs
    question: Which recurring background jobs are scheduled in authentik?
  - id: tasks_schedules_retrieve
    intent: Get a task schedule
    question: What crontab does a specific schedule run on?
  - id: tasks_schedules_update
    intent: Replace a schedule's crontab and state
    question: Can I rewrite a schedule's full definition with a new crontab?
  - id: tasks_schedules_partial_update
    intent: Pause or retime a schedule
    question: How do I pause a recurring job without changing its timing?
  - id: tasks_schedules_send_create
    intent: Run a schedule immediately
    question: Can I trigger a scheduled job right now instead of waiting for its next run?
  - id: tasks_tasks_list
    intent: List background tasks
    question: Which background tasks have run recently, and which failed?
  - id: tasks_tasks_retrieve
    intent: Get a background task
    question: What happened when a specific background task ran?
  - id: tasks_tasks_retry_create
    intent: Retry a background task
    question: Can I re-run a task that failed?
  phrasing_ops: 10
  slug: authentik-tasks-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: Multi-tenant administration for deployments running more than one authentik tenant.
  name: Authentik Tenants API
  phrasing_intents:
  - id: tenants_domains_list
    intent: List tenant domains
    question: Which domains are mapped to tenants in my authentik install?
  - id: tenants_domains_create
    intent: Add a domain to a tenant
    question: How do I point a new domain at one of my tenants?
  - id: tenants_domains_retrieve
    intent: Get a tenant domain
    question: Which tenant does a given domain record belong to?
  - id: tenants_domains_update
    intent: Replace a tenant domain
    question: Can I fully rewrite an existing tenant domain record?
  - id: tenants_domains_partial_update
    intent: Edit fields on a tenant domain
    question: Can I just flip which tenant domain is primary without resending everything?
  - id: tenants_domains_destroy
    intent: Remove a tenant domain
    question: Can I detach a domain from its tenant?
  - id: tenants_tenants_list
    intent: List tenants
    question: What tenants exist on my multi-tenant authentik deployment?
  - id: tenants_tenants_create
    intent: Create a tenant
    question: How do I spin up a new tenant with its own database schema?
  phrasing_ops: 14
  slug: authentik-tenants-api
- baseURL: https://{authentik_host}/api/v3
  baseurl_source: declared
  description: The oauth2 API from Authentik — 9 operation(s) for oauth2.
  name: Authentik Oauth2 API
  phrasing_intents:
  - id: oauth2_access_tokens_list
    intent: List issued OAuth2 access tokens
    question: Which OAuth2 access tokens has authentik issued to a given user?
  - id: oauth2_access_tokens_retrieve
    intent: Get one OAuth2 access token
    question: Which user and provider does a particular access token belong to?
  - id: oauth2_access_tokens_destroy
    intent: Revoke an OAuth2 access token
    question: How do I kill an access token that was leaked?
  - id: oauth2_access_tokens_used_by_list
    intent: See what references an access token
    question: Is anything in authentik still referencing this access token?
  - id: oauth2_authorization_codes_list
    intent: List OAuth2 authorization codes
    question: Which authorization codes are outstanding for a user?
  - id: oauth2_authorization_codes_retrieve
    intent: Get one OAuth2 authorization code
    question: Which user and client is a specific authorization code tied to?
  - id: oauth2_authorization_codes_destroy
    intent: Delete an OAuth2 authorization code
    question: Can I invalidate an authorization code before a client exchanges it?
  - id: oauth2_authorization_codes_used_by_list
    intent: See what references an authorization code
    question: Which objects still point at a given authorization code?
  phrasing_ops: 12
  slug: authentik-oauth2-api
artifact_total: 49
asyncapis:
- description: ''
  name: Authentik Events Webhooks
  slug: authentik-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/overlays/authentik-oauth2-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/authentik-oauth2-api-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/goauthentik/authentik/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/goauthentik/authentik/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/goauthentik/authentik/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/goauthentik/authentik/blob/main/CONTRIBUTING.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/agentic-access/authentik-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/authentik-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/security/authentik-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/authentik-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/security/authentik-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/authentik-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/authentication/authentik-authentication.yml
  title: ''
  type: Authentication
  url: authentication/authentik-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/authentik-security
- group: company
  title: ''
  type: Website
  url: https://goauthentik.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.goauthentik.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/goauthentik
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/goauthentik/authentik
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/goauthentik/authentik/releases
- group: operate
  title: ''
  type: Support
  url: https://github.com/goauthentik/authentik/discussions
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/jg33eMhnj6
- group: commercial
  title: ''
  type: Pricing
  url: https://goauthentik.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://goauthentik.io/blog/rss.xml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/packages/authentik-packages.yml
  title: ''
  type: Packages
  url: packages/authentik-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/packages/authentik-packages.yml
  title: ''
  type: SDKs
  url: packages/authentik-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/well-known/authentik-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/authentik-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/well-known/authentik-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/authentik-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/llms/authentik-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/authentik-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/conformance/authentik-conformance.yml
  title: ''
  type: Conformance
  url: conformance/authentik-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/conformance/authentik-conformance.yml
  title: ''
  type: Compliance
  url: conformance/authentik-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/errors/authentik-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/authentik-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/lifecycle/authentik-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/authentik-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.goauthentik.io
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/lifecycle/authentik-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/authentik-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/security/authentik-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/authentik-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/conventions/authentik-conventions.yml
  title: ''
  type: Conventions
  url: conventions/authentik-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/changelog/authentik-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/authentik-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/cli/authentik-cli.yml
  title: ''
  type: CLI
  url: cli/authentik-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/components/authentik-components.yml
  title: ''
  type: Components
  url: components/authentik-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/data-model/authentik-data-model.yml
  title: ''
  type: DataModel
  url: data-model/authentik-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/asyncapi/authentik-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/authentik-events-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/plans/authentik-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/authentik-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/rate-limits/authentik-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/authentik-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/finops/authentik-finops.yml
  title: ''
  type: FinOps
  url: finops/authentik-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.goauthentik.io/developer-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.goauthentik.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.goauthentik.io/install-config/
- group: start
  title: ''
  type: SignUp
  url: https://customers.goauthentik.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://goauthentik.io/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://goauthentik.io/legal/privacy-policy/
created: '2026-03-25'
description: Authentik is an open source identity provider from Authentik Security Inc., a public benefit company, exposing a 1,193-operation REST API at /api/v3 on every self-hosted instance. The published OpenAPI covers users, groups, applications, tokens, RBAC, flows, stages, policies, property mappings, outposts, events, blueprints, endpoint devices, privileged access management and agent accounts. authentik speaks OAuth2/OIDC (OpenID Certified), SAML 2.0, SCIM 2.0, LDAP, RADIUS, Kerberos, Proxy and the OpenID Shared Signals Framework, and ships first-party API clients for TypeScript, Python, Go and Rust plus a Terraform provider and the `ak` CLI.
features:
- description: Full REST API covering all authentik features with built-in Swagger UI at /api/v3/ on every instance.
  name: Comprehensive REST API
- description: Native support for OAuth2, OIDC, SAML, LDAP, SCIM, RADIUS, and SSTP protocols for broad integration coverage.
  name: Multi-Protocol Support
- description: Customizable authentication and enrollment flows with visual flow designer for configuring multi-step authentication processes.
  name: Flow Engine
- description: Official API client SDKs in TypeScript, Python, Go, Rust, Kotlin, and Swift auto-generated from the OpenAPI schema.
  name: Multi-Language SDKs
- description: Official Terraform provider for infrastructure-as-code management of authentik resources.
  name: Terraform Provider
- description: Official Helm chart for Kubernetes deployment with configurable replicas, persistence, and external database support.
  name: Helm Deployment
- description: Role-based access control for granular permission management across authentik resources and administrative functions.
  name: RBAC
finops:
- name: Authentik Finops
  service_category: API
  slug: authentik-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/authentik.png
layout: provider
modified: '2026-09-16'
name: Authentik
nav: Providers
network: true
overview: 'Authentik publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Core API, Crypto API, Events API, and 24 more. Tagged areas include Authentication, Authorization, Identity Provider, LDAP, and Open Source.


  The Authentik catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Authentik''s developer surface includes authentication, documentation, changelog, support, pricing, engineering blog, CLI, and 40 more developer resources.'
plans:
- name: Authentik Plans Pricing
  plan_count: 3
  slug: authentik-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Authentik Rate Limits
  slug: authentik-rate-limits
score:
  band: exemplar
  composite: 71.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 56.8
    developer_ergonomics: 82.7
    discoverability: 73.2
    operational_transparency: 60.5
  previous_composite: 71.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/authentik/refs/heads/main/screenshots/authentik-2026-06-20T172603.png
security:
- kind: authentication
  name: Authentik Authentication
  slug: authentik-authentication
  summary_line: http · 4 schemes
- kind: domain-security
  name: Authentik Domain Security
  slug: authentik-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Authentik Vulnerability Disclosure
  slug: authentik-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: authentik
solutions:
- description: Complete identity and access management platform deployable on any infrastructure with no vendor lock-in.
  name: Self-Hosted IAM
- description: Secure and authenticate any application using forward auth with optional MFA and per-user access policies.
  name: Application Gateway
tags:
- Authentication
- Authorization
- Identity Provider
- LDAP
- Open Source
- OpenID Connect
- SAML
- SCIM
- Self-Hosted
- Identity Federation
use_cases:
- description: Deploy a complete identity provider on-premises or in private cloud with full data sovereignty.
  name: Self-Hosted Identity Provider
- description: Provide single sign-on for all internal applications using OIDC, SAML, or LDAP protocol support.
  name: SSO Gateway
- description: Build customer-facing registration and authentication flows with customizable enrollment and recovery processes.
  name: B2C Identity
- description: Implement zero trust application access with forward auth proxy integration and per-application policies.
  name: Zero Trust Access
website: https://goauthentik.io
---
