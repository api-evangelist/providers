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
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Azure Log Analytics Agentic Access
  operation_count: 17
  slug: azure-log-analytics-agentic-access
  summary_line: 17 operations · 9 acting
api_count: 5
apis:
- description: Send log data to Log Analytics workspaces
  name: Azure Log Analytics Ingestion API
  slug: azure-log-analytics-ingestion-api
- description: Execute KQL queries against Log Analytics workspaces
  name: Azure Log Analytics Query API
  slug: azure-log-analytics-query-api
- description: Manage saved KQL queries
  name: Azure Log Analytics Saved Searches API
  slug: azure-log-analytics-saved-searches-api
- description: Manage workspace tables
  name: Azure Log Analytics Tables API
  slug: azure-log-analytics-tables-api
- description: Manage Log Analytics workspaces
  name: Azure Log Analytics Workspaces API
  slug: azure-log-analytics-workspaces-api
arazzos:
- description: List saved searches, inspect one, then delete it if it is uncategorized.
  name: Azure Log Analytics Audit and Clean Up a Saved Search
  slug: azure-log-analytics-audit-and-cleanup-saved-search-workflow
- description: Create a workspace, add a baseline custom table, then read the table back.
  name: Azure Log Analytics Create Workspace and Baseline Custom Table
  slug: azure-log-analytics-create-workspace-and-baseline-table-workflow
- description: Discover subscription workspaces, then run one KQL query spanning several of them.
  name: Azure Log Analytics Cross-Workspace Query
  slug: azure-log-analytics-cross-workspace-query-workflow
- description: Find a workspace in a subscription, confirm it, then run a KQL query against it.
  name: Azure Log Analytics Discover and Query Workspace
  slug: azure-log-analytics-discover-and-query-workspace-workflow
- description: Confirm a target table exists, upload logs via a DCR, then query to verify.
  name: Azure Log Analytics Ingest Logs and Verify
  slug: azure-log-analytics-ingest-and-verify-workflow
- description: List a workspace's saved searches, fetch one's KQL, then execute it.
  name: Azure Log Analytics Browse Saved Searches and Run One
  slug: azure-log-analytics-list-saved-searches-and-run-workflow
- description: List a workspace's tables, inspect one table's schema, then query that table.
  name: Azure Log Analytics Inspect Table Schema then Query
  slug: azure-log-analytics-list-tables-then-query-workflow
- description: Run a KQL query to validate it, then persist it as a saved search.
  name: Azure Log Analytics Validate then Save a KQL Query
  slug: azure-log-analytics-promote-query-to-saved-search-workflow
- description: Create a custom table, upload logs through a DCR, then query the table to verify.
  name: Azure Log Analytics Provision Custom Table then Ingest and Verify
  slug: azure-log-analytics-provision-table-and-ingest-workflow
- description: Confirm a workspace exists, then run a KQL query via the GET query endpoint.
  name: Azure Log Analytics Query Workspace by Name (GET)
  slug: azure-log-analytics-query-workspace-by-name-workflow
- description: Narrow workspaces to a resource group, resolve one, then run a KQL query.
  name: Azure Log Analytics Resolve Workspace by Resource Group and Run KQL
  slug: azure-log-analytics-resolve-workspace-and-run-kql-workflow
- description: Fetch a saved search's KQL definition, then execute it against the workspace.
  name: Azure Log Analytics Run a Saved Search
  slug: azure-log-analytics-saved-search-to-query-workflow
- description: Read a workspace's current retention, patch it, then read it back to confirm.
  name: Azure Log Analytics Update Workspace Retention and Verify
  slug: azure-log-analytics-update-workspace-retention-workflow
- description: Resolve a workspace, then list its tables and its saved searches together.
  name: Azure Log Analytics Workspace Inventory Report
  slug: azure-log-analytics-workspace-inventory-report-workflow
artifact_total: 81
collections:
- collection_type: postman
  name: Azure Log Analytics Ingestion API
  slug: postman-azure-log-analytics-ingestion-api
- collection_type: postman
  name: Azure Log Analytics Management API
  slug: postman-azure-log-analytics-management-api
- collection_type: postman
  name: Azure Log Analytics Query API
  slug: postman-azure-log-analytics-query-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Azure Log Analytics Ingestion API
  slug: open-azure-log-analytics-ingestion-api
- collection_type: open
  name: Azure Log Analytics Ingestion Query API
  slug: open-azure-log-analytics-query-api
- collection_type: open
  name: Azure Log Analytics Ingestion Saved Searches API
  slug: open-azure-log-analytics-saved-searches-api
- collection_type: open
  name: Azure Log Analytics Ingestion Tables API
  slug: open-azure-log-analytics-tables-api
