---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-08-10'
api_count: 7
apis:
- description: The Insights (Insights Pro) Metrics API returns aggregated analytics for a Tapcart app from a single POST endpoint whose response shape varies by the requested metricType — push explorer, sessions, re
  name: Tapcart Insights Metrics API
  slug: insights-metrics-api
- description: Tapcart's clickstream webhook delivers realtime shopper behavioral events from the mobile app to an HTTPS endpoint the merchant configures in the Tapcart dashboard. Fifteen event types are eligible fo
  name: Tapcart Clickstream Webhook
  slug: clickstream-webhook
- description: The Development API - Block Templates API from Tapcart — 4 operation(s) for development api - block templates.
  name: Tapcart Development API - Block Templates API
  slug: tapcart-development-api-block-templates-api
- description: The Development API - Blocks API from Tapcart — 1 operation(s) for development api - blocks.
  name: Tapcart Development API - Blocks API
  slug: tapcart-development-api-blocks-api
- description: The Development API - Components API from Tapcart — 5 operation(s) for development api - components.
  name: Tapcart Development API - Components API
  slug: tapcart-development-api-components-api
- description: The Development API - Dependencies API from Tapcart — 1 operation(s) for development api - dependencies.
  name: Tapcart Development API - Dependencies API
  slug: tapcart-development-api-dependencies-api
- description: The Development API - Layouts API from Tapcart — 1 operation(s) for development api - layouts.
  name: Tapcart Development API - Layouts API
  slug: tapcart-development-api-layouts-api
artifact_total: 12
asyncapis:
- description: ''
  name: Tapcart Webhooks
  slug: tapcart-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.tapcart.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.tapcart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.tapcart.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dev.tapcart.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.tapcart.com/docs/app-studio-quick-start
- group: operate
  title: ''
  type: Support
  url: https://help.tapcart.com/en/
- group: company
  title: ''
  type: Blog
  url: https://www.tapcart.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tapcartinc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tapcart.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.tapcart.com/get-started
- group: start
  title: ''
  type: Login
  url: https://app.tapcart.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tapcart.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tapcart.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tapcart.co/
- group: auth
  title: ''
  type: Security
  url: https://security.tapcart.com/vulnerability-program.html
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tapcart-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/tapcart-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tapcart-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/tapcart-cli.yml
- group: design
  title: ''
  type: Components
  url: components/tapcart-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tapcart-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tapcart-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tapcart-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tapcart-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tapcart-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tapcart-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/tapcart-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tapcart-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tapcart-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tapcart-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tapcart-webhooks.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tapcart-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/tapcart-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tapcart-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tapcart-domain-security.yml
created: '2026-08-05'
description: 'Tapcart is a mobile commerce platform for Shopify merchants, turning a Shopify storefront into a native iOS and Android shopping app. Beyond the no-code app builder, Tapcart ships a developer platform: App Studio, a React-based custom block and component framework; a public Development API at api.tapcart.com for creating, versioning and publishing App Studio components, block templates, dependencies and layouts; an Insights (metrics) API for app analytics; a clickstream webhook that streams shopper behavioral events to merchant endpoints; a first-party CLI (@tapcart/tapcart-cli) with a bundled MCP server; and published AI agent skills for driving that CLI from Claude Code, Cursor or Windsurf.'
image: https://cdn.prod.website-files.com/616f0a7a027baaf59a43390b/693886b1460be74c44ae2eca_Open%20graphic%20home.webp
layout: provider
mcp_servers:
- description: ''
  name: tapcart-mcp.yml
  slug: tapcart-mcpyml
modified: '2026-08-05'
name: Tapcart
nav: Providers
network: true
overview: 'Tapcart publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Development API - Block Templates API, Development API - Blocks API, Development API - Components API, and 2 more. Tagged areas include Company, Mobile, Commerce, Shopify, and Ecommerce.


  The Tapcart catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tapcart''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 29 more developer resources.'
random_paper: 55
score:
  band: strong
  composite: 58.0
  delta: -0.8
  facets:
    commercial_clarity: 44.7
    contract_quality: 59.5
    developer_ergonomics: 87.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 58.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Tapcart Authentication
  slug: tapcart-authentication
  summary_line: http/apiKey · 5 schemes
- kind: domain-security
  name: Tapcart Domain Security
  slug: tapcart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tapcart Vulnerability Disclosure
  slug: tapcart-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: tapcart
tags:
- Company
- Mobile
- Commerce
- Shopify
- Ecommerce
- Mobile Apps
- Push Notifications
- Analytics
- Webhooks
- Developer Tools
website: https://www.tapcart.com/
---
