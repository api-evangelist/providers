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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Official Cargado API providing freight marketplace data and integration points.
  name: Cargado API
  slug: cargado-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/cargado/plans/cargado-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cargado-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cargado/llms/cargado-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cargado-llms.txt
- group: other
  href: https://artifacts.apis.io/cargado/a2a/cargado-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/cargado-a2a.yml
- group: agent
  href: https://artifacts.apis.io/cargado/mcp/cargado-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cargado-mcp.yml
- group: auth
  href: https://artifacts.apis.io/cargado/well-known/cargado-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cargado-help-security.txt
- group: agent
  href: https://artifacts.apis.io/cargado/well-known/cargado-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cargado-well-known.yml
- group: other
  href: https://artifacts.apis.io/cargado/hosts/cargado-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cargado-hosts.yml
- group: other
  href: https://artifacts.apis.io/cargado/vendors/cargado-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cargado-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cargado.com/terms
- group: operate
  title: ''
  type: Support
  url: https://help.cargado.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cargado.com/
- group: auth
  title: ''
  type: Security
  url: https://cargado.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cargado.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://cargado.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://cargado.com/media
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cargadoinc
- group: start
  title: ''
  type: GettingStarted
  url: https://cargado.com/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://cargado.com/help-categories/release-notes
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cargado.com/api-reference/concepts/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cargado.com/
- group: auth
  href: https://artifacts.apis.io/cargado/security/cargado-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cargado-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cargado.com
coverage:
  checked: '2026-10-12'
  detail: API documentation is rendered via JavaScript and no machine‑readable OpenAPI spec is available.
  evidence:
  - status: 200
    url: https://docs.cargado.com/api-reference/concepts/overview
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-12'
description: Cargado, Inc. operates a modern freight marketplace and market intelligence platform for Mexico and Canada. It connects brokers with over 2,350 vetted carriers, offering real carrier bids and market rates. The service provides free access for carriers and paid plans for shippers, featuring API access, integrations, and detailed market insights.
image: https://cdn.prod.website-files.com/68f656dee991ae15a5cbb747/6ac72bc2818e7ad15f7a8328_og-home.png
layout: provider
mcp_servers:
- description: Remote MCP server at cargado.main-kill-isr.mintlify.me.
  name: Cargado MCP Server
  slug: cargado-mcp-yml
modified: '2026-10-12'
name: Cargado
nav: Providers
network: true
overview: 'Cargado is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Freight, Marketplace, and Logistics.


  Cargado''s developer surface includes support, pricing, getting-started guide, changelog, API reference, documentation, and 16 more developer resources.'
plans:
- name: Cargado Plans Pricing
  plan_count: 4
  slug: cargado-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.2
    operational_transparency: 23.7
  previous_composite: 32.1
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cargado/cargado-2026-11-03T123345.png
security:
- kind: domain-security
  name: Cargado Domain Security
  slug: cargado-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cargado
tags:
- Company
- Freight
- Marketplace
- Logistics
website: https://cargado.com
---
