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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 47
  human_in_the_loop: 1
  name: Soda Co Agentic Access
  operation_count: 79
  slug: soda-co-agentic-access
  summary_line: 79 operations · 47 acting · 1 human-in-the-loop
api_count: 13
apis:
- description: Custom attribute management for datasets, checks, and columns
  name: Soda Attributes API
  slug: soda-co-attributes-api
- description: Data quality check results and management
  name: Soda Checks API
  slug: soda-co-checks-api
- description: Data contract definition, publishing, and verification
  name: Soda Contracts API
  slug: soda-co-contracts-api
- description: Dataset management, monitoring, and configuration
  name: Soda Datasets API
  slug: soda-co-datasets-api
- description: Data source connection and configuration management
  name: Soda Datasources API
  slug: soda-co-datasources-api
- description: Datasets discovered but not yet onboarded
  name: Soda Discovered Datasets API
  slug: soda-co-discovered-datasets-api
- description: Data quality incident tracking and management
  name: Soda Incidents API
  slug: soda-co-incidents-api
- description: Alert and notification rule management
  name: Soda Notification Rules API
  slug: soda-co-notification-rules-api
- description: Scan runner agent management
  name: Soda Runners API
  slug: soda-co-runners-api
- description: Data quality scan execution and monitoring
  name: Soda Scans API
  slug: soda-co-scans-api
- description: Encrypted secret storage for datasource credentials
  name: Soda Secrets API
  slug: soda-co-secrets-api
- description: User and user group management
  name: Soda Users API
  slug: soda-co-users-api
- description: API connectivity and authentication testing
  name: Soda Utility API
  slug: soda-co-utility-api
artifact_total: 29
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/soda-co-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/soda-co-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/soda-co-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/soda-co-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://soda.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.soda.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sodadata
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sodadata
- group: company
  title: ''
  type: Blog
  url: https://soda.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://soda.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.soda.io
- group: other
  title: ''
  type: X
  url: https://x.com/sodadata
- group: commercial
  title: ''
  type: Plans
  url: plans/soda-co-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/soda-co-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/soda-co-finops.yml
created: 2026-06-13
description: Soda is an AI-native, fully automated data quality platform that helps data engineering and analytics teams define data quality checks, scan datasets, monitor data freshness, and manage data quality incidents. The Soda Cloud REST API enables programmatic access to trigger scans, retrieve check results, manage incidents, and integrate data quality workflows into CI/CD pipelines and data stacks. Soda supports dozens of data sources including Snowflake, BigQuery, Databricks, PostgreSQL, and DuckDB.
examples:
- key_count: 3
  name: Create Datasource Request
  slug: create-datasource-request
- key_count: 7
  name: List Checks Response
  slug: list-checks-response
- key_count: 7
  name: List Datasets Response
  slug: list-datasets-response
- key_count: 15
  name: Scan Status Response
  slug: scan-status-response
- key_count: 1
  name: Test Login Response
  slug: test-login-response
- key_count: 5
  name: Update Incident Request
  slug: update-incident-request
finops:
- name: Soda Co Finops
  service_category: ''
  slug: soda-co-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/soda-co.png
json_schemas:
- name: Soda Cloud REST API Schemas
  property_count: 0
  slug: soda-cloud-rest-api
jsonld:
- class_count: 40
  name: Soda Co Context
  property_count: 0
  slug: soda-co
layout: provider
modified: 2026-06-13
name: Soda
nav: Providers
network: true
overview: 'Soda publishes 13 APIs on the [APIs.io](https://apis.io/) network, including Attributes API, Checks API, Contracts API, and 10 more. Tagged areas include Data Quality, Data Observability, Data Contracts, Data Testing, and Data Monitoring.


  The Soda catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Soda''s developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Soda Co Plans Pricing
  plan_count: 3
  slug: soda-co-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 3
  name: Soda Co Rate Limits
  slug: soda-co-rate-limits
rules:
- name: Soda API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: soda-co-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.5
  delta: -4.1
  facets:
    commercial_clarity: 57.9
    contract_quality: 65.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 57.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/soda-co/refs/heads/main/screenshots/soda-co-2026-06-20T194129.png
security:
- kind: authentication
  name: Soda Co Authentication
  slug: soda-co-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Soda Co Domain Security
  slug: soda-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Soda Co Trust Center
  slug: soda-co-trust-center
  summary_line: SOC 2, GDPR
slug: soda-co
tags:
- Data Quality
- Data Observability
- Data Contracts
- Data Testing
- Data Monitoring
- Data Engineering
website: https://soda.io
---
