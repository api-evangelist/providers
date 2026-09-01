---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rakuten Agentic Access
  operation_count: 3
  slug: rakuten-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Keyword and parameter search across all Rakuten Ichiba marketplace items, returning item titles, prices, images, shop information, and ranking signals.
  name: Rakuten Ichiba Item Search API
  slug: ichiba-item-search
- description: Returns the hierarchical genre tree used to categorize items across Rakuten Ichiba, enabling category navigation and browse-based product discovery.
  name: Rakuten Ichiba Genre Search API
  slug: ichiba-genre-search
- description: Returns tags associated with a genre, supporting faceted navigation and refinement of Ichiba item browse.
  name: Rakuten Ichiba Tag Search API
  slug: ichiba-tag-search
- description: Returns top-ranked items across Rakuten Ichiba by genre, age, and gender, used for trend and bestseller displays.
  name: Rakuten Ichiba Ranking API
  slug: ichiba-item-ranking
- description: Price Navi (Product Search) returns aggregated product records with multi-shop price comparisons, ratings, and review metadata for Ichiba.
  name: Rakuten Item Price Navi API
  slug: ichiba-product-search
- description: Unified search across all Rakuten Books catalogs (books, CDs, DVDs, games, software, magazines), returning normalized product records and Rakuten Books shop information.
  name: Rakuten Books Total Search API
  slug: books-total-search
- description: Search Rakuten Books for Japanese-language and translated books by title, author, ISBN, publisher, and other metadata.
  name: Rakuten Books Book Search API
  slug: books-book-search
- description: Search Rakuten Books CD catalog by title, artist, label, and release date.
  name: Rakuten Books CD Search API
  slug: books-cd-search
- description: Search Rakuten Books DVD and Blu-ray catalog including movies, TV, anime, and live performances.
  name: Rakuten Books DVD / Blu-ray Search API
  slug: books-dvd-search
- description: Search Rakuten Books foreign-language books catalog (mostly English-language).
  name: Rakuten Books Foreign Book Search API
  slug: books-foreign-search
- description: Search Rakuten Books magazine catalog by title, publisher, and issue date.
  name: Rakuten Books Magazine Search API
  slug: books-magazine-search
- description: Search Rakuten Books video game catalog across major consoles and platforms.
  name: Rakuten Books Game Search API
  slug: books-game-search
- description: Search Rakuten Books PC software catalog.
  name: Rakuten Books Software Search API
  slug: books-software-search
- description: Returns the genre tree for Rakuten Books, used for browse and navigation across the unified Books catalog.
  name: Rakuten Books Genre Search API
  slug: books-genre-search
- description: Search Rakuten Kobo's eBook catalog for digital reading content across Japanese and international titles.
  name: Rakuten Kobo eBook Search API
  slug: kobo-ebook-search
- description: Returns the Kobo eBook genre hierarchy for browse and filter.
  name: Rakuten Kobo Genre Search API
  slug: kobo-genre-search
- description: Lightweight keyword and area search over Rakuten Travel's Japanese hotel inventory, returning hotel name, location, and basic descriptors.
  name: Rakuten Travel Simple Hotel Search API
  slug: travel-simple-hotel-search
- description: Returns full hotel detail records including amenities, addresses, images, and access information for one or more Rakuten Travel hotels by hotel number.
  name: Rakuten Travel Hotel Detail Search API
  slug: travel-hotel-detail-search
- description: Searches for hotels with vacancy for given check-in and check-out dates, party composition, and budget filters.
  name: Rakuten Travel Vacant Hotel Search API
  slug: travel-vacant-hotel-search
- description: Returns Rakuten Travel's hierarchical Japanese area classification (prefecture / region / detail), used to scope hotel searches and build location filters.
  name: Rakuten Travel Area Class API
  slug: travel-get-area-class
- description: Full-text keyword search across Rakuten Travel hotel inventory, with filters for area, price, and rating.
  name: Rakuten Travel Keyword Hotel Search API
  slug: travel-keyword-hotel-search
- description: Returns the list of hotel chains available on Rakuten Travel, used to scope searches to a specific brand.
  name: Rakuten Travel Hotel Chain List API
  slug: travel-hotel-chain-list
- description: Returns top-ranked Rakuten Travel hotels by area and category for trend, bestseller, and recommendation displays.
  name: Rakuten Travel Hotel Ranking API
  slug: travel-hotel-ranking
- description: Returns the Rakuten Recipe category hierarchy (large, medium, small) used for browse navigation of user-submitted Japanese recipes.
  name: Rakuten Recipe Category List API
  slug: recipe-category-list
- description: Returns top-ranked recipes within a Rakuten Recipe category, with images, ingredients, and recipe URLs.
  name: Rakuten Recipe Category Ranking API
  slug: recipe-category-ranking
- description: Search Rakuten GORA Japanese golf courses by name, area, and facility attributes.
  name: Rakuten GORA Golf Course Search API
  slug: gora-golf-course-search
- description: Returns full golf course detail records on Rakuten GORA including holes, yardage, fees, access, and amenities.
  name: Rakuten GORA Golf Course Detail API
  slug: gora-golf-course-detail
