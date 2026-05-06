---
aid: cockroachdb
url: https://raw.githubusercontent.com/api-evangelist/cockroachdb/refs/heads/main/apis.yml
name: CockroachDB
description: CockroachDB is a distributed SQL database with strong consistency, PostgreSQL compatibility, and a managed cloud offering. The Cloud API manages cluster lifecycle; the Cluster API exposes per-node operational state for monitoring and troubleshooting.
tags:
  - Cluster Management
  - Cloud
  - Database
  - Distributed SQL
  - Infrastructure
  - PostgreSQL Compatible
  - SQL
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
x-type: company
created: '2024-11-24'
modified: '2026-05-04'
position: Consumer
x-overview: 'CockroachDB is a distributed, PostgreSQL-compatible SQL database built by Cockroach Labs. It scales horizontally, survives disk, machine, rack, and data-center failures with localized fallout, and provides ACID transactions across geographies. CockroachDB is offered as a fully managed service on cockroachlabs.cloud (Basic, Standard, Advanced plans) and as self-hosted software. Two REST APIs are available: the CockroachDB Cloud API for managing the lifecycle of cloud-hosted clusters, and the per-node CockroachDB Cluster API for cluster health, monitoring, and operational status.'
apis:
  - aid: cockroachdb:cloud-api
    name: CockroachDB Cloud API
    tags:
      - Cloud
      - Cluster Management
      - Database
      - Infrastructure
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://cockroachlabs.cloud
    humanURL: https://www.cockroachlabs.com/docs/cockroachcloud/cloud-api
    properties:
      - url: https://www.cockroachlabs.com/docs/cockroachcloud/cloud-api
        type: Documentation
      - url: https://www.cockroachlabs.com/docs/api/cloud/v1
        type: APIReference
      - url: openapi/cockroachdb-cloud-api-openapi.yml
        type: OpenAPI
    description: REST API for managing the lifecycle of CockroachDB Cloud clusters. Supports cluster provisioning, scaling, deletion, SQL user management, network authorization (IP allowlists, private endpoints), customer-managed encryption keys (CMEK), maintenance windows, version deferral, audit log export, metric and log export, SCIM v2 group/user provisioning, folder organization, service accounts, API keys, invoices, and backup configuration. Authenticated via bearer tokens and rate-limited to 10 requests per second per user.
    x-features:
      - Bearer-token authentication
      - Cc-Version header for API versioning
      - Service accounts and API keys
      - Terraform provider for IaC
      - SCIM v2 endpoints for SSO sync
      - CMEK rotation and revocation
      - Audit log and metric export configuration
    x-use-cases:
      - Programmatic cluster provisioning
      - GitOps with the CockroachDB Terraform provider
      - SCIM-based identity sync
      - Audit log export to SIEM
      - Cost monitoring via invoices
  - aid: cockroachdb:cluster-api
    name: CockroachDB Cluster API
    tags:
      - Cluster
      - Database
      - Monitoring
      - Nodes
      - Observability
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://localhost:8080/api/v2
    humanURL: https://www.cockroachlabs.com/docs/stable/cluster-api
    properties:
      - url: https://www.cockroachlabs.com/docs/stable/cluster-api
        type: Documentation
      - url: https://www.cockroachlabs.com/docs/api/cluster/v2
        type: APIReference
      - url: openapi/cockroachdb-cluster-api-openapi.yml
        type: OpenAPI
    description: REST API hosted by every CockroachDB node under the /api/v2 base path, exposed on the same HTTP port as the DB Console (default 8080). Provides health checks, node detail, hot range info, session and query introspection, database and table metadata, and event log retrieval. Authentication uses session tokens obtained via /api/v2/login/ and passed in the X-Cockroach-API-Session header.
    x-features:
      - Available on every CockroachDB node
      - Session-token auth via /api/v2/login/
      - Health, node, range, and database introspection
      - JSON responses suitable for monitoring pipelines
    x-use-cases:
      - Custom dashboards and alerting
      - Liveness probes and readiness checks
      - Hot-range and session troubleshooting
      - Self-hosted observability integrations
common:
  - url: json-schema/cockroachdb-cluster-schema.json
    type: JSONSchema
  - url: json-ld/cockroachdb-context.jsonld
    type: JSON-LD
  - url: rules/cockroachdb-rules.yml
    type: Spectral
  - url: capabilities/cockroachdb-capabilities.yml
    type: NaftikoCapabilities
  - type: Website
    url: https://www.cockroachlabs.com/product/
  - type: Documentation
    url: https://www.cockroachlabs.com/docs/
  - type: Pricing
    url: https://www.cockroachlabs.com/pricing/
  - type: Console
    url: https://cockroachlabs.cloud/
  - type: GitHub
    url: https://github.com/cockroachdb/cockroach
  - type: Status
    url: https://status.cockroachlabs.cloud/
  - type: Features
    data:
      - 'Basic free: 50M RUs + 10 GiB storage/mo, scales to zero'
      - 'Standard from $0.18/hr (2 vCPUs): provisioned compute up to 200 vCPUs'
      - 'Advanced from $0.60/hr (4 vCPUs): unlimited scale, CMEK, PCI/HIPAA'
      - Multi-region across AWS/GCP/Azure
      - Postgres wire-compatible SQL
      - Strongly consistent multi-region writes
      - Cloud API at 60 req/min/user
      - Datadog metrics export (Standard+)
      - Private connectivity (Standard+)
      - Up to 99.999% availability (Advanced)
      - Customer-managed encryption keys (CMEK) on Advanced
      - Backup and PITR included
      - Distributed SQL with horizontal scale
      - JSONB and full-text search
      - Geo-partitioned tables
      - ACID transactions across regions
    sources:
      - https://www.cockroachlabs.com/pricing/
    updated: '2026-05-04'
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
