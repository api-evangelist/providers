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
  name: Csatzo Com Agentic Access
  operation_count: 18
  slug: csatzo-com-agentic-access
  summary_line: 18 operations · 14 acting
api_count: 1
apis:
- baseURL: https://csatzo.com
  baseurl_source: declared
  description: dataset
  name: Csatzo Dataset API
  slug: csatzo-com-dataset-api
- baseURL: https://csatzo.com
  baseurl_source: declared
  description: The mcp API from Csatzo — 1 operation(s) for mcp.
  name: Csatzo MCP API
  slug: csatzo-com-mcp-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/csatzo-com/agentic-access/csatzo-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/csatzo-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/csatzo-com/plans/csatzo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/csatzo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/csatzo-com/rules/csatzo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/csatzo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/csatzo-com/vocabulary/csatzo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/csatzo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/csatzo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://csatzo.com/terms
- group: design
  href: https://artifacts.apis.io/csatzo-com/errors/csatzo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/csatzo-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/csatzo-com/conformance/csatzo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/csatzo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/csatzo-com/llms/csatzo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/csatzo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/csatzo-com/mcp/csatzo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/csatzo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/csatzo-com/well-known/csatzo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/csatzo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/csatzo-com/well-known/csatzo-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/csatzo-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/csatzo-com/well-known/csatzo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/csatzo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/csatzo-com/hosts/csatzo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/csatzo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/csatzo-com/vendors/csatzo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/csatzo-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://csatzo.com/terms/
- group: operate
  title: ''
  type: Support
  url: https://csatzo.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://csatzo.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://csatzo.com/pricing/
- group: auth
  href: https://artifacts.apis.io/csatzo-com/authentication/csatzo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/csatzo-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/csatzo-com/security/csatzo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/csatzo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/csatzo-com/security/csatzo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/csatzo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://csatzo.com/
created: '2026-11-04'
description: Csatzo provides free survey worksheets and customer feedback tools to help businesses determine how many customers to ask, anticipate response rates, and manage follow‑up calls. Their platform offers a range of worksheets, product‑survey question templates, and a simple interface for collecting and scoring feedback, aiming to improve decision‑making for product development and marketing strategies.
image: https://csatzo.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at csatzo.com.
  name: Csatzo MCP Server
  slug: csatzo-com-mcp-yml
modified: '2026-11-04'
name: Csatzo
nav: Providers
network: true
overview: 'Csatzo publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API and MCP API. Tagged areas include Customer Feedback, Survey Tools, Free Worksheets, Product Development, and Marketing.


  The Csatzo catalog on APIs.io includes 1 Spectral governance ruleset.


  Csatzo''s developer surface includes support, pricing, authentication, and 20 more developer resources.'
plans:
- name: Csatzo Com Plans Pricing
  plan_count: 2
  slug: csatzo-com-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Csatzo API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: csatzo-com-rules
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 19
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
  name: Csatzo Com Authentication
  slug: csatzo-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Csatzo Com Domain Security
  slug: csatzo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Csatzo Com Vulnerability Disclosure
  slug: csatzo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: csatzo-com-analyze-dataset
  slug: csatzo-com-analyze-dataset
slug: csatzo-com
tags:
- Customer Feedback
- Survey Tools
- Free Worksheets
- Product Development
- Marketing
website: https://csatzo.com/
---
