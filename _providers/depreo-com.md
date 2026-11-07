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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 12.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Depreo MCP dataset API providing tools for asset management data.
  name: Depreo API
  slug: depreo-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/depreo-com/plans/depreo-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/depreo-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/depreo-com/vocabulary/depreo-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/depreo-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/depreo-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Security
  url: https://depreo.com/terms
- group: design
  href: https://artifacts.apis.io/depreo-com/conformance/depreo-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/depreo-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/depreo-com/llms/depreo-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/depreo-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/depreo-com/mcp/depreo-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/depreo-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/depreo-com/well-known/depreo-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/depreo-com-security.txt
- group: auth
  href: https://artifacts.apis.io/depreo-com/well-known/depreo-com-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/depreo-com-app-security.txt
- group: agent
  href: https://artifacts.apis.io/depreo-com/well-known/depreo-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/depreo-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/depreo-com/hosts/depreo-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/depreo-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/depreo-com/vendors/depreo-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/depreo-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/depreo-com/authentication/depreo-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/depreo-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/depreo-com/security/depreo-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/depreo-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/depreo-com/security/depreo-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/depreo-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://depreo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://depreo.com/tools/
- group: commercial
  title: ''
  type: Pricing
  url: https://depreo.com/pricing/
- group: operate
  title: ''
  type: Support
  url: https://depreo.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://depreo.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://depreo.com/privacy/
- group: operate
  title: ''
  type: Contact
  url: https://depreo.com/contact/
created: '2026-11-05'
description: Depreo provides free asset management worksheets for small organizations, covering depreciation, fixed asset registers, IT inventory cost estimation, and discovery coverage. The platform offers three free tools and a Pro version for deeper insights, with a focus on simplicity and transparency. Contact support at hello@depreo.com for assistance.
image: https://depreo.com/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at depreo.com.
  name: Depreo MCP Server
  slug: depreo-com-mcp-yml
modified: '2026-11-05'
name: Depreo
nav: Providers
network: true
overview: 'Depreo is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Asset Management, Depreciation, IT Inventory, Free Tools, and Small Business.


  Depreo''s developer surface includes authentication, documentation, pricing, support, and 18 more developer resources.'
plans:
- name: Depreo Com Plans Pricing
  plan_count: 2
  slug: depreo-com-plans-pricing
random_paper: 19
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 46.3
    catalog_earned_first_party: 8.0
    catalog_gap: 68.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 65.0
    operational_transparency: 10.5
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Depreo Com Authentication
  slug: depreo-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Depreo Com Domain Security
  slug: depreo-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Depreo Com Vulnerability Disclosure
  slug: depreo-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: dataset-search
  slug: depreo-com-dataset-search
slug: depreo-com
tags:
- Asset Management
- Depreciation
- IT Inventory
- Free Tools
- Small Business
website: https://depreo.com/
---
