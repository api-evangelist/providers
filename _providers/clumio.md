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
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-02'
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
  name: Clumio MCP Server
  slug: clumio-mcp-server
modified: '2026-07-18'
name: Clumio
nav: Providers
network: true
overview: 'Clumio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Backup, Data Protection, and Disaster Recovery.


  Clumio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 18 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 34.2
  previous_composite: 31.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clumio/refs/heads/main/screenshots/clumio-2026-07-25T205738.png
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
