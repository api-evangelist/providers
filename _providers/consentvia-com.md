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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 14.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Consentvia Com Agentic Access
  operation_count: 1
  slug: consentvia-com-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: API providing access to the Consentvia dataset of planning application tools and data.
  name: Consentvia API
  slug: consentvia-api
artifact_total: 10
common:
- group: agent
  href: https://artifacts.apis.io/consentvia-com/agentic-access/consentvia-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/consentvia-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/consentvia-com/plans/consentvia-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/consentvia-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/consentvia-com/rules/consentvia-com-rules.yml
  title: ''
  type: Spectral
  url: rules/consentvia-com-rules.yml
- group: design
  href: https://artifacts.apis.io/consentvia-com/vocabulary/consentvia-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/consentvia-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/consentvia-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://consentvia.com/terms
- group: auth
  href: https://artifacts.apis.io/consentvia-com/authentication/consentvia-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/consentvia-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/consentvia-com/errors/consentvia-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/consentvia-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/consentvia-com/conformance/consentvia-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/consentvia-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/consentvia-com/llms/consentvia-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/consentvia-com-llms.txt
- group: build
  href: https://artifacts.apis.io/consentvia-com/mcp/consentvia-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/consentvia-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/consentvia-com/mcp/consentvia-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/consentvia-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/consentvia-com/well-known/consentvia-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/consentvia-com-security.txt
- group: auth
  href: https://artifacts.apis.io/consentvia-com/well-known/consentvia-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/consentvia-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/consentvia-com/well-known/consentvia-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/consentvia-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/consentvia-com/hosts/consentvia-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/consentvia-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/consentvia-com/vendors/consentvia-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/consentvia-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/consentvia-com/security/consentvia-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/consentvia-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/consentvia-com/security/consentvia-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/consentvia-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://consentvia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.consentvia.com/
- group: operate
  title: ''
  type: Support
  url: https://consentvia.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://consentvia.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://consentvia.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://consentvia.com/privacy/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/consentvia
created: '2026-10-29'
description: Consentvia provides free worksheets and a paid plan to help applicants manage planning applications in England and Wales. Their tools calculate costs, track timelines, and maintain comprehensive records of each application, including authority details, references, fees, dates, conditions, variations, and appeals. The service aims to streamline the planning process for both individuals and professionals.
image: https://consentvia.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at consentvia.com.
  name: consentvia-com MCP Server
  slug: consentvia-com-mcp-yml
modified: '2026-10-29'
name: consentvia-com
nav: Providers
network: true
overview: 'consentvia-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Planning, Worksheets, United Kingdom, and Public Sector.


  The consentvia-com catalog on APIs.io includes 1 Spectral governance ruleset.


  consentvia-com''s developer surface includes authentication, support, pricing, and 23 more developer resources.'
plans:
- name: Consentvia Com Plans Pricing
  plan_count: 2
  slug: consentvia-com-plans-pricing
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: consentvia-com API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: consentvia-com-rules
scopes:
- name: Consentvia Com Scopes
  scope_count: 0
  slug: consentvia-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 23
    catalog_earned: 50.8
    catalog_earned_first_party: 8.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 36.8
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 27.9
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
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 36.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/consentvia-com/consentvia-com-2026-11-03T125144.png
security:
- kind: authentication
  name: Consentvia Com Authentication
  slug: consentvia-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Consentvia Com Domain Security
  slug: consentvia-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Consentvia Com Vulnerability Disclosure
  slug: consentvia-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset-columns
  slug: consentvia-com-dataset-columns
slug: consentvia-com
tags:
- Company
- Planning
- Worksheets
- United Kingdom
- Public Sector
- Tools
website: https://consentvia.com/
---
