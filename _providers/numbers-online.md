---
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.7
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 35
  human_in_the_loop: 3
  name: Numbers Online Agentic Access
  operation_count: 56
  slug: numbers-online-agentic-access
  summary_line: 56 operations · 35 acting · 3 human-in-the-loop
api_count: 1
apis:
- baseURL: https://numbers.online
  baseurl_source: declared
  description: 'One REST API over a single E.164 primitive: parse and validate numbers, single and bulk lookup (line type, range carrier, CNAM, STIR/SHAKEN verstat and a supplementary spam signal), signed inbound cal'
  name: Numbers Online Phone Intelligence API
  slug: numbers-online-phone-intelligence-api
- description: A hosted, stateless, read-only Model Context Protocol server (JSON-RPC 2.0 over Streamable HTTP, protocol 2025-06-18) at POST https://numbers.online/api/v1/mcp for AI voice agents (Vapi, Retell, Pipec
  name: Numbers Online MCP Server
  slug: numbers-online-mcp-server
- description: An Agent-to-Agent (A2A protocolVersion 0.3.0, JSONRPC) endpoint at POST https://numbers.online/api/v1/a2a exposing four read-only skills — phone_lookup, line_type, caller_risk and dnc_check — the same
  name: Numbers Online A2A Agent
  slug: numbers-online-a2a-agent
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://numbers.online/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/security/numbers-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/numbers-online-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/agentic-access/numbers-online-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/numbers-online-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/authentication/numbers-online-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/a2a/numbers-online-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/numbers-online-a2a.yml
- group: other
  title: ''
  type: AgentCard
  url: https://numbers.online/.well-known/agent-card.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/well-known/numbers-online-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/numbers-online-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/llms/numbers-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/numbers-online-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/packages/numbers-online-packages.yml
  title: ''
  type: Packages
  url: packages/numbers-online-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/overlays/numbers-online-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/numbers-online-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/conformance/numbers-online-conformance.yml
  title: ''
  type: Conformance
  url: conformance/numbers-online-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/errors/numbers-online-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/numbers-online-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/lifecycle/numbers-online-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/numbers-online-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/lifecycle/numbers-online-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/numbers-online-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/conventions/numbers-online-conventions.yml
  title: ''
  type: Conventions
  url: conventions/numbers-online-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/conventions/numbers-online-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/numbers-online-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/rate-limits/numbers-online-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/numbers-online-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/plans/numbers-online-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/numbers-online-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/changelog/numbers-online-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/numbers-online-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://numbers.online/api/spec
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/data-model/numbers-online-data-model.yml
  title: ''
  type: DataModel
  url: data-model/numbers-online-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/skills/numbers-online-inbound-caller-intelligence.md
  title: ''
  type: AgentSkill
  url: skills/numbers-online-inbound-caller-intelligence.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/skills/numbers-online-outbound-precall-scrub.md
  title: ''
  type: AgentSkill
  url: skills/numbers-online-outbound-precall-scrub.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/skills/numbers-online-pbx-caller-id.md
  title: ''
  type: AgentSkill
  url: skills/numbers-online-pbx-caller-id.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/skills/numbers-online-key-lifecycle.md
  title: ''
  type: AgentSkill
  url: skills/numbers-online-key-lifecycle.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/numbers-online/refs/heads/main/skills/numbers-online-msp-tenants.md
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
image: https://numbers.online/android-chrome-512x512.png
layout: provider
mcp_servers:
- description: ''
  name: Numbers Online MCP Server
  slug: numbers-online-mcp-server
- description: ''
  name: Numbers Online MCP Server
  slug: numbers-online-mcp-server-2
modified: '2026-09-19'
name: Numbers Online
nav: Providers
network: true
overview: 'Numbers Online publishes 1 API on the [APIs.io](https://apis.io/) network: Phone Intelligence API. Tagged areas include Phone Intelligence, Caller ID, CNAM, Reverse Phone Lookup, and Spam Detection.


  Numbers Online''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, changelog, and 38 more developer resources.'
plans:
- name: Numbers Online Plans Pricing
  plan_count: 5
  slug: numbers-online-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 11
  name: Numbers Online Rate Limits
  slug: numbers-online-rate-limits
score:
  band: strong
  composite: 59.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 55.9
    developer_ergonomics: 56.5
    discoverability: 75.9
    operational_transparency: 60.5
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Numbers Online Authentication
  slug: numbers-online-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Numbers Online Domain Security
  slug: numbers-online-domain-security
  summary_line: TLSv1.3
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
