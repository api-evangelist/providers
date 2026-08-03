---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 23
  human_in_the_loop: 1
  name: Vectara Agentic Access
  operation_count: 34
  slug: vectara-agentic-access
  summary_line: 34 operations · 23 acting · 1 human-in-the-loop
api_count: 9
apis:
- description: Multi-turn conversational interface over a Vectara corpus that maintains chat history and produces grounded, cited answers with optional streaming.
  name: Vectara Chat API
  slug: vectara-chat-api
- description: OAuth 2.0 client credentials flow used to obtain a short-lived JWT for calling the Vectara REST API.
  name: Vectara OAuth 2.0 Token API
  slug: vectara-oauth2-api
- description: Build and operate agents over Vectara corpora.
  name: Vectara Agents API
  slug: vectara-agents-api
- description: OAuth 2.0 client credentials flow for obtaining JWT tokens.
  name: Vectara Authentication API
  slug: vectara-authentication-api
- description: Create, list, update, and delete corpora that hold indexed documents.
  name: Vectara Corpora API
  slug: vectara-corpora-api
- description: Upload, index, retrieve, update, and delete documents in a corpus.
  name: Vectara Documents API
  slug: vectara-documents-api
- description: Manage pipelines and inspect pipeline runs.
  name: Vectara Pipelines API
  slug: vectara-pipelines-api
- description: Semantic, keyword, and hybrid queries with optional grounded generation.
  name: Vectara Query API
  slug: vectara-query-api
- description: Manage tools and tool servers used by agents.
  name: Vectara Tools API
  slug: vectara-tools-api
artifact_total: 37
collections:
- collection_type: postman
  name: Vectara REST Agents API
  slug: postman-vectara-agents-api
- collection_type: postman
  name: Vectara REST Agents Authentication API
  slug: postman-vectara-authentication-api
- collection_type: postman
  name: Vectara REST Agents Corpora API
  slug: postman-vectara-corpora-api
- collection_type: postman
  name: Vectara REST Agents Documents API
  slug: postman-vectara-documents-api
- collection_type: postman
  name: Vectara REST Agents Pipelines API
  slug: postman-vectara-pipelines-api
- collection_type: postman
  name: Vectara REST Agents Query API
  slug: postman-vectara-query-api
- collection_type: postman
  name: Vectara REST Agents Tools API
  slug: postman-vectara-tools-api
- collection_type: open
  name: Vectara REST API
  slug: open-vectara
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vectara/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vectara-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vectara-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vectara-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vectara-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vectara-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.vectara.com/
- group: other
  title: ''
  type: Developer
  url: https://docs.vectara.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.vectara.com/docs/rest-api/
- group: docs
  title: ''
  type: OpenAPI
  url: https://docs.vectara.com/vectara-oas-v2.yaml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vectara/python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vectara/typescript-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vectara/py-vectara-agentic
- group: build
  title: ''
  type: SDKs
  url: https://github.com/vectara/langchain-vectara
- group: build
  title: ''
  type: Tools
  url: https://github.com/vectara/vectara-mcp
- group: build
  title: ''
  type: Tools
  url: https://github.com/vectara/vectara-ingest
- group: build
  title: ''
  type: Tools
  url: https://github.com/vectara/vectara-ui
- group: build
  title: ''
  type: Tools
  url: https://github.com/vectara/react-search
- group: build
  title: ''
  type: Tools
  url: https://github.com/vectara/react-chatbot
- group: build
  title: ''
  type: Tools
  url: https://github.com/vectara/stream-query-client
- group: build
  title: ''
  type: Tools
  url: https://github.com/vectara/create-ui
- group: build
  title: ''
  type: Tools
  url: https://github.com/vectara/vectara-answer
- group: build
  title: ''
  type: Tools
  url: https://github.com/vectara/open-rag-eval
- group: build
  title: ''
  type: Tools
  url: https://github.com/vectara/hallucination-leaderboard
- group: build
  title: ''
  type: Tools
  url: https://github.com/vectara/agent-skills
