---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://invokely.ai/api/v1
  baseurl_source: declared
  description: Official statistics REST API and MCP server providing data endpoints as described in the documentation.
  name: Invokely API
  slug: invokely-api
- baseURL: https://invokely.ai/api/v1
  baseurl_source: declared
  description: The Rank API from Invokely — 1 operation(s) for rank.
  name: Invokely Rank API
  slug: invokely-rank-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/invokely/plans/invokely-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/invokely-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/invokely/rules/invokely-rules.yml
  title: ''
  type: Spectral
  url: rules/invokely-rules.yml
- group: design
  href: https://artifacts.apis.io/invokely/conformance/invokely-conformance.yml
  title: ''
  type: Conformance
  url: conformance/invokely-conformance.yml
- group: agent
  href: https://artifacts.apis.io/invokely/llms/invokely-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/invokely-llms.txt
- group: agent
  href: https://artifacts.apis.io/invokely/mcp/invokely-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/invokely-mcp.yml
- group: agent
  href: https://artifacts.apis.io/invokely/well-known/invokely-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/invokely-well-known.yml
- group: other
  href: https://artifacts.apis.io/invokely/hosts/invokely-hosts.yml
  title: ''
  type: Hosts
  url: hosts/invokely-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://invokely.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://invokely.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://invokely.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://invokely.ai/login
- group: docs
  title: ''
  type: APIReference
  url: https://invokely.ai/docs
- group: auth
  href: https://artifacts.apis.io/invokely/security/invokely-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/invokely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://invokely.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://invokely.ai/docs/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://invokely.ai/openapi.json
  - status: 401
    url: https://invokely.ai/mcp
  - status: 200
    url: https://invokely.ai/
  reason: partner-login
  state: gated
created: '2026-10-12'
description: Invokely provides official statistics on population, GDP, inflation, employment, income, housing, AI adoption and related indicators for every country, U.S. state and county, EU region and other jurisdictions. The data are sourced from national statistics offices, central banks, Eurostat and the World Bank and are available for readers, AI assistants and anyone needing to cite official figures. Access is offered through a web interface, an MCP connector for Claude or ChatGPT, and a REST API.
image: https://invokely.ai/assets/images/og-default.f6f980f08a.png
layout: provider
mcp_servers:
- description: Remote MCP server at invokely.ai requiring an API key.
  name: Invokely MCP Server
  slug: invokely-mcp-yml
modified: '2026-10-12'
name: Invokely
nav: Providers
network: true
overview: 'Invokely is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Rank API, and 1 more. Tagged areas include Statistics, Economic Data, Public Data, and Data API.


  The Invokely catalog on APIs.io includes 1 Spectral governance ruleset.


  Invokely''s developer surface includes pricing, API reference, documentation, and 12 more developer resources.'
plans:
- name: Invokely Plans Pricing
  plan_count: 4
  slug: invokely-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Invokely API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: invokely-rules
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 48.5
    catalog_earned_first_party: 12.0
    catalog_gap: 66.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 10.4
    developer_ergonomics: 8.3
    discoverability: 66.7
    operational_transparency: 0.0
  previous_composite: 31.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/invokely/invokely-2026-11-03T134008.png
security:
- kind: domain-security
  name: Invokely Domain Security
  slug: invokely-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: invokely
tags:
- Statistics
- Economic Data
- Public Data
- Data API
website: https://invokely.ai/
---
