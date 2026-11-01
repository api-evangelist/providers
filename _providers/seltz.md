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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://api.seltz.ai
  baseurl_source: declared
  description: Answer operations
  name: Seltz Answer API
  slug: seltz-answer-api
- baseURL: https://api.seltz.ai
  baseurl_source: declared
  description: Search operations
  name: Seltz Search API
  slug: seltz-search-api
artifact_total: 13
collections:
- collection_type: open
  name: Seltz answer API
  slug: open-seltz-answer-api
- collection_type: open
  name: Seltz answer search API
  slug: open-seltz-search-api
common:
- group: commercial
  href: https://artifacts.apis.io/seltz/plans/seltz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/seltz-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.seltz.ai/
- group: other
  href: https://artifacts.apis.io/seltz/overlays/seltz-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/seltz-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/seltz/security/seltz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seltz-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.seltz.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.seltz.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.seltz.ai/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.seltz.ai/quickstart
- group: start
  title: ''
  type: Sandbox
  url: https://console.seltz.ai/playground
- group: commercial
  title: ''
  type: Pricing
  url: https://seltz.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.seltz.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://seltz.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://seltz.ai/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://seltz.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://seltz.ai/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seltz-ai
- group: build
  href: https://artifacts.apis.io/seltz/packages/seltz-packages.yml
  title: ''
  type: Packages
  url: packages/seltz-packages.yml
- group: build
  href: https://artifacts.apis.io/seltz/packages/seltz-packages.yml
  title: ''
  type: SDKs
  url: packages/seltz-packages.yml
- group: agent
  href: https://artifacts.apis.io/seltz/mcp/seltz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/seltz-mcp.yml
- group: agent
  href: https://artifacts.apis.io/seltz/llms/seltz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seltz-llms.txt
- group: agent
  href: https://artifacts.apis.io/seltz/well-known/seltz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/seltz-well-known.yml
- group: design
  href: https://artifacts.apis.io/seltz/conformance/seltz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/seltz-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.seltz.ai/
- group: auth
  href: https://artifacts.apis.io/seltz/security/seltz-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/seltz-trust-center.yml
- group: design
  href: https://artifacts.apis.io/seltz/lifecycle/seltz-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/seltz-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/seltz/changelog/seltz-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/seltz-changelog.yml
- group: agent
  href: https://artifacts.apis.io/seltz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Seltz is a San Francisco-based AI infrastructure company building the web retrieval and knowledge layer for the agentic internet. Its Web Knowledge API gives LLMs, RAG pipelines, and autonomous agents real-time, context-engineered web data through a single call: POST /v1/search returns ranked, cleaned source documents, POST /v1/answer returns a direct RAG answer with citations, and an OpenAI-compatible /v1/chat/completions endpoint serves web-grounded chat. Rather than returning raw snippets like a traditional search API, Seltz shapes web content to maximize usefulness for machine reasoning. Founded in 2025 by Antonio Mallia (Amazon, Pinecone) and backed by Speedinvest and B Capital, Seltz ships official Python and TypeScript SDKs, a hosted MCP server, and integrations for OpenAI, Anthropic, Mistral, LlamaIndex, Agno, Langroid, Dify, n8n, and Zapier.'
finops:
- has_sources: true
  method: derived
  name: Seltz Finops
  primary_unit: 1,000 requests
  service_category: ''
  slug: seltz-finops
  template: false
image: https://seltz.ai/favicon.ico
layout: provider
mcp_servers:
- description: Official Seltz MCP server. Native integration for Claude Desktop, Cursor, VS Code, Windsurf, and other MCP-compatible AI tools. Remote HTTP/SSE server.
  name: Seltz MCP Server
  slug: seltz
modified: '2026-07-21'
name: Seltz
nav: Providers
network: true
overview: 'Seltz publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Answer API and Search API. Tagged areas include Company, Web Search, AI Infrastructure, Retrieval, and RAG.


  Seltz''s developer surface includes documentation, API reference, getting-started guide, sandbox, pricing, signup flow, engineering blog, and 20 more developer resources.'
plans:
- name: Seltz Plans Pricing
  plan_count: 7
  slug: seltz-plans-pricing
- name: Seltz Price Estimates
  plan_count: 0
  slug: seltz-price-estimates
random_paper: 10
score:
  band: strong
  composite: 57.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 100.0
    contract_governance: 4.5
    contract_quality: 45.9
    developer_ergonomics: 73.2
    discoverability: 65.0
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 56.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/seltz/seltz-2026-08-17T081806.png
security:
- kind: authentication
  name: Seltz Authentication
  slug: seltz-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Seltz Domain Security
  slug: seltz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Seltz Trust Center
  slug: seltz-trust-center
  summary_line: trust center published
skill_count: 2
skills:
- name: Get a cited answer grounded in live web search
  slug: seltz-answer-with-citations
- name: Search the live web for agent context
  slug: seltz-web-search
slug: seltz
tags:
- Company
- Web Search
- AI Infrastructure
- Retrieval
- RAG
- Agents
- LLM
- Knowledge API
- Developer Tools
- MCP
website: https://www.seltz.ai/
---
