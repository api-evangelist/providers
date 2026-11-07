---
access_model:
  confidence: medium
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
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 26.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Duesvo Com Agentic Access
  operation_count: 18
  slug: duesvo-com-agentic-access
  summary_line: 18 operations · 14 acting
api_count: 1
apis:
- baseURL: https://duesvo.com
  baseurl_source: declared
  description: dataset
  name: Duesvo Dataset API
  slug: duesvo-com-dataset-api
- baseURL: https://duesvo.com
  baseurl_source: declared
  description: The mcp API from Duesvo — 1 operation(s) for mcp.
  name: Duesvo MCP API
  slug: duesvo-com-mcp-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/duesvo-com/agentic-access/duesvo-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/duesvo-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/duesvo-com/plans/duesvo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/duesvo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/duesvo-com/rules/duesvo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/duesvo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/duesvo-com/vocabulary/duesvo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/duesvo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/duesvo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://duesvo.com/terms
- group: design
  href: https://artifacts.apis.io/duesvo-com/errors/duesvo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/duesvo-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/duesvo-com/conformance/duesvo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/duesvo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/duesvo-com/llms/duesvo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/duesvo-com-llms.txt
- group: build
  href: https://artifacts.apis.io/duesvo-com/mcp/duesvo-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/duesvo-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/duesvo-com/mcp/duesvo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/duesvo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/duesvo-com/well-known/duesvo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/duesvo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/duesvo-com/well-known/duesvo-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/duesvo-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/duesvo-com/well-known/duesvo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/duesvo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/duesvo-com/hosts/duesvo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/duesvo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/duesvo-com/vendors/duesvo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/duesvo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://duesvo.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://duesvo.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://duesvo.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://duesvo.com/pricing/
- group: auth
  href: https://artifacts.apis.io/duesvo-com/authentication/duesvo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/duesvo-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/duesvo-com/security/duesvo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/duesvo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/duesvo-com/security/duesvo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/duesvo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://duesvo.com/
created: '2026-11-06'
description: Duesvo provides membership management software tailored for nonprofits, clubs, and associations. It offers a free membership database template and a paid Pro plan that includes full member record handling, tiered dues, renewal tracking, and reporting tools, all accessible via a web interface without requiring a credit card for the free tier. The platform emphasizes ease of use for single administrators handling small to medium-sized member bases.
image: https://duesvo.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at duesvo.com.
  name: Duesvo MCP Server
  slug: duesvo-com-mcp-yml
modified: '2026-11-06'
name: Duesvo
nav: Providers
network: true
overview: 'Duesvo publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API and MCP API. Tagged areas include Membership, Non-Profit, Clubs, Associations, and Software.


  The Duesvo catalog on APIs.io includes 1 Spectral governance ruleset.


  Duesvo''s developer surface includes support, pricing, authentication, and 21 more developer resources.'
plans:
- name: Duesvo Com Plans Pricing
  plan_count: 2
  slug: duesvo-com-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Duesvo API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: duesvo-com-rules
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 18
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 18.5
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Duesvo Com Authentication
  slug: duesvo-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Duesvo Com Domain Security
  slug: duesvo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Duesvo Com Vulnerability Disclosure
  slug: duesvo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: duesvo-com-search-and-retrieve-row
  slug: duesvo-com-search-and-retrieve-row
slug: duesvo-com
tags:
- Membership
- Non-Profit
- Clubs
- Associations
- Software
website: https://duesvo.com/
---
