---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Shipcloud Agentic Access
  operation_count: 33
  slug: shipcloud-agentic-access
  summary_line: 33 operations · 12 acting
api_count: 2
apis:
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Addresses API from shipcloud — 2 operation(s) for addresses.
  name: shipcloud Addresses API
  slug: shipcloud-addresses-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Carriers API from shipcloud — 1 operation(s) for carriers.
  name: shipcloud Carriers API
  slug: shipcloud-carriers-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Default Returns Address API from shipcloud — 1 operation(s) for default returns address.
  name: shipcloud Default Returns Address API
  slug: shipcloud-default-returns-address-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Default Shipping Address API from shipcloud — 1 operation(s) for default shipping address.
  name: shipcloud Default Shipping Address API
  slug: shipcloud-default-shipping-address-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Invoice Address API from shipcloud — 1 operation(s) for invoice address.
  name: shipcloud Invoice Address API
  slug: shipcloud-invoice-address-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Manifests API from shipcloud — 2 operation(s) for manifests.
  name: shipcloud Manifests API
  slug: shipcloud-manifests-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Me API from shipcloud — 1 operation(s) for me.
  name: shipcloud Me API
  slug: shipcloud-me-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Orders API from shipcloud — 2 operation(s) for orders.
  name: shipcloud Orders API
  slug: shipcloud-orders-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Pickup Dropoff Locations API from shipcloud — 1 operation(s) for pickup dropoff locations.
  name: shipcloud Pickup Dropoff Locations API
  slug: shipcloud-pickup-dropoff-locations-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Pickup Requests API from shipcloud — 2 operation(s) for pickup requests.
  name: shipcloud Pickup Requests API
  slug: shipcloud-pickup-requests-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Shipment Quotes API from shipcloud — 1 operation(s) for shipment quotes.
  name: shipcloud Shipment Quotes API
  slug: shipcloud-shipment-quotes-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Shipments API from shipcloud — 4 operation(s) for shipments.
  name: shipcloud Shipments API
  slug: shipcloud-shipments-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Trackers API from shipcloud — 2 operation(s) for trackers.
  name: shipcloud Trackers API
  slug: shipcloud-trackers-api
- baseURL: https://api.shipcloud.io/v1
  baseurl_source: declared
  description: The Webhooks API from shipcloud — 2 operation(s) for webhooks.
  name: shipcloud Webhooks API
  slug: shipcloud-webhooks-api
artifact_total: 28
asyncapis:
- description: ''
  name: Shipcloud Webhooks
  slug: shipcloud-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/agentic-access/shipcloud-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/shipcloud-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/rate-limits/shipcloud-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/shipcloud-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/rules/shipcloud-shipcloud-developer-portal-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/shipcloud-shipcloud-developer-portal-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/rules/shipcloud-rules.yml
  title: ''
  type: Spectral
  url: rules/shipcloud-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/json-ld/shipcloud-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/shipcloud-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/vocabulary/shipcloud-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/shipcloud-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/asyncapi/shipcloud-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/shipcloud-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/data-model/shipcloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/shipcloud-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/changelog/shipcloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/shipcloud-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/conventions/shipcloud-conventions.yml
  title: ''
  type: Conventions
  url: conventions/shipcloud-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/sandbox/shipcloud-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/shipcloud-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/lifecycle/shipcloud-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/shipcloud-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/lifecycle/shipcloud-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/shipcloud-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/errors/shipcloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/shipcloud-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/conformance/shipcloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/shipcloud-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/overlays/shipcloud-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/shipcloud-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/llms/shipcloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shipcloud-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/well-known/shipcloud-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shipcloud-support-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/well-known/shipcloud-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/shipcloud-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/well-known/shipcloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/shipcloud-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/hosts/shipcloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shipcloud-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/vendors/shipcloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shipcloud-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/packages/shipcloud-packages.yml
  title: ''
  type: SDKs
  url: packages/shipcloud-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/packages/shipcloud-packages.yml
  title: ''
  type: Packages
  url: packages/shipcloud-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/authentication/shipcloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/shipcloud-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/security/shipcloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shipcloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shipcloud.io/
- group: design
  title: ''
  type: SpectralRules
  url: https://github.com/shipcloud/shipcloud-developer-portal/blob/bc60ff1dbb31cede3a2b512127f1bc195dcc41c4/.spectral.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.shipcloud.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.shipcloud.io/concepts/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.shipcloud.io/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.shipcloud.io/
- group: operate
  title: ''
  type: Support
  url: https://developers.shipcloud.io/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.shipcloud.io/de/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.shipcloud.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/shipcloud
- group: start
  title: ''
  type: SignUp
  url: https://app.shipcloud.io/de/users/sign_up?plan=developer
- group: start
  title: ''
  type: Login
  url: https://app.shipcloud.io/users/sign_in/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/shipcloud_devs
created: '2026-10-09'
description: shipcloud (shipcloud GmbH) is a German multi-carrier shipping platform that lets online shops, apps and services create shipments, print labels, request pickups and track parcels across many carriers through a single REST API. Its developer portal at developers.shipcloud.io offers concepts, carrier-specific guides, integration tools, examples, an API reference and an OpenAPI spec, with a free developer plan for testing.
image: https://developers.shipcloud.io/assets/images/logos/shipcloud_logo.png
json_schemas:
- name: current_user
  property_count: 7
  slug: shipcloud-current-user
- name: Order
  property_count: 12
  slug: shipcloud-order
- name: pickup_dropoff_location
  property_count: 16
  slug: shipcloud-pickup-dropoff-location
- name: shipment_put
  property_count: 13
  slug: shipcloud-shipment-put
- name: shipment_response_object
  property_count: 0
  slug: shipcloud-shipment-response-object
- name: shipment
  property_count: 18
  slug: shipcloud-shipment
jsonld:
- class_count: 26
  name: Shipcloud Context
  property_count: 111
  slug: shipcloud-context
layout: provider
modified: '2026-10-09'
name: shipcloud
nav: Providers
network: true
overview: 'shipcloud publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Addresses API, Carriers API, Default Returns Address API, and 11 more. Tagged areas include Company, Shipping, Logistics, Carrier, and Labels.


  The shipcloud catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  shipcloud''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, support, and 32 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 1
  name: Shipcloud Rate Limits
  slug: shipcloud-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: shipcloud API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: shipcloud-rules
- authorship: provider
  effective_rule_count: 41
  extends:
  - spectral:oas
  name: shipcloud — shipcloud developer portal rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: shipcloud-shipcloud-developer-portal-spectral-rules
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 72.6
    developer_ergonomics: 69.0
    discoverability: 73.2
    operational_transparency: 73.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 52.8
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
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 14.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/shipcloud/refs/heads/main/screenshots/shipcloud-2026-10-11T125804.png
security:
- kind: authentication
  name: Shipcloud Authentication
  slug: shipcloud-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Shipcloud Domain Security
  slug: shipcloud-domain-security
  summary_line: DMARC
slug: shipcloud
tags:
- Company
- Shipping
- Logistics
- Carrier
- Labels
- Tracking
- E-Commerce
website: https://www.shipcloud.io/
---
