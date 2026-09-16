---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.9
  scored_at: '2026-09-15'
api_count: 1
apis:
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: Programmable voice/telephony API. Places and controls live voice calls (initiate, play audio, DTMF, transfer, hangup), streams bidirectional call audio to AI agents over a WebSocket media channel, and
  name: Teler Voice API
  slug: teler-voice-api
artifact_total: 7
asyncapis:
- description: ''
  name: Frejun Teler Webhooks
  slug: frejun-teler-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.frejun.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://frejun.com/docs/teler/
- group: docs
  title: ''
  type: Documentation
  url: https://frejun.com/docs/teler/
- group: docs
  title: ''
  type: APIReference
  url: https://api.frejun.ai/redoc
- group: company
  title: ''
  type: Blog
  url: https://frejun.com/teler-blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://frejun.com/teler/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://platform.frejun.ai/signup
- group: start
  title: ''
  type: Login
  url: https://platform.frejun.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://frejun.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://frejun.com/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/frejun-tech
- group: operate
  title: ''
  type: StatusPage
  url: https://frejun.statuspage.io
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.frejun.ai/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/well-known/frejun-teler-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/frejun-teler-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/authentication/frejun-teler-authentication.yml
  title: ''
  type: Authentication
  url: authentication/frejun-teler-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/security/frejun-teler-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/frejun-teler-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/conventions/frejun-teler-conventions.yml
  title: ''
  type: Conventions
  url: conventions/frejun-teler-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/lifecycle/frejun-teler-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/frejun-teler-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/lifecycle/frejun-teler-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/frejun-teler-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/conformance/frejun-teler-conformance.yml
  title: ''
  type: Conformance
  url: conformance/frejun-teler-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/mcp/frejun-teler-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/frejun-teler-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/packages/frejun-teler-packages.yml
  title: ''
  type: Packages
  url: packages/frejun-teler-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/packages/frejun-teler-packages.yml
  title: ''
  type: SDKs
  url: packages/frejun-teler-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/components/frejun-teler-components.yml
  title: ''
  type: Components
  url: components/frejun-teler-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/asyncapi/frejun-teler-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/frejun-teler-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/data-model/frejun-teler-data-model.yml
  title: ''
  type: DataModel
  url: data-model/frejun-teler-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/errors/frejun-teler-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/frejun-teler-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/overlays/frejun-teler-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/frejun-teler-openapi-overlay.yaml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/sandbox/frejun-teler-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/frejun-teler-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/rate-limits/frejun-teler-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/frejun-teler-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/frejun-teler/refs/heads/main/plans/frejun-teler-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/frejun-teler-plans-pricing.yml
created: '2026-09-15'
description: FreJun Teler is a developer-first programmable voice/telephony API (CPaaS) that handles carriers, phone numbers, and real-time audio streaming so developers can connect AI models (STT/LLM/TTS) to live phone calls. It offers real-time bidirectional audio over WebSocket (L16/8000 Hz, sub-250ms latency) and programmable SIP trunking, with webhook event delivery and official Python (teler) and Node (@frejun/teler) SDKs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: FreJun Teler MCP Server
  slug: frejun-teler-mcp-server
modified: '2026-09-15'
name: FreJun Teler
nav: Providers
network: true
overview: 'FreJun Teler publishes 1 API on the [APIs.io](https://apis.io/) network: Teler Voice API. Tagged areas include programmable voice API, voice AI infrastructure, CPaaS, SIP Trunking, and telephony API.


  The FreJun Teler catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  FreJun Teler''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, authentication, sandbox, and 25 more developer resources.'
plans:
- name: Frejun Teler Plans Pricing
  plan_count: 0
  slug: frejun-teler-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Frejun Teler Rate Limits
  slug: frejun-teler-rate-limits
score:
  band: developing
  composite: 48.3
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 60.4
    developer_ergonomics: 56.5
    discoverability: 75.9
    operational_transparency: 36.8
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 34.7
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Frejun Teler Authentication
  slug: frejun-teler-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Frejun Teler Domain Security
  slug: frejun-teler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: frejun-teler
tags:
- programmable voice API
- voice AI infrastructure
- CPaaS
- SIP Trunking
- telephony API
- real-time media streaming
- WebSocket audio
- Call Automation
- conversational AI infrastructure
website: https://www.frejun.ai
---
