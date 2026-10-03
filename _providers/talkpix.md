---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-03'
api_count: 6
apis:
- description: The Estimate API from TalkPix API — 1 operation(s) for estimate.
  name: TalkPix API Estimate API
  slug: talkpix-estimate-api
- description: The Me API from TalkPix API — 1 operation(s) for me.
  name: TalkPix API Me API
  slug: talkpix-me-api
- description: The TalkPix API API API from TalkPix API — 1 operation(s) for talkpix api api.
  name: TalkPix API TalkPix API API
  slug: talkpix-talkpix-api-api-api
- description: The Uploads API from TalkPix API — 1 operation(s) for uploads.
  name: TalkPix API Uploads API
  slug: talkpix-uploads-api
- description: The Videos API from TalkPix API — 4 operation(s) for videos.
  name: TalkPix API Videos API
  slug: talkpix-videos-api
- description: The Voices API from TalkPix API — 1 operation(s) for voices.
  name: TalkPix API Voices API
  slug: talkpix-voices-api
artifact_total: 16
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/talkpix/refs/heads/main/plans/talkpix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/talkpix-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talkpix/refs/heads/main/rules/talkpix-rules.yml
  title: ''
  type: Spectral
  url: rules/talkpix-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talkpix/refs/heads/main/json-ld/talkpix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/talkpix-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talkpix/refs/heads/main/vocabulary/talkpix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/talkpix-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talkpix/refs/heads/main/data-model/talkpix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/talkpix-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/talkpix/refs/heads/main/conformance/talkpix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/talkpix-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/talkpix/refs/heads/main/llms/talkpix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/talkpix-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/talkpix/refs/heads/main/hosts/talkpix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/talkpix-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/talkpix/refs/heads/main/vendors/talkpix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/talkpix-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/talkpix/refs/heads/main/packages/talkpix-packages.yml
  title: ''
  type: SDKs
  url: packages/talkpix-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/talkpix/refs/heads/main/packages/talkpix-packages.yml
  title: ''
  type: Packages
  url: packages/talkpix-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.talkpix.ai/press
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/talkpix/refs/heads/main/security/talkpix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/talkpix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.talkpix.ai
- group: docs
  title: ''
  type: Documentation
  url: https://www.talkpix.ai/developers
- group: company
  title: ''
  type: Blog
  url: https://www.talkpix.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.talkpix.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.talkpix.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.talkpix.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.talkpix.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://www.talkpix.ai/login
- group: start
  title: ''
  type: GettingStarted
  url: https://www.talkpix.ai/developers
created: '2026-10-02'
description: TalkPix provides AI-powered talking-photo video generation, turning a portrait and a script or audio into a lip‑synced MP4. Users can upload a photo, add voice or script, and receive a realistic talking video for social media, ads, or product showcases. The service offers multiple AI voices, language support, and credit‑based pricing, with an API for programmatic access.
image: https://www.talkpix.ai/opengraph-image
json_schemas:
- name: GetApiV1V1IdResponse
  property_count: 6
  slug: talkpix-get-api-v1-v1-id-response
- name: GetApiV1Videos6C1FResponse
  property_count: 10
  slug: talkpix-get-api-v1-videos6-c1-fresponse
- name: GetVideosIdResponse
  property_count: 10
  slug: talkpix-get-videos-id-response
- name: PostUploadsResponse
  property_count: 6
  slug: talkpix-post-uploads-response
- name: PostVideosRequest
  property_count: 13
  slug: talkpix-post-videos-request
- name: PostVideosResponse
  property_count: 10
  slug: talkpix-post-videos-response
jsonld:
- class_count: 14
  name: Talkpix Context
  property_count: 39
  slug: talkpix-context
layout: provider
modified: '2026-10-02'
name: TalkPix API
nav: Providers
network: true
overview: 'TalkPix API publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Estimate API, Me API, TalkPix API API, and 3 more. Tagged areas include Company, Artificial Intelligence, Video, Talking Photo, and Media.


  The TalkPix API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  TalkPix API''s developer surface includes documentation, engineering blog, pricing, support, signup flow, getting-started guide, and 16 more developer resources.'
plans:
- name: Talkpix Plans Pricing
  plan_count: 11
  slug: talkpix-plans-pricing
random_paper: 17
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: TalkPix API API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: talkpix-rules
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 72.0
    catalog_earned_first_party: 12.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 19.7
    contract_quality: 24.3
    developer_ergonomics: 35.7
    discoverability: 71.4
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 7
      marker_coverage: 100.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Talkpix Domain Security
  slug: talkpix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: talkpix
tags:
- Company
- Artificial Intelligence
- Video
- Talking Photo
- Media
website: https://www.talkpix.ai
---
