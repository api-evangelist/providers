---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 29
  human_in_the_loop: 2
  name: Bithuman Ai Agentic Access
  operation_count: 52
  slug: bithuman-ai-agentic-access
  summary_line: 52 operations · 29 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: Identity, plan, credits, and pricing.
  name: bithuman-ai Account API
  slug: bithuman-ai-account-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: Control live avatar sessions — make them speak or inject knowledge.
  name: bithuman-ai Agent Context API
  slug: bithuman-ai-agent-context-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: Create new avatar agents from prompts, portraits, and voice samples.
  name: bithuman-ai Agent Generation API
  slug: bithuman-ai-agent-generation-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: Retrieve and update existing agents.
  name: bithuman-ai Agent Management API
  slug: bithuman-ai-agent-management-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: 'Create, list and delete your account''s API secrets: [https://docs.bithuman.ai/api/api-keys](https://docs.bithuman.ai/api/api-keys).'
  name: bithuman-ai API secrets API
  slug: bithuman-ai-api-secrets-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: Verify API credentials with `POST /v1/validate`.
  name: bithuman-ai Authentication API
  slug: bithuman-ai-authentication-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: Check credit balance, plan details, and usage history.
  name: bithuman-ai Billing API
  slug: bithuman-ai-billing-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: 'Generate and manage conversational gesture animations (wave, nod, laugh, idle motions) for an avatar. Generate them asynchronously, then toggle on/off to make them the active model for live sessions. '
  name: bithuman-ai Dynamics API
  slug: bithuman-ai-dynamics-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: Mint short-lived tokens for website avatar embeds.
  name: bithuman-ai Embedding API
  slug: bithuman-ai-embedding-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: Upload images, videos, audio, and documents.
  name: bithuman-ai Files API
  slug: bithuman-ai-files-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: 'Ingest sources and build knowledge bases, with an organization API secret: [https://docs.bithuman.ai/api/knowledge](https://docs.bithuman.ai/api/knowledge).'
  name: bithuman-ai Knowledge API
  slug: bithuman-ai-knowledge-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: 'Bring your own LLM, STT and TTS keys: [https://docs.bithuman.ai/api/providers](https://docs.bithuman.ai/api/providers).'
  name: bithuman-ai Providers API
  slug: bithuman-ai-providers-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: OpenAI Realtime voice through bitHuman; the WebSocket relay is on [https://docs.bithuman.ai/api/realtime](https://docs.bithuman.ai/api/realtime).
  name: bithuman-ai Realtime API
  slug: bithuman-ai-realtime-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: 'List live sessions, read a transcript, end or terminate a session, revoke every runtime key: [https://docs.bithuman.ai/api/runtime-sessions](https://docs.bithuman.ai/api/runtime-sessions).'
  name: bithuman-ai Runtime sessions API
  slug: bithuman-ai-runtime-sessions-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: 'The two routes a self-hosted or on-device runtime calls: check that its key is still live, and report the session time it served. See [Pricing](https://docs.bithuman.ai/pricing).'
  name: bithuman-ai Self Hosting API
  slug: bithuman-ai-self-hosting-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: Is the API currently refusing work? Unauthenticated, always HTTP 200 — read the `status` field. For a fleet-wide view use [status.bithuman.ai](https://status.bithuman.ai).
  name: bithuman-ai Status API
  slug: bithuman-ai-status-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: 'Render a finished talking-video mp4 from text or audio. Submit [`POST /v1/video/generate`](#operation/generateTalkingVideo) — async by default, or `wait: true` for a blocking render — and poll [`GET /'
  name: bithuman-ai Video API
  slug: bithuman-ai-video-api
- baseURL: https://api.bithuman.ai
  baseurl_source: declared
  description: Register HTTPS endpoints to receive signed event notifications when async work finishes (`agent.ready`, `agent.failed`, `video.completed`, `video.failed`). Each delivery carries an `X-BitHuman-Signatu
  name: bithuman-ai Webhooks API
  slug: bithuman-ai-webhooks-api
artifact_total: 33
common:
- group: agent
  href: https://artifacts.apis.io/bithuman-ai/agentic-access/bithuman-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bithuman-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/bithuman-ai/plans/bithuman-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bithuman-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bithuman-ai/rules/bithuman-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bithuman-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bithuman-ai/json-ld/bithuman-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bithuman-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/bithuman-ai/vocabulary/bithuman-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bithuman-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bithuman-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bithuman-ai/data-model/bithuman-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bithuman-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/bithuman-ai/changelog/bithuman-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bithuman-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/bithuman-ai/authentication/bithuman-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bithuman-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/bithuman-ai/lifecycle/bithuman-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bithuman-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/bithuman-ai/errors/bithuman-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bithuman-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bithuman-ai/conformance/bithuman-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bithuman-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bithuman-ai/llms/bithuman-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bithuman-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/bithuman-ai/well-known/bithuman-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bithuman-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bithuman-ai/hosts/bithuman-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bithuman-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bithuman-ai/vendors/bithuman-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bithuman-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/bithuman-ai/packages/bithuman-ai-packages.yml
  title: ''
  type: Packages
  url: packages/bithuman-ai-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.bithuman.ai/security
- group: build
  title: ''
  type: SDKs
  url: https://gitlab.com/bithuman/sdk/bithuman-examples
- group: start
  title: ''
  type: Login
  url: https://www.bithuman.ai/sign-in
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bithuman.ai/platforms/ios/quickstart
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.bithuman.ai/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bithuman.ai/api
- group: auth
  href: https://artifacts.apis.io/bithuman-ai/security/bithuman-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bithuman-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bithuman.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.bithuman.ai/developer
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bithuman.ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bithuman.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.bithuman.ai/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bithuman.ai/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bithuman.ai/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bithuman.ai/
- group: operate
  title: ''
  type: Support
  url: https://docs.bithuman.ai/support
created: '2026-10-29'
description: 'bitHuman makes real-time AI avatars for your app or your enterprise: iPhone, Android, Mac, Linux and the browser, or your own servers. Every configuration we publish renders faster than playback speed.'
image: https://www.bithuman.ai/bithuman_heroshot_image.jpg
json_schemas:
- name: AgentListItem
  property_count: 14
  slug: bithuman-ai-agent-list-item
- name: Agent
  property_count: 31
  slug: bithuman-ai-agent
- name: ProviderSelection
  property_count: 0
  slug: bithuman-ai-provider-selection
- name: UsageEvent
  property_count: 11
  slug: bithuman-ai-usage-event
- name: WebhookDelivery
  property_count: 7
  slug: bithuman-ai-webhook-delivery
- name: Webhook
  property_count: 7
  slug: bithuman-ai-webhook
jsonld:
- class_count: 9
  name: Bithuman Ai Context
  property_count: 56
  slug: bithuman-ai-context
layout: provider
modified: '2026-10-29'
name: bithuman-ai
nav: Providers
network: true
overview: 'bithuman-ai publishes 18 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agent Context API, Agent Generation API, and 15 more. Tagged areas include Company, Artificial Intelligence, Avatars, Real-Time, and Platform.


  The bithuman-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  bithuman-ai''s developer surface includes changelog, authentication, getting-started guide, API reference, documentation, pricing, engineering blog, and 26 more developer resources.'
plans:
- name: Bithuman Ai Plans Pricing
  plan_count: 4
  slug: bithuman-ai-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Bithuman Ai Rate Limits
  slug: bithuman-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: bithuman-ai API Rules
  rule_count: 16
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 4
  slug: bithuman-ai-rules
scopes:
- name: Bithuman Ai Scopes
  scope_count: 0
  slug: bithuman-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 32
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.2
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 66.8
    developer_ergonomics: 48.1
    discoverability: 73.2
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 63.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bithuman-ai/bithuman-ai-2026-11-03T121800.png
security:
- kind: authentication
  name: Bithuman Ai Authentication
  slug: bithuman-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bithuman Ai Domain Security
  slug: bithuman-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: api-secret-management
  slug: bithuman-ai-api-secret-management
slug: bithuman-ai
tags:
- Company
- Artificial Intelligence
- Avatars
- Real-Time
- Platform
website: https://bithuman.ai/
---
