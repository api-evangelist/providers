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
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Elk Stack Agentic Access
  operation_count: 19
  slug: elk-stack-agentic-access
  summary_line: 19 operations · 10 acting
api_count: 8
apis:
- description: Data visualization and exploration tool for reviewing logs and events, providing real-time dashboards and analytics for Elasticsearch data.
  name: Kibana API
  slug: kibana-api
- description: The Cat API from Elastic Stack (ELK Stack) — 2 operation(s) for cat.
  name: Elastic Stack (ELK Stack) Cat API
  slug: elk-stack-cat-api
- description: The Cluster API from Elastic Stack (ELK Stack) — 4 operation(s) for cluster.
  name: Elastic Stack (ELK Stack) Cluster API
  slug: elk-stack-cluster-api
- description: The Document API from Elastic Stack (ELK Stack) — 4 operation(s) for document.
  name: Elastic Stack (ELK Stack) Document API
  slug: elk-stack-document-api
- description: The Index API from Elastic Stack (ELK Stack) — 3 operation(s) for index.
  name: Elastic Stack (ELK Stack) Index API
  slug: elk-stack-index-api
- description: The Ingest API from Elastic Stack (ELK Stack) — 1 operation(s) for ingest.
  name: Elastic Stack (ELK Stack) Ingest API
  slug: elk-stack-ingest-api
- description: The Search API from Elastic Stack (ELK Stack) — 2 operation(s) for search.
  name: Elastic Stack (ELK Stack) Search API
  slug: elk-stack-search-api
- description: The Snapshot API from Elastic Stack (ELK Stack) — 1 operation(s) for snapshot.
  name: Elastic Stack (ELK Stack) Snapshot API
  slug: elk-stack-snapshot-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Elasticsearch REST Cat API
  slug: open-elk-stack-cat-api
- collection_type: open
  name: Elasticsearch REST Cat Cluster API
  slug: open-elk-stack-cluster-api
- collection_type: open
  name: Elasticsearch REST Cat Document API
  slug: open-elk-stack-document-api
- collection_type: open
  name: Elasticsearch REST Cat Index API
  slug: open-elk-stack-index-api
- collection_type: open
  name: Elasticsearch REST Cat Ingest API
  slug: open-elk-stack-ingest-api
- collection_type: open
  name: Elasticsearch REST Cat Search API
  slug: open-elk-stack-search-api
- collection_type: open
  name: Elasticsearch REST Cat Snapshot API
  slug: open-elk-stack-snapshot-api
- collection_type: open
  name: Elasticsearch REST API
  slug: open-elk-stack
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elk-stack-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/elk-stack-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elk-stack-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elk-stack-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/elastic-co
- group: company
  title: ''
  type: Website
  url: https://www.elastic.co/elastic-stack/
- group: docs
  title: ''
  type: Documentation
  url: https://www.elastic.co/guide/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.elastic.co/guide/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.elastic.co/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.elastic.co/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.elastic.co/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elastic
created: '2024-01-01'
description: The Elastic Stack (formerly known as the ELK Stack) is a collection of open-source products from Elastic - Elasticsearch, Logstash, Kibana, and Beats - designed for taking data from any source, in any format, and searching, analyzing, and visualizing it in real time. Widely used for log management, observability, and security analytics.
finops:
- name: Elk Stack Finops
  service_category: API
  slug: elk-stack-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elk-stack.png
layout: provider
modified: '2026-03-16'
name: Elastic Stack (ELK Stack)
nav: Providers
network: true
overview: 'Elastic Stack (ELK Stack) publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Cat API, Cluster API, Document API, and 4 more. Tagged areas include Analytics, Logging, Monitoring, Observability, and Search.


  Elastic Stack (ELK Stack)''s developer surface includes authentication, documentation, getting-started guide, engineering blog, support, pricing, and 6 more developer resources.'
plans:
- name: Elk Stack Plans Pricing
  plan_count: 3
  slug: elk-stack-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Elk Stack Rate Limits
  slug: elk-stack-rate-limits
score:
  band: thin
  composite: 35.1
  delta: -0.4
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 46.2
    developer_ergonomics: 40.5
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 35.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/screenshots/elk-stack-2026-06-20T180610.png
security:
- kind: authentication
  name: Elk Stack Authentication
  slug: elk-stack-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Elk Stack Domain Security
  slug: elk-stack-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Elk Stack Trust Center
  slug: elk-stack-trust-center
  summary_line: GDPR
slug: elk-stack
tags:
- Analytics
- Logging
- Monitoring
- Observability
- Search
website: https://www.elastic.co/elastic-stack/
---
