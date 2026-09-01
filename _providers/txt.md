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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Txt Agentic Access
  operation_count: 20
  slug: txt-agentic-access
  summary_line: 20 operations · 10 acting
api_count: 1
apis:
- description: 'Process large volumes of requests asynchronously. Batch processing is ideal when you: - Have many requests that don''t need immediate responses - Want to process data in bulk (e.g., embeddings for a do'
  name: .txt batches API
  slug: txt-batches-api
- description: 'Create model responses for chat conversations. Supports: - **Multi-turn dialogue** with conversation history - **System prompts** to control model behavior - **Tool calling** for function execution an'
  name: .txt chat API
  slug: txt-chat-api
- description: 'Generate vector representations of text. Use embeddings for: - **Semantic search** - find content by meaning, not just keywords - **Clustering** - group similar documents together - **Classification**'
  name: .txt embeddings API
  slug: txt-embeddings-api
- description: 'Upload and manage JSONL files for batch processing. Each line in the file should be a JSON object with: - `custom_id` - your identifier for tracking the request - `method` - HTTP method (POST) - `url`'
  name: .txt files API
  slug: txt-files-api
- description: List and retrieve information about available models. Use these endpoints to discover which models you have access to and their capabilities.
  name: .txt models API
  slug: txt-models-api
- description: 'Create model responses with enhanced capabilities. Open Responses compatible endpoint providing advanced features: - **Reasoning models** - Control computational effort with `reasoning` parameter - **'
  name: .txt responses-api API
  slug: txt-responses-api-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: dottxt batches API
  slug: open-txt-batches-api
- collection_type: open
  name: dottxt batches chat API
  slug: open-txt-chat-api
- collection_type: open
  name: dottxt batches embeddings API
  slug: open-txt-embeddings-api
- collection_type: open
  name: dottxt batches files API
  slug: open-txt-files-api
- collection_type: open
  name: dottxt batches models API
  slug: open-txt-models-api
- collection_type: open
  name: dottxt batches responses-api API
  slug: open-txt-responses-api-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/txt-dottxt-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://dottxt.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dottxt.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.dottxt.ai/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dottxt.ai/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://h1xbpbfsf0w.typeform.com/to/fwQNWmS8
- group: company
  title: ''
  type: Blog
  url: https://blog.dottxt.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dottxt-ai
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/ErZ8XnCmkQ
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dottxt.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/txt-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/txt-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/txt-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/txt-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/txt-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/txt-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/txt-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/txt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/txt-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/txt-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/txt-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/txt-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/txt-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/txt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/txt-domain-security.yml
created: '2026-07-17'
description: '.txt (dottxt) is the structured-generation company behind the open-source Outlines library (65M+ downloads). Its hosted platform, the dottxt API at api.dottxt.ai, is an OpenAI-compatible pay-per-token API whose defining contract is schema enforcement: a JSON Schema passed in response_format is compiled and enforced by constrained decoding, so model outputs are guaranteed valid — including field-by-field RFC 6902 JSON Patch streaming, Open Responses support, embeddings, and JSONL batch processing. Founded by the Outlines maintainers and backed by Seedcamp; inference is operated with launch partner Doubleword.'
image: https://cdn.sanity.io/images/z84vkf2c/production/f496d7868262fbf26f71782579181541f75b45b5-100x50.svg
layout: provider
mcp_servers:
- description: '.txt (dottxt) publishes a hosted, unauthenticated MCP server for its documentation via Mintlify: the manifest at docs.dottxt.ai/.well-known/mcp.json (saved verbatim in well-known/txt-docs-mcp.json) de'
  name: .txt MCP Server
  slug: txt-mcp-server
modified: '2026-07-21'
name: .txt
nav: Providers
network: true
overview: '.txt publishes 6 APIs on the [APIs.io](https://apis.io/) network, including batches API, chat API, embeddings API, and 3 more. Tagged areas include Company, Artificial Intelligence, LLM, Structured Outputs, and JSON-Schema.


  .txt''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, support, CLI, and 19 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 39.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 55.5
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/txt/refs/heads/main/screenshots/txt-2026-08-17T082608.png
security:
- kind: authentication
  name: Txt Authentication
  slug: txt-authentication
  summary_line: http-bearer · 1 scheme
- kind: domain-security
  name: Txt Domain Security
  slug: txt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: txt
tags:
- Company
- Artificial Intelligence
- LLM
- Structured Outputs
- JSON-Schema
- Inference
- Developer Tools
- Machine-Learning
website: https://dottxt.ai
---
