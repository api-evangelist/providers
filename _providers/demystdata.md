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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Demystdata API as documented publicly: 24 operations. Contract generated from the documentation by API Evangelist (2026-10-23); not the provider''s own document.'
  name: Demystdata API
  slug: demystdata-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/demystdata/rules/demystdata-rules.yml
  title: ''
  type: Spectral
  url: rules/demystdata-rules.yml
- group: design
  href: https://artifacts.apis.io/demystdata/json-ld/demystdata-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/demystdata-context.jsonld
- group: design
  href: https://artifacts.apis.io/demystdata/vocabulary/demystdata-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/demystdata-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/demystdata/data-model/demystdata-data-model.yml
  title: ''
  type: DataModel
  url: data-model/demystdata-data-model.yml
- group: design
  href: https://artifacts.apis.io/demystdata/conformance/demystdata-conformance.yml
  title: ''
  type: Conformance
  url: conformance/demystdata-conformance.yml
- group: other
  href: https://artifacts.apis.io/demystdata/hosts/demystdata-hosts.yml
  title: ''
  type: Hosts
  url: hosts/demystdata-hosts.yml
- group: other
  href: https://artifacts.apis.io/demystdata/vendors/demystdata-vendors.yml
  title: ''
  type: Vendors
  url: vendors/demystdata-vendors.yml
- group: auth
  href: https://artifacts.apis.io/demystdata/security/demystdata-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/demystdata-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://demyst.com
- group: operate
  title: ''
  type: Contact
  url: https://demyst.com/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://demyst.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://demyst.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://demyst.com/
- group: operate
  title: ''
  type: Support
  url: https://demyst.com/contact
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://demyst.com/mcp
  - status: 200
    url: https://demyst.com
  - status: 403
    url: https://equityzen.com/company/demystdata
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-22'
description: Demystdata provides an external data management platform that enables businesses to ingest, store, and orchestrate data from multiple sources. The platform offers APIs for data ingestion, transformation, and retrieval, supporting compliance and privacy controls. Founded in 2026, Demystdata serves enterprises seeking scalable data pipelines and governance.
image: https://demyst.com/_next/static/media/demyst_meta_image.f5a4009b.png
json_schemas:
- name: GetCatalogProvidersProvideridRelatedResponse
  property_count: 3
  slug: demystdata-get-catalog-providers-providerid-related-response
- name: GetV2ChannelResponse
  property_count: 4
  slug: demystdata-get-v2-channel-response
- name: PostJwtCreateResponse
  property_count: 4
  slug: demystdata-post-jwt-create-response
- name: PostOauthTokenResponse
  property_count: 4
  slug: demystdata-post-oauth-token-response
- name: PostV2ChannelRequest
  property_count: 3
  slug: demystdata-post-v2-channel-request
- name: PostV2ChannelResponse
  property_count: 4
  slug: demystdata-post-v2-channel-response
jsonld:
- class_count: 11
  name: Demystdata Context
  property_count: 17
  slug: demystdata-context
layout: provider
modified: '2026-10-22'
name: Demystdata
nav: Providers
network: true
overview: 'Demystdata is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Data Management, API Platform, Enterprise, Cloud, and Privacy.


  The Demystdata catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Demystdata''s developer surface includes documentation, support, and 12 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Demystdata API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: demystdata-rules
score:
  band: emerging
  composite: 17.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 10.5
    contract_governance: 19.7
    contract_quality: 24.9
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 21.2
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/demystdata/demystdata-2026-11-03T130522.png
security:
- kind: domain-security
  name: Demystdata Domain Security
  slug: demystdata-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: demystdata
tags:
- Data Management
- API Platform
- Enterprise
- Cloud
- Privacy
website: https://demyst.com
---
