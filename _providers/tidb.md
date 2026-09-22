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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.2
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Tidb Agentic Access
  operation_count: 74
  slug: tidb-agentic-access
  summary_line: 74 operations · 32 acting · 1 human-in-the-loop
api_count: 12
apis:
- baseURL: https://iam.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Operations for creating, listing, updating, and deleting TiDB Cloud API keys.
  name: tidb API Keys API
  slug: tidb-api-keys-api
- baseURL: https://iam.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Operations for retrieving organization-level console audit logs.
  name: tidb Audit Logs API
  slug: tidb-audit-logs-api
- baseURL: https://billing.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Operations for retrieving monthly billing summaries, cost details, and usage trends.
  name: tidb Billing API
  slug: tidb-billing-api
- baseURL: https://data.tidbcloud.com/api/v1beta/app/{dataAppId}/endpoint
  baseurl_source: declared
  description: Operations for translating natural language questions into SQL and executing them against TiDB Cloud clusters.
  name: tidb Chat2Data API
  slug: tidb-chat2data-api
- baseURL: https://dedicated.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Operations for creating, listing, updating, and deleting TiDB Cloud Dedicated clusters.
  name: tidb Clusters API
  slug: tidb-clusters-api
- baseURL: https://dataservice.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Operations for managing API keys scoped to a specific Data App.
  name: tidb Data App API Keys API
  slug: tidb-data-app-api-keys-api
- baseURL: https://dataservice.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Operations for creating, listing, updating, and deleting Data Apps.
  name: tidb Data Apps API
  slug: tidb-data-apps-api
- baseURL: https://dataservice.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Operations for linking and managing TiDB Cloud clusters as data sources within a Data App.
  name: tidb Data Sources API
  slug: tidb-data-sources-api
- baseURL: https://data.tidbcloud.com/api/v1beta/app/{dataAppId}/endpoint
  baseurl_source: declared
  description: Operations for generating and managing AI summaries of database schemas used as context for SQL generation.
  name: tidb Data Summaries API
  slug: tidb-data-summaries-api
- baseURL: http://{tidb-host}:10080
  baseurl_source: declared
  description: Endpoints for managing and inspecting DDL jobs, including ownership and history.
  name: tidb DDL API
  slug: tidb-ddl-api
- baseURL: https://dataservice.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Operations for deploying and managing versions of a Data App.
  name: tidb Deployments API
  slug: tidb-deployments-api
- baseURL: http://{tidb-host}:10080
  baseurl_source: declared
  description: Endpoints for downloading debug information and managing server diagnostics.
  name: tidb Diagnostics API
  slug: tidb-diagnostics-api
- baseURL: https://dataservice.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Operations for creating, listing, updating, testing, and deleting custom SQL-backed API endpoints.
  name: tidb Endpoints API
  slug: tidb-endpoints-api
- baseURL: https://dedicated.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Operations for creating and managing data import tasks into TiDB Cloud clusters.
  name: tidb Imports API
  slug: tidb-imports-api
- baseURL: https://dedicated.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Operations for managing third-party integrations with TiDB Cloud clusters.
  name: tidb Integrations API
  slug: tidb-integrations-api
- baseURL: http://{tidb-host}:10080
  baseurl_source: declared
  description: Endpoints for retrieving multi-version concurrency control (MVCC) key details for debugging.
  name: tidb MVCC API
  slug: tidb-mvcc-api
- baseURL: https://dedicated.tidbapi.com/v1beta1
  baseurl_source: declared
  description: Operations for listing available cloud regions and node specifications.
  name: tidb Regions API
  slug: tidb-regions-api
- baseURL: http://{tidb-host}:10080
  baseurl_source: declared
  description: Endpoints for retrieving database and table schema information from the TiDB information schema.
  name: tidb Schema API
  slug: tidb-schema-api
- baseURL: https://data.tidbcloud.com/api/v1beta/app/{dataAppId}/endpoint
  baseurl_source: declared
  description: Operations for creating and managing multi-round conversational chat sessions.
  name: tidb Sessions API
  slug: tidb-sessions-api
- baseURL: http://{tidb-host}:10080
  baseurl_source: declared
  description: Endpoints for retrieving and modifying TiDB server runtime settings.
  name: tidb Settings API
  slug: tidb-settings-api
