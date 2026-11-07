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
    agentic_access: false
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 9.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Amortlane provides dataset tools via its MCP server, exposing financial dataset operations.
  name: Amortlane API
  slug: amortlane-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/amortlane-com/plans/amortlane-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/amortlane-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/amortlane-com/vocabulary/amortlane-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amortlane-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/amortlane-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://amortlane.com/terms
- group: design
  href: https://artifacts.apis.io/amortlane-com/conformance/amortlane-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amortlane-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amortlane-com/llms/amortlane-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amortlane-com-llms.txt
- group: build
  href: https://artifacts.apis.io/amortlane-com/mcp/amortlane-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/amortlane-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/amortlane-com/mcp/amortlane-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/amortlane-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/amortlane-com/well-known/amortlane-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amortlane-com-security.txt
- group: auth
  href: https://artifacts.apis.io/amortlane-com/well-known/amortlane-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amortlane-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/amortlane-com/well-known/amortlane-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amortlane-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/amortlane-com/hosts/amortlane-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amortlane-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/amortlane-com/vendors/amortlane-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amortlane-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://amortlane.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://amortlane.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://amortlane.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://amortlane.com/pricing/
- group: auth
  href: https://artifacts.apis.io/amortlane-com/authentication/amortlane-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amortlane-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/amortlane-com/security/amortlane-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amortlane-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amortlane-com/security/amortlane-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amortlane-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://amortlane.com/
created: '2026-10-29'
description: Amortlane provides a free, web‑based 30‑year loan calculator and related financial tools, allowing users to generate amortization schedules, explore home‑equity loan payments, and access worksheets. The platform offers a Pro tier with additional features such as worksheet saving and advanced analytics. It serves brokers, loan officers, small lenders, and investors seeking detailed payment breakdowns without requiring an account.
image: https://amortlane.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at amortlane.com.
  name: amortlane-com MCP Server
  slug: amortlane-com-mcp-yml
modified: '2026-10-29'
name: amortlane-com
nav: Providers
network: true
overview: 'amortlane-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Calculator, Mortgage, Loan, and Tools.


  amortlane-com''s developer surface includes support, pricing, authentication, and 18 more developer resources.'
plans:
- name: Amortlane Com Plans Pricing
  plan_count: 2
  slug: amortlane-com-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 46.3
    catalog_earned_first_party: 8.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 16.1
    discoverability: 75.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/amortlane-com/amortlane-com-2026-11-03T120821.png
security:
- kind: authentication
  name: Amortlane Com Authentication
  slug: amortlane-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Amortlane Com Domain Security
  slug: amortlane-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Amortlane Com Vulnerability Disclosure
  slug: amortlane-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset
  slug: amortlane-com-dataset
slug: amortlane-com
tags:
- Finance
- Calculator
- Mortgage
- Loan
- Tools
- Free
website: https://amortlane.com/
---
