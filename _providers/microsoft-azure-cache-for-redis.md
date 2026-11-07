---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 22
  human_in_the_loop: 3
  name: Microsoft Azure Cache For Redis Agentic Access
  operation_count: 41
  slug: microsoft-azure-cache-for-redis-agentic-access
  summary_line: 41 operations · 22 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: Operations operations
  name: microsoft-azure-cache-for-redis Operations API
  phrasing_intents:
  - id: Operations_List
    intent: List the Microsoft.Cache provider's operations
    question: What management operations does the Azure Cache for Redis resource provider support?
  phrasing_ops: 1
  slug: microsoft-azure-cache-for-redis-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The LinkedServer API from Microsoft Azure Cache For Redis — 2 operation(s) for linkedserver.
  name: Microsoft Azure Cache For Redis Linked Server API
  phrasing_intents:
  - id: LinkedServer_List
    intent: List a cache's linked geo-replication servers
    question: Which linked servers are attached to my Premium Redis cache?
  - id: LinkedServer_Get
    intent: Get details of one linked server
    question: What are the details of a specific linked server on my Redis cache?
  - id: LinkedServer_Create
    intent: Link a server to a Redis cache for geo-replication
    question: How do I set up geo-replication by linking a second Premium Redis cache?
  - id: LinkedServer_Delete
    intent: Remove a linked server from a Redis cache
    question: How do I break a geo-replication link between two Redis caches?
  phrasing_ops: 4
  slug: microsoft-azure-cache-for-redis-linkedserver-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The RedisCacheAccessPolicies API from Microsoft Azure Cache For Redis — 2 operation(s) for rediscacheaccesspolicies.
  name: Microsoft Azure Cache For Redis Redis Cache Access Policies API
  phrasing_intents:
  - id: AccessPolicy_List
    intent: List a cache's data access policies
    question: Which data access policies are defined on my Redis cache?
  - id: AccessPolicy_Get
    intent: Get one access policy's permissions
    question: What permissions does a particular access policy grant on my cache?
  - id: AccessPolicy_CreateUpdate
    intent: Create or update a custom access policy
    question: How do I define a custom data access policy for my Redis cache?
  - id: AccessPolicy_Delete
    intent: Delete a custom access policy
    question: How do I remove an access policy I no longer need from a Redis cache?
  phrasing_ops: 4
  slug: microsoft-azure-cache-for-redis-rediscacheaccesspolicies-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The RedisCacheAccessPolicyAssignments API from Microsoft Azure Cache For Redis — 2 operation(s) for rediscacheaccesspolicyassignments.
  name: Microsoft Azure Cache For Redis Redis Cache Access Policy Assignments API
  phrasing_intents:
  - id: AccessPolicyAssignment_List
    intent: List access policy assignments on a cache
    question: Which users and identities have access policies assigned on my Redis cache?
  - id: AccessPolicyAssignment_Get
    intent: Get one access policy assignment
    question: What policy and user does a specific access policy assignment link together?
  - id: AccessPolicyAssignment_CreateUpdate
    intent: Assign an access policy to a user
    question: How do I give a Microsoft Entra user data access to my Redis cache?
  - id: AccessPolicyAssignment_Delete
    intent: Revoke an access policy assignment
    question: How do I revoke a user's data access to my Redis cache?
  phrasing_ops: 4
  slug: microsoft-azure-cache-for-redis-rediscacheaccesspolicyassignments-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The RedisFirewallRules API from Microsoft Azure Cache For Redis — 2 operation(s) for redisfirewallrules.
  name: Microsoft Azure Cache For Redis Redis Firewall Rules API
  phrasing_intents:
  - id: FirewallRules_List
    intent: List a cache's firewall rules
    question: Which IP ranges are allowed through my Redis cache firewall?
  - id: FirewallRules_Get
    intent: Get one firewall rule
    question: What IP range does a specific firewall rule on my cache permit?
  - id: FirewallRules_CreateOrUpdate
    intent: Allow an IP range through the cache firewall
    question: How do I allow my office IP addresses to connect to a Redis cache?
  - id: FirewallRules_Delete
    intent: Delete a firewall rule
    question: How do I block an IP range I previously allowed into my Redis cache?
  phrasing_ops: 4
  slug: microsoft-azure-cache-for-redis-redisfirewallrules-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The RedisPatchSchedules API from Microsoft Azure Cache For Redis — 2 operation(s) for redispatchschedules.
  name: Microsoft Azure Cache For Redis Redis Patch Schedules API
  phrasing_intents:
  - id: PatchSchedules_ListByRedisResource
    intent: List a cache's patch schedules
    question: Does my Redis cache have a patch schedule configured at all?
  - id: PatchSchedules_Get
    intent: Get a cache's patching schedule
    question: When is my Redis cache scheduled to receive updates?
  - id: PatchSchedules_CreateOrUpdate
    intent: Set or replace a cache's patching schedule
    question: How do I restrict Redis cache updates to a weekend maintenance window?
  - id: PatchSchedules_Delete
    intent: Delete a cache's patching schedule
    question: How do I remove the maintenance window so patches can apply anytime?
  phrasing_ops: 4
  slug: microsoft-azure-cache-for-redis-redispatchschedules-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The RedisResources API from Microsoft Azure Cache For Redis — 11 operation(s) for redisresources.
  name: Microsoft Azure Cache For Redis Redis Resources API
  phrasing_intents:
  - id: Redis_ListBySubscription
    intent: List all Redis caches in a subscription
    question: Which Redis caches exist across my whole Azure subscription?
  - id: Redis_ListByResourceGroup
    intent: List Redis caches in a resource group
    question: What Redis caches are in a specific resource group?
  - id: Redis_Get
    intent: Get a Redis cache's details
    question: What SKU, host name and provisioning state does my Redis cache have?
  - id: Redis_Create
    intent: Create or replace a Redis cache
    question: How do I provision a new Azure Cache for Redis instance?
  - id: Redis_Update
    intent: Update settings on an existing Redis cache
    question: How do I scale or change settings on a cache without recreating it?
  - id: Redis_Delete
    intent: Delete a Redis cache
    question: How do I permanently delete an Azure Redis cache I no longer use?
  - id: Redis_ExportData
    intent: Export cache data to blob storage
    question: How do I back up my Redis data to a storage blob container?
  - id: Redis_FlushCache
    intent: Flush all keys from a cache
    question: How do I wipe every key from my Redis cache at once?
  phrasing_ops: 14
  slug: microsoft-azure-cache-for-redis-redisresources-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Subscriptions API from Microsoft Azure Cache For Redis — 2 operation(s) for subscriptions.
  name: Microsoft Azure Cache For Redis Subscriptions API
  phrasing_intents:
  - id: Redis_CheckNameAvailability
    intent: Check whether a cache name is available
    question: Is a particular Redis cache name still free to use?
  - id: AsyncOperationStatus_Get
    intent: Check the status of a long-running operation
    question: How do I find out whether a long-running cache operation has finished?
  phrasing_ops: 2
  slug: microsoft-azure-cache-for-redis-subscriptions-api
