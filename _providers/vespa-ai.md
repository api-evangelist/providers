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
- acting_count: 1
  human_in_the_loop: 0
  name: Vespa Ai Agentic Access
  operation_count: 2
  slug: vespa-ai-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 8
apis:
- description: The Vespa Document API (/document/v1) provides synchronous REST access to document operations against a Vespa content cluster. It supports Put, Get, Update (partial update with assign/add/remove opera
  name: Vespa Document API
  slug: vespa-document-api
- description: The Vespa Deploy API (/application/v2) manages application packages on a Vespa configuration server. It supports preparing, activating, and tearing down application packages, session-based deployments
  name: Vespa Deploy API
  slug: vespa-deploy-api
- description: 'The Vespa Tenant API (/application/v2/tenant) manages tenants and applications hosted on a Vespa configuration server or Vespa Cloud control plane. It exposes operations for creating tenants, listing '
  name: Vespa Tenant and Application API
  slug: vespa-tenant-api
- description: The Vespa Config API (/config/v2) lets services in a Vespa application retrieve their configuration from a Vespa configuration server using the config-server / config-proxy protocol. It is primarily u
  name: Vespa Config API
  slug: vespa-config-api
- description: The Vespa Cluster Controller API (/cluster/v2) exposes runtime state and management endpoints for a Vespa content cluster — including node state queries, maintenance-mode transitions, and storage clus
  name: Vespa Cluster Controller API
  slug: vespa-cluster-api
- description: 'The Vespa State API (/state/v1) exposes per-service health, version, and metrics endpoints for any Vespa node — used by orchestration tooling, monitoring agents, and load balancers to check liveness, '
  name: Vespa State API
  slug: vespa-state-api
- description: Vespa exposes a family of metrics endpoints (/metrics/v1, /metrics/v2, /prometheus/v1) that publish Vespa engine and application metrics in JSON or Prometheus exposition format for scraping by Prometh
  name: Vespa Metrics API
  slug: vespa-metrics-api
- description: The Query API from Vespa — 1 operation(s) for query.
  name: Vespa Query API
  slug: vespa-ai-query-api
artifact_total: 63
collections:
- collection_type: postman
  name: Vespa Query API
  slug: postman-vespa-ai-query-api
- collection_type: open
  name: Vespa Query API
  slug: open-vespa-query-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vespa/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vespa-ai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vespa-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vespa-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vespa-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://vespa.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vespa.ai/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.vespa.ai/en/getting-started.html
- group: learn
  title: ''
  type: Tutorials
  url: https://docs.vespa.ai/en/learn/tutorials/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vespa-engine
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/vespa-engine/vespa
- group: commercial
  title: ''
  type: License
  url: https://github.com/vespa-engine/vespa/blob/master/LICENSE
- group: company
  title: ''
  type: Blog
  url: https://blog.vespa.ai/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.vespa.ai/feed.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.vespa.ai/pricing
- group: start
  title: ''
  type: Console
  url: https://console.vespa-cloud.com/
- group: operate
  title: ''
  type: Slack
  url: https://slack.vespa.ai/
- group: operate
  title: ''
  type: Support
  url: https://github.com/vespa-engine/vespa/issues
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/vespa-engine/vespa/releases
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vespa-engine/vespa/tree/master/client/go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vespa-engine/pyvespa
- group: build
  title: ''
  type: SDKs
  url: https://vespa-engine.github.io/pyvespa/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vespa-engine/vespa/tree/master/vespa-feed-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vespa-engine/vespa-search
- group: build
  title: ''
  type: SampleApps
  url: https://github.com/vespa-engine/sample-apps
- group: other
  title: ''
  type: PrometheusExporter
  url: https://github.com/vespa-engine/vespa_exporter
- group: other
  title: ''
  type: DockerImage
  url: https://github.com/vespa-engine/docker-image
- group: build
  title: ''
  type: GitHubAction
  url: https://github.com/vespa-engine/setup-vespa-cli-action
- group: design
  title: ''
  type: SpectralRules
  url: rules/vespa-ai-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vespa-ai-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/vespa-ai-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: plans/vespa-ai-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vespa-ai-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vespa-ai-finops.yml
created: '2026-05-25'
description: Vespa is an open-source AI search engine, big-data serving engine, and vector database originally developed inside Yahoo and spun out as Vespa.ai AS. Vespa combines vector search, text search (BM25), structured filtering, and machine-learned ranking — including native tensor inference — into a single distributed serving engine that scales to billions of documents with sub-100ms latency. Vespa Cloud is the fully managed commercial offering operated by the Vespa.ai team across AWS and GCP, with Startup, Basic, Commercial, and Enterprise plans plus a Self-Managed option for customers running the open-source engine on their own infrastructure. Vespa is widely used at Spotify, Perplexity, Yahoo, Farfetch, and Elicit for search, recommendation, personalization, and Retrieval-Augmented Generation (RAG).
examples:
- key_count: 2
  name: Vespa Ai Document Put Example
  slug: vespa-ai-document-put-example
- key_count: 2
  name: Vespa Ai Query Example
  slug: vespa-ai-query-example
features:
- Open-source under Apache 2.0
- Vector search with HNSW indexes
- BM25 text search and hybrid search
- Native tensor and ML model inference at serving time
- YQL (Vespa Query Language) for structured queries
- Multi-phase ranking (match-phase, first-phase, second-phase, global-phase)
- Document API with conditional writes, visits, and JSON Lines streaming
- Multi-tenant namespaces and document groups
- Real-time indexing with sub-100ms query latency
- Distributed content clusters with automatic sharding and replication
- Streaming search mode for personal/private corpora
- Built-in machine learning inference (TensorFlow, ONNX, XGBoost, LightGBM)
- Approximate nearest neighbor and exact nearest neighbor operators
- Application packages with schemas, services.xml, and rank profiles
- Container API for custom searchers, document processors, and handlers
- Self-managed (Apache 2.0) or fully managed Vespa Cloud (AWS, GCP)
- Vespa Cloud Startup plan from $0.05 / vCPU-hour, $0.005 / GiB-memory-hour
- Vespa Cloud Commercial plan with 24/7 1-hour SLA support
- Vespa Cloud Enterprise plan with $20k/month minimum and 15-minute SLA
- Up to 50% volume discounts and 15% committed-spend discount
finops:
- name: Vespa Ai Finops
  service_category: AI Search Platform
  slug: vespa-ai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vespa-ai.png
integrations:
- name: AWS
- name: Google Cloud
- name: Prometheus
- name: Grafana
- name: TensorFlow
- name: ONNX Runtime
- name: XGBoost
- name: LightGBM
- name: Kubernetes
- name: LangChain
- name: LlamaIndex
- name: Haystack
json_schemas:
- name: VespaDocument
  property_count: 3
  slug: vespa-ai-document
- name: VespaQuery
  property_count: 10
  slug: vespa-ai-query
json_structures:
- name: Vespa Ai Document Structure
  property_count: 0
  slug: vespa-ai-document-structure
jsonld:
- class_count: 11
  name: Vespa Ai Context
  property_count: 6
  slug: vespa-ai-context
layout: provider
modified: '2026-05-25'
name: Vespa
nav: Providers
network: true
overview: 'Vespa publishes 2 APIs on the [APIs.io](https://apis.io/) network: Document API and Query API. Tagged areas include AI, Search, Vector Database, Big Data, and Machine Learning.


  The Vespa catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vespa''s developer surface includes authentication, documentation, getting-started guide, engineering blog, pricing, developer console, support, and 27 more developer resources.'
plans:
- name: Vespa Ai Plans Pricing
  plan_count: 6
  slug: vespa-ai-plans-pricing
random_paper: 61
rate_limits:
- limit_count: 6
  name: Vespa Ai Rate Limits
  slug: vespa-ai-rate-limits
rules:
- name: Vespa API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vespa-ai-jsonschema-spectral-rules
- name: Vespa API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 7
  slug: vespa-ai-rules
score:
  band: strong
  composite: 59.6
  delta: -3.2
  facets:
    commercial_clarity: 50.0
    contract_quality: 61.9
    developer_ergonomics: 63.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 62.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vespa-ai/refs/heads/main/screenshots/vespa-ai-2026-06-20T201005.png
security:
- kind: authentication
  name: Vespa Ai Authentication
  slug: vespa-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vespa Ai Domain Security
  slug: vespa-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vespa Ai Vulnerability Disclosure
  slug: vespa-ai-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
slug: vespa-ai
tags:
- AI
- Search
- Vector Database
- Big Data
- Machine Learning
- Semantic Search
- Retrieval Augmented Generation
- Open Source
- Tensor
- Recommendations
use_cases:
- description: Combine BM25 text relevance with vector similarity and structured filters in a single query executed by Vespa's multi-phase ranking pipeline.
  name: Hybrid Search
- description: Serve grounded context to large language models by indexing documents, chunks, and embeddings in Vespa and retrieving them with hybrid search at sub-100ms latency.
  name: Retrieval Augmented Generation
- description: Power recommendation systems with machine-learned ranking, real-time feature updates, and tensor inference over user and item embeddings.
  name: Recommendation and Personalization
- description: Match candidate ads against user context and serve ranked impressions within tight latency budgets using Vespa's distributed serving engine.
  name: Ad Targeting and Real-Time Bidding
- description: Combine faceted navigation, structured filters, text relevance, and learned ranking for large product catalogs with frequent updates.
  name: E-Commerce Search and Browse
- description: Run "streaming search" mode that scans a user's personal corpus on demand — ideal for mail, messaging, and document search where each user has their own private index.
  name: Streaming Search for Personal Data
website: https://vespa.ai
---
