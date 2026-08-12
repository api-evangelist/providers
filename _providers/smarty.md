---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Smarty Agentic Access
  operation_count: 19
  slug: smarty-agentic-access
  summary_line: 19 operations · 3 acting
api_count: 6
apis:
- description: The Lookup API from Smarty — 3 operation(s) for lookup.
  name: Smarty Lookup API
  slug: smarty-lookup-api
- description: Operation invlovling reverse geocoding
  name: Smarty reverse-geo API
  slug: smarty-reverse-geo-api
- description: The street-address API from Smarty — 1 operation(s) for street-address.
  name: Smarty street-address API
  slug: smarty-street-address-api
- description: The us-enrichment API from Smarty — 8 operation(s) for us-enrichment.
  name: Smarty us-enrichment API
  slug: smarty-us-enrichment-api
- description: The US Extract API API from Smarty — 1 operation(s) for us extract api.
  name: Smarty US Extract API API
  slug: smarty-us-extract-api-api
- description: The Verify API from Smarty — 1 operation(s) for verify.
  name: Smarty Verify API
  slug: smarty-verify-api
artifact_total: 24
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
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/smarty/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/smarty-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smarty-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/smarty-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smarty-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/smarty-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/smarty-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/smarty-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/smarty-us-address-request.json
- group: docs
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
- name: Smarty Finops
  service_category: ''
  slug: smarty-finops
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
modified: '2026-06-12'
name: Smarty
nav: Providers
network: true
overview: 'Smarty publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Lookup API, reverse-geo API, street-address API, and 3 more. Tagged areas include Address Verification, Geocoding, Address Autocomplete, ZIP Code, and Address Intelligence.


  The Smarty catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Smarty''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 16 more developer resources.'
plans:
- name: Smarty Plans Pricing
  plan_count: 5
  slug: smarty-plans-pricing
random_paper: 92
rate_limits:
- limit_count: 3
  name: Smarty Rate Limits
  slug: smarty-rate-limits
rules:
- name: Smarty API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: smarty-jsonschema-spectral-rules
score:
  band: strong
  composite: 56.6
  delta: -0.6
  facets:
    commercial_clarity: 50.0
    contract_quality: 67.2
    developer_ergonomics: 26.1
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 68.4
  previous_composite: 57.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smarty/refs/heads/main/screenshots/smarty-2026-06-20T194052.png
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
website: https://www.smarty.com/
---
