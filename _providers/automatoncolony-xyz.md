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
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Contract verification and security checks on Base.
  name: Colony
  slug: colony
- description: Large Solidity repository security analysis service.
  name: Scorpio
  slug: scorpio
artifact_total: 15
common:
- group: design
  href: https://artifacts.apis.io/automatoncolony-xyz/rules/automatoncolony-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/automatoncolony-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/automatoncolony-xyz/vocabulary/automatoncolony-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/automatoncolony-xyz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/automatoncolony-xyz/conformance/automatoncolony-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/automatoncolony-xyz-conformance.yml
- group: agent
  href: https://artifacts.apis.io/automatoncolony-xyz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://colony.automatoncolony.xyz/app/en/guides/security-evidence/
- group: design
  href: https://artifacts.apis.io/automatoncolony-xyz/errors/automatoncolony-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/automatoncolony-xyz-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/automatoncolony-xyz/llms/automatoncolony-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/automatoncolony-xyz-llms.txt
- group: other
  href: https://artifacts.apis.io/automatoncolony-xyz/a2a/automatoncolony-xyz-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/automatoncolony-xyz-a2a.yml
- group: build
  href: https://artifacts.apis.io/automatoncolony-xyz/mcp/automatoncolony-xyz-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/automatoncolony-xyz-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/automatoncolony-xyz/mcp/automatoncolony-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/automatoncolony-xyz-mcp.yml
- group: auth
  href: https://artifacts.apis.io/automatoncolony-xyz/well-known/automatoncolony-xyz-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/automatoncolony-xyz-security.txt
- group: auth
  href: https://artifacts.apis.io/automatoncolony-xyz/well-known/automatoncolony-xyz-scorpio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/automatoncolony-xyz-scorpio-security.txt
- group: auth
  href: https://artifacts.apis.io/automatoncolony-xyz/well-known/automatoncolony-xyz-nebula-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/automatoncolony-xyz-nebula-security.txt
- group: auth
  href: https://artifacts.apis.io/automatoncolony-xyz/well-known/automatoncolony-xyz-colony-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/automatoncolony-xyz-colony-security.txt
- group: agent
  href: https://artifacts.apis.io/automatoncolony-xyz/well-known/automatoncolony-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/automatoncolony-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/automatoncolony-xyz/hosts/automatoncolony-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/automatoncolony-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/automatoncolony-xyz/vendors/automatoncolony-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/automatoncolony-xyz-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://automatoncolony.xyz/en/trust/
- group: auth
  href: https://artifacts.apis.io/automatoncolony-xyz/security/automatoncolony-xyz-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/automatoncolony-xyz-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/automatoncolony-xyz/security/automatoncolony-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/automatoncolony-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://automatoncolony.xyz/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://automatoncolony.xyz/en/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://automatoncolony.xyz/en/terms/
- group: operate
  title: ''
  type: Support
  url: https://automatoncolony.xyz/en/contact/
- group: company
  title: ''
  type: About
  url: https://automatoncolony.xyz/en/company/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://automatoncolony.xyz/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://automatoncolony.xyz/openapi.json
  - status: null
    url: https://automatoncolony.xyz/mcp
  - status: null
    url: https://colony.automatoncolony.xyz/openapi.json
  - status: null
    url: https://colony.automatoncolony.xyz/mcp
  - status: null
    url: https://scorpio.automatoncolony.xyz/openapi.json
  - status: 401
    url: https://nebula.automatoncolony.xyz/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Automaton Colony builds tools for governed memory, economic Solidity analysis and contract verification on Base. It offers three products—Nebula for AI memory, Colony for contract verification on Base, and Scorpio for Solidity analysis—providing context, limits and evidence before decisions. The platform emphasizes verifiable decision systems, visible limits, and human control.
image: https://automatoncolony.xyz/assets/og-en.8a97378f64bf.png
layout: provider
mcp_servers:
- description: Remote MCP server at automatoncolony.xyz.
  name: automatoncolony-xyz MCP Server
  slug: automatoncolony-xyz-mcp-yml
modified: '2026-10-29'
name: automatoncolony-xyz
nav: Providers
network: true
overview: 'automatoncolony-xyz publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Governance, Solidity, ContractVerification, and Base.


  The automatoncolony-xyz catalog on APIs.io includes 1 Spectral governance ruleset.


  automatoncolony-xyz''s developer surface includes support and 25 more developer resources.'
plans:
- name: Automatoncolony Xyz Plans Pricing
  plan_count: 0
  slug: automatoncolony-xyz-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Automatoncolony Xyz Rate Limits
  slug: automatoncolony-xyz-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: automatoncolony-xyz API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: automatoncolony-xyz-rules
scopes:
- name: Automatoncolony Xyz Scopes
  scope_count: 0
  slug: automatoncolony-xyz-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 42.8
    catalog_earned_first_party: 0.0
    catalog_gap: 72.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.8
  facets:
    access_clarity: 14.5
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 8.8
    discoverability: 75.0
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 35.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/automatoncolony-xyz/automatoncolony-xyz-2026-11-03T121407.png
security:
- kind: authentication
  name: Automatoncolony Xyz Authentication
  slug: automatoncolony-xyz-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Automatoncolony Xyz Domain Security
  slug: automatoncolony-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Automatoncolony Xyz Vulnerability Disclosure
  slug: automatoncolony-xyz-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 5
skills:
- name: buy-contract-data
  slug: automatoncolony-xyz-buy-contract-data
- name: buy-flash-audit
  slug: automatoncolony-xyz-buy-flash-audit
- name: collect-flash-audit
  slug: automatoncolony-xyz-collect-flash-audit
- name: contract-data-catalog
  slug: automatoncolony-xyz-contract-data-catalog
- name: flash-audit-terms
  slug: automatoncolony-xyz-flash-audit-terms
slug: automatoncolony-xyz
tags:
- Artificial Intelligence
- Governance
- Solidity
- ContractVerification
- Base
website: https://automatoncolony.xyz/
---
