---
aid: elastic-search
name: Elasticsearch
description: Elasticsearch is a distributed, RESTful search and analytics engine capable of addressing a growing number of use cases. As the heart of the Elastic Stack, it centrally stores data for fast search, fine-tuned relevancy, and powerful analytics that scale with ease. It provides a comprehensive REST API for document indexing, searching, aggregations, and cluster management.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Database
  - Distributed Systems
  - Full-Text Search
  - NoSQL
  - Search
url: https://www.elastic.co/elasticsearch/
created: '2024-01-01'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: elastic-search:elasticsearch-rest-api
    name: Elasticsearch REST API
    description: The main REST API for interacting with Elasticsearch clusters, including document indexing, searching, aggregations, and cluster management.
    humanURL: https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html
    baseURL: https://localhost:9200
    tags:
      - Indexing
      - REST API
      - Search
    properties:
      - type: Documentation
        url: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
      - type: OpenAPI
        url: https://github.com/elastic/elasticsearch-specification
common:
  - type: Website
    url: https://www.elastic.co/elasticsearch/
  - type: Documentation
    url: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
  - type: GettingStarted
    url: https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html
  - type: Blog
    url: https://www.elastic.co/blog/
  - type: Pricing
    url: https://www.elastic.co/pricing/
  - type: Support
    url: https://www.elastic.co/support
  - type: Status
    url: https://status.elastic.co/
  - type: TermsOfService
    url: https://www.elastic.co/agreements/
  - type: GitHubOrganization
    url: https://github.com/elastic
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
