---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-10-17'
api_count: 12
apis:
- description: POST /chat/completions for Solar models (OpenAI-compatible).
  name: Upstage Chat Completions API
  slug: chat-completions
- description: OpenAI-compatible Responses API with structured outputs, tool calling, reasoning and file_search.
  name: Upstage Responses API
  slug: responses
- description: Solar Embedding vectors for passages and queries.
  name: Upstage Embeddings API
  slug: embeddings
- description: Parse documents into structured HTML or Markdown, sync and async.
  name: Upstage Document Parse API
  slug: document-parse
- description: OCR for scanned documents and images.
  name: Upstage Document OCR API
  slug: document-ocr
- description: Schema-driven structured extraction from documents, with async and schema generation.
  name: Upstage Universal Information Extraction API
  slug: information-extraction
- description: Classify documents into user-defined classes.
  name: Upstage Document Classification API
  slug: document-classification
- description: Check LLM answers against source context.
  name: Upstage Groundedness Check API
  slug: groundedness-check
- description: Korean, English and Japanese translation models.
  name: Upstage Translation API
  slug: translation
- description: Create, manage and search vector stores and file batches for file search.
  name: Upstage Vector Stores API
  slug: vector-stores
- description: 'Run Studio document agents: upload files and create/retrieve jobs.'
  name: Upstage Agents API
  slug: agents
- baseURL: https://api.upstage.ai/v1
  baseurl_source: declared
  description: The System One API from Upstage — 1 operation(s) for system one.
  name: Upstage System One API
  slug: upstage-ai-system-one-api
artifact_total: 21
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/rate-limits/upstage-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/upstage-ai-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/rules/upstage-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/upstage-ai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/json-ld/upstage-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/upstage-ai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/vocabulary/upstage-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/upstage-ai-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/data-model/upstage-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/upstage-ai-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/authentication/upstage-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/upstage-ai-authentication.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://console.upstage.ai/docs/models/history
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/lifecycle/upstage-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/upstage-ai-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/errors/upstage-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/upstage-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/conformance/upstage-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/upstage-ai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/llms/upstage-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/upstage-ai-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/well-known/upstage-ai-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/upstage-ai-support-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/well-known/upstage-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/upstage-ai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/hosts/upstage-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/upstage-ai-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/vendors/upstage-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/upstage-ai-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/packages/upstage-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/upstage-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/packages/upstage-ai-packages.yml
  title: ''
  type: Packages
  url: packages/upstage-ai-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://support.upstage.ai
- group: operate
  title: ''
  type: StatusPage
  url: https://status.upstage.ai/
- group: start
  title: ''
  type: Sandbox
  url: https://console.upstage.ai/playground/chat
- group: company
  title: ''
  type: Newsroom
  url: https://www.upstage.ai/news
- group: other
  title: ''
  type: Leadership
  url: https://www.upstage.ai/team/pr
- group: company
  title: ''
  type: Blog
  url: https://www.upstage.ai/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/security/upstage-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/upstage-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://upstage.ai
- group: docs
  title: ''
  type: Documentation
  url: https://console.upstage.ai/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://console.upstage.ai/api/chat
- group: agent
  title: ''
  type: LLMsTxt
  url: https://console.upstage.ai/llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: https://console.upstage.ai/docs/guides/rate-limits
- group: design
  title: ''
  type: ErrorCodes
  url: https://console.upstage.ai/docs/resources/error-codes
- group: operate
  title: ''
  type: ChangeLog
  url: https://console.upstage.ai/docs/resources/changelog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/upstage-ai/refs/heads/main/mcp/upstage-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/upstage-ai-mcp.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://console.upstage.ai/docs/guides/mcp-server
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/UpstageAI
- group: commercial
  title: ''
  type: TermsOfService
  url: https://console.upstage.ai/docs/terms/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://console.upstage.ai/docs/terms/privacy-policy
- group: operate
  title: ''
  type: SLA
  url: https://console.upstage.ai/docs/terms/sla
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://solar-chat.upstage.ai/mcp
  - status: 200
    url: https://upstage.ai
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Upstage is a Korean AI company offering the Solar LLM family and document AI (Document Parse, OCR, Information Extract, Classify) through Upstage Console at https://api.upstage.ai/v1. Its Solar Decide model (beta, built on Solar Mini 4) is exposed at POST /v1/systemone, a System One-style endpoint taking a state plus typed questions (choice, score, noul) and returning calibrated decisions; output tokens are not billed. API references are published as markdown under console.upstage.ai/api/ with an llms.txt index; the reference pages cite OpenAPI files (e.g. ./openapi/openapi-systemone.yaml) that are not publicly retrievable, so no provider-published OpenAPI was saved.
image: https://cdn.prod.website-files.com/6743d5190bb2b52f38e99e37/680a25ee07a17eed6deeff74_OG.avif
json_schemas:
- name: SystemOneRequest
  property_count: 3
  slug: upstage-ai-system-one-request
- name: SystemOneResponse
  property_count: 3
  slug: upstage-ai-system-one-response
jsonld:
- class_count: 5
  name: Upstage Ai Context
  property_count: 15
  slug: upstage-ai-context
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 2 tools listed.
  name: MCP server manifest
  slug: mcp-upstage
- description: ''
  name: MCP server guide
  slug: mcp-server-guide
modified: '2026-10-12'
name: Upstage
nav: Providers
network: true
overview: 'Upstage is listed with 12 APIs on the [APIs.io](https://apis.io/) network, including System One API, and 11 more. Tagged areas include Artificial Intelligence, LLM, Document AI, OCR, and Decision Support.


  The Upstage catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Upstage''s developer surface includes authentication, support, sandbox, engineering blog, documentation, API reference, changelog, and 30 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 150
  name: Upstage Ai Rate Limits
  slug: upstage-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Upstage API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: upstage-ai-rules
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 27.7
    developer_ergonomics: 50.0
    discoverability: 80.0
    operational_transparency: 76.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Upstage Ai Authentication
  slug: upstage-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Upstage Ai Domain Security
  slug: upstage-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: upstage-ai
tags:
- Artificial Intelligence
- LLM
- Document AI
- OCR
- Decision Support
- Structured Outputs
- Embeddings
website: https://upstage.ai
---
