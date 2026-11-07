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
  band: agent-ready
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: RESTful API providing headless access to the BeyondWords platform for content items, voices, player settings, analytics and more.
  name: BeyondWords API
  slug: beyondwords-api-2
- baseURL: https://api.beyondwords.io
  baseurl_source: declared
  description: 'BeyondWords API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: BeyondWords API
  slug: beyondwords-api
artifact_total: 12
asyncapis:
- description: ''
  name: Beyondwords Webhooks
  slug: beyondwords-webhooks
common:
- group: design
  href: https://artifacts.apis.io/beyondwords/rules/beyondwords-rules.yml
  title: ''
  type: Spectral
  url: rules/beyondwords-rules.yml
- group: design
  href: https://artifacts.apis.io/beyondwords/json-ld/beyondwords-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/beyondwords-context.jsonld
- group: design
  href: https://artifacts.apis.io/beyondwords/vocabulary/beyondwords-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/beyondwords-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/beyondwords/asyncapi/beyondwords-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/beyondwords-webhooks.yml
- group: design
  href: https://artifacts.apis.io/beyondwords/data-model/beyondwords-data-model.yml
  title: ''
  type: DataModel
  url: data-model/beyondwords-data-model.yml
- group: operate
  href: https://artifacts.apis.io/beyondwords/changelog/beyondwords-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/beyondwords-changelog.yml
- group: operate
  href: https://artifacts.apis.io/beyondwords/lifecycle/beyondwords-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/beyondwords-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/beyondwords/lifecycle/beyondwords-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/beyondwords-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/beyondwords/conformance/beyondwords-conformance.yml
  title: ''
  type: Conformance
  url: conformance/beyondwords-conformance.yml
- group: agent
  href: https://artifacts.apis.io/beyondwords/llms/beyondwords-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beyondwords-llms.txt
- group: other
  href: https://artifacts.apis.io/beyondwords/a2a/beyondwords-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/beyondwords-a2a.yml
- group: agent
  href: https://artifacts.apis.io/beyondwords/well-known/beyondwords-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beyondwords-well-known.yml
- group: other
  href: https://artifacts.apis.io/beyondwords/hosts/beyondwords-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beyondwords-hosts.yml
- group: other
  href: https://artifacts.apis.io/beyondwords/vendors/beyondwords-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beyondwords-vendors.yml
- group: build
  href: https://artifacts.apis.io/beyondwords/packages/beyondwords-packages.yml
  title: ''
  type: SDKs
  url: packages/beyondwords-packages.yml
- group: build
  href: https://artifacts.apis.io/beyondwords/packages/beyondwords-packages.yml
  title: ''
  type: Packages
  url: packages/beyondwords-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.beyondwords.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.beyondwords.io/docs-and-guides/changelog
- group: auth
  href: https://artifacts.apis.io/beyondwords/security/beyondwords-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beyondwords-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beyondwords.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.beyondwords.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.beyondwords.io/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.beyondwords.io/docs-and-guides/getting-started/overview
- group: company
  title: ''
  type: Blog
  url: https://beyondwords.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://beyondwords.io/book-a-demo/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beyondwords.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beyondwords.io/privacy/
created: '2026-10-28'
description: BeyondWords provides an AI-powered audio CMS that enables publishers to convert text articles into natural‑sounding speech. Their platform offers voice cloning, content‑to‑audio transformation, analytics, and integration capabilities, helping media companies boost engagement and accessibility through automated audio publishing.
image: https://beyondwords.io/social.jpg
json_schemas:
- name: GetProjectsProjectidVideoSettingsResponse
  property_count: 40
  slug: beyondwords-get-projects-projectid-video-settings-response
- name: GetRulesIdResponse
  property_count: 13
  slug: beyondwords-get-rules-id-response
- name: GetRulesResponse
  property_count: 13
  slug: beyondwords-get-rules-response
- name: PutProjectsProjectidVideoSettingsRequest
  property_count: 40
  slug: beyondwords-put-projects-projectid-video-settings-request
- name: PutProjectsProjectidVideoSettingsResponse
  property_count: 40
  slug: beyondwords-put-projects-projectid-video-settings-response
- name: PutRulesIdResponse
  property_count: 13
  slug: beyondwords-put-rules-id-response
jsonld:
- class_count: 20
  name: Beyondwords Context
  property_count: 66
  slug: beyondwords-context
layout: provider
modified: '2026-10-28'
name: BeyondWords
nav: Providers
network: true
overview: 'BeyondWords is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Audio, CMS, Publishing, and Voice Cloning.


  The BeyondWords catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  BeyondWords'' developer surface includes changelog, documentation, API reference, getting-started guide, engineering blog, pricing, and 21 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: BeyondWords API Rules
  rule_count: 46
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 2
  slug: beyondwords-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 40.4
    developer_ergonomics: 22.6
    discoverability: 73.2
    operational_transparency: 31.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 40.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 18.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/beyondwords/beyondwords-2026-11-03T121706.png
security:
- kind: domain-security
  name: Beyondwords Domain Security
  slug: beyondwords-domain-security
  summary_line: TLSv1.3
slug: beyondwords
tags:
- Artificial Intelligence
- Audio
- CMS
- Publishing
- Voice Cloning
website: https://beyondwords.io/
---