- collection_type: open
  name: Azure Log Analytics Ingestion Workspaces API
  slug: open-azure-log-analytics-workspaces-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Azure/azure-rest-api-specs/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Azure/azure-rest-api-specs/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/Azure/azure-rest-api-specs/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/Azure/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Azure/azure-rest-api-specs/blob/main/.github/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/Azure/azure-rest-api-specs/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/azure-log-analytics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/azure-log-analytics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/azure-log-analytics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/azure-log-analytics-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/azure-log-analytics/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-audit-and-cleanup-saved-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-create-workspace-and-baseline-table-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-cross-workspace-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-discover-and-query-workspace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-ingest-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-list-saved-searches-and-run-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-list-tables-then-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-promote-query-to-saved-search-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-provision-table-and-ingest-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-query-workspace-by-name-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-resolve-workspace-and-run-kql-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-saved-search-to-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-update-workspace-retention-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/azure-log-analytics-workspace-inventory-report-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/azure-monitor/logs/log-analytics-tutorial
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/monitor/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.azure.com/
- group: operate
  title: ''
  type: Support
  url: https://azure.microsoft.com/en-us/support/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/tag/azure-log-analytics/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://azure.microsoft.com/en-us/support/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Azure/azure-rest-api-specs
- group: build
  title: ''
  type: CLI
  url: https://learn.microsoft.com/en-us/cli/azure/monitor/log-analytics
- group: build
  title: Python SDK
  type: SDKs
  url: https://pypi.org/project/azure-monitor-query/
- group: build
  title: JavaScript SDK
  type: SDKs
  url: https://www.npmjs.com/package/@azure/monitor-query
- group: build
  title: Go SDK
  type: SDKs
  url: https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/monitor/query/azlogs
- group: build
  title: .NET SDK
  type: SDKs
  url: https://learn.microsoft.com/en-us/dotnet/api/overview/azure/Monitor.Query-readme
- group: build
  title: Java SDK
  type: SDKs
  url: https://learn.microsoft.com/en-us/java/api/overview/azure/monitor-query-readme
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/azure/azure-monitor/service-limits#query-api
- group: design
  title: ''
  type: SpectralRules
  url: rules/azure-log-analytics-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/azure-log-analytics-vocabulary.yaml
created: '2024-01-01'
description: Azure Log Analytics is a service that helps you collect and analyze data generated by resources in your cloud and on-premises environments, providing query, management, and data collection APIs for monitoring and analytics.
examples:
- key_count: 3
  name: Ingestion Api Log Entry Example
  slug: ingestion-api-log-entry-example
- key_count: 5
  name: Management Api Saved Search Example
  slug: management-api-saved-search-example
- key_count: 6
  name: Management Api Workspace Example
  slug: management-api-workspace-example
- key_count: 3
  name: Query Api Query Body Example
  slug: query-api-query-body-example
- key_count: 1
  name: Query Api Query Results Example
  slug: query-api-query-results-example
features:
- description: Full KQL query language support for complex log analytics and data exploration across cloud and on-premises resources.
  name: Kusto Query Language
- description: Send custom log data from any source using the Logs Ingestion API with data collection rules and transformations.
  name: Custom Log Ingestion
- description: Create, configure, and manage Log Analytics workspaces including data sources, retention policies, and access control.
  name: Workspace Management
- description: Save and reuse KQL queries across workspace sessions for consistent monitoring and reporting.
  name: Saved Searches
- description: Define data collection pipelines with transformations that shape incoming data before it reaches the workspace.
  name: Data Collection Rules
- description: Query data across multiple Log Analytics workspaces in a single query for centralized analysis.
  name: Cross-Workspace Queries
- description: Point-and-click spreadsheet-like query experience for users who do not need full KQL knowledge.
  name: Simple Mode Queries
- description: Create alert rules directly from log queries to enable proactive monitoring and automated responses.
  name: Alert Rule Integration
- description: Activate and deactivate failover for workspace disaster recovery and high availability.
  name: Workspace Failover
- description: Export query results to Excel, CSV, Power BI, and Grafana dashboards for external analysis.
  name: Data Export
finops:
- name: Azure Log Analytics Finops
  service_category: Observability
  slug: azure-log-analytics-finops
image: /assets/icons/azure-log-analytics.png
integrations:
- description: Core integration with Azure Monitor for unified observability across metrics, logs, and traces.
  name: Azure Monitor
- description: Feed log data into Microsoft Sentinel for SIEM and SOAR capabilities.
  name: Microsoft Sentinel
- description: Built on Azure Data Explorer engine, supports the same KQL query language for advanced analytics.
  name: Azure Data Explorer
