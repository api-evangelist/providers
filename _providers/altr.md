---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 68.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 190
  human_in_the_loop: 10
  name: Altr Agentic Access
  operation_count: 375
  slug: altr-agentic-access
  summary_line: 375 operations · 190 acting · 10 human-in-the-loop
api_count: 24
apis:
- description: Core ALTR platform configuration API — data sources, databases, policies, users, roles, tags, tokenization settings, and account preferences. The largest of ALTR's public surfaces and the API the ALTR
  name: ALTR Management API (MAPI)
  slug: altr-management-api-mapi
- description: Single API for creating and managing ALTR policies across every policy type (tag-based masking, column-based masking, access management, tokenization) and every supported platform.
  name: Unified Policy API
  slug: unified-policy-api
- description: Creates and revokes grants on roles inside a Snowflake database, giving programmatic control of role-based access to governed objects.
  name: RBAC API
  slug: rbac-api
- description: Manages classifiers, classifier collections, and classification jobs across Snowflake, Databricks and OLTP sources — including GDLP scans, findings-tree navigation, match confidence, and human-in-the-
  name: ALTR Classification Engine API
  slug: altr-classification-engine-api
- description: Applies Snowflake object tags automatically from ALTR classification results so masking policies bind to newly discovered sensitive columns without manual tagging.
  name: Auto Tagging API
  slug: auto-tagging-api
- description: Connects Snowflake tags to ALTR and manages the tag-based masking policies and per-role masking rules applied to tagged columns.
  name: Tag Masking API
  slug: tag-masking-api
- description: Refreshes the tag values ALTR holds for a connected Snowflake account so policy evaluation stays in sync with tag changes made in the warehouse.
  name: Snowflake Tag Value Refresh API
  slug: snowflake-tag-value-refresh-api
- description: Alpha API for registering a Databricks service principal and workspace with ALTR and applying tag-based governance policy pushdown to a Databricks metastore.
  name: Tag-based Governance Policy on Databricks (alpha)
  slug: tag-based-governance-policy-on-databricks-alpha
- description: Reads structural metadata about connected datastores — databases, schemas, tables and columns — so classification and policy tooling can navigate a data source's shape.
  name: ALTR Datastore Information Service (DIS)
  slug: altr-datastore-information-service-dis
- description: Retrieves Snowflake account metadata — databases, schemas, tables, columns, roles and warehouses — that ALTR uses to scope classification and policy.
  name: Snowflake Metadata API
  slug: snowflake-metadata-api
- description: Retrieves query audit records captured by ALTR's database activity monitoring for governed Snowflake queries.
  name: Query Audits API
  slug: query-audits-api
- description: Serves the aggregated query-activity views behind ALTR's database activity monitoring dashboard.
  name: Query Dashboard API
  slug: query-dashboard-api
- description: Manages database-activity-monitoring alert rules, triggered alerts, and alert acknowledgement.
  name: DAM Alerting API
  slug: dam-alerting-api
- description: Creates, schedules and reviews structured audit report definitions and instances — including download URLs, comments, and review sign-offs — for compliance artifacts in PDF and CSV.
  name: ALTR Audit Report API
  slug: altr-audit-report-api
- description: Manages the notification delivery channels ALTR routes alerts and platform events through.
  name: ALTR Notification Integration API
  slug: altr-notification-integration-api
- description: Tokenizes, detokenizes, partially detokenizes and deletes values through ALTR's PCI-compliant critical tokenization service.
  name: Critical Tokenization API
  slug: critical-tokenization-api
- description: Configures the ALTR sidecar proxy estate — agents, agent tasks, repositories, repo users, service users, sidecars, listeners and bindings — for OLTP data sources such as PostgreSQL, MySQL, SQL Server,
  name: ALTR Sidecar/Agent Configuration API
  slug: altr-sidecaragent-configuration-api
- description: Searches the audit records the ALTR sidecar proxy captures for governed OLTP database traffic.
  name: Sidecar Audit API
  slug: sidecar-audit-api
- description: Reports health and telemetry for ALTR sidecar proxy agents and sidecar instances.
  name: ALTR Telemetry API
  slug: altr-telemetry-api
