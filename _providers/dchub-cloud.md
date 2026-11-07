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
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://dchub.cloud
  baseurl_source: declared
  description: Live data layer for data center and energy questions, providing endpoints for power, grid, interconnection queues, fiber, markets and sites.
  name: DC Hub API
  slug: dc-hub-api
- baseURL: https://dchub.cloud
  baseurl_source: declared
  description: 'DC Hub (dchub.cloud) is a live data layer for data center and energy questions: power, grid, interconnection queues, fiber, markets and sites, with an as_of date and a source on every result. MCP serv'
  name: DC Hub — Data Center Intelligence API API
  slug: dc-hub-data-center-intelligence-api-api
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/dchub-cloud/plans/dchub-cloud-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dchub-cloud-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dchub-cloud/data-model/dchub-cloud-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dchub-cloud-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dchub-cloud/changelog/dchub-cloud-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dchub-cloud-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://dchub.cloud/terms
- group: auth
  href: https://artifacts.apis.io/dchub-cloud/authentication/dchub-cloud-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dchub-cloud-authentication.yml
- group: design
  href: https://artifacts.apis.io/dchub-cloud/errors/dchub-cloud-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dchub-cloud-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dchub-cloud/conformance/dchub-cloud-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dchub-cloud-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dchub-cloud/llms/dchub-cloud-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dchub-cloud-llms.txt
- group: other
  href: https://artifacts.apis.io/dchub-cloud/a2a/dchub-cloud-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/dchub-cloud-a2a.yml
- group: build
  href: https://artifacts.apis.io/dchub-cloud/mcp/dchub-cloud-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dchub-cloud-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/dchub-cloud/mcp/dchub-cloud-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dchub-cloud-mcp.yml
- group: auth
  href: https://artifacts.apis.io/dchub-cloud/well-known/dchub-cloud-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dchub-cloud-security.txt
- group: auth
  href: https://artifacts.apis.io/dchub-cloud/well-known/dchub-cloud-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dchub-cloud-api-security.txt
- group: agent
  href: https://artifacts.apis.io/dchub-cloud/well-known/dchub-cloud-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dchub-cloud-well-known.yml
- group: other
  href: https://artifacts.apis.io/dchub-cloud/hosts/dchub-cloud-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dchub-cloud-hosts.yml
- group: other
  href: https://artifacts.apis.io/dchub-cloud/vendors/dchub-cloud-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dchub-cloud-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dchub.cloud/
- group: start
  title: ''
  type: Sandbox
  url: https://dchub.cloud/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dchub.cloud/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://dchub.cloud/news
- group: start
  title: ''
  type: Login
  url: https://dchub.cloud/login
- group: other
  title: ''
  type: Leadership
  url: https://dchub.cloud/team
- group: operate
  title: ''
  type: ChangeLog
  url: https://dchub.cloud/whats-new
- group: start
  title: ''
  type: GettingStarted
  url: https://dchub.cloud/guide
- group: docs
  title: ''
  type: APIReference
  url: https://dchub.cloud/developers
- group: auth
  href: https://artifacts.apis.io/dchub-cloud/security/dchub-cloud-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dchub-cloud-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dchub-cloud/security/dchub-cloud-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dchub-cloud-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dchub.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://dchub.cloud/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dchub.cloud/terms
- group: commercial
  title: ''
  type: Pricing
  url: https://dchub.cloud/pricing
- group: company
  title: ''
  type: About
  url: https://dchub.cloud/about
created: '2026-11-05'
description: DC Hub provides a data‑center power and infrastructure intelligence platform, offering a global facility map across 170+ countries and daily Data Center Power Index (DCPI) scores for 300+ markets, with live grid data and API access to power, fiber and M&A intelligence. It serves developers, analysts and operators seeking real‑time infrastructure insights.
image: https://api.dchub.cloud/api/v1/og/dynamic.png?style=editorial&title=The+neutral+data+layer+for+data-center+infrastructure&subheadline=A+global+data-center+facility+map+%C2%B7+170%2B+countries&used_by=1
layout: provider
mcp_servers:
- description: Remote MCP server at dchub.cloud.
  name: DC Hub MCP Server
  slug: dchub-cloud-mcp-yml
modified: '2026-11-05'
name: DC Hub
nav: Providers
network: true
overview: 'DC Hub publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including — Data Center Intelligence API API, and 1 more. Tagged areas include Data Center, Power, Infrastructure, and Open Data.


  DC Hub''s developer surface includes changelog, authentication, sandbox, getting-started guide, API reference, documentation, pricing, and 25 more developer resources.'
plans:
- name: Dchub Cloud Plans Pricing
  plan_count: 5
  slug: dchub-cloud-plans-pricing
random_paper: 18
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 42.9
    developer_ergonomics: 47.6
    discoverability: 60.0
    operational_transparency: 42.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 25.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dchub Cloud Authentication
  slug: dchub-cloud-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dchub Cloud Domain Security
  slug: dchub-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Dchub Cloud Vulnerability Disclosure
  slug: dchub-cloud-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: dchub-cloud
tags:
- Data Center
- Power
- Infrastructure
- Open Data
website: https://dchub.cloud/
---
