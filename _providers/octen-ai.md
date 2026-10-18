---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.1
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Octen Ai Agentic Access
  operation_count: 18
  slug: octen-ai-agentic-access
  summary_line: 18 operations · 15 acting
api_count: 2
apis:
- description: Hosted Model Context Protocol server exposing Octen broad_search, search, image_search, video_search and extract tools at https://mcp.octen.ai/mcp (x-api-key or OAuth), also runnable locally via npx o
  name: Octen MCP Server
  slug: octen-mcp-server
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Answer API from Octen — 1 operation(s) for answer.
  name: Octen Answer API
  slug: octen-ai-answer-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Broad Search API from Octen — 1 operation(s) for broad search.
  name: Octen Broad Search API
  slug: octen-ai-broad-search-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Business Search API from Octen — 1 operation(s) for business search.
  name: Octen Business Search API
  slug: octen-ai-business-search-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Embedding API from Octen — 1 operation(s) for embedding.
  name: Octen Embedding API
  slug: octen-ai-embedding-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Extract API from Octen — 1 operation(s) for extract.
  name: Octen Extract API
  slug: octen-ai-extract-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Grounded Generation API from Octen — 2 operation(s) for grounded generation.
  name: Octen Grounded Generation API
  slug: octen-ai-grounded-generation-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Image Search API from Octen — 1 operation(s) for image search.
  name: Octen Image Search API
  slug: octen-ai-image-search-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Images API from Octen — 1 operation(s) for images.
  name: Octen Images API
  slug: octen-ai-images-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Messages API from Octen — 1 operation(s) for messages.
  name: Octen Messages API
  slug: octen-ai-messages-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The News Search API from Octen — 1 operation(s) for news search.
  name: Octen News Search API
  slug: octen-ai-news-search-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Research API from Octen — 1 operation(s) for research.
  name: Octen Research API
  slug: octen-ai-research-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Search API from Octen — 1 operation(s) for search.
  name: Octen Search API
  slug: octen-ai-search-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Video Search API from Octen — 1 operation(s) for video search.
  name: Octen Video Search API
  slug: octen-ai-video-search-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Videos API from Octen — 2 operation(s) for videos.
  name: Octen Videos API
  slug: octen-ai-videos-api
- baseURL: https://api.octen.ai
  baseurl_source: declared
  description: The Vl Embedding API from Octen — 1 operation(s) for vl embedding.
  name: Octen Vl Embedding API
  slug: octen-ai-vl-embedding-api
- baseURL: https://mcp.octen.ai
  baseurl_source: declared
  description: The Chat Completions API from Octen — 1 operation(s) for chat completions.
  name: Octen Chat Completions API
  slug: octen-ai-chat-completions-api
artifact_total: 32
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/overlays/octen-ai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/octen-ai-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/agentic-access/octen-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/octen-ai-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/rate-limits/octen-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/octen-ai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/plans/octen-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/octen-ai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/rules/octen-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/octen-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/json-ld/octen-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/octen-ai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/vocabulary/octen-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/octen-ai-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/data-model/octen-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/octen-ai-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/cli/octen-ai-cli.yml
  title: ''
  type: CLI
  url: cli/octen-ai-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/changelog/octen-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/octen-ai-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/conventions/octen-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/octen-ai-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://docs.octen.ai/resources/security-&-compliance
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/security/octen-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/octen-ai-trust-center.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.octen.ai
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/lifecycle/octen-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/octen-ai-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/errors/octen-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/octen-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/conformance/octen-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/octen-ai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/llms/octen-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/octen-ai-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/a2a/octen-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/octen-ai-a2a.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/mcp/octen-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/octen-ai-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/mcp/octen-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/octen-ai-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/well-known/octen-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/octen-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/hosts/octen-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/octen-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/vendors/octen-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/octen-ai-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/packages/octen-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/octen-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/packages/octen-ai-packages.yml
  title: ''
  type: Packages
  url: packages/octen-ai-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/authentication/octen-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/octen-ai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://octen.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.octen.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.octen.ai/api-reference/broad-search
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.octen.ai/overview/quickstart
- group: start
  title: ''
  type: DeveloperPortal
  url: https://octen.ai/platform/api-keys
- group: start
  title: ''
  type: SignUp
  url: https://auth.octen.ai
- group: company
  title: ''
  type: Blog
  url: https://octen.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Octen-Team
- group: commercial
  title: ''
  type: Pricing
  url: https://octen.ai/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.octen.ai/resources/changelog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://octen.ai/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://octen.ai/terms-of-service
- group: operate
  title: ''
  type: SLA
  url: https://docs.octen.ai/resources/sla
- group: operate
  title: ''
  type: Support
  url: mailto:support@octen.ai
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/security/octen-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/octen-ai-domain-security.yml
created: '2026-10-07'
description: Octen (Octen.AI) is an AI-native web search and retrieval platform built for LLM applications and agents. Its REST API at api.octen.ai exposes Broad Search (multi-angle query decomposition), Web Search, News Search, Business Search, Image Search, Video Search, URL Extract, text and vision-language Embeddings, Answer, Deep Research, Grounded Generation, and an OpenAI/Anthropic-compatible Model Gateway, alongside a hosted MCP server (mcp.octen.ai), a CLI, a Python SDK, and published agent skills.
image: https://octen.ai/_next/static/media/octen-cover.dc74905e.png
json_schemas:
- name: BusinessSearchRequest
  property_count: 12
  slug: octen-ai-business-search-request
- name: ChatCompletionRequest
  property_count: 31
  slug: octen-ai-chat-completion-request
- name: DeepResearchChunk
  property_count: 18
  slug: octen-ai-deep-research-chunk
- name: ExtractRequest
  property_count: 10
  slug: octen-ai-extract-request
- name: MessagesRequest
  property_count: 15
  slug: octen-ai-messages-request
- name: NewsSearchRequest
  property_count: 12
  slug: octen-ai-news-search-request
jsonld:
- class_count: 120
  name: Octen Ai Context
  property_count: 259
  slug: octen-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.octen.ai over streamable HTTP requiring an API key; 6 tools listed.
  name: Octen MCP
  slug: octen-mcp
modified: '2026-10-07'
name: Octen
nav: Providers
network: true
overview: 'Octen publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Answer API, Broad Search API, Business Search API, and 14 more. Tagged areas include Search, Web Search, Artificial Intelligence, LLM, and Embeddings.


  The Octen catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Octen''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, signup flow, and 36 more developer resources.'
plans:
- name: Octen Ai Plans Pricing
  plan_count: 5
  slug: octen-ai-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 17
  name: Octen Ai Rate Limits
  slug: octen-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Octen API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: octen-ai-rules
score:
  band: exemplar
  composite: 71.5
  coverage:
    artifact_dirs: 30
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.3
  facets:
    access_clarity: 92.1
    contract_governance: 35.6
    contract_quality: 66.8
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 68.4
  previous_composite: 71.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/octen-ai/refs/heads/main/screenshots/octen-ai-2026-10-11T111925.png
security:
- kind: authentication
  name: Octen Ai Authentication
  slug: octen-ai-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Octen Ai Domain Security
  slug: octen-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Octen Ai Trust Center
  slug: octen-ai-trust-center
  summary_line: SOC 2 Type II (Certified), HIPAA (In progress)
slug: octen-ai
tags:
- Search
- Web Search
- Artificial Intelligence
- LLM
- Embeddings
- Content Extraction
- Model Gateway
- MCP
- Agents
- Deep Research
- Company
website: https://octen.ai
---
