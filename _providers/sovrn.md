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
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-09-05'
api_count: 26
apis:
- description: Hosted, beta Model Context Protocol server exposing Sovrn Commerce affiliate data, campaigns and products to AI clients — twelve tools covering price search, link checking, product recommendations and
  name: Sovrn Commerce MCP Server
  slug: sovrn-commerce-mcp-server
- baseURL: https://api.viglink.com/api
  baseurl_source: declared
  description: The Account API from Sovrn — 1 operation(s) for account.
  name: Sovrn Account API
  slug: sovrn-account-api
- baseURL: https://api.viglink.com/api
  baseurl_source: declared
  description: The Ai Orchestration API from Sovrn — 1 operation(s) for ai orchestration.
  name: Sovrn Ai Orchestration API
  slug: sovrn-ai-orchestration-api
- baseURL: https://api.viglink.com/api
  baseurl_source: declared
  description: The Bid API from Sovrn — 1 operation(s) for bid.
  name: Sovrn Bid API
  slug: sovrn-bid-api
- baseURL: https://api.viglink.com/api
  baseurl_source: declared
  description: The Link API from Sovrn — 1 operation(s) for link.
  name: Sovrn Link API
  slug: sovrn-link-api
- baseURL: https://api.viglink.com/api
  baseurl_source: declared
  description: The Merchant Group Summaries API from Sovrn — 2 operation(s) for merchant group summaries.
  name: Sovrn Merchant Group Summaries API
  slug: sovrn-merchant-group-summaries-api
- baseURL: https://api.viglink.com/api
  baseurl_source: declared
  description: The Product Coupons API from Sovrn — 1 operation(s) for product coupons.
  name: Sovrn Product Coupons API
  slug: sovrn-product-coupons-api
- baseURL: https://api.viglink.com/api
  baseurl_source: declared
  description: The reporting API from Sovrn — 1 operation(s) for reporting.
  name: Sovrn Reporting API
  slug: sovrn-reporting-api
- baseURL: https://api.viglink.com/api
  baseurl_source: declared
  description: The reports API from Sovrn — 8 operation(s) for reports.
  name: Sovrn Reports API
  slug: sovrn-reports-api
- baseURL: https://api.viglink.com/api
  baseurl_source: declared
  description: The Sites API from Sovrn — 1 operation(s) for sites.
  name: Sovrn Sites API
  slug: sovrn-sites-api
artifact_total: 26
collections:
- collection_type: open
  name: Sovrn Advertising Performance Reporting API
  slug: open-sovrn-advertising-reporting
- collection_type: open
  name: Sovrn Commerce Bid Check API
  slug: open-sovrn-commerce-bid-check
- collection_type: open
  name: Sovrn Commerce Campaigns API
  slug: open-sovrn-commerce-campaigns
- collection_type: open
  name: Sovrn Commerce Link Check API
  slug: open-sovrn-commerce-link-check
- collection_type: open
  name: Sovrn Commerce Real-Time Reports API
  slug: open-sovrn-commerce-reports
- collection_type: open
  name: Sovrn Commerce Merchant Group Summaries API
  slug: open-sovrn-merchant-summaries
- collection_type: open
  name: Sovrn Commerce Price Comparisons (Product Affiliate) API
  slug: open-sovrn-price-comparisons
- collection_type: open
  name: Sovrn Commerce Product Promo Codes API
  slug: open-sovrn-product-coupons
- collection_type: open
  name: Sovrn Commerce Product Recommendation API
  slug: open-sovrn-product-recommendations
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/sovrn-commerce-link-check-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sovrn-commerce-bid-check-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sovrn-commerce-campaigns-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sovrn-commerce-reports-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sovrn-merchant-summaries-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sovrn-product-recommendations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sovrn-price-comparisons-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sovrn-product-coupons-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sovrn-advertising-reporting-overlay.yaml
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
  name: Commerce MCP Server
  slug: commerce-mcp-server
- description: ''
  name: Sovrn MCP Server
  slug: sovrn-mcp-server
modified: '2026-08-12'
name: Sovrn
nav: Providers
network: true
overview: 'Sovrn publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Account API, Ai Orchestration API, Bid API, and 6 more. Tagged areas include Company, AdTech, Advertising, Monetization, and Affiliate Marketing.


  Sovrn''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 33 more developer resources.'
plans:
- name: Sovrn Plans Pricing
  plan_count: 0
  slug: sovrn-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Sovrn Rate Limits
  slug: sovrn-rate-limits
score:
  band: developing
  composite: 49.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 4.5
    contract_quality: 56.0
    developer_ergonomics: 54.2
    discoverability: 92.6
    governance: 4.5
    operational_transparency: 52.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 48.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sovrn/refs/heads/main/screenshots/sovrn-2026-08-17T082014.png
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
- AdTech
- Advertising
- Monetization
- Affiliate Marketing
- Programmatic
- Publishers
- Commerce
- Data
- Reporting
- Product Data
- agent-native
website: https://www.sovrn.com
---
