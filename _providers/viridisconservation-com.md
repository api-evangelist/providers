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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Viridisconservation Com Agentic Access
  operation_count: 17
  slug: viridisconservation-com-agentic-access
  summary_line: 17 operations · 16 acting
api_count: 1
apis:
- baseURL: https://mcp.viridisconservation.com
  baseurl_source: declared
  description: The adoption API from viridisconservation-com — 2 operation(s) for adoption.
  name: viridisconservation-com Adoption API
  slug: viridisconservation-com-adoption-api
- baseURL: https://mcp.viridisconservation.com
  baseurl_source: declared
  description: The agents API from viridisconservation-com — 1 operation(s) for agents.
  name: viridisconservation-com Agents API
  slug: viridisconservation-com-agents-api
- baseURL: https://mcp.viridisconservation.com
  baseurl_source: declared
  description: The climate API from viridisconservation-com — 1 operation(s) for climate.
  name: viridisconservation-com Climate API
  slug: viridisconservation-com-climate-api
- baseURL: https://mcp.viridisconservation.com
  baseurl_source: declared
  description: The climate-compliance API from viridisconservation-com — 1 operation(s) for climate-compliance.
  name: viridisconservation-com Climate Compliance API
  slug: viridisconservation-com-climate-compliance-api
- baseURL: https://mcp.viridisconservation.com
  baseurl_source: declared
  description: The conservation API from viridisconservation-com — 1 operation(s) for conservation.
  name: viridisconservation-com Conservation API
  slug: viridisconservation-com-conservation-api
- baseURL: https://mcp.viridisconservation.com
  baseurl_source: declared
  description: The construction API from viridisconservation-com — 1 operation(s) for construction.
  name: viridisconservation-com Construction API
  slug: viridisconservation-com-construction-api
- baseURL: https://mcp.viridisconservation.com
  baseurl_source: declared
  description: The csrd API from viridisconservation-com — 1 operation(s) for csrd.
  name: viridisconservation-com Csrd API
  slug: viridisconservation-com-csrd-api
- baseURL: https://mcp.viridisconservation.com
  baseurl_source: declared
  description: The ghg API from viridisconservation-com — 1 operation(s) for ghg.
  name: viridisconservation-com Ghg API
  slug: viridisconservation-com-ghg-api
- baseURL: https://mcp.viridisconservation.com
  baseurl_source: declared
  description: The routing API from viridisconservation-com — 1 operation(s) for routing.
  name: viridisconservation-com Routing API
  slug: viridisconservation-com-routing-api
- baseURL: https://mcp.viridisconservation.com
  baseurl_source: declared
  description: The security API from viridisconservation-com — 4 operation(s) for security.
  name: viridisconservation-com Security API
  slug: viridisconservation-com-security-api
- baseURL: https://mcp.viridisconservation.com
  baseurl_source: declared
  description: The Security Preflight API from viridisconservation-com — 2 operation(s) for security preflight.
  name: viridisconservation-com Security Preflight API
  slug: viridisconservation-com-security-preflight-api
- baseURL: https://mcp.viridisconservation.com
  baseurl_source: declared
  description: The tax-credit API from viridisconservation-com — 1 operation(s) for tax-credit.
  name: viridisconservation-com Tax Credit API
  slug: viridisconservation-com-tax-credit-api
artifact_total: 32
common:
- group: agent
  href: https://artifacts.apis.io/viridisconservation-com/agentic-access/viridisconservation-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/viridisconservation-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/viridisconservation-com/plans/viridisconservation-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/viridisconservation-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/viridisconservation-com/rules/viridisconservation-com-rules.yml
  title: ''
  type: Spectral
  url: rules/viridisconservation-com-rules.yml
- group: design
  href: https://artifacts.apis.io/viridisconservation-com/vocabulary/viridisconservation-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/viridisconservation-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/viridisconservation-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/viridisconservation-com/conventions/viridisconservation-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/viridisconservation-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/viridisconservation-com/conventions/viridisconservation-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/viridisconservation-com-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://viridisconservation.com/security
- group: design
  href: https://artifacts.apis.io/viridisconservation-com/errors/viridisconservation-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/viridisconservation-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/viridisconservation-com/conformance/viridisconservation-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/viridisconservation-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/viridisconservation-com/llms/viridisconservation-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/viridisconservation-com-llms.txt
