---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 62.6
  scored_at: '2026-08-17'
api_count: 4
apis:
- description: The G2 API V2 provides programmatic access to G2's software reviews, buyer intent signals, competitive intelligence, and product data. Uses OAuth 2.0 for authentication. Enables integration of G2 buye
  name: G2 API V2
  slug: g2-api-v2
- description: 'G2 Buyer Intent Data provides signals about companies actively researching software categories, products, and competitors on G2. Tracks nine signal types including profile views, pricing page visits, '
  name: G2 Buyer Intent Data API
  slug: g2-buyer-intent-data
- description: The G2 MCP (Model Context Protocol) Server enables AI assistants like Claude to access G2 data. Uses OAuth for authentication via browser sign-in. Provides access to buyer intent intelligence, competi
  name: G2 MCP Server
  slug: g2-mcp-server
- description: The G2 Data Solutions API delivers enriched review data with flat attribute structures, intended for analytics and warehouse workflows rather than profile rendering. It returns reviews with B2B firmog
  name: G2 Data Solutions API
  slug: g2-data-solutions-api
artifact_total: 13
asyncapis:
- description: ''
  name: Business Software And Services Reviews G2 Webhooks
  slug: business-software-and-services-reviews-g2-webhooks
common:
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/business-software-and-services-reviews-g2-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/business-software-and-services-reviews-g2-authentication.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/business-software-and-services-reviews-g2-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/business-software-and-services-reviews-g2-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/g2dotcom
- group: company
  title: ''
  type: Website
  url: https://www.g2.com/
- group: start
  title: ''
  type: Portal
  url: https://documentation.g2.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.g2.com/static/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.g2.com/docs/integrations
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/business-software-and-services-reviews-g2-v2-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/business-software-and-services-reviews-g2-data-solutions-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/business-software-and-services-reviews-g2-chatgpt-plugin-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/business-software-and-services-reviews-g2-v2-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/business-software-and-services-reviews-g2-data-solutions-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/business-software-and-services-reviews-g2-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/business-software-and-services-reviews-g2-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/business-software-and-services-reviews-g2-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/business-software-and-services-reviews-g2-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/business-software-and-services-reviews-g2-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/business-software-and-services-reviews-g2-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/business-software-and-services-reviews-g2-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.g2.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/business-software-and-services-reviews-g2-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/business-software-and-services-reviews-g2-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/business-software-and-services-reviews-g2-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/business-software-and-services-reviews-g2-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/business-software-and-services-reviews-g2-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/business-software-and-services-reviews-g2-packages.yml
- group: design
  title: ''
  type: Components
  url: components/business-software-and-services-reviews-g2-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/business-software-and-services-reviews-g2-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/business-software-and-services-reviews-g2-plans-pricing.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://my.g2.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://data.g2.com/api/v2/docs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.g2.com/docs/developer-portal
- group: operate
  title: ''
  type: Support
  url: https://support.g2.com/
- group: company
  title: ''
  type: Blog
  url: https://learn.g2.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/g2crowd
- group: start
  title: ''
  type: SignUp
  url: https://my.g2.com/developers
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.g2.com/static/terms
created: '2025-07-11'
description: G2 is the world's largest and most trusted software marketplace. More than 90 million people annually use G2 to make smarter software decisions based on authentic peer reviews. Find the right software and services based on real user reviews.
finops:
- name: Business Software And Services Reviews G2 Finops
  service_category: API
  slug: business-software-and-services-reviews-g2-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/business-software-and-services-reviews-g2.png
layout: provider
mcp_servers:
- description: ''
  name: business-software-and-services-reviews-g2-mcp.yml
  slug: business-software-and-services-reviews-g2-mcpyml
modified: '2026-08-14'
name: Business Software and Services Reviews | G2
nav: Providers
network: true
overview: 'Business Software and Services Reviews | G2 publishes 3 APIs on the [APIs.io](https://apis.io/) network: G2 API V2, G2 Buyer Intent Data API, and G2 Data Solutions API. Tagged areas include B2B, SaaS, Software Reviews, Buyer Intent, and Competitive Intelligence.


  The Business Software and Services Reviews | G2 catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Business Software and Services Reviews | G2''s developer surface includes authentication, developer portal, documentation, changelog, sandbox, API reference, getting-started guide, and 33 more developer resources.'
plans:
- name: Business Software And Services Reviews G2 Plans Pricing
  plan_count: 0
  slug: business-software-and-services-reviews-g2-plans-pricing
random_paper: 54
rate_limits:
- limit_count: 1
  name: Business Software And Services Reviews G2 Rate Limits
  slug: business-software-and-services-reviews-g2-rate-limits
scopes:
- name: Business Software And Services Reviews G2 Scopes
  scope_count: 16
  slug: business-software-and-services-reviews-g2-scopes
  summary_line: 16 scopes · authorizationCode
score:
  band: strong
  composite: 60.1
  delta: 32.2
  facets:
    commercial_clarity: 57.9
    contract_quality: 70.0
    developer_ergonomics: 73.9
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 34.2
  previous_composite: 27.9
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/business-software-and-services-reviews-g2/refs/heads/main/screenshots/business-software-and-services-reviews-g2-2026-06-20T173819.png
security:
- kind: authentication
  name: Business Software And Services Reviews G2 Authentication
  slug: business-software-and-services-reviews-g2-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Business Software And Services Reviews G2 Domain Security
  slug: business-software-and-services-reviews-g2-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Business Software And Services Reviews G2 Trust Center
  slug: business-software-and-services-reviews-g2-trust-center
  summary_line: SOC 2, GDPR, CSA STAR
slug: business-software-and-services-reviews-g2
tags:
- B2B
- SaaS
- Software Reviews
- Buyer Intent
- Competitive Intelligence
- Market Intelligence
- Marketplace
- MCP
website: https://www.g2.com/
---
