---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Doorloop Agentic Access
  operation_count: 96
  slug: doorloop-agentic-access
  summary_line: 96 operations · 49 acting
api_count: 2
apis:
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Accounts API from DoorLoop — 2 operation(s) for accounts.
  name: DoorLoop Accounts API
  slug: doorloop-accounts-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Communications API from DoorLoop — 2 operation(s) for communications.
  name: DoorLoop Communications API
  slug: doorloop-communications-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Expenses API from DoorLoop — 2 operation(s) for expenses.
  name: DoorLoop Expenses API
  slug: doorloop-expenses-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Files API from DoorLoop — 3 operation(s) for files.
  name: DoorLoop Files API
  slug: doorloop-files-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Lease Charges API from DoorLoop — 2 operation(s) for lease charges.
  name: DoorLoop Lease Charges API
  slug: doorloop-lease-charges-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Lease Credits API from DoorLoop — 2 operation(s) for lease credits.
  name: DoorLoop Lease Credits API
  slug: doorloop-lease-credits-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Lease Payments API from DoorLoop — 2 operation(s) for lease payments.
  name: DoorLoop Lease Payments API
  slug: doorloop-lease-payments-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Lease Returned Payments API from DoorLoop — 2 operation(s) for lease returned payments.
  name: DoorLoop Lease Returned Payments API
  slug: doorloop-lease-returned-payments-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Leases API from DoorLoop — 6 operation(s) for leases.
  name: DoorLoop Leases API
  slug: doorloop-leases-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Notes API from DoorLoop — 2 operation(s) for notes.
  name: DoorLoop Notes API
  slug: doorloop-notes-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Owners API from DoorLoop — 2 operation(s) for owners.
  name: DoorLoop Owners API
  slug: doorloop-owners-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Portfolios API from DoorLoop — 2 operation(s) for portfolios.
  name: DoorLoop Portfolios API
  slug: doorloop-portfolios-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Properties API from DoorLoop — 2 operation(s) for properties.
  name: DoorLoop Properties API
  slug: doorloop-properties-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Reports API from DoorLoop — 4 operation(s) for reports.
  name: DoorLoop Reports API
  slug: doorloop-reports-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Tasks API from DoorLoop — 3 operation(s) for tasks.
  name: DoorLoop Tasks API
  slug: doorloop-tasks-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Tenants API from DoorLoop — 2 operation(s) for tenants.
  name: DoorLoop Tenants API
  slug: doorloop-tenants-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Units API from DoorLoop — 2 operation(s) for units.
  name: DoorLoop Units API
  slug: doorloop-units-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Users API from DoorLoop — 3 operation(s) for users.
  name: DoorLoop Users API
  slug: doorloop-users-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Vendor Bills API from DoorLoop — 2 operation(s) for vendor bills.
  name: DoorLoop Vendor Bills API
  slug: doorloop-vendor-bills-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Vendor Credits API from DoorLoop — 2 operation(s) for vendor credits.
  name: DoorLoop Vendor Credits API
  slug: doorloop-vendor-credits-api
- baseURL: https://api.doorloop.com
  baseurl_source: declared
  description: The Vendors API from DoorLoop — 2 operation(s) for vendors.
  name: DoorLoop Vendors API
  slug: doorloop-vendors-api
artifact_total: 37
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/agentic-access/doorloop-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/doorloop-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/rules/doorloop-rules.yml
  title: ''
  type: Spectral
  url: rules/doorloop-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/json-ld/doorloop-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/doorloop-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/vocabulary/doorloop-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/doorloop-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/data-model/doorloop-data-model.yml
  title: ''
  type: DataModel
  url: data-model/doorloop-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/errors/doorloop-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/doorloop-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/conformance/doorloop-conformance.yml
  title: ''
  type: Conformance
  url: conformance/doorloop-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/llms/doorloop-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/doorloop-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/mcp/doorloop-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/doorloop-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/well-known/doorloop-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/doorloop-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/well-known/doorloop-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/doorloop-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/hosts/doorloop-hosts.yml
  title: ''
  type: Hosts
  url: hosts/doorloop-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/integrations/doorloop-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/doorloop-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/vendors/doorloop-vendors.yml
  title: ''
  type: Vendors
  url: vendors/doorloop-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/packages/doorloop-packages.yml
  title: ''
  type: SDKs
  url: packages/doorloop-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/packages/doorloop-packages.yml
  title: ''
  type: Packages
  url: packages/doorloop-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.doorloop.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://support.doorloop.com/en/
