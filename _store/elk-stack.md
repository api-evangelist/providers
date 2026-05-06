---
aid: elk-stack
name: Elastic Stack (ELK Stack)
description: The Elastic Stack (formerly known as the ELK Stack) is a collection of open-source products from Elastic - Elasticsearch, Logstash, Kibana, and Beats - designed for taking data from any source, in any format, and searching, analyzing, and visualizing it in real time. Widely used for log management, observability, and security analytics.
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
modified: '2026-03-16'
position: Consumer
access: 3rd-Party
specificationVersion: '0.19'
apis:
  - aid: elk-stack:elasticsearch-api
    name: Elasticsearch API
    description: Distributed, RESTful search and analytics engine serving as the heart of the Elastic Stack for centralized storage and search.
    humanURL: https://www.elastic.co/elasticsearch/
    baseURL: https://localhost:9200
    tags:
      - Analytics
      - Database
      - Search
    properties:
      - type: Documentation
        url: https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/elastic/elasticsearch-specification/main/output/openapi/elasticsearch-serverless-openapi.json
  - aid: elk-stack:kibana-api
    name: Kibana API
    description: Data visualization and exploration tool for reviewing logs and events, providing real-time dashboards and analytics for Elasticsearch data.
    humanURL: https://www.elastic.co/kibana/
    baseURL: https://localhost:5601
    tags:
      - Analytics
      - Dashboard
      - Visualization
    properties:
      - type: Documentation
        url: https://www.elastic.co/guide/en/kibana/current/index.html
common:
  - type: Website
    url: https://www.elastic.co/elastic-stack/
  - type: Documentation
    url: https://www.elastic.co/guide/index.html
  - type: GettingStarted
    url: https://www.elastic.co/guide/index.html
  - type: Blog
    url: https://www.elastic.co/blog/
  - type: Support
    url: https://www.elastic.co/support
  - type: Pricing
    url: https://www.elastic.co/pricing/
  - type: GitHubOrganization
    url: https://github.com/elastic
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
