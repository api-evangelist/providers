---
aid: api-harmony
name: API Harmony
description: API Harmony was an API discovery and recommendation tool from IBM Research that used graph-based search, machine learning, and cognitive technologies to help developers find, compare, and select compatible APIs. It was offered as a cloud service on IBM Bluemix and has since been discontinued.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Aggregation
  - API Discovery
  - API Recommendation
  - Graph Technology
  - IBM
  - Machine Learning
url: https://raw.githubusercontent.com/api-evangelist/api-harmony/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: api-harmony:api-harmony-service
    name: API Harmony Service
    description: API Harmony was an intelligent API matchmaking service that used graph technology and machine learning to search public APIs, reveal relationships between them, make recommendations, and identify gaps. It anticipated what developers would need to build applications and suggested optimal API combinations. The service has been discontinued.
    humanURL: https://developer.ibm.com/api/view/apiharmony-prod:apih-product:title-API_Harmony
    tags:
      - API Discovery
      - API Recommendation
      - Discontinued
      - Graph Search
      - Machine Learning
    properties:
      - type: Documentation
        url: https://developer.ibm.com/api/view/apiharmony-prod:apih-product:title-API_Harmony
      - type: Website
        url: https://apiharmony-open.mybluemix.net/public
common:
  - type: Website
    url: https://developer.ibm.com/apiharmony/
  - type: Documentation
    url: https://developer.ibm.com/api/view/apiharmony-prod:apih-product:title-API_Harmony
  - type: Research
    url: https://research.ibm.com/publications/api-harmony-graph-based-search-and-selection-of-apis-in-the-cloud
  - type: Article
    url: https://www.linuxjournal.com/node/1338947
  - type: Features
    data:
      - name: API Graph Search
        description: Graph-based search across public APIs to reveal relationships and connections between services.
      - name: API Recommendation
        description: Machine learning-powered recommendations for compatible APIs based on developer intent and context.
      - name: API Composition Support
        description: Tooling to help developers compose multiple APIs into unified applications.
      - name: API Discovery
        description: Unified catalog and discovery interface for cloud-hosted and public APIs.
      - name: API Publishing
        description: Tools for API providers to publish and promote their APIs to the ecosystem.
      - name: Gap Identification
        description: Identifies gaps in the API ecosystem where no existing API satisfies a developer need.
  - type: UseCases
    data:
      - name: Cloud API Discovery
        description: Help developers find the right APIs for cloud-based application development on IBM Bluemix.
      - name: API Compatibility Analysis
        description: Identify which APIs can be combined for a given use case without conflicts or duplication.
      - name: API Portfolio Management
        description: API providers could publish and promote their services to the broader developer ecosystem.
      - name: Microservices Integration
        description: Support microservices architectures by identifying optimal third-party API combinations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
