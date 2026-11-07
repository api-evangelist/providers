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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Mixerbox Agentic Access
  operation_count: 29
  slug: mixerbox-agentic-access
  summary_line: 29 operations · 8 acting
api_count: 12
apis:
- baseURL: https://www.mbplayer.com
  baseurl_source: declared
  description: The Gpt API from MixerBox — 9 operation(s) for gpt.
  name: MixerBox Gpt API
  slug: mixerbox-gpt-api
- baseURL: https://www.mbplayer.com
  baseurl_source: declared
  description: The Gpt Plugins API from MixerBox — 19 operation(s) for gpt plugins.
  name: MixerBox Gpt Plugins API
  slug: mixerbox-gpt-plugins-api
- baseURL: https://www.mbplayer.com
  baseurl_source: declared
  description: The Services API from MixerBox — 1 operation(s) for services.
  name: MixerBox Services API
  slug: mixerbox-services-api
artifact_total: 15
collections:
- collection_type: open
  name: MixerBox Calendar Gpt API
  slug: open-mixerbox-gpt-api
- collection_type: open
  name: MixerBox Calendar Gpt Gpt Plugins API
  slug: open-mixerbox-gpt-plugins-api
- collection_type: open
  name: MixerBox Calendar Gpt Services?funcs=GetWeatherInfo&mobile=0 API
  slug: open-mixerbox-services-funcs-getweatherinfo-mobile-0-api
common:
- group: other
  href: https://artifacts.apis.io/mixerbox/capabilities/mixerbox-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mixerbox-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/mixerbox/overlays/mixerbox-calendar-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mixerbox-calendar-overlay.yaml
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
  href: https://artifacts.apis.io/mixerbox/well-known/mixerbox-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mixerbox-well-known.yml
- group: agent
  href: https://artifacts.apis.io/mixerbox/mcp/mixerbox-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mixerbox-mcp.yml
- group: agent
  href: https://artifacts.apis.io/mixerbox/llms/mixerbox-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mixerbox-llms.txt
- group: auth
  href: https://artifacts.apis.io/mixerbox/authentication/mixerbox-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mixerbox-authentication.yml
- group: design
  href: https://artifacts.apis.io/mixerbox/conventions/mixerbox-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mixerbox-conventions.yml
- group: design
  href: https://artifacts.apis.io/mixerbox/conformance/mixerbox-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mixerbox-conformance.yml
- group: design
  href: https://artifacts.apis.io/mixerbox/errors/mixerbox-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mixerbox-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mixerbox/lifecycle/mixerbox-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mixerbox-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/mixerbox/data-model/mixerbox-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mixerbox-data-model.yml
- group: agent
  href: https://artifacts.apis.io/mixerbox/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/mixerbox/agentic-access/mixerbox-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mixerbox-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/mixerbox/security/mixerbox-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mixerbox-domain-security.yml
created: '2026-07-17'
description: MixerBox ("Super-Apps to Live Easier") is a Y Combinator and Initialized Capital-backed consumer software company that ships a broad family of AI assistant tools as ChatGPT plugins / GPT Actions. Its catalog spans music and podcasts (OnePlayer, Podcasts), weather, a Google Calendar assistant, translation and language learning, text-to-image generation, photo enhancement, PDF and academic-paper question answering (ChatPDF, Scholar), QR generation, diagram rendering, and prompt optimization. Each product publishes an OpenAI plugin manifest (/.well-known/ai-plugin.json) and an OpenAPI 3.1 specification; authentication is service-level or open.
image: https://www.mbplayer.com/favicon-app_store_icon.png
layout: provider
modified: '2026-07-20'
name: MixerBox
nav: Providers
network: true
overview: 'MixerBox publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Gpt API, Gpt Plugins API, and Services API. Tagged areas include Company, Consumer, Artificial Intelligence, ChatGPT Plugins, and GPT Actions.


  The MixerBox catalog on APIs.io includes 1 Spectral governance ruleset.


  MixerBox''s developer surface includes support, authentication, and 16 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: MixerBox API Rules
  rule_count: 41
  severity_counts:
    error: 34
    hint: 0
    info: 3
    warn: 4
  slug: mixerbox-rules
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 44.5
    catalog_earned_first_party: 0.0
    catalog_gap: 70.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 44.1
    developer_ergonomics: 18.5
    discoverability: 78.6
    operational_transparency: 0.0
  previous_composite: 29.4
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mixerbox/mixerbox-2026-08-07T183823.png
security:
- kind: authentication
  name: Mixerbox Authentication
  slug: mixerbox-authentication
  summary_line: none/service_http · 0 schemes
- kind: domain-security
  name: Mixerbox Domain Security
  slug: mixerbox-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: Question a PDF with MixerBox ChatPDF
  slug: mixerbox-chat-with-pdf
- name: Generate images and QR codes with MixerBox
  slug: mixerbox-generate-image-and-qr
- name: Manage a Google Calendar with MixerBox Calendar
  slug: mixerbox-manage-calendar
- name: Play music and podcasts with MixerBox OnePlayer
  slug: mixerbox-play-music-and-podcasts
- name: Translate and learn languages with MixerBox Translate
  slug: mixerbox-translate
slug: mixerbox
tags:
- Company
- Consumer
- Artificial Intelligence
- ChatGPT Plugins
- GPT Actions
- Music
- Weather
- Translation
- Productivity
website: https://www.mixerbox.com/
---
