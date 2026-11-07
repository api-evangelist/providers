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
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://webapi.aspsms.com
  baseurl_source: declared
  description: 'ASPSMS API as documented publicly: 52 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: ASPSMS API
  slug: aspsms-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/aspsms/rules/aspsms-rules.yml
  title: ''
  type: Spectral
  url: rules/aspsms-rules.yml
- group: design
  href: https://artifacts.apis.io/aspsms/json-ld/aspsms-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aspsms-context.jsonld
- group: design
  href: https://artifacts.apis.io/aspsms/vocabulary/aspsms-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aspsms-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/aspsms/data-model/aspsms-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aspsms-data-model.yml
- group: operate
  href: https://artifacts.apis.io/aspsms/changelog/aspsms-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aspsms-changelog.yml
- group: design
  href: https://artifacts.apis.io/aspsms/conformance/aspsms-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aspsms-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aspsms/llms/aspsms-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aspsms-llms.txt
- group: other
  href: https://artifacts.apis.io/aspsms/hosts/aspsms-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aspsms-hosts.yml
- group: build
  href: https://artifacts.apis.io/aspsms/packages/aspsms-packages.yml
  title: ''
  type: SDKs
  url: packages/aspsms-packages.yml
- group: build
  href: https://artifacts.apis.io/aspsms/packages/aspsms-packages.yml
  title: ''
  type: Packages
  url: packages/aspsms-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aspsms.com/en/privacy/
- group: start
  title: ''
  type: Login
  url: https://www.aspsms.com/en/login/
- group: auth
  href: https://artifacts.apis.io/aspsms/security/aspsms-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aspsms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.aspsms.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.aspsms.com/en/documentation/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aspsms.com/en/prices/
- group: company
  title: ''
  type: Blog
  url: https://www.aspsms.com/en/Blog/
- group: operate
  title: ''
  type: Support
  url: https://www.aspsms.com/en/support/
coverage:
  checked: '2026-10-26'
  detail: API documentation pages return 403 HTML blocks, preventing access to machine‑readable specs.
  evidence:
  - status: 403
    url: https://www.aspsms.com/en/json/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: ASPSMS provides a global SMS gateway service for businesses, offering multiple integration options including JSON REST, SOAP, HTTP POST, SMTP, and email‑to‑SMS. The platform supports two‑factor authentication, bulk messaging, and two‑way SMS, with no licence, setup, or monthly fees. Documentation, pricing, and developer resources are available in several languages, and the service includes a web portal for managing credits and messages.
json_schemas:
- name: PostAspsmsdeactivatependingsmswithtransactionreferencenumber
  property_count: 1
  slug: aspsms-post-aspsmsdeactivatependingsmswithtransactionreferencenumber
- name: PostAspsmsestimatecreditconsumptionRequest
  property_count: 1
  slug: aspsms-post-aspsmsestimatecreditconsumption-request
- name: PostAspsmssendsmsRequest
  property_count: 1
  slug: aspsms-post-aspsmssendsms-request
- name: PostMsisdndlrstatignorelistaddPostRequest
  property_count: 1
  slug: aspsms-post-msisdndlrstatignorelistadd-post-request
- name: PostMsisdndlrstatignorelistremovePostRequest
  property_count: 1
  slug: aspsms-post-msisdndlrstatignorelistremove-post-request
- name: PostPhonenumbersAddRequest
  property_count: 1
  slug: aspsms-post-phonenumbers-add-request
jsonld:
- class_count: 8
  name: Aspsms Context
  property_count: 6
  slug: aspsms-context
layout: provider
modified: '2026-10-26'
name: ASPSMS
nav: Providers
network: true
overview: 'ASPSMS is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include SMS, Messaging, Communications, and Business.


  The ASPSMS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ASPSMS''s developer surface includes changelog, documentation, pricing, engineering blog, support, and 13 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: ASPSMS API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: aspsms-rules
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 17.1
    contract_governance: 35.6
    contract_quality: 23.7
    developer_ergonomics: 15.5
    discoverability: 60.7
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 31.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 15.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 22.2
screenshot: https://apis.io/screenshots/aspsms/aspsms-2026-11-03T121214.png
security:
- kind: domain-security
  name: Aspsms Domain Security
  slug: aspsms-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: aspsms
tags:
- SMS
- Messaging
- Communications
- Business
website: https://www.aspsms.com/
---
