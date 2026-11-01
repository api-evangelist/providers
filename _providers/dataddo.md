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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Headless API for managing pipelines and data integration. Documentation at headless.dataddo.com/customer-api/v1/docs/openapi.
  name: Dataddo Headless API
  slug: dataddo-headless-api
- baseURL: https://webhook.dataddo.com
  baseurl_source: declared
  description: 'Dataddo API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-10-20); not the provider''s own document.'
  name: Dataddo API
  slug: dataddo-api
artifact_total: 14
asyncapis:
- description: ''
  name: Dataddo Webhooks
  slug: dataddo-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/dataddo/plans/dataddo-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dataddo-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dataddo/rules/dataddo-rules.yml
  title: ''
  type: Spectral
  url: rules/dataddo-rules.yml
- group: design
  href: https://artifacts.apis.io/dataddo/json-ld/dataddo-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dataddo-context.jsonld
- group: design
  href: https://artifacts.apis.io/dataddo/vocabulary/dataddo-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dataddo-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dataddo/asyncapi/dataddo-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/dataddo-webhooks.yml
- group: design
  href: https://artifacts.apis.io/dataddo/data-model/dataddo-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dataddo-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dataddo/changelog/dataddo-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dataddo-changelog.yml
- group: auth
  href: https://artifacts.apis.io/dataddo/authentication/dataddo-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dataddo-authentication.yml
- group: design
  href: https://artifacts.apis.io/dataddo/conformance/dataddo-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dataddo-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dataddo/llms/dataddo-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dataddo-llms.txt
- group: other
  href: https://artifacts.apis.io/dataddo/hosts/dataddo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dataddo-hosts.yml
- group: other
  href: https://artifacts.apis.io/dataddo/vendors/dataddo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dataddo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dataddo.com/terms/
- group: start
  title: ''
  type: SignUp
  url: https://www.dataddo.com/signup/?ui_mode=data_to_ai
- group: auth
  title: ''
  type: Security
  url: https://www.dataddo.com/platform/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dataddo.com/privacy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.dataddo.com/docs/release-notes
- group: auth
  href: https://artifacts.apis.io/dataddo/security/dataddo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dataddo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dataddo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dataddo.com/
- group: docs
  title: ''
  type: APIReference
  url: https://headless.dataddo.com/customer-api/v1/docs/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.dataddo.com/docs/quick-start
- group: company
  title: ''
  type: Blog
  url: https://blog.dataddo.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dataddo.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://app.dataddo.com/support-ticket
created: '2026-10-20'
description: Dataddo provides a data integration platform that connects sources to destinations, enabling real‑time CDC, batch ingestion, and AI data activation. It offers a headless API for managing pipelines, supports 400+ connectors, and includes tools for data governance, security, and AI model feeding.
image: https://www.dataddo.com/images/share.png
json_schemas:
- name: PostConnectorsSnapchatCreateSourceRequest
  property_count: 24
  slug: dataddo-post-connectors-snapchat-create-source-request
- name: PostConnectorsSnapchatCreateSourceResponse
  property_count: 2
  slug: dataddo-post-connectors-snapchat-create-source-response
- name: PostRequest
  property_count: 3
  slug: dataddo-post-request
- name: PostServicesRequest
  property_count: 5
  slug: dataddo-post-services-request
- name: PostServicesResponse
  property_count: 1
  slug: dataddo-post-services-response
- name: PostSourcesIdExtractionEnqueueRequest
  property_count: 1
  slug: dataddo-post-sources-id-extraction-enqueue-request
jsonld:
- class_count: 6
  name: Dataddo Context
  property_count: 34
  slug: dataddo-context
layout: provider
modified: '2026-10-20'
name: Dataddo
nav: Providers
network: true
overview: 'Dataddo is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Integration, API Platform, Artificial Intelligence, Real-Time, and ETL.


  The Dataddo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Dataddo''s developer surface includes changelog, authentication, signup flow, documentation, API reference, getting-started guide, engineering blog, and 18 more developer resources.'
plans:
- name: Dataddo Plans Pricing
  plan_count: 3
  slug: dataddo-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Dataddo API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: dataddo-rules
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 33.7
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 34.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 13
      marker_coverage: 100.0
      total: 13
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dataddo Authentication
  slug: dataddo-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dataddo Domain Security
  slug: dataddo-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: dataddo
tags:
- Data Integration
- API Platform
- Artificial Intelligence
- Real-Time
- ETL
website: https://www.dataddo.com/
---
