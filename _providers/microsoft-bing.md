---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Microsoft Bing Agentic Access
  operation_count: 10
  slug: microsoft-bing-agentic-access
  summary_line: 10 operations · 1 acting
api_count: 18
apis:
- description: The Bing Image Search API enables developers to search for images across the web with advanced filtering options.
  name: Bing Image Search API
  slug: image-search
- description: The Bing Video Search API allows developers to search for videos across the web and retrieve video metadata.
  name: Bing Video Search API
  slug: video-search
- description: The Bing News Search API returns relevant news articles from across the web for a given query.
  name: Bing News Search API
  slug: news-search
- description: The Bing Entity Search API returns structured information about people, places, organizations, and other entities.
  name: Bing Entity Search API
  slug: entity-search
- description: The Bing Autosuggest API provides intelligent search query suggestions as users type.
  name: Bing Autosuggest API
  slug: autosuggest
- description: The Bing Spell Check API provides contextual spell checking using machine learning models.
  name: Bing Spell Check API
  slug: spell-check
- description: The Bing Visual Search API enables image-based search by analyzing uploaded images or image URLs.
  name: Bing Visual Search API
  slug: visual-search
- description: The Bing Custom Search API allows developers to create tailored search experiences by defining a custom view of the web.
  name: Bing Custom Search API
  slug: custom-search
- description: The Bing Local Business Search API returns information about local businesses based on search queries and location.
  name: Bing Local Business Search API
  slug: local-business-search
- baseURL: https://api.bing.microsoft.com/
  baseurl_source: declared
  description: The Autosuggest API from Microsoft Bing — 1 operation(s) for autosuggest.
  name: Microsoft Bing Autosuggest API
  slug: microsoft-bing-autosuggest-api
- baseURL: https://api.bing.microsoft.com/
  baseurl_source: declared
  description: The Custom Search API from Microsoft Bing — 1 operation(s) for custom search.
  name: Microsoft Bing Custom Search API
  slug: microsoft-bing-custom-search-api
- baseURL: https://api.bing.microsoft.com/
  baseurl_source: declared
  description: The Entity Search API from Microsoft Bing — 1 operation(s) for entity search.
  name: Microsoft Bing Entity Search API
  slug: microsoft-bing-entity-search-api
- baseURL: https://api.bing.microsoft.com/
  baseurl_source: declared
  description: The Image Search API from Microsoft Bing — 1 operation(s) for image search.
  name: Microsoft Bing Image Search API
  slug: microsoft-bing-image-search-api
- baseURL: https://api.bing.microsoft.com/
  baseurl_source: declared
  description: The News Search API from Microsoft Bing — 2 operation(s) for news search.
  name: Microsoft Bing News Search API
  slug: microsoft-bing-news-search-api
- baseURL: https://api.bing.microsoft.com/
  baseurl_source: declared
  description: The Spell Check API from Microsoft Bing — 1 operation(s) for spell check.
  name: Microsoft Bing Spell Check API
  slug: microsoft-bing-spell-check-api
- baseURL: https://api.bing.microsoft.com/
  baseurl_source: declared
  description: The Video Search API from Microsoft Bing — 1 operation(s) for video search.
  name: Microsoft Bing Video Search API
  slug: microsoft-bing-video-search-api
- baseURL: https://api.bing.microsoft.com/
  baseurl_source: declared
  description: The Visual search API from Microsoft Bing — 1 operation(s) for visual search.
  name: Microsoft Bing Visual search API
  slug: microsoft-bing-visual-search-api
- baseURL: https://api.bing.microsoft.com/
  baseurl_source: declared
  description: The Web Search API from Microsoft Bing — 1 operation(s) for web search.
  name: Microsoft Bing Web Search API
  slug: microsoft-bing-web-search-api
artifact_total: 35
collections:
- collection_type: open
  name: Bing Search APIs Autosuggest API
  slug: open-microsoft-bing-autosuggest-api
- collection_type: open
  name: Bing Search APIs Autosuggest CustomSearch API
  slug: open-microsoft-bing-customsearch-api
- collection_type: open
  name: Bing Search APIs Autosuggest EntitySearch API
  slug: open-microsoft-bing-entitysearch-api
- collection_type: open
  name: Bing Search APIs Autosuggest ImageSearch API
  slug: open-microsoft-bing-imagesearch-api
- collection_type: open
  name: Bing Search APIs Autosuggest NewsSearch API
  slug: open-microsoft-bing-newssearch-api
- collection_type: open
  name: Bing Search APIs Autosuggest SpellCheck API
  slug: open-microsoft-bing-spellcheck-api
- collection_type: open
  name: Bing Search APIs Autosuggest VideoSearch API
  slug: open-microsoft-bing-videosearch-api
- collection_type: open
  name: Bing Search APIs Autosuggest VisualSearch API
  slug: open-microsoft-bing-visualsearch-api
- collection_type: open
  name: Bing Search APIs Autosuggest WebSearch API
  slug: open-microsoft-bing-websearch-api
- collection_type: open
  name: Bing Search APIs
  slug: open-microsoft-bing
common:
- group: commercial
  href: https://artifacts.apis.io/microsoft-bing/plans/microsoft-bing-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-bing-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-bing/rate-limits/microsoft-bing-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-bing-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-bing/finops/microsoft-bing-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-bing-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-bing/agentic-access/microsoft-bing-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-bing-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bing/security/microsoft-bing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-bing-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-bing/authentication/microsoft-bing-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-bing-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/bing/apis/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/quickstarts/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/create-bing-search-service-resource
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/quickstarts/sdk/web-search-client-library
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/bing/apis/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://blogs.bing.com/search/feed
created: '2026-03-13'
description: Microsoft Bing provides a comprehensive suite of search APIs that enable developers to integrate web, image, video, news, entity, and visual search capabilities into their applications. These APIs are part of Azure AI Services and provide intelligent search experiences powered by Bing's web-scale index.
finops:
- has_sources: false
  method: generated
  name: Microsoft Bing Finops
  primary_unit: request
  service_category: API
  slug: microsoft-bing-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-bing.png
layout: provider
modified: '2026-05-19'
name: Microsoft Bing
nav: Providers
network: true
overview: 'Microsoft Bing is listed with 18 APIs on the [APIs.io](https://apis.io/) network, including Autosuggest API, Custom Search API, Entity Search API, and 15 more. Tagged areas include Search, Web Search, Image, Video, and News.


  The Microsoft Bing catalog on APIs.io includes 1 Spectral governance ruleset.


  Microsoft Bing''s developer surface includes authentication, developer portal, pricing, getting-started guide, support, engineering blog, and 11 more developer resources.'
plans:
- name: Microsoft Bing Plans Pricing
  plan_count: 3
  slug: microsoft-bing-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Microsoft Bing Rate Limits
  slug: microsoft-bing-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Microsoft Bing API Rules
  rule_count: 49
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 1
  slug: microsoft-bing-rules
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 50.5
    catalog_earned_first_party: 0.0
    catalog_gap: 64.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  previous_composite: 0.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-bing/microsoft-bing-2026-06-20T185445.png
security:
- kind: authentication
  name: Microsoft Bing Authentication
  slug: microsoft-bing-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Microsoft Bing Domain Security
  slug: microsoft-bing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: microsoft-bing
tags:
- Search
- Web Search
- Image
- Video
- News
- Azure AI
- Autosuggest
- Visual Search
- Defunct
website: https://www.microsoft.com/
---
