---
access_model:
  confidence: high
  label: Enterprise
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://skai.io/pricing/
  - https://developers.skai.io/
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Skai's REST API for programmatic access to advertising data and campaign management across search, social and retail-media publishers. Reporting is the primary surface — synchronous for small pulls, a
  name: Skai (Kenshoo) API
  slug: skai-kenshoo-api
- description: First-party hosted, remote Model Context Protocol servers exposing the Skai platform to AI assistants. The Reporting MCP is read-only and publishes five tools — fetch_report, relevant_columns, get_tod
  name: Skai MCP Servers
  slug: skai-mcp-servers
artifact_total: 11
collections:
- collection_type: open
  name: Skai API
  slug: open-skai-kenshoo-api
common:
- group: company
  title: ''
  type: Website
  url: https://skai.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.skai.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.skai.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.kenshoo.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.skai.io/#section/Authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://skai.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://skai.io/blog/
- group: operate
  title: ''
  type: Support
  url: https://skai.io/contact-us/
- group: start
  title: ''
  type: Login
  url: https://app.kenshoo.com/portal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://skai.io/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://skai.io/legal/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kenshoo
- group: operate
  title: ''
  type: StatusPage
  url: https://status.skai.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://skai.io/skai-information-security-and-privacy-center/
- group: auth
  title: ''
  type: Compliance
  url: https://skai.io/skai-information-security-and-privacy-center/
- group: auth
  title: ''
  type: Security
  url: https://skai.io/skai-information-security-and-privacy-center/
- group: design
  title: ''
  type: Conformance
  url: conformance/skai-kenshoo-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/skai-kenshoo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skai-kenshoo-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/skai-kenshoo-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/skai-kenshoo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/skai-kenshoo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/skai-kenshoo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/skai-kenshoo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/skai-kenshoo-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/skai-kenshoo-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/skai-kenshoo-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/skai-kenshoo-packages.yml
- group: design
  title: ''
  type: Components
  url: components/skai-kenshoo-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/skai-kenshoo-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/skai-kenshoo-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/skai-kenshoo-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/skai-kenshoo-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/skai-kenshoo-api-overlay.yaml
created: '2026-07-17'
description: Skai (formerly Kenshoo) is an AI-powered commerce media platform that helps brands and agencies centralize retail media, paid search, and paid social data, then plan, activate, optimize, and measure omnichannel marketing campaigns across Amazon, Google, Microsoft, Meta, Walmart, Instacart, Kroger, Target and 120+ other publishers and marketplaces. Skai publishes a real, anonymously readable OpenAPI 3.0.0 contract — 117 paths, 158 operations, 155 schemas — served through a Redoc developer hub at developers.skai.io and callable at services.kenshoo.com, covering reporting (synchronous and asynchronous), bulk entity management, campaigns, ad groups, ads, portfolios, product groups, custom columns, incrementality testing and budget pacing. Alongside the REST API, Skai runs first-party hosted MCP servers at mcp.kenshoo.com — a read-only Reporting MCP and a write-access Operations MCP for bid, budget and status changes with preview and approval — authenticated with OAuth 2.0 or a 90-day
  personal access token. Products include Celeste AI (a GenAI commerce-media agent), the Skai Data Hub, Retail Media, Search & Social, Omnichannel Planning, and Digital Shelf Optimization.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skai-kenshoo.png
layout: provider
mcp_servers:
- description: ''
  name: Skai (Kenshoo) MCP Server
  slug: skai-kenshoo-mcp-server
modified: '2026-08-12'
name: Skai (Kenshoo)
nav: Providers
network: true
overview: 'Skai (Kenshoo) publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Commerce, Advertising, Marketing, and Retail Media.


  Skai (Kenshoo)''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, authentication, and 28 more developer resources.'
plans:
- name: Skai Kenshoo Plans Pricing
  plan_count: 5
  slug: skai-kenshoo-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Skai Kenshoo Rate Limits
  slug: skai-kenshoo-rate-limits
scopes:
- name: Skai Kenshoo Scopes
  scope_count: 0
  slug: skai-kenshoo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 54.2
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 30.3
    contract_quality: 33.3
    developer_ergonomics: 58.9
    discoverability: 68.5
    governance: 30.3
    operational_transparency: 50.0
  previous_composite: 54.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skai-kenshoo/refs/heads/main/screenshots/skai-kenshoo-2026-08-17T081910.png
security:
- kind: authentication
  name: Skai Kenshoo Authentication
  slug: skai-kenshoo-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Skai Kenshoo Domain Security
  slug: skai-kenshoo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Skai Kenshoo Vulnerability Disclosure
  slug: skai-kenshoo-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Skai Kenshoo Trust Center
  slug: skai-kenshoo-trust-center
  summary_line: ISO/IEC 27001:2013, SOC 2 Type 2, ISO 9001:2015
slug: skai-kenshoo
tags:
- Company
- Commerce
- Advertising
- Marketing
- Retail Media
- Paid Search
- Paid Social
- Marketing Analytics
- Advertising Technology
- Campaign Management
- Commerce Media
- Reporting
- MCP
- agent-native
- Omnichannel
website: https://skai.io/
---
