---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Real‑time UK TPS/CTPS screening API for HubSpot and other CRMs. Supports single and bulk lookups, a personal suppression list, and audit‑ready logs. Bearer‑token authentication; base URL https://api.t
  name: TPSClear API
  slug: tpsclear-api
- baseURL: https://api.tpsclear.co.uk
  baseurl_source: declared
  description: 'tpsclear-co-uk API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: tpsclear-co-uk API
  slug: tpsclear-co-uk-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/tpsclear-co-uk/rate-limits/tpsclear-co-uk-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tpsclear-co-uk-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/tpsclear-co-uk/rules/tpsclear-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/tpsclear-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/tpsclear-co-uk/json-ld/tpsclear-co-uk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tpsclear-co-uk-context.jsonld
- group: design
  href: https://artifacts.apis.io/tpsclear-co-uk/vocabulary/tpsclear-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tpsclear-co-uk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tpsclear-co-uk/data-model/tpsclear-co-uk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tpsclear-co-uk-data-model.yml
- group: auth
  href: https://artifacts.apis.io/tpsclear-co-uk/authentication/tpsclear-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tpsclear-co-uk-authentication.yml
- group: design
  href: https://artifacts.apis.io/tpsclear-co-uk/errors/tpsclear-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tpsclear-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tpsclear-co-uk/conformance/tpsclear-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tpsclear-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tpsclear-co-uk/llms/tpsclear-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tpsclear-co-uk-llms.txt
- group: agent
  href: https://artifacts.apis.io/tpsclear-co-uk/mcp/tpsclear-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tpsclear-co-uk-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tpsclear-co-uk/well-known/tpsclear-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tpsclear-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/tpsclear-co-uk/hosts/tpsclear-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tpsclear-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/tpsclear-co-uk/vendors/tpsclear-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tpsclear-co-uk-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tpsclear.co.uk/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.tpsclear.co.uk</code
- group: auth
  href: https://artifacts.apis.io/tpsclear-co-uk/security/tpsclear-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tpsclear-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tpsclear.co.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://tpsclear.co.uk/developers
- group: docs
  title: ''
  type: APIReference
  url: https://tpsclear.co.uk/developers#endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://tpsclear.co.uk/developers#getting-started
- group: operate
  title: ''
  type: Support
  url: https://tpsclear.co.uk/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://tpsclear.co.uk/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tpsclear.co.uk/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tpsclear.co.uk/privacy
- group: start
  title: ''
  type: SignUp
  url: https://tpsclear.co.uk/account
created: '2026-10-31'
description: TPSClear provides a real‑time UK Telephone Preference Service (TPS) and Corporate TPS (CTPS) screening API integrated with HubSpot. It allows single or bulk phone‑number lookups against the official registers, returning immediate compliance verdicts. The service also offers a suppression list to store opt‑out numbers, audit‑ready logs, and the ability to manage the list via the same API. Plans start at £95 per month with no annual lock‑in, and a free trial key is available for testing. TPSClear aims to replace costly legacy list‑cleaning solutions with a modern, on‑demand API.
image: https://tpsclear.co.uk/logos/tps.png
json_schemas:
- name: GetV1ScreenIdResponse
  property_count: 8
  slug: tpsclear-co-uk-get-v1-screen-id-response
- name: GetV1UsageResponse
  property_count: 6
  slug: tpsclear-co-uk-get-v1-usage-response
- name: PostV1ConsentsResponse
  property_count: 7
  slug: tpsclear-co-uk-post-v1-consents-response
- name: PostV1ScreenResponse
  property_count: 6
  slug: tpsclear-co-uk-post-v1-screen-response
- name: PostV1SuppressionsResponse
  property_count: 7
  slug: tpsclear-co-uk-post-v1-suppressions-response
- name: PostWebhooksTpsclearRequest
  property_count: 5
  slug: tpsclear-co-uk-post-webhooks-tpsclear-request
jsonld:
- class_count: 27
  name: Tpsclear Co Uk Context
  property_count: 53
  slug: tpsclear-co-uk-context
layout: provider
mcp_servers:
- description: Remote MCP server at tpsclear.co.uk.
  name: tpsclear-co-uk MCP Server
  slug: tpsclear-co-uk-mcp-yml
modified: '2026-10-31'
name: tpsclear-co-uk
nav: Providers
network: true
overview: 'tpsclear-co-uk is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Telecommunications, UK, HubSpot, Phone Screening, and API.


  The tpsclear-co-uk catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tpsclear-co-uk''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Tpsclear Co Uk Plans
  plan_count: 14
  slug: tpsclear-co-uk-plans
random_paper: 18
rate_limits:
- limit_count: 1
  name: Tpsclear Co Uk Rate Limits
  slug: tpsclear-co-uk-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: tpsclear-co-uk API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: tpsclear-co-uk-rules
scopes:
- name: Tpsclear Co Uk Scopes
  scope_count: 0
  slug: tpsclear-co-uk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 95.7
    catalog_earned_first_party: 0.0
    catalog_gap: 19.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 55.4
    developer_ergonomics: 54.8
    discoverability: 65.0
    operational_transparency: 34.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 35.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tpsclear Co Uk Authentication
  slug: tpsclear-co-uk-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tpsclear Co Uk Domain Security
  slug: tpsclear-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tpsclear-co-uk
tags:
- Telecommunications
- UK
- HubSpot
- Phone Screening
- API
- Compliance
website: https://tpsclear.co.uk/
---
