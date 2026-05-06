---
aid: microsoft-bing
url: https://raw.githubusercontent.com/api-evangelist/microsoft-bing/refs/heads/main/apis.yml
name: Microsoft Bing
description: Microsoft Bing provides a comprehensive suite of search APIs that enable developers to integrate web, image, video, news, entity, and visual search capabilities into their applications. These APIs are part of Azure AI Services and provide intelligent search experiences powered by Bing's web-scale index.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Search
  - Web Search
  - Images
  - Videos
  - News
  - Azure AI
  - Autosuggest
  - Visual Search
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: microsoft-bing:web-search
    name: Bing Web Search API
    description: The Bing Web Search API provides a comprehensive web search experience by returning relevant web pages, images, videos, news, and more for a given search query.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
    baseURL: https://api.bing.microsoft.com/
    tags:
      - Search
      - Web Search
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
      - type: API Reference
        url: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/reference/endpoints
  - aid: microsoft-bing:image-search
    name: Bing Image Search API
    description: The Bing Image Search API enables developers to search for images across the web with advanced filtering options.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/bing/search-apis/bing-image-search/overview
    baseURL: https://api.bing.microsoft.com/
    tags:
      - Search
      - Images
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/bing/search-apis/bing-image-search/overview
  - aid: microsoft-bing:video-search
    name: Bing Video Search API
    description: The Bing Video Search API allows developers to search for videos across the web and retrieve video metadata.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/bing/search-apis/bing-video-search/overview
    baseURL: https://api.bing.microsoft.com/
    tags:
      - Search
      - Videos
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/bing/search-apis/bing-video-search/overview
  - aid: microsoft-bing:news-search
    name: Bing News Search API
    description: The Bing News Search API returns relevant news articles from across the web for a given query.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/bing/search-apis/bing-news-search/overview
    baseURL: https://api.bing.microsoft.com/
    tags:
      - Search
      - News
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/bing/search-apis/bing-news-search/overview
  - aid: microsoft-bing:entity-search
    name: Bing Entity Search API
    description: The Bing Entity Search API returns structured information about people, places, organizations, and other entities.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/bing/search-apis/bing-entity-search/overview
    baseURL: https://api.bing.microsoft.com/
    tags:
      - Search
      - Entities
      - Knowledge Graph
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/bing/search-apis/bing-entity-search/overview
  - aid: microsoft-bing:autosuggest
    name: Bing Autosuggest API
    description: The Bing Autosuggest API provides intelligent search query suggestions as users type.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/bing/search-apis/bing-autosuggest/overview
    baseURL: https://api.bing.microsoft.com/
    tags:
      - Search
      - Autosuggest
      - Autocomplete
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/bing/search-apis/bing-autosuggest/overview
  - aid: microsoft-bing:spell-check
    name: Bing Spell Check API
    description: The Bing Spell Check API provides contextual spell checking using machine learning models.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/bing/search-apis/bing-spell-check/overview
    baseURL: https://api.bing.microsoft.com/
    tags:
      - Search
      - Spell Check
      - NLP
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/bing/search-apis/bing-spell-check/overview
  - aid: microsoft-bing:visual-search
    name: Bing Visual Search API
    description: The Bing Visual Search API enables image-based search by analyzing uploaded images or image URLs.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/bing/search-apis/bing-visual-search/overview
    baseURL: https://api.bing.microsoft.com/
    tags:
      - Search
      - Visual Search
      - Image Recognition
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/bing/search-apis/bing-visual-search/overview
  - aid: microsoft-bing:custom-search
    name: Bing Custom Search API
    description: The Bing Custom Search API allows developers to create tailored search experiences by defining a custom view of the web.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/bing/search-apis/bing-custom-search/overview
    baseURL: https://api.bing.microsoft.com/
    tags:
      - Search
      - Custom Search
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/bing/search-apis/bing-custom-search/overview
  - aid: microsoft-bing:local-business-search
    name: Bing Local Business Search API
    description: The Bing Local Business Search API returns information about local businesses based on search queries and location.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/bing/search-apis/bing-local-business-search/overview
    baseURL: https://api.bing.microsoft.com/
    tags:
      - Search
      - Local Business
      - Places
      - Azure AI
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/bing/search-apis/bing-local-business-search/overview
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://www.microsoft.com/en-us/bing/apis/pricing
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/quickstarts/quickstart
  - type: Authentication
    url: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/create-bing-search-service-resource
  - type: SDKs
    url: https://learn.microsoft.com/en-us/bing/search-apis/bing-web-search/quickstarts/sdk/web-search-client-library
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/bing/apis/legal
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
