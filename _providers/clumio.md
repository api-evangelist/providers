---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 28.8
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Regional REST API for the Clumio backup-as-a-service platform. Manage AWS and GCP connections, backup policies and protection rules, protection groups, organizational units, users, roles, compliance r
  name: Clumio REST API
  slug: clumio-rest-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clumio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clumio.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.clumio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.commvault.com/clumio/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://developers.clumio.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.clumio.com/reference/introduction
- group: operate
  title: ''
  type: Support
  url: https://help.clumio.com/
- group: company
  title: ''
  type: Blog
  url: https://clumio.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/clumio-code
- group: commercial
  title: ''
  type: Pricing
  url: https://clumio.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.commvault.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.commvault.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.clumio.com/
- group: build
  title: ''
  type: Packages
  url: packages/clumio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/clumio-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/clumio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/clumio-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/clumio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/clumio-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/clumio-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/clumio-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clumio-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/clumio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/clumio-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/clumio-data-model.yml
created: '2026-07-17'
description: 'Clumio (a Commvault company) is a secure, air-gapped backup-as-a-service platform for the public cloud. It delivers fully managed, immutable data protection and on-demand restore for Amazon Web Services (EBS, EC2, RDS, S3, DynamoDB, DocumentDB, Neptune, Iceberg tables, EC2/RDS MSSQL), Google Cloud Storage, and VMware vCenter workloads. Clumio is API-first: its regional REST API lets teams automate AWS/GCP connections, backup policies and protection rules, protection groups, organizational units, users and roles, compliance reports, audit trails, and restore workflows. Authentication uses long-lived signed-JWT bearer tokens (Personal and Service tokens), responses follow HATEOAS/HAL conventions with `_links`, and the API is versioned per resource. First-party Python and Go SDKs and a Terraform provider are published under the clumio-code GitHub org.'
image: https://clumio.com/wp-content/uploads/2021/06/clumio-logo.png
layout: provider
mcp_servers:
- description: ''
  name: clumio-mcp.yml
  slug: clumio-mcpyml
modified: '2026-07-18'
name: Clumio
nav: Providers
network: true
overview: 'Clumio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Backup, Data Protection, and Disaster Recovery.


  Clumio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 18 more developer resources.'
random_paper: 37
score:
  band: thin
  composite: 35.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 35.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Clumio Authentication
  slug: clumio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clumio Domain Security
  slug: clumio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: clumio
tags:
- Company
- Data
- Backup
- Data Protection
- Disaster Recovery
- Cloud
- Storage
- Security
- Compliance
website: https://clumio.com
---
