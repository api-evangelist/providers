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
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 24.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Ask your birth chart anything. Vedic and Western astrology computed for your exact birth time and place — every answer names its school and shows the reasoning. No subscription. The service provides t
  name: Kundaly API
  slug: kundaly-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/kundaly-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/kundaly-com/llms/kundaly-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kundaly-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/kundaly-com/mcp/kundaly-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kundaly-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/kundaly-com/well-known/kundaly-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kundaly-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/kundaly-com/hosts/kundaly-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kundaly-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/kundaly-com/vendors/kundaly-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kundaly-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://kundaly.com/trust/
- group: commercial
  title: ''
  type: Pricing
  url: https://kundaly.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://kundaly.com/app/signin
- group: auth
  href: https://artifacts.apis.io/kundaly-com/security/kundaly-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kundaly-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kundaly.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kundaly.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kundaly.com/legal/privacy
- group: other
  title: ''
  type: Refunds
  url: https://kundaly.com/legal/refunds
created: '2026-10-30'
description: Ask your birth chart anything. Vedic and Western astrology computed for your exact birth time and place — every answer names its school and shows the reasoning. No subscription. The service provides tools to handle unknown birth time, offers rectification, and explains different astrological schools.
image: https://kundaly.com/brand/logo-light.svg
layout: provider
mcp_servers:
- description: Remote MCP server at kundaly.com; 4 tools listed.
  name: kundaly-com MCP Server
  slug: kundaly-com-mcp-yml
modified: '2026-10-30'
name: kundaly-com
nav: Providers
network: true
overview: 'kundaly-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Astrology, Vedic, Western, and BirthChart.


  kundaly-com''s developer surface includes pricing and 13 more developer resources.'
plans:
- name: Kundaly Com Plans Pricing
  plan_count: 0
  slug: kundaly-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Kundaly Com Rate Limits
  slug: kundaly-com-rate-limits
scopes:
- name: Kundaly Com Scopes
  scope_count: 0
  slug: kundaly-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.4
    discoverability: 75.0
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.2
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/kundaly-com/kundaly-com-2026-11-03T134551.png
security:
- kind: authentication
  name: Kundaly Com Authentication
  slug: kundaly-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Kundaly Com Domain Security
  slug: kundaly-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kundaly-com
tags:
- Company
- Astrology
- Vedic
- Western
- BirthChart
website: https://kundaly.com/
---
