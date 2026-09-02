---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Oracle SQL Developer Web and SQLcl, the SQL surfaces through which partitions are actually created and maintained. Partition DDL — CREATE TABLE ... PARTITION BY, ALTER TABLE ... SPLIT/MERGE/EXCHANGE/D
  name: Oracle SQL Developer REST Services - Partitioning
  slug: oracle-sql-developer-rest-services-partitioning
- description: The Oracle Cloud Infrastructure Database API, which manages the DB systems, Autonomous Databases and Exadata infrastructure that host partitioned databases. It manages the database service, not indivi
  name: Oracle Cloud Infrastructure Database API - Partitioning
  slug: oracle-cloud-infrastructure-database-api-partitioning
- description: Services related to the tables and views that provide information about the database.
  name: Oracle Partitioning Data Dictionary API
  slug: oracle-partitioning-data-dictionary-api
- description: Services related to Oracle Data Guard. The product must be installed in the Oracle database that ORDS is configured to use.
  name: Oracle Partitioning Data Guard API
  slug: oracle-partitioning-data-guard-api
- description: Services related to Oracle Data Pump. Oracle Data Pump technology enables very high-speed movement of data and metadata from one database to another. Functionality may differ depending on the configur
  name: Oracle Partitioning Data Pump API
  slug: oracle-partitioning-data-pump-api
- description: Services related to loading, manipulating and analyzing data.
  name: Oracle Partitioning Data Tools API
  slug: oracle-partitioning-data-tools-api
- description: Services related to the Oracle database installation. The implementation is only available for Unix based operating systems.
  name: Oracle Partitioning Environment API
  slug: oracle-partitioning-environment-api
- description: Services related to the Oracle database instance.
  name: Oracle Partitioning General API
  slug: oracle-partitioning-general-api
- description: Services related to monitoring the Oracle database instance.
  name: Oracle Partitioning Monitoring API
  slug: oracle-partitioning-monitoring-api
- description: Services related to the Open Service Broker compliant implementation that ORDS provides.
  name: Oracle Partitioning Open Service Broker API
  slug: oracle-partitioning-open-service-broker-api
- description: Services related to Oracle APEX. The product must be installed in the Oracle database that ORDS is configured to use.
  name: Oracle Partitioning Oracle APEX API
  slug: oracle-partitioning-oracle-apex-api
- description: Services related to Oracle Transactional Event Queues.
  name: Oracle Partitioning Oracle Transactional Event Queues API
  slug: oracle-partitioning-oracle-transactional-event-queues-api
- description: Custom Oracle REST Data Services built with SQL & PL/SQL.
  name: Oracle Partitioning ORDS REST Services API
  slug: oracle-partitioning-ords-rest-services-api
- description: Services related to the runtime performance of the Oracle database instance.
  name: Oracle Partitioning Performance API
  slug: oracle-partitioning-performance-api
- description: Services related to managing pluggable databases in an Oracle multitenant database instance.
  name: Oracle Partitioning Pluggable Database Lifecycle Management API
  slug: oracle-partitioning-pluggable-database-lifecycle-management-api
- description: Services related to managing pluggable databases snapshots in an Oracle database instance.
  name: Oracle Partitioning Pluggable Database Snapshot Carousel API
  slug: oracle-partitioning-pluggable-database-snapshot-carousel-api
- description: Services related to Oracle RDF Graph. Oracle RDF Graph provides functionality to manage knowledge graphs based on World Wide Web Consortium (W3C) standards such as RDF, OWL and SPARQL.
  name: Oracle Partitioning RDF Graph API
  slug: oracle-partitioning-rdf-graph-api
- description: Oracle Scheduler, an enterprise job scheduler to help you simplify the scheduling of hundreds or even thousands of tasks. Oracle Scheduler (the Scheduler) is implemented by the procedures and function
  name: Oracle Partitioning Scheduler API
  slug: oracle-partitioning-scheduler-api
- description: The operations from the Vector Database/Inference Operations category.
  name: Oracle Partitioning Vector Database/Inference Operations API
  slug: oracle-partitioning-vector-database-inference-operations-api
- description: The operations from the Vector Database/Models category.
  name: Oracle Partitioning Vector Database/Models API
  slug: oracle-partitioning-vector-database-models-api
- description: The operations from the Vector Database/Summary category.
  name: Oracle Partitioning Vector Database/Summary API
  slug: oracle-partitioning-vector-database-summary-api
- description: The operations from the Vector Database/Vector Indexes category.
  name: Oracle Partitioning Vector Database/Vector Indexes API
  slug: oracle-partitioning-vector-database-vector-indexes-api
- description: The operations from the Vector Database/Vector Operations category.
  name: Oracle Partitioning Vector Database/Vector Operations API
  slug: oracle-partitioning-vector-database-vector-operations-api
- description: The operations from the Vector Database/Vector Search category.
  name: Oracle Partitioning Vector Database/Vector Search API
  slug: oracle-partitioning-vector-database-vector-search-api
