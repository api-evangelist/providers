---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 51
  human_in_the_loop: 5
  name: Cockroach Labs Agentic Access
  operation_count: 98
  slug: cockroach-labs-agentic-access
  summary_line: 98 operations · 51 acting · 5 human-in-the-loop
api_count: 26
apis:
- description: Manage API keys for programmatic access, including creation, retrieval, listing, updating, and deletion.
  name: Cockroach Labs APIKeys API
  slug: cockroach-labs-apikeys-api
- description: Retrieve audit log events for the organization to support compliance and security investigations.
  name: Cockroach Labs AuditLogs API
  slug: cockroach-labs-auditlogs-api
- description: Authenticate to the Cluster API by creating and terminating API sessions. Session tokens are passed via the X-Cockroach-API-Session header on subsequent requests.
  name: Cockroach Labs Auth API
  slug: cockroach-labs-auth-api
- description: Manage cluster backups, backup configurations, and restore operations for CockroachDB clusters.
  name: Cockroach Labs BackupRestore API
  slug: cockroach-labs-backuprestore-api
- description: Retrieve invoices and billing information for the CockroachDB Cloud organization.
  name: Cockroach Labs Billing API
  slug: cockroach-labs-billing-api
- description: Create, list, retrieve, update, and delete CockroachDB Serverless and Dedicated clusters within an organization.
  name: Cockroach Labs Clusters API
  slug: cockroach-labs-clusters-api
- description: Manage customer-managed encryption keys (CMEK) for encrypting cluster data at rest using customer-controlled keys.
  name: Cockroach Labs CMEK API
  slug: cockroach-labs-cmek-api
- description: Manage databases within a CockroachDB cluster, including creation, listing, updating, and deletion.
  name: Cockroach Labs Databases API
  slug: cockroach-labs-databases-api
- description: Configure egress traffic rules and egress private endpoints for outbound cluster network traffic.
  name: Cockroach Labs EgressRules API
  slug: cockroach-labs-egressrules-api
- description: Organize clusters and other resources into hierarchical folder structures within the organization.
  name: Cockroach Labs Folders API
  slug: cockroach-labs-folders-api
- description: Check the health and readiness of individual CockroachDB nodes. The health endpoint can report whether the node is live and fully operational for accepting SQL connections.
  name: Cockroach Labs Health API
  slug: cockroach-labs-health-api
- description: Configure IP allowlist entries to control network access to a cluster.
  name: Cockroach Labs IPAllowlists API
  slug: cockroach-labs-ipallowlists-api
- description: Manage JWT issuer configurations for external identity provider integrations.
  name: Cockroach Labs JWTIssuers API
  slug: cockroach-labs-jwtissuers-api
- description: Configure log export to external destinations such as AWS CloudWatch or GCP Cloud Logging.
  name: Cockroach Labs LogExport API
  slug: cockroach-labs-logexport-api
- description: Configure maintenance windows and blackout periods for cluster upgrade scheduling.
  name: Cockroach Labs MaintenanceWindows API
  slug: cockroach-labs-maintenancewindows-api
- description: Configure metric export integrations including AWS CloudWatch, Datadog, and Prometheus.
  name: Cockroach Labs MetricExport API
  slug: cockroach-labs-metricexport-api
- description: Retrieve information about all nodes in the cluster, including their status, address, locality, and operational metrics.
  name: Cockroach Labs Nodes API
  slug: cockroach-labs-nodes-api
- description: Retrieve information about the caller's CockroachDB Cloud organization.
  name: Cockroach Labs Organizations API
  slug: cockroach-labs-organizations-api
- description: Manage private endpoint services and connections for secure VPC-level access to clusters.
  name: Cockroach Labs PrivateEndpoints API
  slug: cockroach-labs-privateendpoints-api
- description: List and inspect range information for the cluster, including hot ranges by node and detailed information for specific range IDs.
  name: Cockroach Labs Ranges API
  slug: cockroach-labs-ranges-api
- description: Manage role-based access control, including assigning and removing roles for users across organization, folder, and cluster scopes.
  name: Cockroach Labs RoleManagement API
  slug: cockroach-labs-rolemanagement-api
- description: Retrieve alerting rules templates for use with Prometheus-compatible alerting systems.
  name: Cockroach Labs Rules API
  slug: cockroach-labs-rules-api
