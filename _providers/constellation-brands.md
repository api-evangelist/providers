---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Constellation Brands Agentic Access
  operation_count: 10
  slug: constellation-brands-agentic-access
  summary_line: 10 operations
api_count: 13
apis:
- description: Returns promotional bottle-shot imagery for Constellation Brands products in multiple formats (PNG, JPG) and resolutions for use on partner sites, e-commerce experiences, and printed materials.
  name: Bottle Shots API
  slug: bottle-shots
- description: Retrieves tasting-note documents for wine and spirits brands so partners can render or print structured tasting copy alongside bottle shots and pricing.
  name: Tasting Notes API
  slug: tasting-notes
- description: Delivers "hot sheets" containing critical-review scores, awards, and promotional copy that distributors use to merchandise Constellation brands at retail.
  name: Hot Sheets API
  slug: hot-sheets
- description: Provides point-of-sale shelf-talker artwork keyed to specific products and promotional periods.
  name: Shelf Talkers API
  slug: shelf-talkers
- description: Returns neck-hanger artwork that distributors and retailers attach to bottles for in-store merchandising and promotions.
  name: Neck Hangers API
  slug: neck-hangers
- description: Supplies cocktail and beverage recipes featuring Constellation brands so on-premise partners and digital experiences can surface branded drink ideas.
  name: Recipes API
  slug: recipes
- description: The BottleShots API from Constellation Brands — 2 operation(s) for bottleshots.
  name: Constellation Brands BottleShots API
  slug: constellation-brands-bottleshots-api
- description: The HotSheets API from Constellation Brands — 1 operation(s) for hotsheets.
  name: Constellation Brands HotSheets API
  slug: constellation-brands-hotsheets-api
- description: The Items API from Constellation Brands — 3 operation(s) for items.
  name: Constellation Brands Items API
  slug: constellation-brands-items-api
- description: The NeckHangers API from Constellation Brands — 1 operation(s) for neckhangers.
  name: Constellation Brands NeckHangers API
  slug: constellation-brands-neckhangers-api
- description: The Recipes API from Constellation Brands — 1 operation(s) for recipes.
  name: Constellation Brands Recipes API
  slug: constellation-brands-recipes-api
- description: The ShelfTalkers API from Constellation Brands — 1 operation(s) for shelftalkers.
  name: Constellation Brands ShelfTalkers API
  slug: constellation-brands-shelftalkers-api
- description: The TastingNotes API from Constellation Brands — 1 operation(s) for tastingnotes.
  name: Constellation Brands TastingNotes API
  slug: constellation-brands-tastingnotes-api
artifact_total: 20
collections:
- collection_type: open
  name: Constellation Brands Partner API
  slug: open-constellation-brands
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/constellation-brands-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/constellation-brands-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/constellation-brands-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/constellation-brands
- group: company
  title: ''
  type: Website
  url: https://www.cbrands.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.cbrands.com/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ConstellationBrands
- group: company
  title: ''
  type: Investor Relations
  url: https://ir.cbrands.com/
- group: company
  title: ''
  type: Careers
  url: https://careers.cbrands.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cbrands.com/privacy-notice
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cbrands.com/terms-of-use
created: '2026-03-21'
description: Constellation Brands is a Fortune 500 producer and marketer of beer, wine, and spirits brands such as Corona, Modelo, Robert Mondavi, and Casa Noble. Constellation publishes a partner-oriented API catalog at dev.cbrands.com that exposes product, brand, and digital-asset data (bottle shots, tasting notes, hot sheets, shelf talkers, neck hangers, recipes, and an items product API) to distributors, retailers, and on-premise partners. Most endpoints require an API key issued through the developer registration process.
finops:
- name: Constellation Brands Finops
  service_category: Beverages / Product Data API
  slug: constellation-brands-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/constellation-brands.png
layout: provider
modified: '2026-05-19'
name: Constellation Brands
nav: Providers
network: true
overview: 'Constellation Brands publishes 7 APIs on the [APIs.io](https://apis.io/) network, including BottleShots API, HotSheets API, Items API, and 4 more. Tagged areas include Alcohol, Beer, Beverages, Digital Assets, and Fortune 500.


  Constellation Brands'' developer surface includes authentication and 10 more developer resources.'
plans:
- name: Constellation Brands Plans Pricing
  plan_count: 1
  slug: constellation-brands-plans-pricing
press:
- date: '2026-05-25'
  title: 'Constellation Brands (NYSE: STZ) shifts mix as beer gains ...'
  url: https://www.stocktitan.net/sec-filings/STZ/8-k-constellation-brands-inc-reports-material-event-b16203aed940.html
- date: '2026-05-25'
  title: 8-K - 04/09/2025
  url: https://ir.cbrands.com/sec-filings/all-sec-filings/content/0000016918-25-000017/0000016918-25-000017.pdf
- date: '2026-05-25'
  title: Constellation Brands Updates Fiscal 2025 Outlook
  url: https://www.cbrands.com/blogs/press-releases/constellation-brands-updates-fiscal-2025-outlook
- date: '2026-05-25'
  title: 'Constellation Brands: Markets Drunk On AI Leave Alcohol ...'
  url: https://seekingalpha.com/article/4836848-constellation-brands-markets-drunk-on-ai-leave-alcohol-giant-at-pandemic-level-lows
- date: '2026-05-25'
  title: 'Constellation Brands: Leveraging Technology, Data, and ...'
  url: https://cdotimes.com/2024/07/01/constellation-brands-leveraging-technology-data-and-ai-for-excellence/
random_paper: 114
rate_limits:
- limit_count: 1
  name: Constellation Brands Rate Limits
  slug: constellation-brands-rate-limits
score:
  band: thin
  composite: 32.0
  delta: -5.7
  facets:
    commercial_clarity: 34.2
    contract_quality: 50.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/constellation-brands/refs/heads/main/screenshots/constellation-brands-2026-06-20T174911.png
security:
- kind: authentication
  name: Constellation Brands Authentication
  slug: constellation-brands-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Constellation Brands Domain Security
  slug: constellation-brands-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: constellation-brands
tags:
- Alcohol
- Beer
- Beverages
- Digital Assets
- Fortune 500
- Spirits
- Wine
website: https://www.cbrands.com/
---
