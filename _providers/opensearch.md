---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Opensearch Agentic Access
  operation_count: 47
  slug: opensearch-agentic-access
  summary_line: 47 operations · 27 acting
api_count: 1
apis:
- description: The core OpenSearch REST API for indexing documents, performing search queries (full text, vector, hybrid), aggregations, and managing indices, mappings, templates, aliases, and snapshots.
  name: OpenSearch Search and Indexing REST API
  slug: opensearch-search-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: Self-service account endpoints for the calling user.
  name: OpenSearch Account API
  slug: opensearch-account-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: Reusable groups of cluster and index permissions.
  name: OpenSearch Action Groups API
  slug: opensearch-action-groups-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: Allowlist of HTTP APIs available to non-admin users.
  name: OpenSearch Allowlist API
  slug: opensearch-allowlist-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: Audit log configuration.
  name: OpenSearch Audit API
  slug: opensearch-audit-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: Manage the security cache.
  name: OpenSearch Cache API
  slug: opensearch-cache-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: Inspect SSL certificates loaded by the cluster.
  name: OpenSearch Certificates API
  slug: opensearch-certificates-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: Security plugin health check.
  name: OpenSearch Health API
  slug: opensearch-health-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: CRUD for internal user database entries.
  name: OpenSearch Internal Users API
  slug: opensearch-internal-users-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: Allowlisted distinguished names for cross-cluster nodes.
  name: OpenSearch Nodes DN API
  slug: opensearch-nodes-dn-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: Map users, backend roles, and hosts to security roles.
  name: OpenSearch Role Mappings API
  slug: opensearch-role-mappings-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: CRUD for security roles and their permissions.
  name: OpenSearch Roles API
  slug: opensearch-roles-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: Inspect and update the running security configuration.
  name: OpenSearch Security Config API
  slug: opensearch-security-config-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: Inspect SSL handshake information for the calling client.
  name: OpenSearch SSL Info API
  slug: opensearch-ssl-info-api
- baseURL: https://{cluster-host}:9200
  baseurl_source: declared
  description: Multi-tenancy support for OpenSearch Dashboards.
  name: OpenSearch Tenants API
  slug: opensearch-tenants-api
artifact_total: 50
collections:
- collection_type: open
  name: OpenSearch Security Plugin REST Account API
  slug: open-opensearch-account-api
- collection_type: open
  name: OpenSearch Security Plugin REST Account Action Groups API
  slug: open-opensearch-action-groups-api
- collection_type: open
  name: OpenSearch Security Plugin REST Account Allowlist API
  slug: open-opensearch-allowlist-api
- collection_type: open
  name: OpenSearch Security Plugin REST Account Audit API
  slug: open-opensearch-audit-api
- collection_type: open
  name: OpenSearch Security Plugin REST Account Cache API
  slug: open-opensearch-cache-api
- collection_type: open
  name: OpenSearch Security Plugin REST Account Certificates API
  slug: open-opensearch-certificates-api
- collection_type: open
  name: OpenSearch Security Plugin REST Account Health API
  slug: open-opensearch-health-api
- collection_type: open
  name: OpenSearch Security Plugin REST Account Internal Users API
  slug: open-opensearch-internal-users-api
- collection_type: open
  name: OpenSearch Security Plugin REST Account Nodes DN API
  slug: open-opensearch-nodes-dn-api
- collection_type: open
  name: OpenSearch Security Plugin REST Account Role Mappings API
  slug: open-opensearch-role-mappings-api
- collection_type: open
  name: OpenSearch Security Plugin REST Account Roles API
  slug: open-opensearch-roles-api
- collection_type: open
  name: OpenSearch Security Plugin REST Account Security Config API
  slug: open-opensearch-security-config-api
- collection_type: open
  name: OpenSearch Security Plugin REST API
  slug: open-opensearch-security
- collection_type: open
  name: OpenSearch Security Plugin REST Account SSL Info API
  slug: open-opensearch-ssl-info-api
- collection_type: open
  name: OpenSearch Security Plugin REST Account Tenants API
  slug: open-opensearch-tenants-api
