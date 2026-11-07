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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Disputes Online Agentic Access
  operation_count: 8
  slug: disputes-online-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://disputes.online
  baseurl_source: declared
  description: The categories API from Disputes.online — 1 operation(s) for categories.
  name: Disputes.online Categories API
  slug: disputes-online-categories-api
- baseURL: https://disputes.online
  baseurl_source: declared
  description: The disputes API from Disputes.online — 5 operation(s) for disputes.
  name: Disputes.online Disputes API
  slug: disputes-online-disputes-api
- baseURL: https://disputes.online
  baseurl_source: declared
  description: The feeds API from Disputes.online — 2 operation(s) for feeds.
  name: Disputes.online Feeds API
  slug: disputes-online-feeds-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/disputes-online/agentic-access/disputes-online-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/disputes-online-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/disputes-online/rules/disputes-online-rules.yml
  title: ''
  type: Spectral
  url: rules/disputes-online-rules.yml
- group: design
  href: https://artifacts.apis.io/disputes-online/json-ld/disputes-online-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/disputes-online-context.jsonld
- group: design
  href: https://artifacts.apis.io/disputes-online/vocabulary/disputes-online-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/disputes-online-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/disputes-online/data-model/disputes-online-data-model.yml
  title: ''
  type: DataModel
  url: data-model/disputes-online-data-model.yml
- group: design
  href: https://artifacts.apis.io/disputes-online/errors/disputes-online-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/disputes-online-problem-types.yml
- group: design
  href: https://artifacts.apis.io/disputes-online/conformance/disputes-online-conformance.yml
  title: ''
  type: Conformance
  url: conformance/disputes-online-conformance.yml
- group: agent
  href: https://artifacts.apis.io/disputes-online/llms/disputes-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/disputes-online-llms.txt
- group: other
  href: https://artifacts.apis.io/disputes-online/hosts/disputes-online-hosts.yml
  title: ''
  type: Hosts
  url: hosts/disputes-online-hosts.yml
- group: other
  href: https://artifacts.apis.io/disputes-online/vendors/disputes-online-vendors.yml
  title: ''
  type: Vendors
  url: vendors/disputes-online-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://disputes.online/info/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://disputes.online/info/privacy
- group: start
  title: ''
  type: Login
  url: https://disputes.online/login
- group: docs
  title: ''
  type: Documentation
  url: https://docs.disputes.online/
- group: docs
  title: ''
  type: APIReference
  url: https://disputes.online/developers
- group: auth
  href: https://artifacts.apis.io/disputes-online/security/disputes-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/disputes-online-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://disputes.online/
created: '2026-11-05'
description: Disputes.online is a platform that lets users create disputes with friends, colleagues, and anyone, and make predictions on topics such as sports, politics, technology, and finance. It offers a global community for sharing and discussing disputes, with RSS feeds for new content and an API for integration. The service aims to foster engagement and insight through interactive dispute creation and prediction features.
image: https://disputes.online/og-image.png
json_schemas:
- name: Category
  property_count: 5
  slug: disputes-online-category
- name: DisputeList
  property_count: 2
  slug: disputes-online-dispute-list
- name: Dispute
  property_count: 28
  slug: disputes-online-dispute
- name: JSONFeed
  property_count: 7
  slug: disputes-online-jsonfeed
- name: Odds
  property_count: 10
  slug: disputes-online-odds
jsonld:
- class_count: 8
  name: Disputes Online Context
  property_count: 54
  slug: disputes-online-context
layout: provider
modified: '2026-11-05'
name: Disputes.online
nav: Providers
network: true
overview: 'Disputes.online publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Categories API, Disputes API, and Feeds API. Tagged areas include Dispute, Community, Predictions, Sports, and Politics.


  The Disputes.online catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Disputes.online''s developer surface includes documentation, API reference, and 15 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Disputes.online API Rules
  rule_count: 48
  severity_counts:
    error: 44
    hint: 0
    info: 2
    warn: 2
  slug: disputes-online-rules
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 57.3
    developer_ergonomics: 16.7
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Disputes Online Domain Security
  slug: disputes-online-domain-security
  summary_line: TLSv1.3 · DMARC
slug: disputes-online
tags:
- Dispute
- Community
- Predictions
- Sports
- Politics
website: https://disputes.online/
---
