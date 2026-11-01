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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-10-31'
api_count: 5
apis:
- description: API for accessing WIA Standards data.
  name: WIA Standards API
  slug: wia-standards-api
- baseURL: https://bci.wiastandards.com/api/
  baseurl_source: declared
  description: The Domains API from wiastandards-com — 1 operation(s) for domains.
  name: wiastandards-com Domains API
  slug: wiastandards-com-domains-api
- baseURL: https://bci.wiastandards.com/api/
  baseurl_source: declared
  description: The Keys API from wiastandards-com — 3 operation(s) for keys.
  name: wiastandards-com Keys API
  slug: wiastandards-com-keys-api
- baseURL: https://bci.wiastandards.com/api/
  baseurl_source: declared
  description: The Standards API from wiastandards-com — 7 operation(s) for standards.
  name: wiastandards-com Standards API
  slug: wiastandards-com-standards-api
- baseURL: https://bci.wiastandards.com/api/
  baseurl_source: declared
  description: The Usage API from wiastandards-com — 1 operation(s) for usage.
  name: wiastandards-com Usage API
  slug: wiastandards-com-usage-api
artifact_total: 17
common:
- group: design
  href: https://artifacts.apis.io/wiastandards-com/rules/wiastandards-com-rules.yml
  title: ''
  type: Spectral
  url: rules/wiastandards-com-rules.yml
- group: design
  href: https://artifacts.apis.io/wiastandards-com/json-ld/wiastandards-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/wiastandards-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/wiastandards-com/vocabulary/wiastandards-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wiastandards-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/wiastandards-com/data-model/wiastandards-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wiastandards-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.wiastandards.com/
- group: design
  href: https://artifacts.apis.io/wiastandards-com/conformance/wiastandards-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wiastandards-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/wiastandards-com/llms/wiastandards-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wiastandards-com-llms.txt
- group: other
  href: https://artifacts.apis.io/wiastandards-com/hosts/wiastandards-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wiastandards-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/wiastandards-com/security/wiastandards-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/wiastandards-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/wiastandards-com/security/wiastandards-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wiastandards-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wiastandards.com/
coverage:
  checked: '2026-10-30'
  detail: API endpoint https://bci.wiastandards.com/api/ returns 403 Forbidden, indicating access requires partner login.
  evidence:
  - status: 403
    url: https://bci.wiastandards.com/api/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: WIA Standards (World Certification Industry Association) is a global organization dedicated to developing, maintaining, and promoting certification standards across various industries. With 18 years of experience, it offers over 730 standards covering data exchange, API protocols, digital twins, and interoperability, supporting 24 categories and hundreds of simulators to foster universal compliance and innovation.
image: https://via.placeholder.com/300?text=wiastandards
json_schemas:
- name: PostKeysRequest
  property_count: 1
  slug: wiastandards-com-post-keys-request
- name: PostStandardsSlugValidateRequest
  property_count: 2
  slug: wiastandards-com-post-standards-slug-validate-request
- name: PostV1KeysRequest
  property_count: 1
  slug: wiastandards-com-post-v1-keys-request
- name: PostV1StandardsSecurityValidateRequest
  property_count: 2
  slug: wiastandards-com-post-v1-standards-security-validate-request
jsonld:
- class_count: 4
  name: Wiastandards Com Context
  property_count: 2
  slug: wiastandards-com-context
layout: provider
modified: '2026-10-29'
name: wiastandards-com
nav: Providers
network: true
overview: 'wiastandards-com is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Domains API, Keys API, Standards API, and 2 more. Tagged areas include Standards, Certification, Interoperability, Digital-Twin, and Data-Exchange.


  The wiastandards-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Wiastandards Com Plans Pricing
  plan_count: 0
  slug: wiastandards-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Wiastandards Com Rate Limits
  slug: wiastandards-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: wiastandards-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: wiastandards-com-rules
scopes:
- name: Wiastandards Com Scopes
  scope_count: 0
  slug: wiastandards-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 0.0
    discoverability: 71.4
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Wiastandards Com Authentication
  slug: wiastandards-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Wiastandards Com Domain Security
  slug: wiastandards-com-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Wiastandards Com Trust Center
  slug: wiastandards-com-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: wiastandards-com
tags:
- Standards
- Certification
- Interoperability
- Digital-Twin
- Data-Exchange
website: https://wiastandards.com/
---
