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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API Gateway exposing publicly available endpoints for Crusoe Cloud products.
  name: Crusoe Cloud API
  slug: crusoe-cloud-api
artifact_total: 7
asyncapis:
- description: ''
  name: Crusoeenergysystems Webhooks
  slug: crusoeenergysystems-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/crusoeenergysystems/plans/crusoeenergysystems-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/crusoeenergysystems-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/crusoeenergysystems/asyncapi/crusoeenergysystems-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/crusoeenergysystems-webhooks.yml
- group: build
  href: https://artifacts.apis.io/crusoeenergysystems/cli/crusoeenergysystems-cli.yml
  title: ''
  type: CLI
  url: cli/crusoeenergysystems-cli.yml
- group: auth
  href: https://artifacts.apis.io/crusoeenergysystems/security/crusoeenergysystems-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/crusoeenergysystems-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/crusoeenergysystems/conformance/crusoeenergysystems-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crusoeenergysystems-conformance.yml
- group: agent
  href: https://artifacts.apis.io/crusoeenergysystems/llms/crusoeenergysystems-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/crusoeenergysystems-llms.txt
- group: agent
  href: https://artifacts.apis.io/crusoeenergysystems/mcp/crusoeenergysystems-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/crusoeenergysystems-mcp.yml
- group: auth
  href: https://artifacts.apis.io/crusoeenergysystems/well-known/crusoeenergysystems-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crusoeenergysystems-security.txt
- group: auth
  href: https://artifacts.apis.io/crusoeenergysystems/well-known/crusoeenergysystems-crusoe-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crusoeenergysystems-crusoe-security.txt
- group: auth
  href: https://artifacts.apis.io/crusoeenergysystems/well-known/crusoeenergysystems-console-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/crusoeenergysystems-console-security.txt
- group: agent
  href: https://artifacts.apis.io/crusoeenergysystems/well-known/crusoeenergysystems-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/crusoeenergysystems-well-known.yml
- group: other
  href: https://artifacts.apis.io/crusoeenergysystems/hosts/crusoeenergysystems-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crusoeenergysystems-hosts.yml
- group: other
  href: https://artifacts.apis.io/crusoeenergysystems/vendors/crusoeenergysystems-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crusoeenergysystems-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.crusoe.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crusoe.ai/cloud/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.crusoe.ai/resources/newsroom
- group: other
  title: ''
  type: Leadership
  url: https://www.crusoe.ai/about/leadership
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crusoecloud
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.crusoe.ai/developers
- group: company
  title: ''
  type: Blog
  url: https://www.crusoe.ai/resources/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.crusoecloud.com/tags/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.crusoe.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.crusoe.ai/reference/mcp-server/index.html
- group: auth
  href: https://artifacts.apis.io/crusoeenergysystems/security/crusoeenergysystems-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/crusoeenergysystems-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/crusoeenergysystems/security/crusoeenergysystems-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crusoeenergysystems-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crusoe.ai
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.crusoe.ai
  - status: 403
    url: https://equityzen.com/company/crusoeenergysystems
  reason: no-developer-program
  state: none
created: '2026-10-11'
description: Crusoe Energy Systems provides next‑gen AI‑optimized cloud infrastructure powered by clean, stranded energy. The company builds vertically integrated data centers that combine renewable power generation with high‑performance GPU compute, delivering scalable AI workloads with lower cost and carbon footprint. Founded in 2018, Crusoe serves enterprises seeking sustainable, high‑throughput AI compute across its global edge zones.
finops:
- has_sources: true
  method: derived
  name: Crusoeenergysystems Finops
  primary_unit: seat
  service_category: ''
  slug: crusoeenergysystems-finops
  template: false
image: https://cdn.prod.website-files.com/6855c1aa175582ee23e0aa19/68e56afb7fd29e836c07c81b_og-crusoe-home.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.crusoecloud.com.
  name: Crusoeenergysystems MCP Server
  slug: crusoeenergysystems-mcp-yml
modified: '2026-10-11'
name: Crusoeenergysystems
nav: Providers
network: true
overview: 'Crusoeenergysystems is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Cloud, Sustainable, and Data Center.


  The Crusoeenergysystems catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Crusoeenergysystems'' developer surface includes CLI, pricing, engineering blog, getting-started guide, documentation, API reference, and 20 more developer resources.'
plans:
- name: Crusoeenergysystems Plans Pricing
  plan_count: 17
  slug: crusoeenergysystems-plans-pricing
random_paper: 11
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.3
  facets:
    access_clarity: 57.9
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 33.3
    discoverability: 76.7
    operational_transparency: 21.1
  previous_composite: 43.0
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/crusoeenergysystems/crusoeenergysystems-2026-11-03T125709.png
security:
- kind: domain-security
  name: Crusoeenergysystems Domain Security
  slug: crusoeenergysystems-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Crusoeenergysystems Vulnerability Disclosure
  slug: crusoeenergysystems-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: crusoeenergysystems
tags:
- Company
- Artificial Intelligence
- Cloud
- Sustainable
- Data Center
website: https://www.crusoe.ai
---
