---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.openkrill.app
  baseurl_source: declared
  description: 'openkrill-app API as documented publicly: 18 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: openkrill-app API
  slug: openkrill-app-api
artifact_total: 18
common:
- group: commercial
  href: https://artifacts.apis.io/openkrill-app/plans/openkrill-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/openkrill-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/openkrill-app/rules/openkrill-app-rules.yml
  title: ''
  type: Spectral
  url: rules/openkrill-app-rules.yml
- group: design
  href: https://artifacts.apis.io/openkrill-app/json-ld/openkrill-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openkrill-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/openkrill-app/vocabulary/openkrill-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openkrill-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/openkrill-app/data-model/openkrill-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openkrill-app-data-model.yml
- group: operate
  href: https://artifacts.apis.io/openkrill-app/changelog/openkrill-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/openkrill-app-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://tools.openkrill.app/contact
- group: design
  href: https://artifacts.apis.io/openkrill-app/conformance/openkrill-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openkrill-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/openkrill-app/llms/openkrill-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openkrill-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/openkrill-app/well-known/openkrill-app-tools-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/openkrill-app-tools-security.txt
- group: auth
  href: https://artifacts.apis.io/openkrill-app/well-known/openkrill-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/openkrill-app-security.txt
- group: agent
  href: https://artifacts.apis.io/openkrill-app/well-known/openkrill-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/openkrill-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/openkrill-app/hosts/openkrill-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openkrill-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/openkrill-app/vendors/openkrill-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openkrill-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tools.openkrill.app/terms
- group: operate
  title: ''
  type: Support
  url: https://tools.openkrill.app/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.openkrill.app/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tools.openkrill.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://tools.openkrill.app/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tools.openkrill.app/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://tools.openkrill.app/changelog
- group: company
  title: ''
  type: Blog
  url: https://tools.openkrill.app/blog
- group: docs
  title: ''
  type: Documentation
  url: https://docs.openkrill.app/
- group: auth
  href: https://artifacts.apis.io/openkrill-app/security/openkrill-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/openkrill-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/openkrill-app/security/openkrill-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openkrill-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openkrill.app/
created: '2026-10-29'
description: OpenKrill App provides a platform for managing and analyzing krill population data, offering APIs for data ingestion, retrieval, and visualization. The service targets marine biologists, environmental researchers, and conservation organizations, enabling them to integrate krill metrics into broader ecological models and dashboards. OpenKrill App emphasizes open data standards, robust authentication, and scalable cloud infrastructure to support large datasets and real-time analytics across global research initiatives.
image: https://tools.openkrill.app/og/home-54efed70.jpg
json_schemas:
- name: GetV1FeedbackTicketResponse
  property_count: 2
  slug: openkrill-app-get-v1-feedback-ticket-response
- name: PostDocsortSortRequest
  property_count: 3
  slug: openkrill-app-post-docsort-sort-request
- name: PostMirrorReadRequest
  property_count: 2
  slug: openkrill-app-post-mirror-read-request
- name: PostV1FeedbackRequest
  property_count: 3
  slug: openkrill-app-post-v1-feedback-request
- name: PostV1FeedbackResponse
  property_count: 1
  slug: openkrill-app-post-v1-feedback-response
- name: PostV2ActsOpenkrillXTwitterScraperRunSyncGetDatasetItemsRequ
  property_count: 2
  slug: openkrill-app-post-v2-acts-openkrill-xtwitter-scraper-run-sync-get-dataset-items-requ
jsonld:
- class_count: 6
  name: Openkrill App Context
  property_count: 13
  slug: openkrill-app-context
layout: provider
modified: '2026-10-29'
name: openkrill-app
nav: Providers
network: true
overview: 'openkrill-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MarineBiology, Data Analytics, EnvironmentalResearch, and Open Data.


  The openkrill-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  openkrill-app''s developer surface includes changelog, support, pricing, engineering blog, documentation, and 21 more developer resources.'
plans:
- name: Openkrill App Plans Pricing
  plan_count: 1
  slug: openkrill-app-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 4
  name: Openkrill App Rate Limits
  slug: openkrill-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: openkrill-app API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: openkrill-app-rules
scopes:
- name: Openkrill App Scopes
  scope_count: 0
  slug: openkrill-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.1
  coverage:
    artifact_dirs: 30
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 13.1
    discoverability: 73.2
    operational_transparency: 52.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/openkrill-app/openkrill-app-2026-11-03T140642.png
security:
- kind: authentication
  name: Openkrill App Authentication
  slug: openkrill-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Openkrill App Domain Security
  slug: openkrill-app-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Openkrill App Vulnerability Disclosure
  slug: openkrill-app-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: get-mcp
  slug: openkrill-app-get-mcp
- name: get-v1-tools-job-boards-run
  slug: openkrill-app-get-v1-tools-job-boards-run
- name: post-v2-acts-openkrill-x-twitter-scraper-run-sync-get-dataset-items
  slug: openkrill-app-post-v2-acts-openkrill-x-twitter-scraper-run-sync-get-dataset-items
slug: openkrill-app
tags:
- Company
- MarineBiology
- Data Analytics
- EnvironmentalResearch
- Open Data
website: https://openkrill.app/
---
