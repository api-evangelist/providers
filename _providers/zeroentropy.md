---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.zeroentropy.dev/v1
  baseurl_source: declared
  description: The Admin API from ZeroEntropy — 7 operation(s) for admin.
  name: ZeroEntropy Admin API
  slug: zeroentropy-admin-api
- baseURL: https://api.zeroentropy.dev/v1
  baseurl_source: declared
  description: The Collections API from ZeroEntropy — 3 operation(s) for collections.
  name: ZeroEntropy Collections API
  slug: zeroentropy-collections-api
- baseURL: https://api.zeroentropy.dev/v1
  baseurl_source: declared
  description: The Documents API from ZeroEntropy — 8 operation(s) for documents.
  name: ZeroEntropy Documents API
  slug: zeroentropy-documents-api
- baseURL: https://api.zeroentropy.dev/v1
  baseurl_source: declared
  description: The Models API from ZeroEntropy — 2 operation(s) for models.
  name: ZeroEntropy Models API
  slug: zeroentropy-models-api
- baseURL: https://api.zeroentropy.dev/v1
  baseurl_source: declared
  description: The Queries API from ZeroEntropy — 3 operation(s) for queries.
  name: ZeroEntropy Queries API
  slug: zeroentropy-queries-api
- baseURL: https://api.zeroentropy.dev/v1
  baseurl_source: declared
  description: The Status API from ZeroEntropy — 1 operation(s) for status.
  name: ZeroEntropy Status API
  slug: zeroentropy-status-api
- baseURL: https://api.zeroentropy.dev/v1
  baseurl_source: declared
  description: The Usage API from ZeroEntropy — 6 operation(s) for usage.
  name: ZeroEntropy Usage API
  slug: zeroentropy-usage-api
artifact_total: 18
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: ZeroEntropy
nav: Providers
network: true
overview: 'ZeroEntropy publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Collections API, Documents API, and 4 more. Tagged areas include Company, Enterprise Saas, Artificial Intelligence, Search, and Retrieval.


  ZeroEntropy''s developer surface includes authentication, documentation, API reference, quickstart, signup flow, pricing, engineering blog, and 14 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 41.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 4.5
    contract_quality: 58.8
    developer_ergonomics: 54.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 41.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zeroentropy/refs/heads/main/screenshots/zeroentropy-2026-08-17T083058.png
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
