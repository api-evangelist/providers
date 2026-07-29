---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Mixerbox Agentic Access
  operation_count: 31
  slug: mixerbox-agentic-access
  summary_line: 31 operations · 11 acting
api_count: 3
apis:
- description: The Gpt API from MixerBox — 9 operation(s) for gpt.
  name: MixerBox Gpt API
  slug: mixerbox-gpt-api
- description: The Gpt Plugins API from MixerBox — 19 operation(s) for gpt plugins.
  name: MixerBox Gpt Plugins API
  slug: mixerbox-gpt-plugins-api
- description: The Services?funcs=GetWeatherInfo&mobile=0 API from MixerBox — 1 operation(s) for services?funcs=getweatherinfo&mobile=0.
  name: MixerBox Services?funcs=GetWeatherInfo&mobile=0 API
  slug: mixerbox-services-funcs-getweatherinfo-mobile-0-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.mixerbox.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mixerbox.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mixerbox.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:support@mixerbox.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mixerbox-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mixerbox-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mixerbox-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/mixerbox-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mixerbox-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mixerbox-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mixerbox-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mixerbox-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mixerbox-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mixerbox-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mixerbox-domain-security.yml
created: '2026-07-17'
description: MixerBox ("Super-Apps to Live Easier") is a Y Combinator and Initialized Capital-backed consumer software company that ships a broad family of AI assistant tools as ChatGPT plugins / GPT Actions. Its catalog spans music and podcasts (OnePlayer, Podcasts), weather, a Google Calendar assistant, translation and language learning, text-to-image generation, photo enhancement, PDF and academic-paper question answering (ChatPDF, Scholar), QR generation, diagram rendering, and prompt optimization. Each product publishes an OpenAI plugin manifest (/.well-known/ai-plugin.json) and an OpenAPI 3.1 specification; authentication is service-level or open.
image: https://www.mbplayer.com/favicon-app_store_icon.png
layout: provider
mcp_servers:
- description: ''
  name: mixerbox-mcp.yml
  slug: mixerbox-mcpyml
modified: '2026-07-20'
name: MixerBox
nav: Providers
network: true
overview: 'MixerBox publishes 3 APIs on the [APIs.io](https://apis.io/) network: Gpt API, Gpt Plugins API, and Services?funcs=GetWeatherInfo&mobile=0 API. Tagged areas include Company, Consumer, Artificial Intelligence, ChatGPT Plugins, and GPT Actions.


  MixerBox''s developer surface includes support, authentication, and 14 more developer resources.'
random_paper: 78
score:
  band: thin
  composite: 30.3
  delta: -1.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 46.4
    developer_ergonomics: 19.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 0.0
  previous_composite: 31.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Mixerbox Authentication
  slug: mixerbox-authentication
  summary_line: none/service_http · 0 schemes
- kind: domain-security
  name: Mixerbox Domain Security
  slug: mixerbox-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mixerbox
tags:
- Company
- Consumer
- Artificial Intelligence
- ChatGPT Plugins
- GPT Actions
- Music
- Podcasts
- Weather
- Translation
- Productivity
website: https://www.mixerbox.com/
---
