---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/bandmixr-com/plans/bandmixr-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bandmixr-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/bandmixr-com/security/bandmixr-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/bandmixr-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/bandmixr-com/llms/bandmixr-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bandmixr-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/bandmixr-com/mcp/bandmixr-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bandmixr-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/bandmixr-com/well-known/bandmixr-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bandmixr-com-security.txt
- group: agent
  href: https://artifacts.apis.io/bandmixr-com/well-known/bandmixr-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bandmixr-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/bandmixr-com/hosts/bandmixr-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bandmixr-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bandmixr-com/security/bandmixr-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/bandmixr-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/bandmixr-com/security/bandmixr-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bandmixr-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bandmixr.com/
- group: operate
  title: ''
  type: Support
  url: https://bandmixr.com/help
- group: company
  title: ''
  type: Blog
  url: https://bandmixr.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bandmixr.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bandmixr.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bandmixr.com/privacy
coverage:
  checked: '2026-11-02'
  detail: The Bandmixr website provides a developers page but no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://bandmixr.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Bandmixr is an AI mixing and mastering service for producers, artists and bands. Upload your stems and get a finished, streaming‑ready song in minutes. The platform offers automated mixing, genre‑aware EQ, compression, mastering presets, and tools like Mix Analyzer, Stem Separator, and Rehearsal Cutter. Pricing starts free with paid plans up to $19 per month, providing flexible options for creators.
image: https://bandmixr.com/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at bandmixr.com.
  name: Bandmixr MCP Server
  slug: bandmixr-com-mcp-yml
modified: '2026-11-02'
name: Bandmixr
nav: Providers
network: true
overview: 'Bandmixr is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Audio, Mixing, Mastering, Artificial Intelligence, and Music Production.


  Bandmixr''s developer surface includes support, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Bandmixr Com Plans Pricing
  plan_count: 3
  slug: bandmixr-com-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Bandmixr Com Rate Limits
  slug: bandmixr-com-rate-limits
scopes:
- name: Bandmixr Com Scopes
  scope_count: 0
  slug: bandmixr-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 20
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 48.3
    operational_transparency: 10.5
  previous_composite: 22.9
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bandmixr Com Authentication
  slug: bandmixr-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Bandmixr Com Domain Security
  slug: bandmixr-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Bandmixr Com Vulnerability Disclosure
  slug: bandmixr-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: bandmixr-com
tags:
- Audio
- Mixing
- Mastering
- Artificial Intelligence
- Music Production
website: https://bandmixr.com/
---