- description: Manage service accounts used for machine-to-machine authentication within the organization.
  name: Cockroach Labs ServiceAccounts API
  slug: cockroach-labs-serviceaccounts-api
- description: List active SQL sessions across all nodes of the cluster, with optional filtering by username.
  name: Cockroach Labs Sessions API
  slug: cockroach-labs-sessions-api
- description: Manage SQL users for a cluster, including creating users, listing users, and updating SQL user passwords.
  name: Cockroach Labs SQLUsers API
  slug: cockroach-labs-sqlusers-api
- description: Manage cluster version deferral policies to delay automatic CockroachDB version upgrades.
  name: Cockroach Labs VersionDeferral API
  slug: cockroach-labs-versiondeferral-api
artifact_total: 90
collections:
- collection_type: postman
  name: CockroachDB Cloud APIKeys API
  slug: postman-cockroach-labs-apikeys-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys AuditLogs API
  slug: postman-cockroach-labs-auditlogs-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Auth API
  slug: postman-cockroach-labs-auth-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys BackupRestore API
  slug: postman-cockroach-labs-backuprestore-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Billing API
  slug: postman-cockroach-labs-billing-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Clusters API
  slug: postman-cockroach-labs-clusters-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys CMEK API
  slug: postman-cockroach-labs-cmek-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Databases API
  slug: postman-cockroach-labs-databases-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys EgressRules API
  slug: postman-cockroach-labs-egressrules-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Folders API
  slug: postman-cockroach-labs-folders-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Health API
  slug: postman-cockroach-labs-health-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys IPAllowlists API
  slug: postman-cockroach-labs-ipallowlists-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys JWTIssuers API
  slug: postman-cockroach-labs-jwtissuers-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys LogExport API
  slug: postman-cockroach-labs-logexport-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys MaintenanceWindows API
  slug: postman-cockroach-labs-maintenancewindows-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys MetricExport API
  slug: postman-cockroach-labs-metricexport-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Nodes API
  slug: postman-cockroach-labs-nodes-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Organizations API
  slug: postman-cockroach-labs-organizations-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys PrivateEndpoints API
  slug: postman-cockroach-labs-privateendpoints-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Ranges API
  slug: postman-cockroach-labs-ranges-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys RoleManagement API
  slug: postman-cockroach-labs-rolemanagement-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Rules API
  slug: postman-cockroach-labs-rules-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys ServiceAccounts API
  slug: postman-cockroach-labs-serviceaccounts-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys Sessions API
  slug: postman-cockroach-labs-sessions-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys SQLUsers API
  slug: postman-cockroach-labs-sqlusers-api
- collection_type: postman
  name: CockroachDB Cloud APIKeys VersionDeferral API
  slug: postman-cockroach-labs-versiondeferral-api
- collection_type: open
  name: CockroachDB Cloud API
  slug: open-cockroach-labs-cloud-api
- collection_type: open
  name: CockroachDB Cluster API
  slug: open-cockroach-labs-cluster-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/cockroach-labs/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cockroach-labs-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/cockroach-labs-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cockroach-labs-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cockroach-labs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cockroach-labs-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/cockroachlabs/cockroachdb-skills
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cockroach-labs
- group: company
  title: ''
  type: Website
  url: https://www.cockroachlabs.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.cockroachlabs.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cockroachlabs.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.cockroachlabs.com/blog/
- group: other
  title: ''
  type: Glossary
  url: https://www.cockroachlabs.com/docs/stable/architecture/glossary
- group: start
  title: ''
  type: Console
  url: https://cockroachlabs.cloud/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cockroachlabs.cloud/
- group: operate
  title: ''
  type: Support
  url: https://www.cockroachlabs.com/support/
- group: company
  title: ''
  type: Partners
  url: https://www.cockroachlabs.com/partners/
- group: auth
  title: ''
  type: Security
  url: https://www.cockroachlabs.com/security/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cockroachdb
- group: other
  title: ''
  type: TerraformProvider
  url: https://registry.terraform.io/providers/cockroachdb/cockroach/latest
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cockroachlabs.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cockroachlabs.com/cloud-terms-and-conditions/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/cockroach-labs-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cockroach-labs-cluster-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/cockroach-labs-rules.yml
created: '2024-11-24'
description: 'Cockroach Labs is the New York-based software company that builds CockroachDB, a cloud-native, distributed, PostgreSQL-compatible SQL database. CockroachDB is offered as Cockroach Labs'' fully managed cloud service (Basic, Standard, and Advanced plans) and as self-hosted software. The company provides two primary developer APIs: the CockroachDB Cloud API for managing the lifecycle of cloud-hosted clusters, and the CockroachDB Cluster API exposed by every node for cluster health, monitoring, and operational status. CockroachDB is used in production by banking, retail, gaming, and media companies including Bose, Hard Rock Digital, DoorDash, and Netflix.'
finops:
- name: Cockroach Labs Finops
  service_category: API
  slug: cockroach-labs-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cockroach-labs.png
