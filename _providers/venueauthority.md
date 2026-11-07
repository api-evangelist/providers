---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    event_surface_described: unknown
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://venueauthority.com
  baseurl_source: spec
  description: Create and download workspace-scoped evidence exports.
  name: Venue Authority Audit Exports API
  slug: venueauthority-audit-exports-api
- baseURL: https://venueauthority.com
  baseurl_source: spec
  description: Read supported sources, record counts, availability, and freshness.
  name: Venue Authority Coverage API
  slug: venueauthority-coverage-api
- baseURL: https://venueauthority.com
  baseurl_source: spec
  description: Register endpoints and inspect delivery attempts.
  name: Venue Authority Webhooks API
  slug: venueauthority-webhooks-api
- baseURL: https://venueauthority.com
  baseurl_source: spec
  description: The Facilities API from Venue Authority — 1 operation(s) for facilities.
  name: Venue Authority Facilities API
  slug: venueauthority-facilities-api
- baseURL: https://venueauthority.com
  baseurl_source: spec
  description: The Portfolios API from Venue Authority — 4 operation(s) for portfolios.
  name: Venue Authority Portfolios API
  slug: venueauthority-portfolios-api
- baseURL: https://venueauthority.com
  baseurl_source: spec
  description: The Resolve API from Venue Authority — 1 operation(s) for resolve.
  name: Venue Authority Resolve API
  slug: venueauthority-resolve-api
artifact_total: 8
common:
- group: other
  title: ''
  type: APIsJSON
  url: https://venueauthority.com/apis.json
- group: agent
  title: ''
  type: LLMsTxt
  url: https://venueauthority.com/llms.txt
- group: company
  title: ''
  type: Website
  url: https://venueauthority.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://venueauthority.com/developers
- group: commercial
  title: ''
  type: Plans
  url: https://venueauthority.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://venueauthority.com/status
- group: commercial
  title: ''
  type: TermsOfService
  url: https://venueauthority.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://venueauthority.com/privacy
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://venueauthority.com/trust/api-key-and-tenant-security
- group: operate
  title: ''
  type: Support
  url: https://venueauthority.com/support
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/kingymon1/venue-authority-api
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kingymon1/venue-authority-api/tree/main/packages/node-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/kingymon1/venue-authority-api/tree/main/packages/python-sdk
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/kingymon1/venue-authority-api/tree/main/packages/mcp-server
- group: build
  title: ''
  type: GitHubRelease
  url: https://github.com/kingymon1/venue-authority-api/releases/tag/clients-v0.1.0
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kingymon11-8337942/venue-authority/overview
- group: docs
  title: ''
  type: PostmanDocumentation
  url: https://documenter.getpostman.com/view/57620096/2sBYArVYPE
created: '2026-08-21'
description: Venue Authority is a self-serve facility verification and monitoring API for payment facilitators, marketplaces, KYB providers and restaurant platforms working with food-service businesses. It matches a business name and street address to a supported regulator facility record, returns source-linked evidence for that match, and supports ongoing portfolio monitoring so a change at the regulator surfaces after onboarding rather than at the next manual review. The public contract is an OpenAPI 3.1 document of 12 paths and 15 operations, authenticated with a bearer API key, and the provider tags every operation into five groups — resolution and evidence, coverage, watchlists, webhooks and audit exports — which is how it is carried here as five per-resource documents. Coverage is enumerated by the API itself rather than described in prose, and the provider publishes an APIs.json, llms.txt, llms-full.txt, a Postman collection and a machine-readable error catalogue alongside the contract,
  plus MIT-licensed Node.js, Python and MCP client packages released on GitHub with checksummed build artifacts.
image: https://venueauthority.com/venue-authority-mark.svg
layout: provider
mcp_servers:
- description: ''
  name: Venue Authority MCP Server
  slug: mcp-server
modified: '2026-08-21'
name: Venue Authority
nav: Providers
network: true
overview: 'Venue Authority publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit Exports API, Coverage API, Webhooks API, and 3 more. Tagged areas include Food Service, facility verification, Merchant Onboarding, regulator records, and Monitoring.


  The Venue Authority catalog on APIs.io includes 1 Spectral governance ruleset.


  Venue Authority''s developer surface includes support and 16 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Venue Authority API Rules
  rule_count: 56
  severity_counts:
    error: 52
    hint: 0
    info: 3
    warn: 1
  slug: venueauthority-rules
score:
  band: developing
  composite: 43.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 33.5
    catalog_earned_first_party: 0.0
    catalog_gap: 81.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 34.2
    contract_governance: 13.6
    contract_quality: 52.8
    developer_ergonomics: 66.7
    discoverability: 58.3
    operational_transparency: 28.9
  previous_composite: 42.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/venueauthority/venueauthority-2026-09-02T165648.png
slug: venueauthority
tags:
- Food Service
- facility verification
- Merchant Onboarding
- regulator records
- Monitoring
- KYB
- Payment Facilitators
- Marketplace
- restaurant platforms
website: https://venueauthority.com
---