- description: Search Rakuten GORA tee-time plans by course, date, party size, and budget — used to surface bookable golf rounds.
  name: Rakuten GORA Golf Plan Search API
  slug: gora-plan-search
- description: Rakuten Pay is Rakuten's e-money / QR payment service for Japan, integrated by merchants directly or via PSPs. The merchant API handles order creation, payment authorization, capture, refunds, and rec
  name: Rakuten Pay Merchant API
  slug: rakuten-pay
- description: RMS (Rakuten Merchant Server) is the operational API for Rakuten Ichiba sellers, covering item management, order management, shipping, inventory, and customer messaging. Access is restricted to approv
  name: Rakuten RMS (Merchant Server) API
  slug: rms
- description: The Ichibagt API from Rakuten — 1 operation(s) for ichibagt.
  name: Rakuten Ichibagt API
  slug: rakuten-ichibagt-api
- description: The Ichibams API from Rakuten — 1 operation(s) for ichibams.
  name: Rakuten Ichibams API
  slug: rakuten-ichibams-api
- description: The Ichibaranking API from Rakuten — 1 operation(s) for ichibaranking.
  name: Rakuten Ichibaranking API
  slug: rakuten-ichibaranking-api
artifact_total: 44
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Rakuten Web Services Ichibagt API
  slug: open-rakuten-ichibagt-api
- collection_type: open
  name: Rakuten Web Services Ichibagt Ichibams API
  slug: open-rakuten-ichibams-api
- collection_type: open
  name: Rakuten Web Services Ichibagt Ichibaranking API
  slug: open-rakuten-ichibaranking-api
- collection_type: open
  name: Rakuten Web Services API
  slug: open-rakuten
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rakuten-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rakuten-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rakuten-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://global.rakuten.com/corp/
- group: company
  title: ''
  type: ConsumerWebsite
  url: https://www.rakuten.co.jp/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://webservice.rakuten.co.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://webservice.rakuten.co.jp/documentation
- group: other
  title: ''
  type: APIList
  url: https://webservice.rakuten.co.jp/documentation
- group: start
  title: ''
  type: Signup
  url: https://webservice.rakuten.co.jp/app/create
- group: other
  title: ''
  type: RMS
  url: https://webservice.rms.rakuten.co.jp/
- group: other
  title: ''
  type: RakutenPay
  url: https://pay.rakuten.co.jp/business/
- group: company
  title: ''
  type: InvestorRelations
  url: https://global.rakuten.com/corp/investors/
- group: company
  title: ''
  type: News
  url: https://global.rakuten.com/corp/news/
- group: other
  title: ''
  type: Sustainability
  url: https://global.rakuten.com/corp/sustainability/
- group: company
  title: ''
  type: Careers
  url: https://global.rakuten.com/corp/careers/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/rakutentech
- group: company
  title: ''
  type: TechBlog
  url: https://engineering.rakuten.today/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rakuten/
created: '2026-05-23'
description: Rakuten Group is a Japan-headquartered internet conglomerate spanning e-commerce (Rakuten Ichiba), fintech (Rakuten Bank, Rakuten Card, Rakuten Securities), digital content (Rakuten Books, Kobo, Viki), travel (Rakuten Travel), telecom (Rakuten Mobile, Rakuten Symphony), and advertising (Rakuten Advertising). Rakuten exposes a long-standing public developer platform — Rakuten Web Services (webservice.rakuten.co.jp) — that offers REST/JSON APIs for searching Ichiba items and genres, books, CDs, DVDs, games, software, magazines, Kobo eBooks, Rakuten Travel hotels (simple, detail, vacant, keyword), Rakuten Recipe, and Rakuten GORA golf courses. All RWS APIs use a Rakuten application ID for authentication and are read-only. Rakuten separately operates merchant-facing RMS (Rakuten Merchant Server) APIs and Rakuten Pay merchant APIs, which are partner-gated.
finops:
- name: Rakuten Finops
  service_category: API
  slug: rakuten-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rakuten.png
layout: provider
modified: '2026-05-23'
name: Rakuten
nav: Providers
network: true
overview: 'Rakuten publishes 3 APIs on the [APIs.io](https://apis.io/) network: Ichibagt API, Ichibams API, and Ichibaranking API. Tagged areas include E-Commerce, Travel, Books, Recipes, and Golf.


  Rakuten''s developer surface includes authentication, documentation, signup flow, product news, GitHub presence, and 13 more developer resources.'
plans:
- name: Rakuten Plans Pricing
  plan_count: 1
  slug: rakuten-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Rakuten Rate Limits
  slug: rakuten-rate-limits
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 10
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 52.4
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rakuten/refs/heads/main/screenshots/rakuten-2026-06-20T192542.png
security:
- kind: authentication
  name: Rakuten Authentication
  slug: rakuten-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Rakuten Domain Security
  slug: rakuten-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rakuten
tags:
- E-Commerce
- Travel
- Books
- Recipes
- Golf
- Japan
- Fintech
- Telecom
- Rakuten Web Services
website: https://global.rakuten.com/corp/
---
