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
    error_semantics: false
    event_surface_described: false
    idempotency: documented
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 151
  human_in_the_loop: 0
  name: Microsoft Azure Api Management Agentic Access
  operation_count: 310
  slug: microsoft-azure-api-management-agentic-access
  summary_line: 310 operations · 151 acting
api_count: 1
apis:
- description: Azure API Center is the design-time governance and centralized discovery counterpart to Azure API Management. It enables organizations to track all of their APIs - regardless of type, lifecycle stage,
  name: Azure API Center
  slug: azure-api-center
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The AI API from Microsoft Azure API Management — 3 operation(s) for ai.
  name: Microsoft Azure API Management AI API
  phrasing_intents:
  - id: AIGateway_ChatCompletions
    intent: Send a chat completion through the AI gateway
    question: How do I send chat messages to an Azure OpenAI deployment through API Management's AI gateway?
  - id: AIGateway_Completions
    intent: Complete a text prompt through the AI gateway
    question: Can I send a plain text prompt, not chat messages, to an AI backend via the gateway?
  - id: AIGateway_Embeddings
    intent: Create embeddings through the AI gateway
    question: How do I generate vector embeddings for text through the API Management gateway?
  phrasing_ops: 3
  slug: microsoft-azure-api-management-ai-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiDiagnostic API from Microsoft Azure API Management — 2 operation(s) for apidiagnostic.
  name: Microsoft Azure API Management ApiDiagnostic API
  phrasing_intents:
  - id: ApiDiagnostic_ListByService
    intent: List an API's diagnostics
    question: Which diagnostic settings are configured on one of my APIs?
  - id: ApiDiagnostic_GetEntityTag
    intent: Get an API diagnostic's ETag
    question: Can I read an API diagnostic's ETag without its full body?
  - id: ApiDiagnostic_Get
    intent: Get one diagnostic on an API
    question: How do I see how a particular diagnostic on an API is configured?
  - id: ApiDiagnostic_CreateOrUpdate
    intent: Create or replace an API diagnostic
    question: How do I turn on request logging for a single API?
  - id: ApiDiagnostic_Update
    intent: Update an API diagnostic
    question: Can I change the sampling rate on an existing API diagnostic without recreating it?
  - id: ApiDiagnostic_Delete
    intent: Delete a diagnostic from an API
    question: How can I stop logging on an API by removing its diagnostic?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-apidiagnostic-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiIssue API from Microsoft Azure API Management — 2 operation(s) for apiissue.
  name: Microsoft Azure API Management ApiIssue API
  phrasing_intents:
  - id: ApiIssue_ListByService
    intent: List issues reported against an API
    question: What issues have developers raised about one of my APIs?
  - id: ApiIssue_GetEntityTag
    intent: Check an API issue's ETag
    question: How do I get the ETag of an API issue before editing it?
  - id: ApiIssue_Get
    intent: Get one issue on an API
    question: How do I read the full details of a single issue filed on an API?
  - id: ApiIssue_CreateOrUpdate
    intent: Report a new issue on an API
    question: How do I file an issue against an API in API Management?
  - id: ApiIssue_Update
    intent: Update an existing API issue
    question: Can I change the state of an issue, for example to resolved?
  - id: ApiIssue_Delete
    intent: Delete an issue from an API
    question: Can I remove an issue that was filed on an API by mistake?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-apiissue-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiManagementOperations API from Microsoft Azure API Management — 1 operation(s) for apimanagementoperations.
  name: Microsoft Azure API Management ApiManagementOperations API
  phrasing_intents:
  - id: ApiManagementOperations_List
    intent: List the API Management provider's REST operations
    question: What REST operations does the Microsoft.ApiManagement resource provider support?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-apimanagementoperations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiManagementService API from Microsoft Azure API Management — 10 operation(s) for apimanagementservice.
  name: Microsoft Azure API Management ApiManagementService API
  phrasing_intents:
  - id: ApiManagementService_CheckNameAvailability
    intent: Check if an API Management service name is free
    question: Is the name I want for a new Azure API Management service already taken?
  - id: ApiManagementService_GetDomainOwnershipIdentifier
    intent: Get the custom domain ownership identifier
    question: Where do I find the ownership identifier to prove I own a custom domain for API Management?
  - id: ApiManagementService_List
    intent: List all API Management services in a subscription
    question: Which API Management instances exist across my whole Azure subscription?
  - id: ApiManagementService_ListByResourceGroup
    intent: List API Management services in a resource group
    question: What API Management instances live in one particular resource group?
  - id: ApiManagementService_CreateOrUpdate
    intent: Create or replace an API Management service
    question: How do I provision a new Azure API Management instance?
  - id: ApiManagementService_Update
    intent: Update settings on an existing API Management service
    question: Can I change the pricing tier of an API Management instance that already exists?
  - id: ApiManagementService_Get
    intent: Get an API Management service's details
    question: How do I look up the configuration of one API Management instance?
  - id: ApiManagementService_Delete
    intent: Delete an API Management service
    question: Can I tear down an API Management instance I no longer use?
  phrasing_ops: 13
  slug: microsoft-azure-api-management-apimanagementservice-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiManagementServiceSkus API from Microsoft Azure API Management — 1 operation(s) for apimanagementserviceskus.
  name: Microsoft Azure API Management ApiManagementServiceSkus API
  phrasing_intents:
  - id: ApiManagementServiceSkus_ListAvailableServiceSkus
    intent: List SKUs available to my service
    question: Which pricing tiers can my API Management service be moved to?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-apimanagementserviceskus-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiOperation API from Microsoft Azure API Management — 2 operation(s) for apioperation.
  name: Microsoft Azure API Management ApiOperation API
  phrasing_intents:
  - id: ApiOperation_ListByApi
    intent: List an API's operations
    question: Which operations does one of my APIs expose in API Management?
  - id: ApiOperation_GetEntityTag
    intent: Get an API operation's ETag
    question: Can I read an operation's ETag before editing it?
  - id: ApiOperation_Get
    intent: Get one operation of an API
    question: How do I see the method, URL template and responses of a single API operation?
  - id: ApiOperation_CreateOrUpdate
    intent: Add or replace an API operation
    question: How do I add a new endpoint to an existing API?
  - id: ApiOperation_Update
    intent: Update an API operation
    question: Can I change just the display name or description of an existing operation?
  - id: ApiOperation_Delete
    intent: Delete an operation from an API
    question: How can I remove an endpoint from one of my APIs?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-apioperation-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiOperationsByTag API from Microsoft Azure API Management — 1 operation(s) for apioperationsbytag.
  name: Microsoft Azure API Management ApiOperationsByTag API
  phrasing_intents:
  - id: Operation_ListByTags
    intent: List an API's operations grouped by tag
    question: How can I see an API's operations organized by the tags assigned to them?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-apioperationsbytag-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiPolicy API from Microsoft Azure API Management — 2 operation(s) for apipolicy.
  name: Microsoft Azure API Management ApiPolicy API
  phrasing_intents:
  - id: ApiPolicy_ListByApi
    intent: List the policies set on an API
    question: What policies are applied at the level of one API?
  - id: ApiPolicy_GetEntityTag
    intent: Check an API policy's ETag
    question: How do I get the ETag of an API's policy before overwriting it?
  - id: ApiPolicy_Get
    intent: Get an API's policy document
    question: How do I read the XML policy that runs for one API?
  - id: ApiPolicy_CreateOrUpdate
    intent: Set the policy on an API
    question: How do I add rate limiting or header rewrites to a single API?
  - id: ApiPolicy_Delete
    intent: Remove the policy from an API
    question: Can I strip all policies off one API?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-apipolicy-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiRelease API from Microsoft Azure API Management — 2 operation(s) for apirelease.
  name: Microsoft Azure API Management ApiRelease API
  phrasing_intents:
  - id: ApiRelease_ListByService
    intent: List the releases of an API
    question: What releases have been made for one of my APIs?
  - id: ApiRelease_GetEntityTag
    intent: Check an API release's ETag
    question: How do I get the ETag of an API release?
  - id: ApiRelease_Get
    intent: Get an API release
    question: How do I see the notes and revision behind a specific API release?
  - id: ApiRelease_CreateOrUpdate
    intent: Create a release for an API
    question: How do I release an API revision so it becomes current?
  - id: ApiRelease_Update
    intent: Update an API release's details
    question: Can I edit the release notes on an existing API release?
  - id: ApiRelease_Delete
    intent: Delete an API release
    question: Can I delete a release from an API's history?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-apirelease-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiRevision API from Microsoft Azure API Management — 1 operation(s) for apirevision.
  name: Microsoft Azure API Management ApiRevision API
  phrasing_intents:
  - id: ApiRevision_ListByService
    intent: List the revisions of an API
    question: What revisions exist for one of my APIs, and which one is current?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-apirevision-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiSchema API from Microsoft Azure API Management — 2 operation(s) for apischema.
  name: Microsoft Azure API Management ApiSchema API
  phrasing_intents:
  - id: ApiSchema_ListByApi
    intent: List the schemas of an API
    question: Which schemas are attached to one of my APIs?
  - id: ApiSchema_GetEntityTag
    intent: Check an API schema's ETag
    question: How do I get the ETag of an API schema?
  - id: ApiSchema_Get
    intent: Get one schema from an API
    question: How do I read a specific schema document that belongs to an API?
  - id: ApiSchema_CreateOrUpdate
    intent: Add or replace a schema on an API
    question: How do I attach a schema definition to an API?
  - id: ApiSchema_Delete
    intent: Delete a schema from an API
    question: Can I remove a schema that an API no longer uses?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-apischema-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiTag API from Microsoft Azure API Management — 2 operation(s) for apitag.
  name: Microsoft Azure API Management ApiTag API
  phrasing_intents:
  - id: Tag_ListByApi
    intent: List tags on an API
    question: Which tags are attached to one of my APIs?
  - id: Tag_GetEntityStateByApi
    intent: Check a tag's version on an API
    question: Can I confirm a tag is attached to an API using only a header check?
  - id: Tag_GetByApi
    intent: Get a tag attached to an API
    question: How do I check whether a specific tag is applied to an API and see its details?
  - id: Tag_AssignToApi
    intent: Tag an API
    question: How do I attach an existing tag to an API?
  - id: Tag_DetachFromApi
    intent: Remove a tag from an API
    question: How can I untag an API without deleting the tag itself?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-apitag-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiTagDescription API from Microsoft Azure API Management — 2 operation(s) for apitagdescription.
  name: Microsoft Azure API Management ApiTagDescription API
  phrasing_intents:
  - id: ApiTagDescription_ListByService
    intent: List tag descriptions for an API
    question: What tag descriptions are defined on one of my APIs?
  - id: ApiTagDescription_GetEntityTag
    intent: Check a tag description's ETag
    question: How do I get the ETag of a tag description on an API?
  - id: ApiTagDescription_Get
    intent: Get a tag description on an API
    question: How do I read the description written for one tag on an API?
  - id: ApiTagDescription_CreateOrUpdate
    intent: Write a tag description for an API
    question: How do I document what a tag means within a specific API?
  - id: ApiTagDescription_Delete
    intent: Delete a tag description from an API
    question: Can I remove the description of a tag from an API?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-apitagdescription-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiVersionSet API from Microsoft Azure API Management — 2 operation(s) for apiversionset.
  name: Microsoft Azure API Management ApiVersionSet API
  phrasing_intents:
  - id: WorkspaceApiVersionSet_ListByService
    intent: List API version sets in a workspace
    question: Which API version sets are defined in one of my workspaces?
  - id: WorkspaceApiVersionSet_GetEntityTag
    intent: Get an API version set's ETag
    question: Can I read a version set's ETag before editing it?
  - id: WorkspaceApiVersionSet_Get
    intent: Get an API version set
    question: How do I see the versioning scheme of one version set?
  - id: WorkspaceApiVersionSet_CreateOrUpdate
    intent: Create or replace an API version set
    question: How do I set up a version set so my API can have multiple versions in API Management?
  - id: WorkspaceApiVersionSet_Update
    intent: Update an API version set
    question: Can I change a version set's name or scheme without recreating it?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-apiversionset-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiVersionSets API from Microsoft Azure API Management — 1 operation(s) for apiversionsets.
  name: Microsoft Azure API Management ApiVersionSets API
  phrasing_intents:
  - id: WorkspaceApiVersionSet_Delete
    intent: Delete an API version set in a workspace
    question: Can I remove an API version set from a workspace?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-apiversionsets-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ApiWiki API from Microsoft Azure API Management — 2 operation(s) for apiwiki.
  name: Microsoft Azure API Management ApiWiki API
  phrasing_intents:
  - id: ApiWikis_List
    intent: List an API's wikis
    question: Which wikis are attached to one of my APIs?
  - id: ApiWiki_GetEntityTag
    intent: Get an API wiki's ETag
    question: Can I read an API wiki's ETag without fetching the wiki?
  - id: ApiWiki_Get
    intent: Get an API's default wiki
    question: How do I read the default wiki documentation for an API?
  - id: ApiWiki_CreateOrUpdate
    intent: Create or replace an API's wiki
    question: How do I add wiki documentation to an API in API Management?
  - id: ApiWiki_Update
    intent: Update an API's wiki
    question: Can I change the documents in an existing API wiki without recreating it?
  - id: ApiWiki_Delete
    intent: Delete an API's wiki
    question: How can I remove the wiki from an API?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-apiwiki-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Backend API from Microsoft Azure API Management — 2 operation(s) for backend.
  name: Microsoft Azure API Management Backend API
  phrasing_intents:
  - id: Backend_ListByService
    intent: List the backends in the service
    question: Which backend services has my API Management instance been configured to call?
  - id: Backend_GetEntityTag
    intent: Check a backend's ETag
    question: How do I get a backend's current ETag?
  - id: Backend_Get
    intent: Get a backend's details
    question: How do I look up the URL and protocol of one backend?
  - id: Backend_CreateOrUpdate
    intent: Create or replace a backend
    question: How do I register a new backend service for my APIs to call?
  - id: Backend_Update
    intent: Update an existing backend
    question: Can I change just the URL or description of a backend?
  - id: Backend_Delete
    intent: Delete a backend
    question: Can I remove a backend that's no longer in use?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-backend-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The BackendReconnect API from Microsoft Azure API Management — 1 operation(s) for backendreconnect.
  name: Microsoft Azure API Management BackendReconnect API
  phrasing_intents:
  - id: Backend_Reconnect
    intent: Force the gateway to reconnect to a backend
    question: How do I make the API Management gateway open a fresh connection to a backend?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-backendreconnect-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Certificate API from Microsoft Azure API Management — 3 operation(s) for certificate.
  name: Microsoft Azure API Management Certificate API
  phrasing_intents:
  - id: Certificate_ListByService
    intent: List certificates on the service
    question: Which certificates are uploaded to my API Management service?
  - id: Certificate_GetEntityTag
    intent: Get a certificate's ETag
    question: Can I read a certificate's ETag without downloading its details?
  - id: Certificate_Get
    intent: Get a certificate's details
    question: How do I check a certificate's subject, thumbprint and expiry?
  - id: Certificate_CreateOrUpdate
    intent: Upload or replace a backend certificate
    question: How do I upload a certificate API Management uses to authenticate to my backend?
  - id: Certificate_Delete
    intent: Delete a certificate
    question: How can I remove a certificate from my service?
  - id: Certificate_RefreshSecret
    intent: Refresh a certificate from Key Vault
    question: How do I pull the latest version of a Key Vault certificate into API Management?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-certificate-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Diagnostic API from Microsoft Azure API Management — 2 operation(s) for diagnostic.
  name: Microsoft Azure API Management Diagnostic API
  phrasing_intents:
  - id: Diagnostic_ListByService
    intent: List service-wide diagnostic settings
    question: What diagnostic settings are configured across my API Management instance?
  - id: Diagnostic_GetEntityTag
    intent: Check a diagnostic's ETag
    question: How do I get the ETag of a diagnostic before changing it?
  - id: Diagnostic_Get
    intent: Get a diagnostic setting
    question: How do I see the sampling and logging settings of one diagnostic?
  - id: Diagnostic_CreateOrUpdate
    intent: Create or replace a diagnostic setting
    question: How do I turn on request logging to Application Insights for the whole service?
  - id: Diagnostic_Update
    intent: Update a diagnostic setting
    question: Can I change the sampling rate on an existing diagnostic?
  - id: Diagnostic_Delete
    intent: Delete a diagnostic setting
    question: Can I stop service-wide telemetry by removing a diagnostic?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-diagnostic-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Gateway API from Microsoft Azure API Management — 3 operation(s) for gateway.
  name: Microsoft Azure API Management Gateway API
  phrasing_intents:
  - id: Gateway_ListByService
    intent: List self-hosted gateways in the service
    question: Which gateways are registered with my API Management instance?
  - id: Gateway_GetEntityTag
    intent: Check a gateway's ETag
    question: How do I get the ETag of a gateway before editing it?
  - id: Gateway_Get
    intent: Get a gateway's details
    question: How do I look up the location and description of one gateway?
  - id: Gateway_CreateOrUpdate
    intent: Create or replace a gateway
    question: How do I register a new self-hosted gateway with API Management?
  - id: Gateway_Update
    intent: Update a gateway's details
    question: Can I change the description or location info of an existing gateway?
  - id: Gateway_Delete
    intent: Delete a gateway
    question: Can I unregister a gateway I've decommissioned?
  - id: Gateway_ProxyGet
    intent: Send a GET through the gateway to a backend
    question: How do I call a backend API through the API Management gateway with GET?
  - id: Gateway_ProxyPost
    intent: Send a POST through the gateway to a backend
    question: How do I submit data to a backend API through the gateway with POST?
  phrasing_ops: 10
  slug: microsoft-azure-api-management-gateway-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The GatewayApi API from Microsoft Azure API Management — 2 operation(s) for gatewayapi.
  name: Microsoft Azure API Management GatewayApi API
  phrasing_intents:
  - id: GatewayApi_ListByService
    intent: List the APIs served by a gateway
    question: Which APIs is a particular self-hosted gateway serving?
  - id: GatewayApi_GetEntityTag
    intent: Check if an API is on a gateway
    question: How can I tell if an API is already assigned to a gateway?
  - id: GatewayApi_CreateOrUpdate
    intent: Add an API to a gateway
    question: How do I make an API available on a self-hosted gateway?
  - id: GatewayApi_Delete
    intent: Remove an API from a gateway
    question: Can I stop a gateway from serving a particular API?
  phrasing_ops: 4
  slug: microsoft-azure-api-management-gatewayapi-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The GatewayCertificateAuthority API from Microsoft Azure API Management — 2 operation(s) for gatewaycertificateauthority.
  name: Microsoft Azure API Management GatewayCertificateAuthority API
  phrasing_intents:
  - id: GatewayCertificateAuthority_ListByService
    intent: List a gateway's certificate authorities
    question: Which certificate authorities are trusted by one of my self-hosted gateways?
  - id: GatewayCertificateAuthority_GetEntityTag
    intent: Check if a certificate is a gateway CA
    question: How can I tell whether a certificate is already assigned as a gateway CA?
  - id: GatewayCertificateAuthority_Get
    intent: Get a gateway certificate authority
    question: How do I see whether an assigned CA is marked trusted on a gateway?
  - id: GatewayCertificateAuthority_CreateOrUpdate
    intent: Assign a certificate as a gateway CA
    question: How do I make a gateway trust a certificate as a certificate authority?
  - id: GatewayCertificateAuthority_Delete
    intent: Unassign a CA from a gateway
    question: Can I stop a gateway from trusting a certificate authority?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-gatewaycertificateauthority-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The GatewayGenerateToken API from Microsoft Azure API Management — 1 operation(s) for gatewaygeneratetoken.
  name: Microsoft Azure API Management GatewayGenerateToken API
  phrasing_intents:
  - id: Gateway_GenerateToken
    intent: Generate a gateway access token
    question: Where do I get the shared access token a self-hosted gateway needs to connect?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-gatewaygeneratetoken-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The GatewayHostnameConfiguration API from Microsoft Azure API Management — 2 operation(s) for gatewayhostnameconfiguration.
  name: Microsoft Azure API Management GatewayHostnameConfiguration API
  phrasing_intents:
  - id: GatewayHostnameConfiguration_ListByService
    intent: List a gateway's hostname configurations
    question: Which hostnames are configured on one of my self-hosted gateways?
  - id: GatewayHostnameConfiguration_GetEntityTag
    intent: Check a gateway hostname exists
    question: Can I confirm a hostname configuration exists on a gateway without fetching it?
  - id: GatewayHostnameConfiguration_Get
    intent: Get a gateway hostname configuration
    question: How do I see the settings of one hostname on a gateway?
  - id: GatewayHostnameConfiguration_CreateOrUpdate
    intent: Add or replace a gateway hostname
    question: How do I add a custom hostname to a self-hosted gateway?
  - id: GatewayHostnameConfiguration_Delete
    intent: Remove a hostname from a gateway
    question: How can I remove a hostname from a self-hosted gateway?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-gatewayhostnameconfiguration-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The GatewayInvalidateDebugCredentials API from Microsoft Azure API Management — 1 operation(s) for gatewayinvalidatedebugcredentials.
  name: Microsoft Azure API Management GatewayInvalidateDebugCredentials API
  phrasing_intents:
  - id: Gateway_InvalidateDebugCredentials
    intent: Revoke all debug credentials for a gateway
    question: How do I revoke every debug credential issued for a gateway?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-gatewayinvalidatedebugcredentials-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The GatewayListDebugCredentials API from Microsoft Azure API Management — 1 operation(s) for gatewaylistdebugcredentials.
  name: Microsoft Azure API Management GatewayListDebugCredentials API
  phrasing_intents:
  - id: Gateway_ListDebugCredentials
    intent: Create debug credentials for a gateway
    question: Can I get debug credentials to trace requests through a gateway?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-gatewaylistdebugcredentials-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The GatewayListKeys API from Microsoft Azure API Management — 1 operation(s) for gatewaylistkeys.
  name: Microsoft Azure API Management GatewayListKeys API
  phrasing_intents:
  - id: Gateway_ListKeys
    intent: Retrieve a gateway's access keys
    question: Where do I find the primary and secondary keys for a self-hosted gateway?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-gatewaylistkeys-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The GatewayListTrace API from Microsoft Azure API Management — 1 operation(s) for gatewaylisttrace.
  name: Microsoft Azure API Management GatewayListTrace API
  phrasing_intents:
  - id: Gateway_ListTrace
    intent: Fetch a gateway's collected trace
    question: Where can I read the request trace a gateway collected while debugging?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-gatewaylisttrace-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The GatewayRegenerateKey API from Microsoft Azure API Management — 1 operation(s) for gatewayregeneratekey.
  name: Microsoft Azure API Management GatewayRegenerateKey API
  phrasing_intents:
  - id: Gateway_RegenerateKey
    intent: Regenerate a gateway key
    question: How do I rotate a self-hosted gateway key if it leaked?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-gatewayregeneratekey-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The GraphQLApiResolver API from Microsoft Azure API Management — 2 operation(s) for graphqlapiresolver.
  name: Microsoft Azure API Management GraphQLApiResolver API
  phrasing_intents:
  - id: GraphQLApiResolver_ListByApi
    intent: List resolvers of a GraphQL API
    question: Which resolvers are defined on my GraphQL API in API Management?
  - id: GraphQLApiResolver_GetEntityTag
    intent: Get a GraphQL resolver's ETag
    question: Can I read a GraphQL resolver's ETag before editing it?
  - id: GraphQLApiResolver_Get
    intent: Get a GraphQL resolver
    question: How do I see how one GraphQL resolver is configured?
  - id: GraphQLApiResolver_CreateOrUpdate
    intent: Create or replace a GraphQL resolver
    question: How do I add a resolver to a GraphQL API?
  - id: GraphQLApiResolver_Update
    intent: Update a GraphQL resolver
    question: Can I change a few details on an existing GraphQL resolver without recreating it?
  - id: GraphQLApiResolver_Delete
    intent: Delete a GraphQL resolver
    question: How can I remove a resolver from my GraphQL API?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-graphqlapiresolver-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Group API from Microsoft Azure API Management — 4 operation(s) for group.
  name: Microsoft Azure API Management Group API
  phrasing_intents:
  - id: Group_ListByService
    intent: List developer groups in an API Management service
    question: Which developer groups are defined across my API Management instance?
  - id: Group_GetEntityTag
    intent: Check a service-level group's ETag
    question: How do I get the current ETag of a developer group before editing it?
  - id: Group_Get
    intent: Get a service-level developer group
    question: How do I look up the details of one developer group in APIM?
  - id: Group_CreateOrUpdate
    intent: Create or replace a service-level group
    question: How do I create a new developer group in API Management?
  - id: Group_Update
    intent: Update a service-level group
    question: Can I rename or change the description of an existing APIM group?
  - id: Group_Delete
    intent: Delete a service-level group
    question: Can I remove a developer group from my APIM instance?
  - id: WorkspaceGroup_ListByService
    intent: List groups in a workspace
    question: Which groups are defined inside one API Management workspace?
  - id: WorkspaceGroup_GetEntityTag
    intent: Check a workspace group's ETag
    question: How do I read the ETag of a workspace group for optimistic concurrency?
  phrasing_ops: 12
  slug: microsoft-azure-api-management-group-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Health API from Microsoft Azure API Management — 2 operation(s) for health.
  name: Microsoft Azure API Management Health API
  phrasing_intents:
  - id: Gateway_HealthCheck
    intent: Check gateway health
    question: Is my API Management gateway up and healthy?
  - id: SelfHostedGateway_InternalStatus
    intent: Get a self-hosted gateway's internal status
    question: How can I see detailed internal status from a self-hosted gateway container?
  phrasing_ops: 2
  slug: microsoft-azure-api-management-health-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Logger API from Microsoft Azure API Management — 2 operation(s) for logger.
  name: Microsoft Azure API Management Logger API
  phrasing_intents:
  - id: Logger_ListByService
    intent: List the loggers in the service
    question: Which loggers are set up in my API Management instance?
  - id: Logger_GetEntityTag
    intent: Check a logger's ETag
    question: How do I get the ETag of a logger?
  - id: Logger_Get
    intent: Get a logger's details
    question: How do I look up where a particular logger sends its data?
  - id: Logger_CreateOrUpdate
    intent: Create or replace a logger
    question: How do I add a logger so API Management can ship logs to Event Hubs?
  - id: Logger_Update
    intent: Update an existing logger
    question: Can I change the description or credentials of an existing logger?
  - id: Logger_Delete
    intent: Delete a logger
    question: Can I remove a logger I no longer send data to?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-logger-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The MCP API from Microsoft Azure API Management — 1 operation(s) for mcp.
  name: Microsoft Azure API Management MCP API
  phrasing_intents:
  - id: AIGateway_MCP
    intent: Send an MCP request through the AI gateway
    question: Can I call an MCP server that sits behind API Management's AI gateway?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-mcp-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The NamedValue API from Microsoft Azure API Management — 2 operation(s) for namedvalue.
  name: Microsoft Azure API Management NamedValue API
  phrasing_intents:
  - id: WorkspaceNamedValue_ListByService
    intent: List named values in a workspace
    question: Which named values are defined in one of my API Management workspaces?
  - id: WorkspaceNamedValue_GetEntityTag
    intent: Get a named value's ETag
    question: Can I read a workspace named value's ETag before updating it?
  - id: WorkspaceNamedValue_Get
    intent: Get a named value in a workspace
    question: How do I look up one named value's settings in a workspace?
  - id: WorkspaceNamedValue_CreateOrUpdate
    intent: Create or replace a named value
    question: How do I add a named value my workspace policies can reference?
  - id: WorkspaceNamedValue_Update
    intent: Update a named value in a workspace
    question: Can I change a named value's contents without recreating it?
  - id: WorkspaceNamedValue_Delete
    intent: Delete a named value from a workspace
    question: How can I remove a named value from a workspace?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-namedvalue-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Notification API from Microsoft Azure API Management — 2 operation(s) for notification.
  name: Microsoft Azure API Management Notification API
  phrasing_intents:
  - id: WorkspaceNotification_ListByService
    intent: List a workspace's notifications
    question: Which publisher notifications are configured for one of my workspaces?
  - id: WorkspaceNotification_Get
    intent: Get a workspace notification
    question: How do I see who receives a particular publisher notification in a workspace?
  - id: WorkspaceNotification_CreateOrUpdate
    intent: Set up a workspace publisher notification
    question: How do I configure a publisher notification for a workspace in API Management?
  phrasing_ops: 3
  slug: microsoft-azure-api-management-notification-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Policy API from Microsoft Azure API Management — 2 operation(s) for policy.
  name: Microsoft Azure API Management Policy API
  phrasing_intents:
  - id: Policy_ListByService
    intent: List the global policies of the service
    question: What global policy definitions apply across my whole API Management instance?
  - id: Policy_GetEntityTag
    intent: Check the global policy's ETag
    question: How do I get the ETag of the global policy before updating it?
  - id: Policy_Get
    intent: Get the global policy
    question: How do I read the global policy XML for all my APIs?
  - id: Policy_CreateOrUpdate
    intent: Set the global policy
    question: How do I apply a policy, like CORS, to every API in the service at once?
  - id: Policy_Delete
    intent: Delete the global policy
    question: Can I remove the global policy so only API-level policies apply?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-policy-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The PolicyFragment API from Microsoft Azure API Management — 2 operation(s) for policyfragment.
  name: Microsoft Azure API Management PolicyFragment API
  phrasing_intents:
  - id: WorkspacePolicyFragment_ListByService
    intent: List policy fragments in a workspace
    question: Which reusable policy fragments are defined in one of my workspaces?
  - id: WorkspacePolicyFragment_GetEntityTag
    intent: Get a policy fragment's ETag
    question: Can I read a policy fragment's ETag before editing it?
  - id: WorkspacePolicyFragment_Get
    intent: Get a policy fragment
    question: How do I read the XML of one policy fragment?
  - id: WorkspacePolicyFragment_CreateOrUpdate
    intent: Create or replace a policy fragment
    question: How do I create a reusable policy fragment in API Management?
  - id: WorkspacePolicyFragment_Delete
    intent: Delete a policy fragment
    question: How can I remove a policy fragment from a workspace?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-policyfragment-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Product API from Microsoft Azure API Management — 4 operation(s) for product.
  name: Microsoft Azure API Management Product API
  phrasing_intents:
  - id: Product_ListByService
    intent: List products on the service
    question: What products are defined across my API Management service instance?
  - id: Product_GetEntityTag
    intent: Get a service product's ETag
    question: Can I read a service product's ETag without downloading it?
  - id: Product_Get
    intent: Get a service-level product
    question: How do I see the settings of one product on my service?
  - id: Product_CreateOrUpdate
    intent: Create or replace a service product
    question: How do I create a new product to bundle APIs on my API Management service?
  - id: Product_Update
    intent: Update a service-level product
    question: Can I change just the description or state of an existing service product?
  - id: Product_Delete
    intent: Delete a service-level product
    question: How can I remove a product from my service instance?
  - id: WorkspaceProduct_ListByService
    intent: List products in a workspace
    question: Which products live inside one of my workspaces?
  - id: WorkspaceProduct_GetEntityTag
    intent: Get a workspace product's ETag
    question: Can I read a workspace product's ETag without its full body?
  phrasing_ops: 12
  slug: microsoft-azure-api-management-product-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ProductApiLink API from Microsoft Azure API Management — 2 operation(s) for productapilink.
  name: Microsoft Azure API Management ProductApiLink API
  phrasing_intents:
  - id: ProductApiLink_ListByProduct
    intent: List API links on a product
    question: Which APIs are linked into one of my products?
  - id: ProductApiLink_Get
    intent: Get a product's API link
    question: How do I look up one API link on a product?
  - id: ProductApiLink_CreateOrUpdate
    intent: Add an API to a product
    question: How do I add an API to a product in API Management?
  - id: ProductApiLink_Delete
    intent: Remove an API from a product
    question: How can I take an API out of a product without deleting the API?
  phrasing_ops: 4
  slug: microsoft-azure-api-management-productapilink-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ProductGroupLink API from Microsoft Azure API Management — 2 operation(s) for productgrouplink.
  name: Microsoft Azure API Management ProductGroupLink API
  phrasing_intents:
  - id: ProductGroupLink_ListByProduct
    intent: List group links on a product
    question: Which groups can see one of my products?
  - id: ProductGroupLink_Get
    intent: Get a product's group link
    question: How do I look up one group link on a product?
  - id: ProductGroupLink_CreateOrUpdate
    intent: Give a group access to a product
    question: How do I make a product visible to a group of developers?
  - id: ProductGroupLink_Delete
    intent: Remove a group from a product
    question: How can I stop a group from seeing a product?
  phrasing_ops: 4
  slug: microsoft-azure-api-management-productgrouplink-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ProductPolicy API from Microsoft Azure API Management — 2 operation(s) for productpolicy.
  name: Microsoft Azure API Management ProductPolicy API
  phrasing_intents:
  - id: ProductPolicy_ListByProduct
    intent: List the policies on a product
    question: What policies are applied at the product level?
  - id: ProductPolicy_GetEntityTag
    intent: Check a product policy's ETag
    question: How do I get the ETag of a product's policy?
  - id: ProductPolicy_Get
    intent: Get a product's policy document
    question: How do I read the quota or rate-limit policy on a product?
  - id: ProductPolicy_CreateOrUpdate
    intent: Set the policy on a product
    question: How do I put a call quota on everyone subscribed to a product?
  - id: ProductPolicy_Delete
    intent: Remove the policy from a product
    question: Can I take the quota and rate limits off a product?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-productpolicy-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ProductSubscription API from Microsoft Azure API Management — 1 operation(s) for productsubscription.
  name: Microsoft Azure API Management ProductSubscription API
  phrasing_intents:
  - id: ProductSubscriptions_List
    intent: List subscriptions to a product
    question: Who is subscribed to one of my API products?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-productsubscription-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The ProductWiki API from Microsoft Azure API Management — 2 operation(s) for productwiki.
  name: Microsoft Azure API Management ProductWiki API
  phrasing_intents:
  - id: ProductWikis_list
    intent: List the wikis for a product
    question: Which wiki pages exist for one of my API products?
  - id: ProductWiki_GetEntityTag
    intent: Check a product wiki's ETag
    question: How do I get the ETag of a product's wiki?
  - id: ProductWiki_Get
    intent: Get a product's wiki
    question: How do I read the documentation wiki of a product?
  - id: ProductWiki_CreateOrUpdate
    intent: Create or replace a product's wiki
    question: How do I add a documentation wiki to an API product?
  - id: ProductWiki_Update
    intent: Update a product's wiki
    question: Can I edit only part of an existing product wiki?
  - id: ProductWiki_Delete
    intent: Delete a product's wiki
    question: Can I remove the wiki from a product?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-productwiki-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Schema API from Microsoft Azure API Management — 2 operation(s) for schema.
  name: Microsoft Azure API Management Schema API
  phrasing_intents:
  - id: WorkspaceGlobalSchema_ListByService
    intent: List the shared schemas in a workspace
    question: Which reusable schemas are registered in one API Management workspace?
  - id: WorkspaceGlobalSchema_GetEntityTag
    intent: Check a workspace schema's ETag
    question: How do I get the ETag of a workspace schema?
  - id: WorkspaceGlobalSchema_Get
    intent: Get a workspace schema
    question: How do I read one reusable schema from a workspace?
  - id: WorkspaceGlobalSchema_CreateOrUpdate
    intent: Create or replace a workspace schema
    question: How do I register a reusable XML or JSON schema in a workspace?
  - id: WorkspaceGlobalSchema_Delete
    intent: Delete a workspace schema
    question: Can I remove a reusable schema from a workspace?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-schema-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Subscription API from Microsoft Azure API Management — 8 operation(s) for subscription.
  name: Microsoft Azure API Management Subscription API
  phrasing_intents:
  - id: Subscription_List
    intent: List all subscriptions on the service
    question: Which subscriptions exist across my whole API Management service instance?
  - id: Subscription_GetEntityTag
    intent: Get a subscription's ETag version
    question: Can I read a service subscription's ETag without fetching the full record?
  - id: Subscription_Get
    intent: Get a service-level subscription
    question: How do I look up the details of one subscription on my API Management service?
  - id: Subscription_CreateOrUpdate
    intent: Subscribe a user to a product
    question: How do I subscribe a developer to a product on my API Management service?
  - id: Subscription_Update
    intent: Update a service-level subscription
    question: Can I change just some details of an existing service subscription, like its state or name?
  - id: Subscription_Delete
    intent: Delete a service-level subscription
    question: How can I remove a developer's subscription from the API Management service?
  - id: Subscription_ListSecrets
    intent: Show a subscription's keys
    question: Where do I find the primary and secondary keys for a subscription?
  - id: Subscription_RegeneratePrimaryKey
    intent: Regenerate a subscription's primary key
    question: How do I rotate the primary key on a subscription if it leaked?
  phrasing_ops: 16
  slug: microsoft-azure-api-management-subscription-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Tag API from Microsoft Azure API Management — 4 operation(s) for tag.
  name: Microsoft Azure API Management Tag API
  phrasing_intents:
  - id: Tag_ListByService
    intent: List tags on the service
    question: What tags are defined across my API Management service instance?
  - id: Tag_GetEntityState
    intent: Get a service tag's entity version
    question: Can I check a service tag's entity version without fetching it?
  - id: Tag_Get
    intent: Get a service-level tag
    question: How do I look up one tag's display name on the service?
  - id: Tag_CreateOrUpdate
    intent: Create a service-level tag
    question: How do I create a new tag on my service for grouping APIs?
  - id: Tag_Update
    intent: Rename a service-level tag
    question: Can I change a service tag's display name without recreating it?
  - id: Tag_Delete
    intent: Delete a service-level tag
    question: How can I remove a tag from my API Management service entirely?
  - id: WorkspaceTag_ListByService
    intent: List tags in a workspace
    question: Which tags are defined inside one of my workspaces?
  - id: WorkspaceTag_GetEntityState
    intent: Get a workspace tag's entity version
    question: Can I check a workspace tag's entity version without fetching it?
  phrasing_ops: 12
  slug: microsoft-azure-api-management-tag-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The TagApiLink API from Microsoft Azure API Management — 2 operation(s) for tagapilink.
  name: Microsoft Azure API Management TagApiLink API
  phrasing_intents:
  - id: TagApiLink_ListByProduct
    intent: List the APIs linked to a tag
    question: Which APIs carry a particular tag in my API Management service?
  - id: TagApiLink_Get
    intent: Get one tag-to-API link
    question: How do I look up a specific link between a tag and an API?
  - id: TagApiLink_CreateOrUpdate
    intent: Tag an API
    question: How do I add an API to a tag so it shows up under that category?
  - id: TagApiLink_Delete
    intent: Untag an API
    question: Can I remove an API from a tag without deleting the tag?
  phrasing_ops: 4
  slug: microsoft-azure-api-management-tagapilink-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The TagOperationLink API from Microsoft Azure API Management — 2 operation(s) for tagoperationlink.
  name: Microsoft Azure API Management TagOperationLink API
  phrasing_intents:
  - id: TagOperationLink_ListByProduct
    intent: List operations linked to a tag
    question: Which API operations are linked to one of my tags?
  - id: TagOperationLink_Get
    intent: Get a tag's operation link
    question: How do I look up one operation link on a tag?
  - id: TagOperationLink_CreateOrUpdate
    intent: Link an operation to a tag
    question: How do I tag a single API operation in API Management?
  - id: TagOperationLink_Delete
    intent: Unlink an operation from a tag
    question: How can I remove an operation from a tag?
  phrasing_ops: 4
  slug: microsoft-azure-api-management-tagoperationlink-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The TagProductLink API from Microsoft Azure API Management — 2 operation(s) for tagproductlink.
  name: Microsoft Azure API Management TagProductLink API
  phrasing_intents:
  - id: TagProductLink_ListByProduct
    intent: List the products linked to a tag
    question: Which products carry a particular tag?
  - id: TagProductLink_Get
    intent: Get one tag-to-product link
    question: How do I look up a specific link between a tag and a product?
  - id: TagProductLink_CreateOrUpdate
    intent: Tag a product
    question: How do I add a product to a tag so it's grouped with similar products?
  - id: TagProductLink_Delete
    intent: Untag a product
    question: Can I remove a product from a tag without deleting the tag?
  phrasing_ops: 4
  slug: microsoft-azure-api-management-tagproductlink-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The User API from Microsoft Azure API Management — 3 operation(s) for user.
  name: Microsoft Azure API Management User API
  phrasing_intents:
  - id: User_ListByService
    intent: List registered users
    question: Which developers are registered on my API Management service?
  - id: User_GetEntityTag
    intent: Get a user's ETag version
    question: Can I read a user's ETag before updating their account?
  - id: User_Get
    intent: Get a user's details
    question: How do I look up one registered developer's account details?
  - id: User_CreateOrUpdate
    intent: Create or replace a user
    question: How do I register a new developer account on my service?
  - id: User_Update
    intent: Update a user's details
    question: Can I change a user's name or email without recreating the account?
  - id: User_Delete
    intent: Delete a user
    question: How can I remove a developer account from API Management?
  - id: DevPortal_Profile
    intent: Open my developer portal profile
    question: Where in the developer portal do I manage my own subscriptions and API keys?
  phrasing_ops: 7
  slug: microsoft-azure-api-management-user-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Users API from Microsoft Azure API Management — 1 operation(s) for users.
  name: Microsoft Azure API Management Users API
  phrasing_intents:
  - id: User_GenerateSsoUrl
    intent: Generate a portal sign-in link for a user
    question: Can I sign a user straight into the developer portal from my own app?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-users-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Workspace API from Microsoft Azure API Management — 2 operation(s) for workspace.
  name: Microsoft Azure API Management Workspace API
  phrasing_intents:
  - id: Workspace_ListByService
    intent: List workspaces on the service
    question: Which workspaces exist in my API Management service instance?
  - id: Workspace_GetEntityTag
    intent: Get a workspace's ETag
    question: Can I read a workspace's ETag before updating it?
  - id: Workspace_Get
    intent: Get a workspace's details
    question: How do I look up one workspace's display name and description?
  - id: Workspace_CreateOrUpdate
    intent: Create or replace a workspace
    question: How do I create a new workspace for a team in API Management?
  - id: Workspace_Update
    intent: Update a workspace
    question: Can I rename a workspace or change its description in place?
  - id: Workspace_Delete
    intent: Delete a workspace
    question: How can I remove a workspace from my service instance?
  phrasing_ops: 6
  slug: microsoft-azure-api-management-workspace-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The WorkspacePolicy API from Microsoft Azure API Management — 2 operation(s) for workspacepolicy.
  name: Microsoft Azure API Management WorkspacePolicy API
  phrasing_intents:
  - id: WorkspacePolicy_ListByApi
    intent: List a workspace's policies
    question: What policy configuration is applied at the workspace level?
  - id: WorkspacePolicy_GetEntityTag
    intent: Get a workspace policy's ETag
    question: Can I read a workspace policy's ETag before changing it?
  - id: WorkspacePolicy_Get
    intent: Get a workspace policy
    question: How do I read the XML of one specific workspace policy?
  - id: WorkspacePolicy_CreateOrUpdate
    intent: Set a workspace's policy
    question: How do I apply a policy to every API in a workspace?
  - id: WorkspacePolicy_Delete
    intent: Remove a workspace's policy
    question: How can I remove the policy configuration from a workspace?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-workspacepolicy-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The APIs API from Microsoft Azure API Management — 2 operation(s) for apis.
  name: Microsoft Azure API Management APIs API
  phrasing_intents:
  - id: DevPortal_ListApis
    intent: Browse the APIs published on the developer portal
    question: What APIs can I discover on this API Management developer portal?
  - id: DevPortal_GetApi
    intent: Read an API's documentation on the portal
    question: How do I open the documentation page for one API on the developer portal?
  phrasing_ops: 2
  slug: microsoft-azure-api-management-apis-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Authentication API from Microsoft Azure API Management — 2 operation(s) for authentication.
  name: Microsoft Azure API Management Authentication API
  phrasing_intents:
  - id: DevPortal_SignIn
    intent: Open the developer portal sign-in page
    question: Where do developers sign in to the API Management portal?
  - id: DevPortal_SignUp
    intent: Open the developer portal sign-up page
    question: How does a new developer register an account on the portal?
  phrasing_ops: 2
  slug: microsoft-azure-api-management-authentication-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Portal API from Microsoft Azure API Management — 1 operation(s) for portal.
  name: Microsoft Azure API Management Portal API
  phrasing_intents:
  - id: DevPortal_Home
    intent: Open the developer portal home page
    question: Where is the landing page of the API Management developer portal?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-portal-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Products API from Microsoft Azure API Management — 1 operation(s) for products.
  name: Microsoft Azure API Management Products API
  phrasing_intents:
  - id: DevPortal_ListProducts
    intent: Browse products I can subscribe to
    question: Which API products can I subscribe to in the developer portal?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-products-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Subscriptions API from Microsoft Azure API Management — 4 operation(s) for subscriptions.
  name: Microsoft Azure API Management Subscriptions API
  phrasing_intents:
  - id: Api_ListByService
    intent: List all APIs in an API Management service
    question: What APIs are published in my API Management instance?
  - id: Api_GetEntityTag
    intent: Check a service-level API's ETag
    question: How do I fetch an API's current ETag before I update it?
  - id: Api_Get
    intent: Get a service-level API's details
    question: How do I see the path, protocols and settings of one API in APIM?
  - id: Api_CreateOrUpdate
    intent: Create or replace an API in the service
    question: How do I add a new API to my API Management instance?
  - id: Api_Update
    intent: Update an existing API in the service
    question: Can I change only a few properties on an API that already exists in APIM?
  - id: Api_Delete
    intent: Delete an API from the service
    question: Can I remove an API from API Management once it's retired?
  - id: WorkspaceApi_ListByService
    intent: List the APIs in a workspace
    question: Which APIs belong to one workspace in my API Management instance?
  - id: WorkspaceApi_GetEntityTag
    intent: Check a workspace API's ETag
    question: How do I read the ETag of an API in a workspace?
  phrasing_ops: 12
  slug: microsoft-azure-api-management-subscriptions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Api Product API from Microsoft Azure API Management — 1 operation(s) for api product.
  name: Microsoft Azure API Management Api Product API
  phrasing_intents:
  - id: ApiProduct_ListByApis
    intent: List the products an API belongs to
    question: Which products include a given API?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-api-product-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Group User API from Microsoft Azure API Management — 2 operation(s) for group user.
  name: Microsoft Azure API Management Group User API
  phrasing_intents:
  - id: GroupUser_List
    intent: List members of a group
    question: Which users belong to one of my API Management groups?
  - id: GroupUser_CheckEntityExists
    intent: Check if a user is in a group
    question: Is a particular user already a member of a group?
  - id: GroupUser_Create
    intent: Add a user to a group
    question: How do I add an existing developer to a group?
  - id: GroupUser_Delete
    intent: Remove a user from a group
    question: How can I take a developer out of a group without deleting their account?
  phrasing_ops: 4
  slug: microsoft-azure-api-management-group-user-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Product API API from Microsoft Azure API Management — 2 operation(s) for product api.
  name: Microsoft Azure API Management Product API
  phrasing_intents:
  - id: ProductApi_ListByProduct
    intent: List the APIs in a product
    question: Which APIs are bundled into one of my products?
  - id: ProductApi_CheckEntityExists
    intent: Check if an API is in a product
    question: How can I tell whether an API is already part of a product?
  - id: ProductApi_CreateOrUpdate
    intent: Add an API to a product
    question: How do I include an API in a product so subscribers can call it?
  - id: ProductApi_Delete
    intent: Remove an API from a product
    question: Can I take an API out of a product without deleting it?
  phrasing_ops: 4
  slug: microsoft-azure-api-management-product-api-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Product Group API from Microsoft Azure API Management — 2 operation(s) for product group.
  name: Microsoft Azure API Management Product Group API
  phrasing_intents:
  - id: ProductGroup_ListByProduct
    intent: List the groups that can see a product
    question: Which developer groups have visibility of one of my products?
  - id: ProductGroup_CheckEntityExists
    intent: Check if a group can see a product
    question: How can I tell whether a group already has access to a product?
  - id: ProductGroup_CreateOrUpdate
    intent: Give a developer group access to a product
    question: How do I make a product visible to a specific developer group?
  - id: ProductGroup_Delete
    intent: Remove a group's access to a product
    question: Can I hide a product from a developer group?
  phrasing_ops: 4
  slug: microsoft-azure-api-management-product-group-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Product Tag API from Microsoft Azure API Management — 2 operation(s) for product tag.
  name: Microsoft Azure API Management Product Tag API
  phrasing_intents:
  - id: Tag_ListByProduct
    intent: List tags on a product
    question: Which tags are attached to one of my products?
  - id: Tag_GetEntityStateByProduct
    intent: Check a tag's version on a product
    question: Can I confirm a tag is attached to a product using only a header check?
  - id: Tag_GetByProduct
    intent: Get a tag attached to a product
    question: How do I see the details of a specific tag on a product?
  - id: Tag_AssignToProduct
    intent: Tag a product
    question: How do I attach an existing tag to a product?
  - id: Tag_DetachFromProduct
    intent: Remove a tag from a product
    question: How can I untag a product without deleting the tag itself?
  phrasing_ops: 5
  slug: microsoft-azure-api-management-product-tag-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The User Group API from Microsoft Azure API Management — 1 operation(s) for user group.
  name: Microsoft Azure API Management User Group API
  phrasing_intents:
  - id: UserGroup_List
    intent: List the groups a user belongs to
    question: Which groups is a particular developer a member of?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-user-group-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The User Identity API from Microsoft Azure API Management — 1 operation(s) for user identity.
  name: Microsoft Azure API Management User Identity API
  phrasing_intents:
  - id: UserIdentities_List
    intent: List a user's sign-in identities
    question: Which identity providers has a developer used to sign in to the portal?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-user-identity-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The User Subscription API from Microsoft Azure API Management — 1 operation(s) for user subscription.
  name: Microsoft Azure API Management User Subscription API
  phrasing_intents:
  - id: UserSubscription_List
    intent: List a user's subscriptions
    question: Which product subscriptions does a particular developer hold?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-user-subscription-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The User Token API from Microsoft Azure API Management — 1 operation(s) for user token.
  name: Microsoft Azure API Management User Token API
  phrasing_intents:
  - id: User_GetSharedAccessToken
    intent: Get a shared access token for a user
    question: Can I issue a shared access token that authorizes a specific user?
  phrasing_ops: 1
  slug: microsoft-azure-api-management-user-token-api
