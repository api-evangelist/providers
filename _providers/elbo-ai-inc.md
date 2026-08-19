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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 57.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Elbo Ai Inc Agentic Access
  operation_count: 7
  slug: elbo-ai-inc-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 5
apis:
- description: The Audio Uploads API from ELBO AI, INC — 1 operation(s) for audio uploads.
  name: ELBO AI, INC Audio Uploads API
  slug: elbo-ai-inc-audio-uploads-api
- description: The Text to Speech API from ELBO AI, INC — 1 operation(s) for text to speech.
  name: ELBO AI, INC Text to Speech API
  slug: elbo-ai-inc-text-to-speech-api
- description: The Usage API from ELBO AI, INC — 1 operation(s) for usage.
  name: ELBO AI, INC Usage API
  slug: elbo-ai-inc-usage-api
- description: The Videos API from ELBO AI, INC — 3 operation(s) for videos.
  name: ELBO AI, INC Videos API
  slug: elbo-ai-inc-videos-api
- description: The Voices API from ELBO AI, INC — 1 operation(s) for voices.
  name: ELBO AI, INC Voices API
  slug: elbo-ai-inc-voices-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Puppetry Developer API Beta Audio Uploads API
  slug: open-elbo-ai-inc-audio-uploads-api
- collection_type: open
  name: Puppetry Developer API Beta Audio Uploads Text to Speech API
  slug: open-elbo-ai-inc-text-to-speech-api
- collection_type: open
  name: Puppetry Developer API Beta Audio Uploads Usage API
  slug: open-elbo-ai-inc-usage-api
- collection_type: open
  name: Puppetry Developer API Beta Audio Uploads Videos API
  slug: open-elbo-ai-inc-videos-api
- collection_type: open
  name: Puppetry Developer API Beta Audio Uploads Voices API
  slug: open-elbo-ai-inc-voices-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/elbo-ai-inc-puppetry-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://puppetry.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.puppetry.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://www.puppetry.com/for-agents
- group: docs
  title: ''
  type: APIReference
  url: https://www.puppetry.com/developer
- group: start
  title: ''
  type: GettingStarted
  url: https://www.puppetry.com/developer
- group: company
  title: ''
  type: Blog
  url: https://www.puppetry.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.puppetry.com/changelog
- group: operate
  title: ''
  type: Support
  url: https://www.puppetry.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://www.puppetry.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.puppetry.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://www.puppetry.com/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.puppetry.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.puppetry.com/privacy
- group: build
  title: ''
  type: SDKs
  url: packages/elbo-ai-inc-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/elbo-ai-inc-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/elbo-ai-inc-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elbo-ai-inc-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/elbo-ai-inc-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elbo-ai-inc-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elbo-ai-inc-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/elbo-ai-inc-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: conventions/elbo-ai-inc-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elbo-ai-inc-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elbo-ai-inc-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/elbo-ai-inc-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/elbo-ai-inc-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elbo-ai-inc-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/elbo-ai-inc-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Changelog
  url: changelog/elbo-ai-inc-changelog.yml
created: '2026-07-17'
description: 'ELBO AI, INC operates Puppetry (puppetry.com), an AI video-creation platform that turns any portrait photo into a realistic lip-synced talking-head video. Users upload an image, provide a script or audio, pick from 500+ AI voices across 65+ languages, and Puppetry renders a video in minutes — with voice cloning, AI Stories multi-scene storytelling, caption studio, and cartoon/object animation. Beyond the studio web and iOS apps and a Canva integration, Puppetry ships a Developer API beta (Studio plan) for agents and app integrations: a Puppetry Voice API (list voices + TTS), hosted audio uploads with signed URLs, and credit-backed text-to-video and audio-to-video jobs with idempotent creation and job-and-poll status. It publishes an OpenAPI 3.1 spec, an official TypeScript SDK, an MCP server, llms.txt, and an ai-plugin.json manifest. Founded by ex-Google/Microsoft/Apple/Amazon engineers; backed by 500 Global.'
image: https://www.puppetry.com/puppetry-logo.png
layout: provider
mcp_servers:
- description: ''
  name: elbo-ai-inc-mcp.yml
  slug: elbo-ai-inc-mcpyml
modified: '2026-07-19'
name: ELBO AI, INC
nav: Providers
network: true
overview: 'ELBO AI, INC publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Audio Uploads API, Text to Speech API, Usage API, and 2 more. Tagged areas include Company, Artificial Intelligence, Video, Text to Speech, and Voice.


  ELBO AI, INC''s developer surface includes documentation, API reference, getting-started guide, engineering blog, changelog, support, pricing, and 24 more developer resources.'
random_paper: 130
score:
  band: developing
  composite: 49.7
  delta: -0.7
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 61.3
    developer_ergonomics: 66.1
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 15.8
  previous_composite: 50.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elbo-ai-inc/refs/heads/main/screenshots/elbo-ai-inc-2026-07-25T213052.png
security:
- kind: authentication
  name: Elbo Ai Inc Authentication
  slug: elbo-ai-inc-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Elbo Ai Inc Domain Security
  slug: elbo-ai-inc-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: elbo-ai-inc
tags:
- Company
- Artificial Intelligence
- Video
- Text to Speech
- Voice
- Generative AI
- Avatars
- Content Creation
- Developer API
- MCP
website: https://puppetry.com
---
