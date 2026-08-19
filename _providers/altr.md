---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 47.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 190
  human_in_the_loop: 10
  name: Altr Agentic Access
  operation_count: 375
  slug: altr-agentic-access
  summary_line: 375 operations · 190 acting · 10 human-in-the-loop
api_count: 69
apis:
- description: Tokenizes and detokenizes sensitive data through ALTR's token vault for analytics and transactional workloads, including bring-your-own-key. The public reference endpoint returns HTTP 403 to anonymous
  name: Vaulted Tokenization API
  slug: vaulted-tokenization-api
- description: Manages the keys and tweaks used for ALTR Format-Preserving Encryption (FPE). The reference is served per organization at https://<organization-id>.kma.live.altr.com/v1/docs, so no anonymous machine-r
  name: Key Management API (KMA)
  slug: key-management-api-kma
- description: Official open-source Model Context Protocol server published by ALTR, exposing 156 tools across 13 domains (databases, tags, policies, classification, access management, access requests, audits, audit
  name: ALTR MCP Server
  slug: altr-mcp-server
- description: The access_request API from ALTR — 5 operation(s) for access_request.
  name: ALTR Access Request API
  slug: altr-access-request-api
- description: Operations about administrators
  name: ALTR Administrators API
  slug: altr-administrators-api
- description: The Agent API from ALTR — 2 operation(s) for agent.
  name: ALTR Agent API
  slug: altr-agent-api
- description: The Agent Tasks API from ALTR — 2 operation(s) for agent tasks.
  name: ALTR Agent Tasks API
  slug: altr-agent-tasks-api
- description: The Agents API from ALTR — 2 operation(s) for agents.
  name: ALTR Agents API
  slug: altr-agents-api
- description: The Alerts API from ALTR — 4 operation(s) for alerts.
  name: ALTR Alerts API
  slug: altr-alerts-api
- description: The ALTR Managed Collections API from ALTR — 8 operation(s) for altr managed collections.
  name: ALTR ALTR Managed Collections API
  slug: altr-altr-managed-collections-api
- description: Operations about anomalies
  name: ALTR Anomalies API
  slug: altr-anomalies-api
- description: Operations about ApiKeys
  name: ALTR Apikeys API
  slug: altr-apikeys-api
- description: Operations about applications
  name: ALTR Applications API
  slug: altr-applications-api
- description: The Auth API from ALTR — 3 operation(s) for auth.
  name: ALTR Auth API
  slug: altr-auth-api
- description: The Auto Tagging API API from ALTR — 10 operation(s) for auto tagging api.
  name: ALTR Auto Tagging API API
  slug: altr-auto-tagging-api-api
- description: The batch API from ALTR — 3 operation(s) for batch.
  name: ALTR Batch API
  slug: altr-batch-api
- description: Operations about data classification
  name: ALTR Classification API
  slug: altr-classification-api
- description: The Classification Jobs API from ALTR — 21 operation(s) for classification jobs.
  name: ALTR Classification Jobs API
  slug: altr-classification-jobs-api
- description: The Classifiers API from ALTR — 5 operation(s) for classifiers.
  name: ALTR Classifiers API
  slug: altr-classifiers-api
- description: The Collections API from ALTR — 5 operation(s) for collections.
  name: ALTR Collections API
  slug: altr-collections-api
- description: The Comments API from ALTR — 3 operation(s) for comments.
  name: ALTR Comments API
  slug: altr-comments-api
- description: Configuration information for the ALTRNet
  name: ALTR Configuration API
  slug: altr-configuration-api
- description: The Control Plane API from ALTR — 1 operation(s) for control plane.
  name: ALTR Control Plane API
  slug: altr-control-plane-api
- description: Protected, Governed, Tokenized, and FPE Columns Endpoints
  name: ALTR Data API
  slug: altr-data-api
- description: Data Classification/Tagging job endpoints
  name: ALTR Data Discovery API
  slug: altr-data-discovery-api
- description: Access to column info around available masking types
  name: ALTR Data Masking API
  slug: altr-data-masking-api
- description: Information around tagged columns
  name: ALTR Data Tagging API
  slug: altr-data-tagging-api
- description: Operations about data sources
  name: ALTR Databases API
  slug: altr-databases-api
- description: Operations related to applying tag-based governance policies to Databricks
  name: ALTR Databricks Tag Policy API
  slug: altr-databricks-tag-policy-api
- description: The Definitions API from ALTR — 4 operation(s) for definitions.
  name: ALTR Definitions API
  slug: altr-definitions-api
- description: The Instances API from ALTR — 3 operation(s) for instances.
  name: ALTR Instances API
  slug: altr-instances-api
- description: The Integrations API from ALTR — 3 operation(s) for integrations.
  name: ALTR Integrations API
  slug: altr-integrations-api
- description: Operations related to masking policies
  name: ALTR Maskingpolicies API
  slug: altr-maskingpolicies-api
- description: Operations related to the currently logged in administrator
  name: ALTR Me API
  slug: altr-me-api
- description: Operations related to the currently logged in users metadata and current organizations metadata.
  name: ALTR Metadata API
  slug: altr-metadata-api
- description: Operations about organization
  name: ALTR Organization API
  slug: altr-organization-api
- description: Operations related to the features the organization has
  name: ALTR Plan API
  slug: altr-plan-api
- description: The policy API from ALTR — 13 operation(s) for policy.
  name: ALTR Policy API
  slug: altr-policy-api
- description: The Query Audits API API from ALTR — 2 operation(s) for query audits api.
  name: ALTR Query Audits API API
  slug: altr-query-audits-api-api
- description: The Query Dashboard API API from ALTR — 2 operation(s) for query dashboard api.
  name: ALTR Query Dashboard API API
  slug: altr-query-dashboard-api-api
- description: The RBAC API API from ALTR — 11 operation(s) for rbac api.
  name: ALTR RBAC API API
  slug: altr-rbac-api-api
- description: The Refresh Tag Value Job API from ALTR — 2 operation(s) for refresh tag value job.
  name: ALTR Refresh Tag Value Job API
  slug: altr-refresh-tag-value-job-api
- description: The Repo Users API from ALTR — 2 operation(s) for repo users.
  name: ALTR Repo Users API
  slug: altr-repo-users-api
- description: The Repos API from ALTR — 2 operation(s) for repos.
  name: ALTR Repos API
  slug: altr-repos-api
- description: Operations related to row access policy
  name: ALTR Rowaccess API
  slug: altr-rowaccess-api
- description: The Rules API from ALTR — 6 operation(s) for rules.
  name: ALTR Rules API
  slug: altr-rules-api
- description: Operations related to SCIM
  name: ALTR SCIM API
  slug: altr-scim-api
- description: The Service Users API from ALTR — 3 operation(s) for service users.
  name: ALTR Service Users API
  slug: altr-service-users-api
- description: Operations about the setup-guide
  name: ALTR Setup Guide API
  slug: altr-setup-guide-api
- description: The Sidecar API from ALTR — 2 operation(s) for sidecar.
  name: ALTR Sidecar API
  slug: altr-sidecar-api
- description: The Sidecar Audit API API from ALTR — 2 operation(s) for sidecar audit api.
  name: ALTR Sidecar Audit API API
  slug: altr-sidecar-audit-api-api
- description: The Sidecar Listener Port and Repo bindings API from ALTR — 3 operation(s) for sidecar listener port and repo bindings.
  name: ALTR Sidecar Listener Port and Repo bindings API
  slug: altr-sidecar-listener-port-and-repo-bindings-api
- description: The Sidecar Listeners API from ALTR — 2 operation(s) for sidecar listeners.
  name: ALTR Sidecar Listeners API
  slug: altr-sidecar-listeners-api
- description: The Sidecars API from ALTR — 2 operation(s) for sidecars.
  name: ALTR Sidecars API
  slug: altr-sidecars-api
- description: The Sign-Off API from ALTR — 2 operation(s) for sign-off.
  name: ALTR Sign Off API
  slug: altr-sign-off-api
- description: The Snowflake Metadata API API from ALTR — 13 operation(s) for snowflake metadata api.
  name: ALTR Snowflake Metadata API API
  slug: altr-snowflake-metadata-api-api
- description: Operations related to Single Sign-On
  name: ALTR SSO API
  slug: altr-sso-api
- description: The Subscriptions API from ALTR — 3 operation(s) for subscriptions.
  name: ALTR Subscriptions API
  slug: altr-subscriptions-api
- description: Operations related to system audits
  name: ALTR Systemaudits API
  slug: altr-systemaudits-api
- description: Operations related to asynchronously querying system audits
  name: ALTR Systemaudits/query API
  slug: altr-systemaudits-query-api
- description: The Tag Masking API API from ALTR — 3 operation(s) for tag masking api.
  name: ALTR Tag Masking API API
  slug: altr-tag-masking-api-api
- description: Operations related to tags
  name: ALTR Tags API
  slug: altr-tags-api
- description: The Task API from ALTR — 2 operation(s) for task.
  name: ALTR Task API
  slug: altr-task-api
- description: The Tasks API from ALTR — 3 operation(s) for tasks.
  name: ALTR Tasks API
  slug: altr-tasks-api
- description: Operations about thresholds
  name: ALTR Thresholds API
  slug: altr-thresholds-api
- description: The Unsubscribe API from ALTR — 1 operation(s) for unsubscribe.
  name: ALTR Unsubscribe API
  slug: altr-unsubscribe-api
- description: Operations related to user groups
  name: ALTR Usergroups API
  slug: altr-usergroups-api
- description: The Users API from ALTR — 3 operation(s) for users.
  name: ALTR Users API
  slug: altr-users-api
- description: Access DIS job and third party import information.
  name: ALTR Utility API
  slug: altr-utility-api
artifact_total: 143
asyncapis:
- description: ''
  name: Altr Events Webhooks
  slug: altr-events-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Unified Policy Access Request API
  slug: open-altr-access-request-api
- collection_type: open
  name: ALTR Management Administrators API
  slug: open-altr-administrators-api
- collection_type: open
  name: ALTR Telemetry Agent API
  slug: open-altr-agent-api
- collection_type: open
  name: ALTR Sidecar/Agent Configuration Agent Tasks API
  slug: open-altr-agent-tasks-api
- collection_type: open
  name: ALTR Sidecar/Agent Configuration Agents API
  slug: open-altr-agents-api
- collection_type: open
  name: ALTR DAM Alerting Alerts API
  slug: open-altr-alerts-api
- collection_type: open
  name: ALTR Classification Engine ALTR Managed Collections API
  slug: open-altr-altr-managed-collections-api
- collection_type: open
  name: ALTR Management Anomalies API
  slug: open-altr-anomalies-api
- collection_type: open
  name: ALTR Management Apikeys API
  slug: open-altr-apikeys-api
- collection_type: open
  name: ALTR Management Applications API
  slug: open-altr-applications-api
- collection_type: open
  name: Service User Service Auth API
  slug: open-altr-auth-api
- collection_type: open
  name: Auto Tagging Auto Tagging API API
  slug: open-altr-auto-tagging-api-api
- collection_type: open
  name: Critical Tokenization V2 Batch API
  slug: open-altr-batch-api
- collection_type: open
  name: ALTR Management Classification API
  slug: open-altr-classification-api
- collection_type: open
  name: ALTR Classification Engine Classification Jobs API
  slug: open-altr-classification-jobs-api
- collection_type: open
  name: ALTR Classification Engine Classifiers API
  slug: open-altr-classifiers-api
- collection_type: open
  name: ALTR Classification Engine Collections API
  slug: open-altr-collections-api
- collection_type: open
  name: ALTR Audit Report Comments API
  slug: open-altr-comments-api
- collection_type: open
  name: ALTR Management Configuration API
  slug: open-altr-configuration-api
- collection_type: open
  name: Access Tokens Control Plane API
  slug: open-altr-control-plane-api
- collection_type: open
  name: ALTR Management Data API
  slug: open-altr-data-api
- collection_type: open
  name: ALTR Datastore Information Service Data Discovery API
  slug: open-altr-data-discovery-api
- collection_type: open
  name: ALTR Datastore Information Service Data Masking API
  slug: open-altr-data-masking-api
- collection_type: open
  name: ALTR Datastore Information Service Data Tagging API
  slug: open-altr-data-tagging-api
- collection_type: open
  name: ALTR Management Databases API
  slug: open-altr-databases-api
- collection_type: open
  name: ALTR — Tag-based governance policy on Databricks Databricks Tag Policy API
  slug: open-altr-databricks-tag-policy-api
- collection_type: open
  name: ALTR Audit Report Definitions API
  slug: open-altr-definitions-api
- collection_type: open
  name: ALTR Audit Report Instances API
  slug: open-altr-instances-api
- collection_type: open
  name: ALTR Notification Integration Integrations API
  slug: open-altr-integrations-api
- collection_type: open
  name: ALTR Management Maskingpolicies API
  slug: open-altr-maskingpolicies-api
- collection_type: open
  name: ALTR Management Me API
  slug: open-altr-me-api
- collection_type: open
  name: ALTR Management Metadata API
  slug: open-altr-metadata-api
- collection_type: open
  name: ALTR Management Organization API
  slug: open-altr-organization-api
- collection_type: open
  name: ALTR Management Plan API
  slug: open-altr-plan-api
- collection_type: open
  name: Unified Policy API
  slug: open-altr-policy-api
- collection_type: open
  name: Query Audits Query Audits API API
  slug: open-altr-query-audits-api-api
- collection_type: open
  name: Query Dashboard Query Dashboard API API
  slug: open-altr-query-dashboard-api-api
- collection_type: open
  name: RBAC RBAC API API
  slug: open-altr-rbac-api-api
- collection_type: open
  name: Snowflake Tag Value Refresh Refresh Tag Value Job API
  slug: open-altr-refresh-tag-value-job-api
- collection_type: open
  name: ALTR Sidecar/Agent Configuration Repo Users API
  slug: open-altr-repo-users-api
- collection_type: open
  name: ALTR Sidecar/Agent Configuration Repos API
  slug: open-altr-repos-api
- collection_type: open
  name: ALTR Management Rowaccess API
  slug: open-altr-rowaccess-api
- collection_type: open
  name: Altr Rules API
  slug: open-altr-rules-api
- collection_type: open
  name: ALTR Management SCIM API
  slug: open-altr-scim-api
- collection_type: open
  name: ALTR Sidecar/Agent Configuration Service Users API
  slug: open-altr-service-users-api
- collection_type: open
  name: ALTR Management Setup Guide API
  slug: open-altr-setup-guide-api
- collection_type: open
  name: ALTR Telemetry Sidecar API
  slug: open-altr-sidecar-api
- collection_type: open
  name: Sidecar Audit Sidecar Audit API API
  slug: open-altr-sidecar-audit-api-api
- collection_type: open
  name: ALTR Sidecar/Agent Configuration Sidecar Listener Port and Repo bindings API
  slug: open-altr-sidecar-listener-port-and-repo-bindings-api
- collection_type: open
  name: ALTR Sidecar/Agent Configuration Sidecar Listeners API
  slug: open-altr-sidecar-listeners-api
- collection_type: open
  name: ALTR Sidecar/Agent Configuration Sidecars API
  slug: open-altr-sidecars-api
- collection_type: open
  name: ALTR Audit Report Sign Off API
  slug: open-altr-sign-off-api
- collection_type: open
  name: Snowflake Metadata Snowflake Metadata API API
  slug: open-altr-snowflake-metadata-api-api
- collection_type: open
  name: ALTR Management SSO API
  slug: open-altr-sso-api
- collection_type: open
  name: ALTR Notification Integration Subscriptions API
  slug: open-altr-subscriptions-api
- collection_type: open
  name: ALTR Management Systemaudits API
  slug: open-altr-systemaudits-api
- collection_type: open
  name: ALTR Management Systemaudits/query API
  slug: open-altr-systemaudits-query-api
- collection_type: open
  name: Tag Masking Tag Masking API API
  slug: open-altr-tag-masking-api-api
- collection_type: open
  name: ALTR Management Tags API
  slug: open-altr-tags-api
- collection_type: open
  name: ALTR Telemetry Task API
  slug: open-altr-task-api
- collection_type: open
  name: Service User Service Tasks API
  slug: open-altr-tasks-api
- collection_type: open
  name: ALTR Management Thresholds API
  slug: open-altr-thresholds-api
- collection_type: open
  name: ALTR DAM Alerting Unsubscribe API
  slug: open-altr-unsubscribe-api
- collection_type: open
  name: ALTR Management Usergroups API
  slug: open-altr-usergroups-api
- collection_type: open
  name: Service User Service Users API
  slug: open-altr-users-api
- collection_type: open
  name: ALTR Datastore Information Service Utility API
  slug: open-altr-utility-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/altr-access-tokens-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/altrsoftware/altr-mcp-server/issues
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
overview: 'ALTR publishes 66 APIs on the [APIs.io](https://apis.io/) network, including Access Request API, Administrators API, Agent API, and 63 more. Tagged areas include data-security, data-governance, data-masking, tokenization, and data-classification.


  The ALTR catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  ALTR''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 32 more developer resources.'
random_paper: 137
score:
  band: strong
  composite: 57.5
  delta: -1.6
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 16.7
    contract_quality: 66.4
    developer_ergonomics: 73.2
    discoverability: 87.0
    governance: 16.7
    operational_transparency: 36.8
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 86.4
      derived: 0
      marker_coverage: 0.0
      total: 66
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/altr/refs/heads/main/screenshots/altr-2026-08-07T161253.png
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