- group: build
  title: ''
  type: Samples
  url: https://github.com/vectara/getting-started
- group: build
  title: ''
  type: Samples
  url: https://github.com/vectara/example-notebooks
- group: build
  title: ''
  type: Samples
  url: https://github.com/vectara/design-patterns
- group: build
  title: ''
  type: GitHub
  url: https://github.com/vectara
- group: company
  title: ''
  type: Blog
  url: https://www.vectara.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vectara.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vectara.com/
- group: operate
  title: ''
  type: Support
  url: https://docs.vectara.com/docs/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vectara.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vectara.com/legal/terms-of-service/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vectara/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.vectara.com/docs/release-notes
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.vectara.com/llms.txt
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vectara-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/vectara-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vectara-finops.yml
- group: design
  title: ''
  type: Rules
  url: rules/vectara-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vectara-vocabulary.yml
created: '2026-05-23'
description: Vectara is a Retrieval Augmented Generation (RAG) as a service platform that provides grounded generative AI for enterprises. The API-first platform exposes a unified REST API v2 for managing corpora, ingesting documents, performing semantic and hybrid search, generating answers with hallucination detection via the Hughes Hallucination Evaluation Model (HHEM), and building agents and pipelines on top of enterprise data. Headquartered in Mountain View, California and founded by former Google Search engineers, Vectara ships first-party Python and TypeScript SDKs, a public MCP server, React UI widgets, and an open ingestion framework.
examples:
- key_count: 2
  name: Vectara Add Document Example
  slug: vectara-add-document-example
- key_count: 2
  name: Vectara Create Corpus Example
  slug: vectara-create-corpus-example
- key_count: 2
  name: Vectara Oauth Token Example
  slug: vectara-oauth-token-example
- key_count: 2
  name: Vectara Query Corpus Example
  slug: vectara-query-corpus-example
finops:
- name: Vectara Finops
  service_category: API
  slug: vectara-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vectara.png
json_schemas:
- name: Vectara Agent
  property_count: 8
  slug: vectara-agent
- name: Vectara Corpus
  property_count: 10
  slug: vectara-corpus
- name: Vectara Document
  property_count: 4
  slug: vectara-document
- name: Vectara Query Request
  property_count: 4
  slug: vectara-query
json_structures:
- name: Vectara Corpus Structure
  property_count: 0
  slug: vectara-corpus-structure
jsonld:
- class_count: 22
  name: Vectara Context
  property_count: 4
  slug: vectara-context
layout: provider
modified: '2026-05-25'
name: Vectara
nav: Providers
network: true
overview: 'Vectara publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Agents API, Authentication API, Corpora API, and 4 more. Tagged areas include AI, Agents, Corpora, Embeddings, and Enterprise Search.


  The Vectara catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vectara''s developer surface includes authentication, documentation, tooling, GitHub presence, engineering blog, pricing, support, and 36 more developer resources.'
plans:
- name: Vectara Plans Pricing
  plan_count: 1
  slug: vectara-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 2
  name: Vectara Rate Limits
  slug: vectara-rate-limits
rules:
- name: Vectara API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vectara-jsonschema-spectral-rules
- name: Vectara API Rules
  rule_count: 4
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 2
  slug: vectara-rules
scopes:
- name: Vectara Scopes
  scope_count: 0
  slug: vectara-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.2
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 68.7
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 57.9
  previous_composite: 63.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vectara/refs/heads/main/screenshots/vectara-2026-06-20T200838.png
security:
- kind: authentication
  name: Vectara Authentication
  slug: vectara-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Vectara Domain Security
  slug: vectara-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Vectara Trust Center
  slug: vectara-trust-center
  summary_line: SOC 2, ISO 27001
slug: vectara
tags:
- AI
- Agents
- Corpora
- Embeddings
- Enterprise Search
- Generative AI
- Grounded Generation
- Hallucination Detection
- LLM
- MCP
- RAG
- Retrieval
- Search
- Semantic Search
- Vector Search
website: https://www.vectara.com/
---