common:
- group: commercial
  href: https://artifacts.apis.io/opensearch/plans/opensearch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/opensearch-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/opensearch/rate-limits/opensearch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/opensearch-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/opensearch/finops/opensearch-finops.yml
  title: ''
  type: FinOps
  url: finops/opensearch-finops.yml
- group: other
  href: https://artifacts.apis.io/opensearch/capabilities/opensearch-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/opensearch-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/opensearch/agentic-access/opensearch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/opensearch-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/opensearch/security/opensearch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/opensearch-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/opensearch/authentication/opensearch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/opensearch-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/opensearch-project
- group: company
  title: ''
  type: Website
  url: https://opensearch.org/
- group: start
  title: ''
  type: Portal
  url: https://docs.opensearch.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.opensearch.org/latest/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.opensearch.org/latest/getting-started/
- group: operate
  title: ''
  type: Community
  url: https://opensearch.org/community/
- group: operate
  title: ''
  type: Forums
  url: https://forum.opensearch.org/
- group: company
  title: ''
  type: Blog
  url: https://opensearch.org/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opensearch-project
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/opensearch-project/security
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/opensearch-project/OpenSearch
- group: other
  title: ''
  type: Download
  url: https://opensearch.org/downloads/
- group: commercial
  title: ''
  type: License
  url: https://opensearch.org/license.html
- group: auth
  title: ''
  type: Security
  url: https://opensearch.org/security
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/opensearch-project/opensearch-mcp-server-py
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/opensearch-project/opensearch-agent-skills
created: '2025-01-08'
description: OpenSearch is the open source, community-driven search, analytics, and observability suite (forked from Elasticsearch and Kibana) maintained under the Linux Foundation's OpenSearch Software Foundation. The platform exposes REST APIs across the search engine, the OpenSearch Dashboards UI, and a set of plugins. The Security plugin REST API lets administrators programmatically create and manage internal users, roles, role mappings, action groups, tenants, security configuration, audit log configuration, and SSL certificates.
finops:
- has_sources: false
  method: generated
  name: Opensearch Finops
  primary_unit: request
  service_category: API
  slug: opensearch-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/opensearch.png
json_schemas:
- name: OpenSearch Security Role
  property_count: 7
  slug: opensearch-role
jsonld:
- class_count: 3
  name: Opensearch Context
  property_count: 0
  slug: opensearch-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: OpenSearch
nav: Providers
network: true
overview: 'OpenSearch publishes 15 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Action Groups API, Allowlist API, and 12 more. Tagged areas include OpenSearch, Search, Analytics, Observability, and Open Source.


  The OpenSearch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenSearch''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 18 more developer resources.'
plans:
- name: Opensearch Plans Pricing
  plan_count: 3
  slug: opensearch-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Opensearch Rate Limits
  slug: opensearch-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: OpenSearch — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: opensearch-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 56.7
    catalog_earned_first_party: 0.0
    catalog_gap: 58.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 9.8
    contract_quality: 49.3
    developer_ergonomics: 54.0
    discoverability: 65.0
    operational_transparency: 23.7
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/opensearch/opensearch-2026-06-20T191032.png
security:
- kind: authentication
  name: Opensearch Authentication
  slug: opensearch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Opensearch Domain Security
  slug: opensearch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 10
skills:
- name: aoss-nextgen-provisioning
  slug: aoss-nextgen-provisioning
- name: aws-setup
  slug: aws-setup
- name: cloud
  slug: cloud
- name: log-analytics
  slug: log-analytics
- name: observability
  slug: observability
- name: opensearch-launchpad
  slug: opensearch-launchpad
- name: opensearch-skills
  slug: opensearch-skills
- name: search
  slug: search
- name: solr-opensearch-migration-advisor
  slug: solr-opensearch-migration-advisor
- name: trace-analytics
  slug: trace-analytics
slug: opensearch
tags:
- OpenSearch
- Search
- Analytics
- Observability
- Open Source
- Security
website: https://opensearch.org/
---
