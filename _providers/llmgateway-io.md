---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.3
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Llmgateway Io Agentic Access
  operation_count: 21
  slug: llmgateway-io-agentic-access
  summary_line: 21 operations · 14 acting
api_count: 2
apis:
- description: Model Context Protocol server (Streamable HTTP) at /mcp, as stated in the OpenAPI info.description; not probed further.
  name: LLM Gateway MCP Server
  slug: mcp
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Audio API from LLM Gateway — 2 operation(s) for audio.
  name: LLM Gateway Audio API
  slug: llmgateway-io-audio-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Decisions API from LLM Gateway — 1 operation(s) for decisions.
  name: LLM Gateway Decisions API
  slug: llmgateway-io-decisions-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Embeddings API from LLM Gateway — 1 operation(s) for embeddings.
  name: LLM Gateway Embeddings API
  slug: llmgateway-io-embeddings-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Images API from LLM Gateway — 2 operation(s) for images.
  name: LLM Gateway Images API
  slug: llmgateway-io-images-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Key API from LLM Gateway — 1 operation(s) for key.
  name: LLM Gateway Key API
  slug: llmgateway-io-key-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The LLM Gateway API API from LLM Gateway — 1 operation(s) for llm gateway api.
  name: LLM Gateway LLM Gateway API
  slug: llmgateway-io-llm-gateway-api-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Messages API from LLM Gateway — 1 operation(s) for messages.
  name: LLM Gateway Messages API
  slug: llmgateway-io-messages-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Models API from LLM Gateway — 1 operation(s) for models.
  name: LLM Gateway Models API
  slug: llmgateway-io-models-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Moderations API from LLM Gateway — 1 operation(s) for moderations.
  name: LLM Gateway Moderations API
  slug: llmgateway-io-moderations-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Ocr API from LLM Gateway — 1 operation(s) for ocr.
  name: LLM Gateway Ocr API
  slug: llmgateway-io-ocr-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Realtime API from LLM Gateway — 1 operation(s) for realtime.
  name: LLM Gateway Realtime API
  slug: llmgateway-io-realtime-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Rerank API from LLM Gateway — 1 operation(s) for rerank.
  name: LLM Gateway Rerank API
  slug: llmgateway-io-rerank-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Search API from LLM Gateway — 1 operation(s) for search.
  name: LLM Gateway Search API
  slug: llmgateway-io-search-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Systemone API from LLM Gateway — 1 operation(s) for systemone.
  name: LLM Gateway Systemone API
  slug: llmgateway-io-systemone-api
- baseURL: https://api.llmgateway.io
  baseurl_source: declared
  description: The Videos API from LLM Gateway — 4 operation(s) for videos.
  name: LLM Gateway Videos API
  slug: llmgateway-io-videos-api
- baseURL: https://api.llmgateway.io/mcp
  baseurl_source: declared
  description: The Chat Completions API from LLM Gateway — 1 operation(s) for chat completions.
  name: LLM Gateway Chat Completions API
  slug: llmgateway-io-chat-completions-api
artifact_total: 24
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/capabilities/llmgateway-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/llmgateway-io-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/agentic-access/llmgateway-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/llmgateway-io-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/rules/llmgateway-io-rules.yml
  title: ''
  type: Spectral
  url: rules/llmgateway-io-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/json-ld/llmgateway-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/llmgateway-io-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/vocabulary/llmgateway-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/llmgateway-io-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/data-model/llmgateway-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/llmgateway-io-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.llmgateway.io/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/errors/llmgateway-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/llmgateway-io-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/conformance/llmgateway-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/llmgateway-io-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/llms/llmgateway-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/llmgateway-io-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/well-known/llmgateway-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/llmgateway-io-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/hosts/llmgateway-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/llmgateway-io-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://llmgateway.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://llmgateway.io/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://llmgateway.io/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/theopenco
- group: company
  title: ''
  type: Blog
  url: https://llmgateway.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://llmgateway.io/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.llmgateway.io/quick-start
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.llmgateway.io
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/authentication/llmgateway-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/llmgateway-io-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/security/llmgateway-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/llmgateway-io-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/llmgateway-io/refs/heads/main/security/llmgateway-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llmgateway-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://llmgateway.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.llmgateway.io
- group: operate
  title: ''
  type: ChangeLog
  url: https://llmgateway.io/changelog
- group: design
  title: ''
  type: Versioning
  url: https://docs.llmgateway.io/resources/api-versioning
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.llmgateway.io/llms.txt
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/theopenco/llmgateway
created: '2026-10-12'
description: 'LLM Gateway is an OpenAI-compatible LLM gateway: one API key routes chat completions, embeddings, images, audio, video, moderation, OCR, rerank, web search and typed decisions across model providers. It publishes an OpenAPI 3.0 contract at https://api.llmgateway.io/openapi.json, which includes POST /v1/decisions (OpenAI-compatible typed, probabilistic decisions) and POST /v1/systemone (the TypeSafe System One-compatible endpoint, documented as legacy and to be deprecated in favor of /v1/decisions). An MCP server (Streamable HTTP) is served at /mcp with OAuth metadata at /.well-known/oauth-authorization-server and /.well-known/oauth-protected-resource.'
image: https://llmgateway.io/opengraph-image?6e44604ced30de3d
jsonld:
- class_count: 2
  name: Llmgateway Io Context
  property_count: 2
  slug: llmgateway-io-context
layout: provider
mcp_servers:
- description: ''
  name: LLM Gateway MCP Server
  slug: mcp
modified: '2026-10-12'
name: LLM Gateway
nav: Providers
network: true
overview: 'LLM Gateway publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Decisions API, Embeddings API, and 14 more. Tagged areas include Artificial Intelligence, LLM Gateway, Decision Support, Structured Outputs, and Inference.


  The LLM Gateway catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  LLM Gateway''s developer surface includes engineering blog, pricing, getting-started guide, authentication, documentation, changelog, and 23 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: LLM Gateway API Rules
  rule_count: 17
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 6
  slug: llmgateway-io-rules
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    contract_governance: 22.0
    contract_quality: 50.4
    developer_ergonomics: 45.2
    discoverability: 73.2
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Llmgateway Io Authentication
  slug: llmgateway-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Llmgateway Io Domain Security
  slug: llmgateway-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Llmgateway Io Trust Center
  slug: llmgateway-io-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: llmgateway-io
tags:
- Artificial Intelligence
- LLM Gateway
- Decision Support
- Structured Outputs
- Inference
- MCP
website: https://llmgateway.io
---
