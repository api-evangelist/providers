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
  band: agent-native
  dimensions:
    agent_card: conformant
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
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 51.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 35
  human_in_the_loop: 3
  name: Numbers Online Agentic Access
  operation_count: 56
  slug: numbers-online-agentic-access
  summary_line: 56 operations · 35 acting · 3 human-in-the-loop
api_count: 2
apis:
- description: A hosted, stateless, read-only Model Context Protocol server (JSON-RPC 2.0 over Streamable HTTP, protocol 2025-06-18) at POST https://numbers.online/api/v1/mcp for AI voice agents (Vapi, Retell, Pipec
  name: Numbers Online MCP Server
  slug: numbers-online-mcp-server
- description: An Agent-to-Agent (A2A protocolVersion 0.3.0, JSONRPC) endpoint at POST https://numbers.online/api/v1/a2a exposing four read-only skills — phone_lookup, line_type, caller_risk and dnc_check — the same
  name: Numbers Online A2A Agent
  slug: numbers-online-a2a-agent
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: 'Self-service API account: signup, balance, usage, credit top-ups, and the key lifecycle. Account-management endpoints require an account-level key with the ''manage'' use case (every self-service key ho'
  name: Numbers Online Account API
  slug: numbers-online-account-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: Key-gated spam/scam reporting — the give-to-get half of the community sensor (receipt-gated, tags-only, lane-scoped supplementary signals)
  name: Numbers Online Community reporting API
  slug: numbers-online-community-reporting-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: Inbound caller-intelligence lookup for operators, PBX, and softphones
  name: Numbers Online Inbound API
  slug: numbers-online-inbound-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: 'Number lookup: line type, range carrier, CNAM, verstat, and a supplementary spam signal'
  name: Numbers Online Lookup API
  slug: numbers-online-lookup-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: 'Model Context Protocol server for AI voice agents (Vapi, Retell, Pipecat, LiveKit): read-only phone-intelligence tools over Streamable HTTP'
  name: Numbers Online MCP API
  slug: numbers-online-mcp-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: 'Multi-tenant control plane: per-tenant sub-keys, usage rollups, and suppression lists for MSPs and PBX resellers'
  name: Numbers Online MSP API
  slug: numbers-online-msp-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: Outbound pre-call checks (scrub + call-provenance) and number enrollment for spoofing-defense
  name: Numbers Online Outbound API
  slug: numbers-online-outbound-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: Phone number parsing and validation endpoints
  name: Numbers Online Parsing API
  slug: numbers-online-parsing-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: Plain-text caller-id lookup for header-less PBX integrations (FreeSWITCH mod_cidlookup and similar)
  name: Numbers Online PBX API
  slug: numbers-online-pbx-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: Signed, privacy-safe lookup receipts (Ed25519) — verifiable "checked as of T" evidence
  name: Numbers Online Receipts API
  slug: numbers-online-receipts-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: Reference data and examples
  name: Numbers Online Reference API
  slug: numbers-online-reference-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: SIP redirect-server decisions for session border controllers (Kamailio, OpenSIPS, dSIPRouter, Sansay, Oracle/Acme Packet, ProSBC) via the operator-run shim recipe, plus an FCC robocall-mitigation evid
  name: Numbers Online SBC / SIP API
  slug: numbers-online-sbc-sip-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: Operational endpoints (health checks)
  name: Numbers Online System API
  slug: numbers-online-system-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: Contact-suppression preference lookups
  name: Numbers Online Trust API
  slug: numbers-online-trust-api
- baseURL: https://numbers.online/api/v1/mcp
  baseurl_source: declared
  description: AI-voice-agent webhook adapters (Retell inbound, Vapi custom tool) over the same lookup backend
  name: Numbers Online Webhooks API
  slug: numbers-online-webhooks-api
artifact_total: 31
common:
- group: other
  href: https://artifacts.apis.io/numbers-online/capabilities/numbers-online-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/numbers-online-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://numbers.online/
- group: auth
  href: https://artifacts.apis.io/numbers-online/security/numbers-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/numbers-online-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/numbers-online/agentic-access/numbers-online-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/numbers-online-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/numbers-online/authentication/numbers-online-authentication.yml
  title: ''
  type: Authentication
  url: authentication/numbers-online-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://numbers.online/developers
