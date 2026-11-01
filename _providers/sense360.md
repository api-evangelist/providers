---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.6
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Sense360 API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-10-25); not the provider''s own document.'
  name: Sense360 API
  slug: sense360-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/sense360/rate-limits/sense360-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sense360-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/sense360/rules/sense360-rules.yml
  title: ''
  type: Spectral
  url: rules/sense360-rules.yml
- group: design
  href: https://artifacts.apis.io/sense360/json-ld/sense360-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sense360-context.jsonld
- group: design
  href: https://artifacts.apis.io/sense360/vocabulary/sense360-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sense360-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/sense360/data-model/sense360-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sense360-data-model.yml
- group: design
  href: https://artifacts.apis.io/sense360/conformance/sense360-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sense360-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sense360/llms/sense360-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sense360-llms.txt
- group: agent
  href: https://artifacts.apis.io/sense360/well-known/sense360-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sense360-well-known.yml
- group: other
  href: https://artifacts.apis.io/sense360/hosts/sense360-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sense360-hosts.yml
- group: other
  href: https://artifacts.apis.io/sense360/vendors/sense360-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sense360-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://mysense360.com/blogs/news
- group: start
  title: ''
  type: GettingStarted
  url: https://shopify.dev/docs/agents/get-started/quickstart
- group: auth
  href: https://artifacts.apis.io/sense360/security/sense360-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sense360-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mysense360.com
- group: docs
  title: ''
  type: Documentation
  url: https://mysense360.com/pages/about-us
- group: operate
  title: ''
  type: Support
  url: https://mysense360.com/pages/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mysense360.com/policies/privacy-policy
coverage:
  checked: '2026-10-25'
  detail: The company redirects its domain to Medallia and provides no public developer API documentation.
  evidence:
  - status: 301
    url: https://sense360.com
  reason: no-developer-program
  state: none
created: '2026-10-25'
description: Sense360 provides modular ESPHome sensor kits for Home Assistant, offering PoE-powered bathroom and room sensing solutions. Their products include the Sense360 Core hub, RoomIQ for presence, temperature, humidity, and light detection, and VentIQ for bathroom air quality monitoring. Designed for easy integration, the kits enable smart home automations that respond to environmental conditions, improving comfort and energy efficiency.
image: http://mysense360.com/cdn/shop/files/Modular_ESP32_S3_Sensor_Platform6_ac3b22a8-95fe-4986-8bf6-26e837affa82.png?v=1756669202
json_schemas:
- name: GetWellKnownCustomerAccountApiResponse
  property_count: 1
  slug: sense360-get-well-known-customer-account-api-response
- name: GetWellKnownOpenidConfigurationResponse
  property_count: 2
  slug: sense360-get-well-known-openid-configuration-response
- name: PostCustomerApi202610GraphqlResponse
  property_count: 1
  slug: sense360-post-customer-api202610-graphql-response
- name: PostOrgidApi202610GraphqlJsonRequest
  property_count: 1
  slug: sense360-post-orgid-api202610-graphql-json-request
- name: PostOrgidApi202610GraphqlJsonResponse
  property_count: 2
  slug: sense360-post-orgid-api202610-graphql-json-response
- name: PostResponse
  property_count: 1
  slug: sense360-post-response
jsonld:
- class_count: 10
  name: Sense360 Context
  property_count: 11
  slug: sense360-context
layout: provider
modified: '2026-10-25'
name: Sense360
nav: Providers
network: true
overview: 'Sense360 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, HomeAutomation, IoT, Sensors, and ESPHome.


  The Sense360 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sense360''s developer surface includes getting-started guide, documentation, support, and 14 more developer resources.'
random_paper: 23
rate_limits:
- limit_count: 1
  name: Sense360 Rate Limits
  slug: sense360-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Sense360 API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: sense360-rules
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 25.0
    developer_ergonomics: 26.2
    discoverability: 58.9
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 13
      marker_coverage: 100.0
      total: 13
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sense360 Domain Security
  slug: sense360-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sense360
tags:
- Company
- HomeAutomation
- IoT
- Sensors
- ESPHome
website: https://mysense360.com
---
