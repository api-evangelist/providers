---
aid: elasticsearch
url: https://raw.githubusercontent.com/api-evangelist/elasticsearch/refs/heads/main/apis.yml
apis:
- aid: elasticsearch:elasticsearch-rest-api
  name: Elasticsearch REST API
  description: RESTful API for indexing, searching, and managing data in Elasticsearch clusters, including document, index, cluster, and security operations.
  humanURL: https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html
  baseURL: https://localhost:9200
  tags:
  - Analytics
  - Database
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
- Full-Text Search
- NoSQL
- Search
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Elasticsearch is an open source search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. It provides a RESTful API for indexing, searching, and managing data, with powerful aggregation capabilities and real-time analytics at scale.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

