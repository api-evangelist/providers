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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Ex Human Agentic Access
  operation_count: 12
  slug: ex-human-agentic-access
  summary_line: 12 operations · 11 acting
api_count: 1
apis:
- baseURL: https://api.exh.ai
  baseurl_source: declared
  description: The animations API from Ex-Human — 6 operation(s) for animations.
  name: Ex-Human animations API
  slug: ex-human-animations-api
- baseURL: https://api.exh.ai
  baseurl_source: declared
  description: The chatbot API from Ex-Human — 3 operation(s) for chatbot.
  name: Ex-Human chatbot API
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
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  title: ''
  type: Overlay
  url: overlays/ex-human-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ex-human-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ex-human-agentic-access.yml
- group: auth
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
  title: ''
  type: ErrorCatalog
  url: errors/ex-human-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ex-human-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ex-human-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ex-human-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ex-human-data-model.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/ex-human-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ex-human-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/ex-human-changelog.yml
- group: agent
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
overview: 'Ex-Human publishes 4 APIs on the [APIs.io](https://apis.io/) network, including animations API, chatbot API, Image Generation API, and 1 more. Tagged areas include Company, Artificial Intelligence, Conversational AI, AI Companions, and Generative AI.


  Ex-Human''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, pricing, signup flow, and 18 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 34.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 53.6
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 34.3
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ex-human/refs/heads/main/screenshots/ex-human-2026-07-25T213827.png
security:
- kind: authentication
  name: Ex Human Authentication
  slug: ex-human-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ex Human Domain Security
  slug: ex-human-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ex-human
tags:
- Company
- Artificial Intelligence
- Conversational AI
- AI Companions
- Generative AI
- Text-to-Speech
- Image-Generation
- Video Generation
- Avatars
- Multi-Modal
website: https://docs.exh.ai/
---
