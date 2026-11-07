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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP tool list providing various astrology calculation tools.
  name: AstroTune MCP
  slug: astrotune-mcp
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/astrotune-io/mcp/astrotune-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/astrotune-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/astrotune-io/hosts/astrotune-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/astrotune-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/astrotune-io/vendors/astrotune-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/astrotune-io-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://astrotune.io/en/sign-in
- group: auth
  href: https://artifacts.apis.io/astrotune-io/security/astrotune-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/astrotune-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://astrotune.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://astrotune.io/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://astrotune.io/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://astrotune.io/en/contact
created: '2026-11-01'
description: AstroTune provides a web-based Vedic astrology platform that calculates natal charts using traditional Jyotish methods. Users input birth date, time, and location to receive detailed charts, including ayanamsa, house systems, and planetary positions. The service emphasizes transparency about data handling and offers tools for learning about zodiac signs, nakshatras, and planetary influences.
image: https://astrotune.io/assets/logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at astrotune.io.
  name: AstroTune MCP Server
  slug: astrotune-io-mcp-yml
modified: '2026-11-01'
name: AstroTune
nav: Providers
network: true
overview: 'AstroTune is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Astrology, Vedic, Natal Chart, Horoscope, and Web App.


  AstroTune''s developer surface includes support and 8 more developer resources.'
plans:
- name: Astrotune Io Plans Pricing
  plan_count: 0
  slug: astrotune-io-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Astrotune Io Rate Limits
  slug: astrotune-io-rate-limits
scopes:
- name: Astrotune Io Scopes
  scope_count: 0
  slug: astrotune-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 15.6
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
  name: Astrotune Io Authentication
  slug: astrotune-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Astrotune Io Domain Security
  slug: astrotune-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: astrotune-io
tags:
- Astrology
- Vedic
- Natal Chart
- Horoscope
- Web App
website: https://astrotune.io/
---