arazzos:
- description: Send a chat completion through the AI gateway, then embed the same prompt for retrieval.
  name: Azure API Management AI Gateway Chat and Embed
  slug: microsoft-azure-api-management-ai-gateway-chat-and-embed-workflow
- description: Confirm an API exists, set its policy document, then read the policy back.
  name: Azure API Management Apply API Policy
  slug: microsoft-azure-api-management-apply-api-policy-workflow
- description: Confirm the service exists, trigger a backup to storage, then re-read the service state.
  name: Azure API Management Backup Service
  slug: microsoft-azure-api-management-backup-service-workflow
- description: Confirm an API exists, attach an Application Insights diagnostic, then read it back.
  name: Azure API Management Configure API Diagnostic
  slug: microsoft-azure-api-management-configure-api-diagnostic-workflow
- description: Confirm a GraphQL API exists, attach a resolver, then list the API's resolvers.
  name: Azure API Management Configure GraphQL Resolver
  slug: microsoft-azure-api-management-configure-graphql-resolver-workflow
- description: Create a logger, attach a service-wide diagnostic to it, then read the diagnostic back.
  name: Azure API Management Configure Logger and Service Diagnostic
  slug: microsoft-azure-api-management-configure-logger-diagnostic-workflow
- description: Confirm a product exists, set its policy document, then read the policy back.
  name: Azure API Management Configure Product Policy
  slug: microsoft-azure-api-management-configure-product-policy-workflow
