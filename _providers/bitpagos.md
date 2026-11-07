---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 28.5
  scored_at: '2026-11-06'
api_count: 8
apis:
- description: Payment processing API for merchants, supporting credit cards and Bitcoin.
  name: Bitpagos API
  slug: bitpagos-api-2
- baseURL: https://b2b-api.ripio.com/
  baseurl_source: declared
  description: The Bitpagos API API from Bitpagos — 1 operation(s) for bitpagos api.
  name: Bitpagos Bitpagos API
  slug: bitpagos-bitpagos-api-api
- baseURL: https://b2b-api.ripio.com/
  baseurl_source: declared
  description: The Customers API from Bitpagos — 10 operation(s) for customers.
  name: Bitpagos Customers API
  slug: bitpagos-customers-api
- baseURL: https://b2b-api.ripio.com/
  baseurl_source: declared
  description: The Offramp API from Bitpagos — 1 operation(s) for offramp.
  name: Bitpagos Offramp API
  slug: bitpagos-offramp-api
- baseURL: https://b2b-api.ripio.com/
  baseurl_source: declared
  description: The Quotes API from Bitpagos — 1 operation(s) for quotes.
  name: Bitpagos Quotes API
  slug: bitpagos-quotes-api
- baseURL: https://b2b-api.ripio.com/
  baseurl_source: declared
  description: The Rates API from Bitpagos — 1 operation(s) for rates.
  name: Bitpagos Rates API
  slug: bitpagos-rates-api
- baseURL: https://b2b-api.ripio.com/
  baseurl_source: declared
  description: The Resources API from Bitpagos — 1 operation(s) for resources.
  name: Bitpagos Resources API
  slug: bitpagos-resources-api
- baseURL: https://b2b-api.ripio.com/
  baseurl_source: declared
  description: The Trade API from Bitpagos — 1 operation(s) for trade.
  name: Bitpagos Trade API
  slug: bitpagos-trade-api
artifact_total: 19
asyncapis:
- description: ''
  name: Bitpagos Webhooks
  slug: bitpagos-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/bitpagos/well-known/bitpagos-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bitpagos-status-security.txt
- group: design
  href: https://artifacts.apis.io/bitpagos/rules/bitpagos-rules.yml
  title: ''
  type: Spectral
  url: rules/bitpagos-rules.yml
- group: design
  href: https://artifacts.apis.io/bitpagos/json-ld/bitpagos-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bitpagos-context.jsonld
- group: design
  href: https://artifacts.apis.io/bitpagos/vocabulary/bitpagos-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bitpagos-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bitpagos/asyncapi/bitpagos-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bitpagos-webhooks.yml
- group: design
  href: https://artifacts.apis.io/bitpagos/data-model/bitpagos-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bitpagos-data-model.yml
- group: start
  href: https://artifacts.apis.io/bitpagos/sandbox/bitpagos-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bitpagos-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/bitpagos/authentication/bitpagos-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bitpagos-authentication.yml
- group: design
  href: https://artifacts.apis.io/bitpagos/conformance/bitpagos-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitpagos-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bitpagos/llms/bitpagos-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitpagos-llms.txt
- group: agent
  href: https://artifacts.apis.io/bitpagos/well-known/bitpagos-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitpagos-well-known.yml
- group: other
  href: https://artifacts.apis.io/bitpagos/hosts/bitpagos-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitpagos-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitpagos/vendors/bitpagos-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitpagos-vendors.yml
- group: build
  href: https://artifacts.apis.io/bitpagos/packages/bitpagos-packages.yml
  title: ''
  type: SDKs
  url: packages/bitpagos-packages.yml
- group: build
  href: https://artifacts.apis.io/bitpagos/packages/bitpagos-packages.yml
  title: ''
  type: Packages
  url: packages/bitpagos-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: http://terms.ripio.com/
- group: operate
  title: ''
  type: Support
  url: https://help.ripio.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ripio.com/
- group: company
  title: ''
  type: Blog
  url: https://launchpad.ripio.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.ripio.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ripio.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ripio
- group: auth
  href: https://artifacts.apis.io/bitpagos/security/bitpagos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitpagos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ripio.com
coverage:
  checked: '2026-09-28'
  detail: The provider's documentation links to OpenAPI specs hosted on docs.ripio.com, which belong to Ripio, not Bitpagos.
  evidence:
  - status: 200
    url: https://docs.ripio.com/crypto-as-a-service/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Bitpagos is a payment gateway based in Buenos Aires, Argentina, focused on merchants in Latin America. It processes credit cards and Bitcoin, aiming to reduce international transaction fees for small and medium businesses. Founded as Ripio, the company rebranded to Bitpagos and offers APIs for payment processing, refunds, and transaction reporting, targeting fintech integrations across the region.
image: https://cdn.prod.website-files.com/5f17344acf2c6d3c3a1d6238/680a5d403b378088d8ccb8a3_Contenido_banner-marca_fb_1200x628_0525.png
json_schemas:
- name: PostApiV1CustomersCustomeridKycOtpValidateResponse
  property_count: 4
  slug: bitpagos-post-api-v1-customers-customerid-kyc-otp-validate-response
- name: PostApiV1CustomersCustomeridKycStartResponse
  property_count: 4
  slug: bitpagos-post-api-v1-customers-customerid-kyc-start-response
- name: PostApiV1CustomersRequest
  property_count: 4
  slug: bitpagos-post-api-v1-customers-request
- name: PostApiV1CustomersResponse
  property_count: 5
  slug: bitpagos-post-api-v1-customers-response
- name: PostApiV1QuotesRequest
  property_count: 6
  slug: bitpagos-post-api-v1-quotes-request
- name: PostApiV1QuotesResponse
  property_count: 10
  slug: bitpagos-post-api-v1-quotes-response
jsonld:
- class_count: 19
  name: Bitpagos Context
  property_count: 36
  slug: bitpagos-context
layout: provider
modified: '2026-09-28'
name: Bitpagos
nav: Providers
network: true
overview: 'Bitpagos is listed with 8 APIs on the [APIs.io](https://apis.io/) network, including Bitpagos API, Customers API, Offramp API, and 5 more. Tagged areas include Payments, Fintech, Latin America, Bitcoin, and Credit Cards.


  The Bitpagos catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bitpagos'' developer surface includes sandbox, authentication, support, engineering blog, documentation, API reference, and 18 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Bitpagos API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: bitpagos-rules
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 65.8
    catalog_earned_first_party: 0.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.0
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 33.7
    developer_ergonomics: 38.1
    discoverability: 78.6
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - argentina
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  previous_composite: 35.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Bitpagos Authentication
  slug: bitpagos-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Bitpagos Domain Security
  slug: bitpagos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitpagos
tags:
- Payments
- Fintech
- Latin America
- Bitcoin
- Credit Cards
website: https://www.ripio.com
---
