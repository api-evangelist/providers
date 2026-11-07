---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    agent_skills: derived
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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: QS-grade parametric estimating engine.
  name: CivilQuants API
  slug: civilquants-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/civilquants-com/plans/civilquants-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/civilquants-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/civilquants-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Compliance
  url: https://civilquants.com/legal/security
- group: design
  href: https://artifacts.apis.io/civilquants-com/conformance/civilquants-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/civilquants-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/civilquants-com/llms/civilquants-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/civilquants-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/civilquants-com/mcp/civilquants-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/civilquants-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/civilquants-com/well-known/civilquants-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/civilquants-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/civilquants-com/hosts/civilquants-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/civilquants-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/civilquants-com/vendors/civilquants-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/civilquants-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://civilquants.com/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://civilquants.com/legal/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://civilquants.com/legal/privacy
- group: start
  title: ''
  type: Login
  url: https://civilquants.com/sign-in
- group: auth
  href: https://artifacts.apis.io/civilquants-com/security/civilquants-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/civilquants-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/civilquants-com/security/civilquants-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/civilquants-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/civilquants-com/security/civilquants-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/civilquants-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://civilquants.com/
- group: company
  title: ''
  type: Blog
  url: https://civilquants.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://civilquants.com/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://civilquants.com/agent-docs
created: '2026-11-03'
description: CivilQuants provides cloud‑based Bill of Quantities software for civil engineering, supporting standards such as CESMM4, NRM2, SMM7 and MMHW. Users can generate audit‑traceable quantity take‑offs, material schedules and export results in Excel, DXF or PDF. The platform offers a free 6‑assembly trial and tiered pricing for solo, studio and practice plans, with an MCP server for AI assistant integration.
image: https://civilquants.com/og/civilquants-og.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.civilquants.com.
  name: CivilQuants MCP Server
  slug: civilquants-com-mcp-yml
modified: '2026-11-03'
name: CivilQuants
nav: Providers
network: true
overview: 'CivilQuants is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Civil Engineering, Quantity Surveying, Software, Software-as-a-Service, and Construction.


  CivilQuants'' developer surface includes engineering blog, pricing, documentation, and 17 more developer resources.'
plans:
- name: Civilquants Com Plans Pricing
  plan_count: 5
  slug: civilquants-com-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 26.1
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.7
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
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
  name: Civilquants Com Domain Security
  slug: civilquants-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Civilquants Com Vulnerability Disclosure
  slug: civilquants-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Civilquants Com Trust Center
  slug: civilquants-com-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
skill_count: 1
skills:
- name: assemblies
  slug: civilquants-com-assemblies
slug: civilquants-com
tags:
- Civil Engineering
- Quantity Surveying
- Software
- Software-as-a-Service
- Construction
website: https://civilquants.com/
---
