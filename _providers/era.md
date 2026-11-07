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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Era''s remote Model Context Protocol server. Connect bank accounts to any MCP-compatible AI agent and manage money through natural conversation: spending analysis, cash-flow forecasting, transaction au'
  name: Era Context MCP Server
  slug: era-context-mcp-server
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/era/mcp/era-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/era-mcp.yml
- group: agent
  href: https://artifacts.apis.io/era/llms/era-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/era-llms.txt
- group: agent
  href: https://artifacts.apis.io/era/well-known/era-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/era-well-known.yml
- group: other
  href: https://artifacts.apis.io/era/well-known/era-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/era-api-catalog.json
- group: auth
  href: https://artifacts.apis.io/era/well-known/era-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/era-security.txt
- group: auth
  href: https://artifacts.apis.io/era/authentication/era-authentication.yml
  title: ''
  type: Authentication
  url: authentication/era-authentication.yml
- group: auth
  href: https://artifacts.apis.io/era/scopes/era-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/era-scopes.yml
- group: design
  href: https://artifacts.apis.io/era/conventions/era-conventions.yml
  title: ''
  type: Conventions
  url: conventions/era-conventions.yml
- group: design
  href: https://artifacts.apis.io/era/conformance/era-conformance.yml
  title: ''
  type: Conformance
  url: conformance/era-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/era/plans/era-plans.yml
  title: ''
  type: Plans
  url: plans/era-plans.yml
- group: operate
  href: https://artifacts.apis.io/era/rate-limits/era-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/era-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/era/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://era.app/context/security
- group: auth
  href: https://artifacts.apis.io/era/security/era-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/era-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/era/security/era-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/era-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://era.app/context/finance-mcp
- group: docs
  title: ''
  type: Documentation
  url: https://era.app/help/mcp-server-era-context
- group: docs
  title: ''
  type: APIReference
  url: https://era.app/.well-known/mcp/server-card.json
- group: start
  title: ''
  type: GettingStarted
  url: https://era.app/help/mcp-server-era-context
- group: company
  title: ''
  type: Blog
  url: https://era.app/articles
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/era-app
- group: commercial
  title: ''
  type: Pricing
  url: https://era.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://era.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://era.app/privacy
- group: company
  title: ''
  type: Website
  url: https://era.app
created: '2026-07-17'
description: Era is an AI-native personal finance platform that connects a user's bank accounts to any MCP-compatible AI assistant — Claude, ChatGPT, Gemini, Cursor, and others — so people can analyze spending, forecast cash flow, automate transaction categorization, and manage money through natural conversation. Every capability is exposed through the Era Context remote MCP server (65 tools over Streamable HTTP, OAuth 2.1) rather than a traditional REST API, with a portable cross-agent memory layer, scoped consent, and hard safety boundaries. Founded in 2023 by Stripe alumni and backed by Northzone, Era is a registered investment adviser targeting the mass-affluent market across the US, UK, and Canada.
finops:
- has_sources: true
  method: derived
  name: Era Finops
  primary_unit: subscription
  service_category: ''
  slug: era-finops
  template: false
image: https://era.app/social-card.png
layout: provider
mcp_servers:
- description: AI-native personal finance management. Connect bank accounts, analyze spending, forecast cash flow, automate transactions, and manage your money through natural conversation via MCP.
  name: Era Context
  slug: era-context
modified: '2026-07-19'
name: Era
nav: Providers
network: true
overview: 'Era is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Artificial Intelligence, Personal Finance, and Wealth Management.


  Era''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 19 more developer resources.'
plans:
- name: Era Plans
  plan_count: 4
  slug: era-plans
- name: Era Price Estimates
  plan_count: 0
  slug: era-price-estimates
random_paper: 0
rate_limits:
- limit_count: 4
  name: Era Rate Limits
  slug: era-rate-limits
scopes:
- name: Era Scopes
  scope_count: 10
  slug: era-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 71.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.2
    discoverability: 75.0
    operational_transparency: 44.7
  previous_composite: 42.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 35.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/era/era-2026-07-25T213555.png
security:
- kind: authentication
  name: Era Authentication
  slug: era-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Era Domain Security
  slug: era-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Era Vulnerability Disclosure
  slug: era-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 4
skills:
- name: Automate transaction categorization with rules
  slug: era-automate-categorization
- name: Connect a bank account and analyze spending
  slug: era-connect-and-analyze-spending
- name: Set up portable cross-agent financial memory
  slug: era-cross-agent-memory
- name: Find forgotten recurring subscriptions
  slug: era-find-forgotten-subscriptions
slug: era
tags:
- Company
- Fintech
- Artificial Intelligence
- Personal Finance
- Wealth Management
- MCP
- Agent-Native
- Open Banking
- OAuth
- Authentication
website: https://era.app
---
