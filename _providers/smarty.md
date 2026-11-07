---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Smarty Agentic Access
  operation_count: 16
  slug: smarty-agentic-access
  summary_line: 16 operations · 2 acting
api_count: 9
apis:
- baseURL: https://us-street.api.smarty.com/street-address
  baseurl_source: declared
  description: The Lookup API from Smarty — 3 operation(s) for lookup.
  name: Smarty Lookup API
  slug: smarty-lookup-api
- baseURL: https://us-street.api.smarty.com/street-address
  baseurl_source: declared
  description: The street-address API from Smarty — 1 operation(s) for street-address.
  name: Smarty Street Address API
  slug: smarty-street-address-api
- baseURL: https://us-street.api.smarty.com/street-address
  baseurl_source: declared
  description: The us-enrichment API from Smarty — 8 operation(s) for us-enrichment.
  name: Smarty Us Enrichment API
  slug: smarty-us-enrichment-api
- baseURL: https://us-street.api.smarty.com/street-address
  baseurl_source: declared
  description: The US Extract API API from Smarty — 1 operation(s) for us extract api.
  name: Smarty US Extract API
  slug: smarty-us-extract-api-api
- baseURL: https://us-street.api.smarty.com/street-address
  baseurl_source: declared
  description: The Verify API from Smarty — 1 operation(s) for verify.
  name: Smarty Verify API
  slug: smarty-verify-api
artifact_total: 29
collections:
- collection_type: postman
  name: International Address Autocomplete Lookup API
  slug: postman-smarty-lookup-api
- collection_type: postman
  name: International Address Autocomplete Lookup reverse-geo API
  slug: postman-smarty-reverse-geo-api
- collection_type: postman
  name: International Address Autocomplete Lookup street-address API
  slug: postman-smarty-street-address-api
- collection_type: postman
  name: International Address Autocomplete Lookup us-enrichment API
  slug: postman-smarty-us-enrichment-api
- collection_type: postman
  name: International Address Autocomplete Lookup US Extract API API
  slug: postman-smarty-us-extract-api-api
- collection_type: postman
  name: International Address Autocomplete Lookup Verify API
  slug: postman-smarty-verify-api
- collection_type: open
  name: International Address Autocomplete Lookup API
  slug: open-smarty-lookup-api
- collection_type: open
  name: International Address Autocomplete Lookup reverse-geo API
  slug: open-smarty-reverse-geo-api
- collection_type: open
  name: International Address Autocomplete Lookup street-address API
  slug: open-smarty-street-address-api
- collection_type: open
  name: International Address Autocomplete Lookup us-enrichment API
  slug: open-smarty-us-enrichment-api
- collection_type: open
  name: International Address Autocomplete Lookup US Extract API API
  slug: open-smarty-us-extract-api-api
- collection_type: open
  name: International Address Autocomplete Lookup Verify API
  slug: open-smarty-verify-api
common:
- group: other
  href: https://artifacts.apis.io/smarty/capabilities/smarty-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/smarty-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/smarty/overview
- group: agent
  href: https://artifacts.apis.io/smarty/agentic-access/smarty-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/smarty-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/smarty/security/smarty-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smarty-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/smarty/authentication/smarty-authentication.yml
  title: ''
  type: Authentication
  url: authentication/smarty-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.smarty.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.smarty.com/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smartystreets
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smarty
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smarty-digital-llc
- group: company
  title: ''
  type: Blog
  url: https://www.smarty.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.smarty.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.smarty.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.smarty.com/docs/changelog
- group: other
  title: ''
  type: X
  url: https://x.com/smartycompany
- group: commercial
  href: https://artifacts.apis.io/smarty/plans/smarty-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/smarty-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/smarty/rate-limits/smarty-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/smarty-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/smarty/finops/smarty-finops.yml
  title: ''
  type: FinOps
  url: finops/smarty-finops.yml
- group: design
  href: https://artifacts.apis.io/smarty/vocabulary/smarty-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/smarty-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/smarty/json-ld/smarty-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/smarty-context.jsonld
- group: docs
  href: https://artifacts.apis.io/smarty/json-schema/smarty-us-address-request.json
  title: ''
  type: JSONSchema
  url: json-schema/smarty-us-address-request.json
- group: docs
  href: https://artifacts.apis.io/smarty/json-schema/smarty-us-address-response.json
  title: ''
  type: JSONSchema
  url: json-schema/smarty-us-address-response.json
created: '2026-06-12'
description: Smarty (formerly SmartyStreets) is an address intelligence company that provides REST APIs for US and international address verification, validation, geocoding, and autocomplete at high volume. The platform supports over 210 million US addresses including 20 million non-USPS addresses, delivering up to 55 metadata points and ZIP9-level geocodes per lookup. Smarty offers both cloud-hosted and on-premises deployment options, supporting embedded-key and secret-key authentication patterns. APIs are designed for high-throughput workloads, with US address lookups reaching up to 25,000 per second, making Smarty suitable for enterprise address validation pipelines and real-time checkout address autocomplete.
examples:
- key_count: 1
  name: Smarty Us Autocomplete Response
  slug: smarty-us-autocomplete-response
- key_count: 1
  name: Smarty Us Reverse Geocode Response
  slug: smarty-us-reverse-geocode-response
finops:
- has_sources: false
  method: generated
  name: Smarty Finops
  primary_unit: ''
  service_category: ''
  slug: smarty-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/smarty.png
json_schemas:
- name: Smarty US Address Request
  property_count: 12
  slug: smarty-us-address-request
- name: Smarty US Address Response
  property_count: 11
  slug: smarty-us-address-response
jsonld:
- class_count: 6
  name: Smarty Context
  property_count: 46
  slug: smarty-context
layout: provider
modified: '2026-09-16'
name: Smarty
nav: Providers
network: true
overview: 'Smarty publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Lookup API, Street Address API, Us Enrichment API, and 2 more. Tagged areas include Address Verification, Geocoding, Address Autocomplete, ZIP Code, and Address Intelligence.


  The Smarty catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Smarty''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 17 more developer resources.'
plans:
- name: Smarty Plans Pricing
  plan_count: 5
  slug: smarty-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Smarty Rate Limits
  slug: smarty-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Smarty — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: smarty-jsonschema-spectral-rules
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.8
    catalog_earned_first_party: 0.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 18.4
    contract_governance: 23.5
    contract_quality: 60.9
    developer_ergonomics: 25.0
    discoverability: 71.4
    operational_transparency: 42.1
  previous_composite: 37.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 80.0
      total: 5
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
screenshot: https://apis.io/screenshots/smarty/smarty-2026-06-20T194052.png
security:
- kind: authentication
  name: Smarty Authentication
  slug: smarty-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Smarty Domain Security
  slug: smarty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smarty
tags:
- Address Verification
- Geocoding
- Address Autocomplete
- ZIP Code
- Address Intelligence
- Location Data
- International Address
- US Address
- Geospatial
website: https://www.smarty.com/
---
