---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Tradera Agentic Access
  operation_count: 72
  slug: tradera-agentic-access
  summary_line: 72 operations · 32 acting
api_count: 1
apis:
- baseURL: https://api.tradera.com
  baseurl_source: declared
  description: The Auth API from Tradera — 5 operation(s) for auth.
  name: Tradera Auth API
  slug: tradera-auth-api
- baseURL: https://api.tradera.com
  baseurl_source: declared
  description: The Buyer API from Tradera — 3 operation(s) for buyer.
  name: Tradera Buyer API
  slug: tradera-buyer-api
- baseURL: https://api.tradera.com
  baseurl_source: declared
  description: The Categories API from Tradera — 2 operation(s) for categories.
  name: Tradera Categories API
  slug: tradera-categories-api
- baseURL: https://api.tradera.com
  baseurl_source: declared
  description: The Items API from Tradera — 5 operation(s) for items.
  name: Tradera Items API
  slug: tradera-items-api
- baseURL: https://api.tradera.com
  baseurl_source: declared
  description: The Listings API from Tradera — 24 operation(s) for listings.
  name: Tradera Listings API
  slug: tradera-listings-api
- baseURL: https://api.tradera.com
  baseurl_source: declared
  description: The Orders API from Tradera — 5 operation(s) for orders.
  name: Tradera Orders API
  slug: tradera-orders-api
- baseURL: https://api.tradera.com
  baseurl_source: declared
  description: The Program API from Tradera — 2 operation(s) for program.
  name: Tradera Program API
  slug: tradera-program-api
- baseURL: https://api.tradera.com
  baseurl_source: declared
  description: The Reference Data API from Tradera — 7 operation(s) for reference data.
  name: Tradera Reference Data API
  slug: tradera-reference-data-api
- baseURL: https://api.tradera.com
  baseurl_source: declared
  description: The Search API from Tradera — 5 operation(s) for search.
  name: Tradera Search API
  slug: tradera-search-api
- baseURL: https://api.tradera.com
  baseurl_source: declared
  description: The Tradera.Api.Services.Core API from Tradera — 4 operation(s) for tradera.api.services.core.
  name: Tradera Tradera.Api.Services.Core API
  slug: tradera-tradera-api-services-core-api
- baseURL: https://api.tradera.com
  baseurl_source: declared
  description: The Users API from Tradera — 6 operation(s) for users.
  name: Tradera Users API
  slug: tradera-users-api
artifact_total: 22
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tradera/refs/heads/main/agentic-access/tradera-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tradera-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tradera/refs/heads/main/rules/tradera-rules.yml
  title: ''
  type: Spectral
  url: rules/tradera-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tradera/refs/heads/main/json-ld/tradera-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tradera-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tradera/refs/heads/main/vocabulary/tradera-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tradera-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tradera/refs/heads/main/data-model/tradera-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tradera-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/tradera/refs/heads/main/conformance/tradera-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tradera-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tradera/refs/heads/main/llms/tradera-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tradera-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/tradera/refs/heads/main/well-known/tradera-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tradera-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tradera/refs/heads/main/hosts/tradera-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tradera-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/tradera/refs/heads/main/vendors/tradera-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tradera-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tradera.com/support/se/terms/terms-and-conditions/
- group: operate
  title: ''
  type: Support
  url: https://www.tradera.com/support/se/
- group: start
  title: ''
  type: SignUp
  url: https://www.tradera.com/register
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tradera.com/support/se/terms/Privacy-Statement/
- group: docs
  title: ''
  type: APIReference
  url: https://api.tradera.com/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tradera
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tradera/refs/heads/main/authentication/tradera-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tradera-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/tradera/refs/heads/main/security/tradera-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tradera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tradera.com/
created: '2026-10-15'
description: Tradera is Sweden’s largest online marketplace for buying and selling second‑hand goods, ranging from collectibles and fashion to electronics and vehicles. The platform connects millions of users, offering a secure environment for auctions and direct sales, with features such as buyer protection, seller ratings, and integrated payment solutions. Tradera’s vibrant community fosters sustainable commerce by giving items a second life, supporting both hobbyists and everyday shoppers across a wide variety of categories.
image: http://static.tradera.net/nextweb/_next/static/media/open-graph-tradera-default.0fjg-i_g1_yum.png
json_schemas:
- name: ItemRequest
  property_count: 24
  slug: tradera-item-request
- name: Item
  property_count: 51
  slug: tradera-item
- name: SellerOrder
  property_count: 14
  slug: tradera-seller-order
- name: ShippingCode
  property_count: 6
  slug: tradera-shipping-code
- name: ShopItemData
  property_count: 20
  slug: tradera-shop-item-data
- name: ShopItemVariantData
  property_count: 22
  slug: tradera-shop-item-variant-data
jsonld:
- class_count: 104
  name: Tradera Context
  property_count: 288
  slug: tradera-context
layout: provider
modified: '2026-10-15'
name: Tradera
nav: Providers
network: true
overview: 'Tradera publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Buyer API, Categories API, and 8 more. Tagged areas include Marketplace, E-Commerce, Secondhand, Auctions, and Sweden.


  The Tradera catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Tradera''s developer surface includes support, signup flow, API reference, authentication, and 15 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Tradera API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 1
  slug: tradera-rules
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 51.7
    developer_ergonomics: 23.8
    discoverability: 73.2
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
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
    score: 27.8
security:
- kind: authentication
  name: Tradera Authentication
  slug: tradera-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Tradera Domain Security
  slug: tradera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tradera
tags:
- Marketplace
- E-Commerce
- Secondhand
- Auctions
- Sweden
website: https://tradera.com/
---
