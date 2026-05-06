---
aid: apivault
url: https://raw.githubusercontent.com/api-evangelist/apivault/refs/heads/main/apis.yml
name: Apivault
tags:
  - API Catalog
  - API Directory
  - API Discovery
  - Open Source
  - Public APIs
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-03-01'
modified: '2026-04-19'
position: Consumer
description: Apivault is an open-source directory and gateway for discovering public APIs. The platform catalogs thousands of free and public APIs across 51 categories including animals, anime, blockchain, cryptocurrency, finance, health, music, news, and weather, enabling developers to find and explore APIs for application development.
apis:
  - aid: apivault:apivault
    name: Apivault
    tags:
      - API Catalog
      - API Directory
      - API Discovery
      - Open Source
      - Public APIs
    humanURL: https://apivault.dev/
    properties:
      - url: https://apivault.dev/
        type: Documentation
      - url: https://github.com/Exifly/ApiVault
        type: GitHubRepository
    description: Apivault is a free, open-source API directory that serves as a gateway to a world of public APIs. It catalogs APIs across 51 categories with details on authentication method, CORS support, and HTTPS availability. Developers can search, discover, submit, and browse APIs across all major domains. Licensed under CC BY-NC-ND 4.0.
common:
  - type: GitHubRepository
    url: https://github.com/Exifly/ApiVault
  - type: Features
    data:
      - name: API Directory
        description: Comprehensive directory of free and public APIs across 51 categories.
      - name: API Search and Discovery
        description: Search and discover APIs by category including finance, health, weather, blockchain, and more.
      - name: API Submission
        description: Developers can submit their own APIs with authentication type, CORS, and HTTPS details.
      - name: Trending and Random APIs
        description: Discover trending and randomly surfaced APIs across the catalog.
      - name: User Accounts
        description: User account management via Google sign-in for tracking submitted and liked APIs.
      - name: Open Source
        description: Fully open-source project available on GitHub under CC BY-NC-ND 4.0 license.
  - type: UseCases
    data:
      - name: API Discovery
        description: Find free and public APIs for application development across 51 categories.
      - name: API Promotion
        description: Submit and promote your own API to a community of developers.
      - name: Rapid Prototyping
        description: Quickly discover APIs to accelerate prototype and proof-of-concept development.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
