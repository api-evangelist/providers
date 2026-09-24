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
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://api.accor.com
  baseurl_source: declared
  description: 'Accor API as documented publicly: 79 operations. Contract generated from the documentation by API Evangelist (2026-09-22); not the provider''s own document.'
  name: Accor API
  slug: accor-api
artifact_total: 10
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accor/refs/heads/main/rules/accor-rules.yml
  title: ''
  type: Spectral
  url: rules/accor-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accor/refs/heads/main/json-ld/accor-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/accor-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accor/refs/heads/main/vocabulary/accor-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/accor-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accor/refs/heads/main/data-model/accor-data-model.yml
  title: ''
  type: DataModel
  url: data-model/accor-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/accor/refs/heads/main/conformance/accor-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accor-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accor/refs/heads/main/llms/accor-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accor-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accor/refs/heads/main/well-known/accor-all-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/accor-all-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/accor/refs/heads/main/well-known/accor-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/accor-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/accor/refs/heads/main/hosts/accor-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accor-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/accor/refs/heads/main/vendors/accor-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accor-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/accor/refs/heads/main/security/accor-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accor-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accor.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.accor.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.accor.com/api-portfolio
- group: docs
  title: ''
  type: APIReference
  url: https://developer.accor.com/api-portfolio
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.accor.com/user/register
- group: operate
  title: ''
  type: Support
  url: https://developer.accor.com/contact
- group: company
  title: ''
  type: Blog
  url: https://developer.accor.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.accor.com/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://developer.accor.com/legal_notice
coverage:
  checked: 2026-09-22
  detail: Developer portal returns HTML shells with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://developer.accor.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-22'
description: Accor is a global hospitality group operating a portfolio of hotels, resorts, and residences across more than 110 countries. The company focuses on delivering innovative travel experiences, sustainability initiatives, and digital services for guests and partners. While its consumer-facing sites provide booking and loyalty programs, Accor also offers partner solutions and data services, reflecting its commitment to technology-driven hospitality.
image: https://images.group.accor.com/yrj0orc8tx24/7LDit16MyBanbXwhACNaGu/bb10a516761ba172d743f8b6feb3b319/ACCOR.COM_Hero-Homepage_LeireLeoz2.jpg?w=3840&q=100&fm=avif
json_schemas:
- name: GetCatalogV1HotelsHotelidTaxesResponse
  property_count: 5
  slug: accor-get-catalog-v1-hotels-hotelid-taxes-response
- name: GetCatalogV1InventoryHotelsResponse
  property_count: 2
  slug: accor-get-catalog-v1-inventory-hotels-response
- name: GetLoyaltyV1ReferentialsLoyaltyCardsThresholdsPromotionalOff
  property_count: 3
  slug: accor-get-loyalty-v1-referentials-loyalty-cards-thresholds-promotional-off
- name: GetLoyaltyV1ReferentialsLoyaltyCardsThresholdsResponse
  property_count: 3
  slug: accor-get-loyalty-v1-referentials-loyalty-cards-thresholds-response
- name: PostCatalogV1HotelsIdRatesResponse
  property_count: 2
  slug: accor-post-catalog-v1-hotels-id-rates-response
- name: PostLoyaltyV1BurnPartnerxpPartnerxpidRequest
  property_count: 1
  slug: accor-post-loyalty-v1-burn-partnerxp-partnerxpid-request
jsonld:
- class_count: 57
  name: Accor Context
  property_count: 43
  slug: accor-context
layout: provider
modified: '2026-09-22'
name: Accor
nav: Providers
network: true
overview: 'Accor publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, Travel, Hotels, and Technology.


  The Accor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Accor''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, and 15 more developer resources.'
random_paper: 14
rules:
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: Accor API Rules
  rule_count: 10
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 2
  slug: accor-rules
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 13
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 21.3
    developer_ergonomics: 45.2
    discoverability: 75.9
    operational_transparency: 0.0
  previous_composite: 38.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Accor Domain Security
  slug: accor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: accor
tags:
- Company
- Hospitality
- Travel
- Hotels
- Technology
website: https://accor.com/
---
