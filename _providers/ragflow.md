---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The RAGFlow RESTful HTTP API — 95 documented operations under /api/v1, authenticated with a tenant API key carried as a bearer token. Covers dataset management, document upload / parse / ingest, chunk
  name: RAGFlow HTTP API
  slug: ragflow-http-api
artifact_total: 10
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/infiniflow/ragflow/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://ragflow.io/
- group: docs
  title: ''
  type: Documentation
  url: https://ragflow.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://ragflow.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ragflow.io/docs/http_api_reference
- group: company
  title: ''
  type: Blog
  url: https://ragflow.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infiniflow
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/infiniflow/ragflow
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/infiniflow/ragflow/issues/12241
- group: operate
  title: ''
  type: Support
  url: https://ragflow.io/contact-us
- group: operate
  title: ''
  type: Community
  url: https://discord.gg/NjYzJD3GM3
- group: commercial
  title: ''
  type: Pricing
  url: https://ragflow.io/#pricing-plan
- group: start
  title: ''
  type: SignUp
  url: https://cloud.ragflow.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ragflow.io/policies/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ragflow.io/policies/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://ragflow.io/policies/dpa
- group: auth
  href: https://artifacts.apis.io/ragflow/security/ragflow-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/ragflow-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ragflow/security/ragflow-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/ragflow-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/ragflow/security/ragflow-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ragflow-domain-security.yml
- group: build
  href: https://artifacts.apis.io/ragflow/packages/ragflow-packages.yml
  title: ''
  type: Packages
  url: packages/ragflow-packages.yml
- group: build
  href: https://artifacts.apis.io/ragflow/packages/ragflow-packages.yml
  title: ''
  type: SDKs
  url: packages/ragflow-packages.yml
- group: agent
  href: https://artifacts.apis.io/ragflow/mcp/ragflow-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ragflow-mcp.yml
- group: build
  href: https://artifacts.apis.io/ragflow/mcp/ragflow-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ragflow-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ragflow/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/ragflow/llms/ragflow-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ragflow-llms.txt
- group: design
  href: https://artifacts.apis.io/ragflow/conventions/ragflow-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ragflow-conventions.yml
- group: design
  href: https://artifacts.apis.io/ragflow/errors/ragflow-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/ragflow-error-codes.yml
- group: auth
  href: https://artifacts.apis.io/ragflow/authentication/ragflow-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ragflow-authentication.yml
- group: design
  href: https://artifacts.apis.io/ragflow/conformance/ragflow-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ragflow-conformance.yml
- group: design
  href: https://artifacts.apis.io/ragflow/data-model/ragflow-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ragflow-data-model.yml
- group: design
  href: https://artifacts.apis.io/ragflow/lifecycle/ragflow-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ragflow-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/ragflow/lifecycle/ragflow-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/ragflow-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/ragflow/changelog/ragflow-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ragflow-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://ragflow.io/docs/release_notes
- group: commercial
  href: https://artifacts.apis.io/ragflow/plans/ragflow-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ragflow-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/ragflow/rate-limits/ragflow-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ragflow-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/ragflow/sandbox/ragflow-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/ragflow-sandbox.yml
- group: design
  href: https://artifacts.apis.io/ragflow/components/ragflow-components.yml
  title: ''
  type: Components
  url: components/ragflow-components.yml
created: '2026-08-27'
description: RAGFlow is the open-source Retrieval-Augmented Generation engine built by InfiniFlow Inc. It combines deep document understanding (DeepDoc parsing of PDFs, images, tables and scanned files) with hybrid retrieval — dense vector search, BM25 full-text and tensor/multi-vector re-ranking — and an integrated visual agent platform, to serve as a context layer for LLM applications. The platform ships as an Apache-2.0 self-hosted Docker deployment and as RAGFlow Cloud, a hosted multi-tenant service. Its RESTful HTTP API covers dataset (knowledge base) management, document ingestion and parsing, chunk management, retrieval, chat assistants, sessions, agents, memory, workspace file versioning and search apps, plus an OpenAI-compatible chat-completions surface. A first-party Python SDK and an optional self-hosted Model Context Protocol server expose the same retrieval core to agents.
finops:
- has_sources: true
  method: derived
  name: Ragflow Finops
  primary_unit: subscription
  service_category: ''
  slug: ragflow-finops
  template: false
image: https://ragflow.io/img/logo.svg
layout: provider
mcp_servers:
- description: 'A first-party Model Context Protocol server that InfiniFlow ships inside the RAGFlow repository at mcp/server/server.py. It is an OPTIONAL, DISABLED-BY-DEFAULT component of a RAGFlow deployment: the o'
  name: RAGFlow MCP Server
  slug: ragflow-mcp-server
modified: '2026-08-27'
name: RAGFlow
nav: Providers
network: true
overview: 'RAGFlow is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, RAG, Search, and Vector Search.


  RAGFlow''s developer surface includes documentation, getting-started guide, API reference, engineering blog, support, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Ragflow Plans Pricing
  plan_count: 6
  slug: ragflow-plans-pricing
- name: Ragflow Price Estimates
  plan_count: 0
  slug: ragflow-price-estimates
random_paper: 10
rate_limits:
- limit_count: 3
  name: Ragflow Rate Limits
  slug: ragflow-rate-limits
score:
  band: developing
  composite: 49.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 65.0
    operational_transparency: 73.7
  previous_composite: 49.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ragflow/ragflow-2026-09-02T152804.png
security:
- kind: authentication
  name: Ragflow Authentication
  slug: ragflow-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Ragflow Domain Security
  slug: ragflow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Ragflow Vulnerability Disclosure
  slug: ragflow-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 1
skills:
- name: ragflow-dataset-ingest
  slug: ragflow-dataset-ingest
slug: ragflow
tags:
- Company
- Artificial Intelligence
- RAG
- Search
- Vector Search
- Document Processing
- Knowledge Management
- Agents
- Open Source
- LLM
- MCP
website: https://ragflow.io/
---
