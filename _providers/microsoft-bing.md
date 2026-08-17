---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
  scored_at: '2026-08-17'
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
- description: The Autosuggest API from Microsoft Bing — 1 operation(s) for autosuggest.
  name: Microsoft Bing Autosuggest API
  slug: microsoft-bing-autosuggest-api
- description: The CustomSearch API from Microsoft Bing — 1 operation(s) for customsearch.
  name: Microsoft Bing CustomSearch API
  slug: microsoft-bing-customsearch-api
- description: The EntitySearch API from Microsoft Bing — 1 operation(s) for entitysearch.
  name: Microsoft Bing EntitySearch API
  slug: microsoft-bing-entitysearch-api
- description: The ImageSearch API from Microsoft Bing — 1 operation(s) for imagesearch.
  name: Microsoft Bing ImageSearch API
  slug: microsoft-bing-imagesearch-api
- description: The NewsSearch API from Microsoft Bing — 2 operation(s) for newssearch.
  name: Microsoft Bing NewsSearch API
  slug: microsoft-bing-newssearch-api
- description: The SpellCheck API from Microsoft Bing — 1 operation(s) for spellcheck.
  name: Microsoft Bing SpellCheck API
  slug: microsoft-bing-spellcheck-api
- description: The VideoSearch API from Microsoft Bing — 1 operation(s) for videosearch.
  name: Microsoft Bing VideoSearch API
  slug: microsoft-bing-videosearch-api
- description: The VisualSearch API from Microsoft Bing — 1 operation(s) for visualsearch.
  name: Microsoft Bing VisualSearch API
  slug: microsoft-bing-visualsearch-api
- description: The WebSearch API from Microsoft Bing — 1 operation(s) for websearch.
  name: Microsoft Bing WebSearch API
  slug: microsoft-bing-websearch-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-bing-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-bing-domain-security.yml
- group: auth
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
- name: Microsoft Bing Finops
  service_category: API
  slug: microsoft-bing-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-bing.png
layout: provider
modified: '2026-05-19'
name: Microsoft Bing
nav: Providers
network: true
overview: 'Microsoft Bing publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Autosuggest API, CustomSearch API, EntitySearch API, and 6 more. Tagged areas include Search, Web Search, Images, Videos, and News.


  Microsoft Bing''s developer surface includes authentication, developer portal, pricing, getting-started guide, support, engineering blog, and 7 more developer resources.'
plans:
- name: Microsoft Bing Plans Pricing
  plan_count: 3
  slug: microsoft-bing-plans-pricing
random_paper: 102
rate_limits:
- limit_count: 5
  name: Microsoft Bing Rate Limits
  slug: microsoft-bing-rate-limits
score:
  band: thin
  composite: 40.4
  delta: 0.0
  facets:
    commercial_clarity: 47.4
    contract_quality: 52.2
    developer_ergonomics: 43.5
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-bing/refs/heads/main/screenshots/microsoft-bing-2026-06-20T185445.png
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
- Images
- Videos
- News
- Azure AI
- Autosuggest
- Visual Search
website: https://portal.azure.com/
---
