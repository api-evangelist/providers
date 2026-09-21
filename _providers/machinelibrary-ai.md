---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 61.4
  scored_at: '2026-09-20'
api_count: 2
apis:
- baseURL: https://api.machinelibrary.ai
  baseurl_source: declared
  description: 'REST API over the Machine Library corpus: hybrid full-text search across the documents and social indexes (POST /v2/search/), similarity search, token-bounded document fetch by ID or canonical URI (DO'
  name: Machine Library API
  slug: machine-library-api
- description: Hosted Streamable-HTTP MCP server at https://mcp.machinelibrary.ai (legacy https://mcp.spacefrontiers.org still served) exposing four read-only, idempotent retrieval tools (spacefrontiers_search_docum
  name: Machine Library MCP Server
  slug: machine-library-mcp-server
- description: 'A2A (protocolVersion 0.3.0) research and commerce agent at https://machinelibrary.ai/a2a over JSON-RPC: grounded research answers with citation artifacts, search-access guidance, and prepaid-credit sa'
  name: Machine Library A2A Agent
  slug: machine-library-a2a-agent
- description: 'Self-hosted, MIT-licensed Rust search engine published by Space Frontiers (github.com/SpaceFrontiers/hermes) with a published protobuf wire contract: hermes.SearchService (Search, GetDocument, GetInde'
  name: Hermes Search Engine gRPC API
  slug: hermes-search-engine-grpc-api
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://machinelibrary.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://machinelibrary.ai/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://machinelibrary.ai/docs/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://machinelibrary.ai/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://machinelibrary.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://machinelibrary.ai/contacts
- group: company
  title: ''
  type: Newsroom
  url: https://machinelibrary.ai/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SpaceFrontiers
- group: start
  title: ''
  type: SignUp
  url: https://machinelibrary.ai/auth/signup
- group: start
  title: ''
  type: Login
  url: https://machinelibrary.ai/auth/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://machinelibrary.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://machinelibrary.ai/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/llms/machinelibrary-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/machinelibrary-ai-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/mcp/machinelibrary-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/machinelibrary-ai-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/mcp/machinelibrary-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/machinelibrary-ai-tool-crosswalk.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/a2a/machinelibrary-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/machinelibrary-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/well-known/machinelibrary-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/machinelibrary-ai-well-known.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/packages/machinelibrary-ai-packages.yml
  title: ''
  type: Packages
  url: packages/machinelibrary-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/packages/machinelibrary-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/machinelibrary-ai-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/conformance/machinelibrary-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/machinelibrary-ai-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/authentication/machinelibrary-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/machinelibrary-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/scopes/machinelibrary-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/machinelibrary-ai-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/conventions/machinelibrary-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/machinelibrary-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/conventions/machinelibrary-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/machinelibrary-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/errors/machinelibrary-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/machinelibrary-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/lifecycle/machinelibrary-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/machinelibrary-ai-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/security/machinelibrary-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/machinelibrary-ai-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/plans/machinelibrary-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/machinelibrary-ai-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/rate-limits/machinelibrary-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/machinelibrary-ai-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/changelog/machinelibrary-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/machinelibrary-ai-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/data-model/machinelibrary-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/machinelibrary-ai-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/regulatory/machinelibrary-ai-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/machinelibrary-ai-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/grpc/machinelibrary-ai-hermes.proto
  title: ''
  type: Protobuf
  url: grpc/machinelibrary-ai-hermes.proto
created: '2026-09-19'
description: 'Space Frontiers is a Wyoming corporation whose search and AI product, Machine Library (formerly Space Frontiers search, moved to machinelibrary.ai on 2026-09-12), is a full-text retrieval API and hosted MCP server over a corpus of roughly 2.9 billion records: peer-reviewed papers (CrossRef, PubMed, arXiv), books, USPTO patents, Wikipedia, technical standards, YouTube transcripts, and live Reddit, Telegram and Discord posts. It is built for AI agents doing literature review, fact-checking, citation walking and grounded research synthesis, returning compact reranked hits with canonical source URIs (DOI, arXiv, PMID, ISBN) and token-bounded full text. Three surfaces share one account and API key: a REST API at api.machinelibrary.ai (OpenAPI 3.1, pay-as-you-go), a Streamable-HTTP MCP server at mcp.machinelibrary.ai (OAuth 2.1 with PKCE and RFC 7591 dynamic registration, or a Bearer API key), and an A2A agent at machinelibrary.ai/a2a. It also ships a PDF/EPUB/DJVU-to-Markdown recognition
  API and Stripe-settled prepaid credit packages for agents (ACP checkout, MPP top-up). The company also publishes Hermes, an open-source Rust search engine with a gRPC contract and Python/TypeScript clients.'
image: https://machinelibrary.ai/press/icon-512.png
layout: provider
mcp_servers:
- description: ''
  name: Space Frontiers MCP Server
  slug: space-frontiers-mcp-server
modified: '2026-09-19'
name: Space Frontiers
nav: Providers
network: true
overview: 'Space Frontiers publishes 1 API on the [APIs.io](https://apis.io/) network: Machine Library API. Tagged areas include Research, Scholarly Search, Full-Text Search, Retrieval, and RAG.


  Space Frontiers'' developer surface includes documentation, API reference, getting-started guide, pricing, support, signup flow, authentication, and 27 more developer resources.'
plans:
- name: Machinelibrary Ai Plans Pricing
  plan_count: 2
  slug: machinelibrary-ai-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Machinelibrary Ai Rate Limits
  slug: machinelibrary-ai-rate-limits
scopes:
- name: Machinelibrary Ai Scopes
  scope_count: 0
  slug: machinelibrary-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 49.9
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 54.7
    developer_ergonomics: 59.5
    discoverability: 66.7
    operational_transparency: 18.4
  previous_composite: 5.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 64.8
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Machinelibrary Ai Authentication
  slug: machinelibrary-ai-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Machinelibrary Ai Domain Security
  slug: machinelibrary-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: machinelibrary-ai
tags:
- Research
- Scholarly Search
- Full-Text Search
- Retrieval
- RAG
- Patents
- Documents
- OCR
- Document Recognition
- MCP
- A2A
- agent-native
- AI Agents
- Data
- Search
website: https://machinelibrary.ai/
---
