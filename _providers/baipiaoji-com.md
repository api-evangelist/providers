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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 7.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Free-tier AI tools directory API
  name: Baipiaoji API
  slug: baipiaoji-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/baipiaoji-com/rules/baipiaoji-com-rules.yml
  title: ''
  type: Spectral
  url: rules/baipiaoji-com-rules.yml
- group: design
  href: https://artifacts.apis.io/baipiaoji-com/errors/baipiaoji-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/baipiaoji-com-problem-types.yml
- group: commercial
  href: https://artifacts.apis.io/baipiaoji-com/plans/baipiaoji-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/baipiaoji-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/baipiaoji-com/conformance/baipiaoji-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/baipiaoji-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/baipiaoji-com/llms/baipiaoji-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/baipiaoji-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/baipiaoji-com/mcp/baipiaoji-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/baipiaoji-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/baipiaoji-com/well-known/baipiaoji-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/baipiaoji-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/baipiaoji-com/hosts/baipiaoji-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/baipiaoji-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/baipiaoji-com/vendors/baipiaoji-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/baipiaoji-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://baipiaoji.com/ai-solo/compare/support/
- group: commercial
  title: ''
  type: Pricing
  url: https://baipiaoji.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.cloudflare.com/workers-ai/?utm_source=baipiaoji
- group: auth
  href: https://artifacts.apis.io/baipiaoji-com/security/baipiaoji-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/baipiaoji-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://baipiaoji.com/
created: '2026-10-29'
description: baipiaoji-com operates a Chinese-language platform that aggregates free AI tools, quota comparisons, and practical toolboxes for developers and end‑users. The site curates AI services, provides detailed usage limits, commercial terms, and offers a catalog of over 700 third‑party tools with verified free tiers. It also hosts a developer API directory, guides on integrating AI models, and resources for building agents and MCP (Machine‑Centric Platforms). The platform emphasizes transparency, source verification, and regular updates to ensure users can quickly find cost‑effective AI solutions.
layout: provider
mcp_servers:
- description: Remote MCP server at baipiaoji.com.
  name: baipiaoji-com MCP Server
  slug: baipiaoji-com-mcp-yml
modified: '2026-10-29'
name: baipiaoji-com
nav: Providers
network: true
overview: 'baipiaoji-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Tools, Directory, and Chinese.


  The baipiaoji-com catalog on APIs.io includes 1 Spectral governance ruleset.


  baipiaoji-com''s developer surface includes support, pricing, and 12 more developer resources.'
plans:
- name: Baipiaoji Com Plans Pricing
  plan_count: 2
  slug: baipiaoji-com-plans-pricing
random_paper: 4
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: baipiaoji-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: baipiaoji-com-rules
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 47.5
    catalog_earned_first_party: 8.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 6.0
    developer_ergonomics: 14.3
    discoverability: 61.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Baipiaoji Com Domain Security
  slug: baipiaoji-com-domain-security
  summary_line: TLSv1.3
slug: baipiaoji-com
tags:
- Company
- AI
- Tools
- Directory
- Chinese
website: https://baipiaoji.com/
---
