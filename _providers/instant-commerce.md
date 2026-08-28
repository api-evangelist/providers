---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: Hosted, remote Model Context Protocol server that lets external AI clients — Claude Desktop, Cursor and other MCP clients — work with an Instant project. Documented tools list, create, edit, publish a
  name: Instant MCP Server
  slug: instant-mcp-server
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://instant.so/
- group: other
  title: ''
  type: Company
  url: https://instantcommerce.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://instant.so/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.instant.so
- group: commercial
  title: ''
  type: Pricing
  url: https://instant.so/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.instant.so/register
- group: start
  title: ''
  type: Login
  url: https://app.instant.so/login
- group: company
  title: ''
  type: Blog
  url: https://instant.so/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@instant.so
- group: commercial
  title: ''
  type: TermsOfService
  url: https://instant.so/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://instant.so/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.instant.so/
- group: operate
  title: ''
  type: Roadmap
  url: https://feedback.instant.so
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instantcommerce
- group: operate
  title: ''
  type: ChangeLog
  url: https://instant.so/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/instant-commerce-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/instant-commerce-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/instant-commerce-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/instant-commerce-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/instant-commerce-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/instant-commerce-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.instantcommerce.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.instant.so/en/articles/16068139-the-getting-started-checklist
- group: auth
  title: ''
  type: Authentication
  url: authentication/instant-commerce-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/instant-commerce-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/instant-commerce-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/instant-commerce-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/instant-commerce-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/instant-commerce-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/instant-commerce-rate-limits.yml
- group: build
  title: ''
  type: CLI
  url: cli/instant-commerce-cli.yml
- group: design
  title: ''
  type: Components
  url: components/instant-commerce-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/instant-commerce-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/instant-commerce-data-model.yml
created: '2026-07-17'
description: 'Instant Commerce (product: Instant, instant.so) is an Amsterdam- and Miami-based AI-native eCommerce software company that builds an AI-powered, no-code page builder for Shopify. Merchants describe what they want and Instant''s AI agents generate complete store pages — landing pages, homepages, product and collection pages, popups and cart drawers — including layouts, copy and AI-generated imagery, plus Figma-to-Shopify conversion, A/B testing and conversion-rate optimization. The platform serves roughly 25,000 brands. Instant''s agent surface is a hosted, remote Model Context Protocol (MCP) server at api.instant.so/mcp, shipped 2026-06-02 and labelled beta, which lets Claude Desktop, Cursor and other MCP clients list, create, edit, publish and unpublish landing pages and drive the AI page-builder agent using a project-scoped bearer access token issued in the dashboard. There is no OpenAPI, no public REST reference and no OAuth; an earlier generation of developer tooling —
  the @instantcommerce/sdk React block SDK, the @instantcommerce/cli and the developer docs at docs.instantcommerce.io — is still published but has had no release since 2023. The company has raised about $10M and is backed by HV Capital. Added to the API Evangelist network as a portfolio-company lead and enriched from public sources.'
image: https://instantcommerce.io/og-image.jpg
layout: provider
mcp_servers:
- description: Instant operates a hosted, remote Model Context Protocol (MCP) server that lets external AI clients such as Claude Desktop and Cursor work with an Instant project. It was announced in the product chan
  name: Instant Commerce MCP Server
  slug: instant-commerce-mcp-server
- description: ''
  name: Instant Commerce MCP Server
  slug: instant-commerce-mcp-server-2
modified: '2026-08-13'
name: Instant Commerce
nav: Providers
network: true
overview: 'Instant Commerce publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai Enterprise Software, E-Commerce, Shopify, and No-Code.


  Instant Commerce''s developer surface includes documentation, pricing, signup flow, engineering blog, support, changelog, getting-started guide, and 27 more developer resources.'
plans:
- name: Instant Commerce Plans Pricing
  plan_count: 5
  slug: instant-commerce-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Instant Commerce Rate Limits
  slug: instant-commerce-rate-limits
score:
  band: developing
  composite: 45.9
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 45.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/instant-commerce/refs/heads/main/screenshots/instant-commerce-2026-07-25T222609.png
security:
- kind: authentication
  name: Instant Commerce Authentication
  slug: instant-commerce-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Instant Commerce Domain Security
  slug: instant-commerce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instant-commerce
tags:
- Company
- Ai Enterprise Software
- E-Commerce
- Shopify
- No-Code
- Page Builder
- Artificial Intelligence
- AI Agents
- Conversion Rate Optimization
- Developer Tools
- MCP
- agent-native
website: https://instant.so/
---
