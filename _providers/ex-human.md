---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Ex Human Agentic Access
  operation_count: 12
  slug: ex-human-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.exh.ai
  baseurl_source: declared
  description: The animations API from Ex-Human — 6 operation(s) for animations.
  name: Ex-Human Animations API
  slug: ex-human-animations-api
- baseURL: https://api.exh.ai
  baseurl_source: declared
  description: The chatbot API from Ex-Human — 3 operation(s) for chatbot.
  name: Ex-Human Chatbot API
  slug: ex-human-chatbot-api
- baseURL: https://api.exh.ai
  baseurl_source: declared
  description: The Image Generation API from Ex-Human — 2 operation(s) for image generation.
  name: Ex-Human Image Generation API
  slug: ex-human-image-generation-api
- baseURL: https://api.exh.ai
  baseurl_source: declared
  description: The Text to Speech API from Ex-Human — 1 operation(s) for text to speech.
  name: Ex-Human Text to Speech API
  slug: ex-human-text-to-speech-api
- baseURL: https://api.exh.ai
  baseurl_source: declared
  description: The admin API from Ex-Human — 6 operation(s) for admin.
  name: Ex-Human Admin API
  slug: ex-human-admin-api
- baseURL: https://api.exh.ai
  baseurl_source: declared
  description: The Metrics API from Ex-Human — 1 operation(s) for metrics.
  name: Ex-Human Metrics API
  slug: ex-human-metrics-api
artifact_total: 18
collections:
- collection_type: open
  name: Ex-Human animations API
  slug: open-ex-human-animations-api
- collection_type: open
  name: Ex-Human animations chatbot API
  slug: open-ex-human-chatbot-api
- collection_type: open
  name: Ex-Human animations Image Generation API
  slug: open-ex-human-image-generation-api
- collection_type: open
  name: Ex-Human animations Text to Speech API
  slug: open-ex-human-text-to-speech-api
common:
- group: commercial
  href: https://artifacts.apis.io/ex-human/plans/ex-human-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ex-human-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://www.exh.ai/
- group: other
  href: https://artifacts.apis.io/ex-human/overlays/ex-human-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ex-human-openapi-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/ex-human/security/ex-human-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ex-human-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/ex-human/agentic-access/ex-human-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ex-human-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/ex-human/authentication/ex-human-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ex-human-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.exh.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.exh.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.exh.ai/reference/get_response_chatbot_v3_response_post
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.exh.ai/reference/getting-started-with-your-api
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.exh.ai/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://exh.ai/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://admin.exh.ai/
- group: operate
  title: ''
  type: Support
  url: mailto:support@exh.ai
- group: company
  title: ''
  type: Blog
  url: https://exh.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.privacypolicies.com/live/6e088827-d8ce-4369-bb65-6b0bd4a23146
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.privacypolicies.com/live/a9dd0844-8a81-48dc-bdef-f022e0ef4d4e
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ex-human/
- group: design
  href: https://artifacts.apis.io/ex-human/errors/ex-human-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ex-human-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ex-human/conventions/ex-human-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ex-human-conventions.yml
- group: design
  href: https://artifacts.apis.io/ex-human/lifecycle/ex-human-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ex-human-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/ex-human/conformance/ex-human-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ex-human-conformance.yml
- group: design
  href: https://artifacts.apis.io/ex-human/data-model/ex-human-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ex-human-data-model.yml
- group: agent
  href: https://artifacts.apis.io/ex-human/mcp/ex-human-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ex-human-mcp.yml
- group: agent
  href: https://artifacts.apis.io/ex-human/llms/ex-human-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ex-human-llms.txt
- group: operate
  href: https://artifacts.apis.io/ex-human/changelog/ex-human-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ex-human-changelog.yml
- group: agent
  href: https://artifacts.apis.io/ex-human/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Ex-Human is a "Digital Human as a Service" platform that provides a single, unified API for building fully immersive, emotionally intelligent AI companions that communicate through text, voice, images, and video. Backed by a16z, the company lets developers design unique character personalities and generate multimodal responses at production scale. The Ex-Human API spans a multimodal chatbot (roleplay and realistic-chat models with long-term memory and smart replies), image generation (personalized gallery images and avatars via the persona-2 and supreme models), talking-head avatar animation (lip-sync from text or audio), image-to-video animation jobs, and text-to-speech. It is trusted by large consumer-technology companies to power AI companions, entertainment and gaming NPCs, dating experiences, AI twins, education tutors, and healthcare and therapy support at scale.
image: https://exh.ai/Union512.png?v=2
layout: provider
modified: '2026-07-19'
name: Ex-Human
nav: Providers
network: true
overview: 'Ex-Human publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Animations API, Chatbot API, Image Generation API, and 3 more. Tagged areas include Company, Artificial Intelligence, Conversational AI, AI Companion, and Generative AI.


  The Ex-Human catalog on APIs.io includes 1 Spectral governance ruleset.


  Ex-Human''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Ex Human Plans Pricing
  plan_count: 3
  slug: ex-human-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Ex-Human API Rules
  rule_count: 51
  severity_counts:
    error: 43
    hint: 0
    info: 3
    warn: 5
  slug: ex-human-rules
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 3.6
  facets:
    access_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 49.8
    developer_ergonomics: 47.0
    discoverability: 73.2
    operational_transparency: 15.8
  previous_composite: 40.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 54.5
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/ex-human/ex-human-2026-07-25T213827.png
security:
- kind: authentication
  name: Ex Human Authentication
  slug: ex-human-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ex Human Domain Security
  slug: ex-human-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Build a multimodal AI companion chat
  slug: ex-human-companion-chat
- name: Animate an image into video (create-then-poll)
  slug: ex-human-image-to-video
- name: Generate a talking-head avatar video
  slug: ex-human-talking-head-avatar
slug: ex-human
tags:
- Company
- Artificial Intelligence
- Conversational AI
- AI Companion
- Generative AI
- Text-to-Speech
- Image Generation
- Video Generation
- Avatars
- Multi-Modal
website: https://www.exh.ai/
---
