---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 57
  human_in_the_loop: 0
  name: Fixie Agentic Access
  operation_count: 114
  slug: fixie-agentic-access
  summary_line: 114 operations · 57 acting
api_count: 1
apis:
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The accounts API from Fixie — 9 operation(s) for accounts.
  name: Fixie Accounts API
  slug: fixie-accounts-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The agents API from Fixie — 9 operation(s) for agents.
  name: Fixie Agents API
  slug: fixie-agents-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The api_keys API from Fixie — 2 operation(s) for api_keys.
  name: Fixie API Keys API
  slug: fixie-api-keys-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The call_throttles API from Fixie — 2 operation(s) for call_throttles.
  name: Fixie Call Throttles API
  slug: fixie-call-throttles-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The calls API from Fixie — 13 operation(s) for calls.
  name: Fixie Calls API
  slug: fixie-calls-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The corpora API from Fixie — 8 operation(s) for corpora.
  name: Fixie Corpora API
  slug: fixie-corpora-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The deleted_calls API from Fixie — 2 operation(s) for deleted_calls.
  name: Fixie Deleted Calls API
  slug: fixie-deleted-calls-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The models API from Fixie — 1 operation(s) for models.
  name: Fixie Models API
  slug: fixie-models-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The schema API from Fixie — 1 operation(s) for schema.
  name: Fixie Schema API
  slug: fixie-schema-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The sip API from Fixie — 3 operation(s) for sip.
  name: Fixie Sip API
  slug: fixie-sip-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The telephony_configs API from Fixie — 3 operation(s) for telephony_configs.
  name: Fixie Telephony Configs API
  slug: fixie-telephony-configs-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The tools API from Fixie — 4 operation(s) for tools.
  name: Fixie Tools API
  slug: fixie-tools-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The voices API from Fixie — 4 operation(s) for voices.
  name: Fixie Voices API
  slug: fixie-voices-api
- baseURL: https://api.ultravox.ai/api
  baseurl_source: declared
  description: The webhooks API from Fixie — 2 operation(s) for webhooks.
  name: Fixie Webhooks API
  slug: fixie-webhooks-api
artifact_total: 39
asyncapis:
- description: ''
  name: Fixie Webhooks
  slug: fixie-webhooks
collections:
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
- group: commercial
  href: https://artifacts.apis.io/fixie/plans/fixie-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fixie-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/fixie/capabilities/fixie-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fixie-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/fixie/mcp/fixie-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/fixie-mcp.yml
- group: other
  href: https://artifacts.apis.io/fixie/overlays/fixie-ultravox-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fixie-ultravox-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/fixie/security/fixie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fixie-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/fixie/security/fixie-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fixie-trust-center.yml
- group: build
  href: https://artifacts.apis.io/fixie/packages/fixie-packages.yml
  title: ''
  type: Packages
  url: packages/fixie-packages.yml
- group: build
  href: https://artifacts.apis.io/fixie/packages/fixie-packages.yml
  title: ''
  type: SDKs
  url: packages/fixie-packages.yml
- group: operate
  href: https://artifacts.apis.io/fixie/changelog/fixie-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fixie-changelog.yml
- group: agent
  href: https://artifacts.apis.io/fixie/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/fixie/llms/fixie-llms.txt
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
  href: https://artifacts.apis.io/fixie/asyncapi/fixie-webhooks.yml
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
finops:
- has_sources: true
  method: derived
  name: Fixie Finops
  primary_unit: minute
  service_category: ''
  slug: fixie-finops
  template: false
image: https://raw.githubusercontent.com/api-evangelist/fixie/refs/heads/main/openapi/fixie-ultravox-openapi-original.yml
layout: provider
modified: '2026-07-19'
name: Fixie
nav: Providers
network: true
overview: 'Fixie publishes 14 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Agents API, API Keys API, and 11 more. Tagged areas include Company, Voice AI, Conversational AI, Real-Time, and Speech.


  The Fixie catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Fixie''s developer surface includes changelog, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Fixie Plans Pricing
  plan_count: 7
  slug: fixie-plans-pricing
- name: Fixie Price Estimates
  plan_count: 0
  slug: fixie-price-estimates
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Fixie API Rules
  rule_count: 50
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 10
  slug: fixie-rules
score:
  band: strong
  composite: 60.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 53.9
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 42.1
  previous_composite: 60.8
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
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 27.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fixie/fixie-2026-07-25T214652.png
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
skill_count: 2
skills:
- name: Create a voice agent and start a call
  slug: fixie-create-agent-and-call
- name: Subscribe to call webhooks and fetch recordings
  slug: fixie-webhooks-and-recording
slug: fixie
tags:
- Company
- Voice AI
- Conversational AI
- Real-Time
- Speech
- Agents
- Telephony
- Machine Learning
- SIP
- Webhook
website: https://ultravox.ai/
---
