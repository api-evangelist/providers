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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.7
  scored_at: '2026-11-06'
api_count: 9
apis:
- description: The Access Token API from SuiteCRM — 1 operation(s) for access token.
  name: SuiteCRM Access Token API
  slug: suitecrm-access-token-api
- description: The Authorize API from SuiteCRM — 1 operation(s) for authorize.
  name: SuiteCRM Authorize API
  slug: suitecrm-authorize-api
- description: The Current User API from SuiteCRM — 1 operation(s) for current user.
  name: SuiteCRM Current User API
  slug: suitecrm-current-user-api
- description: The Listview API from SuiteCRM — 1 operation(s) for listview.
  name: SuiteCRM Listview API
  slug: suitecrm-listview-api
- description: The Logout API from SuiteCRM — 1 operation(s) for logout.
  name: SuiteCRM Logout API
  slug: suitecrm-logout-api
- description: The Meta API from SuiteCRM — 3 operation(s) for meta.
  name: SuiteCRM Meta API
  slug: suitecrm-meta-api
- description: The Module API from SuiteCRM — 6 operation(s) for module.
  name: SuiteCRM Module API
  slug: suitecrm-module-api
- description: The Search Defs API from SuiteCRM — 1 operation(s) for search defs.
  name: SuiteCRM Search Defs API
  slug: suitecrm-search-defs-api
- description: The User Preferences API from SuiteCRM — 1 operation(s) for user preferences.
  name: SuiteCRM User Preferences API
  slug: suitecrm-user-preferences-api
artifact_total: 18
common:
- group: design
  href: https://artifacts.apis.io/suitecrm/rules/suitecrm-rules.yml
  title: ''
  type: Spectral
  url: rules/suitecrm-rules.yml
- group: design
  href: https://artifacts.apis.io/suitecrm/json-ld/suitecrm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/suitecrm-context.jsonld
- group: design
  href: https://artifacts.apis.io/suitecrm/vocabulary/suitecrm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/suitecrm-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/suitecrm/data-model/suitecrm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/suitecrm-data-model.yml
- group: design
  href: https://artifacts.apis.io/suitecrm/conformance/suitecrm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/suitecrm-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://suitecrm.com/security-policy/security/
- group: company
  title: ''
  type: Newsroom
  url: https://suitecrm.com/category/news/
- group: start
  title: ''
  type: Login
  url: https://suitecrm.com/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SuiteCRM
- group: operate
  title: ''
  type: ChangeLog
  url: https://suitecrm.com/releases/
- group: company
  title: ''
  type: Blog
  url: https://suitecrm.com/hacktoberfest-2022-x-suitecrm/blog/
- group: auth
  href: https://artifacts.apis.io/suitecrm/security/suitecrm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/suitecrm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://suitecrm.com/
- group: docs
  title: ''
  type: Documentation
  url: https://suitecrm.com/what-is-suitecrm/
- group: start
  title: ''
  type: GettingStarted
  url: https://suitecrm.com/download/
- group: operate
  title: ''
  type: Roadmap
  url: https://suitecrm.com/suitecrm-roadmap/
- group: commercial
  title: ''
  type: Pricing
  url: https://suitecrm.com/suitecrmhosted/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://suitecrm.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://suitecrm.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://suitecrm.com/contact-us/
coverage:
  checked: 2026-09-21
  detail: Documentation pages are served as HTML shells with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.suitecrm.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-21'
description: 'SuiteCRM is the world’s #1 open source CRM, offering self‑hosted deployments for full data sovereignty and a hosted SaaS option with no licence fees. It provides a flexible data model, robust reporting, and extensive customization for sales, marketing, and support teams. The platform supports on‑premise installations as well as SuiteCRM Hosted, delivering enterprise‑grade features without vendor lock‑in.'
image: https://suitecrm.com/wp-content/uploads/2018/01/favicon-144-1.png
json_schemas:
- name: PatchApiV8ModuleRequest
  property_count: 3
  slug: suitecrm-patch-api-v8-module-request
- name: PostApiAccessTokenRequest
  property_count: 8
  slug: suitecrm-post-api-access-token-request
- name: PostApiAccessTokenResponse
  property_count: 4
  slug: suitecrm-post-api-access-token-response
- name: PostApiV8ModuleAccountsIdRelationshipsContactsRequest
  property_count: 2
  slug: suitecrm-post-api-v8-module-accounts-id-relationships-contacts-request
- name: PostApiV8ModuleModulenameIdRelationshipsLinkfieldnameRequest
  property_count: 2
  slug: suitecrm-post-api-v8-module-modulename-id-relationships-linkfieldname-request
- name: PostApiV8ModuleRequest
  property_count: 2
  slug: suitecrm-post-api-v8-module-request
jsonld:
- class_count: 7
  name: Suitecrm Context
  property_count: 14
  slug: suitecrm-context
layout: provider
modified: '2026-09-21'
name: SuiteCRM
nav: Providers
network: true
overview: 'SuiteCRM is listed with 9 APIs on the [APIs.io](https://apis.io/) network, including Access Token API, Authorize API, Current User API, and 6 more. Tagged areas include CRM, Open Source, Software-as-a-Service, Self-Hosted, and Enterprise.


  The SuiteCRM catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SuiteCRM''s developer surface includes changelog, engineering blog, documentation, getting-started guide, pricing, support, and 14 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: SuiteCRM API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: suitecrm-rules
score:
  band: emerging
  composite: 24.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.4
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 26.4
    developer_ergonomics: 14.3
    discoverability: 63.4
    operational_transparency: 18.4
  previous_composite: 34.9
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/suitecrm/suitecrm-2026-10-11T130447.png
security:
- kind: domain-security
  name: Suitecrm Domain Security
  slug: suitecrm-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: suitecrm
tags:
- CRM
- Open Source
- Software-as-a-Service
- Self-Hosted
- Enterprise
website: https://suitecrm.com/
---
