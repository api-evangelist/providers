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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-10-17'
api_count: 7
apis:
- baseURL: https://marketplace-api.curios.com
  baseurl_source: declared
  description: The Collections API from Curios — 2 operation(s) for collections.
  name: Curios Collections API
  slug: curios-collections-api
- baseURL: https://marketplace-api.curios.com
  baseurl_source: declared
  description: The Contracts API from Curios — 3 operation(s) for contracts.
  name: Curios Contracts API
  slug: curios-contracts-api
- baseURL: https://marketplace-api.curios.com
  baseurl_source: declared
  description: The Customers API from Curios — 3 operation(s) for customers.
  name: Curios Customers API
  slug: curios-customers-api
- baseURL: https://marketplace-api.curios.com
  baseurl_source: declared
  description: The Listings API from Curios — 2 operation(s) for listings.
  name: Curios Listings API
  slug: curios-listings-api
- baseURL: https://marketplace-api.curios.com
  baseurl_source: declared
  description: The Orders API from Curios — 3 operation(s) for orders.
  name: Curios Orders API
  slug: curios-orders-api
- baseURL: https://marketplace-api.curios.com
  baseurl_source: declared
  description: The Projects API from Curios — 2 operation(s) for projects.
  name: Curios Projects API
  slug: curios-projects-api
- baseURL: https://marketplace-api.curios.com
  baseurl_source: declared
  description: The Tokens API from Curios — 2 operation(s) for tokens.
  name: Curios Tokens API
  slug: curios-tokens-api
artifact_total: 15
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/curios/refs/heads/main/plans/curios-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/curios-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curios/refs/heads/main/rules/curios-rules.yml
  title: ''
  type: Spectral
  url: rules/curios-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curios/refs/heads/main/json-ld/curios-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/curios-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curios/refs/heads/main/vocabulary/curios-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/curios-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curios/refs/heads/main/data-model/curios-data-model.yml
  title: ''
  type: DataModel
  url: data-model/curios-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curios/refs/heads/main/conventions/curios-conventions.yml
  title: ''
  type: Conventions
  url: conventions/curios-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curios/refs/heads/main/authentication/curios-authentication.yml
  title: ''
  type: Authentication
  url: authentication/curios-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/curios/refs/heads/main/conformance/curios-conformance.yml
  title: ''
  type: Conformance
  url: conformance/curios-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curios/refs/heads/main/hosts/curios-hosts.yml
  title: ''
  type: Hosts
  url: hosts/curios-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/curios/refs/heads/main/vendors/curios-vendors.yml
  title: ''
  type: Vendors
  url: vendors/curios-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.curios.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://www.curios.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.curios.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://studio.curios.com/kb/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://content.curios.com/docs/casper
- group: docs
  title: ''
  type: Documentation
  url: https://docs.curios.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/curios/refs/heads/main/security/curios-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/curios-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.curios.com/
coverage:
  checked: '2026-10-12'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found on the API host.
  evidence:
  - status: 404
    url: https://api.curios.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Curios builds Web3, blockchain and AI technologies, offering a digital content marketplace for creators such as musicians, authors, comedians, and developers. The platform enables creators to sell directly to fans, retain 100% of revenue, and access audience data, while providing APIs for commerce, analytics, and integration. Curios also offers a mobile app and supports NFT and tokenized content, positioning itself as a creator‑first commerce solution.
json_schemas:
- name: PostCustomersCustomeridRequest
  property_count: 2
  slug: curios-post-customers-customerid-request
- name: PostCustomersRequest
  property_count: 8
  slug: curios-post-customers-request
- name: PostOrdersOrderidRequest
  property_count: 1
  slug: curios-post-orders-orderid-request
jsonld:
- class_count: 3
  name: Curios Context
  property_count: 8
  slug: curios-context
layout: provider
modified: '2026-10-12'
name: Curios
nav: Providers
network: true
overview: 'Curios is listed with 7 APIs on the [APIs.io](https://apis.io/) network, including Collections API, Contracts API, Customers API, and 4 more. Tagged areas include Company, Marketplace, Web3, and Creators.


  The Curios catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Curios'' developer surface includes authentication, support, pricing, getting-started guide, documentation, and 13 more developer resources.'
plans:
- name: Curios Plans Pricing
  plan_count: 4
  slug: curios-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Curios API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: curios-rules
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 38.1
    discoverability: 58.9
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Curios Authentication
  slug: curios-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Curios Domain Security
  slug: curios-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: curios
tags:
- Company
- Marketplace
- Web3
- Creators
website: https://www.curios.com/
---