json_schemas:
- name: CockroachDB Cluster
  property_count: 24
  slug: cockroach-labs-cluster
jsonld:
- class_count: 0
  name: Cockroach Labs Context
  property_count: 14
  slug: cockroach-labs-context
layout: provider
modified: '2026-05-19'
name: Cockroach Labs
nav: Providers
network: true
overview: 'Cockroach Labs publishes 26 APIs on the [APIs.io](https://apis.io/) network, including APIKeys API, AuditLogs API, Auth API, and 23 more. Tagged areas include Cluster Management, Cloud, Database, Distributed SQL, and Infrastructure.


  The Cockroach Labs catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Cockroach Labs'' developer surface includes authentication, documentation, pricing, engineering blog, developer console, support, GitHub presence, and 18 more developer resources.'
plans:
- name: Cockroach Labs Plans Pricing
  plan_count: 3
  slug: cockroach-labs-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Cockroach Labs Rate Limits
  slug: cockroach-labs-rate-limits
rules:
- name: Cockroach Labs API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: cockroach-labs-jsonschema-spectral-rules
- name: Cockroach Labs API Rules
  rule_count: 10
  severity_counts:
    error: 3
    hint: 0
    info: 3
    warn: 4
  slug: cockroach-labs-rules
score:
  band: strong
  composite: 62.9
  delta: -3.2
  facets:
    commercial_clarity: 78.9
    contract_quality: 68.4
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 63.2
  previous_composite: 66.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 26
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cockroach-labs/refs/heads/main/screenshots/cockroach-labs-2026-06-20T174648.png
security:
- kind: authentication
  name: Cockroach Labs Authentication
  slug: cockroach-labs-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Cockroach Labs Domain Security
  slug: cockroach-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cockroach Labs Vulnerability Disclosure
  slug: cockroach-labs-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Cockroach Labs Trust Center
  slug: cockroach-labs-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, FIPS 140
skill_count: 33
skills:
- name: analyzing-range-distribution
  slug: analyzing-range-distribution
- name: analyzing-schema-change-storage-risk
  slug: analyzing-schema-change-storage-risk
- name: auditing-cloud-cluster-security
  slug: auditing-cloud-cluster-security
- name: auditing-table-statistics
  slug: auditing-table-statistics
- name: benchmarking-transaction-patterns
  slug: benchmarking-transaction-patterns
- name: cockroachdb-sql
  slug: cockroachdb-sql
- name: configuring-audit-logging
  slug: configuring-audit-logging
- name: configuring-ip-allowlists
  slug: configuring-ip-allowlists
- name: configuring-log-export
  slug: configuring-log-export
- name: configuring-private-connectivity
  slug: configuring-private-connectivity
- name: configuring-sso-and-scim
  slug: configuring-sso-and-scim
- name: designing-application-transactions
  slug: designing-application-transactions
- name: designing-multi-region-applications
  slug: designing-multi-region-applications
- name: enabling-cmek-encryption
  slug: enabling-cmek-encryption
- name: enforcing-password-policies
  slug: enforcing-password-policies
- name: hardening-user-privileges
  slug: hardening-user-privileges
- name: managing-certificates-and-encryption
  slug: managing-certificates-and-encryption
- name: managing-cluster-capacity
  slug: managing-cluster-capacity
- name: managing-cluster-settings
  slug: managing-cluster-settings
- name: managing-tls-certificates
  slug: managing-tls-certificates
- name: molt-fetch
  slug: molt-fetch
- name: molt-replicator
  slug: molt-replicator
- name: molt-verify
  slug: molt-verify
- name: monitoring-background-jobs
  slug: monitoring-background-jobs
slug: cockroach-labs
tags:
- Cluster Management
- Cloud
- Database
- Distributed SQL
- Infrastructure
- PostgreSQL Compatible
- SQL
website: https://www.cockroachlabs.com/
---