- description: Issues the short-lived access tokens ALTR sidecar components use to authenticate to the sidecar control plane.
  name: Access Tokens API
  slug: access-tokens-api
- description: Manages the service users ALTR uses to connect to and act on governed data sources.
  name: Service User Service API
  slug: service-user-service-api
- description: Tokenizes and detokenizes sensitive data through ALTR's token vault for analytics and transactional workloads, including bring-your-own-key. The public reference endpoint returns HTTP 403 to anonymous
  name: Vaulted Tokenization API
  slug: vaulted-tokenization-api
- description: Manages the keys and tweaks used for ALTR Format-Preserving Encryption (FPE). The reference is served per organization at https://<organization-id>.kma.live.altr.com/v1/docs, so no anonymous machine-r
  name: Key Management API (KMA)
  slug: key-management-api-kma
- description: Official open-source Model Context Protocol server published by ALTR, exposing 156 tools across 13 domains (databases, tags, policies, classification, access management, access requests, audits, audit
  name: ALTR MCP Server
  slug: altr-mcp-server
artifact_total: 31
asyncapis:
- description: ''
  name: Altr Events Webhooks
  slug: altr-events-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/altr-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/altr-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/altr-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://altr.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.altr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.altr.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.altr.com/account-and-api/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.altr.com/account-and-api/creating-an-altr-account/
- group: operate
  title: ''
  type: Support
  url: https://docs.altr.com/support/
- group: company
  title: ''
  type: Blog
  url: https://altr.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/altrsoftware
- group: commercial
  title: ''
  type: Pricing
  url: https://altr.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://altrnet.live.altr.com/api/auth/organization_register
- group: start
  title: ''
  type: Login
  url: https://altrnet.live.altr.com/?source=altr
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altr.com/info/altr-solutions-inc-terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altr.com/privacy-policy-2/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.altr.com/en/what-s-new.html
- group: build
  title: ''
  type: Packages
  url: packages/altr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/altr-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/altr-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/altr-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/altr-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/altr-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/altr-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.altr.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/altr-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/altr-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/altr-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/altr-conventions.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/altr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://trust.altr.com/
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/altr-events-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/altr-data-model.yml
- group: build
  title: ''
  type: CLI
  url: cli/altr-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/altr-changelog.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/altrsoftware
created: '2026-08-06'
description: ALTR is a unified data security platform that discovers, classifies, masks, tokenizes and monitors sensitive data across Snowflake, Databricks and OLTP databases (PostgreSQL, MySQL, SQL Server, Oracle, MongoDB). The platform combines automated data classification, tag-based and column-based dynamic data masking, role-based access control, access-approval workflows, database activity monitoring with alerting, format-preserving encryption, and both vaulted and PCI-scoped critical tokenization. Everything the console does is exposed through a large public REST surface — a Management API plus purpose-built classification, policy, RBAC, tagging, audit, telemetry and sidecar-configuration services — alongside an official open-source MCP server, a Terraform provider and a Node.js Shield SDK. Founded in 2018 and headquartered in Austin, Texas.
image: https://altr.com/wp-content/uploads/2025/05/Home-1.png
layout: provider
mcp_servers:
- description: ''
  name: altr-mcp.yml
  slug: altr-mcpyml
modified: '2026-08-06'
name: ALTR
nav: Providers
network: true
overview: 'ALTR publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Management API (MAPI), Unified Policy API, RBAC API, and 18 more. Tagged areas include data-security, data-governance, data-masking, tokenization, and data-classification.


  The ALTR catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ALTR''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 30 more developer resources.'
random_paper: 96
score:
  band: strong
  composite: 61.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 65.7
    developer_ergonomics: 80.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 39.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Altr Authentication
  slug: altr-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Altr Domain Security
  slug: altr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Altr Vulnerability Disclosure
  slug: altr-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Altr Trust Center
  slug: altr-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: altr
tags:
- data-security
- data-governance
- data-masking
- tokenization
- data-classification
- access-control
- snowflake
- databricks
- format-preserving-encryption
- database-activity-monitoring
- rbac
- pii
- compliance
- data-privacy
- mcp
- agent-native
website: https://altr.com/
---
