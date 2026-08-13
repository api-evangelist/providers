---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.9
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1218
  human_in_the_loop: 20
  name: Automattic Agentic Access
  operation_count: 2384
  slug: automattic-agentic-access
  summary_line: 2384 operations · 1218 acting · 20 human-in-the-loop
api_count: 9
apis:
- description: The primary WordPress.com REST API. 253 endpoints covering sites, posts, pages, comments, media, taxonomy, menus, themes, stats, Reader subscriptions, notifications, sharing and account management. Se
  name: WordPress.com REST API v1.1
  slug: wordpresscom-rest-api-v11
- description: Additive alternate version of the WordPress.com REST API. Publishes only the 38 endpoints whose contract differs from v1.1; clients mix versions per endpoint rather than migrating wholesale.
  name: WordPress.com REST API v1.2
  slug: wordpresscom-rest-api-v12
- description: Additive alternate version of the WordPress.com REST API, publishing 19 endpoints including WordPress.com marketplace search.
  name: WordPress.com REST API v1.3
  slug: wordpresscom-rest-api-v13
- description: 'The WordPress core REST API shape as served by WordPress.com, site-scoped at /wp/v2/sites/{site}/. 348 operations across posts, pages, comments, media, taxonomies, block types, block patterns, global '
  name: WordPress.com REST API - wp/v2 namespace
  slug: wordpresscom-rest-api-wpv2-namespace
- description: 'The WordPress.com and Jetpack platform extension namespace — 1,716 operations covering hosting and code deployments, domains and DNS, plans and checkout, marketplace, agency tooling, Jetpack modules, '
  name: WordPress.com REST API - wpcom/v2 namespace
  slug: wordpresscom-rest-api-wpcomv2-namespace
- description: Automattic's hosted Model Context Protocol server for WordPress.com. Streamable HTTP transport secured with OAuth 2.1 (PKCE S256, dynamic client registration, token rotation, no client secret). Twelve
  name: WordPress.com MCP Server
  slug: wordpresscom-mcp-server
- description: Akismet is Automattic's spam-classification service. Six operations — key verification, comment check, submit spam, submit ham, key sites and usage limit — authenticated with an Akismet API key. Autom
  name: Akismet API
  slug: akismet-api
- description: A small OpenAPI-described surface for listing and creating blog posts across a user's Jetpack and WordPress.com sites, published alongside the OpenAI plugin manifest at /.well-known/ai-plugin.json.
  name: Jetpack AI-Plugin API
  slug: jetpack-ai-plugin-api
- description: The GraphQL API for WordPress VIP, Automattic's enterprise WordPress and Node.js platform. Documented operation categories cover apps, domains, organizations, users, integrations, security and observa
  name: WordPress VIP Platform API
  slug: wordpress-vip-platform-api
artifact_total: 17
asyncapis:
- description: ''
  name: Automattic Wordpress Com Webhooks
  slug: automattic-wordpress-com-webhooks
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Automattic/akismet-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Automattic/akismet-api/releases
- group: company
  title: ''
  type: Website
  url: https://automattic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.wordpress.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wordpress.com/docs/api/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.wordpress.com/docs/api/rest-api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.wordpress.com/docs/api/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://wordpress.com/support/
- group: company
  title: ''
  type: Blog
  url: https://automattic.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Automattic
- group: commercial
  title: ''
  type: Pricing
  url: https://wordpress.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://developer.wordpress.com/apps/new/
- group: start
  title: ''
  type: Login
  url: https://wordpress.com/log-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wordpress.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://automattic.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://automatticstatus.com/
- group: auth
  title: ''
  type: Security
  url: https://automattic.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/automattic-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://wpvip.com/trust/
- group: auth
  title: ''
  type: Authentication
  url: authentication/automattic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/automattic-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/automattic-openid-configuration.json
- group: agent
  title: ''
  type: WellKnown
  url: well-known/automattic-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/automattic-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/automattic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/automattic-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/automattic-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/automattic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/automattic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/automattic-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/automattic-changelog.yml
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://developer.wordpress.com/changelog/
- group: design
  title: ''
  type: DataModel
  url: data-model/automattic-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/automattic-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/automattic-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/automattic-cli.yml
- group: design
  title: ''
  type: Components
  url: components/automattic-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/automattic-sandbox.yml
- group: start
  title: ''
  type: Console
  url: https://developer.wordpress.com/docs/api/console/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/automattic-wordpress-com-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/automattic-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/automattic-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/automattic-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/automattic-tool-crosswalk.yml
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/automattic_stock/
created: '2026-07-31'
description: Automattic is the company behind WordPress.com, Jetpack, WooCommerce, Tumblr, Gravatar, Akismet, WordPress VIP, Pocket Casts, Day One, Beeper and Simplenote. Its developer platform centres on the WordPress.com REST API at public-api.wordpress.com, which serves three parallel namespaces — the WordPress.com-native /rest/v1.x family, the WordPress-core-compatible /wp/v2 family, and the WordPress.com and Jetpack platform extensions in /wpcom/v2 — all behind a single OAuth 2.1 and OpenID Connect authorization server with PKCE, dynamic client registration and resource indicators. Every /rest/ version publishes a machine-readable help document and every /wp/ and /wpcom/ namespace publishes a route index, so the whole surface is self-describing even though Automattic does not ship OpenAPI for it. Automattic also runs a hosted Model Context Protocol server for WordPress.com, publishes OpenAPI for Akismet and for the Jetpack ai-plugin surface, and exposes a GraphQL Platform API for the
  enterprise WordPress VIP product.
image: https://automattic.com/wp-content/uploads/2024/11/cropped-automattic-logo-square.png
layout: provider
mcp_servers:
- description: ''
  name: automattic-mcp.yml
  slug: automattic-mcpyml
modified: '2026-07-31'
name: Automattic
nav: Providers
network: true
overview: 'Automattic publishes 7 APIs on the [APIs.io](https://apis.io/) network, including WordPress.com REST API v1.1, WordPress.com REST API v1.2, WordPress.com REST API v1.3, and 4 more. Tagged areas include Company, Content Management, Publishing, Blogging, and Website Hosting.


  The Automattic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Automattic''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 39 more developer resources.'
random_paper: 3
scopes:
- name: Automattic Scopes
  scope_count: 21
  slug: automattic-scopes
  summary_line: 21 scopes · authorizationCode/refreshToken/clientCredentials
score:
  band: strong
  composite: 56.4
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 35.6
    developer_ergonomics: 82.1
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 56.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 71.4
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/automattic/refs/heads/main/screenshots/automattic-2026-08-07T161958.png
security:
- kind: authentication
  name: Automattic Authentication
  slug: automattic-authentication
  summary_line: oauth2/openIdConnect/http/apiKey · 6 schemes
- kind: domain-security
  name: Automattic Domain Security
  slug: automattic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Automattic Vulnerability Disclosure
  slug: automattic-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Automattic Trust Center
  slug: automattic-trust-center
  summary_line: FedRAMP Moderate, SOC 2 Type I, ISO 27001, SOC 1, GovRAMP, TX-RAMP
slug: automattic
tags:
- Company
- Content Management
- Publishing
- Blogging
- Website Hosting
- Web Publishing
- Content
- Comments
- Spam Filtering
- Media
- Analytics
- Domains
- E-Commerce
- Open Source
- Developer Tools
- Model Context Protocol
website: https://automattic.com/
---
