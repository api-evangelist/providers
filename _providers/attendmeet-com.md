---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    auth_clarity: false
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: A public API is planned and listed in the documentation, but no endpoint or specification is currently published.
  name: AttendMeet API
  slug: attendmeet-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/attendmeet-com/llms/attendmeet-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/attendmeet-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/attendmeet-com/mcp/attendmeet-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/attendmeet-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/attendmeet-com/well-known/attendmeet-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/attendmeet-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/attendmeet-com/hosts/attendmeet-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/attendmeet-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/attendmeet-com/vendors/attendmeet-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/attendmeet-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/attendmeet-com/security/attendmeet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/attendmeet-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://attendmeet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://attendmeet.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://attendmeet.com/soporte/
- group: commercial
  title: ''
  type: Pricing
  url: https://attendmeet.com/precios/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://attendmeet.com/cumplimiento/
- group: start
  title: ''
  type: GettingStarted
  url: https://attendmeet.com/docs/
- group: start
  title: ''
  type: SignUp
  url: https://app.attendmeet.com
coverage:
  checked: '2026-11-02'
  detail: Documentation mentions a public API on the roadmap but provides no machine‑readable specification or base URL.
  evidence:
  - status: 200
    url: https://attendmeet.com/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: AttendMeet is an AI‑powered meeting assistant that automatically joins video calls on Google Meet, Microsoft Teams and Zoom, records them, transcribes speech with speaker attribution, and generates structured summaries and action items. It offers both a self‑hosted deployment for privacy‑first customers and a managed SaaS version, supporting multiple AI model providers and providing participation metrics, all secured with AES‑256 encryption and compliance with GDPR, CCPA and Colombian data protection laws.
image: https://attendmeet.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.attendmeet.com.
  name: AttendMeet MCP Server
  slug: attendmeet-com-mcp-yml
modified: '2026-11-02'
name: AttendMeet
nav: Providers
network: true
overview: 'AttendMeet is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Meeting Assistant, Transcription, Software-as-a-Service, and Privacy.


  AttendMeet''s developer surface includes documentation, support, pricing, getting-started guide, signup flow, and 8 more developer resources.'
plans:
- name: Attendmeet Com Plans Pricing
  plan_count: 0
  slug: attendmeet-com-plans-pricing
random_paper: 15
scopes:
- name: Attendmeet Com Scopes
  scope_count: 0
  slug: attendmeet-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.3
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 18.2
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Attendmeet Com Authentication
  slug: attendmeet-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Attendmeet Com Domain Security
  slug: attendmeet-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: attendmeet-com
tags:
- Artificial Intelligence
- Meeting Assistant
- Transcription
- Software-as-a-Service
- Privacy
website: https://attendmeet.com/
---