- description: Confirm an API exists, add an operation to it, then list the API's operations.
  name: Azure API Management Define API Operation
  slug: microsoft-azure-api-management-define-api-operation-workflow
- description: Confirm a product and a group exist, then grant the group access to the product.
  name: Azure API Management Link Product to Group
  slug: microsoft-azure-api-management-link-product-group-workflow
- description: Create a workspace named value, read it back, then list the workspace named values.
  name: Azure API Management Manage Workspace Named Value
  slug: microsoft-azure-api-management-manage-workspace-named-value-workflow
- description: Create a user, confirm a group exists, add the user to the group, then list members.
  name: Azure API Management Onboard User to Group
  slug: microsoft-azure-api-management-onboard-user-to-group-workflow
- description: Register a backend, read it back, then trigger a reconnect.
  name: Azure API Management Provision Backend
  slug: microsoft-azure-api-management-provision-backend-workflow
- description: Upload a certificate, create a backend that uses it for mutual TLS, then read the backend.
  name: Azure API Management Provision Certificate for Backend
  slug: microsoft-azure-api-management-provision-certificate-backend-workflow
- description: Create a product, link an API to it, then list the product's APIs.
  name: Azure API Management Provision Product and Link API
  slug: microsoft-azure-api-management-provision-product-link-api-workflow
