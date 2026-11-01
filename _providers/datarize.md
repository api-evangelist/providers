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
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.7
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Data integration and analytics API providing endpoints for data ingestion, processing, and retrieval.
  name: Datarize API
  slug: datarize-api-2
- baseURL: https://api.datarize.ai
  baseurl_source: declared
  description: 'Datarize API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-22); not the provider''s own document.'
  name: Datarize API
  slug: datarize-api
artifact_total: 10
asyncapis:
- description: ''
  name: Datarize Webhooks
  slug: datarize-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/datarize/plans/datarize-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datarize-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datarize/rules/datarize-rules.yml
  title: ''
  type: Spectral
  url: rules/datarize-rules.yml
- group: design
  href: https://artifacts.apis.io/datarize/json-ld/datarize-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datarize-context.jsonld
- group: design
  href: https://artifacts.apis.io/datarize/vocabulary/datarize-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datarize-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datarize/asyncapi/datarize-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/datarize-webhooks.yml
- group: design
  href: https://artifacts.apis.io/datarize/data-model/datarize-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datarize-data-model.yml
- group: auth
  href: https://artifacts.apis.io/datarize/authentication/datarize-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datarize-authentication.yml
- group: design
  href: https://artifacts.apis.io/datarize/conformance/datarize-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datarize-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datarize/llms/datarize-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datarize-llms.txt
- group: other
  href: https://artifacts.apis.io/datarize/hosts/datarize-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datarize-hosts.yml
- group: other
  href: https://artifacts.apis.io/datarize/vendors/datarize-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datarize-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policy.datarize.ai/ko/terms
- group: auth
  title: ''
  type: Security
  url: https://www.datarize.ai/blog/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policy.datarize.ai/ko/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datarize.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.datarize.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.datarize.ai/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.datarize.ai/
- group: auth
  href: https://artifacts.apis.io/datarize/security/datarize-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datarize-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.datarize.ai
coverage:
  checked: '2026-10-22'
  detail: Documentation pages are HTML without machine‑readable OpenAPI or other contract files.
  evidence:
  - status: 200
    url: https://developer.datarize.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Datarize provides data integration and analytics solutions, enabling businesses to connect, transform, and visualize data from multiple sources. The platform offers APIs for data ingestion, processing, and retrieval, supporting formats like JSON and CSV. Datarize aims to simplify data pipelines, improve data quality, and accelerate insights for enterprises across various industries.
image: https://framerusercontent.com/assets/MakldfTIffp0DiQVqqs9Qmdswg.png
json_schemas:
- name: PostV1EventsRequest
  property_count: 5
  slug: datarize-post-v1-events-request
- name: PostV1EventsResponse
  property_count: 1
  slug: datarize-post-v1-events-response
jsonld:
- class_count: 2
  name: Datarize Context
  property_count: 6
  slug: datarize-context
layout: provider
modified: '2026-10-22'
name: Datarize
nav: Providers
network: true
overview: 'Datarize is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Integration, Analytics, API Platform, and Enterprise.


  The Datarize catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Datarize''s developer surface includes authentication, pricing, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
plans:
- name: Datarize Plans Pricing
  plan_count: 1
  slug: datarize-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Datarize API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: datarize-rules
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 29.2
    developer_ergonomics: 35.7
    discoverability: 57.1
    operational_transparency: 18.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
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
  name: Datarize Authentication
  slug: datarize-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Datarize Domain Security
  slug: datarize-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: datarize
tags:
- Company
- Data Integration
- Analytics
- API Platform
- Enterprise
website: https://www.datarize.ai
---
