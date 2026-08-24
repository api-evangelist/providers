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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Mutiny's hosted Model Context Protocol server and its only public programmatic entry point. It exposes the workspace's asset creation, template, content library and publishing capabilities to any MCP-
  name: Mutiny MCP Server
  slug: mutiny-mcp-server
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.mutinyhq.com/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.mutinyhq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.mutinyhq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mutinyhq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mutinyhq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.mutinyhq.com/register
- group: start
  title: ''
  type: Login
  url: https://app.mutinyhq.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mutinyhq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mutinyhq.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MutinyHQ
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mutiny-hq-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mutiny-hq-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mutiny-hq-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mutiny-hq-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mutiny-hq-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://help.mutinyhq.com/articles/4986991401-mutiny-compliance-overview
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mutiny-hq-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mutiny-hq-llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://help.mutinyhq.com/articles/7238243181-mutiny-mcp-tools-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://help.mutinyhq.com/articles/8733886310-getting-started-with-mutiny-in-your-ai-assistant
- group: build
  title: ''
  type: Packages
  url: packages/mutiny-hq-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mutiny-hq-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mutiny-hq-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mutiny-hq-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mutiny-hq-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mutiny-hq-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mutiny-hq-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mutiny-hq-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mutiny-hq-rate-limits.yml
created: '2026-07-17'
description: Mutiny is a GTM (go-to-market) assistant built for customer-facing work — a vertical AI platform for B2B revenue teams (used by Snowflake, Uber, Rippling, GitLab, and Figma). It generates on-brand customer-facing assets such as deal rooms, pitch decks, business cases, ABM campaigns, comparison pages, and meeting recaps, and automates repetitive sales and marketing workflows through an agent, skill, and routine framework. Mutiny integrates with common CRM and GTM systems (Salesforce, HubSpot, Marketo, 6sense, Segment) and exposes a hosted Model Context Protocol (MCP) server so agents like Claude and ChatGPT can create, browse, and publish assets in conversation. Mutiny is backed by Insight Partners. It does not publish a general-purpose REST API; its programmatic entry point is the OAuth-protected MCP server.
image: https://framerusercontent.com/assets/Ec1hAhKLtluxlMfLydNP0NTrIA.png
layout: provider
mcp_servers:
- description: ''
  name: Mutiny HQ MCP Server
  slug: mutiny-hq-mcp-server
- description: ''
  name: Mutiny HQ MCP Server
  slug: mutiny-hq-mcp-server-2
modified: '2026-08-13'
name: Mutiny HQ
nav: Providers
network: true
overview: 'Mutiny HQ publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Go-To-Market, Sales Enablement, Marketing, and Website Personalization.


  Mutiny HQ''s developer surface includes documentation, engineering blog, pricing, signup flow, authentication, API reference, getting-started guide, and 22 more developer resources.'
plans:
- name: Mutiny Hq Plans Pricing
  plan_count: 3
  slug: mutiny-hq-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Mutiny Hq Rate Limits
  slug: mutiny-hq-rate-limits
scopes:
- name: Mutiny Hq Scopes
  scope_count: 5
  slug: mutiny-hq-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.8
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 37.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mutiny-hq/refs/heads/main/screenshots/mutiny-hq-2026-08-07T184453.png
security:
- kind: authentication
  name: Mutiny Hq Authentication
  slug: mutiny-hq-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Mutiny Hq Domain Security
  slug: mutiny-hq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mutiny-hq
tags:
- Company
- Go-To-Market
- Sales Enablement
- Marketing
- Website Personalization
- Artificial Intelligence
- Agents
- MCP
- Account Based Marketing
- Content Generation
website: https://www.mutinyhq.com/
---
