---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
  score: 24.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for payroll cost calculations and enquiry tools
  name: Canada Payroll Calculator API
  slug: canada-payroll-calculator-api
- baseURL: https://canadapayrollcalculator.com
  baseurl_source: declared
  description: 'Canada Payroll Calculator (https://canadapayrollcalculator.com/): the site''s own MCP server, served from its domain. Canada payroll calculator for employers: CPP at 5.95%, CPP2 at 4%, EI at 1.4 times '
  name: Canada Payroll Calculator API API
  slug: canada-payroll-calculator-api-api
artifact_total: 6
common:
- group: design
  href: https://artifacts.apis.io/canadapayrollcalculator-com/rules/canadapayrollcalculator-com-rules.yml
  title: ''
  type: Spectral
  url: rules/canadapayrollcalculator-com-rules.yml
- group: design
  href: https://artifacts.apis.io/canadapayrollcalculator-com/vocabulary/canadapayrollcalculator-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/canadapayrollcalculator-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/canadapayrollcalculator-com/conformance/canadapayrollcalculator-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canadapayrollcalculator-com-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://canadapayrollcalculator.com/terms
- group: design
  href: https://artifacts.apis.io/canadapayrollcalculator-com/errors/canadapayrollcalculator-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canadapayrollcalculator-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/canadapayrollcalculator-com/llms/canadapayrollcalculator-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canadapayrollcalculator-com-llms.txt
- group: build
  href: https://artifacts.apis.io/canadapayrollcalculator-com/mcp/canadapayrollcalculator-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/canadapayrollcalculator-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/canadapayrollcalculator-com/mcp/canadapayrollcalculator-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/canadapayrollcalculator-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/canadapayrollcalculator-com/well-known/canadapayrollcalculator-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/canadapayrollcalculator-com-security.txt
- group: agent
  href: https://artifacts.apis.io/canadapayrollcalculator-com/well-known/canadapayrollcalculator-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canadapayrollcalculator-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/canadapayrollcalculator-com/hosts/canadapayrollcalculator-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canadapayrollcalculator-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/canadapayrollcalculator-com/vendors/canadapayrollcalculator-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canadapayrollcalculator-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://canadapayrollcalculator.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canadapayrollcalculator.com/privacy/
- group: auth
  href: https://artifacts.apis.io/canadapayrollcalculator-com/security/canadapayrollcalculator-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/canadapayrollcalculator-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/canadapayrollcalculator-com/security/canadapayrollcalculator-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canadapayrollcalculator-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canadapayrollcalculator.com/
created: '2026-11-04'
description: Canada Payroll Calculator provides an online tool for Canadian employers to calculate the true cost of hiring an employee, including employer CPP, CPP2, and EI contributions at 2026 rates, with links to official Canada Revenue Agency sources. The calculator offers transparent breakdowns of statutory payroll taxes, assumptions, and data sources, helping businesses understand payroll expenses beyond basic salary. It does not include provincial taxes, workers' compensation, or employee-side deductions.
image: https://canadapayrollcalculator.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at canadapayrollcalculator.com.
  name: Canada Payroll Calculator MCP Server
  slug: canadapayrollcalculator-com-mcp-yml
modified: '2026-11-04'
name: Canada Payroll Calculator
nav: Providers
network: true
overview: 'Canada Payroll Calculator publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Finance, Payroll, Canada, Calculator, and Employer.


  The Canada Payroll Calculator catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Canada Payroll Calculator API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: canadapayrollcalculator-com-rules
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.4
    developer_ergonomics: 0.0
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Canadapayrollcalculator Com Domain Security
  slug: canadapayrollcalculator-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Canadapayrollcalculator Com Vulnerability Disclosure
  slug: canadapayrollcalculator-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: canadapayrollcalculator-com
tags:
- Finance
- Payroll
- Canada
- Calculator
- Employer
website: https://canadapayrollcalculator.com/
---
