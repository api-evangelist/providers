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
- acting_count: 6
  human_in_the_loop: 0
  name: 409Acost Com Agentic Access
  operation_count: 7
  slug: 409acost-com-agentic-access
  summary_line: 7 operations · 6 acting
api_count: 1
apis:
- baseURL: https://409acost.com
  baseurl_source: declared
  description: calculator
  name: 409A Cost Calculator API
  slug: 409acost-com-calculator-api
- baseURL: https://409acost.com
  baseurl_source: declared
  description: enquiry
  name: 409A Cost Enquiry API
  slug: 409acost-com-enquiry-api
- baseURL: https://409acost.com
  baseurl_source: declared
  description: The mcp API from 409A Cost — 1 operation(s) for mcp.
  name: 409A Cost MCP API
  slug: 409acost-com-mcp-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/409acost-com/agentic-access/409acost-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/409acost-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/409acost-com/rules/409acost-com-rules.yml
  title: ''
  type: Spectral
  url: rules/409acost-com-rules.yml
- group: design
  href: https://artifacts.apis.io/409acost-com/vocabulary/409acost-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/409acost-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/409acost-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://409acost.com/terms
- group: design
  href: https://artifacts.apis.io/409acost-com/errors/409acost-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/409acost-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/409acost-com/conformance/409acost-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/409acost-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/409acost-com/llms/409acost-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/409acost-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/409acost-com/mcp/409acost-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/409acost-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/409acost-com/well-known/409acost-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/409acost-com-security.txt
- group: agent
  href: https://artifacts.apis.io/409acost-com/well-known/409acost-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/409acost-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/409acost-com/hosts/409acost-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/409acost-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/409acost-com/vendors/409acost-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/409acost-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/409acost-com/security/409acost-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/409acost-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/409acost-com/security/409acost-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/409acost-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://409acost.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://409acost.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://409acost.com/privacy/
created: '2026-10-31'
description: 409A Cost provides a comprehensive guide and calculator for US startup 409A valuation costs. The site offers detailed guides on valuation requirements, when to refresh, example reports, and a data table of published prices from multiple providers. It aims to help startups budget for mandatory 409A valuations, understand regulatory requirements, and access transparent pricing information.
image: https://409acost.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at 409acost.com.
  name: 409A Cost MCP Server
  slug: 409acost-com-mcp-yml
modified: '2026-10-31'
name: 409A Cost
nav: Providers
network: true
overview: '409A Cost publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Calculator API, Enquiry API, and MCP API. Tagged areas include Company, Valuation, Startups, Finance, and Calculator.


  The 409A Cost catalog on APIs.io includes 1 Spectral governance ruleset.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: 409A Cost API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: 409acost-com-rules
score:
  band: emerging
  composite: 25.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 48.8
    developer_ergonomics: 1.8
    discoverability: 65.0
    operational_transparency: 5.3
  previous_composite: 28.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: 409Acost Com Authentication
  slug: 409acost-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 409Acost Com Domain Security
  slug: 409acost-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: 409Acost Com Vulnerability Disclosure
  slug: 409acost-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: 409acost-com-enquiry-process
  slug: 409acost-com-enquiry-process
- name: 409acost-com-mcp-interaction
  slug: 409acost-com-mcp-interaction
slug: 409acost-com
tags:
- Company
- Valuation
- Startups
- Finance
- Calculator
website: https://409acost.com/
---
