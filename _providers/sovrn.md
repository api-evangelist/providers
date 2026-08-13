---
access_model:
  confidence: medium
  label: Free with account
  onboarding: unknown
  pricing: free
  public: true
  source:
  - https://platform.sovrn.com/account/signup
  - https://developer.sovrn.com/docs/authorization
  - https://knowledge.sovrn.com/kb/api-onboarding-guide-for-commerce
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
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 49.1
  scored_at: '2026-08-12'
api_count: 10
apis:
- description: Check whether a destination URL can be monetized by Sovrn Commerce, get its estimated earnings per click, and receive the optimized affiliate URL to use in its place. Supports a geo override for affil
  name: Sovrn Commerce Link Check API
  slug: sovrn-commerce-link-check-api
- description: Real-time bid on a single click. Returns either a bid win (pricing model CPC or CPA, expected earnings per click net of revenue share, the Sovrn redirect URL and a millisecond expiry) or a no-fill, so
  name: Sovrn Commerce Bid Check API
  slug: sovrn-commerce-bid-check-api
- description: List the campaigns (sites) on a Sovrn Commerce account or search them by name or campaignId, returning each campaign's id, public API key, approval status, category, platform and application type. Sup
  name: Sovrn Commerce Campaigns API
  slug: sovrn-commerce-campaigns-api
- description: Eight endpoints returning affiliate commission performance in real time, each aggregating the same event set on a different dimension — individual transactions, merchants, merchants by date, links, pa
  name: Sovrn Commerce Real-Time Reports API
  slug: sovrn-commerce-real-time-reports-api
- description: Retrieve the merchants a Commerce account is approved to work with, including geo-specific commission rates, rate formats, average EPC and order value, preferred-status flags and per-merchant domains.
  name: Sovrn Commerce Merchant Group Summaries API
  slug: sovrn-commerce-merchant-group-summaries-api
- description: Returns products tailored to a piece of content. Callers pass their content plus optional filters such as price range or preferred merchants and receive a curated product list with sale and retail pri
  name: Sovrn Commerce Product Recommendation API
  slug: sovrn-commerce-product-recommendation-api
- description: Compare prices for the same product across merchants in a given market, ranked by match accuracy, returning merchant identity and logo, deep link, images, sale and retail price, discount rate, affilia
  name: Sovrn Commerce Price Comparisons (Product Affiliate) API
  slug: sovrn-commerce-price-comparisons-product-affiliate-api
- description: Retrieve ranked, product-specific promo codes with verification status — code, affiliated URL, original price, price with the code applied, currency, verified flag and timestamp — alongside merchant i
  name: Sovrn Commerce Product Promo Codes API
  slug: sovrn-commerce-product-promo-codes-api
- description: Custom reporting over Sovrn Ad Exchange performance across web, connected TV and mobile app inventory. Requires start, end, metrics, dimensions and granularity on every request, with hour, day and mon
  name: Sovrn Advertising Performance Reporting API
  slug: sovrn-advertising-performance-reporting-api
- description: Hosted, beta Model Context Protocol server exposing Sovrn Commerce affiliate data, campaigns and products to AI clients — twelve tools covering price search, link checking, product recommendations and
  name: Sovrn Commerce MCP Server
  slug: sovrn-commerce-mcp-server
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://www.sovrn.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.sovrn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sovrn.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.sovrn.com/reference/campaigns
- group: start
  title: ''
  type: GettingStarted
  url: https://knowledge.sovrn.com/kb/api-onboarding-guide-for-commerce
- group: company
  title: ''
  type: Blog
  url: https://www.sovrn.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://knowledge.sovrn.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sovrn
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sovrn.com/
- group: start
  title: ''
  type: SignUp
  url: https://platform.sovrn.com/account/signup
- group: start
  title: ''
  type: Login
  url: https://platform.sovrn.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.sovrn.com/trust-center/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sovrn.com/privacy-policy/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sovrn.com/legal/msa/
- group: auth
  title: ''
  type: Security
  url: https://www.sovrn.com/responsible-disclosure-policy/
- group: auth
  title: ''
  type: SecurityTxt
  url: https://www.sovrn.com/.well-known/security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sovrn-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sovrn-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sovrn-domain-security.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sovrn-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sovrn-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sovrn-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sovrn-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sovrn-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sovrn-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sovrn-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sovrn-plans-pricing.yml
- group: design
  title: ''
  type: Components
  url: components/sovrn-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sovrn-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developer.sovrn.com/llms.txt
created: '2026-07-17'
description: Sovrn is an advertising technology and content monetization company that helps online publishers, advertisers, and creators earn revenue from their websites and audiences. Its platform spans Ad Exchange (an omnichannel programmatic demand pipeline connecting publisher inventory to buyers and DSPs), Signal (ad-inventory and yield optimization), Commerce (affiliate and commerce-content monetization, formerly VigLink, with access to tens of thousands of merchants), and Data solutions for first-party data activation. Sovrn publishes a ReadMe-hosted developer center at developer.sovrn.com carrying eight OpenAPI definitions across seventeen operations — affiliate link checking, real-time bid pricing on clicks, campaign management, real-time commission reporting, merchant rate summaries, product recommendations, price comparisons, promo codes, and Ad Exchange performance reporting — plus a beta hosted Commerce MCP server at mcp.sovrn.com/commerce, an Agent Skills discovery document,
  and llms.txt files on three hosts. Sovrn is headquartered in Boulder, Colorado.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sovrn.png
layout: provider
mcp_servers:
- description: ''
  name: sovrn-mcp.yml
  slug: sovrn-mcpyml
- description: ''
  name: commerce
  slug: commerce
modified: '2026-08-12'
name: Sovrn
nav: Providers
network: true
overview: 'Sovrn publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Commerce Link Check API, Commerce Bid Check API, Commerce Campaigns API, and 6 more. Tagged areas include Company, Adtech, Advertising, Monetization, and Affiliate Marketing.


  Sovrn''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 24 more developer resources.'
plans:
- name: Sovrn Plans Pricing
  plan_count: 0
  slug: sovrn-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 5
  name: Sovrn Rate Limits
  slug: sovrn-rate-limits
score:
  band: developing
  composite: 53.3
  delta: 37.1
  facets:
    commercial_clarity: 42.1
    contract_quality: 52.6
    developer_ergonomics: 58.7
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 63.2
  previous_composite: 16.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: rising
security:
- kind: authentication
  name: Sovrn Authentication
  slug: sovrn-authentication
  summary_line: apiKey · 5 schemes
- kind: domain-security
  name: Sovrn Domain Security
  slug: sovrn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sovrn Vulnerability Disclosure
  slug: sovrn-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sovrn
tags:
- Company
- Adtech
- Advertising
- Monetization
- Affiliate Marketing
- Programmatic
- Publishers
- Commerce
- Data
- Reporting
- Product Data
- Agent Native
website: https://www.sovrn.com
---
