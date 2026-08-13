---
access_model:
  confidence: high
  label: Contract Only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.mikmak.com/pricing (404)
  - https://docs.mikmak.ai/reference/mikmak-headless-commerce-api
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
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.2
  scored_at: '2026-08-12'
api_count: 5
apis:
- description: 'The MikMak Headless Commerce API (v1) lets brands and their authorized agencies power commerce experiences on brand-owned websites and media ad units with MikMak''s retailer network: product lookup by '
  name: MikMak Headless Commerce API
  slug: mikmak-commerce
- description: MikMak Aura provides real-time intelligence, fueled by AI, to connect marketing spend across channels to actual sales performance at retailers.
  name: MikMak Aura
  slug: mikmak-aura
- description: 'The MikMak Insights API is a reporting API that pushes MikMak commerce intelligence — Purchase Intent, Attributable Sales, historical pricing intelligence and shoppable-recipe performance — into data '
  name: MikMak Insights API
  slug: mikmak-insights
- description: The MikMak Commerce MCP Server is a hosted Model Context Protocol surface in front of the Headless Commerce API (v1). It exposes three strictly-typed, read-only, non-destructive tools — search_product
  name: MikMak Commerce MCP Server
  slug: mikmak-commerce-mcp
- description: The MikMak where-to-buy tag is the client-side distribution of MikMak Commerce for brand-owned websites. A single async script loaded from wtb-tag.mikmak.ai renders buy-now buttons, in-page containers
  name: MikMak Commerce for Brand.com (WTB Tag)
  slug: mikmak-brand-com-tag
artifact_total: 14
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mikmak.ai/docs/developer-portal
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mikmak.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mikmak.ai/reference/mikmak-headless-commerce-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mikmak.ai/docs/quick-start-1
- group: operate
  title: ''
  type: Support
  url: https://docs.mikmak.ai/page/support
- group: operate
  title: ''
  type: Help Center
  url: https://help.mikmak.ai/hc
- group: company
  title: ''
  type: Blog
  url: https://www.mikmak.com/blog
- group: company
  title: ''
  type: Website
  url: https://www.mikmak.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mikmak-tv
- group: operate
  title: ''
  type: Contact
  url: https://www.mikmak.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mikmak.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mikmak.com/legal/privacypolicy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.mikmak.com/product-updates
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mikmak-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mikmak-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://docs.mikmak.ai/llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mikmak-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mikmak-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mikmak-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mikmak-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mikmak-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mikmak-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/mikmak-trust-center.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mikmak-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mikmak-domain-security.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mikmak-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mikmak-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/mikmak-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/mikmak-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mikmak-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Login
  url: https://platform.mikmak.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Swaven
- group: operate
  title: ''
  type: SLA
  url: https://www.mikmak.com/legal/sla
- group: other
  title: ''
  type: Subprocessors
  url: https://www.mikmak.com/legal/subprocessors
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mikmak-tool-crosswalk.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/mikmak-commerce-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/mikmak-insights-api-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/mikmak-commerce-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/mikmak-insights-api-openapi.yml
created: '2025-02-21'
description: MikMak is an eCommerce enablement and analytics platform for multichannel brands, converting shoppers across social media, retail media, brand-owned websites, search, CTV, display and QR codes. The platform pairs a Headless Commerce API — product lookup, retailer availability, offers, carts and experience configuration across a global retailer network — with the MikMak Insights reporting API that pushes purchase-intent and attributable-sales data into data lakes and BI tools, and a hosted Model Context Protocol server that exposes the same commerce surface to AI agents. MikMak acquired the French shoppable-media company Swaven in 2021, whose where-to-buy tag technology still powers the brand.com widget and whose name persists in the platform's asset hosts.
finops:
- name: Mikmak Finops
  service_category: API
  slug: mikmak-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mikmak.png
layout: provider
mcp_servers:
- description: ''
  name: mikmak-mcp.yml
  slug: mikmak-mcpyml
- description: ''
  name: v1
  slug: v1
modified: '2026-08-12'
name: MikMak
nav: Providers
network: true
overview: 'MikMak publishes 2 APIs on the [APIs.io](https://apis.io/) network: Headless Commerce API and Insights API. Tagged areas include Analytics, Commerce, eCommerce, Multichannel, and Retail Media.


  MikMak''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, authentication, and 33 more developer resources.'
plans:
- name: Mikmak Plans Pricing
  plan_count: 0
  slug: mikmak-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 3
  name: Mikmak Rate Limits
  slug: mikmak-rate-limits
scopes:
- name: Mikmak Scopes
  scope_count: 0
  slug: mikmak-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 52.2
  delta: 38.7
  facets:
    commercial_clarity: 57.9
    contract_quality: 54.8
    developer_ergonomics: 67.4
    discoverability: 72.2
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 13.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/mikmak/refs/heads/main/screenshots/mikmak-2026-06-20T185553.png
security:
- kind: authentication
  name: Mikmak Authentication
  slug: mikmak-authentication
  summary_line: apiKey/http/oauth2 · 5 schemes
- kind: domain-security
  name: Mikmak Domain Security
  slug: mikmak-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mikmak Trust Center
  slug: mikmak-trust-center
  summary_line: SOC 2, ISO 27001, GDPR, CSA STAR
slug: mikmak
tags:
- Analytics
- Commerce
- eCommerce
- Multichannel
- Retail Media
- Where to Buy
- Shoppable Media
- Product Availability
- MCP
- Agent Native
- Reporting
- CPG
website: https://www.mikmak.com
---
