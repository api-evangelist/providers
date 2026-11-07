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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Afbudsrejser Dk Agentic Access
  operation_count: 1
  slug: afbudsrejser-dk-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Search for available package trips including flights and accommodation departing from Denmark, returning current prices, availability, hotel info and booking links.
  name: afbudsrejser.dk API
  slug: afbudsrejser-dk-api
- baseURL: https://www.afbudsrejser.dk/services/charter/api_search
  baseurl_source: declared
  description: The Services API from afbudsrejser.dk — 1 operation(s) for services.
  name: afbudsrejser.dk Services API
  slug: afbudsrejser-dk-services-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/afbudsrejser-dk/agentic-access/afbudsrejser-dk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/afbudsrejser-dk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/afbudsrejser-dk/rules/afbudsrejser-dk-rules.yml
  title: ''
  type: Spectral
  url: rules/afbudsrejser-dk-rules.yml
- group: agent
  href: https://artifacts.apis.io/afbudsrejser-dk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/afbudsrejser-dk/errors/afbudsrejser-dk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/afbudsrejser-dk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/afbudsrejser-dk/conformance/afbudsrejser-dk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/afbudsrejser-dk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/afbudsrejser-dk/llms/afbudsrejser-dk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/afbudsrejser-dk-llms.txt
- group: build
  href: https://artifacts.apis.io/afbudsrejser-dk/mcp/afbudsrejser-dk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/afbudsrejser-dk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/afbudsrejser-dk/mcp/afbudsrejser-dk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/afbudsrejser-dk-mcp.yml
- group: other
  href: https://artifacts.apis.io/afbudsrejser-dk/hosts/afbudsrejser-dk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/afbudsrejser-dk-hosts.yml
- group: auth
  href: https://artifacts.apis.io/afbudsrejser-dk/security/afbudsrejser-dk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afbudsrejser-dk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://afbudsrejser.dk/
coverage:
  checked: '2026-11-01'
  detail: Provider's website hosts OpenAPI files but they describe a different product (Reisegiganten) not afbudsrejser.dk.
  evidence:
  - status: 200
    url: https://www.afbudsrejser.dk/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Afbudsrejser.dk is a Danish online marketplace that allows users to compare and book charter and package trips, flights, and hotels in one place. It aggregates offers from major travel operators, providing a convenient platform for finding charter flights, package holidays, and hotel accommodations across Denmark and beyond.
layout: provider
mcp_servers:
- description: Remote MCP server at www.afbudsrejser.dk.
  name: afbudsrejser.dk MCP Server
  slug: afbudsrejser-dk-mcp-yml
modified: '2026-10-31'
name: afbudsrejser.dk
nav: Providers
network: true
overview: 'afbudsrejser.dk publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Services API, and 1 more. Tagged areas include Travel, Marketplace, Denmark, Charter, and Packages.


  The afbudsrejser.dk catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: afbudsrejser.dk API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: afbudsrejser-dk-rules
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 14
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 49.6
    developer_ergonomics: 1.8
    discoverability: 53.3
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - denmark
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 19.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afbudsrejser Dk Domain Security
  slug: afbudsrejser-dk-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: holiday-search
  slug: afbudsrejser-dk-holiday-search
slug: afbudsrejser-dk
tags:
- Travel
- Marketplace
- Denmark
- Charter
- Packages
website: https://afbudsrejser.dk/
---
