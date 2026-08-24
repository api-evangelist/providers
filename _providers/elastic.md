---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Elastic Agentic Access
  operation_count: 21
  slug: elastic-agentic-access
  summary_line: 21 operations · 7 acting
api_count: 12
apis:
- description: Account-level information.
  name: Elastic Account API
  slug: elastic-account-api
- description: Cluster health, state, and statistics.
  name: Elastic Cluster API
  slug: elastic-cluster-api
- description: Manage data views (formerly index patterns).
  name: Elastic DataViews API
  slug: elastic-dataviews-api
- description: Manage Elasticsearch and Kibana deployments.
  name: Elastic Deployments API
  slug: elastic-deployments-api
- description: Index, update, retrieve, and delete documents.
  name: Elastic Documents API
  slug: elastic-documents-api
- description: Manage indices, mappings, and settings.
  name: Elastic Indices API
  slug: elastic-indices-api
- description: Manage Kibana saved objects (dashboards, visualizations, searches).
  name: Elastic SavedObjects API
  slug: elastic-savedobjects-api
- description: Search and query operations across indices.
  name: Elastic Search API
  slug: elastic-search-api
- description: Roles, users, API keys, and access control.
  name: Elastic Security API
  slug: elastic-security-api
- description: Manage Kibana Spaces.
  name: Elastic Spaces API
  slug: elastic-spaces-api
- description: Kibana server status.
  name: Elastic Status API
  slug: elastic-status-api
- description: IP and VPC traffic filter rulesets for deployments.
  name: Elastic TrafficFilters API
  slug: elastic-trafficfilters-api
artifact_total: 59
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Elastic Cloud Account API
  slug: open-elastic-account-api
- collection_type: open
  name: Elastic Cloud API
  slug: open-elastic-cloud
- collection_type: open
  name: Elastic Cloud Account Cluster API
  slug: open-elastic-cluster-api
- collection_type: open
  name: Elastic Cloud Account DataViews API
  slug: open-elastic-dataviews-api
- collection_type: open
  name: Elastic Cloud Account Deployments API
  slug: open-elastic-deployments-api
- collection_type: open
  name: Elastic Cloud Account Documents API
  slug: open-elastic-documents-api
- collection_type: open
  name: Elasticsearch REST API
  slug: open-elastic-elasticsearch
- collection_type: open
  name: Elastic Cloud Account Indices API
  slug: open-elastic-indices-api
- collection_type: open
  name: Kibana API
  slug: open-elastic-kibana
- collection_type: open
  name: Elastic Cloud Account SavedObjects API
  slug: open-elastic-savedobjects-api
- collection_type: open
  name: Elastic Cloud Account Search API
  slug: open-elastic-search-api
- collection_type: open
  name: Elastic Cloud Account Security API
  slug: open-elastic-security-api
- collection_type: open
  name: Elastic Cloud Account Spaces API
  slug: open-elastic-spaces-api
- collection_type: open
  name: Elastic Cloud Account Status API
  slug: open-elastic-status-api
- collection_type: open
  name: Elastic Cloud Account TrafficFilters API
  slug: open-elastic-trafficfilters-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elastic-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/elastic-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elastic-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elastic-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elastic-co
- group: company
  title: ''
  type: Website
  url: https://www.elastic.co
- group: docs
  title: ''
  type: Documentation
  url: https://www.elastic.co/guide/index.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/elastic
- group: start
  title: ''
  type: Console
  url: https://cloud.elastic.co
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elastic.co/pricing
- group: commercial
  title: ''
  type: License
  url: https://www.elastic.co/licensing/elastic-license
- group: agent
  title: ''
  type: LlmsText
  url: https://api.elastic-cloud.com/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.elastic.co/blog/feed
created: '2025-01-08'
description: Elastic is a software company that builds search-powered solutions for observability, security, and search use cases. The Elastic Stack (Elasticsearch, Kibana, and related tools) lets organizations ingest, search, analyze, and visualize structured and unstructured data in real time. Elastic Cloud delivers managed Elasticsearch and Kibana deployments with REST APIs for both data operations and deployment management.
features:
- 'Elastic Cloud Hosted: resource-based with Standard/Gold/Platinum/Enterprise tiers'
- 'Elastic Serverless: VCU + storage usage-based for Search/Observability/Security'
- 'Self-managed: license-based for on-prem deployment'
- 'Multi-cloud: AWS, GCP, Azure'
- REST API for Elasticsearch, Kibana, APM
- Bulk indexing API for high-throughput ingest
- Throughput scales with cluster hardware
- OAuth + API keys + JWT realm
- Watcher for alerting on rules
- ES|QL query language
- Vector search with kNN
- ELSER (Elastic Learned Sparse Encoder) for semantic search
- Cross-cluster search/replication
- Hot/Warm/Cold/Frozen data tiers
- Index Lifecycle Management (ILM)
- 'Compliance: SOC 2, HIPAA, FedRAMP (Enterprise)'
finops:
- name: Elastic Finops
  service_category: Search and Observability
  slug: elastic-finops
graphqls:
- description: This conceptual GraphQL schema covers the Elastic platform — Elasticsearch, Kibana, APM, Machine Learning, Security, and Fleet. It maps the REST API surface described at [https://www.elastic.co/docs/a
  name: Elastic GraphQL Schema
  slug: elastic-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elastic.png
json_schemas:
- name: Deployment
  property_count: 4
  slug: elastic-deployment
- name: Document
  property_count: 4
  slug: elastic-document
- name: SavedObject
  property_count: 4
  slug: elastic-savedobject
- name: SearchResponse
  property_count: 3
  slug: elastic-searchresponse
- name: Space
  property_count: 4
  slug: elastic-space
json_structures:
- name: Elastic Structure
  property_count: 0
  slug: elastic-structure
layout: provider
modified: '2026-05-19'
name: Elastic
nav: Providers
network: true
overview: 'Elastic publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account API, Cluster API, DataViews API, and 9 more. Tagged areas include Search, Analytics, Observability, Security, and Visualization.


  The Elastic catalog on APIs.io includes 1 Spectral governance ruleset.


  Elastic''s developer surface includes authentication, documentation, GitHub presence, developer console, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Elastic Plans Pricing
  plan_count: 3
  slug: elastic-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Elastic Rate Limits
  slug: elastic-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Elastic API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: elastic-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.9
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 9.8
    contract_quality: 58.4
    developer_ergonomics: 31.0
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elastic/refs/heads/main/screenshots/elastic-2026-06-20T180547.png
security:
- kind: authentication
  name: Elastic Authentication
  slug: elastic-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Elastic Domain Security
  slug: elastic-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Elastic Trust Center
  slug: elastic-trust-center
  summary_line: GDPR
slug: elastic
tags:
- Search
- Analytics
- Observability
- Security
- Visualization
- Cloud
website: https://www.elastic.co
---
