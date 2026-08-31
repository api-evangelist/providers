---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.2
  scored_at: '2026-08-30'
api_count: 3
apis:
- description: The ecforce platform REST API. Version 2 splits into v2/admin (administrator-scoped, mirroring the ecforce management screens) and v2/customer (shopper-scoped, mirroring My Page). Responses are JSON:A
  name: ecforce API v2
  slug: ecforce-api-v2
- description: The internal HTTP API behind ecforce AI, called from the first-party @super_studio/ecforce-ai-agent-server npm SDK. It issues chat session tokens, resolves users, records terms acceptance, returns per
  name: ecforce AI Agent API
  slug: ecforce-ai-agent-api
- description: 'A remote, OAuth-protected Model Context Protocol server launched 2026-08-04 that lets external AI tools (Claude Code, Cursor, the ChatGPT app/Codex) read ecforce order and product data, query ecforce '
  name: ecforce AI MCP
  slug: ecforce-ai-mcp
artifact_total: 11
asyncapis:
- description: ''
  name: Super Studio Ecforce Webhooks
  slug: super-studio-ecforce-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.super-studio.jp/
- group: company
  title: ''
  type: ProductWebsite
  url: https://ec-force.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ec-force.com/
- group: docs
  title: ''
  type: APIReference
  url: https://apidoc.ec-force.com/apidoc/v2/admin/index.html
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.ec-force.com/hc/ja
- group: operate
  title: ''
  type: Support
  url: https://ec-force.com/support
- group: company
  title: ''
  type: Blog
  url: https://ec-force.com/blog/
- group: company
  title: ''
  type: TechnicalBlog
  url: https://zenn.dev/p/superstudio
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/super-studio
- group: commercial
  title: ''
  type: Pricing
  url: https://ec-force.com/product_plan
- group: start
  title: ''
  type: SignUp
  url: https://ec-force.com/contact/new
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ec-force.com/info/customer_term
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.super-studio.jp/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://ec-force.com/security
- group: start
  title: ''
  type: GettingStarted
  url: https://ec-force.com/startguide
- group: build
  title: ''
  type: Packages
  url: packages/super-studio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/super-studio-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/super-studio-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/super-studio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/super-studio-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/super-studio-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/super-studio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/super-studio-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/super-studio-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/super-studio-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/super-studio-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/super-studio-trust-center.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/super-studio-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/super-studio-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/super-studio-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/super-studio-ecforce-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/super-studio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/super-studio-rate-limits.yml
created: '2026-08-29'
description: 'SUPER STUDIO (株式会社SUPER STUDIO) is a Tokyo-based commerce software company founded in 2014 that builds "ecforce", an AI commerce platform used by Japanese D2C and subscription brands for storefronts, order management, subscriptions, CRM, marketing automation and BI. The platform is multi-tenant and API-integrable: ecforce exposes a versioned REST admin/customer API (v2, JSON:API shaped, token authenticated) on each merchant''s own shop host, a webhook surface signalled with an x-ecf-event header, and — since August 2026 — an OAuth-protected remote MCP server under agent.ec-force.com that lets external AI tools such as Claude Code, Cursor and the ChatGPT app read ecforce order and product data and drive ecforce bi, ma and AIdp. SUPER STUDIO also publishes first-party npm packages for the ecforce AI Agent (server SDK and React chat UI) and the "albers" design system. The API reference itself sits behind HTTP Basic auth at apidoc.ec-force.com and API integration is a paid contract
  option.'
image: https://www.super-studio.jp/superstudio_ogp.png?version=2
layout: provider
mcp_servers:
- description: ''
  name: ecforce AI MCP
  slug: ecforce-ai-mcp
modified: '2026-08-29'
name: SUPER STUDIO
nav: Providers
network: true
overview: 'SUPER STUDIO publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Commerce, Subscription Commerce, and Order Management.


  The SUPER STUDIO catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SUPER STUDIO''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, getting-started guide, and 26 more developer resources.'
plans:
- name: Super Studio Plans Pricing
  plan_count: 4
  slug: super-studio-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Super Studio Rate Limits
  slug: super-studio-rate-limits
scopes:
- name: Super Studio Scopes
  scope_count: 0
  slug: super-studio-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 17
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 51.2
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 53.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: authentication
  name: Super Studio Authentication
  slug: super-studio-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Super Studio Domain Security
  slug: super-studio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Super Studio Trust Center
  slug: super-studio-trust-center
  summary_line: ISO/IEC 27001 (ISMS), PrivacyMark (JIS Q 15001), PCI DSS, SOC 1 Type 1, SOC 2 Type 1
slug: super-studio
tags:
- Company
- E-Commerce
- Commerce
- Subscription Commerce
- Order Management
- Marketing Automation
- Business Intelligence
- Software-as-a-Service
- Artificial Intelligence
- Agents
- MCP
- Japan
website: https://www.super-studio.jp/
---
