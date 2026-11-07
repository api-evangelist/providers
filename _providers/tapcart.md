---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: The Insights (Insights Pro) Metrics API returns aggregated analytics for a Tapcart app from a single POST endpoint whose response shape varies by the requested metricType — push explorer, sessions, re
  name: Tapcart Insights Metrics API
  slug: insights-metrics-api
- description: Tapcart's clickstream webhook delivers realtime shopper behavioral events from the mobile app to an HTTPS endpoint the merchant configures in the Tapcart dashboard. Fifteen event types are eligible fo
  name: Tapcart Clickstream Webhook
  slug: clickstream-webhook
- baseURL: https://api.tapcart.com
  baseurl_source: declared
  description: The Development API - Block Templates API from Tapcart — 4 operation(s) for development api - block templates.
  name: Tapcart Development API - Block Templates API
  slug: tapcart-development-api-block-templates-api
- baseURL: https://api.tapcart.com
  baseurl_source: declared
  description: The Development API - Blocks API from Tapcart — 1 operation(s) for development api - blocks.
  name: Tapcart Development API - Blocks API
  slug: tapcart-development-api-blocks-api
- baseURL: https://api.tapcart.com
  baseurl_source: declared
  description: The Development API - Components API from Tapcart — 5 operation(s) for development api - components.
  name: Tapcart Development API - Components API
  slug: tapcart-development-api-components-api
- baseURL: https://api.tapcart.com
  baseurl_source: declared
  description: The Development API - Dependencies API from Tapcart — 1 operation(s) for development api - dependencies.
  name: Tapcart Development API - Dependencies API
  slug: tapcart-development-api-dependencies-api
- baseURL: https://api.tapcart.com
  baseurl_source: declared
  description: The Development API - Layouts API from Tapcart — 1 operation(s) for development api - layouts.
  name: Tapcart Development API - Layouts API
  slug: tapcart-development-api-layouts-api
artifact_total: 23
asyncapis:
- description: ''
  name: Tapcart Webhooks
  slug: tapcart-webhooks
collections:
- collection_type: open
  name: Tapcart @tapcart/app-pages Development API - Block Templates API
  slug: open-tapcart-development-api-block-templates-api
- collection_type: open
  name: Tapcart @tapcart/app-pages Development API - Blocks API
  slug: open-tapcart-development-api-blocks-api
- collection_type: open
  name: Tapcart @tapcart/app-pages Development API - Components API
  slug: open-tapcart-development-api-components-api
- collection_type: open
  name: Tapcart @tapcart/app-pages Development API - Dependencies API
  slug: open-tapcart-development-api-dependencies-api
- collection_type: open
  name: Tapcart @tapcart/app-pages Development API - Layouts API
  slug: open-tapcart-development-api-layouts-api
common:
- group: commercial
  href: https://artifacts.apis.io/tapcart/plans/tapcart-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tapcart-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://www.tapcart.com/blog/rss.xml
- group: other
  href: https://artifacts.apis.io/tapcart/overlays/tapcart-client-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/tapcart-client-api-overlay.yaml
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
  href: https://artifacts.apis.io/tapcart/llms/tapcart-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tapcart-llms.txt
- group: build
  href: https://artifacts.apis.io/tapcart/packages/tapcart-packages.yml
  title: ''
  type: Packages
  url: packages/tapcart-packages.yml
- group: build
  href: https://artifacts.apis.io/tapcart/packages/tapcart-packages.yml
  title: ''
  type: SDKs
  url: packages/tapcart-packages.yml
- group: build
  href: https://artifacts.apis.io/tapcart/cli/tapcart-cli.yml
  title: ''
  type: CLI
  url: cli/tapcart-cli.yml
- group: design
  href: https://artifacts.apis.io/tapcart/components/tapcart-components.yml
  title: ''
  type: Components
  url: components/tapcart-components.yml
- group: agent
  href: https://artifacts.apis.io/tapcart/mcp/tapcart-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tapcart-mcp.yml
