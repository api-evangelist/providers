---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'Accompany API as documented publicly: 41 operations. Contract generated from the documentation by API Evangelist (2026-10-27); not the provider''s own document.'
  name: Accompany API
  slug: accompany-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/accompany/rules/accompany-rules.yml
  title: ''
  type: Spectral
  url: rules/accompany-rules.yml
- group: design
  href: https://artifacts.apis.io/accompany/json-ld/accompany-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/accompany-context.jsonld
- group: design
  href: https://artifacts.apis.io/accompany/vocabulary/accompany-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/accompany-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/accompany/data-model/accompany-data-model.yml
  title: ''
  type: DataModel
  url: data-model/accompany-data-model.yml
- group: design
  href: https://artifacts.apis.io/accompany/conventions/accompany-conventions.yml
  title: ''
  type: Conventions
  url: conventions/accompany-conventions.yml
- group: design
  href: https://artifacts.apis.io/accompany/conformance/accompany-conformance.yml
  title: ''
  type: Conformance
  url: conformance/accompany-conformance.yml
- group: other
  href: https://artifacts.apis.io/accompany/hosts/accompany-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accompany-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.zendesk.com/documentation/developer-tools/getting-started/getting-a-trial-or-sponsored-account-for-development/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.zendesk.com/
- group: company
  title: ''
  type: Website
  url: https://www.accompany.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.accompany.com/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.accompany.com/privacy/
- group: operate
  title: ''
  type: HelpCenter
  url: https://accompany.zendesk.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/accompany
coverage:
  checked: '2026-10-27'
  detail: Accompany was acquired by Cisco and its website is a static acquisition announcement page with no API or developer documentation.
  evidence:
  - status: 200
    url: https://www.accompany.com/
  reason: defunct
  state: none
created: '2026-07-17'
description: Accompany was a relationship-intelligence startup that built people-and-company intelligence for executives, backed by Cowboy Ventures and CRV. It was acquired by Cisco (announced May 2018) and folded into Cisco's collaboration products; www.accompany.com is now a static acquisition-announcement page. Enrichment pass 2026-07-17 verified there is no live product, developer portal, documentation, OpenAPI, or any /.well-known/ or /llms.txt surface (the host is an nginx catch-all returning the same parked HTML for every path). No API artifacts exist to harvest; retained as a defunct/acquired VC-portfolio lead.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/accompany.png
json_schemas:
- name: GetApiServicesZisInboundWebhooksGenericIntegrationUuidRespon
  property_count: 15
  slug: accompany-get-api-services-zis-inbound-webhooks-generic-integration-uuid-respon
- name: PostApiServicesZisInboundWebhooksGenericIntegrationResponse
  property_count: 11
  slug: accompany-post-api-services-zis-inbound-webhooks-generic-integration-response
- name: PostApiSunshineObjectsTypesRequest
  property_count: 14
  slug: accompany-post-api-sunshine-objects-types-request
- name: PostApiV2UserProfilesEventsRequest
  property_count: 12
  slug: accompany-post-api-v2-user-profiles-events-request
- name: PutApiV2UserProfilesRequest
  property_count: 7
  slug: accompany-put-api-v2-user-profiles-request
- name: PutApiV2UserProfilesResponse
  property_count: 9
  slug: accompany-put-api-v2-user-profiles-response
jsonld:
- class_count: 41
  name: Accompany Context
  property_count: 81
  slug: accompany-context
layout: provider
modified: '2026-07-17'
name: Accompany
nav: Providers
network: true
overview: 'Accompany is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Relationship Intelligence, Sales Intelligence, and Acquired.


  The Accompany catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Accompany''s developer surface includes getting-started guide, documentation, and 12 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Accompany API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 1
  slug: accompany-rules
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  previous_composite: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/accompany/accompany-2026-07-25T181434.png
security:
- kind: domain-security
  name: Accompany Domain Security
  slug: accompany-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: accompany
tags:
- Company
- Enterprise
- Relationship Intelligence
- Sales Intelligence
- Acquired
- Defunct
website: https://www.accompany.com/
---
