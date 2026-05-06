---
aid: logstash
name: Logstash
description: Open source server-side data processing pipeline that ingests data from multiple sources, transforms it, and sends it to a specified destination. Part of the Elastic Stack.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data Processing
  - ETL
  - Log Management
  - Pipeline
url: https://raw.githubusercontent.com/api-evangelist/logstash/refs/heads/main/apis.yml
created: '2025-01-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: logstash:logstash-monitoring-api
    name: Logstash Monitoring API
    description: The Logstash Monitoring API exposes node info, plugin info, node stats, hot threads, and a health report endpoint over HTTP on port 9600 by default. There is no published OpenAPI specification; see Elastic's monitoring documentation for endpoint details.
    humanURL: https://www.elastic.co/guide/en/logstash/current/monitoring-logstash.html
    tags:
      - Monitoring
      - Operational
    properties:
      - type: Documentation
        url: https://www.elastic.co/guide/en/logstash/current/monitoring-logstash.html
      - type: GitHub Repository
        url: https://github.com/elastic/logstash
common:
  - url: https://www.elastic.co/logstash
    type: Website
  - url: https://www.elastic.co/guide/en/logstash/current/index.html
    type: Documentation
  - url: https://github.com/elastic/logstash
    type: GitHubOrganization
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
