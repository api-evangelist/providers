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
- acting_count: 7
  human_in_the_loop: 0
  name: Disclovo Com Agentic Access
  operation_count: 9
  slug: disclovo-com-agentic-access
  summary_line: 9 operations · 7 acting
api_count: 1
apis:
- baseURL: https://disclovo.com
  baseurl_source: declared
  description: dataset
  name: Disclovo Dataset API
  slug: disclovo-com-dataset-api
- baseURL: https://disclovo.com
  baseurl_source: declared
  description: The mcp API from Disclovo — 1 operation(s) for mcp.
  name: Disclovo MCP API
  slug: disclovo-com-mcp-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/disclovo-com/agentic-access/disclovo-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/disclovo-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/disclovo-com/plans/disclovo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/disclovo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/disclovo-com/rules/disclovo-com-rules.yml
  title: ''
  type: Spectral
  url: rules/disclovo-com-rules.yml
- group: design
  href: https://artifacts.apis.io/disclovo-com/vocabulary/disclovo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/disclovo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/disclovo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://disclovo.com/terms
- group: design
  href: https://artifacts.apis.io/disclovo-com/errors/disclovo-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/disclovo-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/disclovo-com/conformance/disclovo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/disclovo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/disclovo-com/llms/disclovo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/disclovo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/disclovo-com/mcp/disclovo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/disclovo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/disclovo-com/well-known/disclovo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/disclovo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/disclovo-com/well-known/disclovo-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/disclovo-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/disclovo-com/well-known/disclovo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/disclovo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/disclovo-com/hosts/disclovo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/disclovo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/disclovo-com/vendors/disclovo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/disclovo-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://disclovo.com/support/
- group: auth
  href: https://artifacts.apis.io/disclovo-com/authentication/disclovo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/disclovo-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/disclovo-com/security/disclovo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/disclovo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/disclovo-com/security/disclovo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/disclovo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://disclovo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://disclovo.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://disclovo.com/privacy/
- group: commercial
  title: ''
  type: Pricing
  url: https://disclovo.com/pricing/
- group: operate
  title: ''
  type: Contact
  url: https://disclovo.com/contact/
created: '2026-11-05'
description: Disclovo provides regulatory reporting software for small firms, offering free worksheets that size the filing work implied by a set of regulatory returns, track submission hours, and maintain evidence sets. The platform helps firms understand the workload of filing requirements and keeps records of what was filed, aiming to streamline compliance and reporting processes for financial and regulatory obligations.
image: https://disclovo.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at disclovo.com.
  name: Disclovo MCP Server
  slug: disclovo-com-mcp-yml
modified: '2026-11-05'
name: Disclovo
nav: Providers
network: true
overview: 'Disclovo publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API and MCP API. Tagged areas include Company, Regulatory, Reporting, Compliance, and Software.


  The Disclovo catalog on APIs.io includes 1 Spectral governance ruleset.


  Disclovo''s developer surface includes support, authentication, pricing, and 21 more developer resources.'
plans:
- name: Disclovo Com Plans Pricing
  plan_count: 2
  slug: disclovo-com-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Disclovo API Rules
  rule_count: 49
  severity_counts:
    error: 43
    hint: 0
    info: 5
    warn: 1
  slug: disclovo-com-rules
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
  name: Disclovo Com Authentication
  slug: disclovo-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Disclovo Com Domain Security
  slug: disclovo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Disclovo Com Vulnerability Disclosure
  slug: disclovo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: disclovo-com-dataset-search-and-top
  slug: disclovo-com-dataset-search-and-top
slug: disclovo-com
tags:
- Company
- Regulatory
- Reporting
- Compliance
- Software
- Finance
website: https://disclovo.com/
---
