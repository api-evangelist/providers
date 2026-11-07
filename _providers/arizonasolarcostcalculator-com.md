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
    agent_skills: unknown
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 13.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Arizonasolarcostcalculator Com Agentic Access
  operation_count: 7
  slug: arizonasolarcostcalculator-com-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- description: Solar panel cost calculator API for Arizona, providing cost estimates with tax credit details.
  name: Arizona Solar Cost Calculator API
  slug: arizona-solar-cost-calculator-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/arizonasolarcostcalculator-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://arizonasolarcostcalculator.com/terms
- group: design
  href: https://artifacts.apis.io/arizonasolarcostcalculator-com/conformance/arizonasolarcostcalculator-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arizonasolarcostcalculator-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arizonasolarcostcalculator-com/llms/arizonasolarcostcalculator-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arizonasolarcostcalculator-com-llms.txt
- group: build
  href: https://artifacts.apis.io/arizonasolarcostcalculator-com/mcp/arizonasolarcostcalculator-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/arizonasolarcostcalculator-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/arizonasolarcostcalculator-com/mcp/arizonasolarcostcalculator-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arizonasolarcostcalculator-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/arizonasolarcostcalculator-com/well-known/arizonasolarcostcalculator-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arizonasolarcostcalculator-com-security.txt
- group: agent
  href: https://artifacts.apis.io/arizonasolarcostcalculator-com/well-known/arizonasolarcostcalculator-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arizonasolarcostcalculator-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/arizonasolarcostcalculator-com/hosts/arizonasolarcostcalculator-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arizonasolarcostcalculator-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/arizonasolarcostcalculator-com/vendors/arizonasolarcostcalculator-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arizonasolarcostcalculator-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arizonasolarcostcalculator.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arizonasolarcostcalculator.com/privacy/
- group: auth
  href: https://artifacts.apis.io/arizonasolarcostcalculator-com/security/arizonasolarcostcalculator-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arizonasolarcostcalculator-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arizonasolarcostcalculator-com/security/arizonasolarcostcalculator-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arizonasolarcostcalculator-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arizonasolarcostcalculator.com/
created: '2026-11-01'
description: Arizona Solar Cost Calculator provides an online tool to estimate solar panel system costs in Arizona, incorporating the 25% state tax credit (capped at $1,000) and current federal credit information. Users input system size and price per watt to see installed cost, net cost after credit, and other details. The site also offers FAQs on tax credits, utility export rates, and battery considerations, serving as a resource for Arizona residents exploring solar installations.
image: https://arizonasolarcostcalculator.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at arizonasolarcostcalculator.com.
  name: Arizona Solar Cost Calculator MCP Server
  slug: arizonasolarcostcalculator-com-mcp-yml
modified: '2026-11-01'
name: Arizona Solar Cost Calculator
nav: Providers
network: true
overview: 'Arizona Solar Cost Calculator publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Solar, Calculator, Arizona, Renewable Energy, and Finance.


  The Arizona Solar Cost Calculator catalog on APIs.io includes 1 Spectral governance ruleset.'
plans:
- name: Arizonasolarcostcalculator Com Plans Pricing
  plan_count: 0
  slug: arizonasolarcostcalculator-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Arizonasolarcostcalculator Com Rate Limits
  slug: arizonasolarcostcalculator-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Arizona Solar Cost Calculator API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: arizonasolarcostcalculator-com-rules
scopes:
- name: Arizonasolarcostcalculator Com Scopes
  scope_count: 0
  slug: arizonasolarcostcalculator-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 6.0
    developer_ergonomics: 6.4
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 20.2
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
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 31.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arizonasolarcostcalculator Com Authentication
  slug: arizonasolarcostcalculator-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Arizonasolarcostcalculator Com Domain Security
  slug: arizonasolarcostcalculator-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arizonasolarcostcalculator Com Vulnerability Disclosure
  slug: arizonasolarcostcalculator-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: calculate
  slug: arizonasolarcostcalculator-com-calculate
- name: calculator-describe
  slug: arizonasolarcostcalculator-com-calculator_describe
- name: enquiry-describe
  slug: arizonasolarcostcalculator-com-enquiry_describe
- name: enquiry-fields
  slug: arizonasolarcostcalculator-com-enquiry_fields
- name: submit-enquiry
  slug: arizonasolarcostcalculator-com-submit_enquiry
slug: arizonasolarcostcalculator-com
tags:
- Solar
- Calculator
- Arizona
- Renewable Energy
- Finance
website: https://arizonasolarcostcalculator.com/
---
