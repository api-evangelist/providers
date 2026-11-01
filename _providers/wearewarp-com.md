---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Freight quoting, booking, and tracking API.
  name: Warp Freight API
  slug: warp-freight-api
- baseURL: https://stg.wearewarp.com/api/v1
  baseurl_source: declared
  description: '[Get The Postman Collection](https://api.postman.com/collections/43153707-51d60bdf-d837-474b-a3d4-4e6522ad81a8?access_key=PMAT-01JPH7GR5Y1Q3JAT2J8DHJEK4T)'
  name: WARP API Documentation Freight API
  slug: warp-api-documentation-freight-api
artifact_total: 13
asyncapis:
- description: ''
  name: Wearewarp Com Webhooks
  slug: wearewarp-com-webhooks
common:
- group: design
  href: https://artifacts.apis.io/wearewarp-com/rules/wearewarp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/wearewarp-com-rules.yml
- group: design
  href: https://artifacts.apis.io/wearewarp-com/json-ld/wearewarp-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wearewarp-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/wearewarp-com/vocabulary/wearewarp-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wearewarp-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/wearewarp-com/asyncapi/wearewarp-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/wearewarp-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/wearewarp-com/data-model/wearewarp-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wearewarp-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/wearewarp-com/changelog/wearewarp-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/wearewarp-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/wearewarp-com/authentication/wearewarp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wearewarp-com-authentication.yml
- group: operate
  href: https://artifacts.apis.io/wearewarp-com/lifecycle/wearewarp-com-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/wearewarp-com-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.wearewarp.com/status
- group: design
  href: https://artifacts.apis.io/wearewarp-com/lifecycle/wearewarp-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wearewarp-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wearewarp-com/errors/wearewarp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wearewarp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wearewarp-com/conformance/wearewarp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wearewarp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wearewarp-com/llms/wearewarp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wearewarp-com-llms.txt
- group: other
  href: https://artifacts.apis.io/wearewarp-com/a2a/wearewarp-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/wearewarp-com-a2a.yml
- group: agent
  href: https://artifacts.apis.io/wearewarp-com/well-known/wearewarp-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wearewarp-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/wearewarp-com/hosts/wearewarp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wearewarp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/wearewarp-com/vendors/wearewarp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wearewarp-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wearewarp.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wearewarp.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.wearewarp.com/news
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.wearewarp.com/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.wearewarp.com/how-to-set-up-a-supply-chain/checklist
- group: docs
  title: ''
  type: Documentation
  url: https://developer.wearewarp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.wearewarp.com/freight-api
- group: auth
  href: https://artifacts.apis.io/wearewarp-com/security/wearewarp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wearewarp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wearewarp.com
created: '2026-10-25'
description: Warp provides freight services—including LTL, FTL, box‑truck, cargo‑van, parcel, ocean, air and drayage—through an open‑source network. It serves shippers of any size in the United States, offering instant quotes, live tracking and a free TMS API. The company also operates fulfillment warehouses and offers custom logistics programs.
image: https://www.wearewarp.com/opengraph-image?8f75bb7b5475a2e0
json_schemas:
- name: FreightQuoteBody
  property_count: 8
  slug: wearewarp-com-freight-quote-body
- name: GetEventsSuccess
  property_count: 1
  slug: wearewarp-com-get-events-success
- name: MultiStopsBookingBody
  property_count: 4
  slug: wearewarp-com-multi-stops-booking-body
- name: MultiStopsQuoteBody
  property_count: 10
  slug: wearewarp-com-multi-stops-quote-body
- name: QuoteBody
  property_count: 10
  slug: wearewarp-com-quote-body
- name: QuoteResult
  property_count: 11
  slug: wearewarp-com-quote-result
jsonld:
- class_count: 37
  name: Wearewarp Com Context
  property_count: 112
  slug: wearewarp-com-context
layout: provider
modified: '2026-10-25'
name: WARP
nav: Providers
network: true
overview: 'WARP publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Documentation Freight API, and 1 more. Tagged areas include Freight, LTL, FTL, Logistics, and Shipping.


  The WARP catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  WARP''s developer surface includes changelog, authentication, getting-started guide, documentation, API reference, and 21 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: WARP API Rules
  rule_count: 18
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 2
  slug: wearewarp-com-rules
score:
  band: developing
  composite: 48.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 70.8
    developer_ergonomics: 50.0
    discoverability: 67.9
    operational_transparency: 47.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Wearewarp Com Authentication
  slug: wearewarp-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Wearewarp Com Domain Security
  slug: wearewarp-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wearewarp-com
tags:
- Freight
- LTL
- FTL
- Logistics
- Shipping
- Warehousing
- API
- Supply Chain
website: https://wearewarp.com
---
