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
  band: human-only
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: ArabicKeyboard.ai provides a free online Arabic keyboard API accessible via its website.
  name: ArabicKeyboard API
  slug: arabickeyboard-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/arabickeyboard-ai/mcp/arabickeyboard-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arabickeyboard-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/arabickeyboard-ai/hosts/arabickeyboard-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arabickeyboard-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/arabickeyboard-ai/vendors/arabickeyboard-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arabickeyboard-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arabickeyboard.ai/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arabickeyboard.ai/privacy
- group: auth
  href: https://artifacts.apis.io/arabickeyboard-ai/security/arabickeyboard-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arabickeyboard-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arabickeyboard.ai/
coverage:
  checked: '2026-11-01'
  detail: Public website provides an Arabic keyboard tool but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://arabickeyboard.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: ArabicKeyboard.ai provides a free online Arabic keyboard that lets users type Arabic characters using an on-screen layout or by transliterating English letters. The tool supports multiple Arabic spellings, offers copy and save functionality, and includes features like diacritics, typing practice, games, and conversion utilities. It is accessible without installing any application, making Arabic typing instantly available to anyone worldwide.
image: https://arabickeyboard.ai/brand-mark.png
layout: provider
mcp_servers:
- description: Remote MCP server at arabickeyboard.ai.
  name: ArabicKeyboard.ai MCP Server
  slug: arabickeyboard-ai-mcp-yml
modified: '2026-11-01'
name: ArabicKeyboard.ai
nav: Providers
network: true
overview: ArabicKeyboard.ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Arabic, Keyboard, Free, Online, and Typing.
random_paper: 2
scopes:
- name: Arabickeyboard Ai Scopes
  scope_count: 0
  slug: arabickeyboard-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 12.0
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arabickeyboard Ai Authentication
  slug: arabickeyboard-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arabickeyboard Ai Domain Security
  slug: arabickeyboard-ai-domain-security
  summary_line: TLSv1.3 · HSTS
slug: arabickeyboard-ai
tags:
- Arabic
- Keyboard
- Free
- Online
- Typing
website: https://arabickeyboard.ai/
---
