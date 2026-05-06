---
aid: elastic-stack
name: Elastic Stack
description: The Elastic Stack (formerly known as the ELK Stack) is a collection of open-source products from Elastic designed to help users take data from any source, in any format, and search, analyze, and visualize that data in real-time. The stack includes Elasticsearch for search and analytics, Kibana for visualization, Logstash for data processing, and Beats for data shipping.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Analytics
  - Logging
  - Monitoring
  - Observability
  - Search
url: https://www.elastic.co/elastic-stack/
created: '2024-01-01'
modified: '2026-04-28'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: elastic-stack:elasticsearch-api
    name: Elasticsearch API
    description: Distributed search and analytics engine with RESTful API for indexing, searching, and analyzing data at scale.
    humanURL: https://www.elastic.co/elasticsearch/
    baseURL: https://localhost:9200
    tags:
      - Analytics
      - Indexing
      - Search
    properties:
      - type: Documentation
        url: https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html
  - aid: elastic-stack:kibana-api
    name: Kibana API
    description: Data visualization and exploration tool API for Elasticsearch, providing dashboards, saved objects, alerting, and spaces management.
    humanURL: https://www.elastic.co/kibana/
    baseURL: https://localhost:5601/api
    tags:
      - Analytics
      - Dashboards
      - Visualization
    properties:
      - type: Documentation
        url: https://www.elastic.co/guide/en/kibana/current/api.html
common:
  - type: Website
    url: https://www.elastic.co/
  - type: Documentation
    url: https://www.elastic.co/guide/index.html
  - type: Pricing
    url: https://www.elastic.co/pricing
  - type: Blog
    url: https://www.elastic.co/blog
  - type: Support
    url: https://www.elastic.co/support
  - type: Status
    url: https://status.elastic.co
  - type: TermsOfService
    url: https://www.elastic.co/agreements
  - type: PrivacyPolicy
    url: https://www.elastic.co/legal/privacy-statement
  - type: GitHubOrganization
    url: https://github.com/elastic
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