- description: Check a service name, create the API Management service, then poll until provisioning succeeds.
  name: Azure API Management Provision Service
  slug: microsoft-azure-api-management-provision-service-workflow
- description: Confirm a product, create a subscription against it, then retrieve the subscription keys.
  name: Azure API Management Provision Subscription and Retrieve Keys
  slug: microsoft-azure-api-management-provision-subscription-keys-workflow
- description: Create a workspace, register an API inside it, then read the workspace API back.
  name: Azure API Management Provision Workspace API
  slug: microsoft-azure-api-management-provision-workspace-api-workflow
- description: Create a workspace product, create a subscription scoped to it, then read the subscription.
  name: Azure API Management Provision Workspace Product and Subscription
  slug: microsoft-azure-api-management-provision-workspace-product-subscription-workflow
- description: Confirm an API exists, create a release for it, then list its releases.
  name: Azure API Management Publish API Release
  slug: microsoft-azure-api-management-publish-api-release-workflow
- description: Confirm an API exists, register a schema for it, then list the API's schemas.
  name: Azure API Management Register API Schema
  slug: microsoft-azure-api-management-register-api-schema-workflow
- description: Register a self-hosted gateway, link an API to it, then generate a gateway token.
  name: Azure API Management Register Gateway and Link API
  slug: microsoft-azure-api-management-register-gateway-link-api-workflow
