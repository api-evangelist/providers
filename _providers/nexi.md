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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.2
  scored_at: '2026-11-06'
api_count: 9
apis:
- baseURL: https://xpaysandbox.nexigroup.com/api/phoenix-0.0/psp
  baseurl_source: spec
  description: API reference for Nexi's payment services
  name: Nexi API
  slug: nexi-api
- baseURL: https://xpaysandbox.nexigroup.com/api/phoenix-0.0/psp
  baseurl_source: declared
  description: The Build API from Nexi — 1 operation(s) for build.
  name: Nexi Build API
  slug: nexi-build-api
- baseURL: https://xpaysandbox.nexigroup.com/api/phoenix-0.0/psp
  baseurl_source: declared
  description: The Contract API from Nexi — 1 operation(s) for contract.
  name: Nexi Contract API
  slug: nexi-contract-api
- baseURL: https://xpaysandbox.nexigroup.com/api/phoenix-0.0/psp
  baseurl_source: declared
  description: The Contracts API from Nexi — 2 operation(s) for contracts.
  name: Nexi Contracts API
  slug: nexi-contracts-api
- baseURL: https://xpaysandbox.nexigroup.com/api/phoenix-0.0/psp
  baseurl_source: declared
  description: The Nexi API API from Nexi — 1 operation(s) for nexi api.
  name: Nexi Nexi API
  slug: nexi-nexi-api-api
- baseURL: https://xpaysandbox.nexigroup.com/api/phoenix-0.0/psp
  baseurl_source: declared
  description: The Operations API from Nexi — 4 operation(s) for operations.
  name: Nexi Operations API
  slug: nexi-operations-api
- baseURL: https://xpaysandbox.nexigroup.com/api/phoenix-0.0/psp
  baseurl_source: declared
  description: The Orders API from Nexi — 8 operation(s) for orders.
  name: Nexi Orders API
  slug: nexi-orders-api
- baseURL: https://xpaysandbox.nexigroup.com/api/phoenix-0.0/psp
  baseurl_source: declared
  description: The Paybylink API from Nexi — 1 operation(s) for paybylink.
  name: Nexi Paybylink API
  slug: nexi-paybylink-api
- baseURL: https://xpaysandbox.nexigroup.com/api/phoenix-0.0/psp
  baseurl_source: declared
  description: The Payment Methods API from Nexi — 1 operation(s) for payment methods.
  name: Nexi Payment Methods API
  slug: nexi-payment-methods-api
artifact_total: 14
common:
- group: other
  href: https://artifacts.apis.io/nexi/vendors/nexi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nexi-vendors.yml
- group: design
  href: https://artifacts.apis.io/nexi/rules/nexi-rules.yml
  title: ''
  type: Spectral
  url: rules/nexi-rules.yml
- group: design
  href: https://artifacts.apis.io/nexi/json-ld/nexi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nexi-context.jsonld
- group: design
  href: https://artifacts.apis.io/nexi/vocabulary/nexi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nexi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/nexi/data-model/nexi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nexi-data-model.yml
- group: build
  href: https://artifacts.apis.io/nexi/errors/nexi-decline-codes.yml
  title: ''
  type: DeclineCodes
  url: errors/nexi-decline-codes.yml
- group: design
  href: https://artifacts.apis.io/nexi/conformance/nexi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nexi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nexi/llms/nexi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nexi-llms.txt
- group: other
  href: https://artifacts.apis.io/nexi/hosts/nexi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nexi-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nexigroup.com/en/legal-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.nexigroup.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nexigroup.com/en/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.nexigroup.com/en/media-relations/news/
- group: other
  title: ''
  type: Leadership
  url: https://www.nexigroup.com/en/group/governance/management/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.paygate.nexigroup.com/nexi-developer/setup-fraud-prevention-optional
- group: docs
  title: ''
  type: Documentation
  url: https://developer.nexigroup.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.npay.eu/nexi-pos-api/docs/
- group: auth
  href: https://artifacts.apis.io/nexi/security/nexi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nexi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nexigroup.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://docs.paygate.nexigroup.com/mcp
  - status: 200
    url: https://www.nexigroup.com
  reason: no-developer-program
  state: none
created: '2026-10-14'
description: Nexi is a European payment technology company offering a wide range of digital payment solutions for merchants, banks, and consumers. It provides services such as card issuing, open banking, e‑commerce payments, and blockchain‑based solutions, operating across multiple countries in Europe. Nexi focuses on innovation in the PayTech sector, delivering secure, scalable, and compliant payment infrastructures for businesses of all sizes.
json_schemas:
- name: GetApiV1OrdersOrderidResponse
  property_count: 1
  slug: nexi-get-api-v1-orders-orderid-response
- name: GetApiV1OrdersResponse
  property_count: 1
  slug: nexi-get-api-v1-orders-response
jsonld:
- class_count: 2
  name: Nexi Context
  property_count: 2
  slug: nexi-context
layout: provider
modified: '2026-10-14'
name: Nexi
nav: Providers
network: true
overview: 'Nexi is listed with 9 APIs on the [APIs.io](https://apis.io/) network, including Build API, Contract API, and 7 more. Tagged areas include Company, Payments, Fintech, and Europe.


  The Nexi catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Nexi''s developer surface includes getting-started guide, documentation, and 17 more developer resources.'
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Nexi API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: nexi-rules
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 20.2
    developer_ergonomics: 15.5
    discoverability: 58.9
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  previous_composite: 27.9
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 20.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/nexi/nexi-2026-11-03T140154.png
security:
- kind: domain-security
  name: Nexi Domain Security
  slug: nexi-domain-security
  summary_line: TLSv1.2 · DMARC
slug: nexi
tags:
- Company
- Payments
- Fintech
- Europe
website: https://www.nexigroup.com
---
