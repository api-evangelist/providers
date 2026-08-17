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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Fixie Agentic Access
  operation_count: 114
  slug: fixie-agentic-access
  summary_line: 114 operations · 57 acting
api_count: 14
apis:
- description: The accounts API from Fixie — 9 operation(s) for accounts.
  name: Fixie accounts API
  slug: fixie-accounts-api
- description: The agents API from Fixie — 9 operation(s) for agents.
  name: Fixie agents API
  slug: fixie-agents-api
- description: The api_keys API from Fixie — 2 operation(s) for api_keys.
  name: Fixie api_keys API
  slug: fixie-api-keys-api
- description: The call_throttles API from Fixie — 2 operation(s) for call_throttles.
  name: Fixie call_throttles API
  slug: fixie-call-throttles-api
- description: The calls API from Fixie — 13 operation(s) for calls.
  name: Fixie calls API
  slug: fixie-calls-api
- description: The corpora API from Fixie — 8 operation(s) for corpora.
  name: Fixie corpora API
  slug: fixie-corpora-api
- description: The deleted_calls API from Fixie — 2 operation(s) for deleted_calls.
  name: Fixie deleted_calls API
  slug: fixie-deleted-calls-api
- description: The models API from Fixie — 1 operation(s) for models.
  name: Fixie models API
  slug: fixie-models-api
- description: The schema API from Fixie — 1 operation(s) for schema.
  name: Fixie schema API
  slug: fixie-schema-api
- description: The sip API from Fixie — 3 operation(s) for sip.
  name: Fixie sip API
  slug: fixie-sip-api
- description: The telephony_configs API from Fixie — 3 operation(s) for telephony_configs.
  name: Fixie telephony_configs API
  slug: fixie-telephony-configs-api
- description: The tools API from Fixie — 4 operation(s) for tools.
  name: Fixie tools API
  slug: fixie-tools-api
- description: The voices API from Fixie — 4 operation(s) for voices.
  name: Fixie voices API
  slug: fixie-voices-api
- description: The webhooks API from Fixie — 2 operation(s) for webhooks.
  name: Fixie webhooks API
  slug: fixie-webhooks-api
artifact_total: 35
asyncapis:
- description: ''
  name: Fixie Webhooks
  slug: fixie-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ultravox accounts API
  slug: open-fixie-accounts-api
- collection_type: open
  name: Ultravox accounts agents API
  slug: open-fixie-agents-api
- collection_type: open
  name: Ultravox accounts api_keys API
  slug: open-fixie-api-keys-api
- collection_type: open
  name: Ultravox accounts call_throttles API
  slug: open-fixie-call-throttles-api
- collection_type: open
  name: Ultravox accounts calls API
  slug: open-fixie-calls-api
- collection_type: open
  name: Ultravox accounts corpora API
  slug: open-fixie-corpora-api
- collection_type: open
  name: Ultravox accounts deleted_calls API
  slug: open-fixie-deleted-calls-api
- collection_type: open
  name: Ultravox accounts models API
  slug: open-fixie-models-api
- collection_type: open
  name: Ultravox accounts schema API
  slug: open-fixie-schema-api
- collection_type: open
  name: Ultravox accounts sip API
  slug: open-fixie-sip-api
- collection_type: open
  name: Ultravox accounts telephony_configs API
  slug: open-fixie-telephony-configs-api
- collection_type: open
  name: Ultravox accounts tools API
  slug: open-fixie-tools-api
- collection_type: open
  name: Ultravox accounts voices API
  slug: open-fixie-voices-api
- collection_type: open
  name: Ultravox accounts webhooks API
  slug: open-fixie-webhooks-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fixie-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fixie-ultravox-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fixie-domain-security.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/fixie-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/fixie-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/fixie-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fixie-changelog.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fixie-llms.txt
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ultravox.ai
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.ultravox.ai/changelog/deprecation
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fixie-webhooks.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ultravox.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ultravox.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ultravox.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ultravox.ai/gettingstarted/quickstart/agent-console
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fixie-ai
- group: company
  title: ''
  type: Blog
  url: https://ultravox.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://ultravox.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.ultravox.ai
- group: start
  title: ''
  type: Login
  url: https://app.ultravox.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ultravox.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ultravox.ai/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@ultravox.ai
- group: company
  title: ''
  type: Website
  url: https://ultravox.ai/
created: '2026-07-17'
description: Fixie is the company behind Ultravox Realtime, a speech-native voice AI platform for building natural, low-latency conversational voice agents. Rather than transcribing speech to text first, Ultravox processes audio directly to preserve tone, cadence, and pitch while cutting latency. The Ultravox Realtime REST API (api.ultravox.ai) lets developers create reusable agents, start and manage calls, define custom and built-in tools, clone and manage voices, build RAG corpora, wire telephony (Twilio, Telnyx, Plivo, SIP), and subscribe to call-lifecycle webhooks. Client SDKs ship for JavaScript, Python, Flutter/Dart, React Native, Kotlin/Android, and Swift/iOS. Fixie was backed by Redpoint Ventures; fixie.ai now redirects to ultravox.ai and its open models are published under the fixie-ai organization on Hugging Face.
image: https://raw.githubusercontent.com/api-evangelist/fixie/refs/heads/main/openapi/fixie-ultravox-openapi-original.yml
layout: provider
mcp_servers:
- description: ''
  name: fixie-mcp.yml
  slug: fixie-mcpyml
modified: '2026-07-19'
name: Fixie
nav: Providers
network: true
overview: 'Fixie publishes 14 APIs on the [APIs.io](https://apis.io/) network, including accounts API, agents API, api_keys API, and 11 more. Tagged areas include Company, Voice AI, Conversational AI, Real-time, and Speech.


  The Fixie catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fixie''s developer surface includes changelog, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 18 more developer resources.'
random_paper: 86
score:
  band: developing
  composite: 51.1
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 55.5
    developer_ergonomics: 51.6
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 52.6
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fixie/refs/heads/main/screenshots/fixie-2026-07-25T214652.png
security:
- kind: authentication
  name: Fixie Authentication
  slug: fixie-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Fixie Domain Security
  slug: fixie-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Fixie Trust Center
  slug: fixie-trust-center
  summary_line: trust center published
slug: fixie
tags:
- Company
- Voice AI
- Conversational AI
- Real-time
- Speech
- Agents
- Telephony
- Machine Learning
- SIP
- Webhooks
website: https://ultravox.ai/
---
