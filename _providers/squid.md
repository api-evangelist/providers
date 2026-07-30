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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Squid Agentic Access
  operation_count: 15
  slug: squid-agentic-access
  summary_line: 15 operations
api_count: 6
apis:
- description: Squid provides extensive access control configuration through its squid.conf file and runtime reload capabilities. The access control system supports ACLs for IP addresses, domain names, URL patterns,
  name: Squid Access Control Configuration API
  slug: squid-access-control
- description: Cache performance metrics and counters
  name: Squid Cache Statistics API
  slug: squid-cache-statistics-api
- description: Runtime configuration and ACL information
  name: Squid Configuration API
  slug: squid-configuration-api
- description: Active connection and request management
  name: Squid Connections API
  slug: squid-connections-api
- description: Memory allocation and pool statistics
  name: Squid Memory API
  slug: squid-memory-api
- description: Cache operational commands
  name: Squid Operations API
  slug: squid-operations-api
artifact_total: 20
collections:
- collection_type: open
  name: Squid Cache Manager API
  slug: open-squid-cache-manager
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/squid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/squid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/squid-authentication.yml
- group: company
  title: ''
  type: Website
  url: http://www.squid-cache.org/
- group: docs
  title: ''
  type: Documentation
  url: http://www.squid-cache.org/Doc/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/squid-cache
- group: operate
  title: ''
  type: ChangeLog
  url: http://www.squid-cache.org/Versions/
- group: operate
  title: ''
  type: FAQ
  url: http://wiki.squid-cache.org/SquidFaq
- group: other
  title: ''
  type: Mailing List
  url: http://www.squid-cache.org/Support/mailing-lists.html
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/openapi/squid-cache-manager-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/json-schema/squid-cache-stats-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/json-structure/squid-cache-stats-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/json-ld/squid-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/rules/squid-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/vocabulary/squid-vocabulary.yml
created: '2026-03-27'
description: Squid is a high-performance caching and forwarding HTTP web proxy used for content caching, access control, and bandwidth management. It supports HTTP, HTTPS, FTP, and other protocols, providing caching proxy features, access control lists, SSL/TLS inspection, and web content filtering for enterprises and internet service providers.
examples:
- key_count: 4
  name: Squid Get Cache Info Example
  slug: squid-get-cache-info-example
- key_count: 4
  name: Squid Get Connections Example
  slug: squid-get-connections-example
finops:
- name: Squid Finops
  service_category: API
  slug: squid-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/squid.png
json_schemas:
- name: Squid Cache Statistics
  property_count: 11
  slug: squid-cache-stats
json_structures:
- name: Squid Cache Stats Structure
  property_count: 0
  slug: squid-cache-stats-structure
jsonld:
- class_count: 28
  name: Squid Context
  property_count: 4
  slug: squid-context
layout: provider
modified: '2026-05-19'
name: Squid
nav: Providers
network: true
overview: 'Squid publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cache Statistics API, Configuration API, Connections API, and 2 more. Tagged areas include Caching Proxy, Proxy, HTTP Proxy, Web Cache, and Access Control.


  The Squid catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Squid''s developer surface includes authentication, documentation, changelog, FAQ, and 11 more developer resources.'
plans:
- name: Squid Plans Pricing
  plan_count: 3
  slug: squid-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 5
  name: Squid Rate Limits
  slug: squid-rate-limits
rules:
- name: Squid API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: squid-jsonschema-spectral-rules
- name: Squid API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: squid-rules
score:
  band: developing
  composite: 49.3
  delta: -5.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 54.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/squid/refs/heads/main/screenshots/squid-2026-06-20T194428.png
security:
- kind: authentication
  name: Squid Authentication
  slug: squid-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Squid Domain Security
  slug: squid-domain-security
  summary_line: DMARC
slug: squid
tags:
- Caching Proxy
- Proxy
- HTTP Proxy
- Web Cache
- Access Control
- Content Filtering
website: http://www.squid-cache.org/
---
