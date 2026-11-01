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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: FastAPI based Federal Contracts API for Developers
  name: GovCon API
  slug: govcon-api
- description: 'govconapi-com API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: govconapi-com API
  slug: govconapi-com-api
artifact_total: 12
common:
- group: commercial
  title: ''
  type: TermsOfService
  url: https://govconapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://govconapi.com/privacy
- group: commercial
  href: https://artifacts.apis.io/govconapi-com/plans/govconapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/govconapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/govconapi-com/rules/govconapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/govconapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/govconapi-com/json-ld/govconapi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/govconapi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/govconapi-com/vocabulary/govconapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/govconapi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/govconapi-com/data-model/govconapi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/govconapi-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/govconapi-com/conformance/govconapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/govconapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/govconapi-com/llms/govconapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/govconapi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/govconapi-com/well-known/govconapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/govconapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/govconapi-com/hosts/govconapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/govconapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/govconapi-com/vendors/govconapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/govconapi-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://govconapi.com/changelog
- group: auth
  href: https://artifacts.apis.io/govconapi-com/security/govconapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/govconapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://govconapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://govconapi.com/api-guide
- group: docs
  title: ''
  type: APIReference
  url: https://govconapi.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://govconapi.com/api-guide/guides/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://govconapi.com/pricing
created: '2026-10-30'
description: GovCon API provides developers access to U.S. federal procurement data via a REST API and MCP server. It offers endpoints for SAM.gov contract opportunities, FPDS contracts, subawards, registrations, exclusions, solicitation documents, forecasts, labor rates, and bid protests, enabling integration of procurement data into applications and AI agents. Users can obtain a free API key after email verification.
image: https://govconapi.com/static/apple-touch-icon.png
json_schemas:
- name: GetApiV1CompaniesUeiPrimeRelationshipsResponse
  property_count: 2
  slug: govconapi-com-get-api-v1-companies-uei-prime-relationships-response
- name: GetApiV1CompaniesUeiResponse
  property_count: 27
  slug: govconapi-com-get-api-v1-companies-uei-response
- name: GetApiV1CompaniesUeiSubawardsResponse
  property_count: 2
  slug: govconapi-com-get-api-v1-companies-uei-subawards-response
- name: GetApiV1EntitiesE7Xwkerhvvd9Response
  property_count: 2
  slug: govconapi-com-get-api-v1-entities-e7-xwkerhvvd9-response
- name: GetApiV1EntitiesSearchResponse
  property_count: 14
  slug: govconapi-com-get-api-v1-entities-search-response
- name: GetApiV1SubawardsSubawardsamreportidResponse
  property_count: 7
  slug: govconapi-com-get-api-v1-subawards-subawardsamreportid-response
jsonld:
- class_count: 12
  name: Govconapi Com Context
  property_count: 45
  slug: govconapi-com-context
layout: provider
modified: '2026-10-30'
name: govconapi-com
nav: Providers
network: true
overview: 'govconapi-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Federal, Procurement, Data, and API.


  The govconapi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  govconapi-com''s developer surface includes changelog, documentation, API reference, getting-started guide, pricing, and 14 more developer resources.'
plans:
- name: Govconapi Com Plans Pricing
  plan_count: 3
  slug: govconapi-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: govconapi-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: govconapi-com-rules
score:
  band: developing
  composite: 49.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 83.5
    catalog_earned_first_party: 0.0
    catalog_gap: 31.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 79.1
    contract_quality: 53.4
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Govconapi Com Domain Security
  slug: govconapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: govconapi-com
tags:
- Company
- Federal
- Procurement
- Data
- API
website: https://govconapi.com/
---
