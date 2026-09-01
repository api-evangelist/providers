---
access_model:
  confidence: high
  label: Paid plans; API access starts at the Startup tier
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - https://www.makinari.com/product/pricing
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-09-01'
api_count: 5
apis:
- description: Core Makinari platform API covering Visitors (tracking and identification), Finder (contact and company search), Robots (browser-automation instances), Instances, Requirements, and Secure Tokens. API-
  name: Makinari REST API
  slug: makinari-rest-api
- description: Public content delivery API for Makinari sites — fetch published blog posts, RSS feeds, and other content types for headless frontends, directories, and syndication. Browser requests from the register
  name: Makinari Content API
  slug: makinari-content-api
- description: Per-agent HTTP endpoints — 48 documented operations under /api/agents/* covering chat (including a WebSocket channel and human intervention), the CMO agent (daily stand-ups for sales, growth and syste
  name: Makinari Agents API
  slug: makinari-agents-api
- description: Temporal-backed process automation — 25 documented workflows triggered at POST /api/workflow/<name> (agentMessage, analyzeSite, assignLeads, buildCampaigns, buildContent, buildSegments, buildSegmentsI
  name: Makinari Workflows API
  slug: makinari-workflows-api
- description: Official hosted Model Context Protocol server at POST https://backend.makinari.com/api/mcp (JSON-RPC 2.0 over HTTP), exposing 56 documented tools each with a published input schema — CRM (leads, deals
  name: Makinari MCP Server
  slug: makinari-mcp-server
artifact_total: 11
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
  url: https://github.com/Uncodier
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/makinary
- group: build
  title: ''
  type: SourceCode
  url: https://makinari.org
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
- group: design
  title: ''
  type: Conformance
  url: conformance/uncodie-conformance.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/uncodie-tool-crosswalk.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uncodie-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uncodie-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uncodie-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Community
  url: https://chat.whatsapp.com/GWwzWDcCYpdA6aPBBvkp5a
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://www.makinari.com/aup
- group: commercial
  title: ''
  type: DataProcessingAgreement
  url: https://www.makinari.com/dpa
created: '2026-07-17'
description: Uncodie, a 500 Global portfolio company, rebranded as Makinari — an AI-agent business platform that builds the application a business needs and then runs growth on top of it with a team of AI agents (CMO, sales, growth, copywriter, customer support, data analyst, email, WhatsApp, UX) plus a CRM. Developers get a versioned REST API (Visitors, Finder, Robots, Instances, Requirements, Secure Tokens), a per-agent Agents API, a Temporal-backed Workflows API, a public Content API for headless delivery, webhooks, an embeddable chat widget, and an official hosted MCP server exposing 56 documented tools — including a full commerce core (catalog, quotations, checkout, sales orders, entitlements, reservations) that is reachable ONLY over MCP. No OpenAPI is published. The platform source is public at makinari.org (github.com/Uncodier). www.uncodie.com now redirects to www.makinari.com.
image: https://www.makinari.com/images/logo.png
layout: provider
mcp_servers:
- description: ''
  name: Uncodie (now Makinari) MCP Server
  slug: uncodie-now-makinari-mcp-server
modified: '2026-08-13'
name: Uncodie (now Makinari)
nav: Providers
network: true
overview: 'Uncodie (now Makinari) publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, CRM, and Sales Automation.


  The Uncodie (now Makinari) catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Uncodie (now Makinari)''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 31 more developer resources.'
plans:
- name: Uncodie Plans Pricing
  plan_count: 3
  slug: uncodie-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Uncodie Rate Limits
  slug: uncodie-rate-limits
score:
  band: developing
  composite: 54.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 66.1
    discoverability: 74.1
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 54.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uncodie/refs/heads/main/screenshots/uncodie-2026-08-17T082555.png
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
- No-Code
- MCP
- Commerce
- Workflows
- Webhook
- Open-Source
website: https://www.makinari.com
---
