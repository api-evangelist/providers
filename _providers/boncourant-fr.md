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
    agent_card: conformant
    agent_skills: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Boncourant Fr Agentic Access
  operation_count: 6
  slug: boncourant-fr-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- baseURL: https://boncourant.fr
  baseurl_source: declared
  description: The Audit API from Boncourant — 1 operation(s) for audit.
  name: Boncourant Audit API
  slug: boncourant-fr-audit-api
- baseURL: https://boncourant.fr
  baseurl_source: declared
  description: The Commissions API from Boncourant — 1 operation(s) for commissions.
  name: Boncourant Commissions API
  slug: boncourant-fr-commissions-api
- baseURL: https://boncourant.fr
  baseurl_source: declared
  description: The Mcp API from Boncourant — 1 operation(s) for mcp.
  name: Boncourant MCP API
  slug: boncourant-fr-mcp-api
- baseURL: https://boncourant.fr
  baseurl_source: declared
  description: The Simulate API from Boncourant — 2 operation(s) for simulate.
  name: Boncourant Simulate API
  slug: boncourant-fr-simulate-api
- baseURL: https://boncourant.fr
  baseurl_source: declared
  description: The Trv Gap API from Boncourant — 1 operation(s) for trv gap.
  name: Boncourant Trv Gap API
  slug: boncourant-fr-trv-gap-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/boncourant-fr/agentic-access/boncourant-fr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/boncourant-fr-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/boncourant-fr/rules/boncourant-fr-rules.yml
  title: ''
  type: Spectral
  url: rules/boncourant-fr-rules.yml
- group: design
  href: https://artifacts.apis.io/boncourant-fr/errors/boncourant-fr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/boncourant-fr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/boncourant-fr/conformance/boncourant-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boncourant-fr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boncourant-fr/llms/boncourant-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boncourant-fr-llms.txt
- group: other
  href: https://artifacts.apis.io/boncourant-fr/a2a/boncourant-fr-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/boncourant-fr-a2a.yml
- group: agent
  href: https://artifacts.apis.io/boncourant-fr/well-known/boncourant-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boncourant-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/boncourant-fr/hosts/boncourant-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boncourant-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/boncourant-fr/vendors/boncourant-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boncourant-fr-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://boncourant.fr/login
- group: auth
  href: https://artifacts.apis.io/boncourant-fr/security/boncourant-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boncourant-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boncourant.fr/
created: '2026-11-02'
description: Boncourant is an independent online service that audits electricity bills and optimizes tariffs for French households and businesses. It uses Enedis data, CRE and TURPE rates, providing a public, versioned methodology that calculates the optimal contract and subscribed power without being a supplier or comparator.
image: https://boncourant.fr/opengraph-image?2a74f574df36e069
layout: provider
modified: '2026-11-02'
name: Boncourant
nav: Providers
network: true
overview: 'Boncourant publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit API, Commissions API, MCP API, and 2 more. Tagged areas include Electricity, Audit, Optimization, France, and Independent.


  The Boncourant catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Boncourant API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: boncourant-fr-rules
score:
  band: emerging
  composite: 19.5
  coverage:
    artifact_dirs: 14
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 40.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - france
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - france-iberia
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 9.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Boncourant Fr Domain Security
  slug: boncourant-fr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: boncourant-fr
tags:
- Electricity
- Audit
- Optimization
- France
- Independent
website: https://boncourant.fr/
---
