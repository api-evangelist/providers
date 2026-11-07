---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 167
  human_in_the_loop: 7
  name: Call2Me App Agentic Access
  operation_count: 285
  slug: call2me-app-agentic-access
  summary_line: 285 operations · 167 acting · 7 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Agent Wizard API from Call2Me — 6 operation(s) for agent wizard.
  name: Call2Me Agent Wizard API
  slug: call2me-app-agent-wizard-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: 'Create and manage voice AI agents. An agent is the personality, voice and behavior of your AI — system prompt, model, language, voice, function-calling tools and (optionally) a knowledge base. You''ll '
  name: Call2Me Agents API
  slug: call2me-app-agents-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: Manage API keys used to authenticate against this API. Keys are workspace-scoped; rotate or revoke any time.
  name: Call2Me API Keys API
  slug: call2me-app-api-keys-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Audio API from Call2Me — 2 operation(s) for audio.
  name: Call2Me Audio API
  slug: call2me-app-audio-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Authentication API from Call2Me — 15 operation(s) for authentication.
  name: Call2Me Authentication API
  slug: call2me-app-authentication-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: Place outbound phone calls and inspect call history. `POST /v1/calls` starts an outbound call given an `agent_id`, a `from_number` and a `to_number`; the platform handles dialing, the AI conversation,
  name: Call2Me Calls API
  slug: call2me-app-calls-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Chats API from Call2Me — 3 operation(s) for chats.
  name: Call2Me Chats API
  slug: call2me-app-chats-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Contact API from Call2Me — 1 operation(s) for contact.
  name: Call2Me Contact API
  slug: call2me-app-contact-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Copilot API from Call2Me — 6 operation(s) for copilot.
  name: Call2Me Copilot API
  slug: call2me-app-copilot-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Demo API from Call2Me — 1 operation(s) for demo.
  name: Call2Me Demo API
  slug: call2me-app-demo-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Demo Numbers API from Call2Me — 5 operation(s) for demo numbers.
  name: Call2Me Demo Numbers API
  slug: call2me-app-demo-numbers-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The End Users API from Call2Me — 1 operation(s) for end users.
  name: Call2Me End Users API
  slug: call2me-app-end-users-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Events API from Call2Me — 1 operation(s) for events.
  name: Call2Me Events API
  slug: call2me-app-events-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Exchange Rate API from Call2Me — 1 operation(s) for exchange rate.
  name: Call2Me Exchange Rate API
  slug: call2me-app-exchange-rate-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Extensions API from Call2Me — 17 operation(s) for extensions.
  name: Call2Me Extensions API
  slug: call2me-app-extensions-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Functions API from Call2Me — 1 operation(s) for functions.
  name: Call2Me Functions API
  slug: call2me-app-functions-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: API health and status endpoints — useful for monitors and load balancers.
  name: Call2Me Health API
  slug: call2me-app-health-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Internal API from Call2Me — 32 operation(s) for internal.
  name: Call2Me Internal API
  slug: call2me-app-internal-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Interpreters API from Call2Me — 13 operation(s) for interpreters.
  name: Call2Me Interpreters API
  slug: call2me-app-interpreters-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: Upload documents (PDF, DOCX, TXT, MD) and URLs to give an agent domain-specific context. Vector search via pgvector + OpenAI embeddings; agents retrieve relevant chunks during conversation to answer f
  name: Call2Me Knowledge Base API
  slug: call2me-app-knowledge-base-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The LiveKit API from Call2Me — 3 operation(s) for livekit.
  name: Call2Me Live Kit API
  slug: call2me-app-livekit-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The LLM API from Call2Me — 1 operation(s) for llm.
  name: Call2Me LLM API
  slug: call2me-app-llm-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Newsletter API from Call2Me — 1 operation(s) for newsletter.
  name: Call2Me Newsletter API
  slug: call2me-app-newsletter-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Notifications API from Call2Me — 3 operation(s) for notifications.
  name: Call2Me Notifications API
  slug: call2me-app-notifications-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Payments API from Call2Me — 11 operation(s) for payments.
  name: Call2Me Payments API
  slug: call2me-app-payments-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: Provision and assign phone numbers. Buy from supported regions, connect a SIP trunk for BYOC, or reserve a temporary demo number. Numbers can be assigned to a specific agent for inbound routing.
  name: Call2Me Phone Numbers API
  slug: call2me-app-phone-numbers-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Phone Provisioning API from Call2Me — 6 operation(s) for phone provisioning.
  name: Call2Me Phone Provisioning API
  slug: call2me-app-phone-provisioning-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Pricing API from Call2Me — 1 operation(s) for pricing.
  name: Call2Me Pricing API
  slug: call2me-app-pricing-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Referrals API from Call2Me — 10 operation(s) for referrals.
  name: Call2Me Referrals API
  slug: call2me-app-referrals-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: One-shot or recurring scheduled outbound calls. Use this for follow-ups, reminders, periodic check-ins. Recurrence supports daily/weekly/monthly cron-style rules.
  name: Call2Me Schedules API
  slug: call2me-app-schedules-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The SIP API from Call2Me — 4 operation(s) for sip.
  name: Call2Me SIP API
  slug: call2me-app-sip-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The SIP Trunks API from Call2Me — 4 operation(s) for sip trunks.
  name: Call2Me SIP Trunks API
  slug: call2me-app-sip-trunks-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The SMS API from Call2Me — 1 operation(s) for sms.
  name: Call2Me SMS API
  slug: call2me-app-sms-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Stats API from Call2Me — 1 operation(s) for stats.
  name: Call2Me Stats API
  slug: call2me-app-stats-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Unsubscribe API from Call2Me — 1 operation(s) for unsubscribe.
  name: Call2Me Unsubscribe API
  slug: call2me-app-unsubscribe-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Users API from Call2Me — 16 operation(s) for users.
  name: Call2Me Users API
  slug: call2me-app-users-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Voice Sessions API from Call2Me — 2 operation(s) for voice sessions.
  name: Call2Me Voice Sessions API
  slug: call2me-app-voice-sessions-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: Browse available TTS voices from OpenAI, ElevenLabs, Cartesia and MiniMax. Filter by language, gender or provider; preview audio samples; reference a voice's `voice_id` when creating an agent.
  name: Call2Me Voices API
  slug: call2me-app-voices-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: Wallet balance, transaction history and top-ups. Calls, TTS and STT usage are billed per-minute against this balance.
  name: Call2Me Wallet API
  slug: call2me-app-wallet-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The WebCall API from Call2Me — 4 operation(s) for webcall.
  name: Call2Me Web Call API
  slug: call2me-app-webcall-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The WebCallPublic API from Call2Me — 2 operation(s) for webcallpublic.
  name: Call2Me Web Call Public API
  slug: call2me-app-webcallpublic-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: The Webhooks API from Call2Me — 1 operation(s) for webhooks.
  name: Call2Me Webhooks API
  slug: call2me-app-webhooks-api