- group: auth
  title: ''
  type: Security
  url: https://www.doorloop.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.doorloop.com/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.doorloop.com/press
- group: start
  title: ''
  type: Login
  url: https://www.doorloop.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/authentication/doorloop-authentication.yml
  title: ''
  type: Authentication
  url: authentication/doorloop-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/security/doorloop-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/doorloop-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/security/doorloop-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/doorloop-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.doorloop.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.doorloop.com/reference/introduction
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/mezbahalam/doorloop
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/doorloop/
- group: company
  title: ''
  type: Blog
  url: https://www.doorloop.com/blogs/doorloop
- group: commercial
  title: ''
  type: Pricing
  url: https://www.doorloop.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.doorloop.com
- group: other
  title: ''
  type: X
  url: https://x.com/doorloopapp
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/plans/doorloop-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/doorloop-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/rate-limits/doorloop-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/doorloop-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/finops/doorloop-finops.yml
  title: ''
  type: FinOps
  url: finops/doorloop-finops.yml
created: '2026-06-13'
description: DoorLoop is property management software with a REST API for managing properties, units, leases, rent collection, maintenance requests, accounting, and tenant communication. The API provides two-way access to read and write data across nearly every DoorLoop feature, with predictable resource-oriented URLs, JSON-encoded request and response bodies, and standard HTTP response codes. API access is included on the Premium plan.
finops:
- has_sources: false
  method: generated
  name: Doorloop Finops
  primary_unit: ''
  service_category: ''
  slug: doorloop-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/doorloop.png
json_schemas:
- name: fullLeaseCreateRequest
  property_count: 18
  slug: doorloop-full-lease-create-request
- name: Lease-Payment
  property_count: 21
  slug: doorloop-lease-payment
- name: property
  property_count: 12
  slug: doorloop-property
- name: task
  property_count: 0
  slug: doorloop-task
- name: tenant
  property_count: 0
  slug: doorloop-tenant
- name: unit
  property_count: 15
  slug: doorloop-unit
jsonld:
- class_count: 31
  name: Doorloop Context
  property_count: 150
  slug: doorloop-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.doorloop.com over HTTP.
  name: DoorLoop MCP Server
  slug: doorloop
modified: '2026-06-13'
name: DoorLoop
nav: Providers
network: true
overview: 'DoorLoop publishes 21 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Communications API, Expenses API, and 18 more. Tagged areas include Property Management, Real Estate, Leases, Rent Collection, and Maintenance.


  The DoorLoop catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DoorLoop''s developer surface includes support, authentication, documentation, engineering blog, pricing, and 31 more developer resources.'
plans:
- name: Doorloop Plans Pricing
  plan_count: 4
  slug: doorloop-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Doorloop Rate Limits
  slug: doorloop-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: DoorLoop API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 6
  slug: doorloop-rules
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 29.7
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 69.3
    developer_ergonomics: 25.0
    discoverability: 76.7
    operational_transparency: 31.6
  previous_composite: 21.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 21
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 27.8
screenshot: https://raw.githubusercontent.com/api-evangelist/doorloop/refs/heads/main/screenshots/doorloop-2026-06-20T180153.png
security:
- kind: authentication
  name: Doorloop Authentication
  slug: doorloop-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Doorloop Domain Security
  slug: doorloop-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Doorloop Vulnerability Disclosure
  slug: doorloop-vulnerability-disclosure
  summary_line: no policy recorded
slug: doorloop
tags:
- Property Management
- Real Estate
- Leases
- Rent Collection
- Maintenance
- Accounting
- Tenant Communication
website: https://www.doorloop.com
---
