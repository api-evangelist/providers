---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Machine-readable tool list for Assetzaar marketplace via MCP.
  name: Assetzaar MCP
  slug: assetzaar-mcp
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/assetzaar-com/plans/assetzaar-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/assetzaar-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/assetzaar-com/security/assetzaar-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/assetzaar-com-vulnerability-disclosure.yml
- group: agent
  href: https://artifacts.apis.io/assetzaar-com/llms/assetzaar-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/assetzaar-com-llms.txt
- group: build
  href: https://artifacts.apis.io/assetzaar-com/mcp/assetzaar-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/assetzaar-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/assetzaar-com/mcp/assetzaar-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/assetzaar-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/assetzaar-com/well-known/assetzaar-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/assetzaar-com-security.txt
- group: agent
  href: https://artifacts.apis.io/assetzaar-com/well-known/assetzaar-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/assetzaar-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/assetzaar-com/hosts/assetzaar-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/assetzaar-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/assetzaar-com/vendors/assetzaar-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/assetzaar-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/assetzaar-com/security/assetzaar-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/assetzaar-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/assetzaar-com/security/assetzaar-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/assetzaar-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://assetzaar.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://assetzaar.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://assetzaar.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://assetzaar.com/getting-started
- group: operate
  title: ''
  type: Support
  url: https://assetzaar.com/support
- group: company
  title: ''
  type: Blog
  url: https://assetzaar.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://assetzaar.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://assetzaar.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://assetzaar.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://assetzaar.com/signup
created: '2026-11-01'
description: Assetzaar is a curated marketplace offering a wide range of production‑ready Next.js kits, React components, landing pages, AI agent skills, and automations. It enables developers and teams to quickly integrate high‑quality UI and functional building blocks into modern web stacks, supporting worldwide customers with clear licensing and live previews.
image: https://assetzaar.com/assetzaar.svg
json_schemas:
- name: Assetzaar Com Mcp
  property_count: 0
  slug: assetzaar-com-mcp
layout: provider
mcp_servers:
- description: Remote MCP server at assetzaar.com.
  name: Assetzaar MCP Server
  slug: assetzaar-com-mcp-yml
modified: '2026-11-01'
name: Assetzaar
nav: Providers
network: true
overview: 'Assetzaar is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, React, Next.js, Software-as-a-Service, and Components.


  Assetzaar''s developer surface includes documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Assetzaar Com Plans Pricing
  plan_count: 3
  slug: assetzaar-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Assetzaar Com Rate Limits
  slug: assetzaar-com-rate-limits
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 31.2
  provenance:
    conformance: unknown
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Assetzaar Com Authentication
  slug: assetzaar-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Assetzaar Com Domain Security
  slug: assetzaar-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Assetzaar Com Vulnerability Disclosure
  slug: assetzaar-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: assetzaar-com
tags:
- Marketplace
- React
- Next.js
- Software-as-a-Service
- Components
- Artificial Intelligence
- Templates
website: https://assetzaar.com/
---
