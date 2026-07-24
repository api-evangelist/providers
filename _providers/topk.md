---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 32.7
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: Structured document store and query surface. Create collections with typed, indexed fields (keyword_index, semantic_index, vector index), upsert/update/delete documents by `_id`, and run hybrid querie
  name: TopK Collection API
  slug: collection-api
- description: Unstructured document ingestion, semantic search, and grounded question answering. Upload document files (PDF, Markdown, HTML, and more) to a dataset, retrieve the most relevant passages, and get evid
  name: TopK Dataset API
  slug: dataset-api
- description: Create, list, get, update, and delete datasets and collections that back TopK search and retrieval.
  name: TopK Management API
  slug: management-api
artifact_total: 8
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.topk.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.topk.io
- group: docs
  title: ''
  type: APIReference
  url: https://docs.topk.io/sdk/topk-py
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.topk.io/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.topk.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/topk-io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.topk.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.topk.io
- group: start
  title: ''
  type: Login
  url: https://console.topk.io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.topk.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://topk.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://topk.io/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://trust.topk.io
- group: auth
  title: ''
  type: TrustCenter
  url: security/topk-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://topk.io/security
- group: build
  title: ''
  type: Packages
  url: packages/topk-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/topk-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/topk-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/topk-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/topk-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/topk-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/topk-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/topk-authentication.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/topk-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/topk-changelog.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/topk-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/topk-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/topk-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/topk-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/topk-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: TopK is a search engine for accuracy-critical AI applications, delivering hybrid search, multi-vector (late-interaction) retrieval, dense and sparse vector search, BM25 keyword search, custom ranking, document parsing, and grounded question answering through a single API. Built on object storage for roughly 10x lower cost and effectively unlimited scale, TopK exposes a Collection API for structured document storage and querying, a Dataset API for unstructured document ingestion, semantic search, and evidence-backed answers, and a Management API for datasets and collections. It ships official Python, JavaScript, Rust, and SQL (PostgreSQL-wire) SDKs, a Homebrew-installable CLI, and a hosted MCP server so AI agents can query private data with natural language. TopK is developed by topk-io and is a portfolio company of Earlybird.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/topk.png
layout: provider
mcp_servers:
- description: ''
  name: topk-mcp.yml
  slug: topk-mcpyml
modified: '2026-07-21'
name: Topk
nav: Providers
network: true
overview: 'Topk publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Search, Vector Search, Hybrid Search, and Multi-Vector Retrieval.


  Topk''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, CLI, and 24 more developer resources.'
random_paper: 38
score:
  band: thin
  composite: 43.5
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 76.1
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 47.4
  previous_composite: 43.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Topk Authentication
  slug: topk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Topk Domain Security
  slug: topk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Topk Vulnerability Disclosure
  slug: topk-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Topk Trust Center
  slug: topk-trust-center
  summary_line: SOC 2
slug: topk
tags:
- Company
- Search
- Vector Search
- Hybrid Search
- Multi-Vector Retrieval
- Semantic Search
- BM25
- Retrieval
- RAG
- Question Answering
- AI Infrastructure
- Embeddings
- MCP
website: https://docs.topk.io
---
