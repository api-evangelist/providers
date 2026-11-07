---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for Chamade voice and chat gateway
  name: Chamade API
  slug: chamade-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/chamade-io/authentication/chamade-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chamade-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/chamade-io/conformance/chamade-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chamade-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chamade-io/llms/chamade-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chamade-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/chamade-io/well-known/chamade-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chamade-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/chamade-io/hosts/chamade-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chamade-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/chamade-io/vendors/chamade-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chamade-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/chamade-io/packages/chamade-io-packages.yml
  title: ''
  type: SDKs
  url: packages/chamade-io-packages.yml
- group: build
  href: https://artifacts.apis.io/chamade-io/packages/chamade-io-packages.yml
  title: ''
  type: Packages
  url: packages/chamade-io-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://chamade.io/signup
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dev.chamade.io/login
- group: start
  title: ''
  type: GettingStarted
  url: https://chamade.io/llms-setup.txt
- group: auth
  href: https://artifacts.apis.io/chamade-io/security/chamade-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chamade-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chamade.io/
- group: docs
  title: ''
  type: Documentation
  url: https://chamade.io/docs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chamade.io/legal#privacy
created: '2026-11-03'
description: Chamade provides a voice and chat gateway for AI agents, enabling integration with meetings, phone calls, and direct messages across platforms such as Teams, Zoom, Google Meet, Discord, Telegram, Slack, WhatsApp, Nextcloud Talk, and SIP. Users can drive the service via MCP or REST APIs, attach LLM providers like OpenAI, Anthropic, Gemini, or Mistral, and customize audio handling with hosted STT/TTS or their own stack via WebSocket. The platform offers flexible deployment and comprehensive communication capabilities for AI-driven interactions.
layout: provider
modified: '2026-11-03'
name: Chamade
nav: Providers
network: true
overview: 'Chamade is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Voice gateway, Chat gateway, AI Agents, SIP, and Speech API.


  Chamade''s developer surface includes authentication, signup flow, getting-started guide, documentation, and 11 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 15.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 11.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Chamade Io Authentication
  slug: chamade-io-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Chamade Io Domain Security
  slug: chamade-io-domain-security
  summary_line: TLSv1.3
slug: chamade-io
tags:
- Voice gateway
- Chat gateway
- AI Agents
- SIP
- Speech API
website: https://chamade.io/
---
