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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Deepdub Agentic Access
  operation_count: 24
  slug: deepdub-agentic-access
  summary_line: 24 operations · 15 acting
api_count: 2
apis:
- description: The Dubbing API from Deepdub — 4 operation(s) for dubbing.
  name: Deepdub Dubbing API
  slug: deepdub-dubbing-api
- description: The Gender Detection API from Deepdub — 2 operation(s) for gender detection.
  name: Deepdub Gender Detection API
  slug: deepdub-gender-detection-api
- description: The Infrastructure API from Deepdub — 2 operation(s) for infrastructure.
  name: Deepdub Infrastructure API
  slug: deepdub-infrastructure-api
- description: The Issues API from Deepdub — 2 operation(s) for issues.
  name: Deepdub Issues API
  slug: deepdub-issues-api
- description: The TTS API from Deepdub — 1 operation(s) for tts.
  name: Deepdub TTS API
  slug: deepdub-tts-api
- description: The Usage API from Deepdub — 2 operation(s) for usage.
  name: Deepdub Usage API
  slug: deepdub-usage-api
- description: The Voice API from Deepdub — 2 operation(s) for voice.
  name: Deepdub Voice API
  slug: deepdub-voice-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Deepdub Dubbing API
  slug: open-deepdub-dubbing-api
- collection_type: open
  name: Deepdub Dubbing Gender Detection API
  slug: open-deepdub-gender-detection-api
- collection_type: open
  name: Deepdub Dubbing Infrastructure API
  slug: open-deepdub-infrastructure-api
- collection_type: open
  name: Deepdub Dubbing Issues API
  slug: open-deepdub-issues-api
- collection_type: open
  name: Deepdub Dubbing TTS API
  slug: open-deepdub-tts-api
- collection_type: open
  name: Deepdub Dubbing Usage API
  slug: open-deepdub-usage-api
- collection_type: open
  name: Deepdub Dubbing Voice API
  slug: open-deepdub-voice-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/deepdub-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://deepdub.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.deepdub.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deepdub.ai/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.deepdub.ai/api-reference/tts/generate-and-stream-tts-audio
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.deepdub.ai/quickstart
- group: auth
  title: ''
  type: Authentication
  url: authentication/deepdub-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://deepdub.ai/blog
- group: operate
  title: ''
  type: Support
  url: mailto:support@deepdub.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepdub-ai
- group: start
  title: ''
  type: SignUp
  url: https://app.deepdub.ai/signup
- group: start
  title: ''
  type: Login
  url: https://app.deepdub.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://deepdub.ai/demo
- group: commercial
  title: ''
  type: TermsOfService
  url: https://deepdub.ai/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://deepdub.ai/legal/privacy
- group: build
  title: ''
  type: Packages
  url: packages/deepdub-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/deepdub-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/deepdub-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deepdub-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/deepdub-llms.txt
- group: start
  title: ''
  type: Sandbox
  url: sandbox/deepdub-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deepdub-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/deepdub-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/deepdub-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/deepdub-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/deepdub-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/deepdub-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepdub-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/deepdub-well-known.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/deepdub-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/deepdub-managed-dub-overlay.yaml
created: '2026-07-17'
description: 'Deepdub is an AI dubbing, voice-cloning, and text-to-speech company that turns content into natural, emotionally adaptive speech across 100+ languages. Its platform powers media dubbing for studios such as Paramount, Netflix, and Prime Video, real-time AI voice agents (~125ms latency), video localization, live broadcast, and voice cloning. Deepdub exposes a developer platform: a REST Text-to-Speech API (restapi.deepdub.ai) covering TTS generation, a voice bank, gender detection, usage, and issue tracking; a Managed Dubbing API (dubbing.deepdub.app) for end-to-end video dubbing jobs; and a WebSocket streaming API for real-time audio. Authentication is via an x-api-key header, with Python and Node.js SDKs, published OpenAPI specs, and agent files (AGENTS.md, Cursor skill). Deepdub is backed by Insight Partners.'
image: https://deepdub.mintlify.app/mintlify-assets/_next/image?url=%2F_mintlify%2Fapi%2Fog%3Fdivision%3DGetting%2BStarted%26title%3DIntroduction%26logoLight%3Dhttps%253A%252F%252Fmintcdn.com%252Fdeepdub%252FYsh6dRbXX3wLTl5X%252Flogo%252Flogo128.png&w=1200&q=100
layout: provider
mcp_servers:
- description: ''
  name: Deepdub MCP Server
  slug: deepdub-mcp-server
modified: '2026-07-18'
name: Deepdub
nav: Providers
network: true
overview: 'Deepdub publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Dubbing API, Gender Detection API, Infrastructure API, and 4 more. Tagged areas include Company, Voice, Text-to-Speech, Dubbing, and Localization.


  Deepdub''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, signup flow, and 25 more developer resources.'
random_paper: 15
rate_limits:
- limit_count: 2
  name: Deepdub Rate Limits
  slug: deepdub-rate-limits
score:
  band: developing
  composite: 50.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 4.5
    contract_quality: 66.0
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 50.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deepdub/refs/heads/main/screenshots/deepdub-2026-07-25T211547.png
security:
- kind: authentication
  name: Deepdub Authentication
  slug: deepdub-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Deepdub Domain Security
  slug: deepdub-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: deepdub
tags:
- Company
- Voice
- Text-to-Speech
- Dubbing
- Localization
- Speech Synthesis
- Voice Cloning
- Media
- Artificial Intelligence
- Audio
website: https://deepdub.ai/
---
