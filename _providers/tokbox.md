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
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'TokBox API as documented publicly: 43 operations. Contract generated from the documentation by API Evangelist (2026-10-25); not the provider''s own document.'
  name: TokBox API
  slug: tokbox-api
artifact_total: 11
asyncapis:
- description: ''
  name: Tokbox Webhooks
  slug: tokbox-webhooks
common:
- group: operate
  title: ''
  type: StatusPage
  url: https://vonageapi.statuspage.io/
- group: start
  title: ''
  type: SignUp
  url: https://tokbox.com/account/user/signup
- group: design
  href: https://artifacts.apis.io/tokbox/rules/tokbox-rules.yml
  title: ''
  type: Spectral
  url: rules/tokbox-rules.yml
- group: design
  href: https://artifacts.apis.io/tokbox/json-ld/tokbox-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tokbox-context.jsonld
- group: design
  href: https://artifacts.apis.io/tokbox/vocabulary/tokbox-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tokbox-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tokbox/asyncapi/tokbox-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/tokbox-webhooks.yml
- group: design
  href: https://artifacts.apis.io/tokbox/data-model/tokbox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tokbox-data-model.yml
- group: operate
  href: https://artifacts.apis.io/tokbox/changelog/tokbox-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tokbox-changelog.yml
- group: design
  href: https://artifacts.apis.io/tokbox/conformance/tokbox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tokbox-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tokbox/well-known/tokbox-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tokbox-well-known.yml
- group: other
  href: https://artifacts.apis.io/tokbox/hosts/tokbox-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tokbox-hosts.yml
- group: other
  href: https://artifacts.apis.io/tokbox/vendors/tokbox-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tokbox-vendors.yml
- group: build
  href: https://artifacts.apis.io/tokbox/packages/tokbox-packages.yml
  title: ''
  type: SDKs
  url: packages/tokbox-packages.yml
- group: build
  href: https://artifacts.apis.io/tokbox/packages/tokbox-packages.yml
  title: ''
  type: Packages
  url: packages/tokbox-packages.yml
- group: auth
  href: https://artifacts.apis.io/tokbox/security/tokbox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tokbox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tokbox.com/developer/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tokbox.com/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://tokbox.com/developer/
- group: docs
  title: ''
  type: APIReference
  url: https://tokbox.com/developer/rest/
- group: start
  title: ''
  type: GettingStarted
  url: https://tokbox.com/developer/get-started-options/
- group: operate
  title: ''
  type: Support
  url: https://tokbox.com/developer/tools/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/opentok
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vonage.com/communications-apis/video/pricing/
created: '2026-10-25'
description: TokBox, now part of Vonage, provides the Video API (formerly OpenTok) enabling developers to embed real‑time video, voice, and messaging into web and mobile applications using WebRTC. The platform offers SDKs for JavaScript, iOS, Android, .NET, Java, Node.js, PHP, Python, Ruby and more, along with REST APIs, analytics, archiving, and live streaming capabilities. TokBox serves enterprises and developers seeking scalable, low‑latency video communication solutions across browsers and devices.
json_schemas:
- name: GetGraphqlResponse
  property_count: 1
  slug: tokbox-get-graphql-response
- name: GetV2ProjectLtApikeyGtRenderLtResponse
  property_count: 2
  slug: tokbox-get-v2-project-lt-apikey-gt-render-lt-response
- name: PostV2ProjectApiKeyArchiveIdStopResponse
  property_count: 17
  slug: tokbox-post-v2-project-api-key-archive-id-stop-response
- name: PostV2ProjectApiKeySessionSessionIdMuteResponse
  property_count: 4
  slug: tokbox-post-v2-project-api-key-session-session-id-mute-response
- name: PostV2ProjectApikeyBroadcastResponse
  property_count: 7
  slug: tokbox-post-v2-project-apikey-broadcast-response
- name: PostV2ProjectLtApikeyGtRenderResponse
  property_count: 11
  slug: tokbox-post-v2-project-lt-apikey-gt-render-response
jsonld:
- class_count: 18
  name: Tokbox Context
  property_count: 33
  slug: tokbox-context
layout: provider
modified: '2026-10-25'
name: TokBox
nav: Providers
network: true
overview: 'TokBox is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video, WebRTC, Real-Time Communication, SDK, and Vonage.


  The TokBox catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  TokBox''s developer surface includes signup flow, changelog, documentation, API reference, getting-started guide, support, pricing, and 16 more developer resources.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: TokBox API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: tokbox-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 18.4
    contract_governance: 22.0
    contract_quality: 35.0
    developer_ergonomics: 28.6
    discoverability: 53.6
    operational_transparency: 52.6
  previous_composite: 32.4
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
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tokbox/tokbox-2026-11-03T144931.png
security:
- kind: domain-security
  name: Tokbox Domain Security
  slug: tokbox-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: tokbox
tags:
- Video
- WebRTC
- Real-Time Communication
- SDK
- Vonage
website: https://tokbox.com/developer/
---
