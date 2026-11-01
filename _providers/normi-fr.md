---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Normi Fr Agentic Access
  operation_count: 1
  slug: normi-fr-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: API REST for French property transaction data (DVF)
  name: Normi DVF API
  slug: normi-dvf-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/normi-fr/agentic-access/normi-fr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/normi-fr-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/normi-fr/plans/normi-fr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/normi-fr-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/normi-fr/rules/normi-fr-rules.yml
  title: ''
  type: Spectral
  url: rules/normi-fr-rules.yml
- group: design
  href: https://artifacts.apis.io/normi-fr/vocabulary/normi-fr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/normi-fr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/normi-fr/conventions/normi-fr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/normi-fr-conventions.yml
- group: auth
  href: https://artifacts.apis.io/normi-fr/authentication/normi-fr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/normi-fr-authentication.yml
- group: design
  href: https://artifacts.apis.io/normi-fr/conformance/normi-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/normi-fr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/normi-fr/llms/normi-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/normi-fr-llms.txt
- group: build
  href: https://artifacts.apis.io/normi-fr/mcp/normi-fr-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/normi-fr-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/normi-fr/mcp/normi-fr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/normi-fr-mcp.yml
- group: agent
  href: https://artifacts.apis.io/normi-fr/well-known/normi-fr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/normi-fr-well-known.yml
- group: other
  href: https://artifacts.apis.io/normi-fr/hosts/normi-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/normi-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/normi-fr/vendors/normi-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/normi-fr-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.normi.fr/auth/login
- group: auth
  href: https://artifacts.apis.io/normi-fr/security/normi-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/normi-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://normi.fr/
- group: docs
  title: ''
  type: Documentation
  url: https://www.normi.fr/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.normi.fr/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.normi.fr/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.normi.fr/explorer-prix
- group: other
  title: ''
  type: Comparatif
  url: https://www.normi.fr/comparatif-api-dvf
created: '2026-10-30'
description: Normi provides French real‑estate data APIs, offering access to over 18 million DVF (property transaction) records and 13 million DPE (energy diagnostic) entries since 2014. The REST and MCP endpoints enable developers to query property prices, energy performance, green‑prime eligibility, and thermal‑pass‑through statistics by commune, department or region. Free trial available, with paid plans for higher volume and commercial use.
image: https://www.normi.fr/opengraph-image?2b3d2b3f12e1648a
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.normi.fr.
  name: normi-fr MCP Server
  slug: normi-fr-mcp-yml
modified: '2026-10-30'
name: normi-fr
nav: Providers
network: true
overview: 'normi-fr is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Data API, French Market, and Property Transactions.


  The normi-fr catalog on APIs.io includes 1 Spectral governance ruleset.


  normi-fr''s developer surface includes authentication, documentation, pricing, engineering blog, getting-started guide, and 16 more developer resources.'
plans:
- name: Normi Fr Plans Pricing
  plan_count: 4
  slug: normi-fr-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: normi-fr API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: normi-fr-rules
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 68.5
    catalog_earned_first_party: 0.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.1
    contract_governance: 79.1
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 65.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Normi Fr Authentication
  slug: normi-fr-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Normi Fr Domain Security
  slug: normi-fr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: normi-fr
tags:
- Company
- Real Estate
- Data API
- French Market
- Property Transactions
website: https://normi.fr/
---
