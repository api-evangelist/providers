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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.8
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: HubRise API provides REST endpoints for orders, deliveries, catalogs, inventories, customers, and callbacks. Base URL is https://api.hubrise.com/v1 as documented.
  name: HubRise API
  slug: hubrise-api-2
- baseURL: https://api.hubrise.com
  baseurl_source: declared
  description: 'HubRise API as documented publicly: 44 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: HubRise API
  slug: hubrise-api
artifact_total: 14
asyncapis:
- description: ''
  name: Hubrise Webhooks
  slug: hubrise-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/hubrise/plans/hubrise-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hubrise-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/hubrise/rules/hubrise-rules.yml
  title: ''
  type: Spectral
  url: rules/hubrise-rules.yml
- group: design
  href: https://artifacts.apis.io/hubrise/json-ld/hubrise-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hubrise-context.jsonld
- group: design
  href: https://artifacts.apis.io/hubrise/vocabulary/hubrise-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hubrise-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/hubrise/asyncapi/hubrise-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hubrise-webhooks.yml
- group: design
  href: https://artifacts.apis.io/hubrise/data-model/hubrise-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hubrise-data-model.yml
- group: operate
  href: https://artifacts.apis.io/hubrise/changelog/hubrise-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hubrise-changelog.yml
- group: auth
  href: https://artifacts.apis.io/hubrise/authentication/hubrise-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hubrise-authentication.yml
- group: design
  href: https://artifacts.apis.io/hubrise/conformance/hubrise-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hubrise-conformance.yml
- group: other
  href: https://artifacts.apis.io/hubrise/hosts/hubrise-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hubrise-hosts.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.hubrise.com/developers/changelog
- group: auth
  href: https://artifacts.apis.io/hubrise/security/hubrise-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hubrise-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hubrise.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.hubrise.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.hubrise.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.hubrise.com/developers/api/general-concepts
- group: start
  title: ''
  type: GettingStarted
  url: https://www.hubrise.com/developers/quick-start
- group: operate
  title: ''
  type: Support
  url: https://www.hubrise.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.hubrise.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hubrise.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://manager.hubrise.com/signup?locale=en-GB
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hubrise.com/legal/general-terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hubrise.com/legal/legal-notices
created: '2026-10-20'
description: HubRise provides an integration platform for retail and hospitality businesses, connecting point‑of‑sale (EPOS) systems, delivery platforms, marketing tools, and inventory management into a single ecosystem. Their solution enables merchants to centralise orders, synchronise product catalogs, manage inventory across multiple sales channels, and gain unified analytics. With over 2,500 customers across 20+ countries, HubRise supports more than 110 integrations, offering APIs and developer documentation for seamless integration and white‑label partnerships.
json_schemas:
- name: GetCatalogsCatalogidOptionListsOptionlistidOptionsIdResponse
  property_count: 11
  slug: hubrise-get-catalogs-catalogid-option-lists-optionlistid-options-id-response
- name: GetCatalogsCatalogidProductsIdResponse
  property_count: 10
  slug: hubrise-get-catalogs-catalogid-products-id-response
- name: GetCatalogsCatalogidProductsProductidSkusIdResponse
  property_count: 13
  slug: hubrise-get-catalogs-catalogid-products-productid-skus-id-response
- name: PostLocationOrdersRequest
  property_count: 26
  slug: hubrise-post-location-orders-request
- name: PostLocationsLocationidCatalogsRequest
  property_count: 8
  slug: hubrise-post-locations-locationid-catalogs-request
- name: PostLocationsLocationidOrdersRequest
  property_count: 26
  slug: hubrise-post-locations-locationid-orders-request
jsonld:
- class_count: 45
  name: Hubrise Context
  property_count: 74
  slug: hubrise-context
layout: provider
modified: '2026-10-20'
name: HubRise
nav: Providers
network: true
overview: 'HubRise is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, Retail, Hospitality, and API.


  The HubRise catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  HubRise''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 16 more developer resources.'
plans:
- name: Hubrise Plans Pricing
  plan_count: 6
  slug: hubrise-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: HubRise API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: hubrise-rules
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 36.1
    developer_ergonomics: 57.1
    discoverability: 62.5
    operational_transparency: 23.7
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
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hubrise Authentication
  slug: hubrise-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Hubrise Domain Security
  slug: hubrise-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: hubrise
tags:
- Company
- Integration
- Retail
- Hospitality
- API
website: https://hubrise.com/
---