- baseURL: https://management.azure.com
  baseurl_source: declared
  description: The Private Endpoint Connections API from Microsoft Azure Cache For Redis — 2 operation(s) for private endpoint connections.
  name: Microsoft Azure Cache For Redis Private Endpoint Connections API
  phrasing_intents:
  - id: PrivateEndpointConnections_List
    intent: List a cache's private endpoint connections
    question: Which private endpoints are connected to my Redis cache?
  - id: PrivateEndpointConnections_Get
    intent: Get one private endpoint connection
    question: What is the approval state of a specific private endpoint connection on my cache?
  - id: PrivateEndpointConnections_Put
    intent: Approve or reject a private endpoint connection
    question: How do I approve a pending private endpoint connection to my Redis cache?
  - id: PrivateEndpointConnections_Delete
    intent: Delete a private endpoint connection
    question: How do I remove a private endpoint connection from my Redis cache?
  phrasing_ops: 4
  slug: microsoft-azure-cache-for-redis-private-endpoint-connections-api
artifact_total: 97
asyncapis:
- description: The four events Azure Cache for Redis publishes to Azure Event Grid. Derived by API Evangelist from Microsoft's published event catalog and payload samples at https://learn.microsoft.com/en-us/azure/e
  name: Azure Cache for Redis — Event Grid events
  slug: microsoft-azure-cache-for-redis-events-asyncapi
