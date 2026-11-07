---
access_model:
  confidence: high
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
  - scopes
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: MCP JSON-RPC endpoint providing tools for Arroway.
  name: Arroway MCP API
  slug: arroway-mcp-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/arroway-app/plans/arroway-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/arroway-app-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.arroway.app/en/trust
- group: auth
  title: ''
  type: Security
  url: https://www.arroway.app/en/support#security
- group: auth
  href: https://artifacts.apis.io/arroway-app/authentication/arroway-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/arroway-app-authentication.yml
- group: auth
  href: https://artifacts.apis.io/arroway-app/scopes/arroway-app-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/arroway-app-scopes.yml
- group: design
  href: https://artifacts.apis.io/arroway-app/conformance/arroway-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/arroway-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/arroway-app/llms/arroway-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/arroway-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/arroway-app/mcp/arroway-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/arroway-app-mcp.yml
- group: auth
  href: https://artifacts.apis.io/arroway-app/well-known/arroway-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arroway-app-security.txt
- group: auth
  href: https://artifacts.apis.io/arroway-app/well-known/arroway-app-arroway-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arroway-app-arroway-security.txt
- group: auth
  href: https://artifacts.apis.io/arroway-app/well-known/arroway-app-allmcps-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/arroway-app-allmcps-security.txt
- group: agent
  href: https://artifacts.apis.io/arroway-app/well-known/arroway-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/arroway-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/arroway-app/hosts/arroway-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arroway-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/arroway-app/vendors/arroway-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arroway-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.arroway.app/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.arroway.app/en/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.arroway.app/en/changelog
- group: auth
  href: https://artifacts.apis.io/arroway-app/security/arroway-app-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/arroway-app-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/arroway-app/security/arroway-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/arroway-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/arroway-app/security/arroway-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arroway-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arroway.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.arroway.app/en
- group: docs
  title: ''
  type: Documentation
  url: https://www.arroway.app/en
- group: start
  title: ''
  type: GettingStarted
  url: https://www.arroway.app/en/install
- group: commercial
  title: ''
  type: Pricing
  url: https://www.arroway.app/en/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.arroway.app/en/answers
- group: start
  title: ''
  type: SignUp
  url: https://www.arroway.app/signin
- group: docs
  title: ''
  type: APIReference
  url: https://www.arroway.app/api/mcp
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/oaleviola
created: '2026-11-01'
description: Arroway orchestrates people and AI agents around the decisions in force. Connected agents can read the current context before work, record what changed and pass unfinished work on. People decide what becomes authoritative. It works for one person with several agents or for a team.
image: https://www.arroway.app/icon.svg
layout: provider
mcp_servers:
- description: Remote MCP server at www.arroway.app requiring OAuth.
  name: Arroway MCP Server
  slug: arroway-app-mcp-yml
modified: '2026-11-01'
name: Arroway
nav: Providers
network: true
overview: 'Arroway is listed with 1 API on the [APIs.io](https://apis.io/) network: MCP API. Tagged areas include Artificial Intelligence, Collaboration, Memory, Teamwork, and Automation.


  Arroway''s developer surface includes authentication, changelog, documentation, getting-started guide, pricing, support, signup flow, and 22 more developer resources.'
plans:
- name: Arroway App Plans Pricing
  plan_count: 2
  slug: arroway-app-plans-pricing
random_paper: 11
scopes:
- name: Arroway App Scopes
  scope_count: 1
  slug: arroway-app-scopes
  summary_line: 1 scope
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 16
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.5
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 24.0
    developer_ergonomics: 33.3
    discoverability: 65.0
    operational_transparency: 15.8
  previous_composite: 50.1
  provenance:
    conformance: first-party
    mcp: first-party
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
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Arroway App Authentication
  slug: arroway-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Arroway App Domain Security
  slug: arroway-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Arroway App Vulnerability Disclosure
  slug: arroway-app-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Arroway App Trust Center
  slug: arroway-app-trust-center
  summary_line: SOC 2, ISO 27001
slug: arroway-app
tags:
- Artificial Intelligence
- Collaboration
- Memory
- Teamwork
- Automation
website: https://arroway.app/
---
