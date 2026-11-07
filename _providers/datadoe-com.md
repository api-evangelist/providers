---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'DataDoe API as documented publicly: 68 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DataDoe API
  slug: datadoe-com-api
artifact_total: 14
asyncapis:
- description: ''
  name: Datadoe Com Webhooks
  slug: datadoe-com-webhooks
common:
- group: docs
  title: ''
  type: Documentation
  url: https://www.datadoe.com/hub/docs
- group: commercial
  href: https://artifacts.apis.io/datadoe-com/plans/datadoe-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datadoe-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/datadoe-com/rules/datadoe-com-rules.yml
  title: ''
  type: Spectral
  url: rules/datadoe-com-rules.yml
- group: design
  href: https://artifacts.apis.io/datadoe-com/json-ld/datadoe-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datadoe-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/datadoe-com/vocabulary/datadoe-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datadoe-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datadoe-com/asyncapi/datadoe-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/datadoe-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/datadoe-com/data-model/datadoe-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datadoe-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/datadoe-com/changelog/datadoe-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/datadoe-com-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.datadoe.com/security
- group: auth
  href: https://artifacts.apis.io/datadoe-com/authentication/datadoe-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/datadoe-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/datadoe-com/conformance/datadoe-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datadoe-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datadoe-com/llms/datadoe-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/datadoe-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/datadoe-com/well-known/datadoe-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/datadoe-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/datadoe-com/hosts/datadoe-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datadoe-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/datadoe-com/vendors/datadoe-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datadoe-com-vendors.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.datadoe.com/hub/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.datadoe.com/legal/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://www.datadoe.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datadoe.com/legal/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.datadoe.com/solutions/amazon/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.youtube.com/watch?v=9YQd7M2dMyY
- group: docs
  title: ''
  type: APIReference
  url: https://api.datadoe.com/api/v1/docs
- group: auth
  href: https://artifacts.apis.io/datadoe-com/security/datadoe-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/datadoe-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/datadoe-com/security/datadoe-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datadoe-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datadoe.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.datadoe.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.datadoe.com/blog
- group: operate
  title: ''
  type: Changelog
  url: https://www.datadoe.com/changelog
created: '2026-11-04'
description: DataDoe provides an Amazon data and action layer for AI agents, aggregating Seller Central, Vendor Central, and Amazon Ads data into a unified schema. It offers MCP, API, and BigQuery access, enabling AI to read fresh Amazon data and perform actions such as listings, pricing, orders, and ad management. Pricing starts at $97/month with a 14‑day free trial.
image: https://cdn.prod.website-files.com/69c11bffdcac6281fb169db8/6ae1e9e1de86a90afb7ab846_datadoe-og-2026-10-27.png
json_schemas:
- name: GetExportsExportidRawResponse
  property_count: 1
  slug: datadoe-com-get-exports-exportid-raw-response
- name: GetExportsSourcesResponse
  property_count: 1
  slug: datadoe-com-get-exports-sources-response
- name: GetUtilSellersAndVendorsResponse
  property_count: 1
  slug: datadoe-com-get-util-sellers-and-vendors-response
- name: PostApiV1UtilSellersAndVendorsResponse
  property_count: 1
  slug: datadoe-com-post-api-v1-util-sellers-and-vendors-response
- name: PostExportsRequest
  property_count: 6
  slug: datadoe-com-post-exports-request
- name: PostExportsResponse
  property_count: 5
  slug: datadoe-com-post-exports-response
jsonld:
- class_count: 6
  name: Datadoe Com Context
  property_count: 13
  slug: datadoe-com-context
layout: provider
modified: '2026-11-04'
name: DataDoe
nav: Providers
network: true
overview: 'DataDoe is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include DataDoe, Amazon, Artificial Intelligence, MCP, and DataLayer.


  The DataDoe catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  DataDoe''s developer surface includes documentation, changelog, authentication, getting-started guide, API reference, pricing, engineering blog, and 21 more developer resources.'
plans:
- name: Datadoe Com Plans Pricing
  plan_count: 1
  slug: datadoe-com-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: DataDoe API Rules
  rule_count: 45
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 2
  slug: datadoe-com-rules
score:
  band: developing
  composite: 49.2
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 68.4
    contract_governance: 35.6
    contract_quality: 35.0
    developer_ergonomics: 52.4
    discoverability: 57.1
    operational_transparency: 34.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Datadoe Com Authentication
  slug: datadoe-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Datadoe Com Domain Security
  slug: datadoe-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Datadoe Com Trust Center
  slug: datadoe-com-trust-center
  summary_line: GDPR
slug: datadoe-com
tags:
- DataDoe
- Amazon
- Artificial Intelligence
- MCP
- DataLayer
- Software-as-a-Service
website: https://datadoe.com/
---
