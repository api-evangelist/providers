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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 65
  human_in_the_loop: 24
  name: Getcircuit Com Agentic Access
  operation_count: 105
  slug: getcircuit-com-agentic-access
  summary_line: 105 operations · 65 acting · 24 human-in-the-loop
api_count: 3
apis:
- baseURL: https://api.spoke.com/connect/v1
  baseurl_source: declared
  description: Look up the couriers that deliver your orders.
  name: Circuit Couriers API
  slug: getcircuit-com-couriers-api
- baseURL: https://api.spoke.com/public/v0.2b
  baseurl_source: declared
  description: Endpoints to operate on [Depots](/docs/models/depot) resources. This resource is currently read-only on the API.
  name: Circuit Depots API
  slug: getcircuit-com-depots-api
- baseURL: https://api.spoke.com/public/v0.2b
  baseurl_source: declared
  description: Endpoints to operate on [Drivers](/docs/models/driver) resources.
  name: Circuit Drivers API
  slug: getcircuit-com-drivers-api
- baseURL: https://api.spoke.com/public/v0.2b
  baseurl_source: declared
  description: Endpoints to operate on [Plans](/docs/models/plan) resources when it's pending re-optimization and re-distribution. You must use these endpoints to apply the changes when any [Live Stops](#tag/Live-St
  name: Circuit Live Plans API
  slug: getcircuit-com-live-plans-api
- baseURL: https://api.spoke.com/public/v0.2b
  baseurl_source: declared
  description: Endpoints to operate on [Stop](/docs/models/stop) resources when the plan is already optimized and therefore not writable. All the endpoints return the field `pending`. This field indicates whether th
  name: Circuit Live Stops API
  slug: getcircuit-com-live-stops-api
- baseURL: https://api.spoke.com/public/v1
  baseurl_source: declared
  description: Endpoints to operate on Members resources.
  name: Circuit Members API
  slug: getcircuit-com-members-api
- baseURL: https://api.spoke.com/public/v0.2b
  baseurl_source: declared
  description: Endpoints to operate on [Operations](/docs/models/operation) resources.
  name: Circuit Operations API
  slug: getcircuit-com-operations-api
- baseURL: https://api.spoke.com/connect/v1
  baseurl_source: declared
  description: Create, submit, and track delivery orders, and download their printable PDF labels.
  name: Circuit Orders API
  slug: getcircuit-com-orders-api
- baseURL: https://api.spoke.com/connect/v1
  baseurl_source: declared
  description: Look up the pickup locations your orders ship from.
  name: Circuit Pickup Locations API
  slug: getcircuit-com-pickup-locations-api
- baseURL: https://api.spoke.com/public/v0.2b
  baseurl_source: declared
  description: Endpoints to operate on [Plans](/docs/models/plan) resources.
  name: Circuit Plans API
  slug: getcircuit-com-plans-api
- baseURL: https://api.spoke.com/public/v0.2b
  baseurl_source: declared
  description: Endpoints to operate on [Routes](/docs/models/route) resources. This resource is currently read-only on the API.
  name: Circuit Routes API
  slug: getcircuit-com-routes-api
- baseURL: https://api.spoke.com/public/v0.2b
  baseurl_source: declared
  description: Endpoints to operate on [Stop](/docs/models/stop) resources. For any [Plans](/docs/models/plan) created before 2023-04-01 the stop collections and all related operations will not be available. For any
  name: Circuit Stops API
  slug: getcircuit-com-stops-api
- baseURL: https://api.spoke.com/public/v0.2b
  baseurl_source: declared
  description: Endpoints to retrieve [Custom Stop Properties](/docs/models/customStopProperty).
  name: Circuit Team API
  slug: getcircuit-com-team-api
- baseURL: https://api.spoke.com/public/v0.2b
  baseurl_source: declared
  description: Endpoints to operate on [Unassigned Stop](/docs/models/unassignedStop) resources.
  name: Circuit Unassigned Stops API
  slug: getcircuit-com-unassigned-stops-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/getcircuit-com/agentic-access/getcircuit-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/getcircuit-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/getcircuit-com/rules/getcircuit-com-rules.yml
  title: ''
  type: Spectral
  url: rules/getcircuit-com-rules.yml
- group: design
  href: https://artifacts.apis.io/getcircuit-com/json-ld/getcircuit-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/getcircuit-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/getcircuit-com/vocabulary/getcircuit-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/getcircuit-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/getcircuit-com/data-model/getcircuit-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getcircuit-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/getcircuit-com/errors/getcircuit-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getcircuit-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/getcircuit-com/conformance/getcircuit-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getcircuit-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/getcircuit-com/llms/getcircuit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getcircuit-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/getcircuit-com/well-known/getcircuit-com-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/getcircuit-com-help-security.txt
- group: agent
  href: https://artifacts.apis.io/getcircuit-com/well-known/getcircuit-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getcircuit-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/getcircuit-com/hosts/getcircuit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getcircuit-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getcircuit-com/vendors/getcircuit-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getcircuit-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://spoke.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://spoke.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.dispatch.spoke.com/docs/v1/webhooks/getting-started/best-practices
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dispatch.spoke.com/
- group: auth
  href: https://artifacts.apis.io/getcircuit-com/authentication/getcircuit-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getcircuit-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/getcircuit-com/security/getcircuit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getcircuit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spoke.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.dispatch.spoke.com/api/v1
coverage:
  checked: '2026-10-29'
  detail: OpenAPI spec found at https://developer.dispatch.spoke.com/openapi-v1.json belongs to Spoke, not Circuit.
  evidence:
  - status: 200
    url: https://developer.dispatch.spoke.com/openapi-v1.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Circuit, operating under the Spoke brand, provides a logistics platform that enables businesses to manage deliveries, drivers, and dispatch operations through a modern API. The service offers tools for route planning, driver tracking, and real‑time delivery analytics, supporting integration with third‑party systems via RESTful endpoints. Circuit’s platform is designed for scalability and includes comprehensive documentation, SDKs, and support resources for developers building transportation and logistics solutions.
image: https://cdn.sanity.io/images/mod8xlf1/production/fbf3cafe7d906daff1badcdeb39789a254f28a98-1200x630.jpg?w=1200&h=630&fm=jpg&q=90
jsonld:
- class_count: 24
  name: Getcircuit Com Context
  property_count: 77
  slug: getcircuit-com-context
layout: provider
modified: '2026-10-29'
name: Circuit
nav: Providers
network: true
overview: 'Circuit publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Couriers API, Depots API, Drivers API, and 11 more. Tagged areas include Company, Logistics, Delivery, and Platform.


  The Circuit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Circuit''s developer surface includes getting-started guide, API reference, authentication, and 17 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Circuit API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: getcircuit-com-rules
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 58.7
    developer_ergonomics: 25.0
    discoverability: 60.7
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 39.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/getcircuit-com/getcircuit-com-2026-11-03T132655.png
security:
- kind: authentication
  name: Getcircuit Com Authentication
  slug: getcircuit-com-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Getcircuit Com Domain Security
  slug: getcircuit-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: getcircuit-com
tags:
- Company
- Logistics
- Delivery
- Platform
website: https://spoke.com/
---
