---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Milvus Agentic Access
  operation_count: 29
  slug: milvus-agentic-access
  summary_line: 29 operations · 19 acting
api_count: 1
apis:
- description: 'Milvus v2 REST API covers collections, partitions, vectors, search, query, indexes, and role/RBAC management. Authentication: Bearer token formed from `username:password` when auth is enabled (off by '
  name: Milvus REST API v2
  slug: milvus-rest-api-v2
- description: gRPC is the canonical, high-throughput interface to Milvus. The official SDKs are gRPC-based; the REST API is a thin wrapper for non-Go/Python/Java clients.
  name: Milvus gRPC API
  slug: milvus-grpc
- baseURL: http://{milvus_host}:19530/v2/vectordb
  baseurl_source: declared
  description: The Collections API from Milvus — 11 operation(s) for collections.
  name: Milvus Collections API
  slug: milvus-collections-api
- baseURL: http://{milvus_host}:19530/v2/vectordb
  baseurl_source: declared
  description: The Entities API from Milvus — 7 operation(s) for entities.
  name: Milvus Entities API
  slug: milvus-entities-api
- baseURL: http://{milvus_host}:19530/v2/vectordb
  baseurl_source: declared
  description: The Indexes API from Milvus — 4 operation(s) for indexes.
  name: Milvus Indexes API
  slug: milvus-indexes-api
- baseURL: http://{milvus_host}:19530/v2/vectordb
  baseurl_source: declared
  description: The Partitions API from Milvus — 3 operation(s) for partitions.
  name: Milvus Partitions API
  slug: milvus-partitions-api
- baseURL: http://{milvus_host}:19530/v2/vectordb
  baseurl_source: declared
  description: The Roles API from Milvus — 2 operation(s) for roles.
  name: Milvus Roles API
  slug: milvus-roles-api
- baseURL: http://{milvus_host}:19530/v2/vectordb
  baseurl_source: declared
  description: The Users API from Milvus — 2 operation(s) for users.
  name: Milvus Users API
  slug: milvus-users-api
artifact_total: 22
collections:
- collection_type: open
  name: Milvus REST Collections API
  slug: open-milvus-collections-api
- collection_type: open
  name: Milvus REST Collections Entities API
  slug: open-milvus-entities-api
- collection_type: open
  name: Milvus REST Collections Indexes API
  slug: open-milvus-indexes-api
- collection_type: open
  name: Milvus REST Collections Partitions API
  slug: open-milvus-partitions-api
- collection_type: open
  name: Milvus REST Collections Roles API
  slug: open-milvus-roles-api
- collection_type: open
  name: Milvus REST Collections Users API
  slug: open-milvus-users-api
- collection_type: open
  name: Milvus REST API
  slug: open-milvus
common:
- group: other
  href: https://artifacts.apis.io/milvus/capabilities/milvus-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/milvus-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/milvus-io/milvus/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/milvus-io/milvus/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/milvus-io/milvus/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/milvus-io/milvus/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/milvus-io/milvus/blob/master/LICENSE
- group: agent
  href: https://artifacts.apis.io/milvus/agentic-access/milvus-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/milvus-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/milvus/security/milvus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/milvus-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/milvus/authentication/milvus-authentication.yml
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
  href: https://artifacts.apis.io/milvus/plans/milvus-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/milvus-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/milvus/rate-limits/milvus-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/milvus-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/milvus/finops/milvus-finops.yml
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
- has_sources: true
  method: generated
  name: Milvus Finops
  primary_unit: ''
  service_category: Vector Database
  slug: milvus-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/milvus.png
layout: provider
modified: '2026-05-08'
name: Milvus
nav: Providers
network: true
overview: 'Milvus publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Collections API, Entities API, Indexes API, and 5 more. Tagged areas include Vector Search, Artificial Intelligence, Embeddings, Open Source, and Cloud-Native.


  The Milvus catalog on APIs.io includes 1 Spectral governance ruleset.


  Milvus'' developer surface includes authentication, developer portal, engineering blog, and 17 more developer resources.'
plans:
- name: Milvus Plans Pricing
  plan_count: 1
  slug: milvus-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Milvus Rate Limits
  slug: milvus-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Milvus API Rules
  rule_count: 54
  severity_counts:
    error: 51
    hint: 0
    info: 1
    warn: 2
  slug: milvus-rules
score:
  band: developing
  composite: 40.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 45.5
    catalog_earned_first_party: 0.0
    catalog_gap: 69.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 13.6
    contract_quality: 40.4
    developer_ergonomics: 48.8
    discoverability: 73.2
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 65.0
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/milvus/milvus-2026-06-20T185554.png
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
- Vector Search
- Artificial Intelligence
- Embeddings
- Open Source
- Cloud-Native
- Database
website: https://milvus.io/
---
