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
- acting_count: 10
  human_in_the_loop: 0
  name: Eorcompass Com Agentic Access
  operation_count: 12
  slug: eorcompass-com-agentic-access
  summary_line: 12 operations · 10 acting
api_count: 1
apis:
- description: EOR Compass provides a dataset of median advertised EOR pricing per employee per month, sourced from vendor price pages.
  name: EOR Compass API
  slug: eor-compass-api
- baseURL: https://eorcompass.com
  baseurl_source: declared
  description: dataset
  name: eorcompass-com Dataset API
  slug: eorcompass-com-dataset-api
- baseURL: https://eorcompass.com
  baseurl_source: declared
  description: enquiry
  name: eorcompass-com Enquiry API
  slug: eorcompass-com-enquiry-api
- baseURL: https://eorcompass.com
  baseurl_source: declared
  description: The mcp API from eorcompass-com — 1 operation(s) for mcp.
  name: eorcompass-com MCP API
  slug: eorcompass-com-mcp-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/eorcompass-com/agentic-access/eorcompass-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/eorcompass-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/eorcompass-com/rules/eorcompass-com-rules.yml
  title: ''
  type: Spectral
  url: rules/eorcompass-com-rules.yml
- group: design
  href: https://artifacts.apis.io/eorcompass-com/vocabulary/eorcompass-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/eorcompass-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/eorcompass-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://eorcompass.com/terms
- group: design
  href: https://artifacts.apis.io/eorcompass-com/errors/eorcompass-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/eorcompass-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/eorcompass-com/conformance/eorcompass-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/eorcompass-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/eorcompass-com/llms/eorcompass-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/eorcompass-com-llms.txt
- group: build
  href: https://artifacts.apis.io/eorcompass-com/mcp/eorcompass-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/eorcompass-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/eorcompass-com/mcp/eorcompass-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/eorcompass-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/eorcompass-com/well-known/eorcompass-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/eorcompass-com-security.txt
- group: agent
  href: https://artifacts.apis.io/eorcompass-com/well-known/eorcompass-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/eorcompass-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/eorcompass-com/hosts/eorcompass-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/eorcompass-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/eorcompass-com/vendors/eorcompass-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/eorcompass-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://eorcompass.com/terms/
- group: start
  title: ''
  type: SignUp
  url: https://eorcompass.com/register-company-cyprus/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://eorcompass.com/privacy/
- group: auth
  href: https://artifacts.apis.io/eorcompass-com/authentication/eorcompass-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/eorcompass-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/eorcompass-com/security/eorcompass-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/eorcompass-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/eorcompass-com/security/eorcompass-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/eorcompass-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eorcompass.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://eorcompass.com/quote/
- group: operate
  title: ''
  type: Support
  url: https://eorcompass.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://eorcompass.com/datasets/eor-pricing-index/
created: '2026-10-30'
description: EOR Compass aggregates and compares employer of record (EOR) pricing data from multiple vendors, providing verified, dated price quotes across eight countries. The site offers guides on EOR models, payroll services, and international contractor payments, aiming to help businesses make informed hiring decisions.
image: https://eorcompass.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at eorcompass.com.
  name: eorcompass-com MCP Server
  slug: eorcompass-com-mcp-yml
modified: '2026-10-30'
name: eorcompass-com
nav: Providers
network: true
overview: 'eorcompass-com publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Dataset API, Enquiry API, MCP API, and 1 more. Tagged areas include Company, Employer of Record, Payroll, PricingComparison, and Human Resources.


  The eorcompass-com catalog on APIs.io includes 1 Spectral governance ruleset.


  eorcompass-com''s developer surface includes signup flow, authentication, getting-started guide, support, pricing, and 19 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: eorcompass-com API Rules
  rule_count: 16
  severity_counts:
    error: 11
    hint: 0
    info: 4
    warn: 1
  slug: eorcompass-com-rules
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 48.8
    developer_ergonomics: 22.0
    discoverability: 75.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 39.8
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
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/eorcompass-com/eorcompass-com-2026-11-03T131555.png
security:
- kind: authentication
  name: Eorcompass Com Authentication
  slug: eorcompass-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Eorcompass Com Domain Security
  slug: eorcompass-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Eorcompass Com Vulnerability Disclosure
  slug: eorcompass-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: eorcompass-com-dataset-insight
  slug: eorcompass-com-dataset-insight
- name: eorcompass-com-enquiry-process
  slug: eorcompass-com-enquiry-process
slug: eorcompass-com
tags:
- Company
- Employer of Record
- Payroll
- PricingComparison
- Human Resources
website: https://eorcompass.com/
---
