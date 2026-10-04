---
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
    event_surface_described: true
    idempotency: false
    mcp_server: templated
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 54.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 98
  human_in_the_loop: 5
  name: Aembit Agentic Access
  operation_count: 167
  slug: aembit-agentic-access
  summary_line: 167 operations · 98 acting · 5 human-in-the-loop
api_count: 2
apis:
- description: A first-party hosted Model Context Protocol server that gives AI agents and MCP clients read-only access to a tenant's Aembit event logs. Three tools — get_audit_logs, get_auth_events and get_workload
  name: Aembit MCP Server
  slug: aembit-mcp-server
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Access Authorization Event API from Aembit — 2 operation(s) for access authorization event.
  name: Aembit Access Authorization Event API
  phrasing_intents:
  - id: get-access-authorization-events
    intent: List access authorization events
    question: Which workload access requests were authorized or denied in the last hour?
  - id: get-access-authorization-event
    intent: Get one access authorization event
    question: What details are recorded for a single authorization decision?
  phrasing_ops: 2
  slug: aembit-access-authorization-event-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Access Condition API from Aembit — 2 operation(s) for access condition.
  name: Aembit Access Condition API
  phrasing_intents:
  - id: get-access-conditions
    intent: List access conditions
    question: Which access conditions are defined in my tenant?
  - id: post-access-condition
    intent: Create an access condition
    question: How do I create a new access condition to attach to an access policy?
  - id: put-access-condition
    intent: Replace an access condition's full definition
    question: How do I overwrite an existing access condition with a new set of rules?
  - id: get-access-condition
    intent: Get an access condition
    question: What rules does a specific access condition enforce?
  - id: delete-access-condition
    intent: Delete an access condition
    question: Can I remove an access condition I no longer need?
  - id: patch-access-condition
    intent: Rename or toggle an access condition
    question: Can I just deactivate an access condition without redefining it?
  phrasing_ops: 6
  slug: aembit-access-condition-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Access Condition v2 API from Aembit — 2 operation(s) for access condition v2.
  name: Aembit Access Condition v2 API
  phrasing_intents:
  - id: get-access-conditions2
    intent: List access conditions (v2)
    question: Which access conditions exist according to the v2 endpoint?
  - id: post-access-condition2
    intent: Create an access condition (v2)
    question: How do I create an access condition with the v2 API?
  - id: put-access-condition2
    intent: Replace an access condition (v2)
    question: How do I fully update an access condition through the v2 API?
  - id: get-access-condition2
    intent: Get an access condition (v2)
    question: What does the v2 API return for one access condition?
  - id: delete-access-condition2
    intent: Delete an access condition (v2)
    question: Can I delete an access condition through the v2 API?
  - id: patch-access-condition2
    intent: Rename or toggle an access condition (v2)
    question: Can I switch off an access condition with a v2 patch?
  phrasing_ops: 6
  slug: aembit-access-condition-v2-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Access Policy (Deprecated) API from Aembit — 4 operation(s) for access policy (deprecated).
  name: Aembit Access Policy (Deprecated) API
  phrasing_intents:
  - id: get-access-policy
    intent: Get an access policy (v1)
    question: What does an access policy connect, in the older v1 API?
  - id: delete-access-policy
    intent: Delete an access policy (v1)
    question: Can I delete an access policy using the deprecated v1 API?
  - id: patch-access-policy
    intent: Partially update an access policy (v1)
    question: Can I swap the credential provider on an existing policy without rebuilding it?
  - id: get-access-policy-by-workloads
    intent: Find the policy between two workloads (v1)
    question: Is there an access policy linking this client workload to that server workload?
  - id: get-access-policies
    intent: List access policies (v1)
    question: Which access policies exist in my tenant according to v1?
  - id: post-access-policy
    intent: Create an access policy (v1)
    question: How do I let one workload call another with a v1 access policy?
  - id: put-access-policy
    intent: Replace an access policy (v1)
    question: How do I overwrite an access policy's full configuration in v1?
  - id: post-access-policy-note
    intent: Add a note to an access policy (v1)
    question: Can I record why an access policy was changed?
  phrasing_ops: 8
  slug: aembit-access-policy-deprecated-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Access Policy v2 API from Aembit — 5 operation(s) for access policy v2.
  name: Aembit Access Policy v2 API
  phrasing_intents:
  - id: get-access-policy-v2
    intent: Get an access policy
    question: What workloads and providers does one access policy tie together?
  - id: delete-access-policy-v2
    intent: Delete an access policy
    question: Can I delete an access policy I no longer use?
  - id: patch-access-policy-v2
    intent: Partially update an access policy
    question: Can I attach several credential providers to an existing policy?
  - id: get-access-policy-by-workloads-v2
    intent: Find the policy between two workloads
    question: Which access policy governs traffic from a given client workload to a server workload?
  - id: get-access-policies-v2
    intent: List access policies
    question: Which access policies are configured right now?
  - id: post-access-policy-v2
    intent: Create an access policy
    question: How do I grant a client workload access to a server workload?
  - id: put-access-policy-v2
    intent: Replace an access policy
    question: How do I overwrite an entire access policy definition?
  - id: post-access-policy-note-v2
    intent: Add a note to an access policy
    question: How do I document a change on an access policy?
  phrasing_ops: 10
  slug: aembit-access-policy-v2-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Agent Controller API from Aembit — 3 operation(s) for agent controller.
  name: Aembit Agent Controller API
  phrasing_intents:
  - id: get-agent-controllers
    intent: List agent controllers
    question: Which agent controllers are registered in my tenant?
  - id: post-agent-controller
    intent: Create an agent controller
    question: How do I register a new agent controller?
  - id: put-agent-controller
    intent: Replace an agent controller
    question: How do I fully update an agent controller's settings?
  - id: get-agent-controller
    intent: Get an agent controller
    question: Is a particular agent controller healthy and when did it last report?
  - id: patch-agent-controller
    intent: Toggle or rebind an agent controller
    question: Can I switch an agent controller to a different trust provider?
  - id: delete-agent-controller
    intent: Delete an agent controller
    question: Can I remove an agent controller I decommissioned?
  - id: post-agent-controller-device-code
    intent: Generate a device code for an agent controller
    question: How do I get a device code to register an agent controller?
  phrasing_ops: 7
  slug: aembit-agent-controller-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Audit Log API from Aembit — 2 operation(s) for audit log.
  name: Aembit Audit Log API
  phrasing_intents:
  - id: get-audit-logs
    intent: List audit log events
    question: Who changed configuration in my tenant over the last week?
  - id: get-audit-log
    intent: Get one audit log event
    question: What exactly was changed in a specific audit event?
  phrasing_ops: 2
  slug: aembit-audit-log-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Auth API from Aembit — 1 operation(s) for auth.
  name: Aembit Auth API
  phrasing_intents:
  - id: edge-api-auth
    intent: Authenticate a workload to the Edge API
    question: How does a client workload start a session with the Aembit Edge API?
  phrasing_ops: 1
  slug: aembit-auth-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Client Workload API from Aembit — 3 operation(s) for client workload.
  name: Aembit Client Workload API
  phrasing_intents:
  - id: post-client-workload
    intent: Create a client workload
    question: How do I register a new client workload?
  - id: put-client-workload
    intent: Replace a client workload
    question: How do I fully update a client workload's identities?
  - id: get-client-workloads
    intent: List client workloads
    question: Which client workloads are defined in my tenant?
  - id: patch-client-workload
    intent: Rename, toggle or re-identify a client workload
    question: Can I change only the identities of a client workload?
  - id: get-client-workload
    intent: Get a client workload
    question: How is a specific client workload identified?
  - id: delete-client-workload
    intent: Delete a client workload
    question: Can I remove a client workload that is no longer deployed?
  - id: get-client-identifiers
    intent: List the supported client identifier types
    question: What kinds of identifiers can I use to recognize a client workload?
  phrasing_ops: 7
  slug: aembit-client-workload-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Compliance API from Aembit — 1 operation(s) for compliance.
  name: Aembit Compliance API
  phrasing_intents:
  - id: get-compliance-settings
    intent: Get global compliance settings
    question: What compliance rules apply when creating access policies?
  - id: update-compliance-setting
    intent: Change a global compliance setting
    question: How do I change one of the global compliance rules?
  phrasing_ops: 2
  slug: aembit-compliance-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Content Security API from Aembit — 2 operation(s) for content security.
  name: Aembit Content Security API
  phrasing_intents:
  - id: get-content-security
    intent: Get a content security configuration
    question: What does a specific content security configuration contain?
  - id: delete-content-security
    intent: Delete a content security configuration
    question: Can I remove a content security configuration?
  - id: patch-content-security
    intent: Rename or toggle a content security configuration
    question: Can I disable a content security configuration without deleting it?
  - id: get-content-security-list
    intent: List content security configurations
    question: Which content security configurations exist in my tenant?
  - id: post-content-security
    intent: Create a content security configuration
    question: How do I create a new content security configuration?
  - id: put-content-security
    intent: Replace a content security configuration
    question: How do I fully update a content security configuration?
  phrasing_ops: 6
  slug: aembit-content-security-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Credential Provider (Deprecated) API from Aembit — 4 operation(s) for credential provider (deprecated).
  name: Aembit Credential Provider (Deprecated) API
  phrasing_intents:
  - id: get-credential-provider
    intent: Get a credential provider (v1)
    question: What type and lifetime does a credential provider have in the v1 API?
  - id: delete-credential-provider
    intent: Delete a credential provider (v1)
    question: Can I delete a credential provider through the v1 API?
  - id: patch-credential-provider
    intent: Partially update a credential provider (v1)
    question: Can I change a credential provider's provider details without a full update in v1?
  - id: get-credential-provider-authorization
    intent: Get a credential provider's authorization URL (v1)
    question: Where do I send a user to authorize an OAuth credential provider in v1?
  - id: get-credential-providers
    intent: List credential providers (v1)
    question: Which credential providers exist according to the v1 API?
  - id: post-credential-provider
    intent: Create a credential provider (v1)
    question: How do I create a credential provider with the deprecated API?
  - id: put-credential-provider
    intent: Replace a credential provider (v1)
    question: How do I fully update a credential provider with the v1 API?
  - id: get-credential-provider-verification
    intent: Verify a credential provider (v1)
    question: Will this credential provider actually return a credential, checked through v1?
  phrasing_ops: 8
  slug: aembit-credential-provider-deprecated-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Credential Provider Integration API from Aembit — 3 operation(s) for credential provider integration.
  name: Aembit Credential Provider Integration API
  phrasing_intents:
  - id: get-credential-provider-integration
    intent: Get a credential provider integration
    question: What does a specific credential provider integration contain?
  - id: delete-credential-provider-integration
    intent: Delete a credential provider integration
    question: Can I remove a credential provider integration?
  - id: patch-credential-provider-integration
    intent: Rename or toggle a credential provider integration
    question: Can I disable a credential provider integration temporarily?
  - id: get-credential-provider-integrations
    intent: List credential provider integrations
    question: Which credential provider integrations are set up?
  - id: post-credential-provider-integration
    intent: Create a credential provider integration
    question: How do I set up a new credential provider integration?
  - id: put-credential-provider-integration
    intent: Replace a credential provider integration
    question: How do I fully update a credential provider integration?
  - id: get-credential-provider-integration-list
    intent: List credential integrations of one type
    question: Which credential integrations of a given type can I choose from?
  phrasing_ops: 7
  slug: aembit-credential-provider-integration-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Credential Provider v2 API from Aembit — 4 operation(s) for credential provider v2.
  name: Aembit Credential Provider v2 API
  phrasing_intents:
  - id: post-credential-provider2
    intent: Create a credential provider
    question: How do I create a credential provider that issues credentials to workloads?
  - id: put-credential-provider2
    intent: Replace a credential provider
    question: How do I fully update a credential provider?
  - id: get-credential-providers-v2
    intent: List credential providers
    question: Which credential providers are configured in my tenant?
  - id: get-credential-provider2
    intent: Get a credential provider
    question: What is configured on a specific credential provider?
  - id: delete-credential-provider2
    intent: Delete a credential provider
    question: Can I delete a credential provider I no longer use?
  - id: patch-credential-provider-v2
    intent: Partially update a credential provider
    question: Can I change just the type or details of a credential provider?
  - id: get-credential-provider-verification-v2
    intent: Verify a credential provider
    question: Will this credential provider successfully return a credential?
  - id: get-credential-provider-authorization-v2
    intent: Get a credential provider's authorization URL
    question: Where does a user go to authorize an OAuth credential provider?
  phrasing_ops: 8
  slug: aembit-credential-provider-v2-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Credentials API from Aembit — 1 operation(s) for credentials.
  name: Aembit Credentials API
  phrasing_intents:
  - id: edge-api-get-credentials
    intent: Get credentials for a client workload
    question: How does a client workload obtain credentials to call a server workload?
  phrasing_ops: 1
  slug: aembit-credentials-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The DiscoveryIntegration API from Aembit — 2 operation(s) for discoveryintegration.
  name: Aembit Discovery Integration API
  phrasing_intents:
  - id: get-discovery-integrations
    intent: List discovery integrations
    question: Which discovery integrations are set up to find workloads?
  - id: post-discovery-integration
    intent: Create a discovery integration
    question: How do I set up a discovery integration to find workloads automatically?
  - id: put-discovery-integration
    intent: Replace a discovery integration
    question: How do I change the sync frequency of a discovery integration?
  - id: get-discovery-integration
    intent: Get a discovery integration
    question: When did a discovery integration last sync and did it succeed?
  - id: delete-discovery-integration
    intent: Delete a discovery integration
    question: Can I remove a discovery integration?
  - id: patch-discovery-integration
    intent: Rename or toggle a discovery integration
    question: Can I pause a discovery integration without deleting it?
  phrasing_ops: 6
  slug: aembit-discoveryintegration-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The DiscoveryServerWorkloadDraft API from Aembit — 1 operation(s) for discoveryserverworkloaddraft.
  name: Aembit Discovery Server Workload Draft API
  phrasing_intents:
  - id: getApiAlphaServerWorkloadDraftsById
    intent: Get a discovered server workload draft
    question: How do I look up one server workload draft that Aembit discovery created?
  phrasing_ops: 1
  slug: aembit-discoveryserverworkloaddraft-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Health API from Aembit — 1 operation(s) for health.
  name: Aembit Health API
  phrasing_intents:
  - id: get-health
    intent: Check Aembit Cloud API health
    question: Is the Aembit Cloud API up right now?
  phrasing_ops: 1
  slug: aembit-health-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Integration API from Aembit — 2 operation(s) for integration.
  name: Aembit Integration API
  phrasing_intents:
  - id: get-integrations
    intent: List integrations
    question: Which integrations are connected to my tenant?
  - id: post-integration
    intent: Create an integration
    question: How do I connect an integration that access conditions can use?
  - id: put-integration
    intent: Replace an integration
    question: How do I change how often an integration syncs?
  - id: get-integration
    intent: Get an integration
    question: When did an integration last sync?
  - id: delete-integration
    intent: Delete an integration
    question: Can I disconnect and delete an integration?
  - id: patch-integration
    intent: Rename or toggle an integration
    question: Can I pause an integration without deleting it?
  phrasing_ops: 6
  slug: aembit-integration-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Integration v2 API from Aembit — 2 operation(s) for integration v2.
  name: Aembit Integration v2 API
  phrasing_intents:
  - id: get-integrations2
    intent: List integrations (v2)
    question: Which integrations does the v2 API return?
  - id: post-integration2
    intent: Create an integration (v2)
    question: How do I create an integration with the v2 API?
  - id: put-integration2
    intent: Replace an integration (v2)
    question: How do I fully update an integration with the v2 API?
  - id: get-integration2
    intent: Get an integration (v2)
    question: What does the v2 API return for one integration?
  - id: delete-integration2
    intent: Delete an integration (v2)
    question: Can I delete an integration through the v2 API?
  - id: patch-integration2
    intent: Rename or toggle an integration (v2)
    question: Can I switch off an integration with a v2 patch?
  phrasing_ops: 6
  slug: aembit-integration-v2-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Log Stream API from Aembit — 2 operation(s) for log stream.
  name: Aembit Log Stream API
  phrasing_intents:
  - id: get-log-streams
    intent: List log streams
    question: Where are my Aembit logs being streamed?
  - id: post-log-stream
    intent: Create a log stream
    question: How do I start exporting events to an external log destination?
  - id: put-log-stream
    intent: Replace a log stream
    question: How do I fully update a log stream's destination settings?
  - id: get-log-stream
    intent: Get a log stream
    question: What destination is a particular log stream sending to?
  - id: delete-log-stream
    intent: Delete a log stream
    question: Can I stop and remove a log stream?
  - id: patch-log-stream
    intent: Pause, rename or retag a log stream
    question: Can I pause a log stream without deleting it?
  phrasing_ops: 6
  slug: aembit-log-stream-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The MFA SignOn Policy API from Aembit — 1 operation(s) for mfa signon policy.
  name: Aembit MFA SignOn Policy API
  phrasing_intents:
  - id: put-mfa-signonPolicy
    intent: Require or relax MFA for sign-in
    question: What makes multi-factor authentication mandatory for users signing in to my tenant?
  phrasing_ops: 1
  slug: aembit-mfa-signon-policy-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Policy API from Aembit — 1 operation(s) for policy.
  name: Aembit Policy API
  phrasing_intents:
  - id: get-compliance-settings
    intent: Read the tenant's compliance settings
    question: What global rules constrain how access policies are created?
  - id: update-compliance-setting
    intent: Update one compliance setting
    question: How do I update a single global compliance setting?
  phrasing_ops: 2
  slug: aembit-policy-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Resource Set API from Aembit — 2 operation(s) for resource set.
  name: Aembit Resource Set API
  phrasing_intents:
  - id: get-resource-set
    intent: Get a resource set
    question: How many workloads and policies live in a given resource set?
  - id: patch-resource-set
    intent: Rename or toggle a resource set
    question: Can I deactivate a resource set without deleting it?
  - id: delete-resource-set-integration
    intent: Delete a resource set
    question: Can I delete a resource set I no longer use?
  - id: get-resource-sets
    intent: List resource sets
    question: Which resource sets partition my tenant?
  - id: post-resource-set
    intent: Create a resource set
    question: How do I create a resource set to isolate a team's workloads?
  - id: put-resource-set
    intent: Replace a resource set
    question: How do I change which roles and users belong to a resource set?
  phrasing_ops: 6
  slug: aembit-resource-set-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Role API from Aembit — 2 operation(s) for role.
  name: Aembit Role API
  phrasing_intents:
  - id: get-roles
    intent: List roles
    question: Which roles are defined for admin users?
  - id: post-role
    intent: Create a role
    question: How do I create a custom role for administrators?
  - id: put-role
    intent: Replace a role's permissions
    question: How do I change the permissions granted by a role?
  - id: get-role
    intent: Get a role
    question: What permissions does a specific role grant?
  - id: delete-role
    intent: Delete a role
    question: Can I delete a custom role?
  - id: patch-role
    intent: Rename or toggle a role
    question: Can I deactivate a role without deleting it?
  phrasing_ops: 6
  slug: aembit-role-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Routing API from Aembit — 2 operation(s) for routing.
  name: Aembit Routing API
  phrasing_intents:
  - id: get-routing
    intent: Get a routing
    question: Which proxy URL does a routing send traffic through?
  - id: patch-routing
    intent: Rename or toggle a routing
    question: Can I disable a routing without deleting it?
  - id: get-routings
    intent: List routings
    question: Which routings are configured in my tenant?
  - id: post-routing
    intent: Create a routing
    question: How do I route a resource set's traffic through a proxy?
  - id: put-routing
    intent: Replace a routing
    question: How do I change the proxy URL of an existing routing?
  phrasing_ops: 5
  slug: aembit-routing-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Server Workload API from Aembit — 2 operation(s) for server workload.
  name: Aembit Server Workload API
  phrasing_intents:
  - id: post-server-workload
    intent: Create a server workload
    question: How do I register a service that client workloads will call?
  - id: put-server-workload
    intent: Replace a server workload
    question: How do I change the service endpoint of a server workload?
  - id: get-server-workloads
    intent: List server workloads
    question: Which server workloads (target services) are defined?
  - id: patch-server-workload
    intent: Rename or toggle a server workload
    question: Can I deactivate a server workload without deleting it?
  - id: get-server-workload
    intent: Get a server workload
    question: What service endpoint does a specific server workload point to?
  - id: delete-server-workload
    intent: Delete a server workload
    question: Can I remove a server workload that was retired?
  phrasing_ops: 6
  slug: aembit-server-workload-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The SignOn Policy API from Aembit — 1 operation(s) for signon policy.
  name: Aembit SignOn Policy API
  phrasing_intents:
  - id: get-signon-policy
    intent: Get the sign-on policy
    question: Is MFA or SSO currently required to sign in to my tenant?
  phrasing_ops: 1
  slug: aembit-signon-policy-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The SSO Identity Provider API from Aembit — 3 operation(s) for sso identity provider.
  name: Aembit SSO Identity Provider API
  phrasing_intents:
  - id: get-identity-provider-verification
    intent: Verify an SSO identity provider
    question: Is my SSO identity provider fully configured?
  - id: get-identity-provider
    intent: Get an SSO identity provider
    question: What is configured on a specific SSO identity provider?
  - id: delete-identity-provider
    intent: Delete an SSO identity provider
    question: Can I remove an SSO identity provider?
  - id: patch-identity-provider
    intent: Rename or toggle an SSO identity provider
    question: Can I disable an SSO identity provider temporarily?
  - id: get-identity-providers
    intent: List SSO identity providers
    question: Which SSO identity providers are connected to my tenant?
  - id: post-identity-provider
    intent: Add an SSO identity provider
    question: How do I connect a new SSO identity provider?
  - id: put-identity-provider
    intent: Replace an SSO identity provider
    question: How do I fully update an SSO identity provider's settings?
  phrasing_ops: 7
  slug: aembit-sso-identity-provider-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The SSO SignOn Policy API from Aembit — 1 operation(s) for sso signon policy.
  name: Aembit SSO SignOn Policy API
  phrasing_intents:
  - id: put-SSO-signonPolicy
    intent: Require or relax SSO for sign-in
    question: Is there a way to force users to sign in through SSO?
  phrasing_ops: 1
  slug: aembit-sso-signon-policy-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Standalone Certificate Authority API from Aembit — 2 operation(s) for standalone certificate authority.
  name: Aembit Standalone Certificate Authority API
  phrasing_intents:
  - id: delete-standalone-certificate-authority
    intent: Delete a standalone certificate authority
    question: Can I delete a standalone certificate authority?
  - id: get-standalone-certificate-authority
    intent: Get a standalone certificate authority
    question: What leaf certificate lifetime does a standalone CA use?
  - id: patch-standalone-certificate-authority
    intent: Change a standalone CA's leaf lifetime or name
    question: Can I shorten the lifetime of leaf certificates issued by a standalone CA?
  - id: get-standalone-certificate-authorities
    intent: List standalone certificate authorities
    question: Which standalone certificate authorities exist?
  - id: post-standalone-certificate-authority
    intent: Create a standalone certificate authority
    question: How do I create a standalone certificate authority for a resource set?
  - id: put-standalone-certificate-authority
    intent: Replace a standalone certificate authority
    question: How do I fully update a standalone certificate authority?
  phrasing_ops: 6
  slug: aembit-standalone-certificate-authority-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Standalone TLS Decrypt API from Aembit — 1 operation(s) for standalone tls decrypt.
  name: Aembit Standalone TLS Decrypt API
  phrasing_intents:
  - id: standalone-root-ca
    intent: Download a standalone root CA certificate
    question: Where do I get the root certificate of a standalone CA for TLS Decrypt?
  phrasing_ops: 1
  slug: aembit-standalone-tls-decrypt-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The TLS Decrypt API from Aembit — 1 operation(s) for tls decrypt.
  name: Aembit TLS Decrypt API
  phrasing_intents:
  - id: root-ca
    intent: Download the tenant root CA certificate
    question: Where do I get my tenant's root CA certificate for TLS Decrypt?
  phrasing_ops: 1
  slug: aembit-tls-decrypt-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Trust Provider API from Aembit — 2 operation(s) for trust provider.
  name: Aembit Trust Provider API
  phrasing_intents:
  - id: get-trust-providers
    intent: List trust providers
    question: Which trust providers attest my workloads?
  - id: post-trust-provider
    intent: Create a trust provider
    question: How do I add a trust provider to verify workload identity?
  - id: put-trust-provider
    intent: Replace a trust provider
    question: How do I change the match rules on a trust provider?
  - id: get-trust-provider
    intent: Get a trust provider
    question: What match rules does a specific trust provider apply?
  - id: delete-trust-provider
    intent: Delete a trust provider
    question: Can I delete a trust provider no policy uses?
  - id: patch-trust-provider
    intent: Partially update a trust provider
    question: Can I rotate the certificate or symmetric key on a trust provider?
  phrasing_ops: 6
  slug: aembit-trust-provider-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Trust Provider Secret API from Aembit — 2 operation(s) for trust provider secret.
  name: Aembit Trust Provider Secret API
  phrasing_intents:
  - id: get-trust-providers-secrets
    intent: List a trust provider's secrets
    question: Which secrets are registered on a trust provider?
  - id: post-trust-provider-secret
    intent: Add a secret to a trust provider
    question: How do I add a new secret to a trust provider?
  - id: get-trust-provider-secret
    intent: Get a trust provider secret
    question: What are the details of one secret on a trust provider?
  - id: delete-trust-provider-secret
    intent: Delete a trust provider secret
    question: Can I revoke an old secret from a trust provider?
  phrasing_ops: 4
  slug: aembit-trust-provider-secret-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The User API from Aembit — 3 operation(s) for user.
  name: Aembit User API
  phrasing_intents:
  - id: get-users
    intent: List users
    question: Who has admin access to my Aembit tenant?
  - id: post-user
    intent: Invite a new user
    question: How do I add a new admin user to the tenant?
  - id: patch-user
    intent: Edit a user's contact details or status
    question: Can I change just a user's phone number?
  - id: get-user
    intent: Get a user
    question: Is a specific user locked or using two-factor?
  - id: put-user
    intent: Replace a user's profile and roles
    question: How do I change a user's roles?
  - id: delete-user
    intent: Delete a user
    question: Can I remove a user who left the team?
  - id: post-user-unlock
    intent: Unlock a locked user
    question: How do I unlock a user who got locked out?
  phrasing_ops: 7
  slug: aembit-user-api
