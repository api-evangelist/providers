---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 26
  human_in_the_loop: 0
  name: Milvus Agentic Access
  operation_count: 29
  slug: milvus-agentic-access
  summary_line: 29 operations · 26 acting
api_count: 8
apis:
- description: 'Milvus v2 REST API covers collections, partitions, vectors, search, query, indexes, and role/RBAC management. Authentication: Bearer token formed from `username:password` when auth is enabled (off by '
  name: Milvus REST API v2
  slug: milvus-rest-api-v2
- description: gRPC is the canonical, high-throughput interface to Milvus. The official SDKs are gRPC-based; the REST API is a thin wrapper for non-Go/Python/Java clients.
  name: Milvus gRPC API
  slug: milvus-grpc
- description: The Collections API from Milvus — 11 operation(s) for collections.
  name: Milvus Collections API
  slug: milvus-collections-api
- description: The Entities API from Milvus — 7 operation(s) for entities.
  name: Milvus Entities API
  slug: milvus-entities-api
- description: The Indexes API from Milvus — 4 operation(s) for indexes.
  name: Milvus Indexes API
  slug: milvus-indexes-api
- description: The Partitions API from Milvus — 3 operation(s) for partitions.
  name: Milvus Partitions API
  slug: milvus-partitions-api
- description: The Roles API from Milvus — 2 operation(s) for roles.
  name: Milvus Roles API
  slug: milvus-roles-api
- description: The Users API from Milvus — 2 operation(s) for users.
  name: Milvus Users API
  slug: milvus-users-api
artifact_total: 16
collections:
- collection_type: open
  name: Milvus REST API
  slug: open-milvus
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/milvus-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/milvus-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/milvus-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-milvus-project
- group: company
  title: ''
  type: Website
  url: https://milvus.io/
- group: start
  title: ''
  type: Portal
  url: https://milvus.io/docs/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/milvus-io/milvus
- group: other
  title: LF AI & Data
  type: Foundation
  url: https://lfaidata.foundation/projects/milvus/
- group: other
  title: Zilliz Cloud
  type: CommercialOffering
  url: https://zilliz.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/milvus-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/milvus-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/milvus-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://milvus.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://milvus.io/blog
created: '2026-05-08'
description: Milvus is an Apache 2.0 open-source vector database. It exposes a versioned REST API alongside gRPC and language SDKs (Python, Go, Java, Node.js). Maintained by Zilliz; LF AI & Data Foundation graduated project.
finops:
- name: Milvus Finops
  service_category: Vector Database
  slug: milvus-finops
graphqls:
- description: Milvus is an open-source vector database built for scalable similarity search. The API covers collection and index management, data insertion, vector search with filtering, partitions, and hybrid sear
  name: Milvus GraphQL API
  slug: milvus-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/milvus.png
layout: provider
modified: '2026-05-08'
name: Milvus
nav: Providers
network: true
overview: 'Milvus publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Entities API, Indexes API, and 3 more. Tagged areas include Vector Database, AI, Embeddings, Open Source, and Cloud-Native.


  Milvus'' developer surface includes authentication, developer portal, engineering blog, and 11 more developer resources.'
plans:
- name: Milvus Plans Pricing
  plan_count: 1
  slug: milvus-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 1
  name: Milvus Rate Limits
  slug: milvus-rate-limits
score:
  band: thin
  composite: 31.8
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 48.7
    developer_ergonomics: 21.7
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 31.8
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/milvus/refs/heads/main/screenshots/milvus-2026-06-20T185554.png
security:
- kind: authentication
  name: Milvus Authentication
  slug: milvus-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Milvus Domain Security
  slug: milvus-domain-security
  summary_line: TLSv1.3
slug: milvus
tags:
- Vector Database
- AI
- Embeddings
- Open Source
- Cloud-Native
website: https://milvus.io/
---
