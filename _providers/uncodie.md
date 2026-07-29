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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Core Makinari platform API covering Visitors (tracking and identification), Finder (contact and company search), Robots (browser-automation instances), Instances, Requirements, and Secure Tokens. API-
  name: Makinari REST API
  slug: makinari-rest-api
- description: Public content delivery API for Makinari sites — fetch published blog posts, RSS feeds, and other content types for headless frontends, directories, and syndication. Browser requests from the register
  name: Makinari Content API
  slug: makinari-content-api
artifact_total: 6
asyncapis:
- description: ''
  name: Uncodie Webhooks
  slug: uncodie-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uncodie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.makinari.com
- group: company
  title: ''
  type: Website
  url: https://www.uncodie.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.makinari.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.makinari.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.makinari.com/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.makinari.com/first-steps
- group: operate
  title: ''
  type: Support
  url: https://www.makinari.com/product/support
- group: company
  title: ''
  type: Blog
  url: https://www.makinari.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.makinari.com/product/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.makinari.com/auth?mode=register
- group: start
  title: ''
  type: Login
  url: https://app.makinari.com/auth
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.makinari.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.makinari.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/makinary
- group: operate
  title: ''
  type: StatusPage
  url: https://docs.makinari.com/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.makinari.com/product/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uncodie-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uncodie-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uncodie-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/uncodie-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uncodie-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uncodie-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uncodie-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/uncodie-webhooks.yml
- group: build
  title: ''
  type: CLI
  url: cli/uncodie-cli.yml
- group: design
  title: ''
  type: Components
  url: components/uncodie-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uncodie-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uncodie-conformance.yml
created: '2026-07-17'
description: Uncodie, a 500 Global portfolio company, rebranded as Makinari — an AI-agent business platform that builds the application a business needs and then runs growth on top of it with a team of AI agents (CMO, sales, growth, copywriter, customer support, data analyst, email, WhatsApp, UX) plus a CRM. Developers get a versioned REST API (Visitors, Finder, Robots, Instances, Requirements, Secure Tokens), a Content API for headless delivery, Temporal-backed workflow automation, webhooks, an embeddable chat widget, and an official hosted MCP server exposing 40+ tools. www.uncodie.com now redirects to www.makinari.com.
image: https://www.makinari.com/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: uncodie-mcp.yml
  slug: uncodie-mcpyml
modified: '2026-07-21'
name: Uncodie (now Makinari)
nav: Providers
network: true
overview: 'Uncodie (now Makinari) publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, CRM, and Sales Automation.


  The Uncodie (now Makinari) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Uncodie (now Makinari)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
random_paper: 14
score:
  band: developing
  composite: 51.3
  delta: 8.2
  facets:
    commercial_clarity: 44.7
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 44.7
  previous_composite: 43.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: authentication
  name: Uncodie Authentication
  slug: uncodie-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Uncodie Domain Security
  slug: uncodie-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: uncodie
tags:
- Company
- Artificial Intelligence
- AI Agents
- CRM
- Sales Automation
- Marketing Automation
- Lead Generation
- No Code
- MCP
website: https://www.makinari.com
---
