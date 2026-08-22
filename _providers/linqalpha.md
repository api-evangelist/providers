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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 51.1
  scored_at: '2026-08-19'
api_count: 10
apis:
- description: Briefing Agent — automated market briefings with scheduling and delivery
  name: LinqAlpha Briefing API
  slug: linqalpha-briefing-api
- description: Customer Connectors — customer-owned MCP connector management
  name: LinqAlpha Connectors API
  slug: linqalpha-connectors-api
- description: Data retrieval and mapping
  name: LinqAlpha Data API
  slug: linqalpha-data-api
- description: Conversation feedback
  name: LinqAlpha Feedback API
  slug: linqalpha-feedback-api
- description: LinqAlpha MCP — Financial data tools for AI assistants via Model Context Protocol
  name: LinqAlpha MCP API
  slug: linqalpha-mcp-api
- description: Research Management System
  name: LinqAlpha RMS API
  slug: linqalpha-rms-api
- description: Search and generate responses
  name: LinqAlpha Search API
  slug: linqalpha-search-api
- description: Source batch and file management
  name: LinqAlpha Source Management API
  slug: linqalpha-source-management-api
- description: Sync status — check organization, document, and container sync progress
  name: LinqAlpha Status API
  slug: linqalpha-status-api
- description: The Vault API from LinqAlpha — 3 operation(s) for vault.
  name: LinqAlpha Vault API
  slug: linqalpha-vault-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LinqAlpha Briefing API
  slug: open-linqalpha-briefing-api
- collection_type: open
  name: LinqAlpha Briefing Connectors API
  slug: open-linqalpha-connectors-api
- collection_type: open
  name: LinqAlpha Briefing Data API
  slug: open-linqalpha-data-api
- collection_type: open
  name: LinqAlpha Briefing Feedback API
  slug: open-linqalpha-feedback-api
- collection_type: open
  name: LinqAlpha Briefing MCP API
  slug: open-linqalpha-mcp-api
- collection_type: open
  name: LinqAlpha Briefing RMS API
  slug: open-linqalpha-rms-api
- collection_type: open
  name: LinqAlpha Briefing Search API
  slug: open-linqalpha-search-api
- collection_type: open
  name: LinqAlpha Briefing Source Management API
  slug: open-linqalpha-source-management-api
- collection_type: open
  name: LinqAlpha Briefing Status API
  slug: open-linqalpha-status-api
- collection_type: open
  name: LinqAlpha Briefing Vault API
  slug: open-linqalpha-vault-api
common:
- group: company
  title: ''
  type: Website
  url: https://linqalpha.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://linqalpha.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.linqalpha.com/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://docs.linqalpha.com/api-reference/basic/analytics-sse
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.linqalpha.com/quickstart
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/linqalpha-openapi-original.json
- group: company
  title: ''
  type: Blog
  url: https://linqalpha.com/blog
- group: operate
  title: ''
  type: Support
  url: https://linqalpha.com/contact-sales
- group: start
  title: ''
  type: SignUp
  url: https://chat.linqalpha.com/analytics
- group: commercial
  title: ''
  type: TermsOfService
  url: https://linqalpha.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://linqalpha.com/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/linqalpha-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/linqalpha-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/linqalpha-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/linqalpha-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/linqalpha-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/linqalpha-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/linqalpha-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/linqalpha-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.linqalpha.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/linqalpha-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://linqalpha.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/linqalpha-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/linqalpha-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/linqalpha-well-known.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/linqalpha-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/linqalpha-api-overlay.yaml
created: '2026-07-17'
description: LinqAlpha is a domain-specialized multi-agent AI platform for institutional investment research, serving hedge funds, asset managers and investment banks. It runs retrieval-augmented, agentic analysis across SEC filings, earnings-call transcripts, IR materials, news and macroeconomic data covering 57,600+ companies in 120+ countries and 30+ languages, returning answers with inline citations that resolve to the exact source chunks. The LinqAlpha API exposes that engine over a REST surface at api.linqalpha.com — streaming analytics and chat over Server-Sent Events, document search, natural-language-to-SQL, scheduled research briefings, an RMS/Vault ingestion path for a firm's own internal documents, and a source-grounding judge that scores how well each claim in an answer is backed by the sources it cited. LinqAlpha also publishes a first-party remote MCP server exposing 22 financial-data tools to AI assistants.
image: https://framerusercontent.com/assets/D0IBswEXPvcSQAQJ7aO65K0eLAA.png
layout: provider
mcp_servers:
- description: ''
  name: linqalpha-mcp.yml
  slug: linqalpha-mcpyml
modified: '2026-07-19'
name: LinqAlpha
nav: Providers
network: true
overview: 'LinqAlpha publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Briefing API, Connectors API, Data API, and 7 more. Tagged areas include Company, Financial Services, Investment Research, Artificial Intelligence, and Agents.


  LinqAlpha''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 21 more developer resources.'
random_paper: 9
rate_limits:
- limit_count: 1
  name: Linqalpha Rate Limits
  slug: linqalpha-rate-limits
scopes:
- name: Linqalpha Scopes
  scope_count: 1
  slug: linqalpha-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 55.6
  delta: 0.3
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 30.3
    contract_quality: 56.3
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 36.8
  previous_composite: 55.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 66.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/linqalpha/refs/heads/main/screenshots/linqalpha-2026-07-25T225300.png
security:
- kind: authentication
  name: Linqalpha Authentication
  slug: linqalpha-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Linqalpha Domain Security
  slug: linqalpha-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Linqalpha Trust Center
  slug: linqalpha-trust-center
  summary_line: SOC 1 Type II, SOC 2 Type II, ISO 27001
slug: linqalpha
tags:
- Company
- Financial Services
- Investment Research
- Artificial Intelligence
- Agents
- Market Data
- Equities
- Economic Data
- SEC Filings
- Retrieval Augmented Generation
- MCP
website: https://linqalpha.com/
---
