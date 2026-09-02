---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.1
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Kudobuzz Developer API lets merchants and integration developers create customer reviews and sync customers and orders into the After Purchase Mail (APM) product for segmentation and post-purchase
  name: Kudobuzz Developer API
  slug: kudobuzz-developer-api
artifact_total: 8
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/kudobuzz/kbjs-clients/issues
- group: company
  title: ''
  type: Website
  url: https://kudobuzz.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kudobuzz.com/developer-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kudobuzz.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.kudobuzz.com/#/core
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.kudobuzz.com/#/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/kudobuzz-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kudobuzz-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kudobuzz-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/kudobuzz-error-codes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kudobuzz-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kudobuzz-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kudobuzz-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/kudobuzz-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/kudobuzz-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/kudobuzz-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kudobuzz-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/kudobuzz-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kudobuzz-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kudobuzz-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://kudobuzz.com/gdpr
- group: auth
  title: ''
  type: TrustCenter
  url: security/kudobuzz-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kudobuzz-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kudobuzz-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kudobuzz-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/kudobuzz-components.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kudobuzz
- group: operate
  title: ''
  type: Support
  url: https://support.kudobuzz.com/en/
- group: company
  title: ''
  type: Blog
  url: https://blog.kudobuzz.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.kudobuzz.com/rss/
- group: commercial
  title: ''
  type: Pricing
  url: https://kudobuzz.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.kudobuzz.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.kudobuzz.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kudobuzz.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kudobuzz.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://kudobuzz.com/security
- group: docs
  title: ''
  type: DesignGuide
  url: https://github.com/kudobuzz/api-standards
- group: company
  title: ''
  type: Twitter
  url: https://x.com/kudobuzz
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kudobuzz
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UC3RyY_cyWlEBgIjsDE0-8fg
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/kudobuzz/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/kudobuzz/
created: '2026-07-17'
description: Kudobuzz is a reviews, user-generated content (UGC) and conversion-rate-optimization platform for ecommerce merchants. It collects, moderates and displays product and social reviews, imports reviews from Facebook, Google, Yelp, Amazon, Etsy and AliExpress, syncs shoppable UGC video from social channels, and runs After Purchase Mail campaigns that time review requests to a buyer's order. Merchants install it as an app on Shopify, Wix, BigCommerce, Shoplazza and Webflow and embed site, product, full-page and checkout widgets in their storefronts. The gated Developer API (api.kudobuzz.com/v1) exposes review creation plus customer and order sync for the APM product, is available to merchants on the Buffet plan and free to app developers building integrations, and is served by a first-party JavaScript client wrapper. Kudobuzz publishes its REST design standard, covering URLs, status codes, the error envelope, versioning, cursor pagination, rate-limit headers and idempotency, as a
  public repository.
image: https://kudobuzz.com/assets/kudobuzz-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Kudobuzz MCP Server
  slug: kudobuzz-mcp-server
modified: '2026-08-13'
name: Kudobuzz
nav: Providers
network: true
overview: 'Kudobuzz publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Reviews, User Generated Content, E-Commerce, and Social Proof.


  Kudobuzz''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 36 more developer resources.'
plans:
- name: Kudobuzz Plans Pricing
  plan_count: 0
  slug: kudobuzz-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Kudobuzz Rate Limits
  slug: kudobuzz-rate-limits
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 21.1
  open_source:
    applies: true
    score: 0.0
  previous_composite: 30.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kudobuzz/refs/heads/main/screenshots/kudobuzz-2026-07-25T224319.png
security:
- kind: authentication
  name: Kudobuzz Authentication
  slug: kudobuzz-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Kudobuzz Domain Security
  slug: kudobuzz-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Kudobuzz Vulnerability Disclosure
  slug: kudobuzz-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Kudobuzz Trust Center
  slug: kudobuzz-trust-center
  summary_line: trust center published
slug: kudobuzz
tags:
- Company
- Reviews
- User Generated Content
- E-Commerce
- Social Proof
- Conversion Rate Optimization
- Marketing
- Shopify
- Customer Feedback
- Software-as-a-Service
website: https://kudobuzz.com
---
