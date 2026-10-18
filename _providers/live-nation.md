---
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-10-17'
api_count: 9
apis:
- description: Ticketing and event APIs provided via Ticketmaster developer portal.
  name: Live Nation API
  slug: live-nation-api-2
- baseURL: https://app.ticketmaster.eu
  baseurl_source: declared
  description: The Bookings API from Live Nation — 2 operation(s) for bookings.
  name: Live Nation Bookings API
  slug: live-nation-bookings-api
- baseURL: https://app.ticketmaster.eu
  baseurl_source: declared
  description: The Events API from Live Nation — 4 operation(s) for events.
  name: Live Nation Events API
  slug: live-nation-events-api
- baseURL: https://app.ticketmaster.eu
  baseurl_source: declared
  description: The Healhtcheck API from Live Nation — 1 operation(s) for healhtcheck.
  name: Live Nation Healhtcheck API
  slug: live-nation-healhtcheck-api
- baseURL: https://app.ticketmaster.eu
  baseurl_source: declared
  description: The Manifests API from Live Nation — 1 operation(s) for manifests.
  name: Live Nation Manifests API
  slug: live-nation-manifests-api
- baseURL: https://app.ticketmaster.eu
  baseurl_source: declared
  description: The Mfxapi API from Live Nation — 3 operation(s) for mfxapi.
  name: Live Nation Mfxapi API
  slug: live-nation-mfxapi-api
- baseURL: https://app.ticketmaster.eu
  baseurl_source: declared
  description: The Orders API from Live Nation — 2 operation(s) for orders.
  name: Live Nation Orders API
  slug: live-nation-orders-api
- baseURL: https://app.ticketmaster.eu
  baseurl_source: declared
  description: The Tm 3Pi Api API from Live Nation — 2 operation(s) for tm 3pi api.
  name: Live Nation Tm 3Pi API
  slug: live-nation-tm-3pi-api-api
- baseURL: https://app.ticketmaster.eu
  baseurl_source: declared
  description: The Health Check API from Live Nation — 1 operation(s) for health check.
  name: Live Nation Health Check API
  slug: live-nation-health-check-api
artifact_total: 19
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/live-nation/refs/heads/main/rules/live-nation-rules.yml
  title: ''
  type: Spectral
  url: rules/live-nation-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/live-nation/refs/heads/main/json-ld/live-nation-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/live-nation-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/live-nation/refs/heads/main/vocabulary/live-nation-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/live-nation-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/live-nation/refs/heads/main/data-model/live-nation-data-model.yml
  title: ''
  type: DataModel
  url: data-model/live-nation-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/live-nation/refs/heads/main/authentication/live-nation-authentication.yml
  title: ''
  type: Authentication
  url: authentication/live-nation-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/live-nation/refs/heads/main/conformance/live-nation-conformance.yml
  title: ''
  type: Conformance
  url: conformance/live-nation-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/live-nation/refs/heads/main/hosts/live-nation-hosts.yml
  title: ''
  type: Hosts
  url: hosts/live-nation-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/live-nation/refs/heads/main/vendors/live-nation-vendors.yml
  title: ''
  type: Vendors
  url: vendors/live-nation-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://www.livenation.com/help
- group: start
  title: ''
  type: GettingStarted
  url: http://developer.ticketmaster.com/products-and-docs/apis/getting-started/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/live-nation/refs/heads/main/security/live-nation-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/live-nation-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.livenation.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.ticketmaster.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.ticketmaster.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.ticketmaster.com
coverage:
  checked: '2026-10-13'
  detail: Access to the Live Nation API requires a partner login via the Ticketmaster developer portal.
  evidence:
  - status: 401
    url: https://api.livenation.com/graphql
  reason: partner-login
  state: gated
created: '2026-10-13'
description: Live Nation is a global entertainment company that produces, promotes, and sells tickets for live events, including concerts, festivals, and theater productions. It operates a network of venues and partners with artists and brands to deliver experiences worldwide. The company also owns Ticketmaster, providing a comprehensive ticketing platform. Through its digital services, Live Nation offers fans access to event information, ticket purchasing, and exclusive content, while supporting artists with promotion and touring logistics.
image: https://assets.livenationcdn.com/uploads/b9a18840-8205-44c4-9914-5ec9d9b1f75a.png
json_schemas:
- name: GetEventsResponse
  property_count: 2
  slug: live-nation-get-events-response
- name: GetHealhtcheckResponse
  property_count: 3
  slug: live-nation-get-healhtcheck-response
- name: GetHealthcheckResponse
  property_count: 3
  slug: live-nation-get-healthcheck-response
- name: PostOrdersRequest
  property_count: 1
  slug: live-nation-post-orders-request
- name: PostTm3PiApiLoginRequest
  property_count: 3
  slug: live-nation-post-tm3-pi-api-login-request
- name: PostTm3PiApiLoginResponse
  property_count: 4
  slug: live-nation-post-tm3-pi-api-login-response
jsonld:
- class_count: 20
  name: Live Nation Context
  property_count: 27
  slug: live-nation-context
layout: provider
modified: '2026-10-13'
name: Live Nation
nav: Providers
network: true
overview: 'Live Nation is listed with 9 APIs on the [APIs.io](https://apis.io/) network, including Bookings API, Events API, Healhtcheck API, and 6 more. Tagged areas include Entertainment, Ticketing, Live Events, Music, and Technology.


  The Live Nation catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Live Nation''s developer surface includes authentication, support, getting-started guide, documentation, API reference, and 10 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Live Nation API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: live-nation-rules
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 54.8
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Live Nation Authentication
  slug: live-nation-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Live Nation Domain Security
  slug: live-nation-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: live-nation
tags:
- Entertainment
- Ticketing
- Live Events
- Music
- Technology
website: https://www.livenation.com
---
