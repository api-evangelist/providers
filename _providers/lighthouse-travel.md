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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Lighthouse Travel Agentic Access
  operation_count: 14
  slug: lighthouse-travel-agentic-access
  summary_line: 14 operations
api_count: 8
apis:
- description: Market demand predictions per arrival date.
  name: Lighthouse Demand API
  slug: lighthouse-travel-demand-api
- description: List hotels, competitors, compsets, and subscribed features.
  name: Lighthouse Hotels API
  slug: lighthouse-travel-hotels-api
- description: Forward-looking demand and search-volume insights.
  name: Lighthouse Market Insight API
  slug: lighthouse-travel-market-insight-api
- description: List markets and linked subscriptions.
  name: Lighthouse Markets API
  slug: lighthouse-travel-markets-api
- description: Rate parity comparisons across OTAs.
  name: Lighthouse Parity API
  slug: lighthouse-travel-parity-api
- description: Hotel ranking positions across OTAs and ranking summaries.
  name: Lighthouse Ranking API
  slug: lighthouse-travel-ranking-api
- description: Current and historic lowest rates, rates per room type, and raw rates across OTAs.
  name: Lighthouse Rates API
  slug: lighthouse-travel-rates-api
- description: Aggregated review scores across OTAs.
  name: Lighthouse Reviews API
  slug: lighthouse-travel-reviews-api
artifact_total: 13
collections:
- collection_type: open
  name: Lighthouse Integration API
  slug: open-lighthouse-travel-integration-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lighthouse-travel-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lighthouse-travel-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lighthouse-travel-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lighthouse-travel-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.mylighthouse.com
- group: company
  title: ''
  type: About
  url: https://www.mylighthouse.com/company/about
- group: other
  title: ''
  type: Products
  url: https://www.mylighthouse.com/products
- group: commercial
  title: ''
  type: PricingManager
  url: https://www.mylighthouse.com/products/pricing-manager
- group: other
  title: ''
  type: RateInsight
  url: https://www.mylighthouse.com/products/rate-insight
- group: other
  title: ''
  type: MarketInsight
  url: https://www.mylighthouse.com/products/market-insight
- group: other
  title: ''
  type: BenchmarkInsight
  url: https://www.mylighthouse.com/products/benchmark-insight
- group: other
  title: ''
  type: BusinessIntelligence
  url: https://www.mylighthouse.com/products/business-intelligence
- group: other
  title: ''
  type: ParityInsight
  url: https://www.mylighthouse.com/products/parity-insight
- group: other
  title: ''
  type: ChannelManager
  url: https://www.mylighthouse.com/products/channel-manager
- group: other
  title: ''
  type: DataSolutions
  url: https://www.mylighthouse.com/data-services/hotel-data-solutions
- group: other
  title: ''
  type: DeveloperSolutions
  url: https://www.mylighthouse.com/resources/blog/developer-solutions-suite-new-integration-api
- group: other
  title: ''
  type: API
  url: https://api.mylighthouse.com/
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.mylighthouse.com/
- group: company
  title: ''
  type: Partnerships
  url: https://www.mylighthouse.com/company/partnerships
- group: other
  title: ''
  type: Customers
  url: https://www.mylighthouse.com/customers
- group: other
  title: ''
  type: Resources
  url: https://www.mylighthouse.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.mylighthouse.com/resources/blog
- group: other
  title: ''
  type: Insights
  url: https://www.mylighthouse.com/resources/insights
- group: other
  title: ''
  type: Events
  url: https://www.mylighthouse.com/resources/events
- group: other
  title: ''
  type: CustomerCare
  url: https://www.mylighthouse.com/company/customer-care
- group: auth
  title: ''
  type: Trust
  url: https://trust.mylighthouse.com
- group: company
  title: ''
  type: Careers
  url: https://www.mylighthouse.com/company/careers
- group: operate
  title: ''
  type: ContactSales
  url: https://www.mylighthouse.com/contact-sales
- group: start
  title: ''
  type: Login
  url: https://app.mylighthouse.com/login
- group: build
  title: ''
  type: GitHub
  url: https://github.com/OTA-Insight
- group: other
  title: ''
  type: DevTo
  url: https://dev.to/lighthouse-intelligence
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lighthouseintelligence/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@HotelRevenueManagement
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/lighthouse.intel/
created: '2026-05-25'
description: Lighthouse (formerly OTA Insight) is the commercial platform for the travel and hospitality industry, transforming data complexity into revenue growth for 80,000+ hotels across 185+ countries. Headquartered in London with offices across Europe, the Americas, and Asia-Pacific, Lighthouse combines market intelligence, business intelligence, and revenue management into a single SaaS suite. Core products include Rate Insight and Market Insight for competitive pricing and forward demand, Pricing Manager for automated revenue optimization, Benchmark Insight for Smart Compset competitive analysis, Business Intelligence for portfolio reporting, Parity Insight for distribution parity, Channel Manager for independent hotels, and newer AI products like KITT (AI receptionist) and Connect AI (ChatGPT direct-booking app). The platform processes 1.7 billion hotel rates per day across 300,000+ profiled competitor hotels. Lighthouse exposes a public, subscription-gated Integration API (api.mylighthouse.com,
  v3.1) for hotel customers and certified technology partners — covering Hotels, Markets, Rates, Demand, Ranking, Reviews, Parity, and Market Insight — and runs a partner program with 20+ named integrations including Mews, Infor, Duetto, Cendyn, Ideas, Atomize, SHR Group, and Cloudbeds. Revenue model is subscription SaaS sold by sales engagement; pricing is not published publicly.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lighthouse-travel.png
layout: provider
modified: '2026-05-25'
name: Lighthouse
nav: Providers
network: true
overview: 'Lighthouse publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Demand API, Hotels API, Market Insight API, and 5 more. Tagged areas include Hospitality, Hotels, Travel, Revenue Management, and Market Intelligence.


  Lighthouse''s developer surface includes authentication, engineering blog, GitHub presence, YouTube channel, and 30 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 28.9
  delta: -2.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 55.9
    developer_ergonomics: 13.0
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lighthouse-travel/refs/heads/main/screenshots/lighthouse-travel-2026-06-20T184520.png
security:
- kind: authentication
  name: Lighthouse Travel Authentication
  slug: lighthouse-travel-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Lighthouse Travel Domain Security
  slug: lighthouse-travel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lighthouse Travel Vulnerability Disclosure
  slug: lighthouse-travel-vulnerability-disclosure
  summary_line: disclosure policy published
slug: lighthouse-travel
tags:
- Hospitality
- Hotels
- Travel
- Revenue Management
- Market Intelligence
- Business Intelligence
- Pricing
- Rate Shopping
- Competitive Intelligence
- Distribution
- Parity
- Channel Manager
- Demand Forecasting
- SaaS
- AI
website: https://www.mylighthouse.com
---
