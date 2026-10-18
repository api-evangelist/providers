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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-10-17'
api_count: 6
apis:
- description: Clyde's API provides endpoints for warranty registration, issue resolution, and partnership tools.
  name: Clyde API
  slug: clyde-api-2
- baseURL: https://api.joinclyde.com
  baseurl_source: declared
  description: The Contract Sales API from Clyde — 1 operation(s) for contract sales.
  name: Clyde Contract Sales API
  slug: clyde-contract-sales-api
- baseURL: https://api.joinclyde.com
  baseurl_source: declared
  description: The Orders API from Clyde — 2 operation(s) for orders.
  name: Clyde Orders API
  slug: clyde-orders-api
- baseURL: https://api.joinclyde.com
  baseurl_source: declared
  description: The Products API from Clyde — 3 operation(s) for products.
  name: Clyde Products API
  slug: clyde-products-api
- baseURL: https://api.joinclyde.com
  baseurl_source: declared
  description: The Taxonomies API from Clyde — 1 operation(s) for taxonomies.
  name: Clyde Taxonomies API
  slug: clyde-taxonomies-api
- baseURL: https://api.joinclyde.com
  baseurl_source: declared
  description: The Vouchers API from Clyde — 2 operation(s) for vouchers.
  name: Clyde Vouchers API
  slug: clyde-vouchers-api
artifact_total: 15
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clyde/refs/heads/main/rules/clyde-rules.yml
  title: ''
  type: Spectral
  url: rules/clyde-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clyde/refs/heads/main/json-ld/clyde-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clyde-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clyde/refs/heads/main/vocabulary/clyde-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clyde-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clyde/refs/heads/main/data-model/clyde-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clyde-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/clyde/refs/heads/main/conformance/clyde-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clyde-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/clyde/refs/heads/main/llms/clyde-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clyde-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clyde/refs/heads/main/hosts/clyde-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clyde-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/clyde/refs/heads/main/vendors/clyde-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clyde-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://joinclyde.com/legal/terms-of-use
- group: operate
  title: ''
  type: StatusPage
  url: https://status.joinclyde.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://joinclyde.com/legal/privacy-policy
- group: docs
  title: ''
  type: APIReference
  url: https://docs.joinclyde.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.joinclyde.com/docs/sfcc-quickstart
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/clyde/refs/heads/main/security/clyde-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clyde-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joinclyde.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.joinclyde.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.joinclyde.com/docs
- group: company
  title: ''
  type: Blog
  url: https://joinclyde.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.joinclyde.com/hc/en-us
- group: commercial
  title: ''
  type: Pricing
  url: https://joinclyde.com/extended-warranty
coverage:
  checked: '2026-10-12'
  detail: OpenAPI spec endpoints returned 401 unauthorized and no machine-readable contract was found.
  evidence:
  - status: 401
    url: https://api.joinclyde.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Clyde provides ownership enrichment solutions that help businesses drive lifetime value and revenue through extended warranty and product protection plans. Now part of Cover Genius, Clyde offers registration, resolution, and partnership tools for merchants to engage customers, automate issue resolution, and unlock cost savings. The platform includes documentation, a developer portal, and various integration points for insurance and warranty services.
image: https://joinclyde.com/og-image.jpg
json_schemas:
- name: PostContractSalesFbd13A8FB74649888925456843Ddc533ClaimsReque
  property_count: 13
  slug: clyde-post-contract-sales-fbd13-a8-fb74649888925456843-ddc533-claims-reque
- name: PostOrdersRequest
  property_count: 32
  slug: clyde-post-orders-request
- name: PostProductsBulkRequest
  property_count: 15
  slug: clyde-post-products-bulk-request
- name: PostProductsRequest
  property_count: 13
  slug: clyde-post-products-request
- name: PostTaxonomiesRequest
  property_count: 8
  slug: clyde-post-taxonomies-request
- name: PostVouchersBulkRequest
  property_count: 10
  slug: clyde-post-vouchers-bulk-request
jsonld:
- class_count: 16
  name: Clyde Context
  property_count: 53
  slug: clyde-context
layout: provider
modified: '2026-10-12'
name: Clyde
nav: Providers
network: true
overview: 'Clyde is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Contract Sales API, Orders API, Products API, and 3 more. Tagged areas include Extended Warranty, Product Registration, Shipping Protection, E‑commerce Integration, and Claims Processing.


  The Clyde catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clyde''s developer surface includes API reference, getting-started guide, documentation, engineering blog, support, pricing, and 14 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Clyde API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: clyde-rules
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 25.1
    developer_ergonomics: 45.2
    discoverability: 69.6
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Clyde Domain Security
  slug: clyde-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clyde
tags:
- Extended Warranty
- Product Registration
- Shipping Protection
- E‑commerce Integration
- Claims Processing
website: https://joinclyde.com
---
