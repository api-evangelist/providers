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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.9
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Contextdev Agentic Access
  operation_count: 84
  slug: contextdev-agentic-access
  summary_line: 84 operations · 32 acting
api_count: 1
apis:
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: The Brand Intelligence API from Context.dev — 7 operation(s) for brand intelligence.
  name: Context.dev Brand Intelligence API
  slug: contextdev-brand-intelligence-api
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: Monitor pages, sitemaps, and extracted website data for exact or semantic changes. Webhook payloads are documented by the MonitorsChangeDetectedWebhookPayload and MonitorsRunCompletedWebhookPayload sc
  name: Context.dev Monitors API
  slug: contextdev-monitors-api
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: The Parsing API from Context.dev — 1 operation(s) for parsing.
  name: Context.dev Parsing API
  slug: contextdev-parsing-api
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: The People API from Context.dev — 1 operation(s) for people.
  name: Context.dev People API
  slug: contextdev-people-api
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: The Utility API from Context.dev — 3 operation(s) for utility.
  name: Context.dev Utility API
  slug: contextdev-utility-api
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: The Web Extraction API from Context.dev — 9 operation(s) for web extraction.
  name: Context.dev Web Extraction API
  slug: contextdev-web-extraction-api
- baseURL: https://api.context.dev/v1
  baseurl_source: declared
  description: The Web Scraping API from Context.dev — 7 operation(s) for web scraping.
  name: Context.dev Web Scraping API
  slug: contextdev-web-scraping-api
artifact_total: 24
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
- group: agent
  title: ''
  type: AgentSkill
  url: skills/contextdev-scrape-in-batches.md
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
  name: Context.dev MCP Server
  slug: contextdev-mcp-server
modified: '2026-08-14'
name: Context.dev
nav: Providers
network: true
overview: 'Context.dev publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Brand Intelligence API, Monitors API, Parsing API, and 4 more. Tagged areas include Web Scraping, Brand Intelligence, Data Enrichment, AI Agents, and Web Data.


  The Context.dev catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Context.dev''s developer surface includes authentication, CLI, changelog, documentation, API reference, getting-started guide, engineering blog, and 36 more developer resources.'
plans:
- name: Contextdev Plans Pricing
  plan_count: 5
  slug: contextdev-plans-pricing
random_paper: 0
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
  band: strong
  composite: 64.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 81.6
    commercial_clarity: 81.6
    contract_governance: 18.2
    contract_quality: 61.9
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 64.8
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
website: https://docs.context.dev
---