- description: Export and visualize log query results in Power BI dashboards for business intelligence reporting.
  name: Power BI
- description: Connect Azure Monitor Logs as a data source in managed Grafana dashboards for visualization.
  name: Grafana
- description: Create interactive visual reports using log query results within Azure Workbooks.
  name: Azure Workbooks
- description: Trigger automation runbooks based on log query results and alert rules.
  name: Azure Automation
- description: Integrate log analytics alerts with Logic Apps workflows for automated incident response.
  name: Azure Logic Apps
- description: Combine application telemetry from Application Insights with infrastructure logs for full-stack observability.
  name: Application Insights
- description: Manage Log Analytics resources programmatically through Azure Resource Manager REST APIs.
  name: Azure Resource Manager
json_schemas:
- name: LogEntry
  property_count: 3
  slug: ingestion-api-log-entry
- name: SavedSearch
  property_count: 5
  slug: management-api-saved-search
- name: Workspace
  property_count: 7
  slug: management-api-workspace
- name: QueryBody
  property_count: 3
  slug: query-api-query-body
- name: QueryResults
  property_count: 2
  slug: query-api-query-results
json_structures:
- name: Ingestion Api Log Entry Structure
  property_count: 3
  slug: ingestion-api-log-entry-structure
- name: Management Api Saved Search Structure
  property_count: 5
  slug: management-api-saved-search-structure
- name: Management Api Workspace Structure
  property_count: 7
  slug: management-api-workspace-structure
- name: Query Api Query Body Structure
  property_count: 3
  slug: query-api-query-body-structure
- name: Query Api Query Results Structure
  property_count: 2
  slug: query-api-query-results-structure
jsonld:
- class_count: 3
  name: Azure Log Analytics Ingestion Api Context
  property_count: 10
  slug: azure-log-analytics-ingestion-api-context
- class_count: 5
  name: Azure Log Analytics Management Api Context
  property_count: 20
  slug: azure-log-analytics-management-api-context
- class_count: 6
  name: Azure Log Analytics Query Api Context
  property_count: 11
  slug: azure-log-analytics-query-api-context
layout: provider
modified: '2026-05-19'
name: Azure Log Analytics
nav: Providers
network: true
overview: 'Azure Log Analytics publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Ingestion API, Query API, Saved Searches API, and 2 more. Tagged areas include Analytics, Azure, Cloud, Logging, and Monitoring.


  The Azure Log Analytics catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  Azure Log Analytics'' developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, support, engineering blog, and 38 more developer resources.'
plans:
- name: Azure Log Analytics Plans Pricing
  plan_count: 4
  slug: azure-log-analytics-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 19
  name: Azure Log Analytics Rate Limits
  slug: azure-log-analytics-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Azure Log Analytics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: azure-log-analytics-jsonschema-spectral-rules
- effective_rule_count: 86
  extends:
  - spectral:oas
  name: Azure Log Analytics API Rules
  rule_count: 45
  severity_counts:
    error: 20
    hint: 0
    info: 10
    warn: 15
  slug: azure-log-analytics-spectral-rules
scopes:
- name: Azure Log Analytics Scopes
  scope_count: 1
  slug: azure-log-analytics-scopes
  summary_line: 1 scope · implicit
score:
  band: developing
  composite: 51.4
  delta: 2.1
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 28.8
    contract_quality: 30.4
    developer_ergonomics: 83.3
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 52.6
  previous_composite: 49.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/azure-log-analytics/refs/heads/main/screenshots/azure-log-analytics-2026-07-25T202128.png
security:
- kind: authentication
  name: Azure Log Analytics Authentication
  slug: azure-log-analytics-authentication
  summary_line: apiKey/http/oauth2 · 3 schemes
- kind: domain-security
  name: Azure Log Analytics Domain Security
  slug: azure-log-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: azure-log-analytics
tags:
- Analytics
- Azure
- Cloud
- Logging
- Monitoring
use_cases:
- description: Collect and analyze logs from virtual machines, containers, and network resources to monitor infrastructure health.
  name: Infrastructure Monitoring
- description: Query security events and audit logs to investigate incidents and detect threats across Azure resources.
  name: Security Investigation
- description: Analyze application logs and telemetry to identify performance bottlenecks and errors.
  name: Application Performance Monitoring
- description: Collect and retain audit logs to meet regulatory compliance requirements and generate compliance reports.
  name: Compliance Auditing
- description: Ingest custom log data from third-party systems and on-premises resources using the Logs Ingestion API.
  name: Custom Data Integration
- description: Analyze resource usage patterns and log data to identify cost-saving opportunities across Azure deployments.
  name: Cost Optimization
website: https://portal.azure.com/
---
