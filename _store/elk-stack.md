---
aid: elk-stack
url: https://raw.githubusercontent.com/api-evangelist/elk-stack/refs/heads/main/apis.yml
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
name: Elastic Stack (ELK Stack)
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
description: The Elastic Stack (formerly known as the ELK Stack) is a collection of open-source products from Elastic - Elasticsearch, Logstash, Kibana, and Beats - designed for taking data from any source, in any format, and searching, analyzing, and visualizing it in real time. Widely used for log management, observability, and security analytics.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