- baseURL: https://data.tidbcloud.com/api/v1beta/app/{dataAppId}/endpoint
  baseurl_source: declared
  description: Operations for refining and improving previously generated SQL queries.
  name: tidb SQL Refinement API
  slug: tidb-sql-refinement-api
- baseURL: http://{tidb-host}:10080
  baseurl_source: declared
  description: Endpoints for exporting optimizer statistics used for query planning.
  name: tidb Statistics API
  slug: tidb-statistics-api
- baseURL: http://{tidb-host}:10080
  baseurl_source: declared
  description: Endpoints for retrieving the operational status of the TiDB server instance.
  name: tidb Status API
  slug: tidb-status-api
- baseURL: https://dedicated.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The published Swagger 2.0 contract for managing TiDB Cloud Dedicated clusters — clusters, TiDB node groups, regions and node specs, private endpoint connections, data imports, observability integratio
  name: TiDB Cloud Dedicated API
  slug: tidb-cloud-dedicated-api
- baseURL: https://serverless.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The published Swagger 2.0 contract for managing TiDB Cloud Starter and Essential instances — instances, data branches, export tasks and import tasks, plus the region list. 20 operations, harvested ver
  name: TiDB Cloud Starter and Essential API
  slug: tidb-cloud-starter-essential-api
- baseURL: https://cloud.tidbapi.com/v1beta2
  baseurl_source: declared
  description: The published Swagger 2.0 contract for TiDB Cloud Premium, the v1beta2 API — Premium instance lifecycle and configuration, root passwords, CA certificates, cloud provider information, backups and back
  name: TiDB Cloud Premium API
  slug: tidb-cloud-premium-api
- baseURL: https://dataservice.tidbapi.com
  baseurl_source: declared
  description: The published Swagger 2.0 contract for TiDB Cloud Data Service — create Data Apps, link clusters as data sources, define and test custom REST endpoints backed by SQL templates, deploy them, manage the
  name: TiDB Cloud Data Service API
  slug: tidb-cloud-data-service-api
- baseURL: https://iam.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The published Swagger 2.0 contract for TiDB Cloud identity and access management — organization API keys, organization members and invitations, and console audit logs. 12 operations, harvested verbati
  name: TiDB Cloud IAM API
  slug: tidb-cloud-iam-api
- baseURL: https://billing.tidbapi.com/v1beta1
  baseurl_source: declared
  description: The published Swagger 2.0 contract for TiDB Cloud billing — monthly bills, monthly bill details and the cost explorer, addressed by billed month. 4 operations, harvested verbatim from PingCAP. None of
  name: TiDB Cloud Billing API
  slug: tidb-cloud-billing-api
- baseURL: https://msp.tidbapi.com/v1beta1/msp
  baseurl_source: declared
  description: The published Swagger 2.0 contract for the TiDB Cloud Managed Service Provider surface, which PingCAP marks as deprecated in its own v1beta1 overview. Recorded because it is still served and still doc
  name: TiDB Cloud MSP API
  slug: tidb-cloud-msp-api
- baseURL: https://api.tidbcloud.com
  baseurl_source: declared
  description: The original TiDB Cloud management API, still served at api.tidbcloud.com and still the only surface that exposes projects — projects, clusters, backups, restores and the deprecated import operations.
  name: TiDB Cloud API v1beta
  slug: tidb-cloud-api-v1beta
artifact_total: 78
asyncapis:
- description: ''
  name: Tidb Webhooks
  slug: tidb-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TiDB Cloud API Keys API
  slug: open-tidb-api-keys-api
- collection_type: open
  name: TiDB Cloud API Keys Audit Logs API
  slug: open-tidb-audit-logs-api
- collection_type: open
  name: TiDB Cloud API Keys Billing API
  slug: open-tidb-billing-api
- collection_type: open
  name: TiDB Cloud API Keys Chat2Data API
  slug: open-tidb-chat2data-api
- collection_type: open
  name: TiDB Cloud API
  slug: open-tidb-cloud-api
- collection_type: open
  name: TiDB Cloud Chat2Query API
  slug: open-tidb-cloud-chat2query