- group: build
  href: https://artifacts.apis.io/tapcart/mcp/tapcart-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tapcart-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/tapcart/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/tapcart/authentication/tapcart-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tapcart-authentication.yml
- group: design
  href: https://artifacts.apis.io/tapcart/conventions/tapcart-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tapcart-conventions.yml
- group: design
  href: https://artifacts.apis.io/tapcart/errors/tapcart-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tapcart-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tapcart/lifecycle/tapcart-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tapcart-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/tapcart/lifecycle/tapcart-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/tapcart-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tapcart/conformance/tapcart-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tapcart-conformance.yml
- group: design
  href: https://artifacts.apis.io/tapcart/data-model/tapcart-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tapcart-data-model.yml
- group: start
  href: https://artifacts.apis.io/tapcart/sandbox/tapcart-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tapcart-sandbox.yml
- group: design
  href: https://artifacts.apis.io/tapcart/asyncapi/tapcart-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tapcart-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/tapcart/well-known/tapcart-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tapcart-well-known.yml
- group: auth
  href: https://artifacts.apis.io/tapcart/well-known/tapcart-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tapcart-security.txt
- group: auth
  href: https://artifacts.apis.io/tapcart/security/tapcart-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tapcart-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/tapcart/security/tapcart-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tapcart-domain-security.yml
created: '2026-08-05'
description: 'Tapcart is a mobile commerce platform for Shopify merchants, turning a Shopify storefront into a native iOS and Android shopping app. Beyond the no-code app builder, Tapcart ships a developer platform: App Studio, a React-based custom block and component framework; a public Development API at api.tapcart.com for creating, versioning and publishing App Studio components, block templates, dependencies and layouts; an Insights (metrics) API for app analytics; a clickstream webhook that streams shopper behavioral events to merchant endpoints; a first-party CLI (@tapcart/tapcart-cli) with a bundled MCP server; and published AI agent skills for driving that CLI from Claude Code, Cursor or Windsurf.'
finops:
- has_sources: true
  method: derived
  name: Tapcart Finops
  primary_unit: subscription
  service_category: ''
  slug: tapcart-finops
  template: false
image: https://cdn.prod.website-files.com/616f0a7a027baaf59a43390b/693886b1460be74c44ae2eca_Open%20graphic%20home.webp
layout: provider
mcp_servers:
- description: Tapcart publishes a first-party MCP server, shipped inside the Tapcart CLI npm package rather than as a hosted remote endpoint. It exposes the CLI's capability surface — project setup, blocks, compone
  name: Tapcart MCP Server
  slug: tapcart-cli
modified: '2026-10-06'
name: Tapcart
nav: Providers
network: true
overview: 'Tapcart publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Development API - Block Templates API, Development API - Blocks API, Development API - Components API, and 4 more. Tagged areas include Company, Mobile, Commerce, Shopify, and E-Commerce.


  The Tapcart catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Tapcart''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
plans:
- name: Tapcart Plans Pricing
  plan_count: 4
  slug: tapcart-plans-pricing
- name: Tapcart Price Estimates
  plan_count: 0
  slug: tapcart-price-estimates
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Tapcart API Rules
  rule_count: 52
  severity_counts:
    error: 47
    hint: 0
    info: 2
    warn: 3
  slug: tapcart-rules
score:
  band: strong
  composite: 64.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.8
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 85.7
    discoverability: 71.7
    operational_transparency: 44.7
  previous_composite: 61.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tapcart/tapcart-2026-08-17T082251.png
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
skill_count: 2
skills:
- name: tapcart-blocks
  slug: tapcart-blocks
- name: tapcart-project
  slug: tapcart-project
slug: tapcart
tags:
- Company
- Mobile
- Commerce
- Shopify
- E-Commerce
- Mobile App
- Push Notifications
- Analytics
- Webhook
- Developer Tools
website: https://www.tapcart.com/
---