- description: ''
  name: Microsoft Azure Cache For Redis Webhooks
  slug: microsoft-azure-cache-for-redis-webhooks
collections:
- collection_type: open
  name: Azure Cache for Redis REST Operations API
  slug: open-microsoft-azure-cache-for-redis-operations-api
- collection_type: open
  name: Azure Cache for REST Operations Redis API
  slug: open-microsoft-azure-cache-for-redis-redis-api
- collection_type: open
  name: Azure Cache for Redis REST API
  slug: open-microsoft-azure-cache-for-redis
common:
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/rules/microsoft-azure-cache-for-redis-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-cache-for-redis-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/json-ld/microsoft-azure-cache-for-redis-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-cache-for-redis-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/vocabulary/microsoft-azure-cache-for-redis-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-cache-for-redis-vocabulary.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/hosts/microsoft-azure-cache-for-redis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-cache-for-redis-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/vendors/microsoft-azure-cache-for-redis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-cache-for-redis-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/plans/microsoft-azure-cache-for-redis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-cache-for-redis-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/finops/microsoft-azure-cache-for-redis-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-cache-for-redis-finops.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/capabilities/microsoft-azure-cache-for-redis-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-azure-cache-for-redis-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/overlays/microsoft-azure-cache-for-redis-privateendpointconnections-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-azure-cache-for-redis-privateendpointconnections-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/security/microsoft-azure-cache-for-redis-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-cache-for-redis-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/security/microsoft-azure-cache-for-redis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-cache-for-redis-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/agentic-access/microsoft-azure-cache-for-redis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-cache-for-redis-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/security/microsoft-azure-cache-for-redis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-cache-for-redis-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/authentication/microsoft-azure-cache-for-redis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-cache-for-redis-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/scopes/microsoft-azure-cache-for-redis-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-cache-for-redis-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/cache/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/options/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/redis/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/quickstart-create-redis
- group: start
  title: ''
  type: SignUp
  url: https://azure.microsoft.com/en-us/free/
