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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Back Market Agentic Access
  operation_count: 39
  slug: back-market-agentic-access
  summary_line: 39 operations · 14 acting
api_count: 9
apis:
- description: The Backbox API from Back Market — 2 operation(s) for backbox.
  name: Back Market Backbox API
  slug: back-market-backbox-api
- description: The Backship API from Back Market — 4 operation(s) for backship.
  name: Back Market Backship API
  slug: back-market-backship-api
- description: The BuyBack API from Back Market — 12 operation(s) for buyback.
  name: Back Market Buy Back API
  slug: back-market-buyback-api
- description: The Care API from Back Market — 6 operation(s) for care.
  name: Back Market Care API
  slug: back-market-care-api
- description: The Categories API from Back Market — 2 operation(s) for categories.
  name: Back Market Categories API
  slug: back-market-categories-api
- description: The Listings API from Back Market — 3 operation(s) for listings.
  name: Back Market Listings API
  slug: back-market-listings-api
- description: The Orderline API from Back Market — 1 operation(s) for orderline.
  name: Back Market Orderline API
  slug: back-market-orderline-api
- description: The Orders API from Back Market — 3 operation(s) for orders.
  name: Back Market Orders API
  slug: back-market-orders-api
- description: The TaskManager API from Back Market — 1 operation(s) for taskmanager.
  name: Back Market Task Manager API
  slug: back-market-taskmanager-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Back Market - API Guidelines Backbox API
  slug: open-back-market-backbox-api
- collection_type: open
  name: Back Market - API Guidelines Backship API
  slug: open-back-market-backship-api
- collection_type: open
  name: Back Market - API Guidelines Buy Back API
  slug: open-back-market-buyback-api
- collection_type: open
  name: Back Market - API Guidelines Care API
  slug: open-back-market-care-api
- collection_type: open
  name: Back Market - API Guidelines Categories API
  slug: open-back-market-categories-api
- collection_type: open
  name: Back Market - API Guidelines Listings API
  slug: open-back-market-listings-api
- collection_type: open
  name: Back Market - API Guidelines Orderline API
  slug: open-back-market-orderline-api
- collection_type: open
  name: Back Market - API Guidelines Orders API
  slug: open-back-market-orders-api
- collection_type: open
  name: Back Market - API Guidelines Task Manager API
  slug: open-back-market-taskmanager-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.backmarket.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.backmarket.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://api.backmarket.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://api.backmarket.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.backmarket.dev/#getting-started
- group: operate
  title: ''
  type: Support
  url: https://merchant-support.backmarket.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.backmarket.com/en-us/help
- group: company
  title: ''
  type: Blog
  url: https://www.backmarket.com/en-us/c
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BackMarket
- group: start
  title: ''
  type: SignUp
  url: https://www.backmarket.com/en-us/seller/home
- group: start
  title: ''
  type: Login
  url: https://www.backmarket.com/bo-seller
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.backmarket.com/en-us/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.backmarket.com/en-us/legal/data-protection
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/back-market-openapi-original.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/back-market-authentication.yml
- group: auth
  title: ''
  type: Security
  url: https://www.backmarket.com/.well-known/security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/back-market-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/back-market-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/back-market-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/back-market-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/back-market-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/back-market-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/back-market-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/back-market-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/back-market-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/back-market-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/back-market-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/back-market-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/back-market-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/back-market-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/back-market-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/back-market-api-overlay.yaml
- group: design
  title: ''
  type: Rules
  url: rules/back-market-rules.yml
created: '2026-08-02'
description: Back Market is a French-founded global online marketplace dedicated exclusively to refurbished consumer electronics — smartphones, laptops, tablets, consoles, watches, audio and home appliances — operating across 17 countries on three regional platforms (EU via backmarket.fr, North America via backmarket.com, Asia-Pacific via backmarket.co.jp). For the ~1,800 professional refurbishers selling on the platform, Back Market publishes a seller-facing REST API (the "Back Market API Guidelines") covering the marketplace taxonomy, product and listing management, order and orderline workflows, BuyBack (trade-in) orders and listings, Backship deliveries and returns, the Care after-sales platform (claims, messages, refunds, item transfers), and Backbox competitive pricing data. The API is documented as an OpenAPI 3.0.3 contract rendered with Stoplight Elements at api.backmarket.dev, authenticated with a Basic token issued from the seller Back Office, and mirrored by preprod environments
  on every regional platform.
image: https://api.backmarket.dev/statics/backmarket-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: back-market-mcp.yml
  slug: back-market-mcpyml
modified: '2026-08-02'
name: Back Market
nav: Providers
network: true
overview: 'Back Market publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Backbox API, Backship API, Buy Back API, and 6 more. Tagged areas include Company, E-Commerce, Marketplace, Retail, and Refurbished Electronics.


  The Back Market catalog on APIs.io includes 1 Spectral governance ruleset.


  Back Market''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 27 more developer resources.'
random_paper: 47
rate_limits:
- limit_count: 13
  name: Back Market Rate Limits
  slug: back-market-rate-limits
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Back Market API Rules
  rule_count: 12
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 4
  slug: back-market-rules
score:
  band: strong
  composite: 57.2
  delta: 3.3
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 62.1
    contract_quality: 58.5
    developer_ergonomics: 66.1
    discoverability: 92.6
    governance: 62.1
    operational_transparency: 44.7
  previous_composite: 53.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/back-market/refs/heads/main/screenshots/back-market-2026-08-07T162100.png
security:
- kind: authentication
  name: Back Market Authentication
  slug: back-market-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Back Market Domain Security
  slug: back-market-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Back Market Vulnerability Disclosure
  slug: back-market-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: back-market
tags:
- Company
- E-Commerce
- Marketplace
- Retail
- Refurbished Electronics
- Circular Economy
- Orders
- Listings
- Product Catalog
- Logistics
- Customer Support
website: https://www.backmarket.com/
---
