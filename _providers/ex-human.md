---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Ex Human Agentic Access
  operation_count: 12
  slug: ex-human-agentic-access
  summary_line: 12 operations · 11 acting
api_count: 4
apis:
- description: The animations API from Ex-Human — 6 operation(s) for animations.
  name: Ex-Human animations API
  slug: ex-human-animations-api
- description: The chatbot API from Ex-Human — 3 operation(s) for chatbot.
  name: Ex-Human chatbot API
  slug: ex-human-chatbot-api
- description: The Image Generation API from Ex-Human — 2 operation(s) for image generation.
  name: Ex-Human Image Generation API
  slug: ex-human-image-generation-api
- description: The Text to Speech API from Ex-Human — 1 operation(s) for text to speech.
  name: Ex-Human Text to Speech API
  slug: ex-human-text-to-speech-api
artifact_total: 8
common:
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
  type: MCPServer
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
mcp_servers:
- description: ''
  name: ex-human-mcp.yml
  slug: ex-human-mcpyml
modified: '2026-07-19'
name: Ex-Human
nav: Providers
network: true
overview: 'Ex-Human publishes 4 APIs on the [APIs.io](https://apis.io/) network, including animations API, chatbot API, Image Generation API, and 1 more. Tagged areas include Company, Artificial Intelligence, Conversational AI, AI Companions, and Generative AI.


  Ex-Human''s developer surface includes authentication, documentation, API reference, getting-started guide, changelog, pricing, signup flow, and 17 more developer resources.'
random_paper: 65
score:
  band: developing
  composite: 45.4
  delta: -3.1
  facets:
    commercial_clarity: 44.7
    contract_quality: 54.9
    developer_ergonomics: 56.0
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 48.5
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
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- Text to Speech
- Image Generation
- Video Generation
- Avatars
- Multimodal
website: https://docs.exh.ai/
---
