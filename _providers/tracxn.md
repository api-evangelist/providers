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
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Programmatic access to Tracxn's private-market database (API version 2.2). JSON-over-HTTPS POST endpoints for companies, investors, funding transactions and acquisition transactions, filtered by feed/
  name: Tracxn API
  slug: tracxn-api
artifact_total: 4
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
created: '2026-07-17'
description: 'Tracxn is a market intelligence platform for private company data, tracking 7.7M+ companies worldwide across 2,000+ sectors, 3K+ feeds and 55K+ taxonomies for venture capital funds, private equity, investment banks, corporate M&A and innovation teams. Alongside the platform it sells Data Solutions for programmatic access: the Tracxn API (JSON over HTTPS at platform.tracxn.com/api/2.2 with companies, investors, funding transactions and acquisition endpoints, plus a rate-limited Playground sandbox), an official Tracxn MCP server for AI assistants such as Claude, ChatGPT and Cursor, scheduled SFTP dumps, and Snowflake and BigQuery data-share integrations. Founded in Bengaluru by Neha Singh and Abhishek Goyal and backed by Accel, Tracxn is listed on the Indian stock exchanges (NSE: TRACXN).'
image: https://avatars.githubusercontent.com/u/12694738?v=4
layout: provider
mcp_servers:
- description: ''
  name: tracxn-mcp.yml
  slug: tracxn-mcpyml
modified: '2026-07-21'
name: Tracxn
nav: Providers
network: true
overview: 'Tracxn publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cloud Saas, Market Intelligence, Private Markets, and Venture Capital.


  Tracxn''s developer surface includes documentation, getting-started guide, pricing, signup flow, support, FAQ, engineering blog, and 18 more developer resources.'
random_paper: 76
score:
  band: thin
  composite: 30.6
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 5.3
  previous_composite: 30.6
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Tracxn Authentication
  slug: tracxn-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tracxn Domain Security
  slug: tracxn-domain-security
  summary_line: TLSv1.3 · HSTS
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