- collection_type: open
  name: TiDB Cloud Data Service API
  slug: open-tidb-cloud-data-service
- collection_type: open
  name: TiDB Cloud API Keys Clusters API
  slug: open-tidb-clusters-api
- collection_type: open
  name: TiDB Cloud API Keys Data App API Keys API
  slug: open-tidb-data-app-api-keys-api
- collection_type: open
  name: TiDB Cloud API Keys Data Apps API
  slug: open-tidb-data-apps-api
- collection_type: open
  name: TiDB Cloud API Keys Data Sources API
  slug: open-tidb-data-sources-api
- collection_type: open
  name: TiDB Cloud API Keys Data Summaries API
  slug: open-tidb-data-summaries-api
- collection_type: open
  name: TiDB Cloud API Keys DDL API
  slug: open-tidb-ddl-api
- collection_type: open
  name: TiDB Cloud API Keys Deployments API
  slug: open-tidb-deployments-api
- collection_type: open
  name: TiDB Cloud API Keys Diagnostics API
  slug: open-tidb-diagnostics-api
- collection_type: open
  name: TiDB Cloud API Keys Endpoints API
  slug: open-tidb-endpoints-api
- collection_type: open
  name: TiDB HTTP API
  slug: open-tidb-http-api
- collection_type: open
  name: TiDB Cloud API Keys Imports API
  slug: open-tidb-imports-api
- collection_type: open
  name: TiDB Cloud API Keys Integrations API
  slug: open-tidb-integrations-api
- collection_type: open
  name: TiDB Cloud API Keys MVCC API
  slug: open-tidb-mvcc-api
- collection_type: open
  name: TiDB Cloud API Keys Regions API
  slug: open-tidb-regions-api
- collection_type: open
  name: TiDB Cloud API Keys Schema API
  slug: open-tidb-schema-api
- collection_type: open
  name: TiDB Cloud API Keys Sessions API
  slug: open-tidb-sessions-api
- collection_type: open
  name: TiDB Cloud API Keys Settings API
  slug: open-tidb-settings-api
- collection_type: open
  name: TiDB Cloud API Keys SQL Refinement API
  slug: open-tidb-sql-refinement-api
- collection_type: open
  name: TiDB Cloud API Keys Statistics API
  slug: open-tidb-statistics-api
- collection_type: open
  name: TiDB Cloud API Keys Status API
  slug: open-tidb-status-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/agentic-access/tidb-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tidb-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/security/tidb-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tidb-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/authentication/tidb-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tidb-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pingcap
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/json-ld/tidb-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tidb-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/json-schema/tidb-cluster-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/tidb-cluster-schema.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/json-schema/tidb-data-service-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/tidb-data-service-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/rules/tidb-rules.yml
  title: ''
  type: Spectral
  url: rules/tidb-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/vocabulary/tidb-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tidb-vocabulary.yml
- group: company
  title: ''
  type: Website
  url: https://www.pingcap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.pingcap.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pingcap.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.pingcap.com/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pingcap.com/tidbcloud/tidb-cloud-quickstart/
- group: operate
  title: ''
  type: Support
  url: https://docs.pingcap.com/tidbcloud/tidb-cloud-support/
- group: company
  title: ''
  type: Blog
  url: https://www.pingcap.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pingcap
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/pingcap/tidb/blob/master/roadmap.md
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pingcap.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://tidbcloud.com/free-trial
- group: start
  title: ''
  type: Login
  url: https://tidbcloud.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pingcap.com/legal/tidb-cloud-services-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pingcap.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tidbcloud.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://www.pingcap.com/tidb-release-support-policy/
