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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
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
  score: 8.5
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: GRIN's bi-directional REST API lets a brand's own software communicate with GRIN to synchronize creators, content, programs, and reporting data. Reference documentation is published on Stoplight at ap
  name: GRIN API
  slug: grin-api
- description: GRIN's hosted remote Model Context Protocol server for Gia, its AI agent for creator marketing. GRIN documents that "Gia connects to Claude, ChatGPT, and other assistants that support MCP", and the en
  name: GRIN Gia MCP Server
  slug: grin-gia-mcp-server
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/grin-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/grin-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/grin-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://grin.co/security/
- group: auth
  title: ''
  type: Compliance
  url: https://grin.co/security/
- group: company
  title: ''
  type: Website
  url: https://grin.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.grin.co/
- group: docs
  title: ''
  type: APIReference
  url: https://api.grin.co/
- group: docs
  title: ''
  type: Documentation
  url: https://help.grin.co
- group: operate
  title: ''
  type: Support
  url: https://help.grin.co
- group: operate
  title: ''
  type: Community
  url: https://community.grin.co/
- group: company
  title: ''
  type: Blog
  url: https://grin.co/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.grin.co/
- group: start
  title: ''
  type: SignUp
  url: https://grin.co/get-started/
- group: start
  title: ''
  type: Login
  url: https://app.grin.co/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://grin.co/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://grin.co/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://grin.co/pricing
- group: agent
  title: ''
  type: MCPServer
  url: mcp/grin-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/grin-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/grin-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/grin-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/grin-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/grin-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/grin-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/grin-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/grin-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/grin-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/grin-packages.yml
created: '2026-07-17'
description: GRIN is a creator management and influencer marketing platform for consumer and eCommerce brands, operating in the creator economy. Brands use GRIN to discover creators, manage relationships and content, run affiliate and ambassador programs, handle creator payments, track performance, and measure ROI at scale. The product line includes GRIN Classic, a manual creator and affiliate management platform, and Gia, an AI assistant that automates affiliate program management. GRIN exposes a bi-directional REST API (documented on Stoplight at api.grin.co) so a brand's own software can synchronize creators, content, and program data with GRIN, alongside native integrations for Shopify, Klaviyo, PayPal, Slack, and other commerce tools.
image: https://grin.co/wp-content/uploads/2022/11/2022_GRIN_Logo_Black_Transparent-Bkgnd-small.webp
layout: provider
mcp_servers:
- description: ''
  name: Grin MCP Server
  slug: grin-mcp-server
modified: '2026-08-13'
name: Grin
nav: Providers
network: true
overview: 'Grin publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Influencer Marketing, Creator Economy, Creator Management, and Affiliate Marketing.


  Grin''s developer surface includes API reference, documentation, support, engineering blog, signup flow, pricing, authentication, and 22 more developer resources.'
plans:
- name: Grin Plans Pricing
  plan_count: 5
  slug: grin-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Grin Rate Limits
  slug: grin-rate-limits
scopes:
- name: Grin Scopes
  scope_count: 14
  slug: grin-scopes
  summary_line: 14 scopes · authorizationCode/clientCredentials/deviceCode
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 40.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/grin/refs/heads/main/screenshots/grin-2026-07-25T220334.png
security:
- kind: authentication
  name: Grin Authentication
  slug: grin-authentication
  summary_line: openIdConnect/oauth2 · 2 schemes
- kind: domain-security
  name: Grin Domain Security
  slug: grin-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Grin Vulnerability Disclosure
  slug: grin-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Grin Trust Center
  slug: grin-trust-center
  summary_line: SOC 2, GDPR
slug: grin
tags:
- Company
- Influencer Marketing
- Creator Economy
- Creator Management
- Affiliate Marketing
- Marketing
- Social-Media
- E-Commerce
website: https://grin.co
---