- group: docs
  title: ''
  type: Documentation
  url: https://numbers.online/docs
- group: docs
  title: ''
  type: APIReference
  url: https://numbers.online/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://numbers.online/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://numbers.online/pricing
- group: start
  title: ''
  type: SignUp
  url: https://numbers.online/developers
- group: start
  title: ''
  type: Login
  url: https://numbers.online/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://numbers.online/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://numbers.online/privacy
- group: company
  title: ''
  type: About
  url: https://numbers.online/about
- group: auth
  title: ''
  type: Trust
  url: https://numbers.online/trust
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/numbers-online
- group: agent
  title: ''
  type: LLMsTxt
  url: https://numbers.online/llms.txt
- group: other
  href: https://artifacts.apis.io/numbers-online/a2a/numbers-online-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/numbers-online-a2a.yml
- group: other
  title: ''
  type: AgentCard
  url: https://numbers.online/.well-known/agent-card.json
- group: agent
  href: https://artifacts.apis.io/numbers-online/well-known/numbers-online-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/numbers-online-well-known.yml
- group: agent
  href: https://artifacts.apis.io/numbers-online/llms/numbers-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/numbers-online-llms.txt
- group: build
  href: https://artifacts.apis.io/numbers-online/packages/numbers-online-packages.yml
  title: ''
  type: Packages
  url: packages/numbers-online-packages.yml
- group: other
  href: https://artifacts.apis.io/numbers-online/overlays/numbers-online-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/numbers-online-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/numbers-online/conformance/numbers-online-conformance.yml
  title: ''
  type: Conformance
  url: conformance/numbers-online-conformance.yml
- group: design
  href: https://artifacts.apis.io/numbers-online/errors/numbers-online-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/numbers-online-problem-types.yml
- group: design
  href: https://artifacts.apis.io/numbers-online/lifecycle/numbers-online-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/numbers-online-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/numbers-online/lifecycle/numbers-online-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/numbers-online-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/numbers-online/conventions/numbers-online-conventions.yml
  title: ''
  type: Conventions
  url: conventions/numbers-online-conventions.yml
- group: design
  href: https://artifacts.apis.io/numbers-online/conventions/numbers-online-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/numbers-online-conventions.yml
- group: operate
  href: https://artifacts.apis.io/numbers-online/rate-limits/numbers-online-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/numbers-online-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/numbers-online/plans/numbers-online-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/numbers-online-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/numbers-online/changelog/numbers-online-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/numbers-online-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://numbers.online/api/spec
- group: design
  href: https://artifacts.apis.io/numbers-online/data-model/numbers-online-data-model.yml
  title: ''
  type: DataModel
  url: data-model/numbers-online-data-model.yml
- group: agent
  href: https://artifacts.apis.io/numbers-online/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/numbers-online/skills/numbers-online-inbound-caller-intelligence.md
  title: ''
  type: AgentSkill
  url: skills/numbers-online-inbound-caller-intelligence.md
- group: agent
  href: https://artifacts.apis.io/numbers-online/skills/numbers-online-outbound-precall-scrub.md
  title: ''
  type: AgentSkill
  url: skills/numbers-online-outbound-precall-scrub.md
- group: agent
  href: https://artifacts.apis.io/numbers-online/skills/numbers-online-pbx-caller-id.md
  title: ''
  type: AgentSkill
  url: skills/numbers-online-pbx-caller-id.md
- group: agent
  href: https://artifacts.apis.io/numbers-online/skills/numbers-online-key-lifecycle.md
  title: ''
  type: AgentSkill
  url: skills/numbers-online-key-lifecycle.md
- group: agent
  href: https://artifacts.apis.io/numbers-online/skills/numbers-online-msp-tenants.md
  title: ''
  type: AgentSkill
  url: skills/numbers-online-msp-tenants.md
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://numbers.online/opt-out
- group: other
  title: ''
  type: NoticeAndAction
  url: https://numbers.online/opt-out
- group: docs
  title: ''
  type: Guides
  url: https://numbers.online/docs/integrations
- group: other
  title: ''
  type: AgentInstructions
  url: https://numbers.online/ai-agents
