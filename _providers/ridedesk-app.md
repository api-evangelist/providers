---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Machine-readable Contract Protocol (MCP) endpoint providing tools list and documentation for RideDesk.
  name: RideDesk MCP
  slug: ridedesk-mcp
- baseURL: https://your-company.ridedesk.app
  baseurl_source: declared
  description: 'ridedesk-app API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: ridedesk-app API
  slug: ridedesk-app-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/ridedesk-app/plans/ridedesk-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ridedesk-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ridedesk-app/rules/ridedesk-app-rules.yml
  title: ''
  type: Spectral
  url: rules/ridedesk-app-rules.yml
- group: design
  href: https://artifacts.apis.io/ridedesk-app/json-ld/ridedesk-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ridedesk-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/ridedesk-app/vocabulary/ridedesk-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ridedesk-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/ridedesk-app/data-model/ridedesk-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ridedesk-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/ridedesk-app/conformance/ridedesk-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ridedesk-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ridedesk-app/llms/ridedesk-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ridedesk-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/ridedesk-app/mcp/ridedesk-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ridedesk-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ridedesk-app/well-known/ridedesk-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ridedesk-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/ridedesk-app/hosts/ridedesk-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ridedesk-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/ridedesk-app/vendors/ridedesk-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ridedesk-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ridedesk.app/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://ridedesk.app/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ridedesk.app/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://ridedesk.app/login
- group: auth
  href: https://artifacts.apis.io/ridedesk-app/security/ridedesk-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ridedesk-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ridedesk.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ridedesk.app/developers
- group: docs
  title: ''
  type: Documentation
  url: https://ridedesk.app/developers
- group: docs
  title: ''
  type: APIReference
  url: https://ridedesk.app/api/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://ridedesk.app/pricing
- group: operate
  title: ''
  type: Support
  url: https://ridedesk.app/
created: '2026-10-30'
description: RideDesk is an all‑in‑one platform for transfer and car‑rental businesses, offering bookings, dispatch, invoicing, payments and WhatsApp integration as a white‑label solution that can run on a custom domain. The service replaces a patchwork of tools with a single system built for premium ground transport, providing server‑priced quotes, automated approvals, driver portals, and full export of data. It supports API access via an MCP endpoint for AI agents and developers, and offers free and paid plans.
image: https://ridedesk.app/icon-512.png
json_schemas:
- name: PostApiQuoteProgressRequest
  property_count: 2
  slug: ridedesk-app-post-api-quote-progress-request
- name: PostApiQuoteRequest
  property_count: 5
  slug: ridedesk-app-post-api-quote-request
- name: PostApiStripeWalletRequest
  property_count: 2
  slug: ridedesk-app-post-api-stripe-wallet-request
- name: Ridedesk Mcp Tools
  property_count: 0
  slug: ridedesk-mcp-tools
jsonld:
- class_count: 3
  name: Ridedesk App Context
  property_count: 9
  slug: ridedesk-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at ridedesk.app.
  name: ridedesk-app MCP Server
  slug: ridedesk-app-mcp-yml
modified: '2026-10-30'
name: ridedesk-app
nav: Providers
network: true
overview: 'ridedesk-app is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Transportation, Dispatch, Booking, SaaS, and API.


  The ridedesk-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ridedesk-app''s developer surface includes documentation, API reference, pricing, support, and 18 more developer resources.'
plans:
- name: Ridedesk App Plans Pricing
  plan_count: 3
  slug: ridedesk-app-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: ridedesk-app API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: ridedesk-app-rules
scopes:
- name: Ridedesk App Scopes
  scope_count: 0
  slug: ridedesk-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 19.4
    developer_ergonomics: 31.0
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Ridedesk App Authentication
  slug: ridedesk-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Ridedesk App Domain Security
  slug: ridedesk-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ridedesk-app
tags:
- Transportation
- Dispatch
- Booking
- SaaS
- API
website: https://ridedesk.app/
---
