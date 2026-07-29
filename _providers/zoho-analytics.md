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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 103
  human_in_the_loop: 1
  name: Zoho Analytics Agentic Access
  operation_count: 161
  slug: zoho-analytics-agentic-access
  summary_line: 161 operations · 103 acting · 1 human-in-the-loop
api_count: 11
apis:
- description: Asynchronous operations for exporting data in bulk.
  name: Zoho Analytics Bulk Export - Asynchronous API
  slug: zoho-analytics-bulk-export-asynchronous-api
- description: Synchronous operations for exporting data.
  name: Zoho Analytics Bulk Export - Synchronous API
  slug: zoho-analytics-bulk-export-synchronous-api
- description: Asynchronous operations for importing data in bulk.
  name: Zoho Analytics Bulk Import - Asynchronous API
  slug: zoho-analytics-bulk-import-asynchronous-api
- description: Operations for importing large data files in batches.
  name: Zoho Analytics Bulk Import - Batch API
  slug: zoho-analytics-bulk-import-batch-api
- description: Synchronous operations for importing data.
  name: Zoho Analytics Bulk Import - Synchronous API
  slug: zoho-analytics-bulk-import-synchronous-api
- description: Data APIs are used to perform addition, update, deletion actions on Zoho Analytics tables.
  name: Zoho Analytics Data APIs API
  slug: zoho-analytics-data-apis-api
- description: Embed APIs let you dynamically integrate Zoho Analytics reports and dashboards into your websites and applications.
  name: Zoho Analytics Embed APIs API
  slug: zoho-analytics-embed-apis-api
- description: Metadata APIs are used to fetch information about the reporting Workspaces, tables, reports, and dashboards created in Zoho Analytics.
  name: Zoho Analytics Metadata APIs API
  slug: zoho-analytics-metadata-apis-api
- description: Modeling APIs manage workspaces, views, columns, and folders, and support copying across or within Zoho Analytics accounts.
  name: Zoho Analytics Modeling APIs API
  slug: zoho-analytics-modeling-apis-api
- description: APIs for sharing views (reports and dashboards) with users, managing permissions, and removing sharing in Zoho Analytics.
  name: Zoho Analytics Sharing & Collaboration APIs API
  slug: zoho-analytics-sharing-collaboration-apis-api
- description: Manage User APIs allow you to add, remove, activate, or deactivate users in your Zoho Analytics organization programmatically.
  name: Zoho Analytics User Management APIs API
  slug: zoho-analytics-user-management-apis-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoho-analytics-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-analytics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-analytics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoho-analytics-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoho-analytics-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/analytics/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/analytics/api/v2/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/zohoanalytics/
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/analytics/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/analytics/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoho.com/
- group: other
  title: ''
  type: X
  url: https://x.com/ZohoAnalytics
- group: commercial
  title: ''
  type: Plans
  url: plans/zoho-analytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoho-analytics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zoho-analytics-finops.yml
created: '2026-06-13'
description: Zoho Analytics is a business intelligence and self-service analytics platform that provides a REST API for managing workspaces, views, reports, dashboards, data import and export, and sharing analytics content. The API enables ISVs, developers, and system integrators to embed powerful reporting and analytical capabilities into their applications. It supports OAuth 2.0 authentication, regional endpoints across eight data centers, and provides SDKs for Java, C#, Python, PHP, Go, and Node.js.
examples:
- key_count: 27
  name: Zoho Analytics Examples
  slug: zoho-analytics-examples
graphqls:
- description: This conceptual GraphQL schema models the Zoho Analytics REST API (v2) domain for business intelligence and self-service analytics. Zoho Analytics provides workspaces, databases, tables, views, report
  name: Zoho Analytics GraphQL Schema
  slug: zoho-analytics-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-analytics.png
json_schemas:
- name: Zoho Analytics API Schemas
  property_count: 0
  slug: zoho-analytics
jsonld:
- class_count: 0
  name: Zoho Analytics Context
  property_count: 0
  slug: zoho-analytics-context
layout: provider
modified: '2026-06-13'
name: Zoho Analytics
nav: Providers
network: true
overview: 'Zoho Analytics publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Bulk Export - Asynchronous API, Bulk Export - Synchronous API, Bulk Import - Asynchronous API, and 8 more. Tagged areas include Business Intelligence, Analytics, Dashboards, Reports, and Data Import.


  The Zoho Analytics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zoho Analytics'' developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Zoho Analytics Plans Pricing
  plan_count: 6
  slug: zoho-analytics-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Zoho Analytics Rate Limits
  slug: zoho-analytics-rate-limits
rules:
- name: Zoho Analytics API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: zoho-analytics-jsonschema-spectral-rules
scopes:
- name: Zoho Analytics Scopes
  scope_count: 31
  slug: zoho-analytics-scopes
  summary_line: 31 scopes · authorizationCode
score:
  band: developing
  composite: 45.9
  delta: -3.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 64.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 48.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-analytics/refs/heads/main/screenshots/zoho-analytics-2026-06-20T201934.png
security:
- kind: authentication
  name: Zoho Analytics Authentication
  slug: zoho-analytics-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zoho Analytics Domain Security
  slug: zoho-analytics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Analytics Vulnerability Disclosure
  slug: zoho-analytics-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-analytics
tags:
- Business Intelligence
- Analytics
- Dashboards
- Reports
- Data Import
- Data Export
- Workspaces
- Visualizations
website: https://www.zoho.com/analytics/
---
