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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Backend API documented at BitClout developer docs.
  name: BitClout API
  slug: bitclout-api
- description: 'BitClout (DeSo) API as documented publicly: 60 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: BitClout (DeSo) API
  slug: bitclout-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/bitclout-com/rules/bitclout-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bitclout-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bitclout-com/json-ld/bitclout-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bitclout-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bitclout-com/vocabulary/bitclout-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bitclout-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bitclout-com/data-model/bitclout-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bitclout-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/bitclout-com/conformance/bitclout-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bitclout-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bitclout-com/llms/bitclout-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bitclout-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bitclout-com/well-known/bitclout-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bitclout-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bitclout-com/hosts/bitclout-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bitclout-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/bitclout-com/vendors/bitclout-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bitclout-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.bitclout.com/faq/privacy-and-security
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bitclout.com/code/dev-setup
- group: auth
  href: https://artifacts.apis.io/bitclout-com/security/bitclout-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bitclout-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bitclout.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bitclout.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://bitclout.com/developers
coverage:
  checked: '2026-10-30'
  detail: Documentation provides markdown API reference but no OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 404
    url: https://api.bitclout.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: BitClout (DeSo) is a decentralized social media platform built on the DeSo blockchain. It enables creators to monetize their content directly through creator coins and NFTs, offering a user-owned social network where token economics drive engagement and value distribution.
image: https://bitclout.com/assets/bitclout/camelcase_logo_og.jpg
json_schemas:
- name: PostApiV0BuyOrSellCreatorCoinRequest
  property_count: 9
  slug: bitclout-com-post-api-v0-buy-or-sell-creator-coin-request
- name: PostApiV0GetAppStateResponse
  property_count: 13
  slug: bitclout-com-post-api-v0-get-app-state-response
- name: PostApiV0GetProfilesRequest
  property_count: 10
  slug: bitclout-com-post-api-v0-get-profiles-request
- name: PostApiV0SendDiamondsRequest
  property_count: 5
  slug: bitclout-com-post-api-v0-send-diamonds-request
- name: PostApiV0TransferCreatorCoinRequest
  property_count: 5
  slug: bitclout-com-post-api-v0-transfer-creator-coin-request
- name: PostApiV0UpdateProfileRequest
  property_count: 9
  slug: bitclout-com-post-api-v0-update-profile-request
jsonld:
- class_count: 42
  name: Bitclout Com Context
  property_count: 103
  slug: bitclout-com-context
layout: provider
modified: '2026-10-28'
name: BitClout (DeSo)
nav: Providers
network: true
overview: 'BitClout (DeSo) is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Social Media, Decentralized, Cryptocurrency, and Creator Economy.


  The BitClout (DeSo) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BitClout (DeSo)''s developer surface includes getting-started guide, documentation, and 13 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 71
  extends:
  - spectral:oas
  name: BitClout (DeSo) API Rules
  rule_count: 30
  severity_counts:
    error: 28
    hint: 0
    info: 1
    warn: 1
  slug: bitclout-com-rules
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 25.2
    developer_ergonomics: 15.5
    discoverability: 64.3
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.3
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
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bitclout-com/bitclout-com-2026-11-03T121800.png
security:
- kind: domain-security
  name: Bitclout Com Domain Security
  slug: bitclout-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: bitclout-com
tags:
- Blockchain
- Social Media
- Decentralized
- Cryptocurrency
- Creator Economy
website: https://bitclout.com/
---
