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
- acting_count: 6
  human_in_the_loop: 0
  name: Elastic Search Agentic Access
  operation_count: 11
  slug: elastic-search-agentic-access
  summary_line: 11 operations · 6 acting
api_count: 5
apis:
- description: The Cat API from Elasticsearch — 1 operation(s) for cat.
  name: Elasticsearch Cat API
  slug: elastic-search-cat-api
- description: The Cluster API from Elasticsearch — 1 operation(s) for cluster.
  name: Elasticsearch Cluster API
  slug: elastic-search-cluster-api
- description: The Document API from Elasticsearch — 2 operation(s) for document.
  name: Elasticsearch Document API
  slug: elastic-search-document-api
- description: The Index API from Elasticsearch — 1 operation(s) for index.
  name: Elasticsearch Index API
  slug: elastic-search-index-api
- description: The Search API from Elasticsearch — 1 operation(s) for search.
  name: Elasticsearch Search API
  slug: elastic-search-search-api
artifact_total: 13
collections:
- collection_type: open
  name: Elasticsearch REST API
  slug: open-elastic-search
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elastic-search-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/elastic-search-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elastic-search-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elastic-search-authentication.yml
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
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elastic.co/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.elastic.co/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elastic.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elastic.co/agreements/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elastic
created: '2024-01-01'
description: Elasticsearch is a distributed, RESTful search and analytics engine capable of addressing a growing number of use cases. As the heart of the Elastic Stack, it centrally stores data for fast search, fine-tuned relevancy, and powerful analytics that scale with ease. It provides a comprehensive REST API for document indexing, searching, aggregations, and cluster management.
finops:
- name: Elastic Search Finops
  service_category: API
  slug: elastic-search-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elastic-search.png
layout: provider
modified: '2026-04-28'
name: Elasticsearch
nav: Providers
network: true
overview: 'Elasticsearch publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Cat API, Cluster API, Document API, and 2 more. Tagged areas include Analytics, Database, Distributed Systems, Full-Text Search, and NoSQL.


  Elasticsearch''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, support, and 8 more developer resources.'
plans:
- name: Elastic Search Plans Pricing
  plan_count: 3
  slug: elastic-search-plans-pricing
random_paper: 39
rate_limits:
- limit_count: 5
  name: Elastic Search Rate Limits
  slug: elastic-search-rate-limits
score:
  band: developing
  composite: 47.4
  delta: -2.1
  facets:
    commercial_clarity: 68.4
    contract_quality: 49.2
    developer_ergonomics: 37.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elastic-search/refs/heads/main/screenshots/elastic-search-2026-06-20T180534.png
security:
- kind: authentication
  name: Elastic Search Authentication
  slug: elastic-search-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Elastic Search Domain Security
  slug: elastic-search-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Elastic Search Trust Center
  slug: elastic-search-trust-center
  summary_line: GDPR
slug: elastic-search
tags:
- Analytics
- Database
- Distributed Systems
- Full-Text Search
- NoSQL
- Search
website: https://www.elastic.co/elasticsearch/
---
