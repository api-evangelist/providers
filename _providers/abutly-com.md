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
  name: Abutly Com Agentic Access
  operation_count: 18
  slug: abutly-com-agentic-access
  summary_line: 18 operations · 14 acting
api_count: 1
apis:
- baseURL: https://abutly.com
  baseurl_source: declared
  description: dataset
  name: abutly-com Dataset API
  slug: abutly-com-dataset-api
- baseURL: https://abutly.com
  baseurl_source: declared
  description: The mcp API from abutly-com — 1 operation(s) for mcp.
  name: abutly-com MCP API
  slug: abutly-com-mcp-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/abutly-com/agentic-access/abutly-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/abutly-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/abutly-com/rules/abutly-com-rules.yml
  title: ''
  type: Spectral
  url: rules/abutly-com-rules.yml
- group: design
  href: https://artifacts.apis.io/abutly-com/vocabulary/abutly-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/abutly-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/abutly-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://abutly.com/terms
- group: design
  href: https://artifacts.apis.io/abutly-com/errors/abutly-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/abutly-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/abutly-com/conformance/abutly-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/abutly-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/abutly-com/llms/abutly-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/abutly-com-llms.txt
- group: build
  href: https://artifacts.apis.io/abutly-com/mcp/abutly-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/abutly-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/abutly-com/mcp/abutly-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/abutly-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/abutly-com/well-known/abutly-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/abutly-com-security.txt
- group: auth
  href: https://artifacts.apis.io/abutly-com/well-known/abutly-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/abutly-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/abutly-com/well-known/abutly-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/abutly-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/abutly-com/hosts/abutly-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/abutly-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/abutly-com/vendors/abutly-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/abutly-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/abutly-com/authentication/abutly-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/abutly-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/abutly-com/security/abutly-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/abutly-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/abutly-com/security/abutly-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/abutly-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://abutly.com/
- group: operate
  title: ''
  type: Support
  url: https://abutly.com/support
- group: commercial
  title: ''
  type: Pricing
  url: https://abutly.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://abutly.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://abutly.com/privacy
created: '2026-10-29'
description: 'Abutly is software for the building owner, small builder or party wall surveyor in England and Wales working under the Party Wall etc. Act 1996: free worksheets that count the notice dates for a party structure notice, a line of junction notice and an adjacent excavation notice, size the award and the schedule of condition from the rooms being recorded, and work the surveyor cost of the job, all with no account; and Abutly Pro, which keeps each address as a record with its notices, its award, its schedule of condition and the dates they were served. It covers party wall paperwork only. It does not find, list, rate or recommend a surveyor, it gives no legal advice, it does not reproduce the Act, and it does not serve Scotland or Northern Ireland.'
image: https://abutly.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at abutly.com.
  name: abutly-com MCP Server
  slug: abutly-com-mcp-yml
modified: '2026-10-29'
name: abutly-com
nav: Providers
network: true
overview: 'abutly-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Dataset API and MCP API. Tagged areas include Company, Construction, Legal Tech, PartyWall, and United Kingdom.


  The abutly-com catalog on APIs.io includes 1 Spectral governance ruleset.


  abutly-com''s developer surface includes authentication, support, pricing, and 20 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: abutly-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: abutly-com-rules
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 16
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 47.4
    developer_ergonomics: 16.1
    discoverability: 75.0
    operational_transparency: 5.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.0
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
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/abutly-com/abutly-com-2026-11-03T120151.png
security:
- kind: authentication
  name: Abutly Com Authentication
  slug: abutly-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Abutly Com Domain Security
  slug: abutly-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Abutly Com Vulnerability Disclosure
  slug: abutly-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset
  slug: abutly-com-dataset
slug: abutly-com
tags:
- Company
- Construction
- Legal Tech
- PartyWall
- United Kingdom
website: https://abutly.com/
---
