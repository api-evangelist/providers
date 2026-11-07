---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Regional REST API for the Clumio backup-as-a-service platform. Manage AWS and GCP connections, backup policies and protection rules, protection groups, organizational units, users, roles, compliance r
  name: Clumio REST API
  slug: clumio-rest-api
artifact_total: 4
common:
- group: company
  title: ''
  type: BlogRSS
  url: https://www.clumio.com/feed
- group: auth
  href: https://artifacts.apis.io/clumio/security/clumio-domain-security.yml
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
  href: https://artifacts.apis.io/clumio/packages/clumio-packages.yml
  title: ''
  type: Packages
  url: packages/clumio-packages.yml
- group: build
  href: https://artifacts.apis.io/clumio/packages/clumio-packages.yml
  title: ''
  type: SDKs
  url: packages/clumio-packages.yml
- group: agent
  href: https://artifacts.apis.io/clumio/mcp/clumio-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clumio-mcp.yml
- group: agent
  href: https://artifacts.apis.io/clumio/llms/clumio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clumio-llms.txt
- group: design
  href: https://artifacts.apis.io/clumio/conventions/clumio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/clumio-conventions.yml
- group: design
  href: https://artifacts.apis.io/clumio/errors/clumio-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/clumio-error-codes.yml
- group: design
  href: https://artifacts.apis.io/clumio/lifecycle/clumio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clumio-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/clumio/changelog/clumio-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clumio-changelog.yml
- group: auth
  href: https://artifacts.apis.io/clumio/authentication/clumio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clumio-authentication.yml
- group: design
  href: https://artifacts.apis.io/clumio/conformance/clumio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clumio-conformance.yml
- group: auth
  href: https://artifacts.apis.io/clumio/conformance/clumio-conformance.yml
  title: ''
  type: Compliance
  url: conformance/clumio-conformance.yml
- group: design
  href: https://artifacts.apis.io/clumio/data-model/clumio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clumio-data-model.yml
created: '2026-07-17'
description: 'Clumio (a Commvault company) is a secure, air-gapped backup-as-a-service platform for the public cloud. It delivers fully managed, immutable data protection and on-demand restore for Amazon Web Services (EBS, EC2, RDS, S3, DynamoDB, DocumentDB, Neptune, Iceberg tables, EC2/RDS MSSQL), Google Cloud Storage, and VMware vCenter workloads. Clumio is API-first: its regional REST API lets teams automate AWS/GCP connections, backup policies and protection rules, protection groups, organizational units, users and roles, compliance reports, audit trails, and restore workflows. Authentication uses long-lived signed-JWT bearer tokens (Personal and Service tokens), responses follow HATEOAS/HAL conventions with `_links`, and the API is versioned per resource. First-party Python and Go SDKs and a Terraform provider are published under the clumio-code GitHub org.'
image: https://clumio.com/wp-content/uploads/2021/06/clumio-logo.png
layout: provider
mcp_servers:
- description: Local (stdio) MCP server; 9 tools listed.
  name: Clumio MCP Server
  slug: clumio-terraform-mcp
modified: '2026-10-06'
name: Clumio
nav: Providers
network: true
overview: 'Clumio is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Backup, Data Protection, and Disaster Recovery.


  Clumio''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, changelog, and 19 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 71.7
    operational_transparency: 34.2
  previous_composite: 32.9
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/clumio/clumio-2026-07-25T205738.png
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
- Amazon Web Services
- Storage
- Security
- Compliance
website: https://clumio.com
---
