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
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.4
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Opensearch Agentic Access
  operation_count: 47
  slug: opensearch-agentic-access
  summary_line: 47 operations · 27 acting
api_count: 15
apis:
- description: The core OpenSearch REST API for indexing documents, performing search queries (full text, vector, hybrid), aggregations, and managing indices, mappings, templates, aliases, and snapshots.
  name: OpenSearch Search and Indexing REST API
  slug: opensearch-search-api
- description: Self-service account endpoints for the calling user.
  name: OpenSearch Account API
  slug: opensearch-account-api
- description: Reusable groups of cluster and index permissions.
  name: OpenSearch Action Groups API
  slug: opensearch-action-groups-api
- description: Allowlist of HTTP APIs available to non-admin users.
  name: OpenSearch Allowlist API
  slug: opensearch-allowlist-api
- description: Audit log configuration.
  name: OpenSearch Audit API
  slug: opensearch-audit-api
- description: Manage the security cache.
  name: OpenSearch Cache API
  slug: opensearch-cache-api
- description: Inspect SSL certificates loaded by the cluster.
  name: OpenSearch Certificates API
  slug: opensearch-certificates-api
- description: Security plugin health check.
  name: OpenSearch Health API
  slug: opensearch-health-api
- description: CRUD for internal user database entries.
  name: OpenSearch Internal Users API
  slug: opensearch-internal-users-api
- description: Allowlisted distinguished names for cross-cluster nodes.
  name: OpenSearch Nodes DN API
  slug: opensearch-nodes-dn-api
- description: Map users, backend roles, and hosts to security roles.
  name: OpenSearch Role Mappings API
  slug: opensearch-role-mappings-api
- description: CRUD for security roles and their permissions.
  name: OpenSearch Roles API
  slug: opensearch-roles-api
- description: Inspect and update the running security configuration.
  name: OpenSearch Security Config API
  slug: opensearch-security-config-api
- description: Inspect SSL handshake information for the calling client.
  name: OpenSearch SSL Info API
  slug: opensearch-ssl-info-api
- description: Multi-tenancy support for OpenSearch Dashboards.
  name: OpenSearch Tenants API
  slug: opensearch-tenants-api
artifact_total: 52
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/opensearch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/opensearch-domain-security.yml
- group: auth
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
- group: docs
  title: ''
  type: GraphQL
  url: graphql/opensearch-graphql.md
created: '2025-01-08'
description: OpenSearch is the open source, community-driven search, analytics, and observability suite (forked from Elasticsearch and Kibana) maintained under the Linux Foundation's OpenSearch Software Foundation. The platform exposes REST APIs across the search engine, the OpenSearch Dashboards UI, and a set of plugins. The Security plugin REST API lets administrators programmatically create and manage internal users, roles, role mappings, action groups, tenants, security configuration, audit log configuration, and SSL certificates.
finops:
- name: Opensearch Finops
  service_category: API
  slug: opensearch-finops
graphqls:
- description: 'This directory contains a conceptual GraphQL schema for the OpenSearch search, analytics, and observability platform — the open-source, community-driven suite forked from Elasticsearch and Kibana and '
  name: OpenSearch GraphQL Schema
  slug: opensearch-graphql
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
overview: 'OpenSearch publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Account API, Action Groups API, Allowlist API, and 11 more. Tagged areas include Search, Analytics, Observability, Open-Source, and Security.


  The OpenSearch catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenSearch''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, and 15 more developer resources.'
plans:
- name: Opensearch Plans Pricing
  plan_count: 3
  slug: opensearch-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Opensearch Rate Limits
  slug: opensearch-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: OpenSearch API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: opensearch-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.0
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 58.6
    developer_ergonomics: 47.6
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/opensearch/refs/heads/main/screenshots/opensearch-2026-06-20T191032.png
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
- Search
- Analytics
- Observability
- Open-Source
- Security
website: https://opensearch.org/
---