- group: build
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/packages/microsoft-azure-cache-for-redis-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-cache-for-redis-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/packages/microsoft-azure-cache-for-redis-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-cache-for-redis-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/cli/microsoft-azure-cache-for-redis-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-cache-for-redis-cli.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/well-known/microsoft-azure-cache-for-redis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-cache-for-redis-well-known.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/well-known/microsoft-azure-cache-for-redis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-cache-for-redis-security.txt
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/security/microsoft-azure-cache-for-redis-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/microsoft-azure-cache-for-redis-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/conformance/microsoft-azure-cache-for-redis-conformance.yml
  title: ''
  type: Compliance
  url: conformance/microsoft-azure-cache-for-redis-conformance.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/conformance/microsoft-azure-cache-for-redis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-cache-for-redis-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/mcp/microsoft-azure-cache-for-redis-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-azure-cache-for-redis-mcp.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/llms/microsoft-azure-cache-for-redis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-cache-for-redis-llms.txt
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/conventions/microsoft-azure-cache-for-redis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-cache-for-redis-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/conventions/microsoft-azure-cache-for-redis-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-cache-for-redis-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/errors/microsoft-azure-cache-for-redis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-cache-for-redis-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/lifecycle/microsoft-azure-cache-for-redis-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-cache-for-redis-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/azure/azure-cache-for-redis/retirement-faq
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/changelog/microsoft-azure-cache-for-redis-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-cache-for-redis-changelog.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/data-model/microsoft-azure-cache-for-redis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-cache-for-redis-data-model.yml
- group: docs
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/asyncapi/microsoft-azure-cache-for-redis-events-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/microsoft-azure-cache-for-redis-events-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/asyncapi/microsoft-azure-cache-for-redis-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/microsoft-azure-cache-for-redis-webhooks.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/rate-limits/microsoft-azure-cache-for-redis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-cache-for-redis-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-cache-for-redis/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
created: '2026-03-13'
description: 'Azure Cache for Redis is Microsoft''s managed in-memory data store built on the open-source Redis software, used to put a low-latency cache, session store or message broker in front of a slower backing store. This record covers the management (control-plane) REST API — the Microsoft.Cache/redis resource provider on Azure Resource Manager — which creates, scales, secures, backs up and deletes caches across the Basic, Standard, Premium, Enterprise and Enterprise Flash tiers. The Redis data plane itself is plain Redis, spoken with an ordinary Redis client and not described by an OpenAPI. Microsoft announced in October 2025 that every Azure Cache for Redis SKU is retiring: Enterprise and Enterprise Flash on 2027-03-31, Basic, Standard and Premium on 2028-09-30, with Azure Managed Redis as the successor.'
examples:
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Access Policy Assignment Create Update Example
  slug: microsoft-azure-cache-for-redis-redis-cache-access-policy-assignment-create-update-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Access Policy Assignment Delete Example
  slug: microsoft-azure-cache-for-redis-redis-cache-access-policy-assignment-delete-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Access Policy Assignment Get Example
  slug: microsoft-azure-cache-for-redis-redis-cache-access-policy-assignment-get-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Access Policy Assignment List Example
  slug: microsoft-azure-cache-for-redis-redis-cache-access-policy-assignment-list-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Access Policy Create Update Example
  slug: microsoft-azure-cache-for-redis-redis-cache-access-policy-create-update-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Access Policy Delete Example
  slug: microsoft-azure-cache-for-redis-redis-cache-access-policy-delete-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Access Policy Get Example
  slug: microsoft-azure-cache-for-redis-redis-cache-access-policy-get-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Access Policy List Example
  slug: microsoft-azure-cache-for-redis-redis-cache-access-policy-list-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Async Operation Status Example
  slug: microsoft-azure-cache-for-redis-redis-cache-async-operation-status-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Check Name Availability Example
  slug: microsoft-azure-cache-for-redis-redis-cache-check-name-availability-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Create Automatic Zonal Allocation Policy Example
  slug: microsoft-azure-cache-for-redis-redis-cache-create-automatic-zonal-allocation-policy-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Create Default Version Example
  slug: microsoft-azure-cache-for-redis-redis-cache-create-default-version-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Create Example
  slug: microsoft-azure-cache-for-redis-redis-cache-create-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Create Latest Version Example
  slug: microsoft-azure-cache-for-redis-redis-cache-create-latest-version-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Create No Zones Zonal Allocation Policy Example
  slug: microsoft-azure-cache-for-redis-redis-cache-create-no-zones-zonal-allocation-policy-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Create User Defined Zonal Allocation Policy Example
  slug: microsoft-azure-cache-for-redis-redis-cache-create-user-defined-zonal-allocation-policy-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Delete Example
  slug: microsoft-azure-cache-for-redis-redis-cache-delete-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Delete Private Endpoint Connection Example
  slug: microsoft-azure-cache-for-redis-redis-cache-delete-private-endpoint-connection-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Export Example
  slug: microsoft-azure-cache-for-redis-redis-cache-export-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Firewall Rule Create Example
  slug: microsoft-azure-cache-for-redis-redis-cache-firewall-rule-create-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Firewall Rule Delete Example
  slug: microsoft-azure-cache-for-redis-redis-cache-firewall-rule-delete-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Firewall Rule Get Example
  slug: microsoft-azure-cache-for-redis-redis-cache-firewall-rule-get-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Firewall Rules List Example
  slug: microsoft-azure-cache-for-redis-redis-cache-firewall-rules-list-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Flush Example
  slug: microsoft-azure-cache-for-redis-redis-cache-flush-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Force Reboot Example
  slug: microsoft-azure-cache-for-redis-redis-cache-force-reboot-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Get Example
  slug: microsoft-azure-cache-for-redis-redis-cache-get-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Get Private Endpoint Connection Example
  slug: microsoft-azure-cache-for-redis-redis-cache-get-private-endpoint-connection-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Import Example
  slug: microsoft-azure-cache-for-redis-redis-cache-import-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Linked Server_ Create Example
  slug: microsoft-azure-cache-for-redis-redis-cache-linked-server_-create-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Linked Server_ Delete Example
  slug: microsoft-azure-cache-for-redis-redis-cache-linked-server_-delete-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Linked Server_ Get Example
  slug: microsoft-azure-cache-for-redis-redis-cache-linked-server_-get-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Linked Server_ List Example
  slug: microsoft-azure-cache-for-redis-redis-cache-linked-server_-list-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache List By Resource Group Example
  slug: microsoft-azure-cache-for-redis-redis-cache-list-by-resource-group-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache List Example
  slug: microsoft-azure-cache-for-redis-redis-cache-list-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache List Keys Example
  slug: microsoft-azure-cache-for-redis-redis-cache-list-keys-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache List Private Endpoint Connections Example
  slug: microsoft-azure-cache-for-redis-redis-cache-list-private-endpoint-connections-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache List Private Link Resources Example
  slug: microsoft-azure-cache-for-redis-redis-cache-list-private-link-resources-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache List Upgrade Notifications Example
  slug: microsoft-azure-cache-for-redis-redis-cache-list-upgrade-notifications-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Operations Example
  slug: microsoft-azure-cache-for-redis-redis-cache-operations-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Patch Schedules Create Or Update Example
  slug: microsoft-azure-cache-for-redis-redis-cache-patch-schedules-create-or-update-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Patch Schedules Delete Example
  slug: microsoft-azure-cache-for-redis-redis-cache-patch-schedules-delete-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Patch Schedules Get Example
  slug: microsoft-azure-cache-for-redis-redis-cache-patch-schedules-get-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Patch Schedules List Example
  slug: microsoft-azure-cache-for-redis-redis-cache-patch-schedules-list-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Put Private Endpoint Connection Example
  slug: microsoft-azure-cache-for-redis-redis-cache-put-private-endpoint-connection-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Regenerate Key Example
  slug: microsoft-azure-cache-for-redis-redis-cache-regenerate-key-example
