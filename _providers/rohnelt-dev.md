---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
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
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Rohnelt Dev Agentic Access
  operation_count: 1
  slug: rohnelt-dev-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 2
apis:
- description: Cálculos informativos brasileiros de 2026. Free tier 500 calls/day per IP.
  name: Conta Clara API
  slug: conta-clara-api
- description: 20 data lines processed in memory without storage. Free tier.
  name: CSV Repair free sample API
  slug: csv-repair-free-sample-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/rohnelt-dev/agentic-access/rohnelt-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rohnelt-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/rohnelt-dev/plans/rohnelt-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rohnelt-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/rohnelt-dev/rules/rohnelt-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/rohnelt-dev-rules.yml
- group: agent
  href: https://artifacts.apis.io/rohnelt-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/rohnelt-dev/conventions/rohnelt-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/rohnelt-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/rohnelt-dev/conventions/rohnelt-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rohnelt-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/rohnelt-dev/errors/rohnelt-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rohnelt-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rohnelt-dev/conformance/rohnelt-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rohnelt-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rohnelt-dev/llms/rohnelt-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rohnelt-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/rohnelt-dev/mcp/rohnelt-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/rohnelt-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/rohnelt-dev/mcp/rohnelt-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rohnelt-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/rohnelt-dev/well-known/rohnelt-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rohnelt-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/rohnelt-dev/hosts/rohnelt-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rohnelt-dev-hosts.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/phillypmack
- group: docs
  title: ''
  type: APIReference
  url: https://api.rohnelt.dev/docs
- group: auth
  href: https://artifacts.apis.io/rohnelt-dev/security/rohnelt-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rohnelt-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rohnelt.dev/
- group: operate
  title: ''
  type: Support
  url: https://rohnelt.dev/#contato
created: '2026-10-29'
description: Rohnelt-dev is the professional brand of Felipe Rohnelt, a software engineer specializing in end‑to‑end systems for industry, logistics and digital products. Based in Goiás, Brazil, the portfolio showcases over twenty‑three production systems, including public services and private client deployments, integrating ERP, databases, IoT hardware and cloud services. The site presents methodology, results, and a contact channel for consulting projects, reflecting a focus on operational excellence and measurable outcomes.
image: https://rohnelt.dev/opengraph-image?a02ec85dd84b1463
layout: provider
mcp_servers:
- description: Remote MCP server at api.rohnelt.dev.
  name: rohnelt-dev MCP Server
  slug: rohnelt-dev-mcp-yml
modified: '2026-10-29'
name: rohnelt-dev
nav: Providers
network: true
overview: 'rohnelt-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Software Engineering, Consulting, Brazil, Logistics, and Industry.


  The rohnelt-dev catalog on APIs.io includes 1 Spectral governance ruleset.


  rohnelt-dev''s developer surface includes API reference, support, and 16 more developer resources.'
plans:
- name: Rohnelt Dev Plans Pricing
  plan_count: 1
  slug: rohnelt-dev-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Rohnelt Dev Rate Limits
  slug: rohnelt-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: rohnelt-dev API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: rohnelt-dev-rules
scopes:
- name: Rohnelt Dev Scopes
  scope_count: 0
  slug: rohnelt-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 24
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.7
    discoverability: 75.0
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - brazil
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.2
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rohnelt-dev/rohnelt-dev-2026-11-03T142358.png
security:
- kind: authentication
  name: Rohnelt Dev Authentication
  slug: rohnelt-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rohnelt Dev Domain Security
  slug: rohnelt-dev-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: repair-csv
  slug: rohnelt-dev-repair-csv
slug: rohnelt-dev
tags:
- Software Engineering
- Consulting
- Brazil
- Logistics
- Industry
website: https://rohnelt.dev/
---