- baseURL: https://api.call2me.app
  baseurl_source: declared
  description: Embeddable chat/voice widgets you can drop into a website. Each widget is bound to an agent and produces a `<script>` snippet plus optional domain allow-list.
  name: Call2Me Widgets API
  slug: call2me-app-widgets-api
artifact_total: 59
asyncapis:
- description: ''
  name: Call2Me App Webhooks
  slug: call2me-app-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/call2me-app/agentic-access/call2me-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/call2me-app-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/call2me-app/rate-limits/call2me-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/call2me-app-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/call2me-app/plans/call2me-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/call2me-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/call2me-app/rules/call2me-app-rules.yml
  title: ''
  type: Spectral
  url: rules/call2me-app-rules.yml
- group: design
  href: https://artifacts.apis.io/call2me-app/json-ld/call2me-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/call2me-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/call2me-app/vocabulary/call2me-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/call2me-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/call2me-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/call2me-app/asyncapi/call2me-app-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/call2me-app-webhooks.yml
- group: design
  href: https://artifacts.apis.io/call2me-app/data-model/call2me-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/call2me-app-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://call2me.app/docs/security
- group: auth
  href: https://artifacts.apis.io/call2me-app/authentication/call2me-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/call2me-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/call2me-app/errors/call2me-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/call2me-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/call2me-app/conformance/call2me-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/call2me-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/call2me-app/llms/call2me-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/call2me-app-llms.txt
