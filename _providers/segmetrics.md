---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: 'The v1 Import API lets a customer push their own data into a SegMetrics integration — contacts (with UTM attribution, geo, affiliate and custom fields), tags, orders/invoices, subscriptions, products '
  name: SegMetrics Import API
  slug: segmetrics-import-api
- description: The Reporting API returns the metrics SegMetrics generates — saved report data (KPIs, graph series and a table of fields and rows), a customer-journey export of the contacts behind a report, an ad-hoc
  name: SegMetrics Reporting API
  slug: segmetrics-reporting-api
- description: A hosted, read-only Model Context Protocol server that gives Claude, ChatGPT and other MCP clients direct access to a SegMetrics account. Eleven tools split into discovery (get-account-info, get-metri
  name: SegMetrics MCP Server
  slug: segmetrics-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://segmetrics.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.segmetrics.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.segmetrics.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.segmetrics.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.segmetrics.io/#getting-started
- group: operate
  title: ''
  type: Support
  url: https://docs.segmetrics.io/contact/
- group: company
  title: ''
  type: Blog
  url: https://segmetrics.io/articles/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SegMetrics
- group: commercial
  title: ''
  type: Pricing
  url: https://segmetrics.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.segmetrics.io/signup/
- group: start
  title: ''
  type: Login
  url: https://app.segmetrics.io/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://segmetrics.io/terms-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://segmetrics.io/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.segmetrics.io/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/segmetrics-changelog.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/segmetrics-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/segmetrics-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/segmetrics-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/segmetrics-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/segmetrics-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/segmetrics-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/segmetrics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/segmetrics-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/segmetrics-packages.yml
- group: design
  title: ''
  type: Components
  url: components/segmetrics-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/segmetrics-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/segmetrics-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://segmetrics.io/security/
- group: auth
  title: ''
  type: Security
  url: https://segmetrics.io/security/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/segmetrics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/segmetrics-domain-security.yml
created: '2026-08-12'
description: 'SegMetrics is a marketing attribution and revenue analytics platform for digital marketers, info-product businesses and agencies. It stitches ad clicks, opt-ins, email engagement, calls and purchases into a single contact journey so a business can see which traffic sources, campaigns and funnels actually produce revenue and lifetime value rather than just clicks. The platform connects to 100+ marketing tools (ActiveCampaign, Kit/ConvertKit, ClickFunnels, HighLevel, Drip, Ontraport, WooCommerce, Google Ads, Microsoft Advertising and more) and adds fingerprint tracking, full-LTV attribution, multi-report tables, custom dashboards and data monitors on top. Developers get three public surfaces: a v1 Import API at import.segmetrics.io for pushing contacts, tags, orders, subscriptions, products and ad performance into an integration; a Reporting API at api.segmetrics.io for saved reports, customer-journey exports and ad-hoc /v2 data queries; and a read-only hosted MCP server at app.segmetrics.io/mcp
  that exposes 11 OAuth-protected tools to Claude, ChatGPT and other MCP clients. API access is gated to the Scale tier and above.'
image: https://segmetrics.io/wp-content/uploads/2016/02/cropped-icon-lg-300x300.png
layout: provider
mcp_servers:
- description: ''
  name: segmetrics-mcp.yml
  slug: segmetrics-mcpyml
modified: '2026-08-12'
name: SegMetrics
nav: Providers
network: true
overview: 'SegMetrics publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketing, Analytics, Attribution, and Marketing Analytics.


  SegMetrics'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Segmetrics Plans Pricing
  plan_count: 4
  slug: segmetrics-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Segmetrics Rate Limits
  slug: segmetrics-rate-limits
score:
  band: developing
  composite: 44.4
  delta: -0.4
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 44.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/segmetrics/refs/heads/main/screenshots/segmetrics-2026-08-17T081754.png
security:
- kind: authentication
  name: Segmetrics Authentication
  slug: segmetrics-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Segmetrics Domain Security
  slug: segmetrics-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Segmetrics Vulnerability Disclosure
  slug: segmetrics-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: segmetrics
tags:
- Company
- Marketing
- Analytics
- Attribution
- Marketing Analytics
- Reporting
- Business Intelligence
- Advertising
- SaaS
- MCP
website: https://segmetrics.io/
---
