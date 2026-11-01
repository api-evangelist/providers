---
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Hiro MCP provides search and documentation retrieval tools for the Hiro platform.
  name: Hiro MCP
  slug: hiro-mcp
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/hirosecure-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/hirosecure-com/plans/hirosecure-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hirosecure-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/hirosecure-com/llms/hirosecure-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hirosecure-com-llms.txt
- group: other
  href: https://artifacts.apis.io/hirosecure-com/a2a/hirosecure-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hirosecure-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/hirosecure-com/mcp/hirosecure-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/hirosecure-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/hirosecure-com/mcp/hirosecure-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hirosecure-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hirosecure-com/well-known/hirosecure-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hirosecure-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/hirosecure-com/hosts/hirosecure-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hirosecure-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/hirosecure-com/vendors/hirosecure-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hirosecure-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hirosecure.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hirosecure.com/privacy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hirosecure.com/quickstart
- group: auth
  href: https://artifacts.apis.io/hirosecure-com/security/hirosecure-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hirosecure-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hirosecure.com/
- group: docs
  title: ''
  type: Documentation
  url: https://hirosecure.com/platform/autonomy
- group: commercial
  title: ''
  type: Pricing
  url: https://hirosecure.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.hirosecure.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.hirosecure.com
created: '2026-10-30'
description: Hiro provides an agentic security platform that automates remediation of compliance gaps, vulnerability fixes, and access reviews. By integrating with existing security tools, Hiro agents generate pull requests, run tests, and deploy changes, offering SOC 2 implementation and a $500/month trial. The service emphasizes autonomous, audit‑ready evidence and supports enterprise security programs.
image: https://hirosecure.com/hiro-logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.hirosecure.com.
  name: hirosecure-com MCP Server
  slug: hirosecure-com-mcp-yml
modified: '2026-10-30'
name: hirosecure-com
nav: Providers
network: true
overview: 'hirosecure-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Automation, DevOps, Compliance, and AI.


  hirosecure-com''s developer surface includes getting-started guide, documentation, pricing, signup flow, and 14 more developer resources.'
plans:
- name: Hirosecure Com Plans Pricing
  plan_count: 3
  slug: hirosecure-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Hirosecure Com Rate Limits
  slug: hirosecure-com-rate-limits
scopes:
- name: Hirosecure Com Scopes
  scope_count: 0
  slug: hirosecure-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 27.9
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hirosecure Com Authentication
  slug: hirosecure-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hirosecure Com Domain Security
  slug: hirosecure-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hirosecure-com
tags:
- Security
- Automation
- DevOps
- Compliance
- AI
website: https://hirosecure.com/
---
