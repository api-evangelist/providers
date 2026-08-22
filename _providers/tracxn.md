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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.1
  scored_at: '2026-08-19'
api_count: 2
apis:
- description: 'Programmatic access to Tracxn''s private-market database. Version 3.0 is current and version 2.2 is formally announced for deprecation. A uniform JSON-over-HTTPS contract: every data endpoint is a POST'
  name: Tracxn API
  slug: tracxn-api
- description: 'Tracxn''s official first-party remote Model Context Protocol server, exposing the private-market database to any MCP-compatible AI client — Claude, ChatGPT, Cursor, Gemini CLI, Perplexity, or anything '
  name: Tracxn MCP Server
  slug: tracxn-mcp-server
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tracxn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tracxn.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://w.tracxn.com/api-developers-page
- group: docs
  title: ''
  type: Documentation
  url: https://platform.tracxn.com/a/api/gettingstarted/apibasics
- group: start
  title: ''
  type: GettingStarted
  url: https://platform.tracxn.com/a/api/gettingstarted/apibasics
- group: commercial
  title: ''
  type: Pricing
  url: https://tracxn.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://tracxn.com/signup
- group: start
  title: ''
  type: Login
  url: https://tracxn.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tracxn.com/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tracxn.com/privacypolicy
- group: operate
  title: ''
  type: Support
  url: https://help.tracxn.com/en/
- group: operate
  title: ''
  type: ContactUs
  url: https://tracxn.com/contactus
- group: operate
  title: ''
  type: FAQ
  url: https://w.tracxn.com/faqs
- group: company
  title: ''
  type: Blog
  url: https://tracxn.com/p/media
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tracxn
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/tracxnapi/tracxn-api/overview
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tracxn-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tracxn-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/tracxn-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tracxn-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tracxn-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tracxn-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tracxn-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tracxn-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tracxn-data-model.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tracxn-tool-crosswalk.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tracxn-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tracxn-well-known.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tracxn-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tracxn-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/tracxn-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tracxn-lifecycle.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.postman.com/tracxnapi/tracxn-api/folder/gg9mglv/companies-search-3-0
created: '2026-07-17'
description: 'Tracxn is a market intelligence platform for private company data, tracking 7.7M+ companies worldwide across 2,000+ sectors, 3K+ feeds and 55K+ taxonomies for venture capital funds, private equity, investment banks, corporate M&A and innovation teams. Alongside the platform it sells Data Solutions for programmatic access: the Tracxn API (JSON over HTTPS at platform.tracxn.com/api/2.2 with companies, investors, funding transactions and acquisition endpoints, plus a rate-limited Playground sandbox), an official Tracxn MCP server for AI assistants such as Claude, ChatGPT and Cursor, scheduled SFTP dumps, and Snowflake and BigQuery data-share integrations. Founded in Bengaluru by Neha Singh and Abhishek Goyal and backed by Accel, Tracxn is listed on the Indian stock exchanges (NSE: TRACXN).'
image: https://avatars.githubusercontent.com/u/12694738?v=4
layout: provider
mcp_servers:
- description: ''
  name: tracxn-mcp.yml
  slug: tracxn-mcpyml
modified: '2026-08-14'
name: Tracxn
nav: Providers
network: true
overview: 'Tracxn publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Saas, Market Intelligence, Private Markets, and Venture Capital.


  Tracxn''s developer surface includes documentation, getting-started guide, pricing, signup flow, support, FAQ, engineering blog, and 27 more developer resources.'
plans:
- name: Tracxn Plans Pricing
  plan_count: 0
  slug: tracxn-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 9
  name: Tracxn Rate Limits
  slug: tracxn-rate-limits
scopes:
- name: Tracxn Scopes
  scope_count: 0
  slug: tracxn-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.1
  delta: -2.4
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 58.9
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 39.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Tracxn Authentication
  slug: tracxn-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Tracxn Domain Security
  slug: tracxn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tracxn
tags:
- Company
- Cloud Saas
- Market Intelligence
- Private Markets
- Venture Capital
- Startups
- Company Data
- Investors
- Funding
website: https://tracxn.com
---
