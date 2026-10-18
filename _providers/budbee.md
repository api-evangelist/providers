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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.2
  scored_at: '2026-10-17'
api_count: 9
apis:
- baseURL: https://api.budbee.com
  baseurl_source: declared
  description: The Box API from Budbee — 1 operation(s) for box.
  name: Budbee Box API
  slug: budbee-box-api
- baseURL: https://api.budbee.com
  baseurl_source: declared
  description: The Boxes API from Budbee — 3 operation(s) for boxes.
  name: Budbee Boxes API
  slug: budbee-boxes-api
- baseURL: https://api.budbee.com
  baseurl_source: declared
  description: The Budbee API API from Budbee — 1 operation(s) for budbee api.
  name: Budbee Budbee API
  slug: budbee-budbee-api-api
- baseURL: https://api.budbee.com
  baseurl_source: declared
  description: The Intervals API from Budbee — 1 operation(s) for intervals.
  name: Budbee Intervals API
  slug: budbee-intervals-api
- baseURL: https://api.budbee.com
  baseurl_source: declared
  description: The Multiple API from Budbee — 7 operation(s) for multiple.
  name: Budbee Multiple API
  slug: budbee-multiple-api
- baseURL: https://api.budbee.com
  baseurl_source: declared
  description: The Postalcodes API from Budbee — 2 operation(s) for postalcodes.
  name: Budbee Postalcodes API
  slug: budbee-postalcodes-api
- baseURL: https://api.budbee.com
  baseurl_source: declared
  description: The Returns API from Budbee — 1 operation(s) for returns.
  name: Budbee Returns API
  slug: budbee-returns-api
- baseURL: https://api.budbee.com
  baseurl_source: declared
  description: The Users API from Budbee — 1 operation(s) for users.
  name: Budbee Users API
  slug: budbee-users-api
- baseURL: https://api.budbee.com
  baseurl_source: declared
  description: The Webhooks API from Budbee — 1 operation(s) for webhooks.
  name: Budbee Webhooks API
  slug: budbee-webhooks-api
artifact_total: 19
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/budbee/refs/heads/main/well-known/budbee-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/budbee-clarity-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/budbee/refs/heads/main/well-known/budbee-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/budbee-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/budbee/refs/heads/main/rules/budbee-rules.yml
  title: ''
  type: Spectral
  url: rules/budbee-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/budbee/refs/heads/main/json-ld/budbee-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/budbee-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/budbee/refs/heads/main/vocabulary/budbee-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/budbee-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/budbee/refs/heads/main/data-model/budbee-data-model.yml
  title: ''
  type: DataModel
  url: data-model/budbee-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/budbee/refs/heads/main/conformance/budbee-conformance.yml
  title: ''
  type: Conformance
  url: conformance/budbee-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/budbee/refs/heads/main/hosts/budbee-hosts.yml
  title: ''
  type: Hosts
  url: hosts/budbee-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/budbee/refs/heads/main/vendors/budbee-vendors.yml
  title: ''
  type: Vendors
  url: vendors/budbee-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://budbee.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://budbee.com/se/press/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.budbee.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.staging.budbee.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/budbee/refs/heads/main/security/budbee-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/budbee-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/budbee/refs/heads/main/security/budbee-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/budbee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://budbee.com
coverage:
  checked: '2026-10-06'
  detail: Developer portal pages render via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://developer.budbee.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-06'
description: Budbee provides a flexible, last‑mile delivery service across Europe, offering home delivery and returns with convenient time‑slot booking via its app or website. Founded in Sweden, Budbee focuses on sustainable logistics, using renewable diesel and optimizing routes to reduce emissions. It serves merchants and consumers, enabling easy parcel tracking, flexible Box locations for pick‑up and drop‑off, and integrates with e‑commerce platforms. Budbee aims to enhance the online shopping experience by ensuring reliable, environmentally‑friendly deliveries and returns.
image: https://budbee.com/wp-content/uploads/2022/06/adobestock452382338-min.jpeg
json_schemas:
- name: GetResponse
  property_count: 8
  slug: budbee-get-response
- name: PostBoxReturnRequest
  property_count: 5
  slug: budbee-post-box-return-request
- name: PostBoxReturnResponse
  property_count: 5
  slug: budbee-post-box-return-response
- name: PostMultipleOrdersRequest
  property_count: 5
  slug: budbee-post-multiple-orders-request
- name: PostReturnsRequest
  property_count: 4
  slug: budbee-post-returns-request
- name: PostReturnsResponse
  property_count: 4
  slug: budbee-post-returns-response
jsonld:
- class_count: 21
  name: Budbee Context
  property_count: 42
  slug: budbee-context
layout: provider
modified: '2026-10-06'
name: Budbee
nav: Providers
network: true
overview: 'Budbee is listed with 9 APIs on the [APIs.io](https://apis.io/) network, including Box API, Boxes API, Budbee API, and 6 more. Tagged areas include Company, Delivery, Logistics, E-Commerce, and Sustainability.


  The Budbee catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Budbee''s developer surface includes documentation and 16 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Budbee API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: budbee-rules
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 28.1
    developer_ergonomics: 19.0
    discoverability: 73.2
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Budbee Domain Security
  slug: budbee-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Budbee Vulnerability Disclosure
  slug: budbee-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: budbee
tags:
- Company
- Delivery
- Logistics
- E-Commerce
- Sustainability
website: https://budbee.com
---
