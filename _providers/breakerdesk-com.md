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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 23.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: BreakerDesk API provides access to the platform's data and operations.
  name: BreakerDesk API
  slug: breakerdesk-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/breakerdesk-com/rules/breakerdesk-com-rules.yml
  title: ''
  type: Spectral
  url: rules/breakerdesk-com-rules.yml
- group: operate
  href: https://artifacts.apis.io/breakerdesk-com/rate-limits/breakerdesk-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/breakerdesk-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/breakerdesk-com/plans/breakerdesk-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/breakerdesk-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/breakerdesk-com/vocabulary/breakerdesk-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/breakerdesk-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/breakerdesk-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://breakerdesk.com/terms
- group: design
  href: https://artifacts.apis.io/breakerdesk-com/errors/breakerdesk-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/breakerdesk-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/breakerdesk-com/conformance/breakerdesk-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/breakerdesk-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/breakerdesk-com/llms/breakerdesk-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/breakerdesk-com-llms.txt
- group: build
  href: https://artifacts.apis.io/breakerdesk-com/mcp/breakerdesk-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/breakerdesk-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/breakerdesk-com/mcp/breakerdesk-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/breakerdesk-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/breakerdesk-com/well-known/breakerdesk-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/breakerdesk-com-security.txt
- group: auth
  href: https://artifacts.apis.io/breakerdesk-com/well-known/breakerdesk-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/breakerdesk-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/breakerdesk-com/well-known/breakerdesk-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/breakerdesk-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/breakerdesk-com/hosts/breakerdesk-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/breakerdesk-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/breakerdesk-com/vendors/breakerdesk-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/breakerdesk-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/breakerdesk-com/security/breakerdesk-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/breakerdesk-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/breakerdesk-com/security/breakerdesk-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/breakerdesk-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://breakerdesk.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://breakerdesk.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://breakerdesk.com/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://breakerdesk.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://breakerdesk.com/terms/
- group: start
  title: ''
  type: SignUp
  url: https://app.breakerdesk.com/?tab=account
created: '2026-10-29'
description: BreakerDesk provides free electrician calculators and a paid back‑office platform for electrical contractors. The suite includes tools for pricing jobs, estimating costs, generating invoices, creating receipts, and maintaining price books. The free tools run entirely in the browser with no data sent to the server, while the BreakerDesk Pro subscription adds cloud storage, branding, export capabilities, and integration with Stripe, QuickBooks Online and Xero. Operated by Ellul Solutions Ltd in the UK, BreakerDesk aims to streamline the workflow of electricians and small contracting firms.
image: https://breakerdesk.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at breakerdesk.com.
  name: breakerdesk-com MCP Server
  slug: breakerdesk-com-mcp-yml
modified: '2026-10-29'
name: breakerdesk-com
nav: Providers
network: true
overview: 'breakerdesk-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: BreakerDesk API. Tagged areas include Company, Electrician, Software, Tools, and Contractor.


  The breakerdesk-com catalog on APIs.io includes 1 Spectral governance ruleset.


  breakerdesk-com''s developer surface includes pricing, support, signup flow, and 21 more developer resources.'
plans:
- name: Breakerdesk Com Plans Pricing
  plan_count: 2
  slug: breakerdesk-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Breakerdesk Com Rate Limits
  slug: breakerdesk-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: breakerdesk-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: breakerdesk-com-rules
scopes:
- name: Breakerdesk Com Scopes
  scope_count: 0
  slug: breakerdesk-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 52.8
    catalog_earned_first_party: 8.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.8
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 8.8
    discoverability: 75.0
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 37.3
  provenance:
    conformance: derived
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
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/breakerdesk-com/breakerdesk-com-2026-11-03T122526.png
security:
- kind: authentication
  name: Breakerdesk Com Authentication
  slug: breakerdesk-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Breakerdesk Com Domain Security
  slug: breakerdesk-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Breakerdesk Com Vulnerability Disclosure
  slug: breakerdesk-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 7
skills:
- name: dataset-columns
  slug: breakerdesk-com-dataset-columns
- name: dataset-compare
  slug: breakerdesk-com-dataset-compare
- name: dataset-provenance
  slug: breakerdesk-com-dataset-provenance
- name: dataset-row
  slug: breakerdesk-com-dataset-row
- name: dataset-search
  slug: breakerdesk-com-dataset-search
- name: dataset-stats
  slug: breakerdesk-com-dataset-stats
- name: dataset-top
  slug: breakerdesk-com-dataset-top
slug: breakerdesk-com
tags:
- Company
- Electrician
- Software
- Tools
- Contractor
website: https://breakerdesk.com/
---
