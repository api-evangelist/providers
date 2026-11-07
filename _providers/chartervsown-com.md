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
    agent_skills: unknown
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
  score: 29.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Chartervsown Com Agentic Access
  operation_count: 5
  slug: chartervsown-com-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 1
apis:
- baseURL: https://chartervsown.com
  baseurl_source: declared
  description: calculator
  name: Charter vs Own Calculator API
  slug: chartervsown-com-calculator-api
- baseURL: https://chartervsown.com
  baseurl_source: declared
  description: enquiry
  name: Charter vs Own Enquiry API
  slug: chartervsown-com-enquiry-api
- baseURL: https://chartervsown.com
  baseurl_source: declared
  description: The mcp API from Charter vs Own — 1 operation(s) for mcp.
  name: Charter vs Own MCP API
  slug: chartervsown-com-mcp-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/chartervsown-com/agentic-access/chartervsown-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chartervsown-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/chartervsown-com/rules/chartervsown-com-rules.yml
  title: ''
  type: Spectral
  url: rules/chartervsown-com-rules.yml
- group: design
  href: https://artifacts.apis.io/chartervsown-com/vocabulary/chartervsown-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chartervsown-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/chartervsown-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://chartervsown.com/terms
- group: design
  href: https://artifacts.apis.io/chartervsown-com/errors/chartervsown-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chartervsown-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chartervsown-com/conformance/chartervsown-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chartervsown-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chartervsown-com/llms/chartervsown-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chartervsown-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/chartervsown-com/mcp/chartervsown-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/chartervsown-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/chartervsown-com/well-known/chartervsown-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/chartervsown-com-security.txt
- group: agent
  href: https://artifacts.apis.io/chartervsown-com/well-known/chartervsown-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chartervsown-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/chartervsown-com/hosts/chartervsown-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chartervsown-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/chartervsown-com/vendors/chartervsown-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chartervsown-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chartervsown.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chartervsown.com/privacy/
- group: auth
  href: https://artifacts.apis.io/chartervsown-com/authentication/chartervsown-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chartervsown-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/chartervsown-com/security/chartervsown-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/chartervsown-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/chartervsown-com/security/chartervsown-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chartervsown-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chartervsown.com/
created: '2026-11-03'
description: Charter vs Own provides a private jet charter cost estimator that helps users compare the hourly rates, fees, and additional costs associated with chartering a private aircraft versus owning one. The site offers detailed explanations of positioning legs, fuel surcharges, landing and handling fees, and other variables that affect total flight costs. It also includes a calculator tool for estimating total expenses based on user‑provided inputs, aiming to inform decision‑making for individuals and businesses considering private jet use.
image: https://chartervsown.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at chartervsown.com.
  name: Charter vs Own MCP Server
  slug: chartervsown-com-mcp-yml
modified: '2026-11-03'
name: Charter vs Own
nav: Providers
network: true
overview: 'Charter vs Own publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Calculator API, Enquiry API, and MCP API. Tagged areas include Aviation, Finance, Calculator, Private-Jet, and CostEstimator.


  The Charter vs Own catalog on APIs.io includes 1 Spectral governance ruleset.


  Charter vs Own''s developer surface includes authentication and 18 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Charter vs Own API Rules
  rule_count: 53
  severity_counts:
    error: 47
    hint: 0
    info: 5
    warn: 1
  slug: chartervsown-com-rules
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 50.0
    developer_ergonomics: 18.3
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Chartervsown Com Authentication
  slug: chartervsown-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Chartervsown Com Domain Security
  slug: chartervsown-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Chartervsown Com Vulnerability Disclosure
  slug: chartervsown-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: chartervsown-com-main
  slug: chartervsown-com-main
slug: chartervsown-com
tags:
- Aviation
- Finance
- Calculator
- Private-Jet
- CostEstimator
website: https://chartervsown.com/
---
