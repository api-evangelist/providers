---
aid: elastic-search
url: https://raw.githubusercontent.com/api-evangelist/elastic-search/refs/heads/main/apis.yml
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
name: Elasticsearch
tags:
- Analytics
- Database
- Distributed Systems
- Full-Text Search
- NoSQL
- Search
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Elasticsearch is a distributed, RESTful search and analytics engine capable of addressing a growing number of use cases. As the heart of the Elastic Stack, it centrally stores data for fast search, fine-tuned relevancy, and powerful analytics that scale with ease. It provides a comprehensive REST API for document indexing, searching, aggregations, and cluster management.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

