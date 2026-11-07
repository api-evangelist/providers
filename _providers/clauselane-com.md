---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Clauselane Com Agentic Access
  operation_count: 18
  slug: clauselane-com-agentic-access
  summary_line: 18 operations · 14 acting
api_count: 1
apis:
- baseURL: https://clauselane.com
  baseurl_source: declared
  description: dataset
  name: clauselane-com Dataset API
  slug: clauselane-com-dataset-api
- baseURL: https://clauselane.com
  baseurl_source: declared
  description: The mcp API from clauselane-com — 1 operation(s) for mcp.
  name: clauselane-com MCP API
  slug: clauselane-com-mcp-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/clauselane-com/agentic-access/clauselane-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clauselane-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/clauselane-com/plans/clauselane-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clauselane-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clauselane-com/rules/clauselane-com-rules.yml
  title: ''
  type: Spectral
  url: rules/clauselane-com-rules.yml
- group: design
  href: https://artifacts.apis.io/clauselane-com/vocabulary/clauselane-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clauselane-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/clauselane-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://clauselane.com/terms
- group: design
  href: https://artifacts.apis.io/clauselane-com/errors/clauselane-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clauselane-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clauselane-com/conformance/clauselane-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clauselane-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clauselane-com/llms/clauselane-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clauselane-com-llms.txt
- group: build
  href: https://artifacts.apis.io/clauselane-com/mcp/clauselane-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/clauselane-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/clauselane-com/mcp/clauselane-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clauselane-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/clauselane-com/well-known/clauselane-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clauselane-com-security.txt
- group: auth
  href: https://artifacts.apis.io/clauselane-com/well-known/clauselane-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/clauselane-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/clauselane-com/well-known/clauselane-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clauselane-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/clauselane-com/hosts/clauselane-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clauselane-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/clauselane-com/vendors/clauselane-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clauselane-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/clauselane-com/packages/clauselane-com-packages.yml
  title: ''
  type: SDKs
  url: packages/clauselane-com-packages.yml
- group: build
  href: https://artifacts.apis.io/clauselane-com/packages/clauselane-com-packages.yml
  title: ''
  type: Packages
  url: packages/clauselane-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/clauselane-com/security/clauselane-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/clauselane-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/clauselane-com/security/clauselane-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clauselane-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clauselane.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://clauselane.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://clauselane.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clauselane.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clauselane.com/terms/
created: '2026-10-29'
description: Clauselane provides free contract register tools tailored for small US legal teams, offering a contract tracking calculator that projects renewals, notice deadlines, and financial impact within a defined window, alongside a detailed contract lifecycle sheet that records dates, values, obligations, matters, and clauses. The platform includes a paid plan for comprehensive record-keeping and advanced features, positioning itself as a SaaS solution that streamlines contract management and enhances visibility for small legal operations.
image: https://clauselane.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at clauselane.com.
  name: clauselane-com MCP Server
  slug: clauselane-com-mcp-yml
modified: '2026-10-29'
name: clauselane-com
nav: Providers
network: true
overview: 'clauselane-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API and MCP API. Tagged areas include Legal Tech, Contract Management, Software-as-a-Service, Small Business, and US.


  The clauselane-com catalog on APIs.io includes 1 Spectral governance ruleset.


  clauselane-com''s developer surface includes pricing, support, and 23 more developer resources.'
plans:
- name: Clauselane Com Plans Pricing
  plan_count: 2
  slug: clauselane-com-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Clauselane Com Rate Limits
  slug: clauselane-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: clauselane-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: clauselane-com-rules
scopes:
- name: Clauselane Com Scopes
  scope_count: 0
  slug: clauselane-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 29
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 16.0
    discoverability: 75.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/clauselane-com/clauselane-com-2026-11-03T124321.png
security:
- kind: authentication
  name: Clauselane Com Authentication
  slug: clauselane-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Clauselane Com Domain Security
  slug: clauselane-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Clauselane Com Vulnerability Disclosure
  slug: clauselane-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset-search
  slug: clauselane-com-dataset-search-skill
slug: clauselane-com
tags:
- Legal Tech
- Contract Management
- Software-as-a-Service
- Small Business
- US
website: https://clauselane.com/
---
