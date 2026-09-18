---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
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
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.3
  scored_at: '2026-09-17'
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
  slug: microsoft-azure-cache-for-redis-operations-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The LinkedServer API from Microsoft Azure Cache For Redis — 2 operation(s) for linkedserver.
  name: Microsoft Azure Cache For Redis Linked Server API
  slug: microsoft-azure-cache-for-redis-linkedserver-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The PrivateEndpointConnections API from Microsoft Azure Cache For Redis — 2 operation(s) for privateendpointconnections.
  name: Microsoft Azure Cache For Redis Private Endpoint Connections API
  slug: microsoft-azure-cache-for-redis-privateendpointconnections-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The RedisCacheAccessPolicies API from Microsoft Azure Cache For Redis — 2 operation(s) for rediscacheaccesspolicies.
  name: Microsoft Azure Cache For Redis Redis Cache Access Policies API
  slug: microsoft-azure-cache-for-redis-rediscacheaccesspolicies-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The RedisCacheAccessPolicyAssignments API from Microsoft Azure Cache For Redis — 2 operation(s) for rediscacheaccesspolicyassignments.
  name: Microsoft Azure Cache For Redis Redis Cache Access Policy Assignments API
  slug: microsoft-azure-cache-for-redis-rediscacheaccesspolicyassignments-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The RedisFirewallRules API from Microsoft Azure Cache For Redis — 2 operation(s) for redisfirewallrules.
  name: Microsoft Azure Cache For Redis Redis Firewall Rules API
  slug: microsoft-azure-cache-for-redis-redisfirewallrules-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The RedisPatchSchedules API from Microsoft Azure Cache For Redis — 2 operation(s) for redispatchschedules.
  name: Microsoft Azure Cache For Redis Redis Patch Schedules API
  slug: microsoft-azure-cache-for-redis-redispatchschedules-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The RedisResources API from Microsoft Azure Cache For Redis — 11 operation(s) for redisresources.
  name: Microsoft Azure Cache For Redis Redis Resources API
  slug: microsoft-azure-cache-for-redis-redisresources-api
- baseURL: https://management.azure.com/
  baseurl_source: declared
  description: The Subscriptions API from Microsoft Azure Cache For Redis — 2 operation(s) for subscriptions.
  name: Microsoft Azure Cache For Redis Subscriptions API
  slug: microsoft-azure-cache-for-redis-subscriptions-api
artifact_total: 71
asyncapis:
- description: The four events Azure Cache for Redis publishes to Azure Event Grid. Derived by API Evangelist from Microsoft's published event catalog and payload samples at https://learn.microsoft.com/en-us/azure/e
  name: Azure Cache for Redis — Event Grid events
  slug: microsoft-azure-cache-for-redis-events-asyncapi
- description: ''
  name: Microsoft Azure Cache For Redis Webhooks
  slug: microsoft-azure-cache-for-redis-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/security/microsoft-azure-cache-for-redis-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-cache-for-redis-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/security/microsoft-azure-cache-for-redis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-cache-for-redis-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/agentic-access/microsoft-azure-cache-for-redis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-cache-for-redis-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/security/microsoft-azure-cache-for-redis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-cache-for-redis-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/authentication/microsoft-azure-cache-for-redis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-cache-for-redis-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/scopes/microsoft-azure-cache-for-redis-scopes.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/packages/microsoft-azure-cache-for-redis-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-cache-for-redis-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/packages/microsoft-azure-cache-for-redis-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-cache-for-redis-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/cli/microsoft-azure-cache-for-redis-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-cache-for-redis-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/well-known/microsoft-azure-cache-for-redis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-cache-for-redis-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/well-known/microsoft-azure-cache-for-redis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-cache-for-redis-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/security/microsoft-azure-cache-for-redis-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/microsoft-azure-cache-for-redis-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/conformance/microsoft-azure-cache-for-redis-conformance.yml
  title: ''
  type: Compliance
  url: conformance/microsoft-azure-cache-for-redis-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/conformance/microsoft-azure-cache-for-redis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-cache-for-redis-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/mcp/microsoft-azure-cache-for-redis-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-azure-cache-for-redis-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/llms/microsoft-azure-cache-for-redis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-cache-for-redis-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/conventions/microsoft-azure-cache-for-redis-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-cache-for-redis-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/conventions/microsoft-azure-cache-for-redis-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-cache-for-redis-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/errors/microsoft-azure-cache-for-redis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-cache-for-redis-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/lifecycle/microsoft-azure-cache-for-redis-lifecycle.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/changelog/microsoft-azure-cache-for-redis-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-cache-for-redis-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/data-model/microsoft-azure-cache-for-redis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-cache-for-redis-data-model.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/asyncapi/microsoft-azure-cache-for-redis-events-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/microsoft-azure-cache-for-redis-events-asyncapi.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/asyncapi/microsoft-azure-cache-for-redis-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/microsoft-azure-cache-for-redis-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/rate-limits/microsoft-azure-cache-for-redis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-cache-for-redis-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/examples/_index.yml
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
- name: Microsoft Azure Cache For Redis Finops
  service_category: API
  slug: microsoft-azure-cache-for-redis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-cache-for-redis.png
layout: provider
mcp_servers:
- description: ''
  name: Azure MCP Server
  slug: azure-mcp-server
modified: '2026-09-17'
name: Microsoft Azure Cache For Redis
nav: Providers
network: true
overview: 'Microsoft Azure Cache For Redis publishes 9 APIs on the [APIs.io](https://apis.io/) network, including microsoft-azure-cache-for-redis Operations API, Linked Server API, Private Endpoint Connections API, and 6 more. Tagged areas include Azure, Cache, Cloud Infrastructure, Datastore, and In-Memory Database.


  The Microsoft Azure Cache For Redis catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Microsoft Azure Cache For Redis'' developer surface includes authentication, developer portal, pricing, support, engineering blog, documentation, API reference, and 34 more developer resources.'
plans:
- name: Microsoft Azure Cache For Redis Plans Pricing
  plan_count: 5
  slug: microsoft-azure-cache-for-redis-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 7
  name: Microsoft Azure Cache For Redis Rate Limits
  slug: microsoft-azure-cache-for-redis-rate-limits
scopes:
- name: Microsoft Azure Cache For Redis Scopes
  scope_count: 1
  slug: microsoft-azure-cache-for-redis-scopes
  summary_line: 1 scope · implicit
score:
  band: exemplar
  composite: 71.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 33.5
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 73.2
    discoverability: 75.9
    operational_transparency: 92.1
  previous_composite: 38.0
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
  schema_version: 0.22.0
  scored_at: '2026-09-17'
  trend: rising
  upsert:
    applies: true
    score: 22.2
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-cache-for-redis/refs/heads/main/screenshots/microsoft-azure-cache-for-redis-2026-06-20T185402.png
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
slug: microsoft-azure-cache-for-redis
tags:
- Azure
- Cache
- Cloud Infrastructure
- Datastore
- In-Memory Database
- Managed Service
- Microsoft
- Redis
website: https://www.microsoft.com/
---
