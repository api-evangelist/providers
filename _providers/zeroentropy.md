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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-08-17'
api_count: 7
apis:
- description: The Admin API from ZeroEntropy — 7 operation(s) for admin.
  name: ZeroEntropy Admin API
  slug: zeroentropy-admin-api
- description: The Collections API from ZeroEntropy — 3 operation(s) for collections.
  name: ZeroEntropy Collections API
  slug: zeroentropy-collections-api
- description: The Documents API from ZeroEntropy — 8 operation(s) for documents.
  name: ZeroEntropy Documents API
  slug: zeroentropy-documents-api
- description: The Models API from ZeroEntropy — 2 operation(s) for models.
  name: ZeroEntropy Models API
  slug: zeroentropy-models-api
- description: The Queries API from ZeroEntropy — 3 operation(s) for queries.
  name: ZeroEntropy Queries API
  slug: zeroentropy-queries-api
- description: The Status API from ZeroEntropy — 1 operation(s) for status.
  name: ZeroEntropy Status API
  slug: zeroentropy-status-api
- description: The Usage API from ZeroEntropy — 6 operation(s) for usage.
  name: ZeroEntropy Usage API
  slug: zeroentropy-usage-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ZeroEntropy Admin API
  slug: open-zeroentropy-admin-api
- collection_type: open
  name: ZeroEntropy Admin Collections API
  slug: open-zeroentropy-collections-api
- collection_type: open
  name: ZeroEntropy Admin Documents API
  slug: open-zeroentropy-documents-api
- collection_type: open
  name: ZeroEntropy Admin Models API
  slug: open-zeroentropy-models-api
- collection_type: open
  name: ZeroEntropy Admin Queries API
  slug: open-zeroentropy-queries-api
- collection_type: open
  name: ZeroEntropy Admin Status API
  slug: open-zeroentropy-status-api
- collection_type: open
  name: ZeroEntropy Admin Usage API
  slug: open-zeroentropy-usage-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zeroentropy-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zeroentropy-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/zeroentropy-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zeroentropy-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zeroentropy-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/zeroentropy-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/zeroentropy-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zeroentropy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zeroentropy-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.zeroentropy.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.zeroentropy.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.zeroentropy.dev/api-reference/
- group: start
  title: ''
  type: Quickstart
  url: https://docs.zeroentropy.dev/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.zeroentropy.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zeroentropy.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.zeroentropy.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zeroentropy-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zeroentropy.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zeroentropy.dev/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:founders@zeroentropy.dev
created: '2026-07-17'
description: ZeroEntropy builds specialized, lightweight AI models for information retrieval and retrieval-augmented generation (RAG). Its zerank rerankers and zembed embedding models improve the accuracy of any search pipeline, and its hosted retrieval API lets developers create collections, index documents, and run relevance queries (top documents, pages, and snippets) with metadata filtering. The API is a versioned (/v1) HTTP JSON service with US and EU data-center endpoints, official Python and TypeScript SDKs, and API-key bearer authentication. ZeroEntropy is a portfolio company of Initialized Capital operating in the enterprise AI / search sector.
image: https://zeroentropy.dev/assets/images/ze-logo.png
layout: provider
mcp_servers:
- description: ''
  name: zeroentropy-mcp.yml
  slug: zeroentropy-mcpyml
modified: '2026-07-21'
name: ZeroEntropy
nav: Providers
network: true
overview: 'ZeroEntropy publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Collections API, Documents API, and 4 more. Tagged areas include Company, Enterprise Saas, Artificial Intelligence, Search, and Retrieval.


  ZeroEntropy''s developer surface includes authentication, documentation, API reference, quickstart, signup flow, pricing, engineering blog, and 14 more developer resources.'
random_paper: 41
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.5
    developer_ergonomics: 53.8
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 48.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Zeroentropy Authentication
  slug: zeroentropy-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zeroentropy Domain Security
  slug: zeroentropy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Zeroentropy Trust Center
  slug: zeroentropy-trust-center
  summary_line: SOC 2, HIPAA
slug: zeroentropy
tags:
- Company
- Enterprise Saas
- Artificial Intelligence
- Search
- Retrieval
- Embeddings
- Reranking
- RAG
website: https://www.zeroentropy.dev/
---
