---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Elliat Nl Agentic Access
  operation_count: 4
  slug: elliat-nl-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Plain HTTP access to the Fonto XML documentation, converted to Markdown.
  name: Fonto Docs API
  slug: fonto-docs-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/elliat-nl/agentic-access/elliat-nl-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/elliat-nl-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/elliat-nl/rules/elliat-nl-rules.yml
  title: ''
  type: Spectral
  url: rules/elliat-nl-rules.yml
- group: agent
  href: https://artifacts.apis.io/elliat-nl/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/elliat-nl/components/elliat-nl-components.yml
  title: ''
  type: Components
  url: components/elliat-nl-components.yml
- group: design
  href: https://artifacts.apis.io/elliat-nl/errors/elliat-nl-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/elliat-nl-problem-types.yml
- group: design
  href: https://artifacts.apis.io/elliat-nl/conformance/elliat-nl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/elliat-nl-conformance.yml
- group: agent
  href: https://artifacts.apis.io/elliat-nl/llms/elliat-nl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/elliat-nl-llms.txt
- group: build
  href: https://artifacts.apis.io/elliat-nl/mcp/elliat-nl-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/elliat-nl-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/elliat-nl/mcp/elliat-nl-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/elliat-nl-mcp.yml
- group: agent
  href: https://artifacts.apis.io/elliat-nl/well-known/elliat-nl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/elliat-nl-well-known.yml
- group: other
  href: https://artifacts.apis.io/elliat-nl/hosts/elliat-nl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/elliat-nl-hosts.yml
- group: other
  href: https://artifacts.apis.io/elliat-nl/vendors/elliat-nl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/elliat-nl-vendors.yml
- group: auth
  href: https://artifacts.apis.io/elliat-nl/security/elliat-nl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/elliat-nl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://elliat.nl/
- group: docs
  title: ''
  type: Documentation
  url: https://fonto-docs.elliat.nl/
created: '2026-10-30'
description: Elliat is an independent developer brand operated by Martin Middel, specializing in JavaScript and XML technologies. Offering expertise in Fonto XML Editor, FontoXPath, and related standards, Elliat provides consulting, custom development, and open‑source tools such as an MCP server that makes Fonto documentation AI‑readable. The site showcases projects, a portfolio of XML‑related work, and contact information for hiring the developer.
image: https://elliat.nl/favicon.png
layout: provider
mcp_servers:
- description: Remote MCP server at fonto-docs.elliat.nl.
  name: elliat-nl MCP Server
  slug: elliat-nl-mcp-yml
modified: '2026-10-30'
name: elliat-nl
nav: Providers
network: true
overview: 'elliat-nl is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Developer, JavaScript, XML, and Fonto.


  The elliat-nl catalog on APIs.io includes 1 Spectral governance ruleset.


  elliat-nl''s developer surface includes documentation and 14 more developer resources.'
plans:
- name: Elliat Nl Plans Pricing
  plan_count: 0
  slug: elliat-nl-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Elliat Nl Rate Limits
  slug: elliat-nl-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: elliat-nl API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: elliat-nl-rules
scopes:
- name: Elliat Nl Scopes
  scope_count: 0
  slug: elliat-nl-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 65.5
    contract_quality: 0.0
    developer_ergonomics: 16.0
    discoverability: 65.0
    operational_transparency: 0.0
  regulatory:
    applies: true
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
- kind: authentication
  name: Elliat Nl Authentication
  slug: elliat-nl-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Elliat Nl Domain Security
  slug: elliat-nl-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 4
skills:
- name: get-fonto-page
  slug: elliat-nl-get-fonto-page
- name: list-pages
  slug: elliat-nl-list-pages
- name: lookup-api
  slug: elliat-nl-lookup-api
- name: search-fonto-docs
  slug: elliat-nl-search-fonto-docs
slug: elliat-nl
tags:
- Company
- Developer
- JavaScript
- XML
- Fonto
- Consulting
website: https://elliat.nl/
---