- group: operate
  title: ''
  type: Support
  url: https://numbers.online/concierge
created: '2026-09-19'
description: 'Numbers Online is a phone-number trust and intelligence service operated by Evergrow Management Pte. Ltd. of Singapore. It runs a free public reverse phone lookup with a community-driven, advisory spam-risk score, paid number verification for people and businesses, and a B2B API keyed on a single E.164 primitive: parsing and validation, single and batch lookup (line type, range carrier, CNAM, STIR/SHAKEN verstat and a low-confidence spam signal), signed inbound caller intelligence with Ed25519 receipts, an outbound pre-call do-not-contact scrub and call-provenance enrollment, consent-first list scrubbing, a ClearIP-compatible SBC/SIP redirect decision, a multi-tenant MSP control plane, and a hosted read-only MCP server plus Vapi/Retell webhooks for AI voice agents. The 56-operation REST API is published as an OpenAPI 3.0.3 contract at /api/spec, with an llms.txt, an A2A agent card at /.well-known/agent-card.json, markdown mirrors of the docs, and a self-service free tier with
  no card.'
finops:
- has_sources: true
  method: derived
  name: Numbers Online Finops
  primary_unit: verification
  service_category: ''
  slug: numbers-online-finops
  template: false
image: https://numbers.online/android-chrome-512x512.png
layout: provider
mcp_servers:
- description: Numbers Online operates ONE hosted, stateless, read-only MCP server at POST https://numbers.online/api/v1/mcp (JSON-RPC 2.0 over Streamable HTTP; the provider and Vapi call the transport literal "shtt
  name: Numbers Online MCP Server
  slug: numbers-online-mcp-yml
modified: '2026-09-19'
name: Numbers Online
nav: Providers
network: true
overview: 'Numbers Online publishes 17 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Community reporting API, Inbound API, and 14 more. Tagged areas include Phone Intelligence, Caller ID, CNAM, Reverse Phone Lookup, and Spam Detection.


  The Numbers Online catalog on APIs.io includes 1 Spectral governance ruleset.


  Numbers Online''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, changelog, and 39 more developer resources.'
plans:
- name: Numbers Online Plans Pricing
  plan_count: 5
  slug: numbers-online-plans-pricing
- name: Numbers Online Price Estimates
  plan_count: 0
  slug: numbers-online-price-estimates
random_paper: 14
rate_limits:
- limit_count: 11
  name: Numbers Online Rate Limits
  slug: numbers-online-rate-limits
rules:
- authorship: generated
  effective_rule_count: 109
  extends:
  - spectral:oas
  name: Numbers Online API Rules
  rule_count: 68
  severity_counts:
    error: 53
    hint: 0
    info: 3
    warn: 12
  slug: numbers-online-rules
score:
  band: developing
  composite: 51.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.8
  facets:
    access_clarity: 65.8
    contract_governance: 31.8
    contract_quality: 48.5
    developer_ergonomics: 35.1
    discoverability: 75.0
    operational_transparency: 50.0
  previous_composite: 63.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/numbers-online/numbers-online-2026-10-11T111657.png
security:
- kind: authentication
  name: Numbers Online Authentication
  slug: numbers-online-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Numbers Online Domain Security
  slug: numbers-online-domain-security
  summary_line: TLSv1.3
skill_count: 5
skills:
- name: Assess an inbound caller and file a receipt-backed report
  slug: numbers-online-inbound-caller-intelligence
- name: Sign up, fund and rotate API keys safely
  slug: numbers-online-key-lifecycle
- name: Run multi-tenant PBX or SBC customers under one prepaid balance
  slug: numbers-online-msp-tenants
- name: Scrub a destination before dialing and enrol your caller ID for call-provenance
  slug: numbers-online-outbound-precall-scrub
- name: Label inbound calls on a PBX or softphone with caller name and risk
  slug: numbers-online-pbx-caller-id
slug: numbers-online
tags:
- Phone Intelligence
- Caller ID
- CNAM
- Reverse Phone Lookup
- Spam Detection
- Do Not Call
- Telephony
- STIR/SHAKEN
- MCP
- Agent-Native
- Compliance
- Company
- A2A
website: https://numbers.online/
---
