---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Provides real-time AI avatar streaming via WebRTC. Documentation at https://avacast.jp/docs/guide/api-keys.
  name: Avacast Avatar API
  slug: avacast-avatar-api
- description: 'avacast-jp API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: avacast-jp API
  slug: avacast-jp-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/avacast-jp/rules/avacast-jp-rules.yml
  title: ''
  type: Spectral
  url: rules/avacast-jp-rules.yml
- group: design
  href: https://artifacts.apis.io/avacast-jp/json-ld/avacast-jp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/avacast-jp-context.jsonld
- group: design
  href: https://artifacts.apis.io/avacast-jp/vocabulary/avacast-jp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avacast-jp-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/avacast-jp/data-model/avacast-jp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avacast-jp-data-model.yml
- group: auth
  href: https://artifacts.apis.io/avacast-jp/authentication/avacast-jp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/avacast-jp-authentication.yml
- group: design
  href: https://artifacts.apis.io/avacast-jp/conformance/avacast-jp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avacast-jp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/avacast-jp/llms/avacast-jp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avacast-jp-llms.txt
- group: agent
  href: https://artifacts.apis.io/avacast-jp/well-known/avacast-jp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avacast-jp-well-known.yml
- group: other
  href: https://artifacts.apis.io/avacast-jp/hosts/avacast-jp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avacast-jp-hosts.yml
- group: other
  href: https://artifacts.apis.io/avacast-jp/vendors/avacast-jp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avacast-jp-vendors.yml
- group: build
  href: https://artifacts.apis.io/avacast-jp/packages/avacast-jp-packages.yml
  title: ''
  type: SDKs
  url: packages/avacast-jp-packages.yml
- group: build
  href: https://artifacts.apis.io/avacast-jp/packages/avacast-jp-packages.yml
  title: ''
  type: Packages
  url: packages/avacast-jp-packages.yml
- group: auth
  href: https://artifacts.apis.io/avacast-jp/security/avacast-jp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avacast-jp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avacast.jp/
- group: docs
  title: ''
  type: Documentation
  url: https://avacast.jp/docs
- group: company
  title: ''
  type: Blog
  url: https://avacast.jp/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avacast.jp/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avacast.jp/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://avacast.jp/
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are HTML and no machine‑readable OpenAPI/AsyncAPI spec was found.
  evidence:
  - status: 404
    url: https://api.avacast.jp/openapi.json
  - status: 200
    url: https://avacast.jp/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: Avacast株式会社は、リアルタイムで会話するAIアバターAPIを提供する日本の企業です。テキストを送信すると、GPUで生成された映像と音声ストリームをWebRTCで配信し、ウェブアプリやデジタルサイネージ、スマートフォンアプリなど様々な環境に組み込むことができます。無料プランで月30分まで利用可能で、料金は文字数と秒数に基づき課金されます。
image: https://avacast.jp/opengraph-image.png
json_schemas:
- name: DeleteV1SessionsIdResponse
  property_count: 4
  slug: avacast-jp-delete-v1-sessions-id-response
- name: GetV1AvatarsResponse
  property_count: 1
  slug: avacast-jp-get-v1-avatars-response
- name: GetV1SessionsIdResponse
  property_count: 7
  slug: avacast-jp-get-v1-sessions-id-response
- name: PostV1ClientSessionsIdSpeakRequest
  property_count: 1
  slug: avacast-jp-post-v1-client-sessions-id-speak-request
- name: PostV1SessionsIdSpeakRequest
  property_count: 1
  slug: avacast-jp-post-v1-sessions-id-speak-request
- name: PostV1SessionsRequest
  property_count: 2
  slug: avacast-jp-post-v1-sessions-request
jsonld:
- class_count: 9
  name: Avacast Jp Context
  property_count: 14
  slug: avacast-jp-context
layout: provider
modified: '2026-10-30'
name: avacast-jp
nav: Providers
network: true
overview: 'avacast-jp is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Avatars, Real-Time, and Japan.


  The avacast-jp catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  avacast-jp''s developer surface includes authentication, documentation, engineering blog, pricing, and 15 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: avacast-jp API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: avacast-jp-rules
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 24.7
    developer_ergonomics: 25.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 27.3
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/avacast-jp/avacast-jp-2026-11-03T121412.png
security:
- kind: authentication
  name: Avacast Jp Authentication
  slug: avacast-jp-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Avacast Jp Domain Security
  slug: avacast-jp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: avacast-jp
tags:
- Company
- Artificial Intelligence
- Avatars
- Real-Time
- Japan
website: https://avacast.jp/
---
