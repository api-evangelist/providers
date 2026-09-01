---
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/swiftmile-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/swiftmile-llms.txt
- group: company
  title: ''
  type: Website
  url: https://swiftmile.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/swiftmile-inc/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/swiftmile_stock/
coverage:
  checked: '2026-08-29'
  detail: swiftmile.com no longer serves the Swiftmile website — it answers HTTP 200 with a Nexcess hosting placeholder behind a TLS certificate issued for nxcli.net, has returned that same placeholder in every Internet Archive snapshot since 2025-07-09 (the real WordPress site was still live on 2025-04-21), every interior path including /wp-json/ now 404s, and no api., developer., docs., app., dashboard. or portal. subdomain resolves.
  evidence:
  - status: 200
    url: https://swiftmile.com/
  - status: 404
    url: https://swiftmile.com/wp-json/
  - status: 403
    url: https://swiftmile.com/.well-known/agent-card.json
  - status: 404
    url: https://swiftmile.com/openapi.json
  reason: defunct
  state: none
created: '2026-08-29'
description: Swiftmile is a California-based hardware and IoT company building universal charging and parking infrastructure for micromobility — docking stations that power, secure and organize shared and privately owned e-bikes and e-scooters, including solar-powered units and integrated digital advertising panels. Founded around 2014 and headquartered on the San Francisco Peninsula, it supplied secure charging docks to the New York City DOT public e-bike charging pilot alongside PopWheels and Swobbee. Company interviews describe a fleet- and battery-management backend with integrations offered to micromobility operators, but Swiftmile has never published a public developer program, API reference, SDK, or machine-readable contract of any kind, and as of 2026-08-29 swiftmile.com no longer serves the company website at all — the domain answers with a Nexcess hosting placeholder and a TLS certificate that does not match the hostname.
layout: provider
modified: '2026-08-29'
name: Swiftmile
nav: Providers
network: true
overview: Swiftmile is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Micromobility, Electric Vehicle Charging, Transportation, and Internet of Things.
plans:
- name: Swiftmile Plans Pricing
  plan_count: 0
  slug: swiftmile-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Swiftmile Rate Limits
  slug: swiftmile-rate-limits
score:
  band: minimal
  composite: 5.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Swiftmile Domain Security
  slug: swiftmile-domain-security
  summary_line: no transport/DNS hardening detected
slug: swiftmile
tags:
- Company
- Micromobility
- Electric Vehicle Charging
- Transportation
- Internet of Things
- Hardware
- Smart Cities
- Fleet Management
website: https://swiftmile.com/
---
