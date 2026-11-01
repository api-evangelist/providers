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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Elasticsearch Agentic Access
  operation_count: 17
  slug: elasticsearch-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 1
apis:
- baseURL: https://localhost:9200
  baseurl_source: declared
  description: The Cat API from Elasticsearch — 3 operation(s) for cat.
  name: Elasticsearch Cat API
  slug: elasticsearch-cat-api
- baseURL: https://localhost:9200
  baseurl_source: declared
  description: The Cluster API from Elasticsearch — 3 operation(s) for cluster.
  name: Elasticsearch Cluster API
  slug: elasticsearch-cluster-api
- baseURL: https://localhost:9200
  baseurl_source: declared
  description: The Document API from Elasticsearch — 3 operation(s) for document.
  name: Elasticsearch Document API
  slug: elasticsearch-document-api
- baseURL: https://localhost:9200
  baseurl_source: declared
  description: The Index API from Elasticsearch — 1 operation(s) for index.
  name: Elasticsearch Index API
  slug: elasticsearch-index-api
- baseURL: https://localhost:9200
  baseurl_source: declared
  description: The Search API from Elasticsearch — 1 operation(s) for search.
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
artifact_total: 41
collections:
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
- group: commercial
  href: https://artifacts.apis.io/elasticsearch/plans/elasticsearch-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/elasticsearch-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/elasticsearch/rate-limits/elasticsearch-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/elasticsearch-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/elasticsearch/finops/elasticsearch-finops.yml
  title: ''
  type: FinOps
  url: finops/elasticsearch-finops.yml
- group: agent
  href: https://artifacts.apis.io/elasticsearch/agentic-access/elasticsearch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/elasticsearch-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/elasticsearch/packages/elasticsearch-packages.yml
  title: ''
  type: Packages
  url: packages/elasticsearch-packages.yml
- group: agent
  href: https://artifacts.apis.io/elasticsearch/well-known/elasticsearch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elasticsearch-well-known.yml
- group: agent
  href: https://artifacts.apis.io/elasticsearch/mcp/elasticsearch-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/elasticsearch-mcp.yml
- group: agent
  href: https://artifacts.apis.io/elasticsearch/llms/elasticsearch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elasticsearch-llms.txt
- group: other
  href: https://artifacts.apis.io/elasticsearch/overlays/elasticsearch-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/elasticsearch-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/elasticsearch/conformance/elasticsearch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elasticsearch-conformance.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/errors/elasticsearch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elasticsearch-problem-types.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/lifecycle/elasticsearch-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/elasticsearch-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/conventions/elasticsearch-conventions.yml
  title: ''
  type: Conventions
  url: conventions/elasticsearch-conventions.yml
- group: operate
  href: https://artifacts.apis.io/elasticsearch/changelog/elasticsearch-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/elasticsearch-changelog.yml
- group: build
  href: https://artifacts.apis.io/elasticsearch/cli/elasticsearch-cli.yml
  title: ''
  type: CLI
  url: cli/elasticsearch-cli.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/components/elasticsearch-components.yml
  title: ''
  type: Components
  url: components/elasticsearch-components.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/data-model/elasticsearch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/elasticsearch-data-model.yml
- group: auth
  href: https://artifacts.apis.io/elasticsearch/security/elasticsearch-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/elasticsearch-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/elasticsearch/security/elasticsearch-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/elasticsearch-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/elasticsearch/security/elasticsearch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elasticsearch-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/elasticsearch/authentication/elasticsearch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/elasticsearch-authentication.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/arazzo/elasticsearch-index-bootstrap-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-index-bootstrap-workflow.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/arazzo/elasticsearch-index-teardown-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-index-teardown-workflow.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/arazzo/elasticsearch-document-lifecycle-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-document-lifecycle-workflow.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/arazzo/elasticsearch-upsert-document-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-upsert-document-workflow.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/arazzo/elasticsearch-document-purge-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-document-purge-workflow.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/arazzo/elasticsearch-search-and-fetch-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-search-and-fetch-workflow.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/arazzo/elasticsearch-bulk-load-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/elasticsearch-bulk-load-workflow.yml
- group: design
  href: https://artifacts.apis.io/elasticsearch/arazzo/elasticsearch-cluster-health-triage-workflow.yml
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
- has_sources: true
  method: derived
  name: Elasticsearch Finops
  primary_unit: ''
  service_category: ''
  slug: elasticsearch-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elasticsearch.png
layout: provider
mcp_servers:
- description: MCP server; 5 tools listed.
  name: Elasticsearch MCP Server
  slug: elasticsearch
modified: '2026-06-20'
name: Elasticsearch
nav: Providers
network: true
overview: 'Elasticsearch publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cat API, Cluster API, Document API, and 2 more. Tagged areas include Analytics, Database, Full-Text Search, NoSQL, and Search.


  Elasticsearch''s developer surface includes changelog, CLI, authentication, documentation, getting-started guide, engineering blog, pricing, and 33 more developer resources.'
plans:
- name: Elasticsearch Plans Pricing
  plan_count: 0
  slug: elasticsearch-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 2
  name: Elasticsearch Rate Limits
  slug: elasticsearch-rate-limits
score:
  band: developing
  composite: 44.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 34.0
    catalog_earned_first_party: 0.0
    catalog_gap: 81.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 39.5
    contract_governance: 4.5
    contract_quality: 42.2
    developer_ergonomics: 47.6
    discoverability: 63.3
    operational_transparency: 52.6
  previous_composite: 51.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/elasticsearch/elasticsearch-2026-06-20T180540.png
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