- key_count: 4
  name: Microsoft Azure Cache For Redis Redis Cache Update Example
  slug: microsoft-azure-cache-for-redis-redis-cache-update-example
finops:
- has_sources: true
  method: derived
  name: Microsoft Azure Cache For Redis Finops
  primary_unit: ''
  service_category: ''
  slug: microsoft-azure-cache-for-redis-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-cache-for-redis.png
json_schemas:
- name: CheckNameAvailabilityParameters
  property_count: 2
  slug: microsoft-azure-cache-for-redis-check-name-availability-parameters
- name: ExportRDBParameters
  property_count: 5
  slug: microsoft-azure-cache-for-redis-export-rdbparameters
- name: ImportRDBParameters
  property_count: 4
  slug: microsoft-azure-cache-for-redis-import-rdbparameters
- name: OperationListResult
  property_count: 2
  slug: microsoft-azure-cache-for-redis-operation-list-result
- name: OperationStatus
  property_count: 1
  slug: microsoft-azure-cache-for-redis-operation-status
- name: PrivateEndpointConnectionListResult
  property_count: 2
  slug: microsoft-azure-cache-for-redis-private-endpoint-connection-list-result
- name: RedisCacheAccessPolicyAssignmentList
  property_count: 2
  slug: microsoft-azure-cache-for-redis-redis-cache-access-policy-assignment-list
- name: RedisCacheAccessPolicyAssignment
  property_count: 1
  slug: microsoft-azure-cache-for-redis-redis-cache-access-policy-assignment
- name: RedisCacheAccessPolicyList
  property_count: 2
  slug: microsoft-azure-cache-for-redis-redis-cache-access-policy-list
- name: RedisCacheAccessPolicy
  property_count: 1
  slug: microsoft-azure-cache-for-redis-redis-cache-access-policy
- name: RedisCreateParameters
  property_count: 5
  slug: microsoft-azure-cache-for-redis-redis-create-parameters
- name: RedisFirewallRuleListResult
  property_count: 2
  slug: microsoft-azure-cache-for-redis-redis-firewall-rule-list-result
- name: RedisFirewallRule
  property_count: 1
  slug: microsoft-azure-cache-for-redis-redis-firewall-rule
- name: RedisLinkedServerCreateParameters
  property_count: 1
  slug: microsoft-azure-cache-for-redis-redis-linked-server-create-parameters
- name: RedisLinkedServerWithPropertiesList
  property_count: 2
  slug: microsoft-azure-cache-for-redis-redis-linked-server-with-properties-list
