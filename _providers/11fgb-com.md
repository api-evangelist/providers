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
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Connect AI clients to four free, deterministic cleaning calculators for home cost, office cost, staffing and chemical usage.
  name: Cleaning Tools MCP
  slug: cleaning-tools-mcp
- baseURL: https://mcp.11fgb.com
  baseurl_source: declared
  description: 'Eleven Friends of Grumpy Brush Cleaning API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: Eleven Friends of Grumpy Brush Cleaning API
  slug: 11fgb-com-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/11fgb-com/rules/11fgb-com-rules.yml
  title: ''
  type: Spectral
  url: rules/11fgb-com-rules.yml
- group: design
  href: https://artifacts.apis.io/11fgb-com/json-ld/11fgb-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/11fgb-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/11fgb-com/vocabulary/11fgb-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/11fgb-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/11fgb-com/data-model/11fgb-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/11fgb-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/11fgb-com/conformance/11fgb-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/11fgb-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/11fgb-com/llms/11fgb-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/11fgb-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/11fgb-com/mcp/11fgb-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/11fgb-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/11fgb-com/well-known/11fgb-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/11fgb-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/11fgb-com/hosts/11fgb-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/11fgb-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://11fgb.com/developers/mcp/terms
- group: operate
  title: ''
  type: Support
  url: https://11fgb.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://11fgb.com/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://11fgb.com/developers/mcp
- group: auth
  href: https://artifacts.apis.io/11fgb-com/security/11fgb-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/11fgb-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://11fgb.com/
coverage:
  checked: '2026-10-31'
  detail: No machine-readable API specification was found after exhaustive probing of known spec endpoints.
  evidence:
  - status: 403
    url: https://11fgb.com/openapi.yaml
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Eleven Friends of Grumpy Brush Cleaning provides professional house cleaning services across Austin and Central Texas. Customers can book recurring, deep, apartment, office, Airbnb, and move‑in or move‑out cleaning. The company emphasizes reliable, quiet service with flexible scheduling and a focus on thoroughness, serving numerous Texas cities including Austin, Round Rock, and Georgetown. With a team of experienced cleaners, Grumpy Brush ensures each job meets high standards, offering transparent pricing and easy online quotes.
image: https://11fgb.com/assets/static/assets/670d8b684df63.svg
json_schemas:
- name: PostMcpResponse
  property_count: 6
  slug: 11fgb-com-post-mcp-response
jsonld:
- class_count: 1
  name: 11Fgb Com Context
  property_count: 2
  slug: 11fgb-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.11fgb.com.
  name: Eleven Friends of Grumpy Brush Cleaning MCP Server
  slug: 11fgb-com-mcp-yml
modified: '2026-10-31'
name: Eleven Friends of Grumpy Brush Cleaning
nav: Providers
network: true
overview: 'Eleven Friends of Grumpy Brush Cleaning is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cleaning, Home Services, Texas, Austin, and Residential.


  The Eleven Friends of Grumpy Brush Cleaning catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Eleven Friends of Grumpy Brush Cleaning''s developer surface includes support and 14 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Eleven Friends of Grumpy Brush Cleaning API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: 11fgb-com-rules
scopes:
- name: 11Fgb Com Scopes
  scope_count: 0
  slug: 11fgb-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 7.1
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 21.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 11Fgb Com Authentication
  slug: 11fgb-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: 11Fgb Com Domain Security
  slug: 11fgb-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 11fgb-com
tags:
- Cleaning
- Home Services
- Texas
- Austin
- Residential
website: https://11fgb.com/
---
