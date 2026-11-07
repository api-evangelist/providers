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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Boatvaluecalculator Com Agentic Access
  operation_count: 9
  slug: boatvaluecalculator-com-agentic-access
  summary_line: 9 operations · 8 acting
api_count: 1
apis:
- baseURL: https://boatvaluecalculator.com
  baseurl_source: declared
  description: calculator
  name: Boat Value Calculator Calculator API
  slug: boatvaluecalculator-com-calculator-api
- baseURL: https://boatvaluecalculator.com
  baseurl_source: declared
  description: enquiry
  name: Boat Value Calculator Enquiry API
  slug: boatvaluecalculator-com-enquiry-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/boatvaluecalculator-com/agentic-access/boatvaluecalculator-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/boatvaluecalculator-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/boatvaluecalculator-com/rules/boatvaluecalculator-com-rules.yml
  title: ''
  type: Spectral
  url: rules/boatvaluecalculator-com-rules.yml
- group: design
  href: https://artifacts.apis.io/boatvaluecalculator-com/vocabulary/boatvaluecalculator-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/boatvaluecalculator-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/boatvaluecalculator-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://boatvaluecalculator.com/terms
- group: design
  href: https://artifacts.apis.io/boatvaluecalculator-com/errors/boatvaluecalculator-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/boatvaluecalculator-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/boatvaluecalculator-com/conformance/boatvaluecalculator-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/boatvaluecalculator-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/boatvaluecalculator-com/llms/boatvaluecalculator-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/boatvaluecalculator-com-llms.txt
- group: build
  href: https://artifacts.apis.io/boatvaluecalculator-com/mcp/boatvaluecalculator-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/boatvaluecalculator-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/boatvaluecalculator-com/mcp/boatvaluecalculator-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/boatvaluecalculator-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/boatvaluecalculator-com/well-known/boatvaluecalculator-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/boatvaluecalculator-com-security.txt
- group: agent
  href: https://artifacts.apis.io/boatvaluecalculator-com/well-known/boatvaluecalculator-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boatvaluecalculator-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/boatvaluecalculator-com/hosts/boatvaluecalculator-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boatvaluecalculator-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/boatvaluecalculator-com/vendors/boatvaluecalculator-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boatvaluecalculator-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://boatvaluecalculator.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://boatvaluecalculator.com/privacy/
- group: auth
  href: https://artifacts.apis.io/boatvaluecalculator-com/authentication/boatvaluecalculator-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/boatvaluecalculator-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/boatvaluecalculator-com/security/boatvaluecalculator-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/boatvaluecalculator-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/boatvaluecalculator-com/security/boatvaluecalculator-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boatvaluecalculator-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://boatvaluecalculator.com/
created: '2026-11-02'
description: Boat Value Calculator provides an online tool to estimate the market value of a boat. Users input details such as model year, condition, engine hours, and survey findings, and the calculator adjusts a base guide value accordingly. It helps owners understand a realistic selling price, offering insights into how various factors influence boat worth. The service is free and aims to simplify boat valuation for sellers and buyers alike.
image: https://boatvaluecalculator.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at boatvaluecalculator.com.
  name: Boat Value Calculator MCP Server
  slug: boatvaluecalculator-com-mcp-yml
modified: '2026-11-02'
name: Boat Value Calculator
nav: Providers
network: true
overview: 'Boat Value Calculator publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Calculator API and Enquiry API. Tagged areas include Boat, Valuation, Finance, Marine, and Calculator.


  The Boat Value Calculator catalog on APIs.io includes 1 Spectral governance ruleset.


  Boat Value Calculator''s developer surface includes authentication and 19 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Boat Value Calculator API Rules
  rule_count: 53
  severity_counts:
    error: 44
    hint: 0
    info: 8
    warn: 1
  slug: boatvaluecalculator-com-rules
score:
  band: thin
  composite: 29.0
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
    contract_quality: 50.5
    developer_ergonomics: 13.7
    discoverability: 65.0
    operational_transparency: 5.3
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
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Boatvaluecalculator Com Authentication
  slug: boatvaluecalculator-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Boatvaluecalculator Com Domain Security
  slug: boatvaluecalculator-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Boatvaluecalculator Com Vulnerability Disclosure
  slug: boatvaluecalculator-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: calculator
  slug: boatvaluecalculator-com-calculator
slug: boatvaluecalculator-com
tags:
- Boat
- Valuation
- Finance
- Marine
- Calculator
website: https://boatvaluecalculator.com/
---
