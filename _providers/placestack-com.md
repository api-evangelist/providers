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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Placestack Com Agentic Access
  operation_count: 43
  slug: placestack-com-agentic-access
  summary_line: 43 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.placestack.com
  baseurl_source: declared
  description: The credential making the request, its scopes and its credit balance.
  name: placestack-com Account API
  slug: placestack-com-account-api
- baseURL: https://api.placestack.com
  baseurl_source: declared
  description: 'Zoning and development cases: rezonings, variances, special uses, subdivisions and site plans, with their decisions.'
  name: placestack-com Case API
  slug: placestack-com-case-api
- baseURL: https://api.placestack.com
  baseurl_source: declared
  description: Permits and cases filed on monitored places, as events. Each is also sent to webhooks subscribed to its type.
  name: placestack-com Event API
  slug: placestack-com-event-api
- baseURL: https://api.placestack.com
  baseurl_source: declared
  description: States, counties, cities and towns, with their identifiers, boundaries and data coverage.
  name: placestack-com Jurisdiction API
  slug: placestack-com-jurisdiction-api
- baseURL: https://api.placestack.com
  baseurl_source: declared
  description: 'Named lists of saved places: sites, towns and counties, ZIP codes and areas.'
  name: placestack-com List API
  slug: placestack-com-list-api
- baseURL: https://api.placestack.com
  baseurl_source: declared
  description: Monitors on lists, which produce events about the places on a list.
  name: placestack-com Monitor API
  slug: placestack-com-monitor-api
- baseURL: https://api.placestack.com
  baseurl_source: declared
  description: Parcels, with owners, assessed values, buildings, sales and boundaries. Search by address, parcel number, point or area.
  name: placestack-com Parcel API
  slug: placestack-com-parcel-api
- baseURL: https://api.placestack.com
  baseurl_source: declared
  description: Building and trade permits, with their decisions.
  name: placestack-com Permit API
  slug: placestack-com-permit-api
- baseURL: https://api.placestack.com
  baseurl_source: declared
  description: 'Matches for typed text, for search-as-you-type: jurisdictions, addresses and parcel numbers.'
  name: placestack-com Suggestion API
  slug: placestack-com-suggestion-api
- baseURL: https://api.placestack.com
  baseurl_source: declared
  description: Requests, credits spent and the credit balance.
  name: placestack-com Usage API
  slug: placestack-com-usage-api
- baseURL: https://api.placestack.com
  baseurl_source: declared
  description: Webhooks, their deliveries and test events.
  name: placestack-com Webhook API
  slug: placestack-com-webhook-api
- baseURL: https://api.placestack.com
  baseurl_source: declared
  description: Zoning classifications, with the uses each allows and its dimensional standards, cited to the ordinance.
  name: placestack-com Zoning API
  slug: placestack-com-zoning-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/placestack-com/agentic-access/placestack-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/placestack-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/placestack-com/rules/placestack-com-rules.yml
  title: ''
  type: Spectral
  url: rules/placestack-com-rules.yml
- group: design
  href: https://artifacts.apis.io/placestack-com/json-ld/placestack-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/placestack-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/placestack-com/vocabulary/placestack-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/placestack-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/placestack-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/placestack-com/data-model/placestack-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/placestack-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/placestack-com/errors/placestack-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/placestack-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/placestack-com/conformance/placestack-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/placestack-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/placestack-com/llms/placestack-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/placestack-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/placestack-com/well-known/placestack-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/placestack-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/placestack-com/hosts/placestack-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/placestack-com-hosts.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://console.placestack.com/developer/key
- group: auth
  href: https://artifacts.apis.io/placestack-com/authentication/placestack-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/placestack-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/placestack-com/security/placestack-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/placestack-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://placestack.com/
- group: docs
  title: ''
  type: Documentation
  url: https://placestack.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://placestack.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://placestack.com/docs
- group: operate
  title: ''
  type: Support
  url: https://placestack.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://placestack.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://placestack.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://placestack.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://placestack.com/contact
created: '2026-10-30'
description: Placestack provides a comprehensive parcel, permit, and zoning data API for U.S. addresses. It offers an Explorer UI, a RESTful API, and an MCP server designed for AI agents, delivering property ownership, sales history, building permits, zoning regulations, and decision records.
image: https://placestack.com/opengraph-image
json_schemas:
- name: Case
  property_count: 19
  slug: placestack-com-case
- name: Delivery
  property_count: 18
  slug: placestack-com-delivery
- name: Parcel
  property_count: 20
  slug: placestack-com-parcel
- name: Permit
  property_count: 19
  slug: placestack-com-permit
- name: SavedListItem
  property_count: 19
  slug: placestack-com-saved-list-item
- name: Zoning
  property_count: 22
  slug: placestack-com-zoning
jsonld:
- class_count: 120
  name: Placestack Com Context
  property_count: 302
  slug: placestack-com-context
layout: provider
modified: '2026-10-30'
name: placestack-com
nav: Providers
network: true
overview: 'placestack-com publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Case API, Event API, and 9 more. Tagged areas include Company, Real Estate, Data, Geospatial, and Property.


  The placestack-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  placestack-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 16 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: placestack-com API Rules
  rule_count: 17
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 2
  slug: placestack-com-rules
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 59.8
    developer_ergonomics: 39.8
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 46.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/placestack-com/placestack-com-2026-11-03T141253.png
security:
- kind: authentication
  name: Placestack Com Authentication
  slug: placestack-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Placestack Com Domain Security
  slug: placestack-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: parcel-management
  slug: parcel-management
- name: saved-list
  slug: saved-list
slug: placestack-com
tags:
- Company
- Real Estate
- Data
- Geospatial
- Property
website: https://placestack.com/
---
