---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- baseURL: https://crossandcovenant.co
  baseurl_source: declared
  description: Programmatic catalog, recommendation, devotional, and one‑tap cart API for Cross + Covenant.
  name: Cross + Covenant Agent API
  slug: agent-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/crossandcovenant-co/rules/crossandcovenant-co-rules.yml
  title: ''
  type: Spectral
  url: rules/crossandcovenant-co-rules.yml
- group: auth
  href: https://artifacts.apis.io/crossandcovenant-co/security/crossandcovenant-co-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/crossandcovenant-co-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/crossandcovenant-co/errors/crossandcovenant-co-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crossandcovenant-co-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crossandcovenant-co/conformance/crossandcovenant-co-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crossandcovenant-co-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crossandcovenant-co/llms/crossandcovenant-co-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crossandcovenant-co-llms.txt
- group: build
  href: https://artifacts.apis.io/crossandcovenant-co/mcp/crossandcovenant-co-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/crossandcovenant-co-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/crossandcovenant-co/mcp/crossandcovenant-co-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crossandcovenant-co-mcp.yml
- group: auth
  href: https://artifacts.apis.io/crossandcovenant-co/well-known/crossandcovenant-co-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crossandcovenant-co-security.txt
- group: agent
  href: https://artifacts.apis.io/crossandcovenant-co/well-known/crossandcovenant-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crossandcovenant-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/crossandcovenant-co/hosts/crossandcovenant-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crossandcovenant-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/crossandcovenant-co/vendors/crossandcovenant-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crossandcovenant-co-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://crossandcovenant.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://crossandcovenant.co/privacy
- group: auth
  href: https://artifacts.apis.io/crossandcovenant-co/security/crossandcovenant-co-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crossandcovenant-co-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crossandcovenant-co/security/crossandcovenant-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crossandcovenant-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crossandcovenant.co/
created: '2026-10-29'
description: Cross + Covenant is a faith‑focused apparel brand offering Christian‑themed t‑shirts, hoodies, and streetwear that spark conversations about Jesus. Their products feature scripture‑inspired designs and each purchase supports mission work, with 10 % of sales funding a monthly charity. The online store also provides a free Bible and daily devotional content, aiming to spread the gospel through fashion and digital resources. Founded in 2025 and based in Kalispell, Montana, the company serves customers across the United States.
image: https://crossandcovenant.co/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at crossandcovenant.co.
  name: crossandcovenant-co MCP Server
  slug: crossandcovenant-co-mcp-yml
modified: '2026-10-29'
name: crossandcovenant-co
nav: Providers
network: true
overview: 'crossandcovenant-co publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Cross + Covenant Agent API. Tagged areas include Apparel, Christian, E‑commerce, Faith, and Charity.


  The crossandcovenant-co catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: crossandcovenant-co API Rules
  rule_count: 13
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 0
  slug: crossandcovenant-co-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 13
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 15.9
    contract_quality: 42.2
    developer_ergonomics: 9.5
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crossandcovenant Co Domain Security
  slug: crossandcovenant-co-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crossandcovenant Co Vulnerability Disclosure
  slug: crossandcovenant-co-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crossandcovenant-co
tags:
- Apparel
- Christian
- E‑commerce
- Faith
- Charity
website: https://crossandcovenant.co/
---
