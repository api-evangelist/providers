---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.4
  scored_at: '2026-08-10'
api_count: 2
apis:
- description: REST API for the Anomalo data quality platform. Connect and refresh data warehouses, configure which tables are monitored, author and run data quality checks, read check-run results and table data pro
  name: Anomalo Public API
  slug: anomalo-public-api
- description: Official Anomalo MCP (Model Context Protocol) server, published by Anomalo as a Google Gemini CLI extension under the Apache-2.0 license. Runs locally over stdio against a customer's own Anomalo insta
  name: Anomalo MCP Server
  slug: anomalo-mcp-server
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.anomalo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.anomalo.com/product-overview/
- group: operate
  title: ''
  type: Support
  url: https://www.anomalo.com/request-support/
- group: company
  title: ''
  type: Blog
  url: https://www.anomalo.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.anomalo.com/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anomalo-hq
- group: start
  title: ''
  type: SignUp
  url: https://www.anomalo.com/request-a-demo/
- group: start
  title: ''
  type: Login
  url: https://app.anomalo.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.anomalo.com/legal/subscription/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anomalo.com/legal/privacy/
- group: auth
  title: ''
  type: Compliance
  url: https://www.anomalo.com/legal/
- group: build
  title: ''
  type: Packages
  url: packages/anomalo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/anomalo-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/anomalo-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/anomalo-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/anomalo-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/anomalo-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/anomalo-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/anomalo-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/anomalo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/anomalo-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/anomalo-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/anomalo-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/anomalo-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/anomalo-changelog.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/anomalo-domain-security.yml
created: '2026-07-31'
description: Anomalo is an AI-powered data quality and data observability platform that automatically detects, alerts on, triages and helps resolve data issues before they reach analytics, reporting or AI models. It connects directly to cloud data warehouses and lakehouses — Snowflake, Databricks, BigQuery, Redshift, Amazon S3 and others — profiles the tables it monitors, and applies unsupervised machine learning to surface anomalies without requiring engineers to hand-author rules or maintain thresholds, alongside declaratively configured validation checks. The platform covers structured, semi-structured and unstructured data, performs root-cause analysis on failed checks, tracks table lineage, and routes alerts to Slack, Microsoft Teams, Jira, ServiceNow, PagerDuty and email. Anomalo exposes a REST Public API (`/api/public/v1/`) for warehouse connection, table configuration, check authoring and execution, check-run results, labels, lineage edges, users, API keys and access-group administration,
  plus a first-party Python client and CLI, an Apache Airflow provider, and an official MCP server shipped as a Google Gemini CLI extension. Anomalo is deployed per-tenant, with API documentation gated to customers; the company holds SOC 2 Type 2 and ISO 27001 attestations.
image: https://www.anomalo.com/wp-content/uploads/2024/01/logo-1.svg
layout: provider
mcp_servers:
- description: ''
  name: anomalo-mcp.yml
  slug: anomalo-mcpyml
modified: '2026-07-31'
name: Anomalo
nav: Providers
network: true
overview: 'Anomalo publishes 1 API on the [APIs.io](https://apis.io/) network: Public API. Tagged areas include data-quality, data-observability, data-monitoring, anomaly-detection, and data-governance.


  Anomalo''s developer surface includes documentation, support, engineering blog, signup flow, CLI, authentication, changelog, and 20 more developer resources.'
random_paper: 47
scopes:
- name: Anomalo Scopes
  scope_count: 3
  slug: anomalo-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 34.7
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 14.1
    developer_ergonomics: 49.5
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 34.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/anomalo/refs/heads/main/screenshots/anomalo-2026-08-07T161419.png
security:
- kind: authentication
  name: Anomalo Authentication
  slug: anomalo-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Anomalo Domain Security
  slug: anomalo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anomalo
tags:
- data-quality
- data-observability
- data-monitoring
- anomaly-detection
- data-governance
- data-lineage
- data-profiling
- data-validation
- data-engineering
- machine-learning
- snowflake
- databricks
- bigquery
- enterprise-data
- mcp
- agent-native
website: https://www.anomalo.com/
---
