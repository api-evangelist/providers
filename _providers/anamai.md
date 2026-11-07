---
access_model:
  confidence: high
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
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 30
  human_in_the_loop: 1
  name: Anamai Agentic Access
  operation_count: 57
  slug: anamai-agentic-access
  summary_line: 57 operations · 30 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.anam.ai/v1/
  baseurl_source: declared
  description: The Avatars API from Anam.ai — 2 operation(s) for avatars.
  name: Anam.ai Avatars API
  slug: anamai-avatars-api
- baseURL: https://api.anam.ai/v1/
  baseurl_source: declared
  description: The Engine API from Anam.ai — 1 operation(s) for engine.
  name: Anam.ai Engine API
  slug: anamai-engine-api
- baseURL: https://api.anam.ai/v1/
  baseurl_source: declared
  description: The Knowledge API from Anam.ai — 6 operation(s) for knowledge.
  name: Anam.ai Knowledge API
  slug: anamai-knowledge-api
- baseURL: https://api.anam.ai/v1/
  baseurl_source: declared
  description: The Meetings API from Anam.ai — 2 operation(s) for meetings.
  name: Anam.ai Meetings API
  slug: anamai-meetings-api
- baseURL: https://api.anam.ai/v1/
  baseurl_source: declared
  description: The Personas API from Anam.ai — 2 operation(s) for personas.
  name: Anam.ai Personas API
  slug: anamai-personas-api
- baseURL: https://api.anam.ai/v1/
  baseurl_source: declared
  description: The Sessions API from Anam.ai — 9 operation(s) for sessions.
  name: Anam.ai Sessions API
  slug: anamai-sessions-api
- baseURL: https://api.anam.ai/v1/
  baseurl_source: declared
  description: The Share Links API from Anam.ai — 2 operation(s) for share links.
  name: Anam.ai Share Links API
  slug: anamai-share-links-api
- baseURL: https://api.anam.ai/v1/
  baseurl_source: declared
  description: The Tools API from Anam.ai — 2 operation(s) for tools.
  name: Anam.ai Tools API
  slug: anamai-tools-api
- baseURL: https://api.anam.ai/v1/
  baseurl_source: declared
  description: The Voices API from Anam.ai — 3 operation(s) for voices.
  name: Anam.ai Voices API
  slug: anamai-voices-api
- baseURL: https://api.anam.ai/v1/
  baseurl_source: declared
  description: The LLMs API from Anam.ai — 2 operation(s) for llms.
  name: Anam.ai LL Ms API
  slug: anamai-llms-api
- baseURL: https://api.anam.ai/v1/
  baseurl_source: declared
  description: The Avatar Videos API from Anam.ai — 4 operation(s) for avatar videos.
  name: Anam.ai Avatar Videos API
  slug: anamai-avatar-videos-api
- baseURL: https://api.anam.ai/v1/
  baseurl_source: declared
  description: The Pronunciation Dictionaries API from Anam.ai — 3 operation(s) for pronunciation dictionaries.
  name: Anam.ai Pronunciation Dictionaries API
  slug: anamai-pronunciation-dictionaries-api
artifact_total: 45
collections:
- collection_type: postman
  name: Anam AI Avatars API
  slug: postman-anamai-avatars-api
- collection_type: postman
  name: Anam AI Avatars Engine API
  slug: postman-anamai-engine-api
- collection_type: postman
  name: Anam AI Avatars Knowledge API
  slug: postman-anamai-knowledge-api
- collection_type: postman
  name: Anam AI Avatars LLMs API
  slug: postman-anamai-llms-api
- collection_type: postman
  name: Anam AI Avatars Meetings API
  slug: postman-anamai-meetings-api
- collection_type: postman
  name: Anam AI Avatars Personas API
  slug: postman-anamai-personas-api
- collection_type: postman
  name: Anam AI Avatars Sessions API
  slug: postman-anamai-sessions-api
- collection_type: postman
  name: Anam AI Avatars Share Links API
  slug: postman-anamai-share-links-api
- collection_type: postman
  name: Anam AI Avatars Tools API
  slug: postman-anamai-tools-api
- collection_type: postman
  name: Anam AI Avatars Voices API
  slug: postman-anamai-voices-api
- collection_type: open
  name: Anam AI Avatars API
  slug: open-anamai-avatars-api
- collection_type: open
  name: Anam AI Avatars Engine API
  slug: open-anamai-engine-api
- collection_type: open
  name: Anam AI Avatars Knowledge API
  slug: open-anamai-knowledge-api
- collection_type: open
  name: Anam AI Avatars LLMs API
  slug: open-anamai-llms-api
- collection_type: open
  name: Anam AI Avatars Meetings API
  slug: open-anamai-meetings-api
- collection_type: open
  name: Anam AI Avatars Personas API
  slug: open-anamai-personas-api
- collection_type: open
  name: Anam AI Avatars Sessions API
  slug: open-anamai-sessions-api
- collection_type: open
  name: Anam AI Avatars Share Links API
  slug: open-anamai-share-links-api
- collection_type: open
  name: Anam AI Avatars Tools API
  slug: open-anamai-tools-api
- collection_type: open
  name: Anam AI Avatars Voices API
  slug: open-anamai-voices-api
common:
- group: commercial
  href: https://artifacts.apis.io/anamai/plans/anamai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anamai-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/anamai/capabilities/anamai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/anamai-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/anamai/overlays/anamai-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/anamai-openapi-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/anamai/overview