- group: auth
  href: https://artifacts.apis.io/call2me-app/well-known/call2me-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/call2me-app-security.txt
- group: agent
  href: https://artifacts.apis.io/call2me-app/well-known/call2me-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/call2me-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/call2me-app/hosts/call2me-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/call2me-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/call2me-app/vendors/call2me-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/call2me-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://call2me.app/terms/
- group: start
  title: ''
  type: SignUp
  url: https://dash.call2me.app/signup
- group: build
  title: ''
  type: SDKs
  url: https://call2me.app/sdks/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://call2me.app/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/call2me-app
- group: company
  title: ''
  type: Blog
  url: https://call2me.app/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://call2me.app/guides/quickstart/
- group: docs
  title: ''
  type: APIReference
  url: https://call2me.app/docs/api-reference/
- group: auth
  href: https://artifacts.apis.io/call2me-app/security/call2me-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/call2me-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/call2me-app/security/call2me-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/call2me-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://call2me.app/
- group: docs
  title: ''
  type: Documentation
  url: https://call2me.app/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://call2me.app/pricing/
created: '2026-11-03'
description: Call2Me provides a live AI interpreter and voice agents for phone calls, enabling real‑time translation and automated call handling. Users can start for free, paying as low as $0.25 per minute. The platform supports bidirectional communication, multiple languages, and 24/7 availability, targeting businesses, legal, and healthcare sectors.
image: https://call2me.app/opengraph-image?ef6f54b3bb7daaa2
json_schemas:
- name: Agent
  property_count: 41
  slug: call2me-app-agent
- name: Call
  property_count: 18
  slug: call2me-app-call
- name: CreateCallRequest
  property_count: 7
  slug: call2me-app-call2me-core-models-call-create-call-request
- name: CreateAgentRequest
  property_count: 35
  slug: call2me-app-create-agent-request
- name: UpdateAgentRequest
  property_count: 36
  slug: call2me-app-update-agent-request
- name: UserProfile
  property_count: 20
  slug: call2me-app-user-profile
jsonld:
- class_count: 120
  name: Call2Me App Context
  property_count: 376
  slug: call2me-app-context
layout: provider
modified: '2026-11-03'
name: Call2Me
nav: Providers
network: true
overview: 'Call2Me publishes 43 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent Wizard API, Agents API, API Keys API, and 40 more. Tagged areas include Company, Artificial Intelligence, Voice, Interpreter, and Real-Time.


  The Call2Me catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Call2Me''s developer surface includes authentication, signup flow, engineering blog, getting-started guide, API reference, documentation, pricing, and 24 more developer resources.'
plans:
- name: Call2Me App Plans Pricing
  plan_count: 4
  slug: call2me-app-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 1
  name: Call2Me App Rate Limits
  slug: call2me-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Call2Me API Rules
  rule_count: 68
  severity_counts:
    error: 54
    hint: 0
    info: 5
    warn: 9
  slug: call2me-app-rules
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 22
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 70.7
    developer_ergonomics: 41.0
    discoverability: 66.1
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 43
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Call2Me App Authentication
  slug: call2me-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Call2Me App Domain Security
  slug: call2me-app-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Call2Me App Vulnerability Disclosure
  slug: call2me-app-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: health-check
  slug: call2me-app-health-check
slug: call2me-app
tags:
- Company
- Artificial Intelligence
- Voice
- Interpreter
- Real-Time
- Payments
website: https://call2me.app/
---
