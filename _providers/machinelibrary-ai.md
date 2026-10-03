---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
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
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 65.7
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Machinelibrary Ai Agentic Access
  operation_count: 42
  slug: machinelibrary-ai-agentic-access
  summary_line: 42 operations · 18 acting
api_count: 4
apis:
- description: Hosted Streamable-HTTP MCP server at https://mcp.machinelibrary.ai (legacy https://mcp.spacefrontiers.org still served) exposing four read-only, idempotent retrieval tools (spacefrontiers_search_docum
  name: Machine Library MCP Server
  slug: machine-library-mcp-server
- description: 'A2A (protocolVersion 0.3.0) research and commerce agent at https://machinelibrary.ai/a2a over JSON-RPC: grounded research answers with citation artifacts, search-access guidance, and prepaid-credit sa'
  name: Machine Library A2A Agent
  slug: machine-library-a2a-agent
- description: 'Self-hosted, MIT-licensed Rust search engine published by Space Frontiers (github.com/SpaceFrontiers/hermes) with a published protobuf wire contract: hermes.SearchService (Search, GetDocument, GetInde'
  name: Hermes Search Engine gRPC API
  slug: hermes-search-engine-grpc-api
- baseURL: https://api.machinelibrary.ai
  baseurl_source: declared
  description: Fetch documents by ID or canonical URI.
  name: Space Frontiers Documents API
  slug: machinelibrary-ai-documents-api
- baseURL: https://api.machinelibrary.ai
  baseurl_source: declared
  description: The Payments API from Space Frontiers — 1 operation(s) for payments.
  name: Space Frontiers Payments API
  slug: machinelibrary-ai-payments-api
- baseURL: https://api.machinelibrary.ai
  baseurl_source: declared
  description: Authenticated, feature-gated streaming of PDF, EPUB, and DJVU library originals.
  name: Space Frontiers Raw document downloads API
  slug: machinelibrary-ai-raw-document-downloads-api
- baseURL: https://api.machinelibrary.ai
  baseurl_source: declared
  description: 'Document recognition: PDF, EPUB, and DJVU to structured Markdown with quality reports.'
  name: Space Frontiers Recognition API
  slug: machinelibrary-ai-recognition-api
- baseURL: https://api.machinelibrary.ai
  baseurl_source: declared
  description: Ranked retrieval and document similarity.
  name: Space Frontiers Search API
  slug: machinelibrary-ai-search-api
- baseURL: https://mcp.machinelibrary.ai
  baseurl_source: declared
  description: Retrieval-augmented conversation workflows.
  name: Space Frontiers Conversations API
  slug: machinelibrary-ai-conversations-api
artifact_total: 30
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/agentic-access/machinelibrary-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/machinelibrary-ai-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/rules/machinelibrary-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/machinelibrary-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/json-ld/machinelibrary-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/machinelibrary-ai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/vocabulary/machinelibrary-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/machinelibrary-ai-vocabulary.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/security/machinelibrary-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/machinelibrary-ai-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/hosts/machinelibrary-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/machinelibrary-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/vendors/machinelibrary-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/machinelibrary-ai-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://machinelibrary.ai/status
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/security/machinelibrary-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/machinelibrary-ai-vulnerability-disclosure.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/machinelibrary-ai/refs/heads/main/overlays/machinelibrary-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/machinelibrary-ai-openapi-overlay.yaml
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
json_schemas:
- name: AgentCommentSubmission
  property_count: 9
  slug: machinelibrary-ai-agent-comment-submission
- name: ByUriResponse
  property_count: 0
  slug: machinelibrary-ai-by-uri-response
- name: ConversationRequest
  property_count: 11
  slug: machinelibrary-ai-conversation-request
- name: ConversationResponse
  property_count: 10
  slug: machinelibrary-ai-conversation-response
- name: FeedbackAccepted
  property_count: 2
  slug: machinelibrary-ai-feedback-accepted
- name: RecognitionJobStatus
  property_count: 11
  slug: machinelibrary-ai-recognition-job-status
- name: RecognitionSubmission
  property_count: 3
  slug: machinelibrary-ai-recognition-submission
- name: SearchFeedback
  property_count: 6
  slug: machinelibrary-ai-search-feedback
- name: SearchRequestV2
  property_count: 36
  slug: machinelibrary-ai-search-request-v2
- name: SimilarRequestV2
  property_count: 4
  slug: machinelibrary-ai-similar-request-v2
- name: V2DocumentResponse
  property_count: 3
  slug: machinelibrary-ai-v2-document-response
- name: V2SearchResponse
  property_count: 10
  slug: machinelibrary-ai-v2-search-response
jsonld:
- class_count: 59
  name: Machinelibrary Ai Context
  property_count: 202
  slug: machinelibrary-ai-context
layout: provider
mcp_servers:
- description: ''
  name: Space Frontiers MCP Server
  slug: space-frontiers-mcp-server
modified: '2026-09-19'
name: Space Frontiers
nav: Providers
network: true
overview: 'Space Frontiers publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Payments API, Raw document downloads API, and 6 more. Tagged areas include Research, Scholarly Search, Full-Text Search, Retrieval, and RAG.


  The Space Frontiers catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Space Frontiers'' developer surface includes documentation, API reference, getting-started guide, pricing, support, signup flow, authentication, and 37 more developer resources.'
plans:
- name: Machinelibrary Ai Plans Pricing
  plan_count: 2
  slug: machinelibrary-ai-plans-pricing
random_paper: 13
rules:
- effective_rule_count: 57
  extends:
  - spectral:oas
  name: Space Frontiers API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 2
    warn: 5
  slug: machinelibrary-ai-rules
scopes:
- name: Machinelibrary Ai Scopes
  scope_count: 0
  slug: machinelibrary-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.8
    catalog_earned_first_party: 8.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 10.5
  facets:
    access_clarity: 65.8
    contract_governance: 35.6
    contract_quality: 63.4
    developer_ergonomics: 59.5
    discoverability: 72.5
    operational_transparency: 44.7
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 40.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
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
- kind: vulnerability-disclosure
  name: Machinelibrary Ai Vulnerability Disclosure
  slug: machinelibrary-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
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
- Agent-Native
- AI Agents
- Data
- Search
website: https://machinelibrary.ai/
---
