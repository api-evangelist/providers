---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-11-06'
api_count: 5
apis:
- description: Public API for Seedance2AI video generation platform
  name: Seedance2AI API
  slug: seedance2ai-api-2
- baseURL: https://www.seedance2ai.io/api/v1
  baseurl_source: declared
  description: The Downloads API from Seedance2AI (SixBryan LLC) — 1 operation(s) for downloads.
  name: Seedance2AI (SixBryan LLC) Downloads API
  slug: seedance2ai-downloads-api
- baseURL: https://www.seedance2ai.io/api/v1
  baseurl_source: declared
  description: The Image API from Seedance2AI (SixBryan LLC) — 1 operation(s) for image.
  name: Seedance2AI (SixBryan LLC) Image API
  slug: seedance2ai-image-api
- baseURL: https://www.seedance2ai.io/api/v1
  baseurl_source: declared
  description: The Tasks API from Seedance2AI (SixBryan LLC) — 1 operation(s) for tasks.
  name: Seedance2AI (SixBryan LLC) Tasks API
  slug: seedance2ai-tasks-api
- baseURL: https://www.seedance2ai.io/api/v1
  baseurl_source: declared
  description: The Video API from Seedance2AI (SixBryan LLC) — 1 operation(s) for video.
  name: Seedance2AI (SixBryan LLC) Video API
  slug: seedance2ai-video-api
artifact_total: 18
common:
- group: commercial
  href: https://artifacts.apis.io/seedance2ai/plans/seedance2ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/seedance2ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/seedance2ai/rules/seedance2ai-rules.yml
  title: ''
  type: Spectral
  url: rules/seedance2ai-rules.yml
- group: design
  href: https://artifacts.apis.io/seedance2ai/json-ld/seedance2ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/seedance2ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/seedance2ai/vocabulary/seedance2ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/seedance2ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/seedance2ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/seedance2ai/data-model/seedance2ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/seedance2ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/seedance2ai/conformance/seedance2ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/seedance2ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/seedance2ai/overlays/seedance2ai-openapi-generated-overlay.yml
  title: ''
  type: Overlay
  url: overlays/seedance2ai-openapi-generated-overlay.yml
- group: agent
  href: https://artifacts.apis.io/seedance2ai/llms/seedance2ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seedance2ai-llms.txt
- group: other
  href: https://artifacts.apis.io/seedance2ai/hosts/seedance2ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seedance2ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/seedance2ai/vendors/seedance2ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seedance2ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.seedance2ai.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.seedance2ai.io/privacy-policy
- group: auth
  href: https://artifacts.apis.io/seedance2ai/security/seedance2ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seedance2ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.seedance2ai.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.seedance2ai.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.seedance2ai.io/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.seedance2ai.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://www.seedance2ai.io/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://www.seedance2ai.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.seedance2ai.io/app/video/seedance2pro
- group: company
  title: ''
  type: Blog
  url: https://www.seedance2ai.io/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/seedance2ai
coverage:
  checked: '2026-09-28'
  detail: The provider's developer portal only offers a plain‑text API reference (llms-api.txt) without a machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL contract.
  evidence:
  - status: 200
    url: https://www.seedance2ai.io/llms-api.txt
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: Seedance2AI (SixBryan LLC) provides an AI-powered video generation platform that enables users to create cinematic videos from text, images, audio, and video inputs. Leveraging multi‑modal AI, the service offers precise reference control, watermark‑free outputs, and a suite of tools for marketers, educators, and storytellers. The platform includes a developer portal with API documentation, pricing plans, and integration guides, allowing developers to embed video generation capabilities into their applications.
finops:
- has_sources: true
  method: derived
  name: Seedance2Ai Finops
  primary_unit: subscription
  service_category: ''
  slug: seedance2ai-finops
  template: false
image: https://www.seedance2ai.io/favicon.ico
json_schemas:
- name: GetApiV1TasksIdResponse
  property_count: 12
  slug: seedance2ai-get-api-v1-tasks-id-response
- name: GetDownloadsSeedanceSkillMdResponse
  property_count: 1
  slug: seedance2ai-get-downloads-seedance-skill-md-response
- name: PostApiV1ImageImageidRequest
  property_count: 4
  slug: seedance2ai-post-api-v1-image-imageid-request
- name: PostApiV1ImageImageidResponse
  property_count: 5
  slug: seedance2ai-post-api-v1-image-imageid-response
- name: PostApiV1VideoVideoidRequest
  property_count: 6
  slug: seedance2ai-post-api-v1-video-videoid-request
- name: PostApiV1VideoVideoidResponse
  property_count: 6
  slug: seedance2ai-post-api-v1-video-videoid-response
jsonld:
- class_count: 6
  name: Seedance2Ai Context
  property_count: 19
  slug: seedance2ai-context
layout: provider
modified: '2026-09-27'
name: Seedance2AI (SixBryan LLC)
nav: Providers
network: true
overview: 'Seedance2AI (SixBryan LLC) is listed with 5 APIs on the [APIs.io](https://apis.io/) network, including Downloads API, Image API, Tasks API, and 2 more. Tagged areas include Company, Artificial Intelligence, Video Generation, Multi-Modal, and Developer Platform.


  The Seedance2AI (SixBryan LLC) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Seedance2AI (SixBryan LLC)''s developer surface includes documentation, getting-started guide, API reference, pricing, signup flow, engineering blog, and 17 more developer resources.'
plans:
- name: Seedance2Ai Plans Pricing
  plan_count: 15
  slug: seedance2ai-plans-pricing
- name: Seedance2Ai Price Estimates
  plan_count: 0
  slug: seedance2ai-price-estimates
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Seedance2AI (SixBryan LLC) API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: seedance2ai-rules
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 80.0
    catalog_earned_first_party: 12.0
    catalog_gap: 35.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 61.8
    contract_governance: 33.3
    contract_quality: 25.0
    developer_ergonomics: 26.7
    discoverability: 78.6
    operational_transparency: 2.6
  previous_composite: 44.2
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/seedance2ai/seedance2ai-2026-10-11T125641.png
security:
- kind: domain-security
  name: Seedance2Ai Domain Security
  slug: seedance2ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: post-video
  slug: seedance2ai-post_video
slug: seedance2ai
tags:
- Company
- Artificial Intelligence
- Video Generation
- Multi-Modal
- Developer Platform
website: https://www.seedance2ai.io/
---
