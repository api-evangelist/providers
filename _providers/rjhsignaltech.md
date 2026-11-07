---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Rjhsignaltech Agentic Access
  operation_count: 8
  slug: rjhsignaltech-agentic-access
  summary_line: 8 operations · 2 acting
api_count: 1
apis:
- description: API providing U.S. congressional and state legislative district lookup and officeholder info.
  name: Who Represents This Address API
  slug: who-represents-this-address-api
- baseURL: https://whorepresents.rjhsignaltech.workers.dev
  baseurl_source: declared
  description: The Batch API from Who Represents This Address (RJH Signal Technologies) — 1 operation(s) for batch.
  name: Who Represents This Address (RJH Signal Technologies) Batch API
  slug: rjhsignaltech-batch-api
- baseURL: https://whorepresents.rjhsignaltech.workers.dev
  baseurl_source: declared
  description: The Civicinfo API from Who Represents This Address (RJH Signal Technologies) — 2 operation(s) for civicinfo.
  name: Who Represents This Address (RJH Signal Technologies) Civicinfo API
  slug: rjhsignaltech-civicinfo-api
- baseURL: https://whorepresents.rjhsignaltech.workers.dev
  baseurl_source: declared
  description: The Divisions API from Who Represents This Address (RJH Signal Technologies) — 1 operation(s) for divisions.
  name: Who Represents This Address (RJH Signal Technologies) Divisions API
  slug: rjhsignaltech-divisions-api
- baseURL: https://whorepresents.rjhsignaltech.workers.dev
  baseurl_source: declared
  description: The Lookup API from Who Represents This Address (RJH Signal Technologies) — 1 operation(s) for lookup.
  name: Who Represents This Address (RJH Signal Technologies) Lookup API
  slug: rjhsignaltech-lookup-api
- baseURL: https://whorepresents.rjhsignaltech.workers.dev
  baseurl_source: declared
  description: The X402 API from Who Represents This Address (RJH Signal Technologies) — 1 operation(s) for x402.
  name: Who Represents This Address (RJH Signal Technologies) X402 API
  slug: rjhsignaltech-x402-api
- baseURL: https://whorepresents.rjhsignaltech.workers.dev
  baseurl_source: declared
  description: The Zip API from Who Represents This Address (RJH Signal Technologies) — 1 operation(s) for zip.
  name: Who Represents This Address (RJH Signal Technologies) Zip API
  slug: rjhsignaltech-zip-api
artifact_total: 13
common:
- group: other
  href: https://artifacts.apis.io/rjhsignaltech/overlays/rjhsignaltech-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rjhsignaltech-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/rjhsignaltech/mcp/rjhsignaltech-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rjhsignaltech-mcp.yml
- group: agent
  href: https://artifacts.apis.io/rjhsignaltech/agentic-access/rjhsignaltech-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rjhsignaltech-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/rjhsignaltech/rules/rjhsignaltech-rules.yml
  title: ''
  type: Spectral
  url: rules/rjhsignaltech-rules.yml
- group: agent
  href: https://artifacts.apis.io/rjhsignaltech/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/rjhsignaltech/errors/rjhsignaltech-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rjhsignaltech-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rjhsignaltech/conformance/rjhsignaltech-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rjhsignaltech-conformance.yml
- group: other
  href: https://artifacts.apis.io/rjhsignaltech/hosts/rjhsignaltech-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rjhsignaltech-hosts.yml
- group: other
  href: https://artifacts.apis.io/rjhsignaltech/vendors/rjhsignaltech-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rjhsignaltech-vendors.yml
- group: auth
  href: https://artifacts.apis.io/rjhsignaltech/security/rjhsignaltech-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rjhsignaltech-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/rjhsignaltech/authentication/rjhsignaltech-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rjhsignaltech-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://whorepresents.rjhsignaltech.workers.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://whorepresents.rjhsignaltech.workers.dev/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://whorepresents.rjhsignaltech.workers.dev/#pricing
- group: operate
  title: ''
  type: Support
  url: mailto:rjhsignaltech@gmail.com
created: '2026-09-25'
description: Who Represents This Address (RJH Signal Technologies) provides an AI‑operated API that returns U.S. congressional and state legislative districts, current officeholders, statewide executives, mayoral information, and local boundaries for a given street address. It serves as a drop‑in replacement for the discontinued Google Civic Information API, offering free tier access and paid per‑call options, with batch lookup support for up to 40 addresses.
layout: provider
mcp_servers:
- description: Remote MCP server at whorepresents.rjhsignaltech.workers.dev.
  name: Who Represents This Address (RJH Signal Technologies) MCP Server
  slug: rjhsignaltech-mcp-yml
modified: '2026-09-25'
name: Who Represents This Address (RJH Signal Technologies)
nav: Providers
network: true
overview: 'Who Represents This Address (RJH Signal Technologies) publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch API, Civicinfo API, Divisions API, and 4 more. Tagged areas include Company, Civic, Government, and Address.


  The Who Represents This Address (RJH Signal Technologies) catalog on APIs.io includes 1 Spectral governance ruleset.


  Who Represents This Address (RJH Signal Technologies)''s developer surface includes authentication, API reference, pricing, support, and 11 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Who Represents This Address (RJH Signal Technologies) API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: rjhsignaltech-rules
score:
  band: emerging
  composite: 25.5
  coverage:
    artifact_dirs: 15
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 49.4
    developer_ergonomics: 22.0
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 27.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: unknown
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/rjhsignaltech/rjhsignaltech-2026-10-11T125337.png
security:
- kind: authentication
  name: Rjhsignaltech Authentication
  slug: rjhsignaltech-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rjhsignaltech Domain Security
  slug: rjhsignaltech-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: rjhsignaltech-x402-lookup
  slug: rjhsignaltech-x402-lookup
slug: rjhsignaltech
tags:
- Company
- Civic
- Government
- Address
website: https://whorepresents.rjhsignaltech.workers.dev/
---
