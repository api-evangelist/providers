---
aid: elasticsearch
name: Elasticsearch
description: Elasticsearch is an open source search and analytics engine for all types of data, including textual, numerical, geospatial, structured, and unstructured. It provides a RESTful API for indexing, searching, and managing data, with powerful aggregation capabilities and real-time analytics at scale.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Database
  - Full-Text Search
  - NoSQL
  - Search
url: https://www.elastic.co/elasticsearch/
created: '2024-01-01'
modified: '2026-05-04'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
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
common:
  - type: Website
    url: https://www.elastic.co/elasticsearch/
  - type: Documentation
    url: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
  - type: GettingStarted
    url: https://www.elastic.co/guide/en/elasticsearch/reference/current/getting-started.html
  - type: Blog
    url: https://www.elastic.co/blog/
  - type: Status
    url: https://status.elastic.co/
  - type: TermsOfService
    url: https://www.elastic.co/agreements/
  - type: PrivacyPolicy
    url: https://www.elastic.co/legal/privacy-statement
  - type: Pricing
    url: https://www.elastic.co/pricing/
  - type: Support
    url: https://www.elastic.co/support
  - type: GitHubOrganization
    url: https://github.com/elastic
  - type: Features
    data:
      - 'Elasticsearch (Elastic): hundreds of services across Search and Observability'
      - 'Detailed pricing: see https://www.elastic.co/pricing'
      - 'Service: Elasticsearch Service'
      - 'Service: Kibana'
      - 'Service: Logstash'
      - 'Service: Beats'
      - 'Service: APM'
      - 'Service: Synthetics'
      - 'Service: Security (SIEM, Endpoint)'
      - 'Service: Maps'
      - 'Service: Canvas'
      - 'Service: Stack Monitoring'
    sources:
      - https://www.elastic.co/pricing
      - https://focus.finops.org/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
