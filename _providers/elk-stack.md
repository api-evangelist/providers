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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
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
artifact_total: 16
collections:
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
random_paper: 28
rate_limits:
- limit_count: 5
  name: Elk Stack Rate Limits
  slug: elk-stack-rate-limits
score:
  band: thin
  composite: 42.7
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 48.7
    developer_ergonomics: 37.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.7
  schema_version: 0.5
  scored_at: '2026-07-23'
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
