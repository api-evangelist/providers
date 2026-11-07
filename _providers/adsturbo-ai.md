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
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 1
  name: Adsturbo Ai Agentic Access
  operation_count: 34
  slug: adsturbo-ai-agentic-access
  summary_line: 34 operations · 29 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://adsturbo.ai/klian/novartapi
  baseurl_source: declared
  description: AdClone video recreation
  name: AdsTurbo Ad Clone API
  slug: adsturbo-ai-adclone-api
- baseURL: https://adsturbo.ai/klian/novartapi
  baseurl_source: declared
  description: AdClone video recreation (v2beta, editable draft flow)
  name: AdsTurbo AdClone (v2beta) API
  slug: adsturbo-ai-adclone-v2beta-api
- baseURL: https://adsturbo.ai/klian/novartapi
  baseurl_source: declared
  description: System actor workflows
  name: AdsTurbo AI Actor API
  slug: adsturbo-ai-aiactor-api
- baseURL: https://adsturbo.ai/klian/novartapi
  baseurl_source: declared
  description: Image creation and editing
  name: AdsTurbo Image API
  slug: adsturbo-ai-image-api
- baseURL: https://adsturbo.ai/klian/novartapi
  baseurl_source: declared
  description: Image tools (v2beta)
  name: AdsTurbo Image (v2beta) API
  slug: adsturbo-ai-image-v2beta-api
- baseURL: https://adsturbo.ai/klian/novartapi
  baseurl_source: declared
  description: Custom Persona workflows
  name: AdsTurbo Persona API
  slug: adsturbo-ai-persona-api
- baseURL: https://adsturbo.ai/klian/novartapi
  baseurl_source: declared
  description: Video generation and editing tools
  name: AdsTurbo Video API
  slug: adsturbo-ai-video-api
- baseURL: https://adsturbo.ai/klian/novartapi
  baseurl_source: declared
  description: Video tools (v2beta)
  name: AdsTurbo Video (v2beta) API
  slug: adsturbo-ai-video-v2beta-api
- baseURL: https://adsturbo.ai/klian/novartapi
  baseurl_source: declared
  description: Async task status
  name: AdsTurbo Work API
  slug: adsturbo-ai-work-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/adsturbo-ai/agentic-access/adsturbo-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adsturbo-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/adsturbo-ai/plans/adsturbo-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adsturbo-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/adsturbo-ai/rules/adsturbo-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/adsturbo-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/adsturbo-ai/json-ld/adsturbo-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adsturbo-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/adsturbo-ai/vocabulary/adsturbo-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/adsturbo-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/adsturbo-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/adsturbo-ai/data-model/adsturbo-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adsturbo-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/adsturbo-ai/conventions/adsturbo-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/adsturbo-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/adsturbo-ai/conventions/adsturbo-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adsturbo-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/adsturbo-ai/authentication/adsturbo-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adsturbo-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/adsturbo-ai/conformance/adsturbo-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adsturbo-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adsturbo-ai/llms/adsturbo-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adsturbo-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/adsturbo-ai/well-known/adsturbo-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adsturbo-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/adsturbo-ai/hosts/adsturbo-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adsturbo-ai-hosts.yml
- group: build
  href: https://artifacts.apis.io/adsturbo-ai/packages/adsturbo-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/adsturbo-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/adsturbo-ai/packages/adsturbo-ai-packages.yml
  title: ''
  type: Packages
  url: packages/adsturbo-ai-packages.yml
- group: docs
  title: ''
  type: APIReference
  url: https://doc.adsturbo.ai/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdsTurbo
- group: auth
  href: https://artifacts.apis.io/adsturbo-ai/security/adsturbo-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adsturbo-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adsturbo.ai/
- group: company
  title: ''
  type: Blog
  url: https://adsturbo.ai/blog
- group: docs
  title: ''
  type: Documentation
  url: https://adsturbo.ai/open-api
- group: commercial
  title: ''
  type: Pricing
  url: https://adsturbo.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adsturbo.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adsturbo.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://adsturbo.ai/contact
created: '2026-10-31'
description: AdsTurbo is an AI‑powered video ad generation platform that enables businesses to create high‑converting UGC ads, perform face‑swap, lip‑sync, and multilingual video translation in minutes. The service offers image generation, persona creation, ad cloning, and a suite of video editing tools, all accessible via a REST API. It supports batch processing, async job tracking, and webhook callbacks, targeting e‑commerce brands, agencies, and growth teams seeking scalable creative production.
image: https://adsturbo.ai/og-image.png
json_schemas:
- name: ImageCreateBody
  property_count: 9
  slug: adsturbo-ai-image-create-body
- name: OpenAdCloneCreateBody
  property_count: 6
  slug: adsturbo-ai-open-ad-clone-create-body
- name: OpenAiActorListBody
  property_count: 10
  slug: adsturbo-ai-open-ai-actor-list-body
- name: OpenImageEcommerceBody
  property_count: 10
  slug: adsturbo-ai-open-image-ecommerce-body
- name: OpenVideoExtendBody
  property_count: 9
  slug: adsturbo-ai-open-video-extend-body
- name: OpenVideoGenerateBody
  property_count: 12
  slug: adsturbo-ai-open-video-generate-body
jsonld:
- class_count: 74
  name: Adsturbo Ai Context
  property_count: 152
  slug: adsturbo-ai-context
layout: provider
modified: '2026-10-31'
name: AdsTurbo
nav: Providers
network: true
overview: 'AdsTurbo publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ad Clone API, AdClone (v2beta) API, AI Actor API, and 6 more. Tagged areas include Artificial Intelligence, Video Ads, E-Commerce, Marketing, and Automation.


  The AdsTurbo catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AdsTurbo''s developer surface includes authentication, API reference, engineering blog, documentation, pricing, support, and 20 more developer resources.'
plans:
- name: Adsturbo Ai Plans Pricing
  plan_count: 4
  slug: adsturbo-ai-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Adsturbo Ai Rate Limits
  slug: adsturbo-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: AdsTurbo API Rules
  rule_count: 14
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 0
  slug: adsturbo-ai-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.0
    catalog_earned_first_party: 12.0
    catalog_gap: 41.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.5
  facets:
    access_clarity: 47.4
    contract_governance: 19.7
    contract_quality: 60.7
    developer_ergonomics: 37.4
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 48.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Adsturbo Ai Authentication
  slug: adsturbo-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adsturbo Ai Domain Security
  slug: adsturbo-ai-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
skill_count: 2
skills:
- name: ai-actor-list
  slug: adsturbo-ai-ai-actor-list
- name: image-create
  slug: adsturbo-ai-image-create
slug: adsturbo-ai
tags:
- Artificial Intelligence
- Video Ads
- E-Commerce
- Marketing
- Automation
website: https://adsturbo.ai/
---
