---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Machine-readable API for safety standards and citation data
  name: MCP
  slug: mcp
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/cairnsafe-com/plans/cairnsafe-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cairnsafe-com-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://cairnsafe.com/security
- group: design
  href: https://artifacts.apis.io/cairnsafe-com/conformance/cairnsafe-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cairnsafe-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cairnsafe-com/llms/cairnsafe-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cairnsafe-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cairnsafe-com/mcp/cairnsafe-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cairnsafe-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/cairnsafe-com/well-known/cairnsafe-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cairnsafe-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cairnsafe-com/hosts/cairnsafe-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cairnsafe-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cairnsafe-com/vendors/cairnsafe-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cairnsafe-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cairnsafe.com/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://cairnsafe.com/support
- group: auth
  title: ''
  type: Security
  url: https://cairnsafe.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cairnsafe.com/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cairnsafe.com/pricing
- group: start
  title: ''
  type: Login
  url: https://cairnsafe.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://cairnsafe.com/guides
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cairnsafe.com/developers/mcp
- group: auth
  href: https://artifacts.apis.io/cairnsafe-com/security/cairnsafe-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/cairnsafe-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/cairnsafe-com/security/cairnsafe-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cairnsafe-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/cairnsafe-com/security/cairnsafe-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cairnsafe-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cairnsafe.com/
created: '2026-11-03'
description: Cairn provides citation‑grounded answers from the complete federal OSHA compliance record. Built for safety and operations teams, the platform offers searchable, referenced information to help organizations make compliance decisions with confidence. It aggregates the public OSHA record and presents it in an easy‑to‑use interface, ensuring every answer cites its source.
image: https://cairnsafe.com/og-default.png?v=2
layout: provider
mcp_servers:
- description: Remote MCP server at cairnsafe.com.
  name: Cairn MCP Server
  slug: cairnsafe-com-mcp-yml
modified: '2026-11-03'
name: Cairn
nav: Providers
network: true
overview: 'Cairn is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, OSHA, Compliance, Safety, and Research.


  Cairn''s developer surface includes support, pricing, documentation, and 17 more developer resources.'
plans:
- name: Cairnsafe Com Plans Pricing
  plan_count: 3
  slug: cairnsafe-com-plans-pricing
random_paper: 8
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 10
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cairnsafe Com Domain Security
  slug: cairnsafe-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Cairnsafe Com Vulnerability Disclosure
  slug: cairnsafe-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Cairnsafe Com Trust Center
  slug: cairnsafe-com-trust-center
  summary_line: SOC 2, HIPAA, FedRAMP
slug: cairnsafe-com
tags:
- Company
- OSHA
- Compliance
- Safety
- Research
- Platform
website: https://cairnsafe.com/
---