- description: Confirm a subscription, regenerate both keys, then retrieve the new secrets.
  name: Azure API Management Rotate Subscription Keys
  slug: microsoft-azure-api-management-rotate-subscription-keys-workflow
- description: Confirm the service exists, set the global policy, then read the policy back.
  name: Azure API Management Set Global Service Policy
  slug: microsoft-azure-api-management-set-service-policy-workflow
- description: Create a tag, assign it to an API, then list the API's tags.
  name: Azure API Management Tag and Label an API
  slug: microsoft-azure-api-management-tag-api-workflow
- description: Create a tag, assign it to a product, then list the product's tags.
  name: Azure API Management Tag a Product
  slug: microsoft-azure-api-management-tag-product-workflow
- description: Find an API by identifier and update it if present, otherwise create it.
  name: Azure API Management Upsert API
  slug: microsoft-azure-api-management-upsert-api-workflow
- description: Find a product by identifier and update it if present, otherwise create it.
  name: Azure API Management Upsert Product
  slug: microsoft-azure-api-management-upsert-product-workflow
- description: Find a user by identifier and update it if present, otherwise create it.
  name: Azure API Management Upsert User
  slug: microsoft-azure-api-management-upsert-user-workflow
artifact_total: 267
collections:
- collection_type: postman
  name: Azure API Management AI Gateway
  slug: postman-microsoft-azure-api-management-ai-gateway
