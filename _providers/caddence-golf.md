---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
  score: 0.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for golf product data from UK retailers
  name: Golf Product API
  slug: golf-product-api
artifact_total: 4
common:
- group: auth
  href: https://artifacts.apis.io/caddence-golf/security/caddence-golf-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/caddence-golf-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/caddence-golf/conformance/caddence-golf-conformance.yml
  title: ''
  type: Conformance
  url: conformance/caddence-golf-conformance.yml
- group: agent
  href: https://artifacts.apis.io/caddence-golf/llms/caddence-golf-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caddence-golf-llms.txt
- group: agent
  href: https://artifacts.apis.io/caddence-golf/mcp/caddence-golf-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/caddence-golf-mcp.yml
- group: auth
  href: https://artifacts.apis.io/caddence-golf/well-known/caddence-golf-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/caddence-golf-security.txt
- group: agent
  href: https://artifacts.apis.io/caddence-golf/well-known/caddence-golf-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/caddence-golf-well-known.yml
- group: other
  href: https://artifacts.apis.io/caddence-golf/hosts/caddence-golf-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caddence-golf-hosts.yml
- group: other
  href: https://artifacts.apis.io/caddence-golf/vendors/caddence-golf-vendors.yml
  title: ''
  type: Vendors
  url: vendors/caddence-golf-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://caddence.golf/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caddence.golf/privacy
- group: auth
  href: https://artifacts.apis.io/caddence-golf/security/caddence-golf-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/caddence-golf-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/caddence-golf/security/caddence-golf-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caddence-golf-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caddence.golf/
created: '2026-11-03'
description: Caddence provides a platform to compare golf equipment prices and price history across UK retailers. It aggregates data from over 40 retailers, covering new and used clubs, and updates daily to help golfers find the best deals. The service offers price tracking, historical trends, and alerts, aiming to simplify equipment shopping for enthusiasts and professionals alike.
image: https://caddence.golf/og/home.png
layout: provider
mcp_servers:
- description: Remote MCP server at caddence.golf.
  name: Caddence MCP Server
  slug: caddence-golf-mcp-yml
modified: '2026-11-03'
name: Caddence
nav: Providers
network: true
overview: Caddence is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Golf, Price Comparison, Retail, Data Analytics, and United Kingdom.
random_paper: 4
score:
  band: emerging
  composite: 11.3
  coverage:
    artifact_dirs: 9
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caddence Golf Domain Security
  slug: caddence-golf-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Caddence Golf Vulnerability Disclosure
  slug: caddence-golf-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: caddence-golf
tags:
- Golf
- Price Comparison
- Retail
- Data Analytics
- United Kingdom
website: https://caddence.golf/
---
