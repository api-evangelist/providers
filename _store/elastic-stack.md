---
aid: elastic-stack
url: https://raw.githubusercontent.com/api-evangelist/elastic-stack/refs/heads/main/apis.yml
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
name: Elastic Stack
tags:
- Analytics
- Logging
- Monitoring
- Observability
- Search
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Elastic Stack (formerly known as the ELK Stack) is a collection of open-source products from Elastic designed to help users take data from any source, in any format, and search, analyze, and visualize that data in real-time. The stack includes Elasticsearch for search and analytics, Kibana for visualization, Logstash for data processing, and Beats for data shipping.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

