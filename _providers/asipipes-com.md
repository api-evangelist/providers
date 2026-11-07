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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Asipipes provides hosted YAML pipelines and a developer API.
  name: Asipipes API
  slug: asipipes-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/asipipes-com/plans/asipipes-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/asipipes-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/asipipes-com/conformance/asipipes-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/asipipes-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/asipipes-com/llms/asipipes-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/asipipes-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/asipipes-com/mcp/asipipes-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/asipipes-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/asipipes-com/well-known/asipipes-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/asipipes-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/asipipes-com/hosts/asipipes-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/asipipes-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/asipipes-com/vendors/asipipes-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/asipipes-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://asipipes.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://asipipes.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://asipipes.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/asipipes-com/security/asipipes-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/asipipes-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://asipipes.com/
- group: docs
  title: ''
  type: Documentation
  url: https://asipipes.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://asipipes.com/how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://asipipes.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://asipipes.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://asipipes.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://asipipes.com/status
created: '2026-11-01'
description: Asipipes provides hosted YAML pipelines that agents can call as MCP tools, offering a library of reusable data processing pipes. Users can sign up with an invite code, create API keys, and integrate pipelines for tasks like SEC filings checks, news digests, and price snapshots, reducing token usage and improving efficiency. The platform emphasizes reproducibility, low token cost, and easy integration for developers.
layout: provider
mcp_servers:
- description: Remote MCP server at asipipes.com requiring an API key.
  name: Asipipes MCP Server
  slug: asipipes-com-mcp-yml
modified: '2026-11-01'
name: Asipipes
nav: Providers
network: true
overview: 'Asipipes is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Pipelines.


  Asipipes'' developer surface includes API reference, documentation, getting-started guide, pricing, and 14 more developer resources.'
plans:
- name: Asipipes Com Plans Pricing
  plan_count: 3
  slug: asipipes-com-plans-pricing
random_paper: 2
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 53.3
    operational_transparency: 7.9
  previous_composite: 31.3
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Asipipes Com Domain Security
  slug: asipipes-com-domain-security
  summary_line: TLSv1.3
slug: asipipes-com
tags:
- Pipelines
website: https://asipipes.com/
---
