---
access_model:
  confidence: high
  label: Enterprise API access arranged through sales
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - https://docs.mobileaction.co/guide/introduction
  - https://docs.mobileaction.co/mcp/server-setup
  - https://www.mobileaction.co/pricing/
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
  score: 12.3
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Credit-metered REST intelligence API exposing App Store and Google Play keyword rankings, app metadata, ad creatives, Apple Search Ads / CPP data, and dashboard resources. Authenticated with an accoun
  name: MobileAction API
  slug: mobileaction-api
- description: Remote Model Context Protocol server exposing 88 MobileAction tools (App Store and Google Play keyword/category/app intelligence, Ad Intelligence, CPP Intelligence, Dashboard, Search Ads and utility s
  name: MobileAction MCP Server
  slug: mobileaction-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://mobileaction.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mobileaction.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mobileaction.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mobileaction.co/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mobileaction.co/guide/introduction
- group: auth
  title: ''
  type: Authentication
  url: authentication/mobile-action-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mobile-action-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mobile-action-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mobileaction.co
- group: design
  title: ''
  type: Conformance
  url: conformance/mobile-action-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mobile-action-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/mobile-action-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.mobileaction.co/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mobile-action-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.mobileaction.co/en
- group: company
  title: ''
  type: Blog
  url: https://www.mobileaction.co/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mobileaction.co/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.mobileaction.co/register
- group: start
  title: ''
  type: Login
  url: https://app.mobileaction.co/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mobileaction.co/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mobileaction.co/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mobileaction
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mobile-action-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mobile-action-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Packages
  url: packages/mobile-action-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mobile-action-well-known.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mobile-action-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mobile-action-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/mobile-action-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mobile-action-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mobile-action-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mobile-action-llms-published.txt
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpcenter.mobileaction.co/en
created: '2026-07-17'
description: 'MobileAction is an app-store marketing intelligence platform used by 5,000+ mobile app and game companies for App Store Optimization (ASO), Apple Ads campaign management (CMP), ad-creative intelligence across 90M+ creatives, CPP (Custom Product Page) intelligence and market benchmarking. It is an InMobi Advertising company. MobileAction publishes two machine surfaces over the same intelligence core and the same credit allowance: a credit-metered REST API at https://api.mobileaction.co, authenticated with a per-account API key passed as the `token` query parameter, covering App Store and Google Play keyword and category rankings, app metadata and version timelines, reviews and review word analysis, download/revenue estimations, ad creatives, Apple Ads reporting and dashboard data; and a remote MCP server at https://mcp.mobileaction.co/mcp exposing 88 tools whose catalogue is readable anonymously. No OpenAPI document is published. API access is enterprise-only, arranged through
  sales, with keys issued by a Customer Success Manager. Backed by 500 Global.'
image: https://www.mobileaction.co/wp-content/uploads/ma-featured-image-1.png
layout: provider
mcp_servers:
- description: ''
  name: MobileAction
  slug: mobileaction
modified: '2026-08-13'
name: Mobile Action
nav: Providers
network: true
overview: 'Mobile Action publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, App Store Optimization, ASO, Mobile Marketing, and Apple Search Ads.


  Mobile Action''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 27 more developer resources.'
plans:
- name: Mobile Action Plans Pricing
  plan_count: 0
  slug: mobile-action-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 48
  name: Mobile Action Rate Limits
  slug: mobile-action-rate-limits
scopes:
- name: Mobile Action Scopes
  scope_count: 3
  slug: mobile-action-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 33.5
  delta: 0.0
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 33.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mobile-action/refs/heads/main/screenshots/mobile-action-2026-08-07T183845.png
security:
- kind: authentication
  name: Mobile Action Authentication
  slug: mobile-action-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mobile Action Domain Security
  slug: mobile-action-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Mobile Action Trust Center
  slug: mobile-action-trust-center
  summary_line: SOC 2, GDPR
slug: mobile-action
tags:
- Company
- App Store Optimization
- ASO
- Mobile Marketing
- Apple Search Ads
- App Intelligence
- Ad Intelligence
- Market Intelligence
- Analytics
- MCP
- Agent Tools
- App Store Intelligence
- Mobile Measurement
website: https://mobileaction.co
---
