---
aid: artifact-hub
url: https://raw.githubusercontent.com/api-evangelist/artifact-hub/refs/heads/main/apis.yml
apis:
- aid: artifact-hub:artifact-hub-api
  name: Artifact Hub API
  description: The Artifact Hub API provides RESTful endpoints for searching and retrieving cloud-native packages, managing repositories, handling user subscriptions and webhooks, and administering organizations. It supports filtering by package kind, repository, organization, and various metadata attributes. The API enables programmatic access to the full Artifact Hub catalog.
  humanURL: https://artifacthub.io/docs/api/
  properties:
  - type: Documentation
    url: https://artifacthub.io/docs/api/
  tags:
  - Package Search
  - Registry
  - REST API
name: Artifact Hub
tags:
- Cloud Native
- Discovery
- Helm Charts
- Incubating
- Package Registry
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Artifact Hub is a CNCF incubating web-based application that enables finding, installing, and publishing cloud-native packages. It supports Helm charts, OPA policies, Falco rules, OLM operators, Tinkerbell actions, kubectl plugins, Tekton tasks, KEDA scalers, CoreDNS plugins, and more. Artifact Hub provides a searchable catalog with versioning, security reports, and changelog tracking.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