- baseURL: https://{tenant}.aembit.io
  baseurl_source: declared
  description: The Workload Event API from Aembit — 2 operation(s) for workload event.
  name: Aembit Workload Event API
  phrasing_intents:
  - id: get-workload-events
    intent: List workload events
    question: Which workloads talked to each other in the last hour?
  - id: get-workload-event
    intent: Get one workload event
    question: What happened in a specific workload event?
  phrasing_ops: 2
  slug: aembit-workload-event-api
artifact_total: 47
asyncapis:
- description: ''
  name: Aembit Event Surface
  slug: aembit-event-surface
common:
- group: company
  title: ''
  type: Website
  url: https://aembit.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.aembit.io/dev-guide/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aembit.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.aembit.io/dev-guide/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aembit.io/get-started/quickstart/
- group: operate
  title: ''
  type: Support
  url: https://support.aembit.io/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://aembit.io/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aembit
- group: commercial
  title: ''
  type: Pricing
  url: https://aembit.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://useast2.aembit.io/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aembit.io/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aembit.io/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aembit.io/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/lifecycle/aembit-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/aembit-lifecycle.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.aembit.io/
- group: auth
  title: ''
  type: Compliance
  url: https://docs.aembit.io/get-started/security-posture/security-compliance/
- group: auth
  title: ''
  type: Security
  url: https://docs.aembit.io/get-started/security-posture/security-compliance/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/security/aembit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aembit-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/security/aembit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aembit-domain-security.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.aembit.io/changelog/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/cli/aembit-cli.yml
  title: ''
  type: CLI
  url: cli/aembit-cli.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/packages/aembit-packages.yml
  title: ''
  type: Packages
  url: packages/aembit-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/packages/aembit-packages.yml
  title: ''
  type: SDKs
  url: packages/aembit-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/mcp/aembit-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aembit-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/mcp/aembit-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aembit-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/llms/aembit-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aembit-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/agentic-access/aembit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aembit-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/authentication/aembit-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aembit-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/conventions/aembit-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aembit-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/errors/aembit-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aembit-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/lifecycle/aembit-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aembit-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/conformance/aembit-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aembit-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/data-model/aembit-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aembit-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/plans/aembit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aembit-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/rate-limits/aembit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aembit-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/sandbox/aembit-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/aembit-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://useast2.aembit.io/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/overlays/aembit-cloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aembit-cloud-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aembit/refs/heads/main/overlays/aembit-edge-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aembit-edge-overlay.yaml
