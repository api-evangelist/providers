---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 31.2
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: 'Token-authenticated REST endpoints under https://api.webz.io covering seven products: News, Blogs and Forums (/api/news, /api/blogs, /api/forums plus /seg_api/* segmentation), Reviews (/reviewFilter, '
  name: Webz.io API
  slug: webzio-api
- description: A first-party remote Model Context Protocol server that exposes Webz.io semantic news search to any MCP client. It ships one tool, news_search_by_webz, and every call runs a regular News Search API re
  name: Webz.io News Search MCP Server
  slug: webzio-news-search-mcp-server
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/webz-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/webz-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/webz-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/webz-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/webz-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/webz-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/webz-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/webz-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/webz-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/webz-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/webz-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.webz.io
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/webz-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/webz-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/webz-trust-center.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/webz-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/webz-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/webz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/webz-rate-limits.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.webz.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.webz.io/docs/webz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.webz.io/docs/webz/news-blogs-forums-api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.webz.io/docs/webz/start-here
- group: operate
  title: ''
  type: Support
  url: https://webz.io/contact-us
- group: company
  title: ''
  type: Blog
  url: https://webz.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Webhose
- group: commercial
  title: ''
  type: Pricing
  url: https://webz.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.webz.io/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.webz.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://webz.io/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://webz.io/privacy/
created: '2026-08-27'
description: Webz.io provides structured web-data feeds and APIs covering the open, deep, and dark web for AI, cybersecurity, and intelligence use cases. Content is collected at scale, normalized, enriched with metadata, and delivered through machine-readable data feeds and token-authenticated REST APIs.
image: https://webz.io/wp-content/uploads/2026/08/Webz.io-og-image.png
layout: provider
mcp_servers:
- description: A first-party remote MCP server that exposes Webz.io semantic news search to any MCP client. It ships exactly one tool, news_search_by_webz, and every call runs a regular News Search API request again
  name: Webz.io News Search MCP
  slug: webzio-news-search-mcp
- description: ''
  name: Webz.io MCP Server
  slug: webzio-mcp-server
modified: '2026-08-27'
name: Webz.io
nav: Providers
network: true
overview: 'Webz.io publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include News Data, Web Data, Web Scraping, Dark Web, and deep-web.


  Webz.io''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Webz Plans Pricing
  plan_count: 6
  slug: webz-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 6
  name: Webz Rate Limits
  slug: webz-rate-limits
scopes:
- name: Webz Scopes
  scope_count: 0
  slug: webz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 16
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 57.9
  previous_composite: 50.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Webz Authentication
  slug: webz-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Webz Domain Security
  slug: webz-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Webz Trust Center
  slug: webz-trust-center
  summary_line: SOC 2, ISO 27001
slug: webz
tags:
- News Data
- Web Data
- Web Scraping
- Dark Web
- deep-web
- Cybersecurity
- Threat Intelligence
- Data Breach
- pii-monitoring
- OSINT
- reviews-data
- AI Training Data
- Media Monitoring
website: https://docs.webz.io/
---
