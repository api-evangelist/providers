---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 30.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Indicative US personal auto insurance pricing API for Nevada consumers.
  name: Nevada Insurance API
  slug: nevada-insurance-api
- baseURL: https://nevadaautoquotes.com
  baseurl_source: declared
  description: 'Nevada Insurance: Indicative US personal auto insurance prices for AI agents acting on behalf of a consumer in Nevada, and a consented path to licensed agents. Call /v1/eligibility first. Read /v1/ter'
  name: Nevada Insurance Api API
  slug: nevada-insurance-api-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/nevadaautoquotes-com/rules/nevadaautoquotes-com-rules.yml
  title: ''
  type: Spectral
  url: rules/nevadaautoquotes-com-rules.yml
- group: design
  href: https://artifacts.apis.io/nevadaautoquotes-com/conformance/nevadaautoquotes-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nevadaautoquotes-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nevadaautoquotes-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/nevadaautoquotes-com/errors/nevadaautoquotes-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nevadaautoquotes-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/nevadaautoquotes-com/llms/nevadaautoquotes-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nevadaautoquotes-com-llms.txt
- group: other
  href: https://artifacts.apis.io/nevadaautoquotes-com/a2a/nevadaautoquotes-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/nevadaautoquotes-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/nevadaautoquotes-com/mcp/nevadaautoquotes-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/nevadaautoquotes-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/nevadaautoquotes-com/mcp/nevadaautoquotes-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nevadaautoquotes-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/nevadaautoquotes-com/well-known/nevadaautoquotes-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nevadaautoquotes-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/nevadaautoquotes-com/hosts/nevadaautoquotes-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nevadaautoquotes-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/nevadaautoquotes-com/vendors/nevadaautoquotes-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nevadaautoquotes-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/nevadaautoquotes-com/security/nevadaautoquotes-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nevadaautoquotes-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nevadaautoquotes.com/
- group: docs
  title: ''
  type: Documentation
  url: https://nevadaautoquotes.com/openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://nevadaautoquotes.com/openapi.json
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nevadaautoquotes.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nevadaautoquotes.com/v1/terms
created: '2026-10-30'
description: Nevada Auto Quotes provides indicative personal auto insurance pricing for consumers in Nevada. The platform aggregates rates from multiple licensed insurers and presents them to AI agents and end‑users without requiring personal contact details upfront. Users can compare quotes across carriers, and licensed agents may follow up with full quotes after consent. The service operates under Nevada state regulations and aims to simplify auto insurance shopping through a transparent, consent‑driven interface.
layout: provider
mcp_servers:
- description: Remote MCP server at nevadaautoquotes.com.
  name: nevadaautoquotes-com MCP Server
  slug: nevadaautoquotes-com-mcp-yml
modified: '2026-10-30'
name: nevadaautoquotes-com
nav: Providers
network: true
overview: 'nevadaautoquotes-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Nevada Insurance Api API, and 1 more. Tagged areas include Company, AutoInsurance, Nevada, Quotes, and AI.


  The nevadaautoquotes-com catalog on APIs.io includes 1 Spectral governance ruleset.


  nevadaautoquotes-com''s developer surface includes documentation, API reference, and 15 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: nevadaautoquotes-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: nevadaautoquotes-com-rules
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 15
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 75.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 38.6
    developer_ergonomics: 23.1
    discoverability: 61.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nevadaautoquotes Com Domain Security
  slug: nevadaautoquotes-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: nevadaautoquotes-com
tags:
- Company
- AutoInsurance
- Nevada
- Quotes
- AI
website: https://nevadaautoquotes.com/
---
