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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Squid Agentic Access
  operation_count: 15
  slug: squid-agentic-access
  summary_line: 15 operations
api_count: 1
apis:
- description: Squid provides extensive access control configuration through its squid.conf file and runtime reload capabilities. The access control system supports ACLs for IP addresses, domain names, URL patterns,
  name: Squid Access Control Configuration API
  slug: squid-access-control
- baseURL: http://localhost:3128/squid-internal-mgr
  baseurl_source: declared
  description: Cache performance metrics and counters
  name: Squid Cache Statistics API
  slug: squid-cache-statistics-api
- baseURL: http://localhost:3128/squid-internal-mgr
  baseurl_source: declared
  description: Runtime configuration and ACL information
  name: Squid Configuration API
  slug: squid-configuration-api
- baseURL: http://localhost:3128/squid-internal-mgr
  baseurl_source: declared
  description: Active connection and request management
  name: Squid Connections API
  slug: squid-connections-api
- baseURL: http://localhost:3128/squid-internal-mgr
  baseurl_source: declared
  description: Memory allocation and pool statistics
  name: Squid Memory API
  slug: squid-memory-api
- baseURL: http://localhost:3128/squid-internal-mgr
  baseurl_source: declared
  description: Cache operational commands
  name: Squid Operations API
  slug: squid-operations-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Squid Cache Manager API
  slug: open-squid-cache-manager
- collection_type: open
  name: Squid Cache Manager Cache Statistics API
  slug: open-squid-cache-statistics-api
- collection_type: open
  name: Squid Cache Manager Cache Statistics Configuration API
  slug: open-squid-configuration-api
- collection_type: open
  name: Squid Cache Manager Cache Statistics Connections API
  slug: open-squid-connections-api
- collection_type: open
  name: Squid Cache Manager Cache Statistics Memory API
  slug: open-squid-memory-api
- collection_type: open
  name: Squid Cache Manager Cache Statistics Operations API
  slug: open-squid-operations-api
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
random_paper: 4
rate_limits:
- limit_count: 5
  name: Squid Rate Limits
  slug: squid-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Squid API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: squid-jsonschema-spectral-rules
- effective_rule_count: 47
  extends:
  - spectral:oas
  name: Squid API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 4
  slug: squid-rules
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 64.5
    catalog_earned_first_party: 0.0
    catalog_gap: 50.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 58.5
    developer_ergonomics: 33.3
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 37.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
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
