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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 17.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Elastic Stack Agentic Access
  operation_count: 10
  slug: elastic-stack-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 7
apis:
- description: Data visualization and exploration tool API for Elasticsearch, providing dashboards, saved objects, alerting, and spaces management.
  name: Kibana API
  slug: kibana-api
- baseURL: https://localhost:9200
  baseurl_source: declared
  description: The Bulk API from Elastic Stack — 1 operation(s) for bulk.
  name: Elastic Stack Bulk API
  slug: elastic-stack-bulk-api
- baseURL: https://localhost:9200
  baseurl_source: declared
  description: The Cluster API from Elastic Stack — 1 operation(s) for cluster.
  name: Elastic Stack Cluster API
  slug: elastic-stack-cluster-api
- baseURL: https://localhost:9200
  baseurl_source: declared
  description: The Doc API from Elastic Stack — 1 operation(s) for doc.
  name: Elastic Stack Doc API
  slug: elastic-stack-doc-api
- baseURL: https://localhost:9200
  baseurl_source: declared
  description: The Elasticsearch API API from Elastic Stack — 1 operation(s) for elasticsearch api.
  name: Elastic Stack Elasticsearch API API
  slug: elastic-stack-elasticsearch-api-api
- baseURL: https://localhost:9200
  baseurl_source: declared
  description: The Search API from Elastic Stack — 1 operation(s) for search.
  name: Elastic Stack Search API
  slug: elastic-stack-search-api
- baseURL: https://localhost:9200
  baseurl_source: declared
  description: The Settings API from Elastic Stack — 1 operation(s) for settings.
  name: Elastic Stack Settings API
  slug: elastic-stack-settings-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Elasticsearch Bulk API
  slug: open-elastic-stack-bulk-api
- collection_type: open
  name: Elasticsearch Bulk Cluster API
  slug: open-elastic-stack-cluster-api
- collection_type: open
  name: Elasticsearch Bulk Doc API
  slug: open-elastic-stack-doc-api
- collection_type: open
  name: Elasticsearch Bulk Elasticsearch API API
  slug: open-elastic-stack-elasticsearch-api-api
- collection_type: open
  name: Elasticsearch Bulk Search API
  slug: open-elastic-stack-search-api
- collection_type: open
  name: Elasticsearch Bulk Settings API
  slug: open-elastic-stack-settings-api
- collection_type: open
  name: Elasticsearch API
  slug: open-elastic-stack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elastic-stack-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/elastic-stack-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elastic-stack-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.elastic.co/
- group: docs
  title: ''
  type: Documentation
  url: https://www.elastic.co/guide/index.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elastic.co/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.elastic.co/blog
- group: operate
  title: ''
  type: Support
  url: https://www.elastic.co/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elastic.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elastic.co/agreements
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elastic.co/legal/privacy-statement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elastic
created: '2024-01-01'
description: The Elastic Stack (formerly known as the ELK Stack) is a collection of open-source products from Elastic designed to help users take data from any source, in any format, and search, analyze, and visualize that data in real-time. The stack includes Elasticsearch for search and analytics, Kibana for visualization, Logstash for data processing, and Beats for data shipping.
finops:
- name: Elastic Stack Finops
  service_category: API
  slug: elastic-stack-finops
graphqls:
- description: 'This GraphQL schema provides a conceptual representation of the Elastic Stack APIs, covering Elasticsearch search and indexing, Kibana visualization, Logstash data processing, and Beats data shipping '
  name: Elastic Stack GraphQL Schema
  slug: elastic-stack-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elastic-stack.png
layout: provider
modified: '2026-05-19'
name: Elastic Stack
nav: Providers
network: true
overview: 'Elastic Stack publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Bulk API, Cluster API, Doc API, and 3 more. Tagged areas include Analytics, Logging, Monitoring, Observability, and Search.


  Elastic Stack''s developer surface includes documentation, pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Elastic Stack Plans Pricing
  plan_count: 3
  slug: elastic-stack-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Elastic Stack Rate Limits
  slug: elastic-stack-rate-limits
score:
  band: thin
  composite: 27.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 19.7
    developer_ergonomics: 16.7
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 27.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elastic-stack/refs/heads/main/screenshots/elastic-stack-2026-06-20T180536.png
security:
- kind: domain-security
  name: Elastic Stack Domain Security
  slug: elastic-stack-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Elastic Stack Trust Center
  slug: elastic-stack-trust-center
  summary_line: GDPR
slug: elastic-stack
tags:
- Analytics
- Logging
- Monitoring
- Observability
- Search
website: https://www.elastic.co/
---
