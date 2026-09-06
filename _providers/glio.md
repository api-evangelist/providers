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
    error_semantics: documented
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
  score: 23.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Glio Agentic Access
  operation_count: 6
  slug: glio-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.glio.io
  baseurl_source: declared
  description: Job creation and status management
  name: Glio Jobs API
  slug: glio-jobs-api
- baseURL: https://api.glio.io
  baseurl_source: declared
  description: Synchronous text generation endpoints
  name: Glio LLM API
  slug: glio-llm-api
arazzos:
- description: Create an AI media-generation job on Glio and poll until it completes, then read the result. Uses Glio's asynchronous job workflow.
  name: Glio - generate media and retrieve result
  slug: glio-generate-media
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Glio Jobs API
  slug: open-glio-jobs-api
- collection_type: open
  name: Glio Jobs LLM API
  slug: open-glio-llm-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/glio-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glio-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/glio-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/glio-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://glio.io/
- group: docs
  title: ''
  type: Documentation
  url: https://glio.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.glio.io/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://glio.io/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://glio.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://glio.io/app/
- group: operate
  title: ''
  type: Support
  url: https://glio.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://glio.io/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://glio.io/legal/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/glio-llms.txt
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/glio-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/glio-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/glio-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/glio-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/glio-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/glio-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/glio-generate-media.yml
created: '2026-07-17'
description: Glio is a unified API for AI media generation that provides a single interface to 90+ models across video, image, audio, and text from providers such as Kling, ByteDance Seedance, Google Veo and Imagen, OpenAI GPT Image, Suno, ElevenLabs, Runway, and Anthropic Claude. Developers create work via an asynchronous job-based workflow (create job, poll, get result), and also call OpenAI-compatible chat-completions and embeddings endpoints synchronously. Billing is pay-per-use in GL tokens (1 GL = $0.01 USD) with no subscriptions or minimums. Surfaced as an a16z portfolio company and enriched from Glio's public developer surface at glio.io / api.glio.io.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glio.png
layout: provider
modified: '2026-07-19'
name: Glio
nav: Providers
network: true
overview: 'Glio publishes 2 APIs on the [APIs.io](https://apis.io/) network: Jobs API and LLM API. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Media Generation, and Video Generation.


  Glio''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, support, and 15 more developer resources.'
random_paper: 7
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 54.8
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 42.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glio/refs/heads/main/screenshots/glio-2026-07-25T215909.png
security:
- kind: authentication
  name: Glio Authentication
  slug: glio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Glio Domain Security
  slug: glio-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: glio
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Media Generation
- Video Generation
- Image-Generation
- Audio Generation
- Text-to-Speech
- Large Language Models
- Generative AI
- API Aggregator
- Developer Tools
website: https://glio.io/
---
