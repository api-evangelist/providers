---
aid: cockroach-labs
url: https://raw.githubusercontent.com/api-evangelist/cockroach-labs/refs/heads/main/apis.yml
name: Cockroach Labs
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
modified: '2026-04-26'
position: Consumer
description: 'Cockroach Labs is the New York-based software company that builds CockroachDB, a cloud-native, distributed, PostgreSQL-compatible SQL database. CockroachDB is offered as Cockroach Labs'' fully managed cloud service (Basic, Standard, and Advanced plans) and as self-hosted software. The company provides two primary developer APIs: the CockroachDB Cloud API for managing the lifecycle of cloud-hosted clusters, and the CockroachDB Cluster API exposed by every node for cluster health, monitoring, and operational status. CockroachDB is used in production by banking, retail, gaming, and media companies including Bose, Hard Rock Digital, DoorDash, and Netflix.'
apis:
  - aid: cockroach-labs:cockroach-labs-cloud-api
    name: CockroachDB Cloud API
    tags:
      - Cloud
      - Cluster Management
      - Database
      - Infrastructure
    humanURL: https://www.cockroachlabs.com/docs/cockroachcloud/cloud-api
    baseURL: https://cockroachlabs.cloud
    properties:
      - url: https://www.cockroachlabs.com/docs/cockroachcloud/cloud-api
        type: Documentation
      - url: https://www.cockroachlabs.com/docs/api/cloud/v1
        type: APIReference
      - url: openapi/cockroach-labs-cloud-api-openapi.yml
        type: OpenAPI
    description: REST API for managing the lifecycle of CockroachDB Cloud clusters. Supports cluster provisioning, scaling, deletion, SQL user management, network authorization (IP allowlists, private endpoints), customer-managed encryption keys (CMEK), maintenance windows, version deferral, audit log export, metric and log export, SCIM v2 group/user provisioning, folder organization, service accounts, API keys, invoices, and backup configuration. Authenticated via bearer tokens and rate-limited to 10 requests per second per user. Also available via the official CockroachDB Cloud Terraform provider.
    x-features:
      - Bearer-token authentication with service accounts and API keys
      - Cc-Version header for API versioning
      - 10 RPS rate limit per user
      - SCIM v2 endpoints for SSO group/user sync
      - Terraform provider for IaC workflows
      - CMEK rotation, revocation, and key-spec management
      - Cluster scaling, maintenance windows, and version deferral
      - Audit log and metric/log export configuration
    x-use-cases:
      - Programmatic provisioning of CockroachDB clusters
      - GitOps/IaC management with Terraform
      - SCIM-based identity sync from Okta, Entra ID, Google Workspace
      - Compliance automation via audit log export to SIEM
      - Cost monitoring via invoices endpoint
  - aid: cockroach-labs:cockroach-labs-cluster-api
    name: CockroachDB Cluster API
    tags:
      - Cluster
      - Database
      - Monitoring
      - Nodes
      - Observability
    humanURL: https://www.cockroachlabs.com/docs/stable/cluster-api
    baseURL: https://localhost:8080
    properties:
      - url: https://www.cockroachlabs.com/docs/stable/cluster-api
        type: Documentation
      - url: https://www.cockroachlabs.com/docs/api/cluster/v2
        type: APIReference
      - url: openapi/cockroach-labs-cluster-api-openapi.yml
        type: OpenAPI
    description: REST API hosted by every CockroachDB node under the /api/v2 base path, exposed on the same HTTP port as the DB Console (default 8080). Provides health checks, node detail, hot range info, session and query introspection, database and table metadata, and event log retrieval. Authentication uses session tokens obtained via /api/v2/login/ and passed in the X-Cockroach-API-Session header. Self-hosted operators typically front the cluster API with a load balancer or service mesh.
    x-features:
      - Available on every CockroachDB node
      - Session-token authentication via /api/v2/login/
      - Health, node, range, session, and database introspection
      - JSON responses suitable for monitoring and alerting integrations
    x-use-cases:
      - Custom dashboards and observability pipelines
      - Programmatic health/readiness checks
      - Hot-range and session troubleshooting
      - Liveness probes for self-hosted CockroachDB
common:
  - type: Website
    url: https://www.cockroachlabs.com/
  - type: Documentation
    url: https://www.cockroachlabs.com/docs/
  - type: Pricing
    url: https://www.cockroachlabs.com/pricing/
  - type: Blog
    url: https://www.cockroachlabs.com/blog/
  - type: Glossary
    url: https://www.cockroachlabs.com/docs/stable/architecture/glossary
  - type: Console
    url: https://cockroachlabs.cloud/
  - type: Status
    url: https://status.cockroachlabs.cloud/
  - type: Support
    url: https://www.cockroachlabs.com/support/
  - type: Partners
    url: https://www.cockroachlabs.com/partners/
  - type: Security
    url: https://www.cockroachlabs.com/security/
  - type: GitHub
    url: https://github.com/cockroachdb
  - type: TerraformProvider
    url: https://registry.terraform.io/providers/cockroachdb/cockroach/latest
  - type: PrivacyPolicy
    url: https://www.cockroachlabs.com/privacy/
  - type: TermsOfService
    url: https://www.cockroachlabs.com/cloud-terms-and-conditions/
  - url: json-ld/cockroach-labs-context.jsonld
    type: JSON-LD
  - url: json-schema/cockroach-labs-cluster-schema.json
    type: JSONSchema
  - url: rules/cockroach-labs-rules.yml
    type: Spectral
  - url: capabilities/cockroach-labs-capabilities.yml
    type: NaftikoCapabilities
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
