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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Cloudflare Kv Agentic Access
  operation_count: 14
  slug: cloudflare-kv-agentic-access
  summary_line: 14 operations · 9 acting
api_count: 1
apis:
- description: The Workers KV Namespace API from Cloudflare KV — 8 operation(s) for workers kv namespace.
  name: Cloudflare KV Workers KV Namespace API
  slug: cloudflare-kv-workers-kv-namespace-api
artifact_total: 36
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudflare-kv-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cloudflare-kv-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudflare-kv-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cloudflare.com/products/kv/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.cloudflare.com/kv/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.cloudflare.com/kv/get-started/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cloudflare
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/cloudflare/api-schemas
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/cloudflare/api-schemas/main/openapi.yaml
- group: build
  title: ''
  type: SDKTypeScript
  url: https://github.com/cloudflare/cloudflare-typescript
- group: build
  title: ''
  type: SDKPython
  url: https://github.com/cloudflare/cloudflare-python
- group: build
  title: ''
  type: SDKGo
  url: https://github.com/cloudflare/cloudflare-go
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudflare/
- group: company
  title: ''
  type: Blog
  url: https://blog.cloudflare.com/
- group: company
  title: ''
  type: DeveloperBlog
  url: https://blog.cloudflare.com/tag/developers/
- group: commercial
  title: ''
  type: Pricing
  url: https://developers.cloudflare.com/kv/platform/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.cloudflarestatus.com/
- group: other
  title: ''
  type: X
  url: https://x.com/Cloudflare
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developers.cloudflare.com/kv/platform/release-notes/
- group: other
  title: ''
  type: Limits
  url: https://developers.cloudflare.com/kv/platform/limits/
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudflare-kv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudflare-kv-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cloudflare-kv-finops.yml
created: 2026-06-13
description: Cloudflare Workers KV is a globally distributed key-value store that allows developers to store and retrieve data at low latency from Cloudflare's edge network. It provides a REST API for reading, writing, deleting, and listing key-value pairs across namespaces, making it ideal for caching, configuration management, session storage, API authorization, and dynamic routing. KV supports eventual consistency across Cloudflare's global network with read latencies under 5ms, and is accessible both via Workers bindings and external REST API calls.
finops:
- name: Cloudflare Kv Finops
  service_category: ''
  slug: cloudflare-kv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudflare-kv.png
json_schemas:
- name: Any
  property_count: 0
  slug: workers-kv_any
- name: Api Response Collection
  property_count: 0
  slug: workers-kv_api-response-collection
- name: Api Response Common Failure
  property_count: 4
  slug: workers-kv_api-response-common-failure
- name: Api Response Common No Result
  property_count: 0
  slug: workers-kv_api-response-common-no-result
- name: Api Response Common
  property_count: 3
  slug: workers-kv_api-response-common
- name: Bulk Get Result With Metadata
  property_count: 1
  slug: workers-kv_bulk-get-result-with-metadata
- name: Bulk Get Result
  property_count: 1
  slug: workers-kv_bulk-get-result
- name: Bulk Result
  property_count: 2
  slug: workers-kv_bulk-result
- name: Bulk Delete
  property_count: 0
  slug: workers-kv_bulk_delete
- name: Bulk Write
  property_count: 0
  slug: workers-kv_bulk_write
- name: Create Rename Namespace Body
  property_count: 1
  slug: workers-kv_create_rename_namespace_body
- name: Cursor
  property_count: 0
  slug: workers-kv_cursor
- name: Cursor Result Info
  property_count: 2
  slug: workers-kv_cursor_result_info
- name: Expiration
  property_count: 0
  slug: workers-kv_expiration
- name: Expiration Ttl
  property_count: 0
  slug: workers-kv_expiration_ttl
- name: Identifier
  property_count: 0
  slug: workers-kv_identifier
- name: Key
  property_count: 3
  slug: workers-kv_key
- name: Key Name
  property_count: 0
  slug: workers-kv_key_name
- name: Key Name Bulk
  property_count: 0
  slug: workers-kv_key_name_bulk
- name: List Metadata
  property_count: 0
  slug: workers-kv_list_metadata
- name: Messages
  property_count: 0
  slug: workers-kv_messages
- name: Metadata
  property_count: 0
  slug: workers-kv_metadata
- name: Namespace
  property_count: 3
  slug: workers-kv_namespace
- name: Namespace Identifier
  property_count: 0
  slug: workers-kv_namespace_identifier
- name: Namespace Title
  property_count: 0
  slug: workers-kv_namespace_title
- name: Result Info
  property_count: 4
  slug: workers-kv_result_info
- name: Value
  property_count: 0
  slug: workers-kv_value
jsonld:
- class_count: 0
  name: Cloudflare Kv Context
  property_count: 23
  slug: cloudflare-kv-context
layout: provider
modified: 2026-06-13
name: Cloudflare KV
nav: Providers
network: true
overview: 'Cloudflare KV publishes 1 API on the [APIs.io](https://apis.io/) network: Workers KV Namespace API. Tagged areas include Key-Value Store, Edge Computing, Cloudflare Workers, Distributed Storage, and Global Database.


  The Cloudflare KV catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cloudflare KV''s developer surface includes documentation, getting-started guide, engineering blog, pricing, release notes, and 18 more developer resources.'
plans:
- name: Cloudflare Kv Plans Pricing
  plan_count: 2
  slug: cloudflare-kv-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Cloudflare Kv Rate Limits
  slug: cloudflare-kv-rate-limits
rules:
- name: Cloudflare KV API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cloudflare-kv-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.9
  delta: -4.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.2
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 50.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudflare-kv/refs/heads/main/screenshots/cloudflare-kv-2026-06-20T174555.png
security:
- kind: domain-security
  name: Cloudflare Kv Domain Security
  slug: cloudflare-kv-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cloudflare Kv Vulnerability Disclosure
  slug: cloudflare-kv-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: cloudflare-kv
tags:
- Key-Value Store
- Edge Computing
- Cloudflare Workers
- Distributed Storage
- Global Database
- Cache
- Configuration Management
website: https://www.cloudflare.com/products/kv/
---