created: '2026-09-09'
description: Aembit is a Workload Identity and Access Management (Workload IAM) platform for non-human identities — AI agents, applications, microservices, CI/CD pipelines, scripts and service accounts. Instead of long-lived, hard-coded secrets, Aembit cryptographically attests a workload against a Trust Provider (AWS, Azure, GCP, GitHub Actions, GitLab, Kubernetes, Terraform Cloud, OIDC, SPIFFE, Kerberos), evaluates an Access Policy with optional conditional-access signals from CrowdStrike and Wiz, and injects a short-lived credential just-in-time so the application never stores one. The platform is delivered as a SaaS control plane (Aembit Cloud) plus a distributed enforcement layer (Aembit Edge — Agent Proxy, Agent Injector, AWS Lambda extension, CLI and Edge SDKs). Aembit publishes two OpenAPI 3.1.1 contracts — the Aembit Cloud API for managing every platform resource and the Aembit Edge API for workload authentication and credential retrieval — alongside a hosted, read-only MCP Server
  for querying audit, authorization and workload events, an MCP Identity Gateway and an MCP Authorization Server for governing AI-agent access to MCP servers.
image: https://aembit.io/wp-content/uploads/2023/08/aembit-favicon-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: Aembit MCP Server
  slug: aembit-mcp-server
