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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 68.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 102
  human_in_the_loop: 2
  name: Tiktok Ads Agentic Access
  operation_count: 202
  slug: tiktok-ads-agentic-access
  summary_line: 202 operations · 102 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: RESTful Marketing API for managing TikTok ad accounts, campaigns, ad groups, ads, Upgraded Smart+ and GMV Max campaigns, creatives, files, catalogs, audiences, Business Centers, conversions, pixels an
  name: TikTok Marketing API
  slug: marketing-api
artifact_total: 12
asyncapis:
- description: ''
  name: Tiktok Ads Webhooks
  slug: tiktok-ads-webhooks
collections:
- collection_type: open
  name: TikTok API for Business — Marketing API
  slug: open-tiktok-ads-marketing-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/tiktok-ads-marketing-api-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tiktok-ads-marketing-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tiktok-ads-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/tiktok-ads-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tiktok-ads-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tiktok-ads-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tiktok-ads-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tiktok-ads-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tiktok-ads-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tiktok-ads-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tiktok-ads-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tiktok-ads-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tiktok-ads-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/tiktok-ads-plans-pricing.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tiktok-ads-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tiktok-ads-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tiktok-ads-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://business-api.tiktok.com/portal/api-service-status
- group: operate
  title: ''
  type: Deprecation
  url: https://business-api.tiktok.com/portal/docs?id=1740578661644289
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/tiktok-ads-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tiktok-ads-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/tiktok-ads-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tiktok-ads-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tiktok-ads-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tiktok-ads-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/tiktok
- group: company
  title: ''
  type: Website
  url: https://www.tiktok.com/business/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://business-api.tiktok.com/portal
- group: docs
  title: ''
  type: Documentation
  url: https://business-api.tiktok.com/portal/docs
- group: docs
  title: ''
  type: APIReference
  url: https://business-api.tiktok.com/portal/docs?id=1735713875563521
- group: start
  title: ''
  type: GettingStarted
  url: https://business-api.tiktok.com/portal/docs?id=1735713609895937
- group: build
  title: ''
  type: Postman
  url: https://business-api.tiktok.com/portal/docs?id=1747849403155521
- group: operate
  title: ''
  type: Support
  url: https://ads.tiktok.com/help/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tiktok
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/tiktok/tiktok-business-api-sdk
- group: company
  title: ''
  type: Blog
  url: https://ads.tiktok.com/business/en/blog
- group: company
  title: ''
  type: DeveloperBlog
  url: https://business-api.tiktok.com/portal/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tiktok.com/business/en/pricing
- group: start
  title: ''
  type: SignUp
  url: https://ads.tiktok.com/i18n/signup
- group: start
  title: ''
  type: Login
  url: https://ads.tiktok.com/i18n/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tiktok.com/legal/page/global/terms-of-service/en
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tiktok.com/legal/page/global/privacy-policy/en
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/tiktokforbusiness/
created: '2026-05-11'
description: TikTok for Business is TikTok's advertising platform, where brands, agencies and advertisers create, manage and optimize ad campaigns across TikTok and its family of apps. The TikTok API for Business — the Marketing API at business-api.tiktok.com/open_api/v1.3 — is the REST interface behind it, covering advertiser accounts, campaigns, ad groups, ads, Upgraded Smart+ and GMV Max automation, creatives and files, product catalogs, custom and lookalike audiences, Business Center asset and member administration, conversion measurement through the Events API, and synchronous plus asynchronous reporting. Access is granted by a three-legged advertiser authorization that issues a long-lived token presented in an Access-Token header, with permissions expressed as a three-level hierarchy of numeric scope IDs. TikTok also operates a hosted Model Context Protocol server that packages roughly 400 of these endpoints as OAuth-protected MCP tools for AI agents.
graphqls:
- description: TikTok Marketing API covers campaign management, ad groups, creatives, audiences, targeting options, pixel events, attribution, and reporting for TikTok advertising.
  name: TikTok Marketing API GraphQL API
  slug: tiktok-ads-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tiktok-ads.png
layout: provider
mcp_servers:
- description: ''
  name: tiktok-ads-mcp.yml
  slug: tiktok-ads-mcpyml
modified: '2026-08-13'
name: TikTok Marketing API
nav: Providers
network: true
overview: 'TikTok Marketing API publishes 1 API on the [APIs.io](https://apis.io/) network: TikTok Marketing API. Tagged areas include Advertising, Marketing, Social Media, Ad Campaigns, and Performance Marketing.


  The TikTok Marketing API catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  TikTok Marketing API''s developer surface includes authentication, sandbox, changelog, documentation, API reference, getting-started guide, support, and 37 more developer resources.'
plans:
- name: Tiktok Ads Plans Pricing
  plan_count: 0
  slug: tiktok-ads-plans-pricing
random_paper: 125
rate_limits:
- limit_count: 0
  name: Tiktok Ads Rate Limits
  slug: tiktok-ads-rate-limits
scopes:
- name: Tiktok Ads Scopes
  scope_count: 0
  slug: tiktok-ads-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.7
  delta: 33.5
  facets:
    commercial_clarity: 44.7
    contract_quality: 61.5
    developer_ergonomics: 84.8
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 63.2
  previous_composite: 27.2
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/tiktok-ads/refs/heads/main/screenshots/tiktok-ads-2026-06-20T195404.png
security:
- kind: authentication
  name: Tiktok Ads Authentication
  slug: tiktok-ads-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Tiktok Ads Domain Security
  slug: tiktok-ads-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tiktok Ads Vulnerability Disclosure
  slug: tiktok-ads-vulnerability-disclosure
  summary_line: Hackerone · security.txt
slug: tiktok-ads
tags:
- Advertising
- Marketing
- Social Media
- Ad Campaigns
- Performance Marketing
- Conversion Tracking
- Audience Management
- Reporting
- Product Catalog
- Agent Ready
website: https://www.tiktok.com/business/
---