- group: operate
  title: ''
  type: SLA
  url: https://www.pingcap.com/legal/service-level-agreement-for-tidb-cloud-services/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.pingcap.com/tidbcloud/tidb-cloud-release-notes/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/changelog/tidb-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tidb-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/lifecycle/tidb-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tidb-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/security/tidb-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tidb-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/security/tidb-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tidb-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/security/tidb-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tidb-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/security/tidb-trust-center.yml
  title: ''
  type: Compliance
  url: security/tidb-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/conformance/tidb-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tidb-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/packages/tidb-packages.yml
  title: ''
  type: Packages
  url: packages/tidb-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/packages/tidb-packages.yml
  title: ''
  type: SDKs
  url: packages/tidb-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/cli/tidb-cli.yml
  title: ''
  type: CLI
  url: cli/tidb-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/mcp/tidb-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tidb-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/mcp/tidb-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tidb-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/llms/tidb-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tidb-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.pingcap.com/llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/conventions/tidb-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tidb-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/errors/tidb-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tidb-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/data-model/tidb-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tidb-data-model.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/sandbox/tidb-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/tidb-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/asyncapi/tidb-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tidb-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/rate-limits/tidb-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tidb-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/plans/tidb-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tidb-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/finops/tidb-finops.yml
  title: ''
  type: FinOps
  url: finops/tidb-finops.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/examples/tidb-cloud-api-list-clusters-example.json
  title: ''
  type: Examples
  url: examples/tidb-cloud-api-list-clusters-example.json
created: '2026-05-04'
description: TiDB is an open-source, MySQL-compatible distributed SQL database built by PingCAP for Hybrid Transactional and Analytical Processing (HTAP) workloads, with horizontal scale-out, Raft-based strong consistency, high availability and built-in vector search for AI retrieval. It ships both as self-managed open source and as TiDB Cloud, the managed service, whose control plane is published as eight Swagger 2.0 contracts across Starter, Essential, Dedicated and Premium tiers plus Data Service, IAM and billing.
examples:
- key_count: 2
  name: Tidb Cloud Api List Clusters Example
  slug: tidb-cloud-api-list-clusters-example
- key_count: 2
  name: Tidb Cloud Chat2Query Example
  slug: tidb-cloud-chat2query-example
- key_count: 2
  name: Tidb Http Api Get Status Example
  slug: tidb-http-api-get-status-example
finops:
- name: Tidb Finops
  service_category: Database
  slug: tidb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tidb.png
json_schemas:
- name: TiDB Cloud Cluster
  property_count: 14
  slug: tidb-cluster
- name: TiDB Cloud Data Service
  property_count: 6
  slug: tidb-data-service
json_structures:
- name: Tidb Cluster Structure
  property_count: 0
  slug: tidb-cluster-structure
jsonld:
- class_count: 0
  name: Tidb Context
  property_count: 16
  slug: tidb-context
layout: provider
mcp_servers:
- description: ''
  name: Tidb MCP Server
  slug: tidb-mcp-server
modified: '2026-09-17'
name: Tidb
nav: Providers
network: true
overview: 'Tidb publishes 31 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Audit Logs API, Billing API, and 28 more. Tagged areas include Database, Distributed SQL, HTAP, Cloud, and Open-Source.


  The Tidb catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Tidb''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 44 more developer resources.'
plans:
- name: Tidb Plans Pricing
  plan_count: 6
  slug: tidb-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 6
  name: Tidb Rate Limits
  slug: tidb-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Tidb API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: tidb-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Tidb API Rules
  rule_count: 11
  severity_counts:
    error: 4
    hint: 0
    info: 4
    warn: 3
  slug: tidb-rules
score:
  band: exemplar
  composite: 78.4
  coverage:
    artifact_dirs: 32
    catalog_earned: 91.5
    catalog_earned_first_party: 24.0
    catalog_gap: 23.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.6
  facets:
    access_clarity: 93.4
    contract_governance: 33.3
    contract_quality: 80.2
    developer_ergonomics: 80.4
    discoverability: 75.9
    operational_transparency: 97.4
  previous_composite: 74.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/tidb/refs/heads/main/screenshots/tidb-2026-06-20T195336.png
security:
- kind: authentication
  name: Tidb Authentication
  slug: tidb-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tidb Domain Security
  slug: tidb-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Tidb Vulnerability Disclosure
  slug: tidb-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Tidb Trust Center
  slug: tidb-trust-center
  summary_line: SOC 2, PCI DSS, ISO/IEC 27001, ISO/IEC 27701, HIPAA
slug: tidb
tags:
- Database
- Distributed SQL
- HTAP
- Cloud
- Open-Source
- Vector Search
- Data Infrastructure
- Database-as-a-Service
- MySQL Compatible
- Artificial Intelligence
website: https://www.pingcap.com/
---
