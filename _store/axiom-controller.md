---
aid: axiom-controller
url: https://raw.githubusercontent.com/api-evangelist/axiom-controller/refs/heads/main/apis.yml
apis:
- aid: axiom-controller:axiom-ingest-api
  name: Axiom Ingest API
  description: API for ingesting logs, events, and telemetry data into Axiom datasets.
  humanURL: https://axiom.co/docs/restapi/ingest
  baseURL: https://api.axiom.co/v1
  tags:
  - Events
  - Ingest
  - Logs
  - Telemetry
  properties:
  - type: Documentation
    url: https://axiom.co/docs/restapi/ingest
- aid: axiom-controller:axiom-query-api
  name: Axiom Query API
  description: API for querying and analyzing data stored in Axiom datasets using APL (Axiom Processing Language).
  humanURL: https://axiom.co/docs/restapi/query
  baseURL: https://api.axiom.co/v1
  tags:
  - Analytics
  - APL
  - Query
  properties:
  - type: Documentation
    url: https://axiom.co/docs/restapi/query
name: Axiom Controller
tags:
- Analytics
- Cloud Native
- Logging
- Monitoring
- Observability
- Telemetry
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Axiom is a cloud-native observability platform providing APIs for ingesting, querying, and managing telemetry data including logs, traces, and metrics with support for datasets, monitors, and organization management.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

