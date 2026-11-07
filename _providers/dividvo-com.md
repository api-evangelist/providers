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
    agent_skills: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dividvo Com Agentic Access
  operation_count: 1
  slug: dividvo-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: Dividvo MCP dataset API providing monthly search data via tools.
  name: Dividvo API
  slug: dividvo-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/dividvo-com/agentic-access/dividvo-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dividvo-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/dividvo-com/plans/dividvo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dividvo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dividvo-com/rules/dividvo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dividvo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dividvo-com/vocabulary/dividvo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dividvo-com-vocabulary.yml
- group: auth
  title: ''
  type: Security
  url: https://dividvo.com/terms
- group: design
  href: https://artifacts.apis.io/dividvo-com/errors/dividvo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dividvo-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dividvo-com/conformance/dividvo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dividvo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dividvo-com/llms/dividvo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dividvo-com-llms.txt
- group: build
  href: https://artifacts.apis.io/dividvo-com/mcp/dividvo-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dividvo-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dividvo-com/mcp/dividvo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dividvo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dividvo-com/well-known/dividvo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dividvo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/dividvo-com/well-known/dividvo-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dividvo-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/dividvo-com/well-known/dividvo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dividvo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dividvo-com/hosts/dividvo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dividvo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dividvo-com/vendors/dividvo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dividvo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dividvo.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://dividvo.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dividvo.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://dividvo.com/pricing/
- group: auth
  href: https://artifacts.apis.io/dividvo-com/authentication/dividvo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dividvo-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dividvo-com/security/dividvo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dividvo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dividvo-com/security/dividvo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dividvo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dividvo.com/
created: '2026-11-05'
description: Dividvo provides free UK limited company tax calculators and tools for directors, including corporation tax, salary versus dividend, stamp duty for company purchases, and director loan calculations. The service offers five free tools with a paid Pro plan for advanced features, targeting UK company directors seeking accurate tax planning.
image: https://dividvo.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at dividvo.com.
  name: Dividvo MCP Server
  slug: dividvo-com-mcp-yml
modified: '2026-11-05'
name: Dividvo
nav: Providers
network: true
overview: 'Dividvo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Tax, United Kingdom, and Tools.


  The Dividvo catalog on APIs.io includes 1 Spectral governance ruleset.


  Dividvo''s developer surface includes support, pricing, authentication, and 20 more developer resources.'
plans:
- name: Dividvo Com Plans Pricing
  plan_count: 2
  slug: dividvo-com-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Dividvo API Rules
  rule_count: 50
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 1
  slug: dividvo-com-rules
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
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
  name: Dividvo Com Authentication
  slug: dividvo-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dividvo Com Domain Security
  slug: dividvo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Dividvo Com Vulnerability Disclosure
  slug: dividvo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dividvo-com
tags:
- Company
- Finance
- Tax
- United Kingdom
- Tools
website: https://dividvo.com/
---