modified: '2026-09-09'
name: Aembit
nav: Providers
network: true
overview: 'Aembit publishes 38 APIs on the [APIs.io](https://apis.io/) network, including Access Authorization Event API, Access Condition API, Access Condition v2 API, and 35 more. Tagged areas include Security, Identity, Access Management, Workload Identity, and Non-Human Identity.


  The Aembit catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Aembit''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Aembit Plans Pricing
  plan_count: 6
  slug: aembit-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 3
  name: Aembit Rate Limits
  slug: aembit-rate-limits
score:
  band: exemplar
  composite: 72.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 60.5
    developer_ergonomics: 76.8
    discoverability: 68.3
    operational_transparency: 84.2
  previous_composite: 72.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 37
    mcp: first-party
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
security:
- kind: authentication
  name: Aembit Authentication
  slug: aembit-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Aembit Domain Security
  slug: aembit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aembit Vulnerability Disclosure
  slug: aembit-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Aembit Trust Center
  slug: aembit-trust-center
  summary_line: SOC 2, ISO 27001
slug: aembit
tags:
- Security
- Identity
- Access Management
- Workload Identity
- Non-Human Identity
- Secrets Management
- Zero Trust
- AI Agents
- MCP
- Authentication
- Authorization
- DevSecOps
- Cloud Security
website: https://aembit.io/
---
