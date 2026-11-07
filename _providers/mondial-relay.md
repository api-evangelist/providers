---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://api.mondialrelay.com/
  baseurl_source: declared
  description: SOAP web service for creating shipments and related operations.
  name: Mondial Relay Web Service
  slug: mondial-relay-web-service
- description: 'Mondial Relay API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Mondial Relay API
  slug: mondial-relay-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/mondial-relay/rules/mondial-relay-rules.yml
  title: ''
  type: Spectral
  url: rules/mondial-relay-rules.yml
- group: design
  href: https://artifacts.apis.io/mondial-relay/json-ld/mondial-relay-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mondial-relay-context.jsonld
- group: design
  href: https://artifacts.apis.io/mondial-relay/vocabulary/mondial-relay-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mondial-relay-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mondial-relay/data-model/mondial-relay-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mondial-relay-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://vdp.inpost.pl/p/Policy?lang=en-gb
- group: design
  href: https://artifacts.apis.io/mondial-relay/conformance/mondial-relay-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mondial-relay-conformance.yml
- group: other
  href: https://artifacts.apis.io/mondial-relay/wsdl/mondialrelay-webservice.wsdl
  title: ''
  type: WSDL
  url: wsdl/mondialrelay-webservice.wsdl
- group: auth
  href: https://artifacts.apis.io/mondial-relay/well-known/mondial-relay-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mondial-relay-security.txt
- group: auth
  href: https://artifacts.apis.io/mondial-relay/well-known/mondial-relay-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/mondial-relay-api-security.txt
- group: agent
  href: https://artifacts.apis.io/mondial-relay/well-known/mondial-relay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mondial-relay-well-known.yml
- group: other
  href: https://artifacts.apis.io/mondial-relay/hosts/mondial-relay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mondial-relay-hosts.yml
- group: other
  href: https://artifacts.apis.io/mondial-relay/vendors/mondial-relay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mondial-relay-vendors.yml
- group: auth
  href: https://artifacts.apis.io/mondial-relay/security/mondial-relay-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/mondial-relay-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/mondial-relay/security/mondial-relay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mondial-relay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mondialrelay.com/
created: '2026-10-27'
description: Mondial Relay provides parcel delivery and locker services across Europe, operating a dense network of over 12,000 lockers and 94,500 pickup points. It offers e‑livraison solutions for both consumers and e‑commerce merchants, enabling flexible parcel sending, tracking, and collection through its web portal and mobile apps. The company focuses on reliable, simple, and convenient logistics for shipments within France and across European markets.
json_schemas:
- name: PostWebServicesAsmxRequest
  property_count: 4
  slug: mondial-relay-post-web-services-asmx-request
- name: PostWebServicesAsmxResponse
  property_count: 6
  slug: mondial-relay-post-web-services-asmx-response
jsonld:
- class_count: 2
  name: Mondial Relay Context
  property_count: 10
  slug: mondial-relay-context
layout: provider
modified: '2026-10-27'
name: Mondial Relay
nav: Providers
network: true
overview: 'Mondial Relay is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Web Service, and 1 more. Tagged areas include Company, Logistics, Parcel Delivery, E-Commerce, and Europe.


  The Mondial Relay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Mondial Relay API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: mondial-relay-rules
score:
  band: emerging
  composite: 13.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 21.9
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 14.4
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mondial-relay/mondial-relay-2026-11-03T135823.png
security:
- kind: domain-security
  name: Mondial Relay Domain Security
  slug: mondial-relay-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Mondial Relay Vulnerability Disclosure
  slug: mondial-relay-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: mondial-relay
tags:
- Company
- Logistics
- Parcel Delivery
- E-Commerce
- Europe
website: https://mondialrelay.com/
---
