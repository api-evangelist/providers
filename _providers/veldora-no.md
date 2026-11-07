---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Veldora No Agentic Access
  operation_count: 44
  slug: veldora-no-agentic-access
  summary_line: 44 operations · 4 acting
api_count: 1
apis:
- baseURL: https://veldora.no
  baseurl_source: declared
  description: The Addresses API from veldora-no — 2 operation(s) for addresses.
  name: veldora-no Addresses API
  slug: veldora-no-addresses-api
- baseURL: https://veldora.no
  baseurl_source: declared
  description: The Alerts API from veldora-no — 2 operation(s) for alerts.
  name: veldora-no Alerts API
  slug: veldora-no-alerts-api
- baseURL: https://veldora.no
  baseurl_source: declared
  description: The Companies API from veldora-no — 5 operation(s) for companies.
  name: veldora-no Companies API
  slug: veldora-no-companies-api
- baseURL: https://veldora.no
  baseurl_source: declared
  description: The Exchange Rates API from veldora-no — 1 operation(s) for exchange rates.
  name: veldora-no Exchange Rates API
  slug: veldora-no-exchange-rates-api
- baseURL: https://veldora.no
  baseurl_source: declared
  description: The Fi API from veldora-no — 2 operation(s) for fi.
  name: veldora-no Fi API
  slug: veldora-no-fi-api
- baseURL: https://veldora.no
  baseurl_source: declared
  description: The Health API from veldora-no — 1 operation(s) for health.
  name: veldora-no Health API
  slug: veldora-no-health-api
- baseURL: https://veldora.no
  baseurl_source: declared
  description: The Laws API from veldora-no — 3 operation(s) for laws.
  name: veldora-no Laws API
  slug: veldora-no-laws-api
- baseURL: https://veldora.no
  baseurl_source: declared
  description: The Statistics API from veldora-no — 3 operation(s) for statistics.
  name: veldora-no Statistics API
  slug: veldora-no-statistics-api
- baseURL: https://veldora.no
  baseurl_source: declared
  description: The Tenders API from veldora-no — 2 operation(s) for tenders.
  name: veldora-no Tenders API
  slug: veldora-no-tenders-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/veldora-no/agentic-access/veldora-no-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/veldora-no-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/veldora-no/rate-limits/veldora-no-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/veldora-no-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/veldora-no/rules/veldora-no-rules.yml
  title: ''
  type: Spectral
  url: rules/veldora-no-rules.yml
- group: design
  href: https://artifacts.apis.io/veldora-no/json-ld/veldora-no-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/veldora-no-context.jsonld
- group: design
  href: https://artifacts.apis.io/veldora-no/vocabulary/veldora-no-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/veldora-no-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/veldora-no/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/veldora-no/data-model/veldora-no-data-model.yml
  title: ''
  type: DataModel
  url: data-model/veldora-no-data-model.yml
- group: build
  href: https://artifacts.apis.io/veldora-no/cli/veldora-no-cli.yml
  title: ''
  type: CLI
  url: cli/veldora-no-cli.yml
- group: design
  href: https://artifacts.apis.io/veldora-no/conventions/veldora-no-conventions.yml
  title: ''
  type: Conventions
  url: conventions/veldora-no-conventions.yml
- group: auth
  href: https://artifacts.apis.io/veldora-no/authentication/veldora-no-authentication.yml
  title: ''
  type: Authentication
  url: authentication/veldora-no-authentication.yml
- group: operate
  href: https://artifacts.apis.io/veldora-no/lifecycle/veldora-no-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/veldora-no-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://veldora.no/v1/health
- group: design
  href: https://artifacts.apis.io/veldora-no/lifecycle/veldora-no-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/veldora-no-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/veldora-no/errors/veldora-no-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/veldora-no-problem-types.yml
- group: design
  href: https://artifacts.apis.io/veldora-no/conformance/veldora-no-conformance.yml
  title: ''
  type: Conformance
  url: conformance/veldora-no-conformance.yml
- group: agent
  href: https://artifacts.apis.io/veldora-no/llms/veldora-no-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/veldora-no-llms.txt
- group: build
  href: https://artifacts.apis.io/veldora-no/mcp/veldora-no-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/veldora-no-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/veldora-no/mcp/veldora-no-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/veldora-no-mcp.yml
- group: other
  href: https://artifacts.apis.io/veldora-no/hosts/veldora-no-hosts.yml
  title: ''
  type: Hosts
  url: hosts/veldora-no-hosts.yml
- group: other
  href: https://artifacts.apis.io/veldora-no/vendors/veldora-no-vendors.yml
  title: ''
  type: Vendors
  url: vendors/veldora-no-vendors.yml
- group: build
  href: https://artifacts.apis.io/veldora-no/packages/veldora-no-packages.yml
  title: ''
  type: SDKs
  url: packages/veldora-no-packages.yml
- group: build
  href: https://artifacts.apis.io/veldora-no/packages/veldora-no-packages.yml
  title: ''
  type: Packages
  url: packages/veldora-no-packages.yml
- group: auth
  href: https://artifacts.apis.io/veldora-no/security/veldora-no-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/veldora-no-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://veldora.no/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://veldora.no/docs
- group: docs
  title: ''
  type: Documentation
  url: https://veldora.no/docs
- group: docs
  title: ''
  type: APIReference
  url: https://veldora.no/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://veldora.no/docs#quickstart
- group: operate
  title: ''
  type: Support
  url: https://veldora.no/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://veldora.no/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://veldora.no/personvern
created: '2026-10-31'
description: Veldora provides a paid data API for AI agents, delivering cleaned Norwegian company information, public tenders, contract awards, addresses, laws, exchange rates, and statistics sourced from Brønnøysundregistrene, Doffin, TED, Kartverket, Lovdata, Norges Bank, SSB, and Finnish companies from PRH. Payments are made per request in USDC on Base via x402, with no account or API key required.
image: https://veldora.no/og.png
jsonld:
- class_count: 2
  name: Veldora No Context
  property_count: 5
  slug: veldora-no-context
layout: provider
mcp_servers:
- description: Remote MCP server at veldora.no.
  name: veldora-no MCP Server
  slug: veldora-no-mcp-yml
modified: '2026-10-31'
name: veldora-no
nav: Providers
network: true
overview: 'veldora-no publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Addresses API, Alerts API, Companies API, and 6 more. Tagged areas include Company, Data, Norway, Artificial Intelligence, and Public Data.


  The veldora-no catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  veldora-no''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, support, pricing, and 24 more developer resources.'
plans:
- name: Veldora No Plans Pricing
  plan_count: 0
  slug: veldora-no-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Veldora No Rate Limits
  slug: veldora-no-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: veldora-no API Rules
  rule_count: 16
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 2
  slug: veldora-no-rules
scopes:
- name: Veldora No Scopes
  scope_count: 0
  slug: veldora-no-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 41.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 55.8
    catalog_earned_first_party: 8.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 10.5
    contract_governance: 35.6
    contract_quality: 49.7
    developer_ergonomics: 49.4
    discoverability: 65.0
    operational_transparency: 36.8
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - norway
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 49.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Veldora No Authentication
  slug: veldora-no-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Veldora No Domain Security
  slug: veldora-no-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: get-company
  slug: veldora-no-get-company
slug: veldora-no
tags:
- Company
- Data
- Norway
- Artificial Intelligence
- Public Data
website: https://veldora.no/
---
