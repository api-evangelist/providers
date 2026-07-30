---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Workday Reporting Agentic Access
  operation_count: 2
  slug: workday-reporting-agentic-access
  summary_line: 2 operations
api_count: 7
apis:
- description: API for managing and executing custom reports programmatically.
  name: Workday Custom Reports API
  slug: workday-custom-reports-api
- description: API for accessing advanced reporting features including matrix reports and composite reports.
  name: Workday Advanced Reports API
  slug: workday-advanced-reports-api
- description: REST API for working with Workday Prism Analytics tables, data change tasks, and datasets. Enables programmatic creation and management of analytics data including ingesting external data, building tr
  name: Workday Prism Analytics REST API
  slug: workday-prism-analytics-rest-api
- description: SOAP web service for creating, editing, and retrieving objects related to Prism Analytics, including analytic dimension business objects, analytic dimension hierarchies, and analytic dimension values.
  name: Workday Prism Analytics SOAP Web Service
  slug: workday-prism-analytics-soap-web-service
- description: Workday Query Language (WQL) API enabling SQL-like querying of Workday data through REST endpoints. Provides high-performance data access for reporting and analytics use cases, with support for pagina
  name: Workday WQL API
  slug: workday-wql-api
- description: Retrieve metadata about report fields, prompts, and filter parameters
  name: Workday Reporting Report Metadata API
  slug: workday-reporting-report-metadata-api
- description: Execute and retrieve data from custom and standard Workday reports configured as web services
  name: Workday Reporting Reports API
  slug: workday-reporting-reports-api
artifact_total: 24
collections:
- collection_type: postman
  name: Workday Reporting Workday Report-as-a-Service (RaaS) Report Metadata API
  slug: postman-workday-reporting-report-metadata-api
- collection_type: postman
  name: Workday Reporting Workday Report-as-a-Service (RaaS) Report Metadata Reports API
  slug: postman-workday-reporting-reports-api
- collection_type: open
  name: Workday Reporting Workday Report-as-a-Service (RaaS) API
  slug: open-workday-reporting-raas
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday-reporting/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-reporting-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workday-reporting-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workday-reporting-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-reporting-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.workday.com
- group: operate
  title: ''
  type: Community
  url: https://community.workday.com
- group: start
  title: ''
  type: GettingStarted
  url: https://community.workday.com/api-start
- group: docs
  title: ''
  type: Documentation
  url: https://community.workday.com/api
- group: auth
  title: ''
  type: Authentication
  url: https://doc.workday.com/admin-guide/en-us/lef1569276711011/kqh1569276711095.html
- group: operate
  title: ''
  type: RateLimits
  url: https://doc.workday.com/reader/J1YvI9CYZUWl1U7_PSHyHA/f8K9WJ7Kh5FfQDNnvlHNFQ
- group: operate
  title: ''
  type: StatusPage
  url: https://community.workday.com/trust/status
- group: operate
  title: ''
  type: Support
  url: https://www.workday.com/en-us/customer-experience/support.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/legal.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: company
  title: ''
  type: Blog
  url: https://blog.workday.com/en-us/application-development.html
- group: company
  title: ''
  type: Website
  url: https://www.workday.com
- group: start
  title: ''
  type: Signup
  url: https://resourcecenter.workday.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Workday
- group: docs
  title: ''
  type: Reference
  url: https://community.workday.com/sites/default/files/file-hosting/productionapi/index.html
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.workday.com/en-US/home
- group: company
  title: ''
  type: Partners
  url: https://www.workday.com/en-us/company/partners/overview.html
created: '2024-01-01'
description: APIs for accessing Workday reporting functionality including custom reports, report data extraction, and report management.
finops:
- name: Workday Reporting Finops
  service_category: HR / Finance / Analytics SaaS
  slug: workday-reporting-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-reporting.png
json_schemas:
- name: Error
  property_count: 2
  slug: workday-reporting-error
- name: ReportField
  property_count: 3
  slug: workday-reporting-reportfield
- name: ReportMetadata
  property_count: 4
  slug: workday-reporting-reportmetadata
- name: ReportPrompt
  property_count: 4
  slug: workday-reporting-reportprompt
- name: ReportResponse
  property_count: 3
  slug: workday-reporting-reportresponse
json_structures:
- name: Workday Reporting Structure
  property_count: 0
  slug: workday-reporting-structure
layout: provider
modified: '2026-05-19'
name: Workday Reporting
nav: Providers
network: true
overview: 'Workday Reporting publishes 2 APIs on the [APIs.io](https://apis.io/) network: Report Metadata API and Reports API. Tagged areas include Analytics, Business Intelligence, Financial Reporting, Hr Data, and Reporting.


  The Workday Reporting catalog on APIs.io includes 1 Spectral governance ruleset.


  Workday Reporting''s developer surface includes authentication, getting-started guide, documentation, support, engineering blog, signup flow, and 16 more developer resources.'
plans:
- name: Workday Reporting Plans Pricing
  plan_count: 1
  slug: workday-reporting-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 1
  name: Workday Reporting Rate Limits
  slug: workday-reporting-rate-limits
rules:
- name: Workday Reporting API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-reporting-jsonschema-spectral-rules
score:
  band: strong
  composite: 57.3
  delta: -2.8
  facets:
    commercial_clarity: 57.9
    contract_quality: 61.9
    developer_ergonomics: 56.5
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 60.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-reporting/refs/heads/main/screenshots/workday-reporting-2026-06-20T201611.png
security:
- kind: authentication
  name: Workday Reporting Authentication
  slug: workday-reporting-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Workday Reporting Domain Security
  slug: workday-reporting-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Workday Reporting Trust Center
  slug: workday-reporting-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday-reporting
tags:
- Analytics
- Business Intelligence
- Financial Reporting
- Hr Data
- Reporting
website: https://www.workday.com
---
