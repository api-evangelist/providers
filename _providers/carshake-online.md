---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
  score: 9.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: GPS‑verified car condition documentation for valet, rental, and parking damage protection
  name: CarShake API
  slug: carshake-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/carshake-online/plans/carshake-online-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/carshake-online-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/carshake-online/conformance/carshake-online-conformance.yml
  title: ''
  type: Conformance
  url: conformance/carshake-online-conformance.yml
- group: agent
  href: https://artifacts.apis.io/carshake-online/llms/carshake-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/carshake-online-llms.txt
- group: other
  href: https://artifacts.apis.io/carshake-online/a2a/carshake-online-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/carshake-online-a2a.yml
- group: agent
  href: https://artifacts.apis.io/carshake-online/mcp/carshake-online-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/carshake-online-mcp.yml
- group: other
  href: https://artifacts.apis.io/carshake-online/hosts/carshake-online-hosts.yml
  title: ''
  type: Hosts
  url: hosts/carshake-online-hosts.yml
- group: other
  href: https://artifacts.apis.io/carshake-online/vendors/carshake-online-vendors.yml
  title: ''
  type: Vendors
  url: vendors/carshake-online-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://carshake.online/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carshake.online/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carshake.online/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://carshake.online/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://carshake.online/press
- group: docs
  title: ''
  type: Documentation
  url: https://carshake.online/guides
- group: company
  title: ''
  type: Blog
  url: https://carshake.online/blog/
- group: auth
  href: https://artifacts.apis.io/carshake-online/security/carshake-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/carshake-online-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carshake.online/
created: '2026-11-03'
description: CarShake provides a free valet damage protection app that lets drivers capture timestamped, GPS‑verified photos of their vehicle condition before hand‑off. Founded after the creator lost $4,200 to a hotel valet, the service aims to ensure drivers never pay for damage they didn’t cause. The app is available on iOS and Android and integrates with insurance partners to streamline claims.
image: https://carshake.online/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at carshake.online.
  name: CarShake MCP Server
  slug: carshake-online-mcp-yml
modified: '2026-11-03'
name: CarShake
nav: Providers
network: true
overview: 'CarShake is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CarShake, Valet, DamageProtection, Mobile App, and Insurance.


  CarShake''s developer surface includes pricing, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Carshake Online Plans Pricing
  plan_count: 2
  slug: carshake-online-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 13
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 40.8
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 65.8
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 15.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Carshake Online Domain Security
  slug: carshake-online-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carshake-online
tags:
- CarShake
- Valet
- DamageProtection
- Mobile App
- Insurance
website: https://carshake.online/
---
