---
aid: springer-nature
name: Springer Nature
description: Springer Nature is a globally recognized leader in scientific, technical, and medical publishing, providing access to a wide array of scholarly and professional content. Their developer APIs empower developers to integrate high-quality research metadata, open access full-text content, and text mining capabilities into applications, platforms, and research tools. The APIs cover metadata search, full-text retrieval, open access content, and rich scholarly publication data.
type: Index
position: Consumer
access: 3rd-Party
image: https://resource-cms.springernature.com/springer-cms/rest/v1/content/26613678/data/Springer_Nature_Logo_April21.png
tags:
  - Academic Publishing
  - Open Access
  - Research
  - Scholarly Content
  - Scientific Publishing
created: '2025-02-06'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/springer-nature/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: springer-nature:springer-nature-meta-api
    name: Springer Nature Meta API
    description: The Meta API (versioned metadata) provides access to metadata for over 14 million online documents including articles, books, and book chapters. Supports search by keyword, author, journal, ISBN, DOI, subject, and date range. Returns rich metadata including abstracts, author affiliations, funding, and links.
    humanURL: https://dev.springernature.com/docs/api-endpoints/meta-api/
    baseURL: https://api.springernature.com/meta/v2
    tags:
      - Bibliometrics
      - Metadata
      - Research
      - Search
    properties:
      - type: Documentation
        url: https://dev.springernature.com/docs/api-endpoints/meta-api/
      - type: Getting Started
        url: https://dev.springernature.com/docs/introduction/
      - type: OpenAPI
        url: openapi/springer-nature-meta-openapi.yml
  - aid: springer-nature:springer-nature-openaccess-api
    name: Springer Nature Open Access API
    description: Provides free access to open access research articles and book chapters published by Springer Nature. Returns full-text content (where licensed), metadata, abstracts, and PDF links for open access publications.
    humanURL: https://dev.springernature.com/docs/api-endpoints/open-access/
    baseURL: https://api.springernature.com/openaccess
    tags:
      - Full Text
      - Open Access
      - Research Content
    properties:
      - type: Documentation
        url: https://dev.springernature.com/docs/api-endpoints/open-access/
      - type: OpenAPI
        url: openapi/springer-nature-openaccess-openapi.yml
  - aid: springer-nature:springer-nature-metadata-api
    name: Springer Nature Metadata API
    description: The legacy Metadata API provides metadata retrieval for Springer publications. Returns article and book metadata via DOI, journal name, ISSN, or keyword. Predecessor to the Meta API with slightly different response structure.
    humanURL: https://dev.springernature.com/docs/api-endpoints/metadata-api/
    baseURL: https://api.springernature.com
    tags:
      - Books
      - Journals
      - Metadata
      - Publications
    properties:
      - type: Documentation
        url: https://dev.springernature.com/docs/api-endpoints/metadata-api/
  - aid: springer-nature:springer-nature-fulltext-api
    name: Springer Nature Full Text API
    description: Premium full-text API providing content retrieval for licensed Springer Nature publications including text and data mining (TDM) capabilities. Requires institutional or premium API access. Returns XML and HTML article content.
    humanURL: https://dev.springernature.com/docs/api-endpoints/fulltext-api/
    baseURL: https://api.springernature.com
    tags:
      - Full Text
      - Premium
      - Text Mining
    properties:
      - type: Documentation
        url: https://dev.springernature.com/docs/api-endpoints/fulltext-api/
common:
  - type: Portal
    url: https://dev.springernature.com/
  - type: Sign Up
    url: https://dev.springernature.com/signup
  - type: Website
    url: https://www.springernature.com/
  - type: API Playground
    url: https://dev.springernature.com/docs/live-documentation/
  - type: Rate Limits
    url: https://dev.springernature.com/docs/rate-limit-details/rate-limits/
  - type: Terms and Conditions
    url: https://dev.springernature.com/terms-conditions/
  - type: GitHub Organization
    url: https://github.com/springernature
  - type: Blog
    url: https://www.springernature.com/gp/researchers/the-source
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
