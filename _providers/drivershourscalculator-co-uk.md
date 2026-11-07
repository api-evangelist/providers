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
- acting_count: 2
  human_in_the_loop: 0
  name: Drivershourscalculator Co Uk Agentic Access
  operation_count: 2
  slug: drivershourscalculator-co-uk-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- baseURL: https://drivershourscalculator.co.uk
  baseurl_source: declared
  description: calculator
  name: Drivers' Hours Calculator Calculator API
  slug: drivershourscalculator-co-uk-calculator-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/agentic-access/drivershourscalculator-co-uk-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/drivershourscalculator-co-uk-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/rules/drivershourscalculator-co-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/drivershourscalculator-co-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/vocabulary/drivershourscalculator-co-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/drivershourscalculator-co-uk-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://drivershourscalculator.co.uk/terms
- group: design
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/errors/drivershourscalculator-co-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/drivershourscalculator-co-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/conformance/drivershourscalculator-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/drivershourscalculator-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/llms/drivershourscalculator-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/drivershourscalculator-co-uk-llms.txt
- group: build
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/mcp/drivershourscalculator-co-uk-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/drivershourscalculator-co-uk-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/mcp/drivershourscalculator-co-uk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/drivershourscalculator-co-uk-mcp.yml
- group: auth
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/well-known/drivershourscalculator-co-uk-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/drivershourscalculator-co-uk-security.txt
- group: agent
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/well-known/drivershourscalculator-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/drivershourscalculator-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/hosts/drivershourscalculator-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/drivershourscalculator-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/vendors/drivershourscalculator-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/drivershourscalculator-co-uk-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://drivershourscalculator.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://drivershourscalculator.co.uk/privacy/
- group: auth
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/authentication/drivershourscalculator-co-uk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/drivershourscalculator-co-uk-authentication.yml
- group: auth
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/security/drivershourscalculator-co-uk-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/drivershourscalculator-co-uk-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/drivershourscalculator-co-uk/security/drivershourscalculator-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/drivershourscalculator-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://drivershourscalculator.co.uk/
created: '2026-11-05'
description: Drivers' Hours Calculator provides an online EU drivers' hours calculator for HGV operators, allowing them to plan legal driving and rest times. The tool computes remaining daily, weekly and fortnightly driving time and required breaks, helping fleet managers ensure compliance with EU and UK regulations. It offers a free web application with detailed guidance on limits, rest periods, and rostering scenarios.
image: https://drivershourscalculator.co.uk/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at drivershourscalculator.co.uk.
  name: Drivers' Hours Calculator MCP Server
  slug: drivershourscalculator-co-uk-mcp-yml
modified: '2026-11-05'
name: Drivers' Hours Calculator
nav: Providers
network: true
overview: 'Drivers'' Hours Calculator publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Calculator API. Tagged areas include Drivers, EU, HGV, Compliance, and Calculator.


  The Drivers'' Hours Calculator catalog on APIs.io includes 1 Spectral governance ruleset.


  Drivers'' Hours Calculator''s developer surface includes authentication and 19 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Drivers' Hours Calculator API Rules
  rule_count: 51
  severity_counts:
    error: 49
    hint: 0
    info: 1
    warn: 1
  slug: drivershourscalculator-co-uk-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 51.4
    developer_ergonomics: 13.7
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
  name: Drivershourscalculator Co Uk Authentication
  slug: drivershourscalculator-co-uk-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Drivershourscalculator Co Uk Domain Security
  slug: drivershourscalculator-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Drivershourscalculator Co Uk Vulnerability Disclosure
  slug: drivershourscalculator-co-uk-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: drivershourscalculator-co-uk-calculator-workflow
  slug: drivershourscalculator-co-uk-calculator-workflow
slug: drivershourscalculator-co-uk
tags:
- Drivers
- EU
- HGV
- Compliance
- Calculator
website: https://drivershourscalculator.co.uk/
---