- group: other
  href: https://artifacts.apis.io/viridisconservation-com/a2a/viridisconservation-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/viridisconservation-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/viridisconservation-com/mcp/viridisconservation-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/viridisconservation-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/viridisconservation-com/mcp/viridisconservation-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/viridisconservation-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/viridisconservation-com/hosts/viridisconservation-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/viridisconservation-com-hosts.yml
- group: auth
  title: ''
  type: Security
  url: https://viridisconservation.com/security
- group: auth
  href: https://artifacts.apis.io/viridisconservation-com/authentication/viridisconservation-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/viridisconservation-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/viridisconservation-com/security/viridisconservation-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/viridisconservation-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/viridisconservation-com/security/viridisconservation-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/viridisconservation-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://viridisconservation.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://viridisconservation.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://viridisconservation.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://viridisconservation.com/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://viridisconservation.com/project-pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://viridisconservation.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://viridisconservation.com/privacy
- group: start
  title: ''
  type: Login
  url: https://viridisconservation.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/viridisconservation
created: '2026-10-29'
description: Viridis Ecological OS provides an ecological operating system for business, industry and conservation, enabling users to frame decisions, compare supported options and costs, review evidence, and track follow-up. It supports ecological and economic decision-making through a comprehensive platform.
image: https://viridisconservation.com/brand/viridis-mark.svg
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.viridisconservation.com.
  name: viridisconservation-com MCP Server
  slug: viridisconservation-com-mcp-yml
modified: '2026-10-29'
name: viridisconservation-com
nav: Providers
network: true
overview: 'viridisconservation-com publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Adoption API, Agents API, Climate API, and 9 more. Tagged areas include Conservation, Environment, Data, and Software-as-a-Service.


  The viridisconservation-com catalog on APIs.io includes 1 Spectral governance ruleset.


  viridisconservation-com''s developer surface includes authentication, documentation, API reference, pricing, and 24 more developer resources.'
plans:
- name: Viridisconservation Com Plans Pricing
  plan_count: 4
  slug: viridisconservation-com-plans-pricing
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: viridisconservation-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: viridisconservation-com-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 49.8
    catalog_earned_first_party: 12.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 65.8
    contract_governance: 22.0
    contract_quality: 51.0
    developer_ergonomics: 31.4
    discoverability: 66.7
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/viridisconservation-com/viridisconservation-com-2026-11-03T145833.png
security:
- kind: authentication
  name: Viridisconservation Com Authentication
  slug: viridisconservation-com-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Viridisconservation Com Domain Security
  slug: viridisconservation-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Viridisconservation Com Trust Center
  slug: viridisconservation-com-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP
skill_count: 13
skills:
- name: disclosure-compiler-compile-disclosure
  slug: viridisconservation-com-disclosure-compiler-compile_disclosure
- name: ghg-ledger-calculate-inventory
  slug: viridisconservation-com-ghg-ledger-calculate_inventory
- name: hive-solve
  slug: viridisconservation-com-hive-solve
- name: maxwell-defense-rehearse-defense
  slug: viridisconservation-com-maxwell-defense-rehearse_defense
- name: os-decisions-build-decision-report
  slug: viridisconservation-com-os-decisions-build_decision_report
- name: quantity-takeoff-calculate-takeoff
  slug: viridisconservation-com-quantity-takeoff-calculate_takeoff
- name: regulatory-radar-monitor-changes
  slug: viridisconservation-com-regulatory-radar-monitor_changes
- name: regulatory-radar-scan-regulations
  slug: viridisconservation-com-regulatory-radar-scan_regulations
- name: security-preflight-scan-source
  slug: viridisconservation-com-security-preflight-scan_source
- name: security-preflight-screen-injection
  slug: viridisconservation-com-security-preflight-screen_injection
- name: security-preflight-security-preflight
  slug: viridisconservation-com-security-preflight-security_preflight
- name: taxcredit-engine-calculate-tax-credit
  slug: viridisconservation-com-taxcredit-engine-calculate_tax_credit
- name: wu-wei-router-plan-workload
  slug: viridisconservation-com-wu-wei-router-plan_workload
slug: viridisconservation-com
tags:
- Conservation
- Environment
- Data
- Software-as-a-Service
website: https://viridisconservation.com/
---