- group: start
  title: ''
  type: DeveloperPortal
  url: https://anam.ai/docs
- group: docs
  title: ''
  type: Documentation
  url: https://anam.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://anam.ai/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://anam.ai/docs/quickstart
- group: company
  title: ''
  type: Blog
  url: https://anam.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://anam.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://lab.anam.ai/register
- group: start
  title: ''
  type: Login
  url: https://lab.anam.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anam.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anam.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@anam.ai
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anam-org
- group: operate
  title: ''
  type: StatusPage
  url: https://status.anam.ai/
- group: operate
  href: https://artifacts.apis.io/anamai/changelog/anamai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/anamai-changelog.yml
- group: auth
  title: ''
  type: Trust
  url: https://trust.anam.ai/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.anam.ai/
- group: build
  href: https://artifacts.apis.io/anamai/packages/anamai-packages.yml
  title: ''
  type: Packages
  url: packages/anamai-packages.yml
- group: build
  href: https://artifacts.apis.io/anamai/packages/anamai-packages.yml
  title: ''
  type: SDKs
  url: packages/anamai-packages.yml
- group: agent
  href: https://artifacts.apis.io/anamai/mcp/anamai-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/anamai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/anamai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/anamai/llms/anamai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anamai-llms.txt
- group: agent
  href: https://artifacts.apis.io/anamai/well-known/anamai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anamai-well-known.yml
- group: auth
  href: https://artifacts.apis.io/anamai/well-known/anamai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/anamai-security.txt
- group: auth
  title: ''
  type: Security
  url: https://anam.ai/.well-known/security.txt
- group: design
  href: https://artifacts.apis.io/anamai/conformance/anamai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anamai-conformance.yml
- group: design
  href: https://artifacts.apis.io/anamai/errors/anamai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anamai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anamai/lifecycle/anamai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/anamai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/anamai/conventions/anamai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/anamai-conventions.yml
- group: design
  href: https://artifacts.apis.io/anamai/data-model/anamai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anamai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/anamai/rate-limits/anamai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/anamai-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/anamai/agentic-access/anamai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anamai-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/anamai/security/anamai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/anamai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/anamai/security/anamai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/anamai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/anamai/security/anamai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anamai-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/anamai/authentication/anamai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/anamai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://anam.ai/
created: '2026-07-17'
description: Anam.ai is a real-time interactive AI avatar platform for building conversational video AI agents with photorealistic personas. Its proprietary CARA-4 avatar model streams over WebRTC with ultra-low latency (around 180ms) across 70+ languages, powering customer support, sales, tutoring, medical, and training use cases. The REST API (https://api.anam.ai/v1/) lets teams create and manage personas, avatars, voices, LLM configs, RAG knowledge groups, tools, share links, and sessions, and invite personas into Google Meet, Zoom, and Microsoft Teams calls via the Meetings API. Auth is a two-step Bearer flow (API key exchanged for a short-lived session token). Anam is HIPAA and SOC 2 certified. Surfaced as a Techstars portfolio company and enriched into the API Evangelist network.
finops:
- has_sources: true
  method: derived
  name: Anamai Finops
  primary_unit: minute
  service_category: ''
  slug: anamai-finops
  template: false
image: https://framerusercontent.com/assets/cyASyHEg6g3WK5dCwQoOyyVbFZU.png
layout: provider
modified: '2026-07-17'
name: Anam.ai
nav: Providers
network: true
overview: 'Anam.ai publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Avatars API, Engine API, Knowledge API, and 9 more. Tagged areas include Company, AI Avatars, Conversational AI, Real-Time Video, and WebRTC.


  The Anam.ai catalog on APIs.io includes 1 Spectral governance ruleset.


  Anam.ai''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 33 more developer resources.'
plans:
- name: Anamai Plans Pricing
  plan_count: 6
  slug: anamai-plans-pricing
- name: Anamai Price Estimates
  plan_count: 0
  slug: anamai-price-estimates
random_paper: 15
rate_limits:
- limit_count: 5
  name: Anamai Rate Limits
  slug: anamai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 97
  extends:
  - spectral:oas
  name: Anam.ai API Rules
  rule_count: 56
  severity_counts:
    error: 41
    hint: 0
    info: 2
    warn: 13
  slug: anamai-rules
score:
  band: strong
  composite: 64.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 58.4
    developer_ergonomics: 67.3
    discoverability: 73.2
    operational_transparency: 71.1
  previous_composite: 63.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 52.2
      total: 23
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/anamai/anamai-2026-07-25T200158.png
security:
- kind: authentication
  name: Anamai Authentication
  slug: anamai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Anamai Domain Security
  slug: anamai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Anamai Vulnerability Disclosure
  slug: anamai-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Anamai Trust Center
  slug: anamai-trust-center
  summary_line: SOC 2, HIPAA
skill_count: 3
skills:
- name: Build a RAG knowledge base for a persona
  slug: anamai-build-knowledge-base
- name: Create a persona and start a live avatar session
  slug: anamai-create-persona-and-start-session
- name: Invite a persona to a video meeting
  slug: anamai-invite-persona-to-meeting
slug: anamai
tags:
- Company
- AI Avatars
- Conversational AI
- Real-Time Video
- WebRTC
- Digital Humans
- Generative AI
website: https://anam.ai/
---