- collection_type: postman
  name: Azure API Management Developer Portal
  slug: postman-microsoft-azure-api-management-developer-portal
- collection_type: postman
  name: Azure API Management Gateway
  slug: postman-microsoft-azure-api-management-gateway
- collection_type: postman
  name: Azure API Management REST API
  slug: postman-microsoft-azure-api-management-rest-api
- collection_type: postman
  name: Azure API Management Self-Hosted Gateway
  slug: postman-microsoft-azure-api-management-self-hosted-gateway
- collection_type: open
  name: Azure API Management Gateway AI API
  slug: open-microsoft-azure-api-management-ai-api
- collection_type: open
  name: Azure Management Gateway AI Api API
  slug: open-microsoft-azure-api-management-api-api
- collection_type: open
  name: Azure API Management Gateway AI ApiDiagnostic API
  slug: open-microsoft-azure-api-management-apidiagnostic-api
- collection_type: open
  name: Azure API Management Gateway AI ApiIssue API
  slug: open-microsoft-azure-api-management-apiissue-api
- collection_type: open
  name: Azure API Management Gateway AI ApiManagementOperations API
  slug: open-microsoft-azure-api-management-apimanagementoperations-api
- collection_type: open
  name: Azure API Management Gateway AI ApiManagementService API
  slug: open-microsoft-azure-api-management-apimanagementservice-api
- collection_type: open
  name: Azure API Management Gateway AI ApiManagementServiceSkus API
  slug: open-microsoft-azure-api-management-apimanagementserviceskus-api
- collection_type: open
  name: Azure API Management Gateway AI ApiOperation API
  slug: open-microsoft-azure-api-management-apioperation-api
- collection_type: open
  name: Azure API Management Gateway AI ApiOperationsByTag API
  slug: open-microsoft-azure-api-management-apioperationsbytag-api
- collection_type: open
  name: Azure API Management Gateway AI ApiPolicy API
  slug: open-microsoft-azure-api-management-apipolicy-api
- collection_type: open
  name: Azure API Management Gateway AI ApiProduct API
  slug: open-microsoft-azure-api-management-apiproduct-api
- collection_type: open
  name: Azure API Management Gateway AI ApiRelease API
  slug: open-microsoft-azure-api-management-apirelease-api
- collection_type: open
  name: Azure API Management Gateway AI ApiRevision API
  slug: open-microsoft-azure-api-management-apirevision-api
- collection_type: open
  name: Azure API Management Gateway AI ApiSchema API
  slug: open-microsoft-azure-api-management-apischema-api
- collection_type: open
  name: Azure API Management Gateway AI ApiTag API
  slug: open-microsoft-azure-api-management-apitag-api
- collection_type: open
  name: Azure API Management Gateway AI ApiTagDescription API
  slug: open-microsoft-azure-api-management-apitagdescription-api
- collection_type: open
  name: Azure API Management Gateway AI ApiVersionSet API
  slug: open-microsoft-azure-api-management-apiversionset-api
- collection_type: open
  name: Azure API Management Gateway AI ApiVersionSets API
  slug: open-microsoft-azure-api-management-apiversionsets-api
- collection_type: open
  name: Azure API Management Gateway AI ApiWiki API
  slug: open-microsoft-azure-api-management-apiwiki-api
- collection_type: open
  name: Azure API Management Gateway AI Backend API
  slug: open-microsoft-azure-api-management-backend-api
- collection_type: open
  name: Azure API Management Gateway AI BackendReconnect API
  slug: open-microsoft-azure-api-management-backendreconnect-api
- collection_type: open
  name: Azure API Management Gateway AI Certificate API
  slug: open-microsoft-azure-api-management-certificate-api
- collection_type: open
  name: Azure API Management Gateway AI Diagnostic API
  slug: open-microsoft-azure-api-management-diagnostic-api
- collection_type: open
  name: Azure API Management AI Gateway API
  slug: open-microsoft-azure-api-management-gateway-api
- collection_type: open
  name: Azure API Management Gateway AI GatewayApi API
  slug: open-microsoft-azure-api-management-gatewayapi-api
- collection_type: open
  name: Azure API Management Gateway AI GatewayCertificateAuthority API
  slug: open-microsoft-azure-api-management-gatewaycertificateauthority-api
- collection_type: open
  name: Azure API Management Gateway AI GatewayGenerateToken API
  slug: open-microsoft-azure-api-management-gatewaygeneratetoken-api
- collection_type: open
  name: Azure API Management Gateway AI GatewayHostnameConfiguration API
  slug: open-microsoft-azure-api-management-gatewayhostnameconfiguration-api
- collection_type: open
  name: Azure API Management Gateway AI GatewayInvalidateDebugCredentials API
  slug: open-microsoft-azure-api-management-gatewayinvalidatedebugcredentials-api
- collection_type: open
  name: Azure API Management Gateway AI GatewayListDebugCredentials API
  slug: open-microsoft-azure-api-management-gatewaylistdebugcredentials-api
- collection_type: open
  name: Azure API Management Gateway AI GatewayListKeys API
  slug: open-microsoft-azure-api-management-gatewaylistkeys-api
- collection_type: open
  name: Azure API Management Gateway AI GatewayListTrace API
  slug: open-microsoft-azure-api-management-gatewaylisttrace-api
- collection_type: open
  name: Azure API Management Gateway AI GatewayRegenerateKey API
  slug: open-microsoft-azure-api-management-gatewayregeneratekey-api
- collection_type: open
  name: Azure API Management Gateway AI GraphQLApiResolver API
  slug: open-microsoft-azure-api-management-graphqlapiresolver-api
- collection_type: open
  name: Azure API Management Gateway AI Group API
  slug: open-microsoft-azure-api-management-group-api
- collection_type: open
  name: Azure API Management Gateway AI GroupUser API
  slug: open-microsoft-azure-api-management-groupuser-api
- collection_type: open
  name: Azure API Management Gateway AI Health API
  slug: open-microsoft-azure-api-management-health-api
- collection_type: open
  name: Azure API Management Gateway AI Logger API
  slug: open-microsoft-azure-api-management-logger-api
- collection_type: open
  name: Azure API Management Gateway AI MCP API
  slug: open-microsoft-azure-api-management-mcp-api
- collection_type: open
  name: Azure API Management Gateway AI NamedValue API
  slug: open-microsoft-azure-api-management-namedvalue-api
- collection_type: open
  name: Azure API Management Gateway AI Notification API
  slug: open-microsoft-azure-api-management-notification-api
- collection_type: open
  name: Azure API Management Gateway AI Policy API
  slug: open-microsoft-azure-api-management-policy-api
- collection_type: open
  name: Azure API Management Gateway AI PolicyFragment API
  slug: open-microsoft-azure-api-management-policyfragment-api
- collection_type: open
  name: Azure API Management Gateway AI Product API
  slug: open-microsoft-azure-api-management-product-api
- collection_type: open
  name: Azure API Management Gateway AI ProductApi API
  slug: open-microsoft-azure-api-management-productapi-api
- collection_type: open
  name: Azure API Management Gateway AI ProductApiLink API
  slug: open-microsoft-azure-api-management-productapilink-api
- collection_type: open
  name: Azure API Management Gateway AI ProductGroup API
  slug: open-microsoft-azure-api-management-productgroup-api
- collection_type: open
  name: Azure API Management Gateway AI ProductGroupLink API
  slug: open-microsoft-azure-api-management-productgrouplink-api
- collection_type: open
  name: Azure API Management Gateway AI ProductPolicy API
  slug: open-microsoft-azure-api-management-productpolicy-api
- collection_type: open
  name: Azure API Management Gateway AI ProductSubscription API
  slug: open-microsoft-azure-api-management-productsubscription-api
- collection_type: open
  name: Azure API Management Gateway AI ProductTag API
  slug: open-microsoft-azure-api-management-producttag-api
- collection_type: open
  name: Azure API Management Gateway AI ProductWiki API
  slug: open-microsoft-azure-api-management-productwiki-api
- collection_type: open
  name: Azure API Management Gateway AI Schema API
  slug: open-microsoft-azure-api-management-schema-api
- collection_type: open
  name: Azure API Management Gateway AI Subscription API
  slug: open-microsoft-azure-api-management-subscription-api
- collection_type: open
  name: Azure API Management Gateway AI Tag API
  slug: open-microsoft-azure-api-management-tag-api
- collection_type: open
  name: Azure API Management Gateway AI TagApiLink API
  slug: open-microsoft-azure-api-management-tagapilink-api
- collection_type: open
  name: Azure API Management Gateway AI TagOperationLink API
  slug: open-microsoft-azure-api-management-tagoperationlink-api
- collection_type: open
  name: Azure API Management Gateway AI TagProductLink API
  slug: open-microsoft-azure-api-management-tagproductlink-api
- collection_type: open
  name: Azure API Management Gateway AI User API
  slug: open-microsoft-azure-api-management-user-api
- collection_type: open
  name: Azure API Management Gateway AI UserGroup API
  slug: open-microsoft-azure-api-management-usergroup-api
- collection_type: open
  name: Azure API Management Gateway AI UserIdentity API
  slug: open-microsoft-azure-api-management-useridentity-api
