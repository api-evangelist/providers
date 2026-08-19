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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 65.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Contextdev Agentic Access
  operation_count: 84
  slug: contextdev-agentic-access
  summary_line: 84 operations · 32 acting
api_count: 8
apis:
- description: The Brand Intelligence API from Context.dev — 7 operation(s) for brand intelligence.
  name: Context.dev Brand Intelligence API
  slug: contextdev-brand-intelligence-api
- description: Monitor pages, sitemaps, and extracted website data for exact or semantic changes. Webhook payloads are documented by the MonitorsChangeDetectedWebhookPayload and MonitorsRunCompletedWebhookPayload sc
  name: Context.dev Monitors API
  slug: contextdev-monitors-api
- description: The Parsing API from Context.dev — 1 operation(s) for parsing.
  name: Context.dev Parsing API
  slug: contextdev-parsing-api
- description: The People API from Context.dev — 1 operation(s) for people.
  name: Context.dev People API
  slug: contextdev-people-api
- description: The Utility API from Context.dev — 3 operation(s) for utility.
  name: Context.dev Utility API
  slug: contextdev-utility-api
- description: The Web Extraction API from Context.dev — 9 operation(s) for web extraction.
  name: Context.dev Web Extraction API
  slug: contextdev-web-extraction-api
- description: The Web Scraping API from Context.dev — 7 operation(s) for web scraping.
  name: Context.dev Web Scraping API
  slug: contextdev-web-scraping-api
- description: Submit up to 25,000 URLs or a whole-site crawl as a single asynchronous job and collect the results as paginated JSON or gzipped NDJSON. One batch submission counts as a single request against the per
  name: Context.dev Batch API
  slug: contextdev-batch-api
artifact_total: 25
asyncapis:
- description: ''
  name: Contextdev Webhooks
  slug: contextdev-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Context Brand Intelligence API
  slug: open-contextdev-brand-intelligence-api
- collection_type: open
  name: Context Brand Intelligence Monitors API
  slug: open-contextdev-monitors-api
- collection_type: open
  name: Context Brand Intelligence Parsing API
  slug: open-contextdev-parsing-api
- collection_type: open
  name: Context Brand Intelligence People API
  slug: open-contextdev-people-api
- collection_type: open
  name: Context Brand Intelligence Utility API
  slug: open-contextdev-utility-api
- collection_type: open
  name: Context Brand Intelligence Web Extraction API
  slug: open-contextdev-web-extraction-api
- collection_type: open
  name: Context Brand Intelligence Web Scraping API
  slug: open-contextdev-web-scraping-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/contextdev-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/contextdev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/contextdev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/contextdev-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/contextdev-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/contextdev-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/contextdev-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/contextdev-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/contextdev-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/contextdev-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/contextdev-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/contextdev-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/contextdev-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/contextdev-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/contextdev-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/contextdev-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.context.dev
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/contextdev-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/contextdev-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.context.dev/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.context.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.context.dev/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.context.dev
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.context.dev/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.context.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/context-dot-dev
- group: operate
  title: ''
  type: Support
  url: mailto:support@context.dev
- group: commercial
  title: ''
  type: Pricing
  url: https://www.context.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.context.dev/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.context.dev/privacy
- group: other
  title: ''
  type: X
  url: https://x.com/getcontextdev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/contextdev/
- group: design
  title: ''
  type: Idempotency
  url: conventions/contextdev-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/contextdev-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/contextdev-plans-pricing.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/contextdev-a2a.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/contextdev-tool-crosswalk.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/contextdev-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: security/contextdev-trust-center.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/contextdev-batch-api-overlay.yaml
- group: start
  title: ''
  type: Login
  url: https://www.context.dev/login
created: '2026-07-17'
description: Context.dev is the unified web-context API for software and AI agents — one API that turns any domain or URL into structured, typed JSON. It covers brand intelligence (logos, colors, fonts, socials, address, industry codes, stock ticker / ISIN and transaction-descriptor resolution), web scraping and crawling to clean Markdown or HTML, screenshots, sitemap discovery, web search, structured data extraction against a JSON Schema, product extraction, document parsing to Markdown, NAICS / SIC classification, and website change monitoring with signed webhooks. Typed first-party SDKs ship for TypeScript, Python, Ruby, Go, and PHP, alongside a CLI, a hosted MCP server, and a published Agent Skill. Founded in 2025 by Yahia Bakour and backed by Y Combinator (S26).
image: https://www.context.dev/logo.png
layout: provider
mcp_servers:
- description: ''
  name: contextdev-mcp.yml
  slug: contextdev-mcpyml
modified: '2026-08-14'
name: Context.dev
nav: Providers
network: true
overview: 'Context.dev publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Brand Intelligence API, Monitors API, Parsing API, and 5 more. Tagged areas include Web Scraping, Brand Intelligence, Data Enrichment, AI Agents, and Web Data.


  The Context.dev catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Context.dev''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, engineering blog, and 35 more developer resources.'
plans:
- name: Contextdev Plans Pricing
  plan_count: 5
  slug: contextdev-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 8
  name: Contextdev Rate Limits
  slug: contextdev-rate-limits
scopes:
- name: Contextdev Scopes
  scope_count: 2
  slug: contextdev-scopes
  summary_line: 2 scopes
score:
  band: exemplar
  composite: 68.5
  delta: -1.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 30.3
    contract_quality: 64.3
    developer_ergonomics: 78.6
    discoverability: 92.6
    governance: 30.3
    operational_transparency: 57.9
  previous_composite: 69.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/contextdev/refs/heads/main/screenshots/contextdev-2026-07-25T210330.png
security:
- kind: authentication
  name: Contextdev Authentication
  slug: contextdev-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Contextdev Domain Security
  slug: contextdev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Contextdev Trust Center
  slug: contextdev-trust-center
  summary_line: SOC 2 Type 1, SOC 2 Type 2
slug: contextdev
tags:
- Web Scraping
- Brand Intelligence
- Data Enrichment
- AI Agents
- Web Data
- Classification
- Website Monitoring
- Company Data
- Developer Tools
- APIs
website: https://docs.context.dev
---
