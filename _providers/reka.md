---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Reka Agentic Access
  operation_count: 13
  slug: reka-agentic-access
  summary_line: 13 operations · 9 acting
api_count: 1
apis:
- description: Chat completions with the Reka model family.
  name: Reka Chat API
  slug: reka-chat-api
- description: Generate and manage video clips.
  name: Reka Clips API
  slug: reka-clips-api
- description: List and describe available Reka models.
  name: Reka Models API
  slug: reka-models-api
- description: Question-answer interactions over video content.
  name: Reka QA API
  slug: reka-qa-api
- description: Research chat completions with web search.
  name: Reka Research API
  slug: reka-research-api
- description: Search across uploaded video content.
  name: Reka Search API
  slug: reka-search-api
- description: Speech transcription and translation.
  name: Reka Speech API
  slug: reka-speech-api
- description: Organize videos into named groups.
  name: Reka VideoGroups API
  slug: reka-videogroups-api
- description: Upload and manage videos for the Reka Vision platform.
  name: Reka Videos API
  slug: reka-videos-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Reka Chat API
  slug: open-reka-chat-api
- collection_type: open
  name: Reka Chat Clips API
  slug: open-reka-clips-api
- collection_type: open
  name: Reka Chat Models API
  slug: open-reka-models-api
- collection_type: open
  name: Reka Chat QA API
  slug: open-reka-qa-api
- collection_type: open
  name: Reka Chat Research API
  slug: open-reka-research-api
- collection_type: open
  name: Reka Chat Search API
  slug: open-reka-search-api
- collection_type: open
  name: Reka Chat Speech API
  slug: open-reka-speech-api
- collection_type: open
  name: Reka Chat VideoGroups API
  slug: open-reka-videogroups-api
- collection_type: open
  name: Reka Chat Videos API
  slug: open-reka-videos-api
- collection_type: open
  name: Reka API
  slug: open-reka
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reka-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/reka-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reka-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/reka-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://reka.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reka.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://platform.reka.ai
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.reka.ai/openapi.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/reka-ai
- group: other
  title: ''
  type: HuggingFace
  url: https://huggingface.co/RekaAI
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/rekaai
- group: company
  title: ''
  type: Blog
  url: https://reka.ai/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/reka-ai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/RekaAILabs
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.reka.ai/llms.txt
created: '2026-05-23'
description: Reka is a multimodal foundation model company building natively multimodal large language models capable of joint reasoning over text, image, video, and audio. The Reka model family spans Spark (1B) for embedded use cases, Edge (7B), Flash (21B), and Core (67B) for complex enterprise tasks. Reka exposes its hosted models through the Reka API at api.reka.ai with OpenAI-compatible chat completions, and also ships products including the Reka Vision Platform for enterprise perception, Reka Speech for audio understanding, and Reka Clip for creators. The platform supports flexible deployment across cloud, VPC, on-premises, and fully air-gapped environments, and the company maintains an active open-source presence on Hugging Face and GitHub including the Reka VibeEval benchmark.
finops:
- name: Reka Finops
  service_category: API
  slug: reka-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/reka.png
layout: provider
modified: '2026-05-23'
name: Reka
nav: Providers
network: true
overview: 'Reka publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Clips API, Models API, and 6 more. Tagged areas include Artificial Intelligence, Multimodal, Large Language Models, Vision, and Speech.


  Reka''s developer surface includes authentication, documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Reka Plans Pricing
  plan_count: 1
  slug: reka-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Reka Rate Limits
  slug: reka-rate-limits
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 11
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 54.4
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reka/refs/heads/main/screenshots/reka-2026-06-20T192942.png
security:
- kind: authentication
  name: Reka Authentication
  slug: reka-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Reka Domain Security
  slug: reka-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Reka Trust Center
  slug: reka-trust-center
  summary_line: SOC 2
slug: reka
tags:
- Artificial Intelligence
- Multimodal
- Large Language Models
- Vision
- Speech
- Foundation Models
- OpenAI-Compatible
- SDK
- Enterprise
- On-Premises
website: https://reka.ai
---
