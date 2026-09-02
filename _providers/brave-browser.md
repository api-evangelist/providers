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
  name: Brave Browser Agentic Access
  operation_count: 9
  slug: brave-browser-agentic-access
  summary_line: 9 operations
api_count: 1
apis:
- description: Privacy-first Chromium-based browser for Windows, macOS, Linux, Android, and iOS, with built-in tracker and ad blocking (Brave Shields), HTTPS upgrades, Global Privacy Control, and a Tor-enabled priva
  name: Brave Browser
  slug: browser
- description: Independent privacy-respecting web search engine backed by Brave's own index. Surfaces the consumer product at search.brave.com and powers the Brave Search API.
  name: Brave Search
  slug: search
- description: REST endpoint for general web search results with country, language, safe-search, and freshness filtering. Authenticated via X-Subscription-Token header.
  name: Brave Search API - Web Search
  slug: search-api-web
- description: Image search endpoint returning images with metadata, thumbnails, and SafeSearch filtering.
  name: Brave Search API - Image Search
  slug: search-api-images
- description: Video search endpoint returning videos with thumbnails, duration, and source metadata.
  name: Brave Search API - Video Search
  slug: search-api-videos
- description: Real-time news search endpoint returning articles from trusted sources with freshness filtering.
  name: Brave Search API - News Search
  slug: search-api-news
- description: Autosuggest endpoint that returns query completions for a partial input.
  name: Brave Search API - Suggest
  slug: search-api-suggest
- description: Spelling correction endpoint for refining noisy or misspelled user queries.
  name: Brave Search API - Spellcheck
  slug: search-api-spellcheck
- description: AI summarizer endpoint that condenses search results into a generated summary for use in agentic and AI-grounded applications.
  name: Brave Search API - Summarizer
  slug: search-api-summarizer
- description: Local search endpoint returning point-of-interest details given IDs surfaced by web search results.
  name: Brave Search API - Local POIs
  slug: search-api-local-pois
- description: AI-generated descriptions for local points of interest, complementing the Local POIs endpoint.
  name: Brave Search API - Local Descriptions
  slug: search-api-local-descriptions
- description: Model Context Protocol server wrapping the Brave Search API so AI agents can ground answers in real-time web results.
  name: Brave Search MCP Server
  slug: search-mcp
- description: In-browser AI assistant offering chat, summarization, translation, and content generation grounded in the page or tab the user is viewing. Surfaced inside the browser; not a public REST API.
  name: Brave Leo AI
  slug: leo
- description: End-to-end encrypted video conferencing product, available free with premium tier for larger meetings.
  name: Brave Talk
  slug: talk
- description: Opt-in attention rewards program paying users in Basic Attention Token (BAT) for viewing privacy-preserving ads, and enabling tipping of verified creators.
  name: Brave Rewards
  slug: rewards
- description: Privacy-respecting advertising platform for advertisers that targets anonymized cohorts inside the Brave browser and on Brave Search.
  name: Brave Ads
  slug: ads
- description: Native multi-chain crypto wallet built into the Brave browser. Supports EVM and Solana networks; integrates with WalletConnect and dApps.
  name: Brave Wallet
  slug: wallet
- description: The Images API from Brave — 1 operation(s) for images.
  name: Brave Images API
  slug: brave-browser-images-api
- description: The Local API from Brave — 2 operation(s) for local.
  name: Brave Local API
  slug: brave-browser-local-api
- description: The News API from Brave — 1 operation(s) for news.
  name: Brave News API
  slug: brave-browser-news-api
- description: The Spellcheck API from Brave — 1 operation(s) for spellcheck.
  name: Brave Spellcheck API
  slug: brave-browser-spellcheck-api
- description: The Suggest API from Brave — 1 operation(s) for suggest.
  name: Brave Suggest API
  slug: brave-browser-suggest-api
- description: The Summarizer API from Brave — 1 operation(s) for summarizer.
  name: Brave Summarizer API
  slug: brave-browser-summarizer-api
- description: The Videos API from Brave — 1 operation(s) for videos.
  name: Brave Videos API
  slug: brave-browser-videos-api
- description: The Web API from Brave — 1 operation(s) for web.
  name: Brave Web API
  slug: brave-browser-web-api
- description: Privacy-preserving news feed integrated into the browser's new tab page, sourced from a curated set of publisher feeds.
  name: Brave News
  slug: news
artifact_total: 43
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Brave Search Images API
  slug: open-brave-browser-images-api
- collection_type: open
  name: Brave Search Images Local API
  slug: open-brave-browser-local-api
- collection_type: open
  name: Brave Search Images News API
  slug: open-brave-browser-news-api
- collection_type: open
  name: Brave Search Images Spellcheck API
  slug: open-brave-browser-spellcheck-api
- collection_type: open
  name: Brave Search Images Suggest API
  slug: open-brave-browser-suggest-api
- collection_type: open
  name: Brave Search Images Summarizer API
  slug: open-brave-browser-summarizer-api
- collection_type: open
  name: Brave Search Images Videos API
  slug: open-brave-browser-videos-api
- collection_type: open
  name: Brave Search Images Web API
  slug: open-brave-browser-web-api
- collection_type: open
  name: Brave Search API
  slug: open-brave-browser
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/brave/brave-browser/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/brave/brave-browser/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/brave/brave-browser/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brave-browser-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brave-browser-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brave-browser-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brave-browser-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://brave.com/
- group: other
  title: ''
  type: Search
  url: https://search.brave.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-dashboard.search.brave.com/app/documentation
- group: build
  title: ''
  type: GitHub
  url: https://github.com/brave
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brave-software-
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/brave
- group: company
  title: ''
  type: Blog
  url: https://brave.com/blog/index.xml
created: '2026-05-23'
description: Brave Software builds a privacy-first Chromium-based browser, an independent search engine (Brave Search), an in-browser AI assistant (Leo), a video conferencing product (Brave Talk), an opt-in attention economy (Brave Rewards / Basic Attention Token), a wallet (Brave Wallet), and a privacy advertising platform (Brave Ads). Developer-facing APIs are concentrated in the Brave Search API (api.search.brave.com), which exposes web, news, image, video, suggest, spellcheck, summarizer, and local POI endpoints authenticated via X-Subscription-Token. Browser code is open source under MPL-2.0 on GitHub.
finops:
- name: Brave Browser Finops
  service_category: API
  slug: brave-browser-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brave-browser.png
layout: provider
modified: '2026-07-25'
name: Brave
nav: Providers
network: true
overview: 'Brave publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Images API, Local API, News API, and 5 more. Tagged areas include Browser, Search, Privacy, Chromium, and Web3.


  Brave''s developer surface includes authentication, documentation, GitHub presence, engineering blog, and 10 more developer resources.'
plans:
- name: Brave Browser Plans Pricing
  plan_count: 1
  slug: brave-browser-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Brave Browser Rate Limits
  slug: brave-browser-rate-limits
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 10
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 51.9
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  open_source:
    applies: true
    score: 25.0
  previous_composite: 34.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brave-browser/refs/heads/main/screenshots/brave-browser-2026-06-20T173637.png
security:
- kind: authentication
  name: Brave Browser Authentication
  slug: brave-browser-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Brave Browser Domain Security
  slug: brave-browser-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Brave Browser Vulnerability Disclosure
  slug: brave-browser-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: brave-browser
tags:
- Browser
- Search
- Privacy
- Chromium
- Web3
- Artificial Intelligence
- Advertising
website: https://brave.com/
---
