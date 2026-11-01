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
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: The CrateDB Cloud REST API manages CrateDB Cloud resources — organizations, regions, projects, clusters, products, users, roles, subscriptions, and audit logs. Authentication uses HTTP Basic auth with
  name: CrateDB Cloud API
  slug: cratedb-cloud-api
- description: 'CrateDB''s native developer interface: a JSON-over-HTTP SQL endpoint. Clients POST a JSON body ({"stmt": "...", "args": [...], "bulk_args": [[...]]}) to /_sql (default port 4200) and receive cols/rows/'
  name: CrateDB HTTP SQL Endpoint
  slug: cratedb-http-sql-endpoint
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/crate-io/plans/crate-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crate-io-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://cratedb.com/blog/rss.xml
- group: company
  title: ''
  type: Website
  url: https://www.cratedb.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.cratedb.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://cratedb.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://cratedb.com/docs/cloud/en/latest/reference/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://cratedb.com/docs/guide/
- group: operate
  title: ''
  type: Support
  url: https://cratedb.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://community.cratedb.com/
- group: company
  title: ''
  type: Blog
  url: https://cratedb.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crate
- group: commercial
  title: ''
  type: Pricing
  url: https://cratedb.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.cratedb.cloud/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cratedb.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cratedb.com/legal/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://cratedb.statuspage.io/
- group: build
  href: https://artifacts.apis.io/crate-io/packages/crate-io-packages.yml
  title: ''
  type: Packages
  url: packages/crate-io-packages.yml
- group: build
  href: https://artifacts.apis.io/crate-io/packages/crate-io-packages.yml
  title: ''
  type: SDKs
  url: packages/crate-io-packages.yml
- group: build
  href: https://artifacts.apis.io/crate-io/cli/crate-io-cli.yml
  title: ''
  type: CLI
  url: cli/crate-io-cli.yml
- group: agent
  href: https://artifacts.apis.io/crate-io/mcp/crate-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crate-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/crate-io/llms/crate-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crate-io-llms.txt
- group: auth
  href: https://artifacts.apis.io/crate-io/authentication/crate-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/crate-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/crate-io/conventions/crate-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/crate-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/crate-io/errors/crate-io-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/crate-io-error-codes.yml
- group: design
  href: https://artifacts.apis.io/crate-io/lifecycle/crate-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/crate-io-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/crate-io/changelog/crate-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/crate-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/crate-io/conformance/crate-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crate-io-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cratedb.com/security
- group: auth
  href: https://artifacts.apis.io/crate-io/security/crate-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crate-io-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/crate-io/security/crate-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crate-io-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/crate/crate/security
- group: auth
  href: https://artifacts.apis.io/crate-io/security/crate-io-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/crate-io-trust-center.yml
created: '2026-07-17'
description: Crate.io is the company behind CrateDB, a distributed SQL database engineered for real-time analytics on large volumes of operational data. CrateDB unifies time-series, JSON/document, full-text search, vector, geospatial, and relational data behind standard SQL, is PostgreSQL wire-protocol compatible, and is built on Lucene for horizontal scalability and sub-second queries over billions of rows. Developers interact with CrateDB through an HTTP SQL endpoint (POST /_sql on port 4200) and with the managed CrateDB Cloud service through the CrateDB Cloud REST API (https://console.cratedb.cloud/api/v2), which manages organizations, projects, clusters, users, roles, subscriptions, and audit logs. Crate.io is a Speedinvest portfolio company; CrateDB Cloud is certified to ISO 27001 and SOC 2 Type II.
finops:
- has_sources: true
  method: derived
  name: Crate Io Finops
  primary_unit: hour
  service_category: ''
  slug: crate-io-finops
  template: false
image: https://cratedb.com/hubfs/cr-featured-image-23.jpg
layout: provider
mcp_servers:
- description: Official CrateDB MCP Server providing natural-language Text-to-SQL query execution against a CrateDB cluster and retrieval over CrateDB documentation.
  name: Crate Io MCP Server
  slug: cratedb-mcp
modified: '2026-10-06'
name: Crate Io
nav: Providers
network: true
overview: 'Crate Io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Database, SQL, Distributed Database, and Analytics.


  Crate Io''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Crate Io Plans Pricing
  plan_count: 3
  slug: crate-io-plans-pricing
random_paper: 20
score:
  band: developing
  composite: 52.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 65.0
    operational_transparency: 47.4
  previous_composite: 44.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/crate-io/crate-io-2026-07-25T210645.png
security:
- kind: authentication
  name: Crate Io Authentication
  slug: crate-io-authentication
  summary_line: http-basic/http-basic-apikey/jwt · 3 schemes
- kind: domain-security
  name: Crate Io Domain Security
  slug: crate-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crate Io Vulnerability Disclosure
  slug: crate-io-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Crate Io Trust Center
  slug: crate-io-trust-center
  summary_line: SOC 2 Type II, ISO 27001
slug: crate-io
tags:
- Company
- Database
- SQL
- Distributed Database
- Analytics
- Time Series
- Vector Search
- IoT
- Cloud
- Developer Tools
website: https://www.cratedb.com/
---
