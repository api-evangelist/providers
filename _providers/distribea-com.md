---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Distribea Com Agentic Access
  operation_count: 9
  slug: distribea-com-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- baseURL: https://distribea.com
  baseurl_source: declared
  description: The account behind an API key.
  name: Distribea Account API
  slug: distribea-com-account-api
- baseURL: https://distribea.com
  baseurl_source: declared
  description: Royalty-free music, sound effects, footage and images. Public.
  name: Distribea Catalog API
  slug: distribea-com-catalog-api
- baseURL: https://distribea.com
  baseurl_source: declared
  description: Generate images, video, music and voice, paid in credits.
  name: Distribea Generation API
  slug: distribea-com-generation-api
- baseURL: https://distribea.com
  baseurl_source: declared
  description: Generation models, settings and prices. Public.
  name: Distribea Models API
  slug: distribea-com-models-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/distribea-com/agentic-access/distribea-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/distribea-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/distribea-com/plans/distribea-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/distribea-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/distribea-com/rules/distribea-com-rules.yml
  title: ''
  type: Spectral
  url: rules/distribea-com-rules.yml
- group: design
  href: https://artifacts.apis.io/distribea-com/json-ld/distribea-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/distribea-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/distribea-com/vocabulary/distribea-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/distribea-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/distribea-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/distribea-com/data-model/distribea-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/distribea-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/distribea-com/security/distribea-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/distribea-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/distribea-com/errors/distribea-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/distribea-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/distribea-com/conformance/distribea-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/distribea-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/distribea-com/llms/distribea-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/distribea-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/distribea-com/well-known/distribea-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/distribea-com-security.txt
- group: agent
  href: https://artifacts.apis.io/distribea-com/well-known/distribea-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/distribea-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/distribea-com/hosts/distribea-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/distribea-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/distribea-com/vendors/distribea-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/distribea-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://distribea.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://distribea.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://distribea.com/pricing
- group: start
  title: ''
  type: Login
  url: https://distribea.com/auth/sign-in
- group: company
  title: ''
  type: Blog
  url: https://distribea.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://distribea.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/distribea-com/authentication/distribea-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/distribea-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/distribea-com/security/distribea-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/distribea-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/distribea-com/security/distribea-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/distribea-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://distribea.com/
created: '2026-11-05'
description: Distribua is an AI‑powered video creation platform that lets creators turn ideas into finished videos. It offers motion‑control AI to replace people in clips, a royalty‑free library of music, sound effects and stock footage, and subscription plans starting at €19.99 per month. The service aims to simplify video production for marketers, influencers and small businesses.
image: https://distribea.com/og/home-motion-control.jpg
json_schemas:
- name: ApiIndex
  property_count: 8
  slug: distribea-com-api-index
- name: CatalogItem
  property_count: 12
  slug: distribea-com-catalog-item
- name: GenerateImageRequest
  property_count: 9
  slug: distribea-com-generate-image-request
- name: GenerateVideoRequest
  property_count: 7
  slug: distribea-com-generate-video-request
- name: GenerateVoiceRequest
  property_count: 5
  slug: distribea-com-generate-voice-request
- name: ModelsResponse
  property_count: 0
  slug: distribea-com-models-response
jsonld:
- class_count: 18
  name: Distribea Com Context
  property_count: 74
  slug: distribea-com-context
layout: provider
modified: '2026-11-05'
name: Distribea
nav: Providers
network: true
overview: 'Distribea publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Catalog API, Generation API, and 1 more. Tagged areas include Artificial Intelligence, Video, Media, Software-as-a-Service, and Platform.


  The Distribea catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Distribea''s developer surface includes pricing, engineering blog, API reference, authentication, and 21 more developer resources.'
plans:
- name: Distribea Com Plans Pricing
  plan_count: 4
  slug: distribea-com-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 106
  extends:
  - spectral:oas
  name: Distribea API Rules
  rule_count: 65
  severity_counts:
    error: 61
    hint: 0
    info: 1
    warn: 3
  slug: distribea-com-rules
score:
  band: developing
  composite: 49.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 67.9
    developer_ergonomics: 23.2
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Distribea Com Authentication
  slug: distribea-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Distribea Com Domain Security
  slug: distribea-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Distribea Com Vulnerability Disclosure
  slug: distribea-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: distribea-com-generate-media
  slug: distribea-com-generate-media
slug: distribea-com
tags:
- Artificial Intelligence
- Video
- Media
- Software-as-a-Service
- Platform
website: https://distribea.com/
---
