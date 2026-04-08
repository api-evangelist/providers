---
aid: cockroachdb
url: https://raw.githubusercontent.com/api-evangelist/cockroachdb/refs/heads/main/apis.yml
apis:
- aid: cockroachdb:cloud-api
  name: CockroachDB Cloud API
  tags:
  - Cloud
  - Cluster Management
  - Database
  - Infrastructure
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://cockroachlabs.cloud/api/v1
  humanURL: https://www.cockroachlabs.com/docs/cockroachcloud/cloud-api
  properties:
  - url: https://www.cockroachlabs.com/docs/cockroachcloud/cloud-api
    type: Documentation
  - url: https://www.cockroachlabs.com/docs/api/cloud/v1.html
    type: Documentation
  - url: openapi/cockroachdb-cloud-api-openapi.yml
    type: OpenAPI
  description: The CockroachDB Cloud API is a REST interface that provides programmatic access to manage the lifecycle of clusters within a CockroachDB Cloud organization. It enables developers and operators to create, configure, scale, and delete CockroachDB Serverless and Dedicated clusters without using the web console. The API supports operations including cluster provisioning, node management, network authorization, customer-managed encryption keys, and export configurations.
- aid: cockroachdb:cluster-api
  name: CockroachDB Cluster API
  tags:
  - Cluster
  - Database
  - Monitoring
  - Nodes
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://localhost:8080/api/v2
  humanURL: https://www.cockroachlabs.com/docs/stable/cluster-api
  properties:
  - url: https://www.cockroachlabs.com/docs/stable/cluster-api
    type: Documentation
  - url: https://www.cockroachlabs.com/docs/api/cluster/v2.html
    type: Documentation
  - url: openapi/cockroachdb-cluster-api-openapi.yml
    type: OpenAPI
  description: The CockroachDB Cluster API is a REST API hosted by all nodes of a CockroachDB cluster that provides information about the cluster, its nodes, and operational status. It is available on the same HTTP port used by the DB Console, defaulting to port 8080, and exposes endpoints under the /api/v2 base path. The API enables monitoring and troubleshooting workflows using any HTTP-capable tooling, covering endpoints for health checks, node details, sessions, ranges, and database metadata.
name: Cockroachdb
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: The Cloud API is used to manage clusters within an organization.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

