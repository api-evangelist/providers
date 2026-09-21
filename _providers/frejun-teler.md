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
  scored_at: '2026-09-20'
api_count: 2
apis:
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: Inspect the webhook events Teler generated for your account and redeliver any that your endpoint missed.
  name: FreJun Teler Events API
  slug: frejun-teler-events-api
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: Manage secret API keys used for authenticating requests. Create, rotate, and delete secrets — rotate periodically and keep them server-side.
  name: FreJun Teler Secrets API
  slug: frejun-teler-secrets-api
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: Read calls that arrived or left over your SIP trunks (`st_`).
  name: FreJun Teler SIP / Calls API
  slug: frejun-teler-sip-calls-api
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: 'Named sets of source IPs or CIDR networks (`acl_`) that SIP trunks with `authentication_type: IP` authorise against. Attach one to many trunks and update it in a single place.'
  name: FreJun Teler SIP / IP Access Control Lists API
  slug: frejun-teler-sip-ip-access-control-lists-api
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: SIP trunks connect Teler to your upstream carrier or PBX. Create, configure, and manage your trunks, or inspect which virtual numbers are assigned to each one.
  name: FreJun Teler SIP / Trunks API
  slug: frejun-teler-sip-trunks-api
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: Fetch short-lived, signed download URLs for call recordings.
  name: FreJun Teler Utilities API
  slug: frejun-teler-utilities-api
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: Phone numbers that Teler provisions for your account. List, assign to a voice app or SIP trunk, unassign, or update individual numbers.
  name: FreJun Teler Virtual Numbers API
  slug: frejun-teler-virtual-numbers-api
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: Voice apps are the configuration context for calls — they define webhook URLs, flows, and channel limits. Create and manage your voice apps here.
  name: FreJun Teler Voice / Apps API
  slug: frejun-teler-voice-apps-api
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: Act on a live call in real time — hang up, mute, send DTMF, or play audio. These actions are accepted asynchronously and return `202` with a `request_id`.
  name: FreJun Teler Voice / Call Controls API
  slug: frejun-teler-voice-call-controls-api
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: Place outbound calls and read call state. A **call** (`cs_`) is the top-level session; each party on it is a **leg** (`cl_`).
  name: FreJun Teler Voice / Calls API
  slug: frejun-teler-voice-calls-api
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: Deprecated endpoints kept for backwards compatibility. Prefer the **Voice / Calls** endpoints for all new integrations.
  name: FreJun Teler Voice / Calls (legacy) API
  slug: frejun-teler-voice-calls-legacy-api
- baseURL: https://api.frejun.ai
  baseurl_source: declared
  description: Higher-level, multi-step operations on a live call, such as transferring it to a new destination.
  name: FreJun Teler Voice / Operations API
  slug: frejun-teler-voice-operations-api
artifact_total: 18
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
overview: 'FreJun Teler publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Events API, Secrets API, SIP / Calls API, and 9 more. Tagged areas include programmable voice API, voice AI infrastructure, CPaaS, SIP Trunking, and telephony API.


  The FreJun Teler catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  FreJun Teler''s developer surface includes documentation, API reference, engineering blog, pricing, signup flow, authentication, sandbox, and 25 more developer resources.'
plans:
- name: Frejun Teler Plans Pricing
  plan_count: 0
  slug: frejun-teler-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Frejun Teler Rate Limits
  slug: frejun-teler-rate-limits
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 22.4
    contract_governance: 4.5
    contract_quality: 69.8
    developer_ergonomics: 45.8
    discoverability: 75.9
    operational_transparency: 34.2
  previous_composite: 42.9
  provenance:
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
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 29.2
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
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
