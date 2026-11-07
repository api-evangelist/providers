---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
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
  score: 8.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Akkilahdot Fi Agentic Access
  operation_count: 2
  slug: akkilahdot-fi-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Hae saatavilla olevia pakettimatkoja, jotka sisältävät lennot ja majoituksen ja lähtevät Suomesta.
  name: Package Holiday Search API
  slug: package-holiday-search-api
- description: NDC-yhteensopiva API lentojen (vain lennot) hakuun Suomesta.
  name: Flight Search API
  slug: flight-search-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/akkilahdot-fi/agentic-access/akkilahdot-fi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/akkilahdot-fi-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/akkilahdot-fi/rules/akkilahdot-fi-rules.yml
  title: ''
  type: Spectral
  url: rules/akkilahdot-fi-rules.yml
- group: agent
  href: https://artifacts.apis.io/akkilahdot-fi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/akkilahdot-fi/conformance/akkilahdot-fi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/akkilahdot-fi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/akkilahdot-fi/llms/akkilahdot-fi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/akkilahdot-fi-llms.txt
- group: build
  href: https://artifacts.apis.io/akkilahdot-fi/mcp/akkilahdot-fi-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/akkilahdot-fi-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/akkilahdot-fi/mcp/akkilahdot-fi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/akkilahdot-fi-mcp.yml
- group: other
  href: https://artifacts.apis.io/akkilahdot-fi/hosts/akkilahdot-fi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/akkilahdot-fi-hosts.yml
- group: auth
  href: https://artifacts.apis.io/akkilahdot-fi/security/akkilahdot-fi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akkilahdot-fi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://akkilahdot.fi/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.akkilahdot.fi/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.akkilahdot.fi/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.akkilahdot.fi/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.akkilahdot.fi/
- group: operate
  title: ''
  type: Support
  url: https://www.akkilahdot.fi/artikkelit/yhteystiedot
- group: operate
  title: ''
  type: FAQ
  url: https://www.akkilahdot.fi/faq
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.akkilahdot.fi/artikkelit/tietosuojalauseke
created: '2026-11-01'
description: Äkkilähdöt.fi on Suomen suurin lomamatkojen hakukone ja turvallisin paikka löytää äkkilähdöt ja muut pakettimatkat. Teemme yhteistyötä kaikkien suurimpien matkanjärjestäjien ja matkatoimistojen kanssa, ja yhdistämme samaan hakutulokseen suuren määrän matkoja yhdellä kertaa. Matkustitpa sitten yksin, perheen kanssa tai isommassa, enintään yhdeksän hengen porukassa, löydät parhaat matkatarjoukset täältä.
image: https://www.akkilahdot.fi/cdn/images/green/akkilahdot-logo.svg
layout: provider
mcp_servers:
- description: Remote MCP server at www.akkilahdot.fi.
  name: Äkkilähdöt MCP Server
  slug: akkilahdot-fi-mcp-yml
modified: '2026-11-01'
name: Äkkilähdöt
nav: Providers
network: true
overview: 'Äkkilähdöt is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Finland, Holiday, Search, and Package.


  The Äkkilähdöt catalog on APIs.io includes 1 Spectral governance ruleset.


  Äkkilähdöt''s developer surface includes documentation, API reference, getting-started guide, support, FAQ, and 12 more developer resources.'
plans:
- name: Akkilahdot Fi Plans Pricing
  plan_count: 0
  slug: akkilahdot-fi-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Akkilahdot Fi Rate Limits
  slug: akkilahdot-fi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Äkkilähdöt API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: akkilahdot-fi-rules
scopes:
- name: Akkilahdot Fi Scopes
  scope_count: 0
  slug: akkilahdot-fi-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 5.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 23.2
    discoverability: 65.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - finland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  previous_composite: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Akkilahdot Fi Authentication
  slug: akkilahdot-fi-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Akkilahdot Fi Domain Security
  slug: akkilahdot-fi-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 2
skills:
- name: flight-search
  slug: akkilahdot-fi-flight-search
- name: holiday-search
  slug: akkilahdot-fi-holiday-search
slug: akkilahdot-fi
tags:
- Travel
- Finland
- Holiday
- Search
- Package
website: https://akkilahdot.fi/
---