- collection_type: open
  name: Azure API Management Gateway AI Users API
  slug: open-microsoft-azure-api-management-users-api
- collection_type: open
  name: Azure API Management Gateway AI UserSubscription API
  slug: open-microsoft-azure-api-management-usersubscription-api
- collection_type: open
  name: Azure API Management Gateway AI UserToken API
  slug: open-microsoft-azure-api-management-usertoken-api
- collection_type: open
  name: Azure API Management Gateway AI Workspace API
  slug: open-microsoft-azure-api-management-workspace-api
- collection_type: open
  name: Azure API Management Gateway AI WorkspacePolicy API
  slug: open-microsoft-azure-api-management-workspacepolicy-api
common:
- group: other
  href: https://artifacts.apis.io/microsoft-azure-api-management/overlays/microsoft-azure-api-management-ai-api-phrasing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-api-management-ai-api-phrasing-overlay.yaml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-api-management/cli/microsoft-azure-api-management-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-api-management-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/conventions/microsoft-azure-api-management-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-api-management-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/conventions/microsoft-azure-api-management-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-api-management-conventions.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/azure/api-management/breaking-changes/overview
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/lifecycle/microsoft-azure-api-management-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-api-management-lifecycle.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-api-management/integrations/microsoft-azure-api-management-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-azure-api-management-integration-edges.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/rules/microsoft-azure-api-management-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-api-management-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/rules/microsoft-azure-api-management-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-api-management-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/json-ld/microsoft-azure-api-management-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-api-management-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/vocabulary/microsoft-azure-api-management-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-api-management-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-api-management/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/data-model/microsoft-azure-api-management-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-api-management-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/conformance/microsoft-azure-api-management-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-api-management-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-api-management/llms/microsoft-azure-api-management-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-api-management-llms.txt
- group: build
  href: https://artifacts.apis.io/microsoft-azure-api-management/mcp/microsoft-azure-api-management-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-azure-api-management-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-api-management/well-known/microsoft-azure-api-management-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-api-management-www-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-api-management/well-known/microsoft-azure-api-management-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-api-management-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-api-management/hosts/microsoft-azure-api-management-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-api-management-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-api-management/vendors/microsoft-azure-api-management-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-api-management-vendors.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-api-management/vendor-facets/microsoft-azure-api-management-vendor-facets.yml
  title: ''
  type: VendorFacets
  url: vendor-facets/microsoft-azure-api-management-vendor-facets.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Azure/api-management-self-hosted-gateway/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Azure/api-management-self-hosted-gateway/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Azure/api-management-self-hosted-gateway/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Azure/api-management-self-hosted-gateway/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Azure/api-management-self-hosted-gateway/blob/main/CONTRIBUTING.md
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-api-management/agentic-access/microsoft-azure-api-management-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-api-management-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-api-management/security/microsoft-azure-api-management-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-api-management-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-api-management/security/microsoft-azure-api-management-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-api-management-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-api-management/authentication/microsoft-azure-api-management-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-api-management-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-api-management/scopes/microsoft-azure-api-management-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-api-management-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-azure-api-management/overview
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-ai-gateway-chat-and-embed-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-ai-gateway-chat-and-embed-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-apply-api-policy-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-apply-api-policy-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-backup-service-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-backup-service-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-configure-api-diagnostic-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-configure-api-diagnostic-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-configure-graphql-resolver-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-configure-graphql-resolver-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-configure-logger-diagnostic-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-configure-logger-diagnostic-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-configure-product-policy-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-configure-product-policy-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-define-api-operation-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-define-api-operation-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-link-product-group-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-link-product-group-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-manage-workspace-named-value-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-manage-workspace-named-value-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-onboard-user-to-group-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-onboard-user-to-group-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-provision-backend-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-provision-backend-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-provision-certificate-backend-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-provision-certificate-backend-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-provision-product-link-api-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-provision-product-link-api-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-provision-service-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-provision-service-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-provision-subscription-keys-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-provision-subscription-keys-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-provision-workspace-api-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-provision-workspace-api-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-provision-workspace-product-subscription-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-provision-workspace-product-subscription-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-publish-api-release-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-publish-api-release-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-register-api-schema-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-register-api-schema-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-register-gateway-link-api-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-register-gateway-link-api-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-rotate-subscription-keys-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-rotate-subscription-keys-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-set-service-policy-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-set-service-policy-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-tag-api-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-tag-api-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-tag-product-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-tag-product-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-upsert-api-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-upsert-api-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-upsert-product-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-upsert-product-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/arazzo/microsoft-azure-api-management-upsert-user-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-azure-api-management-upsert-user-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/products/api-management/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/api-management/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/api-management/get-started-create-service-instance
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/api-management/get-started-create-service-instance-cli
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/apimanagement/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/azure/api-management/authentication-authorization-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/pricing/details/api-management/
- group: other
  title: ''
  type: Tiers
  url: https://learn.microsoft.com/en-us/azure/api-management/api-management-features
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/api-management/breaking-changes/overview
- group: operate
  title: ''
  type: Support
  url: https://learn.microsoft.com/answers/tags/29/azure-api-management/
- group: start
  title: ''
  type: Console
  url: https://portal.azure.com/
- group: build
  title: ''
  type: CLI
  url: https://learn.microsoft.com/en-us/cli/azure/apim
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/apimanagement
- group: learn
  title: ''
  type: Tutorials
  url: https://learn.microsoft.com/en-us/azure/api-management/import-and-publish
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/modules/explore-api-management/
- group: auth
  title: ''
  type: Security
  url: https://learn.microsoft.com/en-us/azure/api-management/authentication-authorization-overview
- group: other
  title: ''
  type: BestPractices
  url: https://learn.microsoft.com/en-us/azure/api-management/api-management-howto-policies
- group: company
  title: ''
  type: Blog
  url: https://techcommunity.microsoft.com/t5/azure/ct-p/Azure
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/api-management-samples
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/privacystatement
- group: other
  title: ''
  type: Regions
  url: https://azure.microsoft.com/explore/global-infrastructure/products-by-region/
- group: auth
  title: ''
  type: Compliance
  url: https://learn.microsoft.com/en-us/azure/compliance/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.microsoft.com/trust-center
- group: start
  title: ''
  type: Signup
  url: https://azure.microsoft.com/free/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/azure/api-management/developer-portal-overview
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/apimanagement
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/apimanagement
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/apimanagement
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Azure/azure-sdk-for-go/tree/main/sdk/resourcemanager/apimanagement
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Azure/api-management-samples
- group: other
  title: ''
  type: PolicySnippets
  url: https://github.com/Azure/api-management-policy-snippets
- group: build
  title: ''
  type: Tools
  url: https://github.com/Azure/azure-api-management-policy-toolkit
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/Azure/API-Management/blob/master/changelogs/api-management-service.md
- group: other
  title: ''
  type: BreakingChanges
  url: https://learn.microsoft.com/en-us/azure/api-management/breaking-changes/overview
- group: other
  title: ''
  type: APICenter
  url: https://learn.microsoft.com/en-us/azure/api-center/overview
- group: build
  title: ''
  type: FoundryIntegration
  url: https://learn.microsoft.com/en-us/azure/ai-foundry/configuration/enable-ai-api-management-gateway-portal
- group: build
  title: ''
  type: AIGatewaySamples
  url: https://github.com/Azure-Samples/ai-gateway
- group: learn
  title: ''
  type: AIGatewayWorkshop
  url: https://aka.ms/ai-gateway/workshop
- group: build
  title: ''
  type: VSCodeExtension
  url: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-apimanagement
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/rules/microsoft-azure-api-management-rules.yaml
  title: ''
  type: SpectralRules
  url: rules/microsoft-azure-api-management-rules.yaml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-api-management/vocabulary/microsoft-azure-api-management-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-api-management-vocabulary.yaml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-api-management/plans/microsoft-azure-api-management-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-api-management-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-api-management/rate-limits/microsoft-azure-api-management-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-api-management-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-api-management/finops/microsoft-azure-api-management-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-api-management-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/Azure/azure-api-mcp
created: '2026-03-16'
description: Microsoft Azure API Management is a hybrid, multicloud management platform for APIs across all environments. It is composed of an API gateway (data plane), a management plane, and a developer portal, and supports the complete API lifecycle for publishing, securing, monitoring, and transforming APIs for external, partner, and internal developers. It now includes an AI gateway for governing OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, Microsoft Foundry models, Amazon Bedrock, MCP servers exposed from REST APIs or proxied from external MCP backends, and A2A agent APIs - with token rate limiting, semantic caching, content safety, backend load balancing, circuit breakers, and token emission to Application Insights. It pairs with Azure API Center for design-time inventory, governance, and discovery.
examples:
- key_count: 3
  name: Ai Gateway Chat Completion Request Example
  slug: ai-gateway-chat-completion-request-example
- key_count: 6
  name: Ai Gateway Chat Completion Response Example
  slug: ai-gateway-chat-completion-response-example
- key_count: 3
  name: Ai Gateway Completion Request Example
  slug: ai-gateway-completion-request-example
- key_count: 6
  name: Ai Gateway Completion Response Example
  slug: ai-gateway-completion-response-example
- key_count: 2
  name: Ai Gateway Embedding Request Example
  slug: ai-gateway-embedding-request-example
- key_count: 4
  name: Ai Gateway Embedding Response Example
  slug: ai-gateway-embedding-response-example
- key_count: 4
  name: Ai Gateway Mcp Request Example
  slug: ai-gateway-mcp-request-example
- key_count: 3
  name: Ai Gateway Mcp Response Example
  slug: ai-gateway-mcp-response-example
- key_count: 6
  name: Microsoft Azure Api Management Aigateway Chatcompletions Example
  slug: microsoft-azure-api-management-aigateway-chatcompletions-example
- key_count: 6
  name: Microsoft Azure Api Management Aigateway Completions Example
  slug: microsoft-azure-api-management-aigateway-completions-example
- key_count: 6
  name: Microsoft Azure Api Management Aigateway Embeddings Example
  slug: microsoft-azure-api-management-aigateway-embeddings-example
- key_count: 6
  name: Microsoft Azure Api Management Aigateway Mcp Example
  slug: microsoft-azure-api-management-aigateway-mcp-example
- key_count: 6
  name: Microsoft Azure Api Management Api Createorupdate Example
  slug: microsoft-azure-api-management-api-createorupdate-example
- key_count: 6
  name: Microsoft Azure Api Management Api Get Example
  slug: microsoft-azure-api-management-api-get-example
- key_count: 6
  name: Microsoft Azure Api Management Api Listbyservice Example
  slug: microsoft-azure-api-management-api-listbyservice-example
- key_count: 6
  name: Microsoft Azure Api Management Api Update Example
  slug: microsoft-azure-api-management-api-update-example
- key_count: 6
  name: Microsoft Azure Api Management Apidiagnostic Createorupdate Example
  slug: microsoft-azure-api-management-apidiagnostic-createorupdate-example
