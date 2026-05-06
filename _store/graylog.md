---
aid: graylog
name: Graylog
description: Graylog is an open source log management platform for collecting, indexing, and analyzing log data with alerting and dashboard capabilities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Logging
  - Observability
  - Log Management
  - SIEM
url: https://raw.githubusercontent.com/api-evangelist/graylog/refs/heads/main/apis.yml
created: '2026-03-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: graylog:graylog
    name: Graylog REST API
    description: Graylog provides a REST API for managing log data, streams, dashboards, alerts, users, and system configuration. The API is browseable via the bundled API Browser at /api/api-browser/.
    humanURL: https://graylog.org
    baseURL: https://api.graylog.org
    tags:
      - Logging
      - Observability
      - Log Management
      - SIEM
    properties:
      - type: Documentation
        url: https://go2docs.graylog.org
      - type: API Browser
        url: https://go2docs.graylog.org/current/setting_up_graylog/rest_api.htm
      - type: GitHub Repository
        url: https://github.com/Graylog2/graylog2-server
common:
  - type: Website
    url: https://graylog.org
  - type: Documentation
    url: https://go2docs.graylog.org
  - type: GitHub Organization
    url: https://github.com/Graylog2
  - type: Blog
    url: https://graylog.org/post/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
