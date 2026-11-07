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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 14.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: '7 free HVAC tools, no account: system cost, flat rate pricing, duct sizing, quotes, invoices, checklists and service agreements.'
  name: CoilDesk API
  slug: coildesk-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/coildesk-com/plans/coildesk-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coildesk-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/coildesk-com/vocabulary/coildesk-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coildesk-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/coildesk-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://coildesk.com/terms
- group: auth
  href: https://artifacts.apis.io/coildesk-com/authentication/coildesk-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/coildesk-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/coildesk-com/conformance/coildesk-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coildesk-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coildesk-com/llms/coildesk-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coildesk-com-llms.txt
- group: build
  href: https://artifacts.apis.io/coildesk-com/mcp/coildesk-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/coildesk-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/coildesk-com/mcp/coildesk-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/coildesk-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/coildesk-com/well-known/coildesk-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coildesk-com-security.txt
- group: auth
  href: https://artifacts.apis.io/coildesk-com/well-known/coildesk-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/coildesk-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/coildesk-com/well-known/coildesk-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coildesk-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/coildesk-com/hosts/coildesk-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coildesk-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/coildesk-com/vendors/coildesk-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coildesk-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/coildesk-com/packages/coildesk-com-packages.yml
  title: ''
  type: SDKs
  url: packages/coildesk-com-packages.yml
- group: build
  href: https://artifacts.apis.io/coildesk-com/packages/coildesk-com-packages.yml
  title: ''
  type: Packages
  url: packages/coildesk-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/coildesk-com/security/coildesk-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coildesk-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/coildesk-com/security/coildesk-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coildesk-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coildesk.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://coildesk.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coildesk.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coildesk.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://coildesk.com/support/
created: '2026-10-29'
description: CoilDesk provides free HVAC quoting, invoicing, pricing and maintenance tools for contractors, along with a paid professional plan that adds branding, export capabilities, and advanced features. The platform offers seven free tools—including a maintenance checklist, invoice software, service agreement template, quote builder, duct size calculator, labor rate calculator, and system cost estimator—to streamline HVAC contractor workflows. CoilDesk serves the US market and positions itself as a dedicated work‑order software solution for HVAC contractors.
image: https://coildesk.com/icon-512.png
layout: provider
mcp_servers:
- description: Remote MCP server at coildesk.com.
  name: coildesk-com MCP Server
  slug: coildesk-com-mcp-yml
modified: '2026-10-29'
name: coildesk-com
nav: Providers
network: true
overview: 'coildesk-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include HVAC, Contractor, Software, Tools, and workorder.


  coildesk-com''s developer surface includes authentication, pricing, support, and 20 more developer resources.'
plans:
- name: Coildesk Com Plans Pricing
  plan_count: 2
  slug: coildesk-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Coildesk Com Rate Limits
  slug: coildesk-com-rate-limits
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 46.3
    catalog_earned_first_party: 8.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 36.8
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 27.9
    discoverability: 75.0
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 28.7
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/coildesk-com/coildesk-com-2026-11-03T124809.png
security:
- kind: authentication
  name: Coildesk Com Authentication
  slug: coildesk-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Coildesk Com Domain Security
  slug: coildesk-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coildesk Com Vulnerability Disclosure
  slug: coildesk-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: coildesk-com
tags:
- HVAC
- Contractor
- Software
- Tools
- workorder
- Pricing
- Invoicing
website: https://coildesk.com/
---
