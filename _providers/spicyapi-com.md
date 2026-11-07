---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 40
  human_in_the_loop: 1
  name: Spicyapi Com Agentic Access
  operation_count: 67
  slug: spicyapi-com-agentic-access
  summary_line: 67 operations · 40 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.spicyapi.com
  baseurl_source: declared
  description: 'REST mirror of the MCP server at https://www.spicyapi.com/api/mcp: same key, same handlers, same guardrails.'
  name: spicyapi-com Agent tools API
  slug: spicyapi-com-agent-tools-api
- baseURL: https://api.spicyapi.com
  baseurl_source: declared
  description: The Audio API from spicyapi-com — 6 operation(s) for audio.
  name: spicyapi-com Audio API
  slug: spicyapi-com-audio-api
- baseURL: https://api.spicyapi.com
  baseurl_source: declared
  description: The Characters API from spicyapi-com — 5 operation(s) for characters.
  name: spicyapi-com Characters API
  slug: spicyapi-com-characters-api
- baseURL: https://api.spicyapi.com
  baseurl_source: declared
  description: The Core API from spicyapi-com — 3 operation(s) for core.
  name: spicyapi-com Core API
  slug: spicyapi-com-core-api
- baseURL: https://api.spicyapi.com
  baseurl_source: declared
  description: Always available with a valid key.
  name: spicyapi-com Default API
  slug: spicyapi-com-default-api
- baseURL: https://api.spicyapi.com
  baseurl_source: declared
  description: The Embeddings API from spicyapi-com — 1 operation(s) for embeddings.
  name: spicyapi-com Embeddings API
  slug: spicyapi-com-embeddings-api
- baseURL: https://api.spicyapi.com
  baseurl_source: declared
  description: 'Spending and credential tools: need approval_token unless the account turned approvals off.'
  name: spicyapi-com Guarded API
  slug: spicyapi-com-guarded-api
- baseURL: https://api.spicyapi.com
  baseurl_source: declared
  description: The Images API from spicyapi-com — 5 operation(s) for images.
  name: spicyapi-com Images API
  slug: spicyapi-com-images-api
- baseURL: https://api.spicyapi.com
  baseurl_source: declared
  description: The Live calls API from spicyapi-com — 2 operation(s) for live calls.
  name: spicyapi-com Live calls API
  slug: spicyapi-com-live-calls-api
- baseURL: https://api.spicyapi.com
  baseurl_source: declared
  description: The Moderation API from spicyapi-com — 2 operation(s) for moderation.
  name: spicyapi-com Moderation API
  slug: spicyapi-com-moderation-api
- baseURL: https://api.spicyapi.com
  baseurl_source: declared
  description: The Video API from spicyapi-com — 5 operation(s) for video.
  name: spicyapi-com Video API
  slug: spicyapi-com-video-api
- baseURL: https://api.spicyapi.com
  baseurl_source: declared
  description: The Chat Completions API from spicyapi-com — 1 operation(s) for chat completions.
  name: spicyapi-com Chat Completions API
  slug: spicyapi-com-chat-completions-api
artifact_total: 29
common:
- group: agent
  href: https://artifacts.apis.io/spicyapi-com/agentic-access/spicyapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/spicyapi-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/spicyapi-com/rate-limits/spicyapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/spicyapi-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/spicyapi-com/rules/spicyapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/spicyapi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/spicyapi-com/vocabulary/spicyapi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/spicyapi-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/spicyapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/spicyapi-com/authentication/spicyapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/spicyapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/spicyapi-com/errors/spicyapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/spicyapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/spicyapi-com/conformance/spicyapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/spicyapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/spicyapi-com/well-known/spicyapi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/spicyapi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/spicyapi-com/hosts/spicyapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spicyapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/spicyapi-com/vendors/spicyapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/spicyapi-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.spicyapi.com/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://www.spicyapi.com/dashboard/help
- group: operate
  title: ''
  type: StatusPage
  url: https://www.spicyapi.com/status
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.spicyapi.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.spicyapi.com/docs/integrations
- group: auth
  href: https://artifacts.apis.io/spicyapi-com/security/spicyapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spicyapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spicyapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.spicyapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.spicyapi.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://www.spicyapi.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spicyapi
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://spicyapi.com/openapi.json
  - status: null
    url: https://www.spicyapi.com/openapi.json
  - status: null
    url: https://api.spicyapi.com/openapi.json
  - status: 401
    url: https://www.spicyapi.com/api/mcp
  - status: 401
    url: https://api.spicyapi.com/api/mcp
  - status: 200
    url: https://spicyapi.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Spicy API provides an uncensored adult‑focused AI generation platform offering chat, image, video, voice and live voice call capabilities through a single OpenAI‑compatible endpoint. Developers can integrate role‑play chat, photorealistic image creation, video with sound, and expressive voice synthesis in minutes, paying per unit with prices starting at $0.06 per image. Operated by Wayfinity Ltd, a Cyprus‑registered company, the service enforces 18+ age gating, prohibits real people, and logs all requests for compliance. The API is hosted at api.spicyapi.com and accessed via a dashboard at spicyapi.com.
image: https://www.spicyapi.com/favicon.ico
layout: provider
modified: '2026-10-31'
name: spicyapi-com
nav: Providers
network: true
overview: 'spicyapi-com publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent tools API, Audio API, Characters API, and 9 more. Tagged areas include Company, Artificial Intelligence, Adult, Image Generation, and Video Generation.


  The spicyapi-com catalog on APIs.io includes 1 Spectral governance ruleset.


  spicyapi-com''s developer surface includes authentication, support, getting-started guide, documentation, API reference, pricing, and 16 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 1
  name: Spicyapi Com Rate Limits
  slug: spicyapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: spicyapi-com API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 6
  slug: spicyapi-com-rules
scopes:
- name: Spicyapi Com Scopes
  scope_count: 0
  slug: spicyapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 52.9
    developer_ergonomics: 30.4
    discoverability: 66.1
    operational_transparency: 31.6
  previous_composite: 45.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/spicyapi-com/spicyapi-com-2026-11-03T143631.png
security:
- kind: authentication
  name: Spicyapi Com Authentication
  slug: spicyapi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Spicyapi Com Domain Security
  slug: spicyapi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 11
skills:
- name: creat-e-lcharacter
  slug: creat-e-lcharacter
- name: creat-e-limage
  slug: creat-e-limage
- name: edi-t-limage
  slug: edi-t-limage
- name: eras-e-len-d-luser
  slug: eras-e-len-d-luser
- name: ge-t-laccount
  slug: ge-t-laccount
- name: impor-t-lcharacter
  slug: impor-t-lcharacter
- name: lis-t-limages
  slug: lis-t-limages
- name: lis-t-lmodels
  slug: lis-t-lmodels
- name: lis-t-lstyles
  slug: lis-t-lstyles
- name: moderatio-n-lappeals
  slug: moderatio-n-lappeals
- name: moderations
  slug: moderations
slug: spicyapi-com
tags:
- Company
- Artificial Intelligence
- Adult
- Image Generation
- Video Generation
- Voice
website: https://spicyapi.com/
---