- name: RedisLinkedServerWithProperties
  property_count: 1
  slug: microsoft-azure-cache-for-redis-redis-linked-server-with-properties
- name: RedisPatchScheduleListResult
  property_count: 2
  slug: microsoft-azure-cache-for-redis-redis-patch-schedule-list-result
- name: RedisPatchSchedule
  property_count: 2
  slug: microsoft-azure-cache-for-redis-redis-patch-schedule
- name: RedisRebootParameters
  property_count: 3
  slug: microsoft-azure-cache-for-redis-redis-reboot-parameters
- name: RedisResource
  property_count: 3
  slug: microsoft-azure-cache-for-redis-redis-resource
- name: RedisUpdateParameters
  property_count: 3
  slug: microsoft-azure-cache-for-redis-redis-update-parameters
jsonld:
- class_count: 59
  name: Microsoft Azure Cache For Redis Context
  property_count: 91
  slug: microsoft-azure-cache-for-redis-context
layout: provider
mcp_servers:
- description: MCP server requiring OAuth; 2 tools listed.
  name: Azure MCP Server
  slug: azure-mcp-server
modified: '2026-09-17'
name: Microsoft Azure Cache For Redis
nav: Providers
network: true
overview: 'Microsoft Azure Cache For Redis publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including microsoft-azure-cache-for-redis Operations API, Linked Server API, Redis Cache Access Policies API, and 6 more. Tagged areas include Microsoft Azure, Cache, Cloud Infrastructure, Datastore, and In-Memory Database.


  The Microsoft Azure Cache For Redis catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Microsoft Azure Cache For Redis'' developer surface includes authentication, developer portal, pricing, support, engineering blog, documentation, API reference, and 44 more developer resources.'
plans:
- name: Microsoft Azure Cache For Redis Plans Pricing
  plan_count: 0
  slug: microsoft-azure-cache-for-redis-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 7
  name: Microsoft Azure Cache For Redis Rate Limits
  slug: microsoft-azure-cache-for-redis-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Microsoft Azure Cache For Redis API Rules
  rule_count: 55
  severity_counts:
    error: 47
    hint: 0
    info: 4
    warn: 4
  slug: microsoft-azure-cache-for-redis-rules
scopes:
- name: Microsoft Azure Cache For Redis Scopes
  scope_count: 1
  slug: microsoft-azure-cache-for-redis-scopes
  summary_line: 1 scope · implicit
score:
  band: exemplar
  composite: 72.8
  coverage:
    artifact_dirs: 36
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.9
  facets:
    access_clarity: 60.5
    contract_governance: 35.6
    contract_quality: 66.0
    developer_ergonomics: 73.2
    discoverability: 73.3
    operational_transparency: 92.1
  previous_composite: 68.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
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
    score: 22.2
screenshot: https://apis.io/screenshots/microsoft-azure-cache-for-redis/microsoft-azure-cache-for-redis-2026-06-20T185402.png
security:
- kind: authentication
  name: Microsoft Azure Cache For Redis Authentication
  slug: microsoft-azure-cache-for-redis-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Azure Cache For Redis Domain Security
  slug: microsoft-azure-cache-for-redis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Cache For Redis Vulnerability Disclosure
  slug: microsoft-azure-cache-for-redis-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Cache For Redis Trust Center
  slug: microsoft-azure-cache-for-redis-trust-center
  summary_line: GDPR
skill_count: 4
skills:
- name: azure-cache-for-redis-backup-and-restore
  slug: microsoft-azure-cache-for-redis-backup-and-restore
- name: azure-cache-for-redis-entra-access-control
  slug: microsoft-azure-cache-for-redis-entra-access-control
- name: lock-down-azure-cache-for-redis-network
  slug: microsoft-azure-cache-for-redis-lock-down-network
- name: provision-azure-cache-for-redis
  slug: microsoft-azure-cache-for-redis-provision-cache
slug: microsoft-azure-cache-for-redis
tags:
- Microsoft Azure
- Cache
- Cloud Infrastructure
- Datastore
- In-Memory Database
- Managed Service
- Microsoft
- Redis
website: https://www.microsoft.com/
---
