---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Awardsecrets Com Agentic Access
  operation_count: 1
  slug: awardsecrets-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://awardsecrets.com
  baseurl_source: declared
  description: The Api.php API from AwardSecrets — 1 operation(s) for api.php.
  name: AwardSecrets Api.php API
  slug: awardsecrets-com-api-php-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/awardsecrets-com/vocabulary/awardsecrets-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/awardsecrets-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/awardsecrets-com/data-model/awardsecrets-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/awardsecrets-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/awardsecrets-com/agentic-access/awardsecrets-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/awardsecrets-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/awardsecrets-com/plans/awardsecrets-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/awardsecrets-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/awardsecrets-com/rules/awardsecrets-com-rules.yml
  title: ''
  type: Spectral
  url: rules/awardsecrets-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/awardsecrets-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/awardsecrets-com/changelog/awardsecrets-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/awardsecrets-com-changelog.yml
- group: auth
  href: https://artifacts.apis.io/awardsecrets-com/authentication/awardsecrets-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/awardsecrets-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/awardsecrets-com/conformance/awardsecrets-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/awardsecrets-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/awardsecrets-com/llms/awardsecrets-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/awardsecrets-com-llms.txt
- group: other
  href: https://artifacts.apis.io/awardsecrets-com/a2a/awardsecrets-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/awardsecrets-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/awardsecrets-com/mcp/awardsecrets-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/awardsecrets-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/awardsecrets-com/mcp/awardsecrets-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/awardsecrets-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/awardsecrets-com/well-known/awardsecrets-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/awardsecrets-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/awardsecrets-com/hosts/awardsecrets-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/awardsecrets-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/awardsecrets-com/security/awardsecrets-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/awardsecrets-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://awardsecrets.com/
- group: docs
  title: ''
  type: Documentation
  url: https://awardsecrets.com/api.html
- group: commercial
  title: ''
  type: Pricing
  url: https://awardsecrets.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://awardsecrets.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://awardsecrets.com/privacy
created: '2026-11-02'
description: AwardSecrets is an AI‑powered award flight search engine and data service that helps travelers find business and first‑class award seats across 60+ airlines using points from major programs. Operated by MetroSpaces LLC, it offers a live GDS‑connected inventory, points pricing, and AI‑driven recommendations. The platform provides a REST API and MCP tool for developers and AI agents, with tiered subscription plans starting at $49/month.
image: https://awardsecrets.com/og-image.png
json_schemas:
- name: SearchRequest
  property_count: 0
  slug: awardsecrets-com-search-request
- name: SearchResponse
  property_count: 0
  slug: awardsecrets-com-search-response
layout: provider
mcp_servers:
- description: Remote MCP server at awardsecrets.com.
  name: AwardSecrets MCP Server
  slug: awardsecrets-com-mcp-yml
modified: '2026-11-02'
name: AwardSecrets
nav: Providers
network: true
overview: 'AwardSecrets publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Api.php API. Tagged areas include Travel, Awards, Flights, Points, and Company.


  The AwardSecrets catalog on APIs.io includes 1 Spectral governance ruleset.


  AwardSecrets'' developer surface includes changelog, authentication, documentation, pricing, and 17 more developer resources.'
plans:
- name: Awardsecrets Com Plans Pricing
  plan_count: 3
  slug: awardsecrets-com-plans-pricing
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: AwardSecrets API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: awardsecrets-com-rules
scopes:
- name: Awardsecrets Com Scopes
  scope_count: 0
  slug: awardsecrets-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 52.7
    developer_ergonomics: 23.1
    discoverability: 65.0
    operational_transparency: 15.8
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Awardsecrets Com Authentication
  slug: awardsecrets-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Awardsecrets Com Domain Security
  slug: awardsecrets-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: search-award-availability
  slug: awardsecrets-com-search_award_availability
slug: awardsecrets-com
tags:
- Travel
- Awards
- Flights
- Points
- Company
website: https://awardsecrets.com/
---
