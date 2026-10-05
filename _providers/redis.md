---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
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
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.8
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 103
  human_in_the_loop: 9
  name: Redis Agentic Access
  operation_count: 179
  slug: redis-agentic-access
  summary_line: 179 operations · 103 acting · 9 human-in-the-loop
api_count: 1
apis:
- description: Core Redis commands and data structure operations. Redis supports strings, hashes, lists, sets, sorted sets, streams, and more. The primary interface is the Redis Serialization Protocol (RESP) over TC
  name: Redis Core
  slug: redis-core
- description: The Redis Cloud REST API for managing subscriptions, databases, cloud accounts, access control, and logs on the Redis Cloud platform. Available at api.redislabs.com/v1 with API key authentication.
  name: Redis Cloud API
  slug: redis-cloud-api
- description: REST API for managing Redis Enterprise Software clusters. Provides endpoints for cluster configuration, database creation and management, user access control, and monitoring. Available at the cluster'
  name: Redis Enterprise API
  slug: redis-enterprise-api
- description: Redis Insight is a free GUI management tool for Redis. Provides database browsing, query execution, memory analysis, slow log inspection, and Redis Streams visualization. Available as a desktop app an
  name: Redis Insight
  slug: redis-insight
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: Current account details.
  name: Redis Account API
  slug: redis-account-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Actuator API from Redis — 1 operation(s) for actuator.
  name: Redis Actuator API
  slug: redis-actuator-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: All operations related to Agent Memory store lifecycle
  name: Redis Agent Memory - Stores API
  slug: redis-agent-memory-stores-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Ai API from Redis — 1 operation(s) for ai.
  name: Redis AI API
  slug: redis-ai-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Bdbs API from Redis — 1 operation(s) for bdbs.
  name: Redis Bdbs API
  slug: redis-bdbs-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Caches API from Redis — 5 operation(s) for caches.
  name: Redis Caches API
  slug: redis-caches-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: All operations related to cloud accounts (AWS only).
  name: Redis Cloud Accounts API
  slug: redis-cloud-accounts-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Data Integration API from Redis — 3 operation(s) for data integration.
  name: Redis Data Integration API
  slug: redis-data-integration-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: All Essentials database operations.
  name: Redis Databases - Essentials API
  slug: redis-databases-essentials-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: All Pro database operations.
  name: Redis Databases - Pro API
  slug: redis-databases-pro-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Dedup API from Redis — 2 operation(s) for dedup.
  name: Redis Dedup API
  slug: redis-dedup-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: Dynamic endpoint redirection operations.
  name: Redis Endpoint Redirections API
  slug: redis-endpoint-redirections-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Gpg API from Redis — 1 operation(s) for gpg.
  name: Redis Gpg API
  slug: redis-gpg-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Homebrew API from Redis — 1 operation(s) for homebrew.
  name: Redis Homebrew API
  slug: redis-homebrew-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Images API from Redis — 1 operation(s) for images.
  name: Redis Images API
  slug: redis-images-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Long Term Memory API from Redis — 1 operation(s) for long term memory.
  name: Redis Long Term Memory API
  slug: redis-long-term-memory-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Redis API API from Redis — 1 operation(s) for redis api.
  name: Redis Redis API
  slug: redis-redis-api-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Redis Cli API from Redis — 1 operation(s) for redis cli.
  name: Redis Redis Cli API
  slug: redis-redis-cli-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: All operations for [Role-based Access Control](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/role-based-access-control/) (RBAC).
  name: Redis Role-based Access Control (RBAC) API
  slug: redis-role-based-access-control-rbac-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: All Essentials subscription operations.
  name: Redis Subscriptions - Essentials API
  slug: redis-subscriptions-essentials-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: All Pro subscription operations.
  name: Redis Subscriptions - Pro API
  slug: redis-subscriptions-pro-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: All Pro subscription connectivity operations.
  name: Redis Subscriptions - Pro - Connectivity API
  slug: redis-subscriptions-pro-connectivity-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: Tracks asynchronous background operations. See [API request lifecycle](https://redis.io/docs/latest/operate/rc/api/get-started/process-lifecycle/) for more information.
  name: Redis Tasks API
  slug: redis-tasks-api
- baseURL: https://packages.redis.io
  baseurl_source: declared
  description: The Users API from Redis — 5 operation(s) for users.
  name: Redis Users API
  slug: redis-users-api
artifact_total: 70
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/agentic-access/redis-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/redis-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/finops/redis-finops.yml
  title: ''
  type: FinOps
  url: finops/redis-finops.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/rate-limits/redis-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/redis-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/plans/redis-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/redis-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/rules/redis-rules.yml
  title: ''
  type: Spectral
  url: rules/redis-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/rules/redis-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/redis-jsonschema-spectral-rules.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/data-model/redis-data-model.yml
  title: ''
  type: DataModel
  url: data-model/redis-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/cli/redis-cli.yml
  title: ''
  type: CLI
  url: cli/redis-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.redis.io/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/authentication/redis-authentication.yml
  title: ''
  type: Authentication
  url: authentication/redis-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/errors/redis-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/redis-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/conformance/redis-conformance.yml
  title: ''
  type: Conformance
  url: conformance/redis-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/llms/redis-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/redis-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/mcp/redis-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/redis-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/well-known/redis-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/redis-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/well-known/redis-docs-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/redis-docs-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/well-known/redis-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/redis-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/hosts/redis-hosts.yml
  title: ''
  type: Hosts
  url: hosts/redis-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/vendors/redis-vendors.yml
  title: ''
  type: Vendors
  url: vendors/redis-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/packages/redis-packages.yml
  title: ''
  type: Packages
  url: packages/redis-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://redis.io/security/notice-apache-log4j2-cve-2021-44228/
- group: commercial
  title: ''
  type: Pricing
  url: https://redis.io/pricing/
- group: company
  title: ''
  type: Newsroom
  url: https://redis.io/company/news/
- group: start
  title: ''
  type: Login
  url: https://redis.io/login/
- group: other
  title: ''
  type: Leadership
  url: https://redis.io/company/team/
- group: operate
  title: ''
  type: ChangeLog
  url: https://redis.io/docs/latest/develop/whats-new/
- group: docs
  title: ''
  type: APIReference
  url: https://redis.io/docs/latest/develop/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://redis.io/docs/latest/operate/rc/rc-quickstart/index.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/security/redis-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/redis-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/security/redis-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/redis-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/security/redis-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/redis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://redis.io/
- group: docs
  title: ''
  type: Documentation
  url: https://redis.io/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/redis
- group: company
  title: ''
  type: Blog
  url: https://redis.io/blog/
- group: operate
  title: ''
  type: Community
  url: https://redis.io/community/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/redis/
- group: other
  title: ''
  type: X
  url: https://twitter.com/redisinc
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Redisinc
- group: operate
  title: ''
  type: StatusPage
  url: https://status.redis.com/
- group: operate
  title: ''
  type: Support
  url: https://redis.io/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://redis.io/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://redis.io/legal/privacy/
- group: docs
  title: ''
  type: Documentation
  url: https://redis.io/docs/latest/commands/
- group: build
  title: ''
  type: SDKs
  url: https://redis.io/docs/latest/develop/connect/clients/
- group: build
  title: ''
  type: npm
  url: https://www.npmjs.com/package/redis
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/redis/
- group: agent
  title: ''
  type: LlmsText
  url: https://redis.io/llms.txt
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://redis.io/mcp
  - status: 403
    url: https://packages.redis.io/mcp
  - status: 200
    url: https://redis.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2024-01-01'
description: Redis is an open source, in-memory data structure store used as a database, cache, message broker, and streaming engine. It supports strings, hashes, lists, sets, sorted sets, streams, JSON, and more. Redis is used by millions of developers for caching, session management, leaderboards, pub/sub messaging, real-time analytics, and event streaming. The Redis project is governed by the Redis Community and maintained by Redis Inc.
examples:
- key_count: 2
  name: Redis Hash Example
  slug: redis-hash-example
- key_count: 2
  name: Redis Set Get Example
  slug: redis-set-get-example
- key_count: 2
  name: Redis Sorted Set Example
  slug: redis-sorted-set-example
features:
- 'Free: 30 MB shared cloud DB'
- 'Essentials from $0.007/hr ($5/mo min): 250 MB-100 GB DB, SSO/RBAC'
- 'Pro from $0.014/hr ($200/mo min): dedicated, multi-region active-active'
- 'Enterprise: self-managed Redis Enterprise Software, hybrid, on-prem'
- 'Multi-cloud: AWS, GCP, Azure'
- Cloud API for cluster management at 60 req/min
- 'Redis Stack modules: RediSearch, RedisJSON, RedisGraph, RedisTimeSeries, RedisBloom'
- Vector similarity search (RediSearch)
- Redis Flex (RAM:Flash ratio for cost reduction)
- Auto-tiering for hot/cold data
- Active-active geo-distribution (Pro)
- Up to 99.999% uptime (Pro)
- Encryption in transit and at rest (Essentials+)
- Private connectivity (Pro)
- OAuth + API keys
- Open-source self-managed Redis OSS alternative
finops:
- name: Redis Finops
  service_category: Database / Cache
  slug: redis-finops
image: https://redis.io/images/redis-logo.png
json_schemas:
- name: Redis Command
  property_count: 8
  slug: redis-command
- name: GetApiDedupStatsResponse
  property_count: 6
  slug: redis-get-api-dedup-stats-response
- name: GetUsersUseridResponse
  property_count: 5
  slug: redis-get-users-userid-response
- name: Redis Key-Value Entry
  property_count: 5
  slug: redis-key-value
- name: PostApiDedupDedupidRequest
  property_count: 4
  slug: redis-post-api-dedup-dedupid-request
- name: PostApiDedupDedupidResponse
  property_count: 6
  slug: redis-post-api-dedup-dedupid-response
- name: PostUsersRequest
  property_count: 4
  slug: redis-post-users-request
- name: PostV1LongTermMemoryRequest
  property_count: 1
  slug: redis-post-v1-long-term-memory-request
- name: Redis Server Info
  property_count: 19
  slug: redis-server-info
json_structures:
- name: Redis Key Value Structure
  property_count: 0
  slug: redis-key-value-structure
- name: Redis Server Info Structure
  property_count: 0
  slug: redis-server-info-structure
jsonld:
- class_count: 0
  name: Redis Context
  property_count: 3
  slug: redis-context
layout: provider
mcp_servers:
- description: Remote MCP server at redis.io over HTTP; 3 tools listed.
  name: Redis MCP Server
  slug: redis
modified: '2026-05-04'
name: Redis
nav: Providers
network: true
overview: 'Redis publishes 28 APIs on the [APIs.io](https://apis.io/) network, including Account API, Actuator API, Agent Memory - Stores API, and 25 more. Tagged areas include Cache, Database, In-Memory, Key-Value Store, and NoSQL.


  The Redis catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Redis'' developer surface includes CLI, authentication, pricing, changelog, API reference, getting-started guide, documentation, and 42 more developer resources.'
plans:
- name: Redis Plans Pricing
  plan_count: 4
  slug: redis-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Redis Rate Limits
  slug: redis-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Redis API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: redis-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: Redis API Rules
  rule_count: 20
  severity_counts:
    error: 13
    hint: 0
    info: 4
    warn: 3
  slug: redis-rules
score:
  band: strong
  composite: 59.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 18.8
  facets:
    access_clarity: 76.3
    contract_governance: 31.8
    contract_quality: 44.4
    developer_ergonomics: 63.7
    discoverability: 70.0
    operational_transparency: 55.3
  previous_composite: 40.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 52.0
      total: 25
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/redis/refs/heads/main/screenshots/redis-2026-06-20T192736.png
security:
- kind: authentication
  name: Redis Authentication
  slug: redis-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Redis Domain Security
  slug: redis-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Redis Vulnerability Disclosure
  slug: redis-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Redis Trust Center
  slug: redis-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR, CSA STAR, FIPS 140
slug: redis
tags:
- Cache
- Database
- In-Memory
- Key-Value Store
- NoSQL
- Open Source
- Streaming
website: https://redis.io/
---
