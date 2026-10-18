---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 8
apis:
- baseURL: https://YOUR_BASE_URL
  baseurl_source: declared
  description: The Activity API from Tripgic — 1 operation(s) for activity.
  name: Tripgic Activity API
  slug: tripgic-activity-api
- baseURL: https://YOUR_BASE_URL
  baseurl_source: declared
  description: The Esim API from Tripgic — 1 operation(s) for esim.
  name: Tripgic Esim API
  slug: tripgic-esim-api
- baseURL: https://YOUR_BASE_URL
  baseurl_source: declared
  description: The Flight API from Tripgic — 1 operation(s) for flight.
  name: Tripgic Flight API
  slug: tripgic-flight-api
- baseURL: https://YOUR_BASE_URL
  baseurl_source: declared
  description: The Hotel API from Tripgic — 1 operation(s) for hotel.
  name: Tripgic Hotel API
  slug: tripgic-hotel-api
- baseURL: https://YOUR_BASE_URL
  baseurl_source: declared
  description: The Service Tour API from Tripgic — 1 operation(s) for service tour.
  name: Tripgic Service Tour API
  slug: tripgic-service-tour-api
- baseURL: https://YOUR_BASE_URL
  baseurl_source: declared
  description: The Train API from Tripgic — 1 operation(s) for train.
  name: Tripgic Train API
  slug: tripgic-train-api
- baseURL: https://YOUR_BASE_URL
  baseurl_source: declared
  description: The Transfer API from Tripgic — 1 operation(s) for transfer.
  name: Tripgic Transfer API
  slug: tripgic-transfer-api
- baseURL: https://YOUR_BASE_URL
  baseurl_source: declared
  description: The Visa API from Tripgic — 1 operation(s) for visa.
  name: Tripgic Visa API
  slug: tripgic-visa-api
artifact_total: 15
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/plans/tripgic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tripgic-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/rules/tripgic-rules.yml
  title: ''
  type: Spectral
  url: rules/tripgic-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/json-ld/tripgic-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tripgic-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/vocabulary/tripgic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tripgic-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/data-model/tripgic-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tripgic-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/changelog/tripgic-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tripgic-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.tripgic.com/security.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/security/tripgic-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/tripgic-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/conformance/tripgic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tripgic-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/llms/tripgic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tripgic-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/hosts/tripgic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tripgic-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/vendors/tripgic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tripgic-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tripgic.com/terms.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tripgic.com/doc/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/security/tripgic-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/tripgic-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/security/tripgic-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tripgic-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tripgic/refs/heads/main/security/tripgic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tripgic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tripgic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tripgic.com/docs.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.tripgic.com/docs.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tripgic.com/pricing.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tripgic.com/privacy.html
- group: operate
  title: ''
  type: Support
  url: https://www.tripgic.com/contact.html
coverage:
  checked: '2026-10-15'
  detail: Swagger UI at developer.tripgic.com renders API docs but provides no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.tripgic.com/swagger/?urls.primaryName=Flight
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-15'
description: Tripgic provides a unified travel API platform aggregating flights, hotels, tours, transfers, car rentals, and more. Their API offers access to GDS and NDC flight data, over 2 million hotel properties, activity tickets, and ancillary services, enabling developers to build comprehensive travel booking solutions. The company emphasizes extensive coverage, flexible integration, and support for various travel partners.
image: https://www.tripgic.com/assets/og-image.png
json_schemas:
- name: PostFlightFlightidResponse
  property_count: 2
  slug: tripgic-post-flight-flightid-response
jsonld:
- class_count: 1
  name: Tripgic Context
  property_count: 2
  slug: tripgic-context
layout: provider
modified: '2026-10-15'
name: Tripgic
nav: Providers
network: true
overview: 'Tripgic is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Activity API, Esim API, Flight API, and 5 more. Tagged areas include Company, Travel, Booking, and Aggregator.


  The Tripgic catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tripgic''s developer surface includes changelog, documentation, API reference, pricing, support, and 18 more developer resources.'
plans:
- name: Tripgic Plans Pricing
  plan_count: 4
  slug: tripgic-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Tripgic API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: tripgic-rules
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 63.2
    catalog_earned_first_party: 12.0
    catalog_gap: 51.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 17.0
    developer_ergonomics: 31.0
    discoverability: 69.6
    operational_transparency: 26.3
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
    score: 29.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Tripgic Domain Security
  slug: tripgic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tripgic Vulnerability Disclosure
  slug: tripgic-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Tripgic Trust Center
  slug: tripgic-trust-center
  summary_line: SOC 2, GDPR
slug: tripgic
tags:
- Company
- Travel
- Booking
- Aggregator
website: https://www.tripgic.com/
---
