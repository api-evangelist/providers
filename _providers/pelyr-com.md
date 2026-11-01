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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 3.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: ''
  name: Pelyr AIS API
  slug: pelyr-ais-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/pelyr-com/plans/pelyr-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pelyr-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/pelyr-com/security/pelyr-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/pelyr-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/pelyr-com/conformance/pelyr-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pelyr-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pelyr-com/llms/pelyr-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pelyr-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/pelyr-com/mcp/pelyr-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pelyr-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/pelyr-com/well-known/pelyr-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pelyr-com-security.txt
- group: agent
  href: https://artifacts.apis.io/pelyr-com/well-known/pelyr-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pelyr-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/pelyr-com/hosts/pelyr-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pelyr-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pelyr-com/vendors/pelyr-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pelyr-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pelyr.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://dashboard.pelyr.com/en/docs
- group: auth
  href: https://artifacts.apis.io/pelyr-com/security/pelyr-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pelyr-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/pelyr-com/security/pelyr-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pelyr-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pelyr.com
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.pelyr.com/openapi.json
  - status: 401
    url: https://api.pelyr.com/mcp
  - status: 200
    url: https://pelyr.com
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Pelyr provides free maritime intelligence through an HTTPS AIS API, a live WebSocket stream, and a vessel map. The platform offers radar and satellite imagery, route change detection, zone alerts, and a developer portal with documentation, pricing, and support. It targets developers and businesses needing vessel position data for non‑commercial and commercial use.
image: https://pelyr.com/images/social-home.jpg
layout: provider
mcp_servers:
- description: Remote MCP server at api.pelyr.com.
  name: Pelyr MCP Server
  slug: pelyr-com-mcp-yml
modified: '2026-10-28'
name: Pelyr
nav: Providers
network: true
overview: 'Pelyr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Maritime, AIS, Data, and API.


  Pelyr''s developer surface includes documentation and 13 more developer resources.'
plans:
- name: Pelyr Com Plans Pricing
  plan_count: 9
  slug: pelyr-com-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 21.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Pelyr Com Domain Security
  slug: pelyr-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pelyr Com Vulnerability Disclosure
  slug: pelyr-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pelyr-com
tags:
- Company
- Maritime
- AIS
- Data
- API
website: https://pelyr.com
---
