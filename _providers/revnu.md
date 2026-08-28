---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: A live remote MCP server over streamable HTTP that gives an AI assistant operator-level control of a Revnu store — 49 documented tools across store, products, coupons, analytics, purchases, affiliates
  name: Revnu MCP Server
  slug: revnu-mcp-server
- description: The authentication API behind the @revnu/auth SDK, serving a Revnu store's buyers. Purchase-first — buying a product creates the account and sends a password setup link, so there is no separate sign-u
  name: Revnu Auth API
  slug: revnu-auth-api
artifact_total: 8
asyncapis:
- description: ''
  name: Revnu Webhooks
  slug: revnu-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://revnu.com
- group: commercial
  title: ''
  type: Pricing
  url: https://revnu.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://revnu.com/blog
- group: company
  title: ''
  type: About
  url: https://revnu.com/about
- group: operate
  title: ''
  type: Support
  url: https://revnu.com/faq
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/MBsVQ9eFKg
- group: start
  title: ''
  type: SignUp
  url: https://revnu.com/book
- group: commercial
  title: ''
  type: TermsOfService
  url: https://revnu.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://revnu.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revnu-app
- group: docs
  title: ''
  type: Documentation
  url: https://auth.revnu.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://auth.revnu.app/docs/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://auth.revnu.app/docs/getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://auth.revnu.app/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revnu-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/revnu-app-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/revnu-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/revnu-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/revnu-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/revnu-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/revnu-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/revnu-cli.yml
- group: design
  title: ''
  type: Components
  url: components/revnu-components.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revnu-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/revnu-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/revnu-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/revnu-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/revnu-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/revnu-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/revnu-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/revnu-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/revnu-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/revnu-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revnu-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Revnu is an AI growth-automation platform for early-stage and technical founders, positioning itself as an "AI growth hire" that runs marketing work across channels so builders can stay in the codebase. The platform finds and qualifies leads from real signals, drafts cold outbound and partnership pitches, writes SEO content, runs paid ad experiments across Meta, LinkedIn, Reddit, and TikTok, turns product wins into short-form video and social posts, and tests pricing and landing-page copy. Founded in 2026 out of the Y Combinator Spring 2026 batch and based in San Francisco, Revnu is agent-first rather than API-first: it publishes no OpenAPI, but it does ship a live remote MCP server with a documented 49-tool surface, a first-party CLI, an authentication SDK for a customer''s own app, an HMAC-signed webhook catalog, an RFC 9727 api-catalog, and machine-readable llms.txt context files across its hosts.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revnu.png
layout: provider
mcp_servers:
- description: Manage a Revnu store, products, A/B tests, SEO content, ads, coupons, affiliates, and analytics via MCP.
  name: MCP Server
  slug: mcp-server
modified: '2026-08-13'
name: Revnu
nav: Providers
network: true
overview: 'Revnu publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Growth Automation, Marketing, Artificial Intelligence, and Software-as-a-Service.


  The Revnu catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Revnu''s developer surface includes pricing, engineering blog, support, signup flow, documentation, API reference, getting-started guide, and 28 more developer resources.'
plans:
- name: Revnu Plans Pricing
  plan_count: 1
  slug: revnu-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Revnu Rate Limits
  slug: revnu-rate-limits
score:
  band: developing
  composite: 49.6
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 63.7
    discoverability: 87.0
    governance: 4.5
    operational_transparency: 28.9
  previous_composite: 49.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revnu/refs/heads/main/screenshots/revnu-2026-08-17T081547.png
security:
- kind: authentication
  name: Revnu Authentication
  slug: revnu-authentication
  summary_line: http/apiKey · 4 schemes
- kind: domain-security
  name: Revnu Domain Security
  slug: revnu-domain-security
  summary_line: TLSv1.3 · HSTS
slug: revnu
tags:
- Company
- Growth Automation
- Marketing
- Artificial Intelligence
- Software-as-a-Service
- Startups
- Lead Generation
- SEO
- MCP
- Agents
- Commerce
- A/B Testing
website: https://revnu.com
---
