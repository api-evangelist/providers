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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Google Cloud Sql Agentic Access
  operation_count: 12
  slug: google-cloud-sql-agentic-access
  summary_line: 12 operations · 6 acting
api_count: 4
apis:
- description: Operations on backup runs
  name: Google Cloud SQL BackupRuns API
  slug: google-cloud-sql-backupruns-api
- description: Operations on databases within instances
  name: Google Cloud SQL Databases API
  slug: google-cloud-sql-databases-api
- description: Operations on Cloud SQL instances
  name: Google Cloud SQL Instances API
  slug: google-cloud-sql-instances-api
- description: Operations on database users
  name: Google Cloud SQL Users API
  slug: google-cloud-sql-users-api
artifact_total: 20
collections:
- collection_type: postman
  name: Google Cloud SQL Admin BackupRuns API
  slug: postman-google-cloud-sql-backupruns-api
- collection_type: postman
  name: Google Cloud SQL Admin BackupRuns Databases API
  slug: postman-google-cloud-sql-databases-api
- collection_type: postman
  name: Google Cloud SQL Admin BackupRuns Instances API
  slug: postman-google-cloud-sql-instances-api
- collection_type: postman
  name: Google Cloud SQL Admin BackupRuns Users API
  slug: postman-google-cloud-sql-users-api
- collection_type: open
  name: Google Cloud SQL Admin API
  slug: open-cloud-sql
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-cloud-sql/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-cloud-sql-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-cloud-sql-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-cloud-sql-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-cloud-sql-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-cloud-sql-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoogleCloudPlatform
- group: start
  title: ''
  type: Portal
  url: https://cloud.google.com/sql
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud.google.com/sql/docs/mysql/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://cloud.google.com/sql/docs
- group: auth
  title: ''
  type: Authentication
  url: https://cloud.google.com/sql/docs/mysql/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://cloud.google.com/sql/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloud.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://cloud.google.com/sql/docs/mysql/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-cloud-sql-context.jsonld
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/feeds/cloud-sql-release-notes.xml
created: '2026-03-13'
description: Google Cloud SQL is a fully managed relational database service that supports MySQL, PostgreSQL, and SQL Server. It handles routine database tasks such as provisioning, replication, backups, and failover, allowing developers to focus on application development. Cloud SQL provides high availability, automatic storage scaling, and integrated security features.
finops:
- name: Google Cloud Sql Finops
  service_category: API
  slug: google-cloud-sql-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-cloud-sql.png
json_schemas:
- name: Google Cloud SQL Database Instance
  property_count: 13
  slug: instance
jsonld:
- class_count: 17
  name: Google Cloud Sql Context
  property_count: 0
  slug: google-cloud-sql-context
layout: provider
modified: '2026-05-19'
name: Google Cloud SQL
nav: Providers
network: true
overview: 'Google Cloud SQL publishes 4 APIs on the [APIs.io](https://apis.io/) network, including BackupRuns API, Databases API, Instances API, and 1 more. Tagged areas include Database, Google Cloud, MySQL, PostgreSQL, and Relational.


  The Google Cloud SQL catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Cloud SQL''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, engineering blog, and 11 more developer resources.'
plans:
- name: Google Cloud Sql Plans Pricing
  plan_count: 3
  slug: google-cloud-sql-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 5
  name: Google Cloud Sql Rate Limits
  slug: google-cloud-sql-rate-limits
rules:
- name: Google Cloud SQL API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-cloud-sql-jsonschema-spectral-rules
scopes:
- name: Google Cloud Sql Scopes
  scope_count: 2
  slug: google-cloud-sql-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 55.2
  delta: -8.5
  facets:
    commercial_clarity: 47.4
    contract_quality: 70.1
    developer_ergonomics: 50.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 63.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/google-cloud-sql/refs/heads/main/screenshots/google-cloud-sql-2026-06-20T182138.png
security:
- kind: authentication
  name: Google Cloud Sql Authentication
  slug: google-cloud-sql-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Cloud Sql Domain Security
  slug: google-cloud-sql-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Cloud Sql Vulnerability Disclosure
  slug: google-cloud-sql-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-cloud-sql
tags:
- Database
- Google Cloud
- MySQL
- PostgreSQL
- Relational
- SQL
website: https://cloud.google.com/sql
---
