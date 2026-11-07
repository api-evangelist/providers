---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 17.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Duplicati API provides backup management endpoints.
  name: Duplicati API
  slug: duplicati-api-2
- baseURL: https://graph.microsoft.com
  baseurl_source: declared
  description: 'Duplicati API as documented publicly: 220 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Duplicati API
  slug: duplicati-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/duplicati/plans/duplicati-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/duplicati-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/duplicati/rules/duplicati-rules.yml
  title: ''
  type: Spectral
  url: rules/duplicati-rules.yml
- group: design
  href: https://artifacts.apis.io/duplicati/json-ld/duplicati-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/duplicati-context.jsonld
- group: design
  href: https://artifacts.apis.io/duplicati/vocabulary/duplicati-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/duplicati-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/duplicati/data-model/duplicati-data-model.yml
  title: ''
  type: DataModel
  url: data-model/duplicati-data-model.yml
- group: design
  href: https://artifacts.apis.io/duplicati/conformance/duplicati-conformance.yml
  title: ''
  type: Conformance
  url: conformance/duplicati-conformance.yml
- group: agent
  href: https://artifacts.apis.io/duplicati/llms/duplicati-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duplicati-llms.txt
- group: agent
  href: https://artifacts.apis.io/duplicati/well-known/duplicati-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/duplicati-well-known.yml
- group: other
  href: https://artifacts.apis.io/duplicati/hosts/duplicati-hosts.yml
  title: ''
  type: Hosts
  url: hosts/duplicati-hosts.yml
- group: other
  href: https://artifacts.apis.io/duplicati/vendors/duplicati-vendors.yml
  title: ''
  type: Vendors
  url: vendors/duplicati-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://duplicati.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://duplicati.com/legal/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.duplicati.com/getting-started/installation
- group: auth
  href: https://artifacts.apis.io/duplicati/security/duplicati-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duplicati-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://duplicati.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://duplicati.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://duplicati.com/articles
- group: docs
  title: ''
  type: Documentation
  url: https://duplicati.com/download
created: '2026-10-28'
description: Duplicati provides a free, open-source backup solution that offers zero‑trust, fully encrypted backups for your data. It integrates with all major cloud providers, ensuring secure storage and easy accessibility, while supporting individuals and enterprises with robust features and a user‑friendly interface.
image: https://framerusercontent.com/images/sK16ZZeM3bLvzk4MGpFsclRNU.png
json_schemas:
- name: GetGmailV1UsersUseridLabelsIdResponse
  property_count: 2
  slug: duplicati-get-gmail-v1-users-userid-labels-id-response
- name: GetGmailV1UsersUseridMessagesIdResponse
  property_count: 2
  slug: duplicati-get-gmail-v1-users-userid-messages-id-response
- name: PatchGmailV1UsersUseridLabelsIdResponse
  property_count: 2
  slug: duplicati-patch-gmail-v1-users-userid-labels-id-response
- name: PostGmailV1UsersUseridMessagesBatchmodifyRequest
  property_count: 3
  slug: duplicati-post-gmail-v1-users-userid-messages-batchmodify-request
- name: PostGmailV1UsersUseridMessagesImportRequest
  property_count: 2
  slug: duplicati-post-gmail-v1-users-userid-messages-import-request
- name: PutV1ContactgroupResourcenameContactgroupsRequest
  property_count: 12
  slug: duplicati-put-v1-contactgroup-resourcename-contactgroups-request
jsonld:
- class_count: 16
  name: Duplicati Context
  property_count: 23
  slug: duplicati-context
layout: provider
modified: '2026-10-28'
name: Duplicati
nav: Providers
network: true
overview: 'Duplicati is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Backup, Open Source, Cloud, and Security.


  The Duplicati catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Duplicati''s developer surface includes getting-started guide, pricing, engineering blog, documentation, and 14 more developer resources.'
plans:
- name: Duplicati Plans Pricing
  plan_count: 3
  slug: duplicati-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Duplicati API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: duplicati-rules
score:
  band: thin
  composite: 28.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 27.6
    developer_ergonomics: 11.9
    discoverability: 73.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
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
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/duplicati/duplicati-2026-11-03T131126.png
security:
- kind: domain-security
  name: Duplicati Domain Security
  slug: duplicati-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: duplicati
tags:
- Company
- Backup
- Open Source
- Cloud
- Security
website: https://duplicati.com/
---
