---
access_model:
  confidence: medium
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Elasticsearch Agentic Access
  operation_count: 17
  slug: elasticsearch-agentic-access
  summary_line: 17 operations · 7 acting
api_count: 5
apis:
- description: The Cat API from Elasticsearch — 3 operation(s) for cat.
  name: Elasticsearch Cat API
  slug: elasticsearch-cat-api
- description: The Cluster API from Elasticsearch — 3 operation(s) for cluster.
  name: Elasticsearch Cluster API
  slug: elasticsearch-cluster-api
- description: The Document API from Elasticsearch — 3 operation(s) for document.
  name: Elasticsearch Document API
  slug: elasticsearch-document-api
- description: The Index API from Elasticsearch — 1 operation(s) for index.
  name: Elasticsearch Index API
  slug: elasticsearch-index-api
- description: The Search API from Elasticsearch — 1 operation(s) for search.
  name: Elasticsearch Search API
  slug: elasticsearch-search-api
arazzos:
- description: Check the cluster can take writes, push an NDJSON bulk payload, verify the resulting document count, and inspect the index.
  name: Elasticsearch Bulk Load and Verify
  slug: elasticsearch-bulk-load-workflow
- description: Walk cluster health, the cat health and nodes views, cluster stats, and cluster state to triage a degraded cluster.
  name: Elasticsearch Cluster Health Triage
  slug: elasticsearch-cluster-health-triage-workflow
- description: Index a document by id, read it back, apply a partial update, and confirm the merged result.
  name: Elasticsearch Document Lifecycle
  slug: elasticsearch-document-lifecycle-workflow
- description: Locate a document by a business key, delete it by its internal id, and prove it is no longer retrievable or searchable.
  name: Elasticsearch Purge a Document by Business Key
  slug: elasticsearch-document-purge-workflow
- description: Check the cluster is ready, create an index only if it does not already exist, and read back its settings and mappings.
  name: Elasticsearch Bootstrap an Index
  slug: elasticsearch-index-bootstrap-workflow
- description: Confirm an index exists, capture its definition for the record, delete it, and verify it is gone.
  name: Elasticsearch Tear Down an Index
  slug: elasticsearch-index-teardown-workflow
- description: Run a quick URI search to size a result set, re-run it as a paged DSL query, and fetch the full source of the top hit.
  name: Elasticsearch Search and Fetch the Top Hit
  slug: elasticsearch-search-and-fetch-workflow
- description: Search an index for a document matching a business key and update it if found, otherwise index a new one.
  name: Elasticsearch Upsert a Document by Business Key
  slug: elasticsearch-upsert-document-workflow
artifact_total: 42
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Elasticsearch REST API
  slug: open-elastic-search
- collection_type: open
  name: Elasticsearch REST Cat API
  slug: open-elasticsearch-cat-api
- collection_type: open
  name: Elasticsearch REST Cat Cluster API
  slug: open-elasticsearch-cluster-api
- collection_type: open
  name: Elasticsearch REST Cat Document API
  slug: open-elasticsearch-document-api
- collection_type: open
  name: Elasticsearch REST Cat Index API
  slug: open-elasticsearch-index-api
- collection_type: open
  name: Elasticsearch REST Cat Search API
  slug: open-elasticsearch-search-api
- collection_type: open
  name: Elasticsearch REST API
  slug: open-elasticsearch
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elasticsearch-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/elasticsearch-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/elasticsearch-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/elasticsearch-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elasticsearch-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/elasticsearch-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/elasticsearch-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elasticsearch-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elasticsearch-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elasticsearch-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/elasticsearch-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/elasticsearch-cli.yml
- group: design
  title: ''
  type: Components
  url: components/elasticsearch-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/elasticsearch-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/elasticsearch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/elasticsearch-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elasticsearch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elasticsearch-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-index-bootstrap-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-index-teardown-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-document-lifecycle-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-upsert-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-document-purge-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-search-and-fetch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-bulk-load-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-cluster-health-triage-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elastic-co
- group: company
  title: ''
  type: Website
  url: https://www.elastic.co/elasticsearch/
- group: docs
  title: ''
  type: Documentation
  url: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html
- group: company
  title: ''
  type: Blog
  url: https://www.elastic.co/blog/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elastic.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elastic.co/agreements/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elastic.co/legal/privacy-statement
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elastic.co/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.elastic.co/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elastic
created: '2024-01-01'
description: Elasticsearch is an open source search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. It provides a RESTful API for indexing, searching, and managing data, with powerful aggregation capabilities and real-time analytics at scale.
features:
- 'Elasticsearch (Elastic): hundreds of services across Search and Observability'
- 'Detailed pricing: see https://www.elastic.co/pricing'
- 'Service: Elasticsearch Service'
- 'Service: Kibana'
- 'Service: Logstash'
- 'Service: Beats'
- 'Service: APM'
- 'Service: Synthetics'
- 'Service: Security (SIEM, Endpoint)'
- 'Service: Maps'
- 'Service: Canvas'
- 'Service: Stack Monitoring'
finops:
- name: Elasticsearch Finops
  service_category: Search and Observability
  slug: elasticsearch-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elasticsearch.png
layout: provider
mcp_servers:
- description: ''
  name: Elasticsearch MCP Server
  slug: elasticsearch-mcp-server
modified: '2026-06-20'
name: Elasticsearch
nav: Providers
network: true
overview: 'Elasticsearch publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cat API, Cluster API, Document API, and 2 more. Tagged areas include Analytics, Database, Full-Text Search, NoSQL, and Search.


  Elasticsearch''s developer surface includes changelog, CLI, authentication, documentation, getting-started guide, engineering blog, pricing, and 30 more developer resources.'
plans:
- name: Elasticsearch Plans Pricing
  plan_count: 3
  slug: elasticsearch-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Elasticsearch Rate Limits
  slug: elasticsearch-rate-limits
score:
  band: developing
  composite: 44.5
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 46.9
    developer_ergonomics: 47.6
    discoverability: 72.2
    governance: 16.7
    operational_transparency: 39.5
  previous_composite: 44.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elasticsearch/refs/heads/main/screenshots/elasticsearch-2026-06-20T180540.png
security:
- kind: authentication
  name: Elasticsearch Authentication
  slug: elasticsearch-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Elasticsearch Domain Security
  slug: elasticsearch-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Elasticsearch Vulnerability Disclosure
  slug: elasticsearch-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Elasticsearch Trust Center
  slug: elasticsearch-trust-center
  summary_line: GDPR
slug: elasticsearch
tags:
- Analytics
- Database
- Full-Text Search
- NoSQL
- Search
website: https://www.elastic.co/elasticsearch/
---
