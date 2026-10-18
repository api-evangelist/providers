---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: REST API for Broker Genius providing customs brokerage automation
  name: Broker Genius API
  slug: broker-genius-api
- baseURL: https://api.brokergenius.ai
  baseurl_source: declared
  description: The Brokergenius API API from Brokergenius — 1 operation(s) for brokergenius api.
  name: Brokergenius Brokergenius API
  slug: brokergenius-brokergenius-api-api
- baseURL: https://api.brokergenius.ai
  baseurl_source: declared
  description: The Classify API from Brokergenius — 1 operation(s) for classify.
  name: Brokergenius Classify API
  slug: brokergenius-classify-api
artifact_total: 9
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/brokergenius/refs/heads/main/plans/brokergenius-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/brokergenius-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brokergenius/refs/heads/main/rules/brokergenius-rules.yml
  title: ''
  type: Spectral
  url: rules/brokergenius-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brokergenius/refs/heads/main/json-ld/brokergenius-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/brokergenius-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brokergenius/refs/heads/main/vocabulary/brokergenius-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/brokergenius-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brokergenius/refs/heads/main/data-model/brokergenius-data-model.yml
  title: ''
  type: DataModel
  url: data-model/brokergenius-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/brokergenius/refs/heads/main/conformance/brokergenius-conformance.yml
  title: ''
  type: Conformance
  url: conformance/brokergenius-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/brokergenius/refs/heads/main/well-known/brokergenius-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/brokergenius-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/brokergenius/refs/heads/main/hosts/brokergenius-hosts.yml
  title: ''
  type: Hosts
  url: hosts/brokergenius-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://brokergenius.ai/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/brokergenius/refs/heads/main/security/brokergenius-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/brokergenius-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://brokergenius.ai
- group: docs
  title: ''
  type: Documentation
  url: https://brokergenius.ai/developer
- group: docs
  title: ''
  type: APIReference
  url: https://brokergenius.ai/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://brokergenius.ai/join
- group: operate
  title: ''
  type: Support
  url: https://brokergenius.ai/support
- group: company
  title: ''
  type: Blog
  url: https://brokergenius.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://brokergenius.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brokergenius.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brokergenius.ai/privacy-policy
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://brokergenius.ai
  - status: 403
    url: https://equityzen.com/company/brokergenius
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-06'
description: Broker Genius provides AI‑powered customs brokerage automation for brokers, freight forwarders, and trade teams. The platform reads invoices, classifies line items, assigns HS codes, and generates ASYCUDA‑compatible declarations, reducing manual entry time by up to 80%. Built in Anguilla, it offers a web portal, REST API, and webhooks to integrate with existing TMS and ERP systems, with a free trial and no credit‑card required.
image: https://brokergenius.ai/wp-content/uploads/2025/07/Blue-Orange-Green-Lined-Illustration-Social-Media-Policy-Presentation-2.jpg
json_schemas:
- name: PostApiApiidRequest
  property_count: 1
  slug: brokergenius-post-api-apiid-request
- name: PostApiApiidResponse
  property_count: 4
  slug: brokergenius-post-api-apiid-response
jsonld:
- class_count: 2
  name: Brokergenius Context
  property_count: 4
  slug: brokergenius-context
layout: provider
modified: '2026-10-06'
name: Brokergenius
nav: Providers
network: true
overview: 'Brokergenius is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Brokergenius API, Classify API, and 1 more. Tagged areas include Customs, Artificial Intelligence, Automation, Brokerage, and Logistics.


  The Brokergenius catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Brokergenius'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Brokergenius Plans Pricing
  plan_count: 5
  slug: brokergenius-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Brokergenius API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: brokergenius-rules
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 21.8
    developer_ergonomics: 35.7
    discoverability: 62.5
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 26.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Brokergenius Domain Security
  slug: brokergenius-domain-security
  summary_line: TLSv1.3 · DMARC
slug: brokergenius
tags:
- Customs
- Artificial Intelligence
- Automation
- Brokerage
- Logistics
website: https://brokergenius.ai
---