- key_count: 6
  name: Microsoft Azure Api Management Apidiagnostic Get Example
  slug: microsoft-azure-api-management-apidiagnostic-get-example
- key_count: 6
  name: Microsoft Azure Api Management Apidiagnostic Listbyservice Example
  slug: microsoft-azure-api-management-apidiagnostic-listbyservice-example
- key_count: 6
  name: Microsoft Azure Api Management Apimanagementoperations List Example
  slug: microsoft-azure-api-management-apimanagementoperations-list-example
- key_count: 6
  name: Microsoft Azure Api Management Apimanagementservice Checknameavailability Example
  slug: microsoft-azure-api-management-apimanagementservice-checknameavailability-example
- key_count: 6
  name: Microsoft Azure Api Management Apimanagementservice Createorupdate Example
  slug: microsoft-azure-api-management-apimanagementservice-createorupdate-example
- key_count: 6
  name: Microsoft Azure Api Management Apimanagementservice Get Example
  slug: microsoft-azure-api-management-apimanagementservice-get-example
- key_count: 6
  name: Microsoft Azure Api Management Apimanagementservice Getdomainownershipidentifier Example
  slug: microsoft-azure-api-management-apimanagementservice-getdomainownershipidentifier-example
- key_count: 6
  name: Microsoft Azure Api Management Apimanagementservice List Example
  slug: microsoft-azure-api-management-apimanagementservice-list-example
- key_count: 6
  name: Microsoft Azure Api Management Apimanagementservice Listbyresourcegroup Example
  slug: microsoft-azure-api-management-apimanagementservice-listbyresourcegroup-example
- key_count: 6
  name: Microsoft Azure Api Management Apimanagementservice Update Example
  slug: microsoft-azure-api-management-apimanagementservice-update-example
- key_count: 6
  name: Microsoft Azure Api Management Gateway Healthcheck Example
  slug: microsoft-azure-api-management-gateway-healthcheck-example
- key_count: 6
  name: Microsoft Azure Api Management Gateway Proxydelete Example
  slug: microsoft-azure-api-management-gateway-proxydelete-example
- key_count: 6
  name: Microsoft Azure Api Management Gateway Proxyget Example
  slug: microsoft-azure-api-management-gateway-proxyget-example
- key_count: 6
  name: Microsoft Azure Api Management Gateway Proxypost Example
  slug: microsoft-azure-api-management-gateway-proxypost-example
- key_count: 6
  name: Microsoft Azure Api Management Gateway Proxyput Example
  slug: microsoft-azure-api-management-gateway-proxyput-example
- key_count: 6
  name: Microsoft Azure Api Management Selfhostedgateway Healthcheck Example
  slug: microsoft-azure-api-management-selfhostedgateway-healthcheck-example
- key_count: 6
  name: Microsoft Azure Api Management Selfhostedgateway Internalstatus Example
  slug: microsoft-azure-api-management-selfhostedgateway-internalstatus-example
- key_count: 6
  name: Microsoft Azure Api Management Selfhostedgateway Proxyget Example
  slug: microsoft-azure-api-management-selfhostedgateway-proxyget-example
- key_count: 6
  name: Microsoft Azure Api Management Selfhostedgateway Proxypost Example
  slug: microsoft-azure-api-management-selfhostedgateway-proxypost-example
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Api Management Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-api-management-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-api-management.png
json_schemas:
- name: ChatCompletionRequest
  property_count: 3
  slug: ai-gateway-chat-completion-request
- name: ChatCompletionResponse
  property_count: 6
  slug: ai-gateway-chat-completion-response
- name: CompletionRequest
  property_count: 3
  slug: ai-gateway-completion-request
- name: CompletionResponse
  property_count: 6
  slug: ai-gateway-completion-response
- name: EmbeddingRequest
  property_count: 2
  slug: ai-gateway-embedding-request
- name: EmbeddingResponse
  property_count: 4
  slug: ai-gateway-embedding-response
- name: MCPRequest
  property_count: 4
  slug: ai-gateway-mcp-request
- name: MCPResponse
  property_count: 3
  slug: ai-gateway-mcp-response
- name: ApiCollection
  property_count: 3
  slug: microsoft-azure-api-management-apicollection
- name: ApiContract
  property_count: 4
  slug: microsoft-azure-api-management-apicontract
- name: ApiCreateOrUpdateParameter
  property_count: 1
  slug: microsoft-azure-api-management-apicreateorupdateparameter
- name: ApiDetail
  property_count: 6
  slug: microsoft-azure-api-management-apidetail
- name: ApiList
  property_count: 2
  slug: microsoft-azure-api-management-apilist
- name: ApiManagementServiceListResult
  property_count: 3
  slug: microsoft-azure-api-management-apimanagementservicelistresult
- name: ApiManagementServiceResource
  property_count: 6
  slug: microsoft-azure-api-management-apimanagementserviceresource
- name: ApiSummary
  property_count: 4
  slug: microsoft-azure-api-management-apisummary
- name: ChatCompletionRequest
  property_count: 3
  slug: microsoft-azure-api-management-chatcompletionrequest
- name: ChatCompletionResponse
  property_count: 6
  slug: microsoft-azure-api-management-chatcompletionresponse
- name: CompletionRequest
  property_count: 3
  slug: microsoft-azure-api-management-completionrequest
- name: CompletionResponse
  property_count: 6
  slug: microsoft-azure-api-management-completionresponse
- name: DiagnosticCollection
  property_count: 3
  slug: microsoft-azure-api-management-diagnosticcollection
- name: DiagnosticContract
  property_count: 4
  slug: microsoft-azure-api-management-diagnosticcontract
- name: DomainOwnershipIdentifierResult
  property_count: 1
  slug: microsoft-azure-api-management-domainownershipidentifierresult
- name: EmbeddingRequest
  property_count: 2
  slug: microsoft-azure-api-management-embeddingrequest
- name: EmbeddingResponse
  property_count: 4
  slug: microsoft-azure-api-management-embeddingresponse
- name: GatewayResponse
  property_count: 3
  slug: microsoft-azure-api-management-gatewayresponse
- name: HealthStatus
  property_count: 2
  slug: microsoft-azure-api-management-healthstatus
- name: InternalStatus
  property_count: 6
  slug: microsoft-azure-api-management-internalstatus
- name: MCPRequest
  property_count: 4
  slug: microsoft-azure-api-management-mcprequest
- name: MCPResponse
  property_count: 3
  slug: microsoft-azure-api-management-mcpresponse
- name: OperationListResult
  property_count: 2
  slug: microsoft-azure-api-management-operationlistresult
- name: ProductList
  property_count: 2
  slug: microsoft-azure-api-management-productlist
- name: ProductSummary
  property_count: 5
  slug: microsoft-azure-api-management-productsummary
- name: ServiceNameAvailabilityResult
  property_count: 3
  slug: microsoft-azure-api-management-servicenameavailabilityresult
- name: UserProfile
  property_count: 6
  slug: microsoft-azure-api-management-userprofile
json_structures:
- name: Ai Gateway Chat Completion Request Structure
  property_count: 3
  slug: ai-gateway-chat-completion-request-structure
- name: Ai Gateway Chat Completion Response Structure
  property_count: 6
  slug: ai-gateway-chat-completion-response-structure
- name: Ai Gateway Completion Request Structure
  property_count: 3
  slug: ai-gateway-completion-request-structure
- name: Ai Gateway Completion Response Structure
  property_count: 6
  slug: ai-gateway-completion-response-structure
- name: Ai Gateway Embedding Request Structure
  property_count: 2
  slug: ai-gateway-embedding-request-structure
- name: Ai Gateway Embedding Response Structure
  property_count: 4
  slug: ai-gateway-embedding-response-structure
- name: Ai Gateway Mcp Request Structure
  property_count: 4
  slug: ai-gateway-mcp-request-structure
- name: Ai Gateway Mcp Response Structure
  property_count: 3
  slug: ai-gateway-mcp-response-structure
- name: Microsoft Azure Api Management Structure
  property_count: 0
  slug: microsoft-azure-api-management-structure
jsonld:
- class_count: 0
  name: Microsoft Azure Api Management Ai Gateway Context
  property_count: 8
  slug: microsoft-azure-api-management-ai-gateway-context
- class_count: 29
  name: Microsoft Azure Api Management Context
  property_count: 50
  slug: microsoft-azure-api-management-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-09-16'
name: Microsoft Azure API Management
nav: Providers
network: true
overview: 'Microsoft Azure API Management publishes 71 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI API, ApiDiagnostic API, ApiIssue API, and 68 more. Tagged areas include A2A, AI Gateway, API Center, API Gateway, and API Management.


  The Microsoft Azure API Management catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  Microsoft Azure API Management''s developer surface includes CLI, authentication, documentation, getting-started guide, API reference, pricing, changelog, and 101 more developer resources.'
plans:
- name: Microsoft Azure Api Management Plans Pricing
  plan_count: 11
  slug: microsoft-azure-api-management-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 6
  name: Microsoft Azure Api Management Rate Limits
  slug: microsoft-azure-api-management-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Microsoft Azure API Management — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-azure-api-management-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Microsoft Azure API Management API Rules
  rule_count: 15
  severity_counts:
    error: 1
    hint: 0
    info: 8
    warn: 6
  slug: microsoft-azure-api-management-rules
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Microsoft Azure API Management API Rules
  rule_count: 61
  severity_counts:
    error: 50
    hint: 0
    info: 5
    warn: 6
  slug: microsoft-azure-api-management-rules
scopes:
- name: Microsoft Azure Api Management Scopes
  scope_count: 1
  slug: microsoft-azure-api-management-scopes
  summary_line: 1 scope · implicit
score:
  band: exemplar
  composite: 80.3
  coverage:
    artifact_dirs: 40
    catalog_earned: 90.0
    catalog_earned_first_party: 24.0
    catalog_gap: 25.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.1
  facets:
    access_clarity: 92.1
    contract_governance: 45.5
    contract_quality: 57.6
    developer_ergonomics: 91.1
    discoverability: 68.3
    operational_transparency: 84.2
  previous_composite: 76.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 13.5
      total: 74
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
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
screenshot: https://apis.io/screenshots/microsoft-azure-api-management/microsoft-azure-api-management-2026-08-07T172834.png
security:
- kind: authentication
  name: Microsoft Azure Api Management Authentication
  slug: microsoft-azure-api-management-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Api Management Domain Security
  slug: microsoft-azure-api-management-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Api Management Vulnerability Disclosure
  slug: microsoft-azure-api-management-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: microsoft-azure-api-management-certificate-create
  slug: microsoft-azure-api-management-certificate-create
- name: microsoft-azure-api-management-create-or-update-service
  slug: microsoft-azure-api-management-create-or-update-service
- name: microsoft-azure-api-management-gateway-create-or-update
  slug: microsoft-azure-api-management-gateway-create-or-update
slug: microsoft-azure-api-management
tags:
- A2A
- AI Gateway
- API Center
- API Gateway
- API Management
- Enterprise
- MCP
- Microsoft Azure
website: https://azure.microsoft.com/products/api-management/
---
