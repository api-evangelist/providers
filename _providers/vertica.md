---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 41.3
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 1
  name: Vertica Agentic Access
  operation_count: 2
  slug: vertica-agentic-access
  summary_line: 2 operations · 1 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: Agent-backed REST API used by Vertica Management Console for monitoring, provisioning, and managing Vertica databases and clusters. Returns JSON responses for node, database, and cluster operations.
  name: Vertica Management Console REST API
  slug: management-console-api
- description: The Health API from Vertica — 1 operation(s) for health.
  name: Vertica Health API
  slug: vertica-health-api
- description: The Lifecycle API from Vertica — 1 operation(s) for lifecycle.
  name: Vertica Lifecycle API
  slug: vertica-lifecycle-api
artifact_total: 7
collections:
- collection_type: open
  name: Vertica Node Management Agent (NMA) API
  slug: open-vertica
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vertica-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vertica-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vertica-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/vertica-co
- group: company
  title: ''
  type: Website
  url: https://www.vertica.com
- group: other
  title: ''
  type: Product Page
  url: https://www.opentext.com/products/analytics-database
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vertica.com/
- group: operate
  title: ''
  type: Community Edition
  url: https://docs.vertica.com/latest/en/getting-started/community-edition-ce/
- group: operate
  title: ''
  type: Community
  url: https://community.opentext.com/data-analytics/analytics-db
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vertica
- group: build
  title: ''
  type: GitHub vcluster
  url: https://github.com/vertica/vcluster
- group: operate
  title: ''
  type: Support
  url: https://www.opentext.com/support
- group: other
  title: ''
  type: Parent Company
  url: https://www.opentext.com/
created: '2026-05-11'
description: Vertica (now branded OpenText Analytics Database) is a high-performance, columnar, MPP analytics database designed for petabyte-scale data warehousing, data lakehouse, and advanced analytics workloads across on-premises, cloud, and Kubernetes deployments. The platform delivers in-database machine learning, geospatial and time-series analytics, separation of storage and compute, and broad SQL compatibility. Vertica exposes a REST API via the Node Management Agent (NMA) for programmatic cluster and database operations authenticated with mutual TLS.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vertica.png
layout: provider
modified: '2026-05-11'
name: Vertica
nav: Providers
network: true
overview: 'Vertica publishes 2 APIs on the [APIs.io](https://apis.io/) network: Health API and Lifecycle API. Tagged areas include Database, Analytics Database, Data Warehouse, Data Lakehouse, and Columnar Database.


  Vertica''s developer surface includes authentication, documentation, support, and 10 more developer resources.'
random_paper: 36
score:
  band: emerging
  composite: 25.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 53.1
    developer_ergonomics: 23.9
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 25.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vertica/refs/heads/main/screenshots/vertica-2026-06-20T200949.png
security:
- kind: authentication
  name: Vertica Authentication
  slug: vertica-authentication
  summary_line: mutualTLS · 1 scheme
- kind: domain-security
  name: Vertica Domain Security
  slug: vertica-domain-security
  summary_line: TLSv1.3 · DMARC
slug: vertica
tags:
- Database
- Analytics Database
- Data Warehouse
- Data Lakehouse
- Columnar Database
- MPP
- In-Database Machine Learning
- SQL
website: https://www.vertica.com
---
