---
aid: microsoft-azure-search
url: https://raw.githubusercontent.com/api-evangelist/microsoft-azure-search/refs/heads/main/apis.yml
name: Azure AI Search
description: Azure AI Search (formerly Azure Cognitive Search) is a cloud search service with built-in AI capabilities for enriching content and enabling vector and semantic search over heterogeneous data. It indexes content from Azure data sources and supports full-text, faceted, geospatial, vector, and hybrid retrieval.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - AI Search
  - Cognitive Search
  - Hybrid Search
  - Search
  - Semantic Search
  - Vector Search
created: '2026-03-13'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: microsoft-azure-search:rest-api
    name: Azure AI Search REST API
    description: Azure AI Search provides REST APIs for creating and managing search indexes, loading documents, running full-text and vector queries, configuring AI enrichment pipelines with skillsets, and managing indexers for automatic data ingestion from Azure data sources.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/rest/api/searchservice/
    baseURL: https://{search-service}.search.windows.net/
    tags:
      - Indexers
      - Indexes
      - Search
      - Skillsets
      - Vector Search
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/searchservice/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/search/search-security-api-keys
      - type: Versioning
        url: https://learn.microsoft.com/en-us/rest/api/searchservice/search-service-api-versions
  - aid: microsoft-azure-search:management-api
    name: Azure AI Search Management REST API
    description: The management REST API provides operations for creating and managing Azure AI Search service instances, scaling replicas and partitions, and managing keys and shared private link resources.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://learn.microsoft.com/en-us/rest/api/searchmanagement/
    baseURL: https://management.azure.com/
    tags:
      - Management
      - Provisioning
      - Search
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/rest/api/searchmanagement/
      - type: Authentication
        url: https://learn.microsoft.com/en-us/azure/active-directory/develop/authentication-flows-app-scenarios
common:
  - type: Portal
    url: https://portal.azure.com/
  - type: Pricing
    url: https://azure.microsoft.com/en-us/pricing/details/search/
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/search/
  - type: Getting Started
    url: https://learn.microsoft.com/en-us/azure/search/search-get-started-portal
  - type: SDKs
    url: https://learn.microsoft.com/en-us/azure/search/search-howto-dotnet-sdk
  - type: Status
    url: https://azure.status.microsoft/en-us/status
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/legal/terms-of-use
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: Support
    url: https://support.microsoft.com/
  - type: Blog
    url: https://azure.microsoft.com/en-us/blog/product/azure-cognitive-search/
  - type: Stack Overflow
    url: https://stackoverflow.com/questions/tagged/azure-cognitive-search
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