- description: The operations from the Vector Database/Vector Tables category.
  name: Oracle Partitioning Vector Database/Vector Tables API
  slug: oracle-partitioning-vector-database-vector-tables-api
artifact_total: 33
common:
- group: company
  title: ''
  type: Website
  url: https://www.oracle.com/database/technologies/partitioning.html
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/oracle-partitioning-ords-database-api-openapi.json
- group: other
  title: ''
  type: Overlay
  url: overlays/oracle-partitioning-ords-database-api-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/oracle-partitioning-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/oracle-partitioning-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oracle-partitioning-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/oracle-partitioning-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/oracle-partitioning-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/oracle-partitioning-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/oracle-partitioning-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/oracle-partitioning-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/oracle-partitioning-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/oracle-partitioning-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/oracle-partitioning-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/oracle-partitioning-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/oracle-partitioning-changelog.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/oracle-partitioning-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://ocistatus.oraclecloud.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/oracle-partitioning-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/oracle-partitioning-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/oracle-partitioning-finops.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/oracle-partitioning-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/oracle-partitioning-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oracle-partitioning-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/oracle-partitioning-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.oracle.com/corporate/security-practices/assurance/vulnerability/
- group: auth
  title: ''
  type: Compliance
  url: https://www.oracle.com/corporate/cloud-compliance/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.oracle.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-concepts.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.oracle.com/en/database/oracle/oracle-rest-data-services/26.1/orrst/rest-endpoints.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.oracle.com/en/database/oracle/oracle-database/19/vldbg/partition-intro.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oracle
- group: other
  title: ''
  type: White Papers
  url: https://www.oracle.com/technetwork/database/options/partitioning/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oracle.com/a/ocom/docs/corporate/pricing/technology-price-list-070617.pdf
- group: start
  title: ''
  type: SignUp
  url: https://signup.cloud.oracle.com/
- group: operate
  title: ''
  type: Support
  url: https://support.oracle.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oracle.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oracle.com/legal/privacy/
created: '2024-01-01'
description: 'Oracle Partitioning is a licensed option of Oracle Database Enterprise Edition that divides large tables and indexes into smaller, independently manageable segments called partitions, accessed transparently through the table name. It delivers partition pruning (the optimizer eliminates irrelevant partitions from query plans), partition-wise parallel operations, and partition maintenance as atomic DDL — archiving or purging a partition instead of deleting rows. Strategies include range, interval, list, hash, reference, composite and auto-partitioning. It is not a standalone API product: partitions are CREATED and MAINTAINED through SQL DDL, and READ over REST through two Data Dictionary endpoints of the Oracle REST Data Services (ORDS) Database API, which is the machine-readable contract captured in this repository.'
finops:
- name: Oracle Partitioning Finops
  service_category: API
  slug: oracle-partitioning-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/oracle-partitioning.png
layout: provider
mcp_servers:
- description: Oracle publishes three first-party MCP servers for Oracle AI Database, all of which reach partitioned tables the same way a DBA does — by executing SQL against the database. There is no partitioning-s
  name: Oracle AI Database MCP Servers
  slug: oracle-ai-database-mcp-servers
modified: '2026-08-27'
name: Oracle Partitioning
nav: Providers
network: true
overview: 'Oracle Partitioning publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Data Dictionary API, Data Guard API, Data Pump API, and 20 more. Tagged areas include Agent Skills, Composite-Partitioning, Data Dictionary, Database, and Enterprise Edition Option.


  Oracle Partitioning''s developer surface includes CLI, sandbox, changelog, authentication, documentation, API reference, getting-started guide, and 32 more developer resources.'
plans:
- name: Oracle Partitioning Plans Pricing
  plan_count: 2
  slug: oracle-partitioning-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Oracle Partitioning Rate Limits
  slug: oracle-partitioning-rate-limits
scopes:
- name: Oracle Partitioning Scopes
  scope_count: 0
  slug: oracle-partitioning-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.1
  coverage:
    artifact_dirs: 22
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.5
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 4.5
    contract_quality: 42.1
    developer_ergonomics: 83.3
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 53.6
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/oracle-partitioning/refs/heads/main/screenshots/oracle-partitioning-2026-06-20T191138.png
security:
- kind: authentication
  name: Oracle Partitioning Authentication
  slug: oracle-partitioning-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Oracle Partitioning Domain Security
  slug: oracle-partitioning-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Oracle Partitioning Vulnerability Disclosure
  slug: oracle-partitioning-vulnerability-disclosure
  summary_line: Hackerone
slug: oracle-partitioning
tags:
- Agent Skills
- Composite-Partitioning
- Data Dictionary
- Database
- Enterprise Edition Option
- Hash-Partitioning
- Interval-Partitioning
- List-Partitioning
- MCP
- ORDS
- Oracle
- Oracle Database
- Partitioning
- Performance
- Range-Partitioning
- SQL
- Scalability
- Table Partitioning
- VLDB
website: https://www.oracle.com/database/technologies/partitioning.html
---
