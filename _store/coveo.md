---
aid: coveo
name: Coveo
x-type: company
description: Coveo is a cloud-based AI-relevance platform that delivers personalized search, recommendations, and discovery experiences across digital workplaces, customer service portals, websites, and commerce storefronts. The Coveo platform exposes a family of REST APIs covering search, content indexing (Push and Stream), usage analytics, machine learning, commerce, and platform administration.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/coveo/refs/heads/main/apis.yml
type: Index
access: 3rd-Party
position: Consuming
created: '2025-02-08'
modified: '2026-04-28'
tags:
  - AI
  - Analytics
  - Catalog
  - Commerce
  - Customers
  - Experiences
  - Machine Learning
  - Personalization
  - Recommendations
  - Search
specificationVersion: '0.19'
apis:
  - aid: coveo:search
    name: Coveo Search API
    description: The Coveo Search API is a RESTful interface for issuing queries against the Coveo unified index, retrieving relevance-ranked results with facets, highlights, and personalization context. It supports query pipelines, authentication tokens, and analytics correlation.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.coveo.com/en/52/
    baseURL: https://platform.cloud.coveo.com/rest/search/v2
    tags:
      - Facets
      - Query Pipelines
      - REST
      - Search
    properties:
      - type: Documentation
        url: https://docs.coveo.com/en/52/
      - type: APIReference
        url: https://docs.coveo.com/en/13/api-reference/search-api
      - type: BuildSearchUI
        url: https://docs.coveo.com/en/1370/
    features:
      - name: Query Pipelines
        description: Server-side query rewriting, ranking, and conditional rules.
      - name: Personalization
        description: Per-user relevance based on profile and activity context.
      - name: Search Tokens
        description: Short-lived JWT search tokens for secure end-user querying.
  - aid: coveo:push
    name: Coveo Push API
    description: The Coveo Push API enables programmatic indexing of items into a Coveo Push source, including individual document push, batch push via secure cloud storage, and source state management for partial or full indexing operations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.coveo.com/en/1546/
    baseURL: https://api.cloud.coveo.com/push/v1
    tags:
      - Indexing
      - Push
      - REST
      - Sources
    properties:
      - type: Documentation
        url: https://docs.coveo.com/en/1546/
      - type: PushSourceManagement
        url: https://docs.coveo.com/en/68/
  - aid: coveo:stream
    name: Coveo Stream API
    description: The Coveo Stream API is the modern high-throughput indexing interface used to add and update content in Catalog sources for commerce, replacing batch Push for catalog ingestion.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.coveo.com/en/lb4a0344/
    baseURL: https://api.cloud.coveo.com/push/v1
    tags:
      - Catalog
      - Commerce
      - Indexing
      - Stream
    properties:
      - type: Documentation
        url: https://docs.coveo.com/en/lb4a0344/
      - type: PushAndUpdateCatalog
        url: https://docs.coveo.com/en/p5je0317/
  - aid: coveo:commerce
    name: Coveo Commerce API
    description: The Coveo Commerce API provides endpoints to power product search result pages, product listing pages (PLPs), product recommendations, and product discovery, plus endpoints for managing product inventories.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.coveo.com/en/p5je0317/
    baseURL: https://platform.cloud.coveo.com/rest/organizations
    tags:
      - Commerce
      - PLP
      - Product Listings
      - Recommendations
      - Search
    properties:
      - type: Documentation
        url: https://docs.coveo.com/en/p5je0317/
      - type: CommerceSetup
        url: https://docs.coveo.com/en/o25a0034/
  - aid: coveo:usage-analytics
    name: Coveo Usage Analytics API
    description: The Coveo Usage Analytics (UA) Read and Write APIs record search and click events from end-user search experiences, and expose query and reporting endpoints used by dashboards and Coveo Machine Learning models.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.coveo.com/en/365/
    baseURL: https://analytics.cloud.coveo.com/rest/ua/v15
    tags:
      - Analytics
      - Events
      - REST
      - Reporting
    properties:
      - type: Documentation
        url: https://docs.coveo.com/en/365/
      - type: TrackUsageAnalytics
        url: https://docs.coveo.com/en/ncd90215/
  - aid: coveo:machine-learning
    name: Coveo Machine Learning API
    description: The Coveo Machine Learning API provides endpoints for managing ML models including Automatic Relevance Tuning (ART), Query Suggestions (QS), Recommendations (PR), and Dynamic Navigation Experience (DNE) models.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.coveo.com/en/1727/
    baseURL: https://platform.cloud.coveo.com/rest/organizations
    tags:
      - AI
      - Machine Learning
      - Recommendations
      - Relevance
    properties:
      - type: Documentation
        url: https://docs.coveo.com/en/1727/
  - aid: coveo:platform
    name: Coveo Platform API
    description: The Coveo Platform API provides administrative endpoints for managing organizations, sources, security identities, query pipelines, fields, tokens, and configuration of the Coveo Platform.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://docs.coveo.com/en/124/
    baseURL: https://platform.cloud.coveo.com/rest
    tags:
      - Administration
      - Organizations
      - Pipelines
      - Sources
      - Tokens
    properties:
      - type: Documentation
        url: https://docs.coveo.com/en/124/
      - type: APIOverview
        url: https://docs.coveo.com/en/143/
common:
  - type: Website
    url: https://www.coveo.com
  - type: Documentation
    url: https://docs.coveo.com/
  - type: APIOverview
    url: https://docs.coveo.com/en/143/
  - type: DeveloperBlog
    url: https://blog.coveo.com/
  - type: GitHub
    url: https://github.com/coveo
  - type: TermsOfService
    url: https://www.coveo.com/en/company/legal
  - type: PrivacyPolicy
    url: https://www.coveo.com/en/company/legal/privacy-statement
  - type: Support
    url: https://connect.coveo.com/s/
  - type: LinkedIn
    url: https://www.linkedin.com/company/coveo
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
