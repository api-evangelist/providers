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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.5
  scored_at: '2026-10-17'
api_count: 4
apis:
- baseURL: https://api-leoeu.gep.com
  baseurl_source: declared
  description: The Leo Gr Domaingateway Api API from GEP — 1 operation(s) for leo gr domaingateway api.
  name: GEP Leo Gr Domaingateway API
  slug: gep-leo-gr-domaingateway-api-api
- baseURL: https://api-leoeu.gep.com
  baseurl_source: declared
  description: The Leo Order Aggregator Api API from GEP — 2 operation(s) for leo order aggregator api.
  name: GEP Leo Order Aggregator API
  slug: gep-leo-order-aggregator-api-api
- baseURL: https://api-leoeu.gep.com
  baseurl_source: declared
  description: The Leo Sc Aggregator Api API from GEP — 1 operation(s) for leo sc aggregator api.
  name: GEP Leo Sc Aggregator API
  slug: gep-leo-sc-aggregator-api-api
- baseURL: https://api-leoeu.gep.com
  baseurl_source: declared
  description: The Token API from GEP — 1 operation(s) for token.
  name: GEP Token API
  slug: gep-token-api
artifact_total: 12
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gep/refs/heads/main/rules/gep-rules.yml
  title: ''
  type: Spectral
  url: rules/gep-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gep/refs/heads/main/json-ld/gep-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gep-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gep/refs/heads/main/vocabulary/gep-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gep-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gep/refs/heads/main/data-model/gep-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gep-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gep/refs/heads/main/conformance/gep-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gep-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gep/refs/heads/main/llms/gep-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gep-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gep/refs/heads/main/hosts/gep-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gep-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gep/refs/heads/main/vendors/gep-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gep-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gep.com/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gep.com/privacy-statement
- group: company
  title: ''
  type: Newsroom
  url: https://www.gep.com/company/news
- group: start
  title: ''
  type: Login
  url: https://www.gep.com/login
- group: other
  title: ''
  type: Leadership
  url: https://www.gep.com/company/leadership
- group: company
  title: ''
  type: Blog
  url: https://www.gep.com/blog/mind/nft-basics
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gep/refs/heads/main/security/gep-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gep-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gep.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://partner.gep.com/mcp
  - status: 200
    url: https://www.gep.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: GEP provides AI‑powered procurement and supply chain software, offering solutions such as quantum intelligence, e‑invoicing, strategic consulting, and managed services. The company emphasizes sustainability, diversity, and innovation across global markets, serving clients with end‑to‑end source‑to‑pay suites and advanced analytics. GEP’s platform integrates AI to optimize spend, risk, and supplier management, supporting enterprises worldwide.
json_schemas:
- name: GetLeoGrDomaingatewayApiApiV1V1IdResponse
  property_count: 7
  slug: gep-get-leo-gr-domaingateway-api-api-v1-v1-id-response
- name: GetLeoOrderAggregatorApiApiV1OrderaggregationV1Getorderbydoc
  property_count: 4
  slug: gep-get-leo-order-aggregator-api-api-v1-orderaggregation-v1-getorderbydoc
- name: GetLeoOrderAggregatorApiApiV1OrderaggregationV1Response
  property_count: 4
  slug: gep-get-leo-order-aggregator-api-api-v1-orderaggregation-v1-response
- name: PostLeoGrDomaingatewayApiApiV1V1IdRequest
  property_count: 7
  slug: gep-post-leo-gr-domaingateway-api-api-v1-v1-id-request
- name: PostLeoGrDomaingatewayApiApiV1V1IdResponse
  property_count: 4
  slug: gep-post-leo-gr-domaingateway-api-api-v1-v1-id-response
jsonld:
- class_count: 5
  name: Gep Context
  property_count: 18
  slug: gep-context
layout: provider
modified: '2026-10-13'
name: GEP
nav: Providers
network: true
overview: 'GEP is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Leo Gr Domaingateway API, Leo Order Aggregator API, Leo Sc Aggregator API, and 1 more. Tagged areas include Company, Procurement, Supply Chain, Artificial Intelligence, and Software-as-a-Service.


  The GEP catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GEP''s developer surface includes engineering blog and 15 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: GEP API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: gep-rules
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 14
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 2.4
    discoverability: 78.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Gep Domain Security
  slug: gep-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: gep
tags:
- Company
- Procurement
- Supply Chain
- Artificial Intelligence
- Software-as-a-Service
website: https://www.gep.com
---
